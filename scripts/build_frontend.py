#!/usr/bin/env python3
"""Build the static AI Radar frontend without external dependencies."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "dist"
REQUIRED_ITEM_FIELDS = {
    "id",
    "title",
    "summary",
    "source",
    "source_type",
    "display_time",
    "time_type",
    "url",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the static frontend")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output directory (default: dist)",
    )
    return parser.parse_args()


def validate_frontend_data(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("date"), str):
        raise ValueError(f"Invalid frontend date in {path}")
    if not isinstance(payload.get("items"), list):
        raise ValueError(f"Invalid frontend items in {path}")

    for index, item in enumerate(payload["items"], start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Item {index} is not an object in {path}")
        missing = REQUIRED_ITEM_FIELDS - item.keys()
        if missing:
            raise ValueError(
                f"Item {index} is missing fields in {path}: {', '.join(sorted(missing))}"
            )


def main() -> None:
    args = parse_args()
    html_source = PROJECT_ROOT / "web" / "index.html"
    data_source = PROJECT_ROOT / "data" / "frontend" / "latest.json"

    if not html_source.is_file():
        raise FileNotFoundError(f"Frontend entry not found: {html_source}")
    if not data_source.is_file():
        raise FileNotFoundError(f"Frontend data not found: {data_source}")

    validate_frontend_data(data_source)

    output = args.output.resolve()
    data_output = output / "data"
    data_output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(html_source, output / "index.html")
    shutil.copy2(data_source, data_output / "latest.json")

    print(f"Frontend built: {output}")


if __name__ == "__main__":
    main()
