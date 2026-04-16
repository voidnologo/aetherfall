#!/usr/bin/env python3
"""Sync art assets to/from S3.

Push and pull generated/approved/archived art to an S3 bucket so large
binary files stay out of git. Wraps `aws s3 sync` with project-aware defaults.

Usage:
    python tools/art_sync.py push [--path generated|approved|all] [--dry-run] [--delete]
    python tools/art_sync.py pull [--path generated|approved|all] [--dry-run] [--delete]
    python tools/art_sync.py status

Configuration:
    Set the bucket via ART_SYNC_BUCKET env var or create .art-sync.conf in the project root
    with the bucket name on the first non-comment line.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / ".art-sync.conf"

SYNC_TIMEOUT = 600  # seconds per sync command

# Art types that have the generated/approved/archived pipeline
ART_TYPES = ["characters", "creatures", "equipment", "spots", "decorative", "locations", "plates",
             "logo", "hero", "emboss"]


@dataclass(frozen=True)
class SyncTarget:
    """A local directory <-> S3 prefix mapping."""
    key: str
    local_path: Path
    s3_prefix: str
    description: str


def _build_targets() -> dict[str, SyncTarget]:
    """Build sync targets covering all art pipeline stages."""
    return {
        "generated": SyncTarget(
            key="generated",
            local_path=ROOT / "art",
            s3_prefix="art/",
            description="All art (generated + approved + archived)",
        ),
    }


SYNC_TARGETS = _build_targets()


# ── Configuration ─────────────────────────────────────────────


def _resolve_bucket() -> str | None:
    """Resolve the S3 bucket name from env var or config file."""
    env_val = os.environ.get("ART_SYNC_BUCKET")
    if env_val:
        return env_val.strip()

    if CONFIG_FILE.is_file():
        for line in CONFIG_FILE.read_text().splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                return stripped
    return None


# ── Validation ────────────────────────────────────────────────


def _check_aws_cli() -> bool:
    """Check that the AWS CLI is installed and reachable."""
    try:
        result = subprocess.run(
            ["aws", "--version"],
            capture_output=True,
            timeout=10,
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False
    except subprocess.TimeoutExpired:
        return False


def _check_bucket_access(bucket: str) -> bool:
    """Verify the bucket exists and we have list access."""
    try:
        result = subprocess.run(
            ["aws", "s3", "ls", f"s3://{bucket}/", "--page-size", "1"],
            capture_output=True,
            timeout=30,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


# ── Core sync ─────────────────────────────────────────────────


def _run_sync(
    source: str,
    dest: str,
    dry_run: bool,
    delete: bool,
) -> subprocess.CompletedProcess[bytes]:
    """Execute a single aws s3 sync command."""
    cmd = ["aws", "s3", "sync", source, dest]
    if dry_run:
        cmd.append("--dryrun")
    if delete:
        cmd.append("--delete")
    return subprocess.run(cmd, capture_output=True, timeout=SYNC_TIMEOUT)


# ── Helpers ───────────────────────────────────────────────────


def _format_size(size_bytes: int) -> str:
    """Human-readable file size."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


def _count_local_files(path: Path) -> tuple[int, int]:
    """Count files and total size under a directory. Returns (count, total_bytes)."""
    if not path.is_dir():
        return 0, 0
    count = 0
    total = 0
    for f in path.rglob("*"):
        if f.is_file():
            count += 1
            total += f.stat().st_size
    return count, total


def _parse_s3_summary(output: str) -> int:
    """Parse aws s3 sync --dryrun output to count files."""
    lines = [line for line in output.strip().splitlines() if line.strip()]
    return len(lines)


def _show_diff_summary(target: SyncTarget, bucket: str) -> None:
    """Show what would push and pull for a single target."""
    local_count, local_size = _count_local_files(target.local_path)
    s3_uri = f"s3://{bucket}/{target.s3_prefix}"

    print(f"\n  {target.description} ({target.key})")
    print(f"    Local: {local_count} files ({_format_size(local_size)})")
    if not target.local_path.is_dir():
        print("    Local directory does not exist")
        return

    try:
        push_result = _run_sync(str(target.local_path), s3_uri, dry_run=True, delete=False)
        push_count = _parse_s3_summary(push_result.stdout.decode())
        print(f"    Would push: {push_count} file(s)")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("    Would push: (unable to check)")

    try:
        pull_result = _run_sync(s3_uri, str(target.local_path), dry_run=True, delete=False)
        pull_count = _parse_s3_summary(pull_result.stdout.decode())
        print(f"    Would pull: {pull_count} file(s)")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("    Would pull: (unable to check)")


