from __future__ import annotations

import argparse
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX_DIR = ROOT / "data" / "inbox"
BRIEFS_DIR = ROOT / "data" / "briefs"


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def build_prompt(brief_input: str, date: str) -> str:
    return (
        "请根据下面的 brief input 生成 AI Daily Brief。\n\n"
        "要求：\n"
        "- 只输出最终 Markdown 简报正文\n"
        "- 不要输出解释、寒暄或代码围栏\n"
        "- 日期使用 " + date + "\n"
        "- 如果候选内容不足，在简报末尾明确写入限制\n\n"
        "brief input 如下：\n\n"
        f"{brief_input}\n"
    )


def generate(date: str, overwrite: bool = False, retries: int = 1) -> Path:
    if shutil.which("claude") is None:
        raise RuntimeError("Claude Code CLI not found: claude")

    input_path = INBOX_DIR / f"{date}-brief-input.md"
    if not input_path.exists():
        raise FileNotFoundError(f"brief input not found: {input_path.relative_to(ROOT)}")

    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
    if output_path.exists() and not overwrite:
        print(f"brief exists, skipped: {output_path.relative_to(ROOT)}")
        return output_path

    brief_input = input_path.read_text(encoding="utf-8")
    prompt = build_prompt(brief_input, date)

    last_error: subprocess.CalledProcessError | None = None
    for attempt in range(1, retries + 2):
        try:
            result = subprocess.run(
                ["claude", "-p", "--output-format", "text", "--no-session-persistence"],
                input=prompt,
                check=True,
                capture_output=True,
                text=True,
                timeout=600,
            )
            break
        except subprocess.CalledProcessError as error:
            last_error = error
            print(f"Claude Code failed on attempt {attempt}: exit {error.returncode}")
            if error.stdout:
                print("stdout:")
                print(error.stdout.strip())
            if error.stderr:
                print("stderr:")
                print(error.stderr.strip())
            if attempt > retries:
                raise
            time.sleep(2)
    else:
        raise last_error or RuntimeError("Claude Code failed")

    brief = result.stdout.strip()
    if not brief:
        raise RuntimeError("Claude Code returned empty brief")

    output_path.write_text(brief + "\n", encoding="utf-8")
    print(f"written: {output_path.relative_to(ROOT)}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a daily brief with Claude Code CLI.")
    parser.add_argument("--date", default=today(), help="Date to generate, format YYYY-MM-DD.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing brief file.")
    args = parser.parse_args()

    generate(args.date, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
