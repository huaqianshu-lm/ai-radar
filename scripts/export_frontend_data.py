#!/usr/bin/env python3
"""Translate daily items and export the stable frontend JSON contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import httpx


ROOT = Path(__file__).resolve().parents[1]
ITEMS_DIR = ROOT / "data" / "items"
FRONTEND_DIR = ROOT / "data" / "frontend"
TRANSLATIONS_DIR = ROOT / "data" / "translations"
ENV_LOCAL_PATH = ROOT / ".env.local"
GEMINI_MODEL = "gemini-3.5-flash-lite"
GEMINI_API_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent"
)
TRACKING_PARAMS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "ref",
    "source",
}


def valid_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from error
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate items and export frontend JSON."
    )
    parser.add_argument(
        "--date",
        type=valid_date,
        default=datetime.now(timezone.utc).date().isoformat(),
        help="Items date in YYYY-MM-DD format (default: today in UTC).",
    )
    return parser.parse_args()


def env_local_values() -> dict[str, str]:
    if not ENV_LOCAL_PATH.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in ENV_LOCAL_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[key] = value
    return values


def gemini_api_key() -> str:
    return os.environ.get("GEMINI_API_KEY") or env_local_values().get(
        "GEMINI_API_KEY", ""
    )


def iso_utc(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_url(value: str) -> str:
    parts = urlsplit(value.strip())
    query = [
        (key, item_value)
        for key, item_value in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMS
    ]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), path, urlencode(query), "")
    )


def source_item(item: dict[str, Any], line_number: int) -> dict[str, str]:
    url = str(item.get("canonical_url") or item.get("url") or "").strip()
    title = str(item.get("title") or "").strip()
    summary = str(item.get("display_summary") or item.get("summary") or "").strip()
    source = str(item.get("source") or "").strip()
    source_type = str(item.get("source_type") or "").strip()
    published_at = str(item.get("published_at") or "").strip()
    fetched_at = str(item.get("fetched_at") or "").strip()

    required = {
        "title": title,
        "summary": summary,
        "source": source,
        "source_type": source_type,
        "url": url,
        "display_time": published_at or fetched_at,
    }
    missing = [name for name, value in required.items() if not value]
    if missing:
        raise ValueError(
            f"Item line {line_number} is missing fields: {', '.join(missing)}"
        )

    return {
        "id": hashlib.sha256(url.encode("utf-8")).hexdigest(),
        "title": title,
        "summary": summary,
        "source": source,
        "source_type": source_type,
        "display_time": iso_utc(published_at or fetched_at),
        "time_type": "published" if published_at else "fetched",
        "url": url,
    }


def content_hash(item: dict[str, str]) -> str:
    source = json.dumps(
        {"title": item["title"], "summary": item["summary"]},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def cache_path(item: dict[str, str]) -> Path:
    cache_key = f"{normalize_url(item['url'])}\0{content_hash(item)}"
    return TRANSLATIONS_DIR / f"{hashlib.sha256(cache_key.encode('utf-8')).hexdigest()}.json"


def has_chinese(value: str) -> bool:
    return any("\u4e00" <= character <= "\u9fff" for character in value)


def validate_translation(value: Any, expected_id: str) -> dict[str, str]:
    if not isinstance(value, dict) or set(value) != {"id", "title", "summary"}:
        raise ValueError(f"Invalid translation structure for item {expected_id}")
    if value.get("id") != expected_id:
        raise ValueError(f"Translation ID mismatch for item {expected_id}")

    title = value.get("title")
    summary = value.get("summary")
    if not isinstance(summary, str) or not summary.strip() or not has_chinese(summary):
        raise ValueError(f"Translated summary is not Chinese for item {expected_id}")
    if not isinstance(title, str) or not title.strip():
        raise ValueError(f"Translated title is empty for item {expected_id}")

    title = title.strip()
    summary = summary.strip()
    if not has_chinese(title):
        title = f"{title}：{summary.split('。', 1)[0].rstrip('！!?？')}"
    return {"title": title.strip(), "summary": summary.strip()}


def read_cached_translation(item: dict[str, str]) -> dict[str, str] | None:
    path = cache_path(item)
    if not path.is_file():
        return None
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
        if cached.get("normalized_url") != normalize_url(item["url"]):
            return None
        if cached.get("content_hash") != content_hash(item):
            return None
        return validate_translation(cached.get("translation"), item["id"])
    except (json.JSONDecodeError, OSError, ValueError, AttributeError):
        return None


def translate_items(items: list[dict[str, str]], api_key: str) -> dict[str, dict[str, str]]:
    prompt_items = [
        {"id": item["id"], "title": item["title"], "summary": item["summary"]}
        for item in items
    ]
    prompt = (
        "将以下 AI 新闻的 title 和 summary 翻译、整理为简洁准确的中文。"
        "产品名、模型名、机构名和必要技术缩写保留原文；不得补充输入中没有的事实；"
        "来源信息不足时只翻译已有内容，不根据标题扩写。每个 title 和 summary 都必须包含中文；"
        "如果原始 title 只有产品名、仓库名或其他专有名称，保留该名称并根据 summary 中已有信息补充简短中文说明。\n\n"
        + json.dumps(prompt_items, ensure_ascii=False)
    )
    item_schema = {
        "type": "OBJECT",
        "properties": {
            "id": {"type": "STRING"},
            "title": {"type": "STRING"},
            "summary": {"type": "STRING"},
        },
        "required": ["id", "title", "summary"],
    }
    request_body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": {"type": "ARRAY", "items": item_schema},
        },
    }

    try:
        response = httpx.post(
            GEMINI_API_URL,
            headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
            json=request_body,
            timeout=90,
        )
        response.raise_for_status()
        response_body = response.json()
        response_text = response_body["candidates"][0]["content"]["parts"][0]["text"]
        translated_values = json.loads(response_text)
    except (httpx.HTTPError, json.JSONDecodeError, KeyError, IndexError, TypeError) as error:
        raise RuntimeError(f"Gemini translation request failed: {type(error).__name__}") from error

    if not isinstance(translated_values, list) or len(translated_values) != len(items):
        raise ValueError("Gemini returned an incomplete translation batch")

    translations: dict[str, dict[str, str]] = {}
    expected_ids = {item["id"] for item in items}
    for value in translated_values:
        item_id = value.get("id") if isinstance(value, dict) else ""
        if item_id not in expected_ids or item_id in translations:
            raise ValueError("Gemini returned an unknown or duplicate translation ID")
        translations[item_id] = validate_translation(value, item_id)
    if set(translations) != expected_ids:
        raise ValueError("Gemini returned an incomplete translation batch")
    return translations


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as temporary_file:
        temporary_file.write(content)
        temporary_path = Path(temporary_file.name)
    temporary_path.replace(path)


def write_cache(item: dict[str, str], translation: dict[str, str]) -> None:
    payload = {
        "normalized_url": normalize_url(item["url"]),
        "content_hash": content_hash(item),
        "model": GEMINI_MODEL,
        "translation": {
            "id": item["id"],
            "title": translation["title"],
            "summary": translation["summary"],
        },
    }
    atomic_write(
        cache_path(item), json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )


def translated_frontend_items(items: list[dict[str, str]]) -> tuple[list[dict[str, str]], int]:
    translations: dict[str, dict[str, str]] = {}
    missing: list[dict[str, str]] = []
    for item in items:
        cached = read_cached_translation(item)
        if cached:
            translations[item["id"]] = cached
        else:
            missing.append(item)

    if missing:
        api_key = gemini_api_key()
        if not api_key:
            raise RuntimeError(
                f"GEMINI_API_KEY is required to translate {len(missing)} uncached items"
            )
        new_translations = translate_items(missing, api_key)
        for item in missing:
            write_cache(item, new_translations[item["id"]])
        translations.update(new_translations)

    translated_items = []
    for item in items:
        translated = dict(item)
        translated.update(translations[item["id"]])
        translated_items.append(translated)
    return translated_items, len(missing)


def export(date: str) -> tuple[Path, Path, int]:
    source = ITEMS_DIR / f"{date}.jsonl"
    if not source.is_file():
        raise FileNotFoundError(f"Items file not found: {source}")

    items = []
    for line_number, line in enumerate(
        source.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if line.strip():
            items.append(source_item(json.loads(line), line_number))

    items, translated_count = translated_frontend_items(items)
    payload = {"date": date, "items": items}
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    archive_path = FRONTEND_DIR / f"{date}.json"
    latest_path = FRONTEND_DIR / "latest.json"
    atomic_write(archive_path, serialized)
    atomic_write(latest_path, serialized)
    print(
        f"Frontend translations: {translated_count} Gemini, "
        f"{len(items) - translated_count} cache"
    )
    return archive_path, latest_path, len(items)


def main() -> None:
    args = parse_args()
    archive_path, latest_path, count = export(args.date)
    print(
        f"Frontend data exported: {count} items -> "
        f"{archive_path.relative_to(ROOT)}, {latest_path.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
