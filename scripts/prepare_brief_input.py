from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = ROOT / "config" / "brief_prompt.md"
ITEMS_DIR = ROOT / "data" / "items"
INBOX_DIR = ROOT / "data" / "inbox"


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def prepare(date: str) -> Path:
    items_path = ITEMS_DIR / f"{date}.jsonl"
    if not items_path.exists():
        raise FileNotFoundError(f"items file not found: {items_path.relative_to(ROOT)}")

    prompt = PROMPT_PATH.read_text(encoding="utf-8").strip()
    items = items_path.read_text(encoding="utf-8").strip()

    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    output_path = INBOX_DIR / f"{date}-brief-input.md"
    output_path.write_text(
        "# AI Daily Brief Input - " + date + "\n\n"
        "把这个文件的全部内容交给 Claude Code，让它生成简报，并保存到：\n\n"
        f"```text\ndata/briefs/{date}-ai-daily-brief.md\n```\n\n"
        "## Prompt\n\n"
        f"{prompt}\n\n"
        "## Items JSONL\n\n"
        "```jsonl\n"
        f"{items}\n"
        "```\n",
        encoding="utf-8",
    )
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare a single markdown file for semi-automatic brief generation.")
    parser.add_argument("--date", default=today(), help="Date to prepare, format YYYY-MM-DD.")
    args = parser.parse_args()

    output_path = prepare(args.date)
    print(f"written: {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
