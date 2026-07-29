from __future__ import annotations

import argparse
import json
from datetime import timezone
from pathlib import Path

from check_brief import check
from export_obsidian import export_brief
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


def source_contributions(items_path: Path) -> list[dict[str, object]]:
    if not items_path.exists():
        return []

    stats: dict[str, dict[str, int]] = {}
    for line in items_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        source = str(item.get("source") or "unknown")
        summary = str(item.get("summary") or "")
        source_stats = stats.setdefault(source, {"items": 0, "list_pages": 0, "summary_chars": 0})
        source_stats["items"] += 1
        source_stats["summary_chars"] += len(summary)
        if item.get("is_list_page"):
            source_stats["list_pages"] += 1

    contributions = []
    for source, source_stats in stats.items():
        items = source_stats["items"]
        contributions.append(
            {
                "source": source,
                "items": items,
                "list_pages": source_stats["list_pages"],
                "avg_summary_chars": round(source_stats["summary_chars"] / items) if items else 0,
            }
        )
    return sorted(contributions, key=lambda item: (-int(item["items"]), str(item["source"])))


def cluster_summary(items_path: Path) -> dict[str, int]:
    if not items_path.exists():
        return {"clusters": 0, "multi_item_clusters": 0, "max_cluster_size": 0}

    clusters: dict[str, int] = {}
    for line in items_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        cluster_key = str(item.get("cluster_key") or item.get("canonical_url") or item.get("url") or item.get("raw_path") or "")
        if not cluster_key:
            continue
        clusters[cluster_key] = clusters.get(cluster_key, 0) + 1

    sizes = list(clusters.values())
    return {
        "clusters": len(clusters),
        "multi_item_clusters": sum(1 for size in sizes if size > 1),
        "max_cluster_size": max(sizes, default=0),
    }


def daily_reminders(
    statuses: list[dict[str, object]],
    normalize_result: NormalizeResult,
    brief_issues: list[str],
    contributions: list[dict[str, object]],
    brief_error: str = "",
    obsidian_error: str = "",
) -> list[str]:
    reminders: list[str] = []
    failed_sources = [str(status["name"]) for status in statuses if not status["ok"]]
    if failed_sources:
        reminders.append("复查失败来源：" + "、".join(failed_sources))

    if normalize_result.written_count < 5:
        reminders.append(f"今日进入 brief input 的 items 只有 {normalize_result.written_count} 条，注意候选不足")

    weak_sources = [
        str(contribution["source"])
        for contribution in contributions
        if int(contribution["items"]) >= 2 and int(contribution["avg_summary_chars"]) < 80
    ]
    if weak_sources:
        reminders.append("这些来源摘要偏短，生成简报时要注意信息不足：" + "、".join(weak_sources))

    list_page_sources = [
        str(contribution["source"])
        for contribution in contributions
        if int(contribution["items"]) > 0 and int(contribution["items"]) == int(contribution["list_pages"])
    ]
    if list_page_sources:
        reminders.append("这些来源主要是列表页，Top 5 中应谨慎使用：" + "、".join(list_page_sources))

    if brief_error:
        reminders.append("简报未生成，需要手动检查 Claude Code 调用失败原因")
    elif brief_issues:
        reminders.append("简报质量检查未通过，需要先修正 brief 再使用")

    if obsidian_error:
        reminders.append("Obsidian 导出失败，需要手动检查 Vault 配置或目标文件")

    if not reminders:
        reminders.append("今日无明显异常，重点看 Top 5 是否有实际参考价值")
    return reminders


