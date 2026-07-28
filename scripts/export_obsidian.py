from __future__ import annotations

import argparse
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV_LOCAL_PATH = ROOT / ".env.local"
BRIEFS_DIR = ROOT / "data" / "briefs"
DEFAULT_OBSIDIAN_DIR = "Daily Briefs"


def today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def env_local_values() -> dict[str, str]:
    if not ENV_LOCAL_PATH.exists():
        return {}

    values: dict[str, str] = {}
    for raw_line in ENV_LOCAL_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[key] = value
    return values


def setting(name: str, default: str = "") -> str:
    value = os.environ.get(name)
    if value:
        return value
    return env_local_values().get(name, default)


def export_brief(date: str, overwrite: bool = False) -> Path:
    brief_path = BRIEFS_DIR / f"{date}-ai-daily-brief.md"
    if not brief_path.exists():
        raise FileNotFoundError(f"brief not found: {brief_path.relative_to(ROOT)}")

    vault_path = setting("OBSIDIAN_VAULT_PATH")
    if not vault_path:
        raise RuntimeError("OBSIDIAN_VAULT_PATH is not set")

    obsidian_dir = setting("OBSIDIAN_AI_RADAR_DIR", DEFAULT_OBSIDIAN_DIR).strip().strip("/")
    target_dir = Path(vault_path).expanduser() / obsidian_dir
    target_dir.mkdir(parents=True, exist_ok=True)

    target_path = target_dir / brief_path.name
    if target_path.exists() and not overwrite:
        print(f"obsidian brief exists, skipped: {target_path}")
        return target_path

    shutil.copy2(brief_path, target_path)
    print(f"exported: {target_path}")
    return target_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a daily brief to an Obsidian vault.")
    parser.add_argument("--date", default=today(), help="Date to export, format YYYY-MM-DD.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Obsidian brief file.")
    args = parser.parse_args()

    export_brief(args.date, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
