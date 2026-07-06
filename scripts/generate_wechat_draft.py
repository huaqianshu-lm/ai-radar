from __future__ import annotations

import argparse
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIEFS_DIR = ROOT / "data" / "briefs"
DRAFTS_DIR = ROOT / "data" / "wechat" / "drafts"
PROMPT_PATH = ROOT / "config" / "wechat_draft_prompt.md"


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def build_prompt(base_prompt: str, brief: str, date: str) -> str:
    return (
        f"{base_prompt.rstrip()}\n\n"
        f"## 日期\n\n{date}\n\n"
        "## AI Daily Brief\n\n"
        f"{brief}\n"
    )


def generate(date: str, overwrite: bool = False, retries: int = 1) -> Path:
    if shutil.which("claude") is None:
        raise RuntimeError("Claude Code CLI not found: claude")

    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"wechat draft prompt not found: {PROMPT_PATH.relative_to(ROOT)}")

    brief_path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
    if not brief_path.exists():
        raise FileNotFoundError(f"brief not found: {brief_path.relative_to(ROOT)}")

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = DRAFTS_DIR / f"{date}.md"
    if output_path.exists() and not overwrite:
        print(f"wechat draft exists, skipped: {output_path.relative_to(ROOT)}")
        return output_path

    base_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    brief = brief_path.read_text(encoding="utf-8")
    prompt = build_prompt(base_prompt, brief, date)

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

    draft = result.stdout.strip()
    if not draft:
        raise RuntimeError("Claude Code returned empty wechat draft")

    output_path.write_text(draft + "\n", encoding="utf-8")
    print(f"written: {output_path.relative_to(ROOT)}")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a WeChat Markdown draft from the daily brief.")
    parser.add_argument("--date", default=today(), help="Date to generate, format YYYY-MM-DD.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing WeChat draft file.")
    args = parser.parse_args()

    generate(args.date, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
