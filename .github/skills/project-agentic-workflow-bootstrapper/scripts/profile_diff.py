#!/usr/bin/env python3
"""Show file-level differences between workflow profiles and bundle sets."""
from __future__ import annotations

import argparse
from typing import Dict, List

from validate_scaffold import expected_files


def bundle_flags(ns, prefix: str) -> Dict[str, bool]:
    return {
        'research': getattr(ns, f'{prefix}_include_research_agents'),
        'docs': getattr(ns, f'{prefix}_include_doc_agents'),
        'security': getattr(ns, f'{prefix}_include_security_agents'),
        'hooks': getattr(ns, f'{prefix}_include_hooks'),
    }


def summarize(from_profile: str, from_bundles: Dict[str, bool], to_profile: str, to_bundles: Dict[str, bool]) -> str:
    from_set = set(expected_files(from_profile, from_bundles))
    to_set = set(expected_files(to_profile, to_bundles))
    added = sorted(to_set - from_set)
    removed = sorted(from_set - to_set)
    kept = sorted(from_set & to_set)

    lines: List[str] = []
    lines.append('# Profile diff')
    lines.append('')
    lines.append('## From')
    lines.append(f'- profile: `{from_profile}`')
    lines.append(f"- bundles: `{', '.join([k for k, v in from_bundles.items() if v]) or 'none'}`")
    lines.append('')
    lines.append('## To')
    lines.append(f'- profile: `{to_profile}`')
    lines.append(f"- bundles: `{', '.join([k for k, v in to_bundles.items() if v]) or 'none'}`")
    lines.append('')
    lines.append('## Summary')
    lines.append(f'- files added: `{len(added)}`')
    lines.append(f'- files removed: `{len(removed)}`')
    lines.append(f'- files unchanged: `{len(kept)}`')
    lines.append('')
    lines.append('## Added files')
    lines.extend([f'- {x}' for x in added] or ['- none'])
    lines.append('')
    lines.append('## Removed files')
    lines.extend([f'- {x}' for x in removed] or ['- none'])
    lines.append('')
    lines.append('## Interpretation')
    if len(removed) > len(added):
        lines.append('- this migration simplifies the kit; audit local customizations before pruning managed files')
    elif len(added) > len(removed):
        lines.append('- this migration hardens or expands the kit; verify that the team will actually use the added roles and documents')
    else:
        lines.append('- this migration is mostly lateral; review whether the role or bundle change materially improves the workflow')
    return '\n'.join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-profile', choices=['lean', 'standard', 'rigorous'], required=True)
    ap.add_argument('--to-profile', choices=['lean', 'standard', 'rigorous'], required=True)
    for side in ('from', 'to'):
        ap.add_argument(f'--{side}-include-research-agents', action='store_true')
        ap.add_argument(f'--{side}-include-doc-agents', action='store_true')
        ap.add_argument(f'--{side}-include-security-agents', action='store_true')
        ap.add_argument(f'--{side}-include-hooks', action='store_true')
    args = ap.parse_args()
    print(summarize(args.from_profile, bundle_flags(args, 'from'), args.to_profile, bundle_flags(args, 'to')))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
