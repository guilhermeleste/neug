#!/usr/bin/env python3
"""Repair a scaffolded kit by restoring missing managed files and optionally pruning extras."""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from audit_existing_kit import markdown_report
from scaffold_agentic_kit import parse_args, scaffold
from validate_scaffold import (
    ALL_MANAGED_FILES,
    check_placeholders,
    consistency_issues,
    expected_files,
    find_unmanaged_within_managed_dirs,
    infer_bundles,
    infer_profile,
    partial_sets,
)


def as_bundles(ns) -> Dict[str, bool]:
    return {
        'research': ns.include_research_agents,
        'docs': ns.include_doc_agents,
        'security': ns.include_security_agents,
        'hooks': ns.include_hooks,
    }


def infer_or_default(repo: Path, profile: str | None, bundles: Dict[str, bool]) -> tuple[str, Dict[str, bool]]:
    p = profile or infer_profile(repo) or 'standard'
    if not any(bundles.values()):
        inferred = infer_bundles(repo)
        if any(inferred.values()):
            bundles = inferred
    return p, bundles


def default_quarantine_dir(repo: Path, label: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    return repo / '.agentic-quarantine' / f'{label}-{stamp}'


def prune_managed(repo: Path, expected: set[str], quarantine_dir: Path | None = None) -> List[str]:
    removed: List[str] = []
    for rel in sorted(ALL_MANAGED_FILES - expected):
        path = repo / rel
        if path.exists() and path.is_file():
            if quarantine_dir is not None:
                dest = quarantine_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(path), str(dest))
            else:
                path.unlink()
            removed.append(rel)
    for d in sorted({(repo / rel).parent for rel in removed}, key=lambda x: len(x.parts), reverse=True):
        cur = d
        while cur != repo and cur.exists():
            try:
                cur.rmdir()
            except OSError:
                break
            cur = cur.parent
    return removed


def rewrite_placeholders(repo: Path, replacements: Dict[str, str]) -> List[str]:
    touched: List[str] = []
    for path in repo.rglob('*'):
        if not path.is_file() or path.suffix.lower() in {'.png', '.jpg', '.jpeg', '.svg', '.ico', '.pyc'}:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except Exception:
            continue
        new = text
        for key, value in replacements.items():
            new = new.replace(f'{{{{{key}}}}}', value)
        if new != text:
            path.write_text(new, encoding='utf-8')
            touched.append(str(path.relative_to(repo)))
    return touched


def build_report(repo: Path, profile: str, bundles: Dict[str, bool]) -> str:
    report = {
        'missing': [rel for rel in expected_files(profile, bundles) if not (repo / rel).exists()],
        'placeholders': check_placeholders(repo),
        'partials': [
            f"{name}: {present}/{total} present; missing {', '.join(missing[:6])}{' ...' if len(missing) > 6 else ''}"
            for name, (present, total, missing) in partial_sets(repo).items()
        ],
        'extras': find_unmanaged_within_managed_dirs(repo),
        'consistency': consistency_issues(repo, profile, bundles),
    }
    return markdown_report(repo, profile, bundles, report)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('--profile', choices=['lean', 'standard', 'rigorous'])
    ap.add_argument('--include-research-agents', action='store_true')
    ap.add_argument('--include-doc-agents', action='store_true')
    ap.add_argument('--include-security-agents', action='store_true')
    ap.add_argument('--include-hooks', action='store_true')
    ap.add_argument('--project-name')
    ap.add_argument('--backend-glob', default='src/**')
    ap.add_argument('--test-glob', default='tests/**')
    ap.add_argument('--prune-managed-extras', action='store_true')
    ap.add_argument('--quarantine-pruned-managed-extras', action='store_true')
    ap.add_argument('--quarantine-dir')
    ap.add_argument('--rewrite-placeholders', action='store_true')
    ap.add_argument('--report-output')
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    bundles = as_bundles(args)
    profile, bundles = infer_or_default(repo, args.profile, bundles)

    scaffold_argv = [
        str(repo), '--profile', profile,
        '--project-name', args.project_name or repo.name.replace('-', ' ').replace('_', ' '),
        '--backend-glob', args.backend_glob,
        '--test-glob', args.test_glob,
    ]
    if bundles['research']:
        scaffold_argv.append('--include-research-agents')
    if bundles['docs']:
        scaffold_argv.append('--include-doc-agents')
    if bundles['security']:
        scaffold_argv.append('--include-security-agents')
    if bundles['hooks']:
        scaffold_argv.append('--include-hooks')
    target_root, force, resolved_profile, include_hooks, include_research, include_docs, include_security, replacements = parse_args(scaffold_argv)
    created, skipped = scaffold(target_root, replacements, resolved_profile, force=False, include_hooks=include_hooks, include_research_agents=include_research, include_doc_agents=include_docs, include_security_agents=include_security)

    rewritten: List[str] = []
    if args.rewrite_placeholders:
        rewritten = rewrite_placeholders(repo, replacements)

    pruned: List[str] = []
    quarantine_dir: Path | None = None
    if args.prune_managed_extras:
        if args.quarantine_pruned_managed_extras:
            quarantine_dir = Path(args.quarantine_dir).resolve() if args.quarantine_dir else default_quarantine_dir(repo, 'repair-prune')
        pruned = prune_managed(repo, set(expected_files(profile, bundles)), quarantine_dir=quarantine_dir)

    report_md = build_report(repo, profile, bundles)
    if args.report_output:
        out = Path(args.report_output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report_md, encoding='utf-8')
        print(f'Wrote repair report to {out}')
    print(f'Profile: {profile}')
    print(f"Bundles: {', '.join([k for k, v in bundles.items() if v]) or 'none'}")
    print(f'Restored missing files: {len(created)}')
    for rel in created:
        print(f'RESTORE {rel}')
    print(f'Preserved existing files: {len(skipped)}')
    print(f'Rewritten placeholders: {len(rewritten)}')
    for rel in rewritten:
        print(f'REWRITE {rel}')
    print(f'Pruned managed extras: {len(pruned)}')
    for rel in pruned:
        action = 'QUARANTINE' if quarantine_dir is not None else 'PRUNE'
        print(f'{action:<10} {rel}')
    if quarantine_dir is not None:
        print(f'Quarantine directory: {quarantine_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
