#!/usr/bin/env python3
"""Validate a scaffolded agentic kit for profile and bundle consistency."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

BASE_FILES = [
    '.github/copilot-instructions.md',
    '.github/agents/developer.agent.md',
    '.github/agents/test-engineer.agent.md',
    '.github/instructions/backend.instructions.md',
    '.github/instructions/testing.instructions.md',
    '.github/instructions/review.instructions.md',
    '.github/prompts/focused-backend-change.prompt.md',
    '.github/prompts/generate-backend-tests.prompt.md',
    '.github/prompts/review-ai-patch.prompt.md',
    'docs/agentic-workflow/README.md',
    'docs/agentic-workflow/ONBOARDING.md',
    'docs/agentic-workflow/ARCHITECTURE.md',
    'docs/agentic-workflow/SKILL_ROUTING.md',
    'docs/agentic-workflow/00_goal.md',
    'docs/agentic-workflow/06_test_spec.md',
    'docs/agentic-workflow/07_execution_log.md',
    'docs/agentic-workflow/10_closure_report.md',
]
STANDARD_FILES = [
    '.github/agents/planner.agent.md',
    '.github/prompts/plan-backend-change.prompt.md',
    '.github/prompts/implement-from-plan.prompt.md',
    'docs/agentic-workflow/02_plan.md',
    'docs/agentic-workflow/04_plan_frozen.md',
]
RIGOROUS_FILES = [
    '.github/agents/context-researcher.agent.md',
    '.github/agents/architecture-synthesizer.agent.md',
    '.github/agents/critical-judge.agent.md',
    '.github/agents/plan-verifier.agent.md',
    '.github/prompts/redteam-plan.prompt.md',
    '.github/prompts/check-plan-conformance.prompt.md',
    '.github/prompts/synthesize-architecture.prompt.md',
    'docs/agentic-workflow/01_context_pack.md',
    'docs/agentic-workflow/01c_architecture_overview.md',
    'docs/agentic-workflow/03_plan_redteam.md',
    'docs/agentic-workflow/08_conformance_report.md',
    'docs/agentic-workflow/09_patch_redteam.md',
]
RESEARCH_FILES = [
    '.github/agents/official-docs-researcher.agent.md',
    '.github/agents/academic-literature-researcher.agent.md',
    '.github/agents/research-technical-spike.agent.md',
    '.github/agents/specification.agent.md',
    '.github/agents/doublecheck.agent.md',
    '.github/prompts/research-technical-spike.prompt.md',
    '.github/prompts/write-or-update-specification.prompt.md',
    '.github/prompts/doublecheck-claims.prompt.md',
    'docs/agentic-workflow/01a_official_docs_memo.md',
    'docs/agentic-workflow/01b_academic_memo.md',
    'docs/agentic-workflow/01d_technical_spike.md',
    'spec/spec-task.md',
]
DOC_FILES = [
    '.github/agents/gem-documentation-writer.agent.md',
    '.github/agents/technical-content-evaluator.agent.md',
    '.github/prompts/review-specification.prompt.md',
    '.github/prompts/review-adr-or-doc.prompt.md',
    '.github/prompts/update-parity-documentation.prompt.md',
    'docs/adr/ADR-template.md',
    'docs/agentic-workflow/02b_spec_review.md',
    'docs/agentic-workflow/10a_documentation_closeout.md',
    'docs/agentic-workflow/10b_documentation_review.md',
]
SECURITY_FILES = [
    '.github/agents/security-review-lead.agent.md',
    '.github/agents/security-threat-modeler.agent.md',
    '.github/agents/security-api-reviewer.agent.md',
    '.github/agents/security-web-reviewer.agent.md',
    '.github/agents/security-asvs-governor.agent.md',
    '.github/prompts/security-threat-model.prompt.md',
    '.github/prompts/review-api-surface-security.prompt.md',
    '.github/prompts/review-web-surface-security.prompt.md',
    '.github/prompts/build-asvs-evidence-matrix.prompt.md',
    'docs/agentic-workflow/01e_security_scope.md',
    'docs/agentic-workflow/01f_threat_register.md',
    'docs/agentic-workflow/02c_security_requirements.md',
    'docs/agentic-workflow/03c_security_redteam.md',
    'docs/agentic-workflow/08c_security_conformance_report.md',
    'docs/agentic-workflow/10c_security_evidence_matrix.md',
    'docs/agentic-workflow/10d_security_release_gates.md',
]
HOOK_FILES = [
    '.github/hooks/settings.example.json',
    '.github/hooks/scripts/session-banner.sh',
    '.github/hooks/scripts/log-prompt.sh',
    '.github/hooks/scripts/pre-tool-policy.sh',
]

PROFILE_FILES: Dict[str, List[str]] = {
    'lean': list(BASE_FILES),
    'standard': list(BASE_FILES + STANDARD_FILES),
    'rigorous': list(BASE_FILES + STANDARD_FILES + RIGOROUS_FILES),
}
BUNDLE_FILES: Dict[str, List[str]] = {
    'research': list(RESEARCH_FILES),
    'docs': list(DOC_FILES),
    'security': list(SECURITY_FILES),
    'hooks': list(HOOK_FILES),
}
MANAGED_DIR_PREFIXES = [
    '.github/agents/',
    '.github/prompts/',
    '.github/instructions/',
    '.github/hooks/',
    'docs/agentic-workflow/',
    'docs/adr/',
    'spec/',
]
OPTIONAL_MANAGED_OUTPUTS = {'docs/agentic-workflow/KIT_DRIFT_REPORT.md', 'docs/agentic-workflow/PROFILE_MIGRATION_REPORT.md', 'docs/agentic-workflow/ROLLBACK_REPORT.md'}
ALL_MANAGED_FILES = set(PROFILE_FILES['rigorous']) | OPTIONAL_MANAGED_OUTPUTS
for files in BUNDLE_FILES.values():
    ALL_MANAGED_FILES.update(files)


def expected_files(profile: str, bundles: Dict[str, bool]) -> List[str]:
    files = list(PROFILE_FILES[profile])
    for name, enabled in bundles.items():
        if enabled:
            files += BUNDLE_FILES[name]
    return files


def check_missing(root: Path, rels: List[str]) -> List[str]:
    return [rel for rel in rels if not (root / rel).exists()]


def find_existing(root: Path, rels: List[str]) -> List[str]:
    return [rel for rel in rels if (root / rel).exists()]


def check_placeholders(root: Path) -> List[str]:
    bad: List[str] = []
    for path in root.rglob('*'):
        if path.is_file() and path.suffix.lower() not in {'.png', '.jpg', '.jpeg', '.svg', '.ico', '.pyc'}:
            try:
                text = path.read_text(encoding='utf-8')
            except Exception:
                continue
            if '{{' in text or '}}' in text:
                bad.append(str(path.relative_to(root)))
    return bad


def infer_profile(root: Path) -> str | None:
    if find_existing(root, RIGOROUS_FILES):
        return 'rigorous'
    if find_existing(root, STANDARD_FILES):
        return 'standard'
    if find_existing(root, BASE_FILES):
        return 'lean'
    return None


def infer_bundles(root: Path) -> Dict[str, bool]:
    return {name: bool(find_existing(root, files)) for name, files in BUNDLE_FILES.items()}


def partial_sets(root: Path) -> Dict[str, Tuple[int, int, List[str]]]:
    results: Dict[str, Tuple[int, int, List[str]]] = {}
    for name, files in BUNDLE_FILES.items():
        existing = find_existing(root, files)
        if 0 < len(existing) < len(files):
            results[name] = (len(existing), len(files), sorted(set(files) - set(existing)))
    for name in ('standard', 'rigorous'):
        files = STANDARD_FILES if name == 'standard' else RIGOROUS_FILES
        existing = find_existing(root, files)
        if 0 < len(existing) < len(files):
            results[name] = (len(existing), len(files), sorted(set(files) - set(existing)))
    return results


def find_unmanaged_within_managed_dirs(root: Path) -> List[str]:
    extras: List[str] = []
    for path in root.rglob('*'):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        if any(rel.startswith(prefix) for prefix in MANAGED_DIR_PREFIXES) and rel not in ALL_MANAGED_FILES:
            extras.append(rel)
    return sorted(extras)


def consistency_issues(root: Path, profile: str, bundles: Dict[str, bool]) -> List[str]:
    issues: List[str] = []
    # Core role dependencies
    if (root / '.github/agents/planner.agent.md').exists():
        for rel in ['.github/prompts/plan-backend-change.prompt.md', 'docs/agentic-workflow/02_plan.md', 'docs/agentic-workflow/04_plan_frozen.md']:
            if not (root / rel).exists():
                issues.append(f'planner exists but required artifact is missing: {rel}')
    if (root / '.github/agents/test-engineer.agent.md').exists() and not (root / 'docs/agentic-workflow/06_test_spec.md').exists():
        issues.append('test-engineer exists but docs/agentic-workflow/06_test_spec.md is missing')
    if profile == 'rigorous':
        for rel in ['docs/agentic-workflow/01_context_pack.md', 'docs/agentic-workflow/01c_architecture_overview.md', 'docs/agentic-workflow/08_conformance_report.md']:
            if not (root / rel).exists():
                issues.append(f'rigorous profile selected but artifact is missing: {rel}')
    if bundles.get('docs'):
        for rel in ['.github/prompts/review-adr-or-doc.prompt.md', 'docs/agentic-workflow/10a_documentation_closeout.md']:
            if not (root / rel).exists():
                issues.append(f'documentation bundle selected but artifact is missing: {rel}')
    if bundles.get('research'):
        for rel in ['spec/spec-task.md', '.github/prompts/doublecheck-claims.prompt.md']:
            if not (root / rel).exists():
                issues.append(f'research bundle selected but artifact is missing: {rel}')
    if bundles.get('security'):
        for rel in ['docs/agentic-workflow/01e_security_scope.md', 'docs/agentic-workflow/10d_security_release_gates.md']:
            if not (root / rel).exists():
                issues.append(f'security bundle selected but artifact is missing: {rel}')
    if bundles.get('hooks') and not (root / '.github/hooks/settings.example.json').exists():
        issues.append('hooks bundle selected but .github/hooks/settings.example.json is missing')
    return issues


def validate_root(root: Path, profile: str, bundles: Dict[str, bool]) -> Dict[str, List[str]]:
    expected = expected_files(profile, bundles)
    return {
        'missing': check_missing(root, expected),
        'placeholders': check_placeholders(root),
        'partials': [
            f"{name}: {present}/{total} present; missing {', '.join(missing[:6])}{' ...' if len(missing) > 6 else ''}"
            for name, (present, total, missing) in partial_sets(root).items()
        ],
        'extras': find_unmanaged_within_managed_dirs(root),
        'consistency': consistency_issues(root, profile, bundles),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('--profile', choices=['lean', 'standard', 'rigorous'], default='standard')
    ap.add_argument('--include-research-agents', action='store_true')
    ap.add_argument('--include-doc-agents', action='store_true')
    ap.add_argument('--include-security-agents', action='store_true')
    ap.add_argument('--include-hooks', action='store_true')
    args = ap.parse_args()
    root = Path(args.repo).resolve()
    bundles = {
        'research': args.include_research_agents,
        'docs': args.include_doc_agents,
        'security': args.include_security_agents,
        'hooks': args.include_hooks,
    }
    report = validate_root(root, args.profile, bundles)
    has_errors = False
    for key, title in [
        ('missing', 'Missing files'),
        ('placeholders', 'Unresolved placeholders'),
        ('partials', 'Partial bundles or profiles'),
        ('extras', 'Unmanaged files in managed directories'),
        ('consistency', 'Consistency issues'),
    ]:
        items = report[key]
        if items:
            has_errors = True
            print(f'{title}:')
            for rel in items:
                print(f'  - {rel}')
    if has_errors:
        return 1
    print('Scaffold is valid for the requested profile and bundles.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
