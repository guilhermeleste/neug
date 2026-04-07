#!/usr/bin/env python3
"""Migrate a scaffolded kit between profiles and bundle sets with optional quarantine."""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from audit_existing_kit import markdown_report
from profile_diff import summarize
from scaffold_agentic_kit import parse_args, scaffold
from validate_scaffold import expected_files, infer_bundles, infer_profile, validate_root


def default_quarantine_dir(repo: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    return repo / '.agentic-quarantine' / f'profile-migration-{stamp}'




def write_metadata(quarantine_dir: Path, from_profile: str, from_bundles: Dict[str, bool], to_profile: str, to_bundles: Dict[str, bool], removed: List[str]) -> None:
    quarantine_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        'kind': 'profile-migration',
        'from_profile': from_profile,
        'from_bundles': from_bundles,
        'to_profile': to_profile,
        'to_bundles': to_bundles,
        'removed': removed,
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
    }
    (quarantine_dir / 'metadata.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')
def flags_from_ns(ns, prefix: str) -> Dict[str, bool]:
    return {
        'research': getattr(ns, f'{prefix}_include_research_agents'),
        'docs': getattr(ns, f'{prefix}_include_doc_agents'),
        'security': getattr(ns, f'{prefix}_include_security_agents'),
        'hooks': getattr(ns, f'{prefix}_include_hooks'),
    }


def resolve_from(repo: Path, ns) -> tuple[str, Dict[str, bool]]:
    profile = ns.from_profile or infer_profile(repo) or 'standard'
    bundles = flags_from_ns(ns, 'from')
    if not any(bundles.values()):
        bundles = infer_bundles(repo)
    return profile, bundles


def resolve_to(ns, from_bundles: Dict[str, bool]) -> tuple[str, Dict[str, bool]]:
    profile = ns.to_profile
    bundles = flags_from_ns(ns, 'to')
    if not any(bundles.values()) and ns.copy_bundles:
        bundles = dict(from_bundles)
    return profile, bundles


def remove_or_quarantine(repo: Path, rels: List[str], quarantine_dir: Path | None) -> List[str]:
    moved: List[str] = []
    for rel in rels:
        path = repo / rel
        if not path.exists() or not path.is_file():
            continue
        if quarantine_dir is not None:
            dest = quarantine_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest))
        else:
            path.unlink()
        moved.append(rel)
    for d in sorted({(repo / rel).parent for rel in moved}, key=lambda x: len(x.parts), reverse=True):
        cur = d
        while cur != repo and cur.exists():
            try:
                cur.rmdir()
            except OSError:
                break
            cur = cur.parent
    return moved


def build_report(repo: Path, profile: str, bundles: Dict[str, bool], from_profile: str, from_bundles: Dict[str, bool], removed: List[str], created_count: int, quarantine_dir: Path | None) -> str:
    validation = validate_root(repo, profile, bundles)
    lines: List[str] = []
    lines.append(summarize(from_profile, from_bundles, profile, bundles))
    lines.append('')
    lines.append('## Migration actions')
    lines.append(f'- created or restored target files: `{created_count}`')
    lines.append(f'- removed from active kit: `{len(removed)}`')
    if quarantine_dir is not None:
        lines.append(f'- quarantine directory: `{quarantine_dir}`')
        lines.append(f'- rollback hint: `python scripts/rollback_migration.py {repo} --apply --quarantine-dir {quarantine_dir}`')
    lines.append('')
    lines.append('## Removed or quarantined files')
    lines.extend([f'- {x}' for x in removed] or ['- none'])
    lines.append('')
    lines.append('## Post-migration validation')
    lines.append(markdown_report(repo, profile, bundles, validation))
    return '\n'.join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('--from-profile', choices=['lean', 'standard', 'rigorous'])
    ap.add_argument('--to-profile', choices=['lean', 'standard', 'rigorous'], required=True)
    for side in ('from', 'to'):
        ap.add_argument(f'--{side}-include-research-agents', action='store_true')
        ap.add_argument(f'--{side}-include-doc-agents', action='store_true')
        ap.add_argument(f'--{side}-include-security-agents', action='store_true')
        ap.add_argument(f'--{side}-include-hooks', action='store_true')
    ap.add_argument('--copy-bundles', action='store_true', help='if no to-bundle flags are given, reuse the inferred current bundle set')
    ap.add_argument('--apply', action='store_true', help='perform the migration; without this flag, only print the diff')
    ap.add_argument('--keep-removed-managed', action='store_true', help='keep files that leave the active kit')
    ap.add_argument('--delete-removed-managed', action='store_true', help='delete removed managed files instead of quarantining them')
    ap.add_argument('--quarantine-dir')
    ap.add_argument('--project-name')
    ap.add_argument('--backend-glob', default='src/**')
    ap.add_argument('--test-glob', default='tests/**')
    ap.add_argument('--report-output')
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    from_profile, from_bundles = resolve_from(repo, args)
    to_profile, to_bundles = resolve_to(args, from_bundles)
    summary = summarize(from_profile, from_bundles, to_profile, to_bundles)
    if not args.apply:
        print(summary)
        return 0

    scaffold_argv = [
        str(repo), '--profile', to_profile,
        '--project-name', args.project_name or repo.name.replace('-', ' ').replace('_', ' '),
        '--backend-glob', args.backend_glob,
        '--test-glob', args.test_glob,
    ]
    if to_bundles['research']:
        scaffold_argv.append('--include-research-agents')
    if to_bundles['docs']:
        scaffold_argv.append('--include-doc-agents')
    if to_bundles['security']:
        scaffold_argv.append('--include-security-agents')
    if to_bundles['hooks']:
        scaffold_argv.append('--include-hooks')
    target_root, force, resolved_profile, include_hooks, include_research, include_docs, include_security, replacements = parse_args(scaffold_argv)
    created, skipped = scaffold(target_root, replacements, resolved_profile, force=False, include_hooks=include_hooks, include_research_agents=include_research, include_doc_agents=include_docs, include_security_agents=include_security)

    removed_candidates = sorted(set(expected_files(from_profile, from_bundles)) - set(expected_files(to_profile, to_bundles)))
    quarantine_dir: Path | None = None
    removed: List[str] = []
    if not args.keep_removed_managed:
        quarantine_dir = None if args.delete_removed_managed else (Path(args.quarantine_dir).resolve() if args.quarantine_dir else default_quarantine_dir(repo))
        removed = remove_or_quarantine(repo, removed_candidates, quarantine_dir)
        if quarantine_dir is not None and removed:
            write_metadata(quarantine_dir, from_profile, from_bundles, to_profile, to_bundles, removed)

    report = build_report(repo, to_profile, to_bundles, from_profile, from_bundles, removed, len(created), quarantine_dir)
    if args.report_output:
        out = Path(args.report_output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding='utf-8')
        print(f'Wrote migration report to {out}')

    print(f'Migrated profile: {from_profile} -> {to_profile}')
    print(f"From bundles: {', '.join([k for k, v in from_bundles.items() if v]) or 'none'}")
    print(f"To bundles: {', '.join([k for k, v in to_bundles.items() if v]) or 'none'}")
    print(f'Created or restored target files: {len(created)}')
    print(f'Removed from active kit: {len(removed)}')
    if quarantine_dir is not None:
        print(f'Quarantine directory: {quarantine_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
