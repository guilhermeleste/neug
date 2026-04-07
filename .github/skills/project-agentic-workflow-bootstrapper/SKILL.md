---
name: project-agentic-workflow-bootstrapper
description: "inspect a software project, its repository structure, existing workflow files, and relevant skills, then propose and generate or update a repository-specific copilot workflow kit. use when chatgpt needs to bootstrap, audit, simplify, harden, or revise a github copilot workflow for backend and testing work. prefer a profile-based design: lean for small teams, standard for plan-driven work, and rigorous only when strict governance is justified. add research, documentation, security, or hooks bundles only when the repository has a concrete need."
---

# Project agentic workflow bootstrapper

## Overview

Generate or update a repository-specific Copilot workflow kit.

Default to the smallest justified shape. First inspect the repository, then choose a profile, then add only the optional bundles that materially improve reliability, reviewability, or repeatability.

## Operating model

1. inspect the project
2. inspect the existing kit, if any
3. inspect only the skills that materially help this project
4. propose the architecture in text before generating files
5. choose `lean`, `standard`, or `rigorous`
6. generate or update the minimal justified kit
7. summarize the resulting workflow, chosen profile, optional bundles, omitted mechanisms, and unresolved gaps
8. recommend a concrete repository-type scenario and onboarding path
9. audit the existing kit for drift, partial bundles, placeholders, and unmanaged files in managed directories
10. use repair mode, profile diff, or migration mode when migration or recovery is justified
11. quarantine removed managed files during de-escalation when preserving history matters
12. when helpful, roll back a migration from quarantine instead of reconstructing the kit by hand
13. when helpful, run the smoke test script

## Profile strategy

### Lean profile
Use for small teams, low-friction adoption, or repositories where heavy governance would not be followed.

Generate only:
- `developer`
- `test-engineer`
- repository and path instructions
- minimal prompts for focused changes, testing, and patch review
- lightweight workflow docs

### Standard profile
Use by default for normal backend work that benefits from explicit planning.

Add to lean:
- `planner`
- formal plan prompts
- `02_plan.md`
- `04_plan_frozen.md`

### Rigorous profile
Use only when the repository needs strict governance, multi-file discipline, or repeated drift control.

Add to standard:
- `context-researcher`
- `architecture-synthesizer`
- `critical-judge`
- `plan-verifier`
- context, architecture, destructive-review, conformance, and patch-red-team artifacts

Do not choose `rigorous` unless the extra discipline will actually be used.

## Optional bundles

### Research bundle
Add only when repository reading alone is not enough or when the project needs durable behavioral artifacts or source-backed claim verification.

### Documentation bundle
Add only when the repository needs documentation parity, ADR discipline, or technical-text review.

### Security bundle
Add only when the repository has real security-sensitive surfaces or evidence-backed release requirements.

### Hooks bundle
Add only when command policy, prompt logging, or runtime enforcement solves a real governance gap.

## Project inspection workflow

Use `references/project-discovery.md`, `references/use-case-profiles.md`, `references/repository-type-examples.md`, `references/onboarding-checklist.md`, `references/runtime-maturity.md`, `references/profile-migration.md`, `references/change-control.md`, and `references/rollback-and-restore.md`.

At minimum, determine:
- repository layout and major subsystems
- backend paths and test paths
- build, lint, test, and verification commands
- public contracts, invariants, and risky surfaces
- existing workflow files and project conventions
- recurring work types in this repository
- whether the repository justifies research, documentation, security, or hooks bundles
- whether the repository should start as lean, standard, or rigorous

## Architecture proposal

Before generating or editing files, produce a compact architecture proposal using `references/architecture-proposal-format.md`.

The proposal must cover:
- project reading and constraints
- recommended profile
- which optional bundles are justified and why
- write permissions and stop conditions
- document workflow
- skill routing
- mechanisms intentionally omitted for now

## Generation workflow

When creating a new kit, use `scripts/scaffold_agentic_kit.py` if code execution is available.

Default command:
```bash
python scripts/scaffold_agentic_kit.py /path/to/repo
```

Supported flags:
- `--profile lean|standard|rigorous`
- `--include-research-agents`
- `--include-doc-agents`
- `--include-security-agents`
- `--include-hooks`
- `--project-name`
- `--backend-glob`
- `--test-glob`

The documentation bundle now defaults to:
- `gem-documentation-writer`
- `technical-content-evaluator`

Do not add a broader technical-writing agent unless the repository explicitly needs authoring help beyond parity and review.

After scaffolding:
1. replace placeholders with project-specific content
2. remove files that the project does not need
3. tighten tool access and role boundaries
4. adapt prompts and process documents to repository commands, paths, and invariants
5. populate architecture, routing, onboarding, and workflow docs with repository-specific content
6. run `scripts/validate_scaffold.py` against the chosen profile and bundles

## Validation workflow

Use `scripts/validate_scaffold.py` to confirm that the generated repository contains:
- all required files for the chosen profile
- all required files for selected bundles
- no unresolved `{{...}}` placeholders
- no partial bundles or profile fragments
- no unmanaged files inside managed directories
- no obvious role-to-artifact consistency breaks

## Drift audit

When the repository already contains a kit, run:

```bash
python scripts/audit_existing_kit.py /path/to/repo --output /path/to/repo/docs/agentic-workflow/KIT_DRIFT_REPORT.md
```

Use the resulting report to decide whether to repair, simplify, quarantine, migrate, or harden the kit.

## Repair mode

When drift is real and the target profile is known, run:

```bash
python scripts/repair_kit.py /path/to/repo --profile standard --report-output /path/to/repo/docs/agentic-workflow/KIT_DRIFT_REPORT.md
```

Use `--prune-managed-extras` only after reviewing local customizations. Use `--rewrite-placeholders` only when project name and path globs are known.

## Profile diff

Before changing profile or bundle posture, run:

```bash
python scripts/profile_diff.py --from-profile lean --to-profile standard
```

Use this to preview file additions and removals before migrating the kit.

## Migration mode

When the team has decided to change profile or bundle posture, run:

```bash
python scripts/migrate_profile.py /path/to/repo --to-profile standard --apply --report-output /path/to/repo/docs/agentic-workflow/PROFILE_MIGRATION_REPORT.md
```

By default, removed managed files are quarantined under `.agentic-quarantine/` instead of being deleted. Use `--keep-removed-managed` to leave them in place, or `--delete-removed-managed` only when quarantine is unnecessary.

## Smoke test

When you change the scaffold, repair logic, or bundle composition, run:

```bash
python scripts/smoke_test_workflow.py
```

This scaffolds and validates representative `lean`, `standard`, and `rigorous` repositories in temporary directories.

## Rollback mode

When a migration needs to be undone and the quarantine is still available, run:

```bash
python scripts/rollback_migration.py /path/to/repo --apply --report-output /path/to/repo/docs/agentic-workflow/ROLLBACK_REPORT.md
```

Use rollback before hand-copying managed files back into place. Let the script restore quarantined files, quarantine current conflicts, prune files outside the target state, and validate the result.


## Adoption guidance

Use `references/repository-type-examples.md` to anchor the first profile choice in a concrete repository shape.

Use `references/onboarding-checklist.md` to keep rollout lightweight and to decide whether the workflow should be simplified or hardened after the first real task.

## Output expectations

When you finish, provide:
- architecture summary
- chosen profile and why
- file summary
- workflow summary
- explicit omissions and deferred bundles