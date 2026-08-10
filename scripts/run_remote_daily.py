from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

from run_daily import run
from sync_remote_raw import sync_remote_raw

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
ITEMS_DIR = ROOT / "data" / "items"
INBOX_DIR = ROOT / "data" / "inbox"
BRIEFS_DIR = ROOT / "data" / "briefs"
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def valid_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from error
    return value


def raw_dates(date_filter: str | None, generate_brief: bool) -> list[str]:
    dates: set[str] = set()
    if not RAW_DIR.exists():
        return []

    for date_dir in RAW_DIR.iterdir():
        if not date_dir.is_dir() or not DATE_PATTERN.fullmatch(date_dir.name):
            continue
        if date_filter and date_dir.name != date_filter:
            continue
        if not any(date_dir.rglob("*.md")):
            continue

        date = date_dir.name
        items_path = ITEMS_DIR / f"{date}.jsonl"
        brief_input_path = INBOX_DIR / f"{date}-brief-input.md"
        brief_path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
        if not items_path.exists() or not brief_input_path.exists():
            dates.add(date)
        elif generate_brief and not brief_path.exists():
            dates.add(date)
    return sorted(dates)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync remote raw news, then run the local AI Radar pipeline."
    )
    parser.add_argument("--remote", default="origin", help="Git remote name.")
    parser.add_argument("--branch", default="remote-news", help="Remote raw branch name.")
    parser.add_argument("--date", type=valid_date, default=None, help="Only process one date, format YYYY-MM-DD.")
    parser.add_argument("--no-brief", action="store_true", help="Do not call Claude Code CLI.")
    parser.add_argument("--overwrite-brief", action="store_true", help="Overwrite an existing brief.")
    parser.add_argument("--no-obsidian", action="store_true", help="Do not export the brief to Obsidian.")
    parser.add_argument("--overwrite-obsidian", action="store_true", help="Overwrite an existing Obsidian brief.")
    args = parser.parse_args()

    generate_brief = not args.no_brief
    sync_result = sync_remote_raw(remote=args.remote, branch=args.branch, date_filter=args.date)
    dates = set(raw_dates(args.date, generate_brief=generate_brief))
    dates.update(sync_result.dates)
    dates = sorted(dates)
    if not dates:
        print("no pending remote raw dates to process")
        return

    for date in dates:
        print(f"processing remote raw locally: {date}")
        run(
            limit=10,
            generate_brief=generate_brief,
            overwrite_brief=args.overwrite_brief,
            export_obsidian=not args.no_obsidian,
            overwrite_obsidian=args.overwrite_obsidian,
            run_date=date,
            fetch=False,
        )


if __name__ == "__main__":
    main()
