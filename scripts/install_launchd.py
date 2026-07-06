from __future__ import annotations

import argparse
import os
import plistlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABEL = "com.huaqianshu.ai-radar.daily"
PLIST_PATH = Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
STDOUT_LOG = ROOT / "logs" / "launchd.out.log"
STDERR_LOG = ROOT / "logs" / "launchd.err.log"


def build_plist() -> dict[str, object]:
    return {
        "Label": LABEL,
        "ProgramArguments": [str(ROOT / "ai-radar")],
        "WorkingDirectory": str(ROOT),
        "StartCalendarInterval": {"Hour": 8, "Minute": 0},
        "StandardOutPath": str(STDOUT_LOG),
        "StandardErrorPath": str(STDERR_LOG),
        "EnvironmentVariables": {
            "PATH": os.environ.get("PATH", "/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"),
        },
    }


def write_plist() -> None:
    PLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    STDOUT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with PLIST_PATH.open("wb") as file:
        plistlib.dump(build_plist(), file, sort_keys=False)


def run_launchctl(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["launchctl", *args], check=False, capture_output=True, text=True)


def gui_domain() -> str:
    return f"gui/{os.getuid()}"


def install() -> None:
    write_plist()
    run_launchctl(["bootout", gui_domain(), str(PLIST_PATH)])
    result = run_launchctl(["bootstrap", gui_domain(), str(PLIST_PATH)])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "launchctl bootstrap failed")
    enable_result = run_launchctl(["enable", f"{gui_domain()}/{LABEL}"])
    if enable_result.returncode != 0:
        raise RuntimeError(enable_result.stderr.strip() or enable_result.stdout.strip() or "launchctl enable failed")
    print(f"installed: {PLIST_PATH}")
    print("schedule: daily at 08:00 local time")
    print(f"stdout: {STDOUT_LOG.relative_to(ROOT)}")
    print(f"stderr: {STDERR_LOG.relative_to(ROOT)}")


def uninstall() -> None:
    result = run_launchctl(["bootout", gui_domain(), str(PLIST_PATH)])
    if result.returncode != 0 and "No such process" not in result.stderr:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "launchctl bootout failed")
    if PLIST_PATH.exists():
        PLIST_PATH.unlink()
    print(f"uninstalled: {LABEL}")


def status() -> None:
    print(f"label: {LABEL}")
    print(f"plist: {PLIST_PATH}")
    print(f"plist exists: {PLIST_PATH.exists()}")
    result = run_launchctl(["print", f"{gui_domain()}/{LABEL}"])
    if result.returncode == 0:
        print("launchctl: loaded")
    else:
        print("launchctl: not loaded")
        if result.stderr.strip():
            print(result.stderr.strip())


def print_plist() -> None:
    print(plistlib.dumps(build_plist(), sort_keys=False).decode("utf-8"), end="")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the AI Radar daily user LaunchAgent.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("install", help="Install and load the daily LaunchAgent.")
    subparsers.add_parser("uninstall", help="Unload and remove the daily LaunchAgent.")
    subparsers.add_parser("status", help="Show LaunchAgent status.")
    subparsers.add_parser("print-plist", help="Print the generated plist.")
    args = parser.parse_args()

    if args.command == "install":
        install()
    elif args.command == "uninstall":
        uninstall()
    elif args.command == "status":
        status()
    elif args.command == "print-plist":
        print_plist()


if __name__ == "__main__":
    main()
