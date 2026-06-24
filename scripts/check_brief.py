from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "data" / "briefs"

REQUIRED_TEXT = [
    "# AI Daily Brief",
    "## 今日最重要的 5 件事",
    "## GitHub Trending 技术趋势观察",
    "## 其他值得关注",
    "## 今日判断",
    "## 明天继续追踪",
]

BANNED_TEXT = [
    "是否值得入库",
    "是否值得写文章",
    "## 可写选题",
    "## 值得入库的原始资料",
    "建议放入：raw / notes / wiki",
]

PLACEHOLDERS = ["____", "TODO", "待补充"]


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def check(date: str) -> list[str]:
    path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
    if not path.exists():
        return [f"missing brief file: {path.relative_to(ROOT)}"]

    text = path.read_text(encoding="utf-8")
    issues: list[str] = []

    for required in REQUIRED_TEXT:
        if required not in text:
            issues.append(f"missing required text: {required}")

    for banned in BANNED_TEXT:
        if banned in text:
            issues.append(f"contains banned text: {banned}")

    for placeholder in PLACEHOLDERS:
        if placeholder in text:
            issues.append(f"contains placeholder: {placeholder}")

    if text.count("### ") < 3:
        issues.append("has fewer than 3 highlighted items")

    if "http" not in text:
        issues.append("missing source links")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Check generated brief quality.")
    parser.add_argument("--date", default=today(), help="Date to check, format YYYY-MM-DD.")
    args = parser.parse_args()

    issues = check(args.date)
    if not issues:
        print("brief quality check: passed")
        return

    print("brief quality check: failed")
    for issue in issues:
        print(f"- {issue}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
