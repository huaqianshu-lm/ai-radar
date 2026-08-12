#!/usr/bin/env python3
"""Export daily items JSONL to the stable frontend JSON contract."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ITEMS_DIR = ROOT / "data" / "items"
FRONTEND_DIR = ROOT / "data" / "frontend"


def valid_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from error
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export items JSONL for the static frontend without translation."
    )
    parser.add_argument(
        "--date",
        type=valid_date,
        default=datetime.now(timezone.utc).date().isoformat(),
        help="Items date in YYYY-MM-DD format (default: today in UTC).",
    )
    return parser.parse_args()


def iso_utc(value: str) -> str:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def frontend_item(item: dict[str, Any], line_number: int) -> dict[str, str]:
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


def export(date: str) -> tuple[Path, Path, int]:
    source = ITEMS_DIR / f"{date}.jsonl"
    if not source.is_file():
        raise FileNotFoundError(f"Items file not found: {source}")

    items = []
    for line_number, line in enumerate(
        source.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if line.strip():
            items.append(frontend_item(json.loads(line), line_number))

    payload = {"date": date, "items": items}
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    FRONTEND_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = FRONTEND_DIR / f"{date}.json"
    latest_path = FRONTEND_DIR / "latest.json"
    archive_path.write_text(serialized, encoding="utf-8")
    latest_path.write_text(serialized, encoding="utf-8")
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