def write_run_summary(
    date: str,
    statuses: list[dict[str, object]],
    normalize_result: NormalizeResult,
    brief_input_path: Path,
    brief_path: Path | None,
    obsidian_path: Path | None,
    brief_issues: list[str],
    contributions: list[dict[str, object]],
    cluster_stats: dict[str, int],
    reminders: list[str],
    brief_error: str = "",
    obsidian_error: str = "",
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
        f"- obsidian: `{obsidian_path}`" if obsidian_path else "- obsidian: not exported",
        "",
        "## 去重状态",
        "",
        f"- raw scanned: {normalize_result.raw_count}",
        f"- items written: {normalize_result.written_count}",
        f"- duplicates skipped: {normalize_result.skipped_current_duplicates} current, {normalize_result.skipped_history_duplicates} history",
        "",
        "## 事件聚类观察",
        "",
        f"- clusters: {cluster_stats['clusters']}",
        f"- multi-item clusters: {cluster_stats['multi_item_clusters']}",
        f"- max cluster size: {cluster_stats['max_cluster_size']}",
        "",
        "## 来源状态",
        "",
    ]
    for status in statuses:
        if status["ok"]:
            lines.append(f"- {status['name']}：成功，{status['items']} 条，新增 raw {status['saved']} 条")
        else:
            lines.append(f"- {status['name']}：失败，原因：{status['error']}")
    lines.extend(["", "## 来源贡献统计", ""])
    if contributions:
        lines.append("| 来源 | items | list pages | avg summary chars |")
        lines.append("| --- | ---: | ---: | ---: |")
        for contribution in contributions:
            lines.append(
                f"| {contribution['source']} | {contribution['items']} | "
                f"{contribution['list_pages']} | {contribution['avg_summary_chars']} |"
            )
    else:
        lines.append("- 无 items 贡献")
    lines.extend(["", "## 简报质量检查", ""])
    if brief_path:
        if brief_issues:
            lines.extend([f"- {issue}" for issue in brief_issues])
        else:
            lines.append("- 通过")
    elif brief_error:
        lines.append(f"- 未生成简报：{brief_error}")
    else:
        lines.append("- 未生成简报")
    lines.extend(["", "## Obsidian 导出", ""])
    if obsidian_path:
        lines.append(f"- 已导出：`{obsidian_path}`")
    elif obsidian_error:
        lines.append(f"- 导出失败：{obsidian_error}")
    else:
        lines.append("- 未导出")
    lines.extend(["", "## 今日提醒", ""])
    lines.extend([f"- {reminder}" for reminder in reminders])
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def run(limit: int, generate_brief: bool, overwrite_brief: bool, export_obsidian: bool, overwrite_obsidian: bool) -> None:
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
    brief_path = None
    brief_error = ""
    if generate_brief:
        try:
            brief_path = generate(run_date, overwrite=overwrite_brief)
        except Exception as error:
            brief_error = str(error)
            print(f"failed to generate brief: {brief_error}")
            write_log(f"failed to generate brief: {brief_error}")
    if brief_path:
        append_source_status(brief_path, statuses)
    brief_issues = check(run_date) if brief_path else []
    obsidian_path = None
    obsidian_error = ""
    if export_obsidian and brief_path and not brief_issues:
        try:
            obsidian_path = export_brief(run_date, overwrite=overwrite_obsidian)
        except Exception as error:
            obsidian_error = str(error)
            print(f"failed to export obsidian brief: {obsidian_error}")
            write_log(f"failed to export obsidian brief: {obsidian_error}")
    contributions = source_contributions(items_path)
    cluster_stats = cluster_summary(items_path)
    reminders = daily_reminders(statuses, normalize_result, brief_issues, contributions, brief_error, obsidian_error)

    summary_path = write_run_summary(
        run_date,
        statuses,
        normalize_result,
        brief_input_path,
        brief_path,
        obsidian_path,
        brief_issues,
        contributions,
        cluster_stats,
        reminders,
        brief_error,
        obsidian_error,
    )

    print(f"done: {total_saved} new raw files")
    print(f"items: {items_path.relative_to(ROOT)}")
    print(f"items written: {normalize_result.written_count}")
    print(
        "duplicates skipped: "
        f"{normalize_result.skipped_current_duplicates} current, {normalize_result.skipped_history_duplicates} history"
    )
    print(f"brief input: {brief_input_path.relative_to(ROOT)}")
    if obsidian_path:
        print(f"obsidian: {obsidian_path}")
    elif export_obsidian and obsidian_error:
        print(f"obsidian export: failed: {obsidian_error}")
    elif export_obsidian and not brief_path:
        print("obsidian export: skipped because brief was not generated")
    elif export_obsidian and brief_issues:
        print("obsidian export: skipped because brief quality check failed")
    print(f"run summary: {summary_path.relative_to(ROOT)}")
    print("daily reminders:")
    for reminder in reminders:
        print(f"- {reminder}")
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
    parser.add_argument("--export-obsidian", action="store_true", help="Export the generated brief to the configured Obsidian vault.")
    parser.add_argument("--overwrite-obsidian", action="store_true", help="Overwrite existing Obsidian brief file when exporting.")
    args = parser.parse_args()

    run(
        args.limit,
        generate_brief=args.generate_brief,
        overwrite_brief=args.overwrite_brief,
        export_obsidian=args.export_obsidian,
        overwrite_obsidian=args.overwrite_obsidian,
    )


if __name__ == "__main__":
    main()