# ── Commands ──────────────────────────────────────────────────


def cmd_push(bucket: str, dry_run: bool, delete: bool) -> int:
    """Push local art to S3."""
    target = SYNC_TARGETS["generated"]

    if not target.local_path.is_dir():
        print(f"SKIP: local path {target.local_path} does not exist")
        return 1

    s3_uri = f"s3://{bucket}/{target.s3_prefix}"
    label = "DRY RUN push" if dry_run else "Pushing"
    print(f"{label}: {target.local_path} -> {s3_uri}")

    try:
        result = _run_sync(str(target.local_path), s3_uri, dry_run, delete)
    except subprocess.TimeoutExpired:
        print(f"FAIL: sync timed out after {SYNC_TIMEOUT}s")
        return 1

    if result.returncode != 0:
        print(f"FAIL: {result.stderr.decode().strip()}")
        return 1

    output = result.stdout.decode().strip()
    if output:
        print(output)
    print("OK")
    return 0


def cmd_pull(bucket: str, dry_run: bool, delete: bool) -> int:
    """Pull art from S3 to local."""
    target = SYNC_TARGETS["generated"]
    target.local_path.mkdir(parents=True, exist_ok=True)

    s3_uri = f"s3://{bucket}/{target.s3_prefix}"
    label = "DRY RUN pull" if dry_run else "Pulling"
    print(f"{label}: {s3_uri} -> {target.local_path}")

    try:
        result = _run_sync(s3_uri, str(target.local_path), dry_run, delete)
    except subprocess.TimeoutExpired:
        print(f"FAIL: sync timed out after {SYNC_TIMEOUT}s")
        return 1

    if result.returncode != 0:
        print(f"FAIL: {result.stderr.decode().strip()}")
        return 1

    output = result.stdout.decode().strip()
    if output:
        print(output)
    print("OK")
    return 0


def cmd_status(bucket: str) -> int:
    """Show sync status."""
    print(f"Bucket: s3://{bucket}/")
    _show_diff_summary(SYNC_TARGETS["generated"], bucket)

    # Also show per-type breakdown
    print("\n  Per-type breakdown (local):")
    for art_type in ART_TYPES:
        type_dir = ROOT / "art" / art_type
        if not type_dir.is_dir():
            continue
        for stage in ("generated", "approved", "archived"):
            stage_dir = type_dir / stage
            count, size = _count_local_files(stage_dir)
            if count > 0:
                print(f"    {art_type}/{stage}: {count} files ({_format_size(size)})")
    print()
    return 0


# ── CLI ───────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Sync Aetherfall art assets to/from S3",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  %(prog)s push --dry-run    Preview what would be pushed\n"
            "  %(prog)s pull              Pull all art from S3\n"
            "  %(prog)s status            Show local art inventory and sync status\n"
        ),
    )
    sub = parser.add_subparsers(dest="command")

    for cmd_name in ("push", "pull"):
        p = sub.add_parser(cmd_name, help=f"{cmd_name.title()} art assets")
        p.add_argument("--dry-run", action="store_true", help="Preview without making changes")
        p.add_argument("--delete", action="store_true", help="Remove files at destination not in source")

    sub.add_parser("status", help="Show sync status")

    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 1

    bucket = _resolve_bucket()
    if not bucket:
        print(
            "ERROR: No S3 bucket configured.\n"
            "Set ART_SYNC_BUCKET env var or create .art-sync.conf in the project root."
        )
        return 1

    if not _check_aws_cli():
        print("ERROR: AWS CLI not found. Install it: https://aws.amazon.com/cli/")
        return 1

    if not _check_bucket_access(bucket):
        print(f"ERROR: Cannot access bucket s3://{bucket}/. Check credentials and bucket name.")
        return 1

    if args.command == "status":
        return cmd_status(bucket)
    elif args.command == "push":
        return cmd_push(bucket, args.dry_run, args.delete)
    elif args.command == "pull":
        return cmd_pull(bucket, args.dry_run, args.delete)
    return 1


if __name__ == "__main__":
    sys.exit(main())
