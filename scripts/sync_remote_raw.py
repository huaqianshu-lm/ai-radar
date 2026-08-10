from __future__ import annotations

import argparse
import re
import subprocess
import tarfile
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class SyncResult:
    copied_files: int
    unchanged_files: int
    dates: tuple[str, ...]


def valid_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from error
    return value


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "no details"
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result


def remote_branch_exists(remote: str, branch: str) -> bool:
    result = run_git(["ls-remote", "--exit-code", "--heads", remote, branch], check=False)
    if result.returncode == 0:
        return True
    if result.returncode == 2:
        return False
    detail = result.stderr.strip() or result.stdout.strip() or "no details"
    raise RuntimeError(f"cannot inspect remote branch {remote}/{branch}: {detail}")


def fetch_remote_branch(remote: str, branch: str) -> str:
    if not remote_branch_exists(remote, branch):
        return ""

    tracking_ref = f"refs/remotes/{remote}/{branch}"
    run_git(["fetch", "--no-tags", remote, f"refs/heads/{branch}:{tracking_ref}"])
    return f"{remote}/{branch}"


def archive_raw(ref: str, archive_path: Path) -> None:
    with archive_path.open("wb") as archive_file:
        result = subprocess.run(
            ["git", "archive", "--format=tar", ref, "data/raw"],
            cwd=ROOT,
            stdout=archive_file,
            stderr=subprocess.PIPE,
        )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip() or "no details"
        raise RuntimeError(f"cannot read remote raw archive: {detail}")


def sync_remote_raw(
    remote: str = "origin",
    branch: str = "remote-news",
    date_filter: str | None = None,
) -> SyncResult:
    ref = fetch_remote_branch(remote, branch)
    if not ref:
        print(f"remote branch not found: {remote}/{branch}")
        return SyncResult(copied_files=0, unchanged_files=0, dates=())

    pending: list[tuple[Path, bytes, str]] = []
    unchanged_files = 0
    dates: set[str] = set()

    with tempfile.TemporaryDirectory(prefix="ai-radar-remote-raw-") as temp_dir:
        archive_path = Path(temp_dir) / "raw.tar"
        archive_raw(ref, archive_path)
        with tarfile.open(archive_path, mode="r:") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue

                parts = Path(member.name).parts
                if len(parts) < 4 or parts[:2] != ("data", "raw"):
                    continue
                if any(part in {"", ".", ".."} for part in parts):
                    raise RuntimeError(f"unsafe path in remote raw archive: {member.name}")

                run_date = parts[2]
                if not DATE_PATTERN.fullmatch(run_date):
                    continue
                if date_filter and run_date != date_filter:
                    continue

                source = archive.extractfile(member)
                if source is None:
                    continue
                content = source.read()
                destination = ROOT.joinpath(*parts)
                if destination.exists():
                    if not destination.is_file():
                        raise RuntimeError(f"local raw path is not a file: {destination.relative_to(ROOT)}")
                    if destination.read_bytes() != content:
                        raise RuntimeError(
                            "local raw conflicts with remote file; refusing to overwrite: "
                            f"{destination.relative_to(ROOT)}"
                        )
                    unchanged_files += 1
                    continue

                pending.append((destination, content, run_date))
                dates.add(run_date)

    for destination, content, _ in pending:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)

    result = SyncResult(
        copied_files=len(pending),
        unchanged_files=unchanged_files,
        dates=tuple(sorted(dates)),
    )
    print(
        f"remote raw sync: copied {result.copied_files}, "
        f"unchanged {result.unchanged_files}, dates {', '.join(result.dates) or 'none'}"
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync raw news from the remote-news Git branch.")
    parser.add_argument("--remote", default="origin", help="Git remote name.")
    parser.add_argument("--branch", default="remote-news", help="Remote raw branch name.")
    parser.add_argument("--date", type=valid_date, default=None, help="Only sync one date, format YYYY-MM-DD.")
    args = parser.parse_args()

    sync_remote_raw(remote=args.remote, branch=args.branch, date_filter=args.date)


if __name__ == "__main__":
    main()
