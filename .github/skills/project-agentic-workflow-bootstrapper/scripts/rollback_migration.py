#!/usr/bin/env python3
"""Rollback a profile migration using quarantined managed files without relying on Git."""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

from audit_existing_kit import markdown_report
from validate_scaffold import expected_files, infer_bundles, infer_profile, validate_root


def latest_quarantine(repo: Path) -> Path | None:
    base = repo / '.agentic-quarantine'
    if not base.exists():
        return None
    candidates = [p for p in base.iterdir() if p.is_dir() and p.name.startswith('profile-migration-')]
    if not candidates:
        return None
    return sorted(candidates)[-1]


def load_metadata(quarantine_dir: Path) -> Dict | None:
    meta = quarantine_dir / 'metadata.json'
    if not meta.exists():
        return None
    try:
        return json.loads(meta.read_text(encoding='utf-8'))
    except Exception:
        return None


def flags_from_args(args) -> Dict[str, bool]:
    return {
        'research': args.include_research_agents,
        'docs': args.include_doc_agents,
        'security': args.include_security_agents,
        'hooks': args.include_hooks,
    }


def resolve_target(repo: Path, args, metadata: Dict | None) -> Tuple[str, Dict[str, bool]]:
    profile = args.target_profile
    bundles = flags_from_args(args)
    if metadata:
        profile = profile or metadata.get('from_profile')
        if not any(bundles.values()) and isinstance(metadata.get('from_bundles'), dict):
            bundles = {k: bool(v) for k, v in metadata['from_bundles'].items()}
    if profile is None:
        profile = infer_profile(repo) or 'standard'
    if not any(bundles.values()) and metadata is None:
        bundles = infer_bundles(repo)
    return profile, bundles


def filecmp(a: Path, b: Path) -> bool:
    try:
        return a.read_bytes() == b.read_bytes()
    except Exception:
        return False


def quarantine_dir(repo: Path, label: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    return repo / '.agentic-quarantine' / f'{label}-{stamp}'


def list_payload_files(quarantine: Path) -> List[str]:
    files: List[str] = []
    for p in quarantine.rglob('*'):
        if p.is_file() and p.name != 'metadata.json':
            files.append(str(p.relative_to(quarantine)))
    return sorted(files)


def restore_payload(repo: Path, quarantine: Path, conflict_dir: Path | None) -> Tuple[List[str], List[str]]:
    restored: List[str] = []
    conflicted: List[str] = []
    for rel in list_payload_files(quarantine):
        src = quarantine / rel
        dst = repo / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            if filecmp(src, dst):
                src.unlink()
                restored.append(rel)
                continue
            if conflict_dir is not None:
                backup = conflict_dir / rel
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(dst), str(backup))
                conflicted.append(rel)
            else:
                dst.unlink()
        shutil.move(str(src), str(dst))
        restored.append(rel)
    # clean empty dirs under quarantine, preserving metadata
    for d in sorted([p for p in quarantine.rglob('*') if p.is_dir()], key=lambda x: len(x.parts), reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass
    return restored, conflicted


def prune_current_to_target(repo: Path, target_profile: str, target_bundles: Dict[str, bool], quarantine_prune: Path | None) -> List[str]:
    target = set(expected_files(target_profile, target_bundles))
    current_profile = infer_profile(repo) or target_profile
    current_bundles = infer_bundles(repo)
    current = set(expected_files(current_profile, current_bundles))
    remove = sorted(current - target)
    pruned: List[str] = []
    for rel in remove:
        path = repo / rel
        if not path.exists() or not path.is_file():
            continue
        if quarantine_prune is not None:
            dest = quarantine_prune / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest))
        else:
            path.unlink()
        pruned.append(rel)
    for d in sorted({(repo / rel).parent for rel in pruned}, key=lambda x: len(x.parts), reverse=True):
        cur = d
        while cur != repo and cur.exists():
            try:
                cur.rmdir()
            except OSError:
                break
            cur = cur.parent
    return pruned


