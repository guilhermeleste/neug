#!/usr/bin/env python3
"""Copy the bundled agentic kit template into a target repository.

Profiles:
    lean     -> smallest default: developer + test-engineer + minimal workflow docs
    standard -> lean + planner and formal plan artifacts
    rigorous -> standard + strict governance roles and documents
"""
from __future__ import annotations

import sys
from pathlib import Path

TEMPLATE_ROOT = Path(__file__).resolve().parents[1] / "assets" / "kit-template"
OPTIONAL_STANDARD_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-standard"
OPTIONAL_GOVERNANCE_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-strict-governance"
OPTIONAL_HOOKS_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-hooks"
OPTIONAL_RESEARCH_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-research"
OPTIONAL_DOC_AGENTS_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-addons"
OPTIONAL_SECURITY_ROOT = Path(__file__).resolve().parents[1] / "assets" / "optional-security"
VALID_PROFILES = {"lean", "standard", "rigorous"}


def iter_template_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            yield path


def render_destination(template_file: Path, target_root: Path, template_root: Path) -> Path:
    rel = template_file.relative_to(template_root)
    parts = [p[:-9] if p.endswith('.template') else p for p in rel.parts]
    return target_root.joinpath(*parts)


def parse_args(argv: list[str]):
    if not argv:
        raise ValueError('Usage: scaffold_agentic_kit.py /path/to/repo [--force] [--profile lean|standard|rigorous] [--include-research-agents] [--include-doc-agents] [--include-security-agents] [--include-hooks] [--project-name NAME] [--backend-glob GLOB] [--test-glob GLOB]')

    target = Path(argv[0]).resolve()
    force = False
    include_hooks = False
    include_research_agents = False
    include_doc_agents = False
    include_security_agents = False
    profile = 'standard'
    project_name = None
    backend_glob = 'src/**'
    test_glob = 'tests/**'

    i = 1
    while i < len(argv):
        arg = argv[i]
        if arg == '--force':
            force = True
            i += 1
        elif arg == '--include-hooks':
            include_hooks = True
            i += 1
        elif arg == '--include-research-agents':
            include_research_agents = True
            i += 1
        elif arg == '--include-doc-agents':
            include_doc_agents = True
            i += 1
        elif arg == '--include-security-agents':
            include_security_agents = True
            i += 1
        elif arg == '--profile' and i + 1 < len(argv):
            profile = argv[i + 1].strip().lower()
            if profile not in VALID_PROFILES:
                raise ValueError(f'Unknown profile: {profile}. Use one of: lean, standard, rigorous')
            i += 2
        elif arg == '--project-name' and i + 1 < len(argv):
            project_name = argv[i + 1]
            i += 2
        elif arg == '--backend-glob' and i + 1 < len(argv):
            backend_glob = argv[i + 1]
            i += 2
        elif arg == '--test-glob' and i + 1 < len(argv):
            test_glob = argv[i + 1]
            i += 2
        else:
            raise ValueError(f'Unknown or incomplete argument: {arg}')

    if project_name is None:
        project_name = target.name.replace('-', ' ').replace('_', ' ').strip() or target.name

    # dependency promotion
    if profile == 'lean' and (include_research_agents or include_security_agents):
        profile = 'rigorous'
    elif profile == 'lean' and include_doc_agents:
        profile = 'standard'
    elif profile == 'standard' and include_security_agents:
        profile = 'rigorous'

    replacements = {
        'PROJECT_NAME': project_name,
        'BACKEND_GLOB': backend_glob,
        'TEST_GLOB': test_glob,
        'PROFILE': profile,
        'STRICT_GOVERNANCE': 'enabled' if profile == 'rigorous' else 'disabled',
        'ROLE': '',
        'TRIGGER': '',
        'NOTE': '',
    }
    return target, force, profile, include_hooks, include_research_agents, include_doc_agents, include_security_agents, replacements


def render_text(content: str, replacements: dict[str, str]) -> str:
    for key, value in replacements.items():
        content = content.replace(f'{{{{{key}}}}}', value)
    return content


def copy_tree(template_root: Path, target_root: Path, replacements: dict[str, str], force: bool = False):
    created = []
    skipped = []
    for source in iter_template_files(template_root):
        destination = render_destination(source, target_root, template_root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not force:
            skipped.append(destination)
            continue
        text = source.read_text(encoding='utf-8')
        destination.write_text(render_text(text, replacements), encoding='utf-8')
        if source.stat().st_mode & 0o111:
            destination.chmod(destination.stat().st_mode | 0o755)
        created.append(destination)
    return created, skipped


def scaffold(target_root: Path, replacements: dict[str, str], profile: str, force: bool = False, include_hooks: bool = False, include_research_agents: bool = False, include_doc_agents: bool = False, include_security_agents: bool = False):
    created, skipped = copy_tree(TEMPLATE_ROOT, target_root, replacements, force=force)
    if profile in {'standard', 'rigorous'}:
        c, s = copy_tree(OPTIONAL_STANDARD_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    if profile == 'rigorous':
        c, s = copy_tree(OPTIONAL_GOVERNANCE_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    if include_research_agents:
        c, s = copy_tree(OPTIONAL_RESEARCH_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    if include_doc_agents:
        c, s = copy_tree(OPTIONAL_DOC_AGENTS_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    if include_security_agents:
        c, s = copy_tree(OPTIONAL_SECURITY_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    if include_hooks:
        c, s = copy_tree(OPTIONAL_HOOKS_ROOT, target_root, replacements, force=force)
        created.extend(c); skipped.extend(s)
    return created, skipped


def main() -> int:
    try:
        target_root, force, profile, include_hooks, include_research_agents, include_doc_agents, include_security_agents, replacements = parse_args(sys.argv[1:])
    except ValueError as exc:
        print(str(exc))
        return 1
    if not target_root.exists() or not target_root.is_dir():
        print(f'Target directory does not exist or is not a directory: {target_root}')
        return 2
    created, skipped = scaffold(target_root, replacements, profile, force=force, include_hooks=include_hooks, include_research_agents=include_research_agents, include_doc_agents=include_doc_agents, include_security_agents=include_security_agents)
    print(f'Profile: {profile}')
    print(f'Created {len(created)} file(s).')
    for p in created:
        print(f'CREATE {p}')
    print(f'Skipped {len(skipped)} existing file(s).')
    for p in skipped:
        print(f'SKIP   {p}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
