from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
ITEMS_DIR = ROOT / "data" / "items"
DEFAULT_DEDUPE_DAYS = 14
TRACKING_QUERY_PARAMS = {"fbclid", "gclid", "ref"}
CORE_AI_COMPANY_SOURCES = {
    "Anthropic News",
    "OpenAI News",
    "Google DeepMind Blog",
    "Meta AI Blog",
    "Mistral AI News",
}


@dataclass(frozen=True)
class NormalizeResult:
    path: Path
    raw_count: int
    written_count: int
    skipped_current_duplicates: int
    skipped_history_duplicates: int


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text

    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return {}, text

    frontmatter = text[4:end]
    body = text[end + len(marker) :]
    data = yaml.safe_load(frontmatter) or {}
    return data, body.strip()


def compact_summary(body: str, max_length: int = 500) -> str:
    text = re.sub(r"\s+", " ", body).strip()
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.lower()).strip()


def normalize_url(url: str) -> str:
    if not url:
        return ""

    parts = urlsplit(url.strip())
    query = urlencode(
        [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_") and key.lower() not in TRACKING_QUERY_PARAMS
        ],
        doseq=True,
    )
    path = parts.path.rstrip("/") or parts.path
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def historical_item_keys(date: str, days: int = DEFAULT_DEDUPE_DAYS) -> tuple[set[str], set[str]]:
    target_date = datetime.fromisoformat(date).date()
    urls: set[str] = set()
    titles: set[str] = set()

    for offset in range(1, days + 1):
        item_path = ITEMS_DIR / f"{target_date - timedelta(days=offset)}.jsonl"
        if not item_path.exists():
            continue
        for line in item_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            url_key = normalize_url(str(item.get("url") or ""))
            title_key = normalize_title(str(item.get("title") or ""))
            if url_key:
                urls.add(url_key)
            if title_key:
                titles.add(title_key)

    return urls, titles


def sort_key(item: dict[str, Any]) -> tuple[int, str, str]:
    return (
        1 if item.get("is_list_page") else 0,
        str(item.get("published_at") or item.get("fetched_at") or ""),
        str(item.get("title") or ""),
    )


def credibility_score(source_type: str) -> int:
    if source_type == "official":
        return 5
    if source_type == "developer":
        return 4
    if source_type == "aggregator":
        return 3
    return 0


def raw_to_item(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    source_type = str(meta.get("source_type") or "")
    is_list_page = meta.get("is_list_page") in (True, "true", "True")

    return {
        "title": meta.get("title") or "Untitled",
        "url": meta.get("url") or "",
        "source": meta.get("source") or "",
        "source_type": source_type,
        "published_at": meta.get("published_at") or "",
        "fetched_at": meta.get("fetched_at") or "",
        "summary": compact_summary(body),
        "category": "pending_manual_review",
        "importance_score": 0,
        "relevance_score": 0,
        "credibility_score": credibility_score(source_type),
        "should_archive": False,
        "should_write": False,
        "reason": "list_page_low_priority" if is_list_page else "pending_manual_review",
        "raw_path": str(path.relative_to(ROOT)),
        "is_list_page": is_list_page,
    }


def normalize(date: str) -> NormalizeResult:
    raw_date_dir = RAW_DIR / date
    ITEMS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = ITEMS_DIR / f"{date}.jsonl"

    raw_files = sorted(raw_date_dir.glob("**/*.md")) if raw_date_dir.exists() else []
    history_urls, history_titles = historical_item_keys(date)
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    items: list[dict[str, Any]] = []
    skipped_current_duplicates = 0
    skipped_history_duplicates = 0

    for path in raw_files:
        item = raw_to_item(path)
        url_key = normalize_url(str(item.get("url") or ""))
        title_key = normalize_title(str(item.get("title") or ""))
        if (url_key and url_key in seen_urls) or (title_key and title_key in seen_titles):
            skipped_current_duplicates += 1
            continue
        if (url_key and url_key in history_urls) or (title_key and title_key in history_titles):
            if item.get("source") not in CORE_AI_COMPANY_SOURCES:
                skipped_history_duplicates += 1
                continue
        if url_key:
            seen_urls.add(url_key)
        if title_key:
            seen_titles.add(title_key)
        items.append(item)

    items.sort(key=sort_key)

    with output_path.open("w", encoding="utf-8") as file:
        for item in items:
            file.write(json.dumps(item, ensure_ascii=False) + "\n")

    return NormalizeResult(
        path=output_path,
        raw_count=len(raw_files),
        written_count=len(items),
        skipped_current_duplicates=skipped_current_duplicates,
        skipped_history_duplicates=skipped_history_duplicates,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize raw markdown files into items JSONL.")
    parser.add_argument("--date", default=today(), help="Date to normalize, format YYYY-MM-DD.")
    args = parser.parse_args()

    result = normalize(args.date)
    print(f"written: {result.path.relative_to(ROOT)}")
    print(f"items written: {result.written_count}")
    print(
        "duplicates skipped: "
        f"{result.skipped_current_duplicates} current, {result.skipped_history_duplicates} history"
    )


if __name__ == "__main__":
    main()
