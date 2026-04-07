#!/usr/bin/env python3
"""Audit an existing scaffolded kit and emit a markdown drift report."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

from validate_scaffold import (
    BUNDLE_FILES,
    PROFILE_FILES,
    check_placeholders,
    consistency_issues,
    expected_files,
    find_existing,
    find_unmanaged_within_managed_dirs,
    infer_bundles,
    infer_profile,
    partial_sets,
)


def recommend(profile: str | None, bundles: Dict[str, bool], report: Dict[str, List[str]]) -> List[str]:
    recs: List[str] = []
    if profile is None:
        recs.append('no recognizable kit profile was detected; scaffold lean or standard before trying to harden the repository workflow')
        return recs
    if report['missing']:
        recs.append('repair missing expected files before adding new bundles or roles; use scripts/repair_kit.py when the target profile is known')
    if report['placeholders']:
        recs.append('resolve remaining placeholders before using the workflow in a real repository')
    if report['partials']:
        recs.append('collapse partial bundles back to a complete enabled bundle or remove the orphaned files; run scripts/profile_diff.py before changing profile posture')
    if report['consistency']:
        recs.append('fix consistency violations before trusting the generated process documents')
    if report['extras']:
        recs.append('review unmanaged files inside managed directories and either merge, quarantine, delete, or migrate them out of the active kit')
    if profile == 'rigorous' and not report['partials'] and not report['consistency']:
        recs.append('consider de-escalating to standard if strict-governance artifacts are rarely used in real tasks; inspect the delta with scripts/profile_diff.py before applying scripts/migrate_profile.py')
    if profile == 'lean' and bundles.get('security'):
        recs.append('security bundle on lean is unusual; consider standard or rigorous if security review is frequent')
    if bundles.get('docs') and not bundles.get('research'):
        recs.append('documentation review without research is acceptable, but specification-heavy repositories often benefit from the research bundle too')
    if not any(bundles.values()):
        recs.append('stay bundle-free unless repeated repository pain justifies research, docs, security, or hooks')
    return recs


def markdown_report(repo: Path, profile: str | None, bundles: Dict[str, bool], report: Dict[str, List[str]]) -> str:
    detected_profile = profile or 'none'
    enabled_bundles = [name for name, enabled in bundles.items() if enabled]
    expected = expected_files(profile or 'lean', bundles) if profile else []
    existing_expected = find_existing(repo, expected) if expected else []
    coverage = f"{len(existing_expected)}/{len(expected)}" if expected else '0/0'
    lines: List[str] = []
    lines.append('# Kit drift report')
    lines.append('')
    lines.append('## Detected state')
    lines.append(f'- repository: `{repo}`')
    lines.append(f'- inferred profile: `{detected_profile}`')
    lines.append(f"- inferred bundles: `{', '.join(enabled_bundles) if enabled_bundles else 'none'}`")
    lines.append(f'- expected-file coverage for inferred state: `{coverage}`')
    lines.append('')
    for key, title in [
        ('missing', 'Missing expected files'),
        ('placeholders', 'Unresolved placeholders'),
        ('partials', 'Partial bundles or profiles'),
        ('consistency', 'Consistency issues'),
        ('extras', 'Unmanaged files in managed directories'),
    ]:
        lines.append(f'## {title}')
        items = report[key]
        if items:
            lines.extend([f'- {item}' for item in items])
        else:
            lines.append('- none')
        lines.append('')
    lines.append('## Recommendations')
    recs = recommend(profile, bundles, report)
    lines.extend([f'- {rec}' for rec in recs] or ['- no corrective action recommended'])
    lines.append('')
    lines.append('## Bundle coverage')
    for name, files in BUNDLE_FILES.items():
        existing = len(find_existing(repo, files))
        lines.append(f'- {name}: `{existing}/{len(files)}`')
    lines.append('')
    lines.append('## Profile markers')
    for name, files in PROFILE_FILES.items():
        existing = len(find_existing(repo, files))
        lines.append(f'- {name}: `{existing}/{len(files)}`')
    lines.append('')
    return '\n'.join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('--output', help='optional markdown output path')
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    profile = infer_profile(repo)
    bundles = infer_bundles(repo)
    if profile is None:
        report = {
            'missing': [],
            'placeholders': check_placeholders(repo),
            'partials': [
                f"{name}: {present}/{total} present; missing {', '.join(missing[:6])}{' ...' if len(missing) > 6 else ''}"
                for name, (present, total, missing) in partial_sets(repo).items()
            ],
            'extras': find_unmanaged_within_managed_dirs(repo),
            'consistency': [],
        }
    else:
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
    md = markdown_report(repo, profile, bundles, report)
    if args.output:
        out = Path(args.output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding='utf-8')
        print(f'Wrote audit report to {out}')
    else:
        print(md)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
