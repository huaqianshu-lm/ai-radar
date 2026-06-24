from __future__ import annotations

import argparse
from datetime import timezone
from pathlib import Path

from check_brief import check
from fetch_sources import fetch_source, load_sources, save_raw_items, utc_now, write_log
from generate_brief import generate
from normalize_items import NormalizeResult, normalize
from prepare_brief_input import prepare

ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "data" / "inbox"


def render_source_status(statuses: list[dict[str, object]]) -> str:
    lines = ["", "## 抓取状态", ""]
    for status in statuses:
        if status["ok"]:
            lines.append(f"- {status['name']}：成功，{status['items']} 条，新增 raw {status['saved']} 条")
        else:
            lines.append(f"- {status['name']}：失败，原因：{status['error']}")
    return "\n".join(lines) + "\n"


def append_source_status(brief_path: Path, statuses: list[dict[str, object]]) -> None:
    text = brief_path.read_text(encoding="utf-8")
    marker = "\n## 抓取状态\n"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip() + "\n"
    brief_path.write_text(text.rstrip() + "\n" + render_source_status(statuses), encoding="utf-8")


def write_run_summary(
    date: str,
    statuses: list[dict[str, object]],
    normalize_result: NormalizeResult,
    brief_input_path: Path,
    brief_path: Path | None,
    brief_issues: list[str],
) -> Path:
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    output_path = INBOX_DIR / f"{date}-run-summary.md"
    lines = [
        f"# AI Radar Run Summary - {date}",
        "",
        "## 输出文件",
        "",
        f"- items: `{normalize_result.path.relative_to(ROOT)}`",
        f"- brief input: `{brief_input_path.relative_to(ROOT)}`",
        f"- brief: `{brief_path.relative_to(ROOT)}`" if brief_path else "- brief: not generated",
        "",
        "## 去重状态",
        "",
        f"- raw scanned: {normalize_result.raw_count}",
        f"- items written: {normalize_result.written_count}",
        f"- duplicates skipped: {normalize_result.skipped_current_duplicates} current, {normalize_result.skipped_history_duplicates} history",
        "",
        "## 来源状态",
        "",
    ]
    for status in statuses:
        if status["ok"]:
            lines.append(f"- {status['name']}：成功，{status['items']} 条，新增 raw {status['saved']} 条")
        else:
            lines.append(f"- {status['name']}：失败，原因：{status['error']}")
    lines.extend(["", "## 简报质量检查", ""])
    if brief_path:
        if brief_issues:
            lines.extend([f"- {issue}" for issue in brief_issues])
        else:
            lines.append("- 通过")
    else:
        lines.append("- 未生成简报")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def run(limit: int, generate_brief: bool, overwrite_brief: bool) -> None:
    fetched_at = utc_now().isoformat()
    run_date = fetched_at[:10]
    sources = load_sources()

    total_saved = 0
    statuses: list[dict[str, object]] = []
    for source in sources:
        name = source.get("name", "unknown")
        try:
            source_limit = int(source.get("max_items") or limit)
            items = fetch_source(source, source_limit, fetched_at)
            saved = save_raw_items(items, run_date)
            total_saved += saved
            message = f"fetched {name}: {len(items)} items, {saved} new raw files"
            statuses.append({"name": name, "ok": True, "items": len(items), "saved": saved, "error": ""})
            print(message)
            write_log(message)
        except Exception as error:
            message = f"failed {name}: {error}"
            statuses.append({"name": name, "ok": False, "items": 0, "saved": 0, "error": str(error)})
            print(message)
            write_log(message)

    normalize_result = normalize(run_date)
    items_path = normalize_result.path
    brief_input_path = prepare(run_date)
    brief_path = generate(run_date, overwrite=overwrite_brief) if generate_brief else None
    if brief_path:
        append_source_status(brief_path, statuses)
    brief_issues = check(run_date) if brief_path else []

    summary_path = write_run_summary(run_date, statuses, normalize_result, brief_input_path, brief_path, brief_issues)

    print(f"done: {total_saved} new raw files")
    print(f"items: {items_path.relative_to(ROOT)}")
    print(f"items written: {normalize_result.written_count}")
    print(
        "duplicates skipped: "
        f"{normalize_result.skipped_current_duplicates} current, {normalize_result.skipped_history_duplicates} history"
    )
    print(f"brief input: {brief_input_path.relative_to(ROOT)}")
    print(f"run summary: {summary_path.relative_to(ROOT)}")
    if brief_path:
        print(f"brief: {brief_path.relative_to(ROOT)}")
        if brief_issues:
            print("brief quality check: failed")
            for issue in brief_issues:
                print(f"- {issue}")
        else:
            print("brief quality check: passed")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the v0 daily AI radar workflow.")
    parser.add_argument("--limit", type=int, default=10, help="Max entries per RSS source.")
    parser.add_argument("--generate-brief", action="store_true", help="Generate the final Markdown brief with Claude Code CLI.")
    parser.add_argument("--overwrite-brief", action="store_true", help="Overwrite existing brief file when generating.")
    args = parser.parse_args()

    run(args.limit, generate_brief=args.generate_brief, overwrite_brief=args.overwrite_brief)


if __name__ == "__main__":
    main()