def build_report(repo: Path, quarantine: Path, target_profile: str, target_bundles: Dict[str, bool], restored: List[str], conflicted: List[str], conflict_dir: Path | None, pruned: List[str], prune_dir: Path | None) -> str:
    validation = validate_root(repo, target_profile, target_bundles)
    lines: List[str] = []
    lines.append('# Rollback report')
    lines.append('')
    lines.append('## Target state')
    lines.append(f'- repository: `{repo}`')
    lines.append(f'- quarantine source: `{quarantine}`')
    lines.append(f'- target profile: `{target_profile}`')
    lines.append(f"- target bundles: `{', '.join([k for k,v in target_bundles.items() if v]) or 'none'}`")
    lines.append('')
    lines.append('## Rollback actions')
    lines.append(f'- restored from quarantine: `{len(restored)}`')
    lines.append(f'- conflicting current files moved aside: `{len(conflicted)}`')
    lines.append(f'- managed files pruned after restore: `{len(pruned)}`')
    if conflict_dir is not None:
        lines.append(f'- conflict quarantine: `{conflict_dir}`')
    if prune_dir is not None:
        lines.append(f'- prune quarantine: `{prune_dir}`')
    lines.append('')
    lines.append('## Restored files')
    lines.extend([f'- {x}' for x in restored] or ['- none'])
    lines.append('')
    lines.append('## Conflicted current files')
    lines.extend([f'- {x}' for x in conflicted] or ['- none'])
    lines.append('')
    lines.append('## Pruned files after rollback')
    lines.extend([f'- {x}' for x in pruned] or ['- none'])
    lines.append('')
    lines.append('## Post-rollback validation')
    lines.append(markdown_report(repo, target_profile, target_bundles, validation))
    return '\n'.join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('--quarantine-dir')
    ap.add_argument('--target-profile', choices=['lean','standard','rigorous'])
    ap.add_argument('--include-research-agents', action='store_true')
    ap.add_argument('--include-doc-agents', action='store_true')
    ap.add_argument('--include-security-agents', action='store_true')
    ap.add_argument('--include-hooks', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--keep-current-managed', action='store_true', help='do not prune managed files that are outside the target state')
    ap.add_argument('--delete-pruned-managed', action='store_true', help='delete pruned managed files instead of quarantining them')
    ap.add_argument('--report-output')
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    qdir = Path(args.quarantine_dir).resolve() if args.quarantine_dir else latest_quarantine(repo)
    if qdir is None or not qdir.exists():
        print('No migration quarantine directory found. Use --quarantine-dir to point to a specific directory.')
        return 2
    metadata = load_metadata(qdir)
    target_profile, target_bundles = resolve_target(repo, args, metadata)
    payload_files = list_payload_files(qdir)
    print(f'Quarantine source: {qdir}')
    print(f'Target profile: {target_profile}')
    print(f"Target bundles: {', '.join([k for k,v in target_bundles.items() if v]) or 'none'}")
    print(f'Files available for restore: {len(payload_files)}')
    if not args.apply:
        print('Preview only. Re-run with --apply to perform the rollback.')
        return 0

    conflict_dir = quarantine_dir(repo, 'rollback-conflicts')
    restored, conflicted = restore_payload(repo, qdir, conflict_dir)

    prune_dir = None if args.delete_pruned_managed else quarantine_dir(repo, 'rollback-prune')
    pruned: List[str] = []
    if not args.keep_current_managed:
        pruned = prune_current_to_target(repo, target_profile, target_bundles, prune_dir)
        if args.delete_pruned_managed:
            prune_dir = None

    report = build_report(repo, qdir, target_profile, target_bundles, restored, conflicted, conflict_dir if conflicted else None, pruned, prune_dir if pruned and not args.delete_pruned_managed else None)
    if args.report_output:
        out = Path(args.report_output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding='utf-8')
        print(f'Wrote rollback report to {out}')

    validation = validate_root(repo, target_profile, target_bundles)
    remaining = sum(len(v) for v in validation.values())
    print(f'Restored files: {len(restored)}')
    print(f'Conflicted files moved aside: {len(conflicted)}')
    print(f'Pruned current managed files: {len(pruned)}')
    if remaining:
        print('Rollback completed but validation still reports issues.')
        return 1
    print('Rollback completed and validation passed for the target profile and bundles.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
