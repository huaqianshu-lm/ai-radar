from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "data" / "briefs"

REQUIRED_TEXT = [
    "# AI Daily Brief",
    "## 今日最重要的 5 件事",
    "## 次级关注 5 条",
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
TOP_SECTION = "## 今日最重要的 5 件事"
SECONDARY_SECTION = "## 次级关注 5 条"
GITHUB_SECTION = "## GitHub Trending 技术趋势观察"
SUMMARY_MIN_CHARS = 80
SUMMARY_MAX_CHARS = 500


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def get_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(heading)}(?:（.*?）)?\s*$")
    match = pattern.search(text)
    if not match:
        return ""
    after_heading = text[match.end() :]
    next_heading = re.search(r"\n## ", after_heading)
    if not next_heading:
        return after_heading.strip()
    return after_heading[: next_heading.start()].strip()


def get_items(section: str) -> list[str]:
    matches = list(re.finditer(r"(?m)^### \d+\. ", section))
    items: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        items.append(section[start:end].strip())
    return items


def field_value(item: str, field: str) -> str:
    list_match = re.search(rf"(?m)^- {re.escape(field)}：(.+)$", item)
    if list_match:
        return list_match.group(1).strip()

    quote_match = re.search(rf"(?m)^> \*\*{re.escape(field)}：\*\*\s*(.+)$", item)
    if quote_match:
        return quote_match.group(1).strip()

    inline_bold_match = re.search(rf"(?m)^\*\*{re.escape(field)}：\*\*\s*(.+)$", item)
    if inline_bold_match:
        return inline_bold_match.group(1).strip()

    heading_match = re.search(rf"(?m)^\*\*{re.escape(field)}\*\*\s*$", item)
    if not heading_match:
        return ""

    lines = item[heading_match.end() :].splitlines()
    value_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not value_lines and not stripped:
            continue
        if re.match(r"^(\*\*[^*]+\*\*|> |---$|### |## )", stripped):
            break
        value_lines.append(line)

    return "\n".join(value_lines).strip()


def check_top_items(text: str) -> list[str]:
    issues: list[str] = []
    top_section = get_section(text, TOP_SECTION)
    top_items = get_items(top_section)

    if not top_items:
        issues.append("missing Top 5 items")
        return issues

    if len(top_items) > 5:
        issues.append(f"has more than 5 Top items: {len(top_items)}")

    if len(top_items) < 5 and "今日候选不足" not in text:
        issues.append("has fewer than 5 Top items but does not explain candidate shortage")

    required_fields = ["来源", "原文链接", "摘要", "能力与应用", "为什么重要", "对我的影响", "后续关注", "推荐动作"]
    source_counts: dict[str, int] = {}
    for index, item in enumerate(top_items, start=1):
        for field in required_fields:
            if not field_value(item, field):
                issues.append(f"Top item {index} missing field: {field}")

        source = field_value(item, "来源")
        if source:
            source_counts[source] = source_counts.get(source, 0) + 1

        source_link = field_value(item, "原文链接")
        if source_link and not source_link.startswith("http"):
            issues.append(f"Top item {index} source link is not a URL")

        summary = field_value(item, "摘要")
        if summary:
            summary_chars = len(summary)
            if summary_chars < SUMMARY_MIN_CHARS:
                issues.append(f"Top item {index} summary too short: {summary_chars} chars")
            if summary_chars > SUMMARY_MAX_CHARS:
                issues.append(f"Top item {index} summary too long: {summary_chars} chars")

    concentrated_sources = [source for source, count in source_counts.items() if count > 2]
    if concentrated_sources:
        judgment_section = get_section(text, "## 今日判断")
        for source in concentrated_sources:
            if source not in judgment_section:
                issues.append(f"Top 5 has more than 2 items from {source} but 今日判断 does not explain it")

    return issues


def check_secondary_items(text: str) -> list[str]:
    issues: list[str] = []
    secondary_section = get_section(text, SECONDARY_SECTION)
    secondary_items = get_items(secondary_section)

    if len(secondary_items) > 5:
        issues.append(f"Secondary item count should be at most 5, got {len(secondary_items)}")
    if len(secondary_items) < 5 and "今日候选不足" not in text:
        issues.append("has fewer than 5 secondary items but does not explain candidate shortage")

    required_fields = ["来源", "原文链接", "关注理由"]
    for index, item in enumerate(secondary_items, start=1):
        for field in required_fields:
            if not field_value(item, field):
                issues.append(f"Secondary item {index} missing field: {field}")

        source_link = field_value(item, "原文链接")
        if source_link and not source_link.startswith("http"):
            issues.append(f"Secondary item {index} source link is not a URL")

    return issues


def check_github_items(text: str) -> list[str]:
    issues: list[str] = []
    github_section = get_section(text, GITHUB_SECTION)
    github_items = get_items(github_section)

    if len(github_items) > 5:
        issues.append(f"GitHub Trending item count should be at most 5, got {len(github_items)}")
    if len(github_items) < 5 and "今日候选不足" not in text:
        issues.append(f"GitHub Trending has fewer than 5 items but does not explain candidate shortage: {len(github_items)}")

    required_fields = ["链接", "它解决什么问题", "反映的技术 / 产品趋势", "对我的参考价值"]
    for index, item in enumerate(github_items, start=1):
        for field in required_fields:
            if not field_value(item, field):
                issues.append(f"GitHub item {index} missing field: {field}")

        link = field_value(item, "链接")
        if link and not link.startswith("http"):
            issues.append(f"GitHub item {index} link is not a URL")

    return issues


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

    if "http" not in text:
        issues.append("missing source links")

    issues.extend(check_top_items(text))
    issues.extend(check_secondary_items(text))
    issues.extend(check_github_items(text))
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
