#!/usr/bin/env python3
"""Scaffold and validate representative profiles in temporary directories."""
from __future__ import annotations
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "scripts" / "scaffold_agentic_kit.py"
VALIDATE = ROOT / "scripts" / "validate_scaffold.py"
AUDIT = ROOT / "scripts" / "audit_existing_kit.py"
REPAIR = ROOT / "scripts" / "repair_kit.py"
PROFILE_DIFF = ROOT / "scripts" / "profile_diff.py"
MIGRATE = ROOT / "scripts" / "migrate_profile.py"
ROLLBACK = ROOT / "scripts" / "rollback_migration.py"

CASES = [
    ("lean", []),
    ("standard", []),
    ("rigorous", ["--include-research-agents", "--include-doc-agents", "--include-security-agents"]),
]


def run_case(base: Path, profile: str, extras: list[str]) -> None:
    repo = base / f"repo-{profile}"
    repo.mkdir(parents=True, exist_ok=True)
    scaffold_cmd = [sys.executable, str(SCAFFOLD), str(repo), "--profile", profile] + extras
    validate_cmd = [sys.executable, str(VALIDATE), str(repo), "--profile", profile] + extras
    audit_cmd = [sys.executable, str(AUDIT), str(repo), "--output", str(repo / 'docs' / 'agentic-workflow' / 'KIT_DRIFT_REPORT.md')]
    subprocess.run(scaffold_cmd, check=True)
    subprocess.run(validate_cmd, check=True)
    subprocess.run(audit_cmd, check=True)
    # remove one managed file and confirm repair can restore it
    lost = repo / 'docs' / 'agentic-workflow' / '10_closure_report.md'
    lost.unlink()
    repair_cmd = [sys.executable, str(REPAIR), str(repo), '--profile', profile, '--report-output', str(repo / 'docs' / 'agentic-workflow' / 'KIT_DRIFT_REPORT.md')] + extras
    subprocess.run(repair_cmd, check=True)
    subprocess.run(validate_cmd, check=True)


def main() -> int:
    tempdir = Path(tempfile.mkdtemp(prefix="agentic-kit-smoke-"))
    try:
        for profile, extras in CASES:
            run_case(tempdir, profile, extras)
        subprocess.run([sys.executable, str(PROFILE_DIFF), '--from-profile', 'lean', '--to-profile', 'standard'], check=True, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, str(PROFILE_DIFF), '--from-profile', 'standard', '--to-profile', 'rigorous', '--to-include-research-agents'], check=True, stdout=subprocess.DEVNULL)
        migrate_repo = tempdir / 'repo-rigorous'
        subprocess.run([sys.executable, str(MIGRATE), str(migrate_repo), '--to-profile', 'standard', '--apply', '--report-output', str(migrate_repo / 'docs' / 'agentic-workflow' / 'PROFILE_MIGRATION_REPORT.md')], check=True)
        subprocess.run([sys.executable, str(VALIDATE), str(migrate_repo), '--profile', 'standard'], check=True)
        subprocess.run([sys.executable, str(ROLLBACK), str(migrate_repo), '--target-profile', 'rigorous', '--include-research-agents', '--include-doc-agents', '--include-security-agents', '--apply', '--report-output', str(migrate_repo / 'docs' / 'agentic-workflow' / 'ROLLBACK_REPORT.md')], check=True)
        subprocess.run([sys.executable, str(VALIDATE), str(migrate_repo), '--profile', 'rigorous', '--include-research-agents', '--include-doc-agents', '--include-security-agents'], check=True)
        print("Smoke test passed for lean, standard, and rigorous profiles, including repair, profile diff, migration, and rollback checks.")
        return 0
    finally:
        shutil.rmtree(tempdir, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
