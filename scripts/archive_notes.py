from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "data" / "briefs"
ENV_LOCAL_PATH = ROOT / ".env.local"
DEFAULT_MEMORA_ROOT = ROOT.parent / "memora"
ARCHIVE_SECTION = "## 知识库入库候选"


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


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
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if key:
            values[key] = value
    return values


def setting(name: str, default: str = "") -> str:
    return os.environ.get(name) or env_local_values().get(name, default)


def section(text: str, heading: str) -> str:
    match = re.search(rf"(?m)^{re.escape(heading)}\s*$", text)
    if not match:
        return ""
    remainder = text[match.end() :]
    next_heading = re.search(r"(?m)^## ", remainder)
    return (remainder[: next_heading.start()] if next_heading else remainder).strip()


def numbered_items(text: str) -> list[str]:
    matches = list(re.finditer(r"(?m)^### \d+\. ", text))
    return [
        text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)].strip()
        for index, match in enumerate(matches)
    ]


def field_value(text: str, field: str) -> str:
    patterns = [
        rf"(?m)^> \*\*{re.escape(field)}：\*\*\s*(.+)$",
        rf"(?m)^- \*\*{re.escape(field)}：\*\*\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()

    heading = re.search(rf"(?m)^\*\*{re.escape(field)}\*\*\s*$", text)
    if not heading:
        return ""
    lines: list[str] = []
    for line in text[heading.end() :].splitlines():
        stripped = line.strip()
        if not lines and not stripped:
            continue
        if re.match(r"^(\*\*[^*]+\*\*|> |### |## )", stripped):
            break
        lines.append(line)
    return "\n".join(lines).strip()


def title(item: str) -> str:
    match = re.search(r"(?m)^### \d+\. (.+)$", item)
    return match.group(1).strip() if match else "未命名知识卡片"


def parse_candidates(brief: str) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    for item in numbered_items(section(brief, ARCHIVE_SECTION)):
        candidate = {
            "title": title(item),
            "source": field_value(item, "来源"),
            "url": field_value(item, "原文链接"),
            "recommendation": field_value(item, "入库建议"),
            "type": field_value(item, "入库类型"),
            "topic": field_value(item, "关联主题"),
            "reason": field_value(item, "入库理由"),
            "connection": field_value(item, "与现有知识或项目的连接"),
            "understanding": field_value(item, "我的理解"),
            "implication": field_value(item, "对我的启发"),
            "summary": field_value(item, "摘要"),
        }
        if (
            candidate["url"]
            and candidate["recommendation"]
            and candidate["understanding"]
            and candidate["implication"]
        ):
            candidates.append(candidate)
    return candidates


def archive_brief(date: str, overwrite: bool = False) -> list[Path]:
    brief_path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
    if not brief_path.exists():
        raise FileNotFoundError(f"brief not found: {brief_path.relative_to(ROOT)}")
    candidates = parse_candidates(brief_path.read_text(encoding="utf-8"))
    direct_candidates = [candidate for candidate in candidates if candidate["recommendation"] == "直接入库"]
    if not direct_candidates:
        print("archived: 0")
        return []
    return archive_candidates(date, direct_candidates, overwrite=overwrite)

def slugify(value: str) -> str:
    value = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", value, flags=re.UNICODE).strip("-")
    return value[:80] or "untitled-knowledge-card"


def yaml_value(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def normalized_url(value: str) -> str:
    return value.split("#", 1)[0].rstrip("/")


def find_raw_path(date: str, source_url: str) -> Path | None:
    target_url = normalized_url(source_url)
    items_path = ROOT / "data" / "items" / f"{date}.jsonl"
    if not items_path.exists():
        return None
    for line in items_path.read_text(encoding="utf-8").splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        item_urls = {normalized_url(str(item.get(key, ""))) for key in ("url", "source_url", "canonical_url")}
        if target_url not in item_urls:
            continue
        raw_value = str(item.get("raw_path", "")).strip()
        if not raw_value:
            return None
        raw_path = ROOT / raw_value
        return raw_path if raw_path.exists() else None
    return None


def copy_raw_to_memora(date: str, source_url: str, title_value: str, memora_root: Path) -> Path | None:
    source_path = find_raw_path(date, source_url)
    if source_path is None:
        return None
    raw_dir = memora_root / "knowledge" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    target_path = raw_dir / f"{date}-ai-radar-{slugify(title_value)}.md"
    if not target_path.exists():
        shutil.copyfile(source_path, target_path)
    return target_path


def tags_for(candidate: dict[str, str]) -> list[str]:
    values = [candidate["topic"], "AI Radar"]
    tags: list[str] = []
    for value in values:
        for tag in re.split(r"[/、，,]+", value):
            tag = tag.strip()
            if tag and tag not in tags:
                tags.append(tag)
    return tags[:5]


def run_memora_finalize(note_path: Path, memora_root: Path) -> None:
    finalize = memora_root / "tools" / "finalize_ingest.py"
    if not finalize.exists():
        raise RuntimeError(f"Memora finalize tool not found: {finalize}")
    result = subprocess.run(
        [sys.executable, str(finalize), str(note_path)],
        cwd=memora_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0 and "## 自动完成" not in result.stdout:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Memora finalize failed")


def refresh_memora_overview(memora_root: Path) -> None:
    overview = memora_root / "tools" / "generate_overview.py"
    result = subprocess.run(
        [sys.executable, str(overview)],
        cwd=memora_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Memora overview generation failed")


def archive_candidates(date: str, candidates: list[dict[str, str]], overwrite: bool = False) -> list[Path]:
    memora_value = setting("MEMORA_ROOT", str(DEFAULT_MEMORA_ROOT))
    memora_root = Path(memora_value).expanduser()
    if not (memora_root / "knowledge").exists():
        raise RuntimeError(f"Memora knowledge directory not found: {memora_root / 'knowledge'}")

    written: list[Path] = []
    skipped: list[str] = []
    overview_needed = False
    for candidate in candidates:
        if candidate["recommendation"] != "直接入库":
            continue
        item_title = candidate["title"]
        source_url = candidate["url"]
        raw_path = copy_raw_to_memora(date, source_url, item_title, memora_root)
        if raw_path is None:
            skipped.append(f"{item_title}：未找到完整 raw 原文")
            continue
        notes_dir = memora_root / "knowledge" / "notes"
        notes_dir.mkdir(parents=True, exist_ok=True)
        output_path = notes_dir / f"{date}-{slugify(item_title)}.md"
        if output_path.exists() and not overwrite:
            skipped.append(f"{item_title}：目标文件已存在")
            continue

        tags = tags_for(candidate)
        content = "\n".join(
            [
                "---",
                f"title: {yaml_value(item_title)}",
                f"source: {yaml_value(source_url)}",
                f"date: {date}",
                "tags:",
                *[f"  - {yaml_value(tag)}" for tag in tags],
                "related: []",
                f"raw: {raw_path.relative_to(memora_root).as_posix()}",
                "origin: AI Radar",
                "---",
                "",
                f"# {item_title}",
                "",
                "## 摘要",
                "",
                candidate["summary"] or candidate["understanding"],
                "",
                "## 要点",
                "",
                f"- {candidate['reason']}",
                f"- {candidate['connection']}",
                "",
                "## 我的判断",
                "",
                candidate["understanding"],
                "",
                "## 可用于",
                "",
                candidate["implication"],
                "",
                "## 后续问题",
                "",
                "- 后续需要结合 Memora 中的相关笔记，判断是否更新对应 Wiki。",
                "",
            ]
        )
        output_path.write_text(content, encoding="utf-8")
        try:
            run_memora_finalize(output_path, memora_root)
            overview_needed = True
            written.append(output_path)
        except Exception:
            output_path.unlink(missing_ok=True)
            raise

    if overview_needed:
        refresh_memora_overview(memora_root)

    print(f"archived: {len(written)}")
    for output_path in written:
        print(f"- {output_path}")
    for message in skipped:
        print(f"skipped: {message}")
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive AI-confirmed knowledge-card candidates automatically.")
    parser.add_argument("--date", default=today(), help="Date to process, format YYYY-MM-DD.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--prepare", action="store_true", help="Archive direct-insert candidates from the daily brief.")
    mode.add_argument("--apply", action="store_true", help="Archive direct-insert candidates from the daily brief.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing Memora note.")
    args = parser.parse_args()

    archive_brief(args.date, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
