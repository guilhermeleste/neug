# Onboarding checklist

Use this checklist when introducing the generated workflow to a repository or team.

## Before scaffolding
- confirm the repository type and choose `lean`, `standard`, or `rigorous`
- identify backend and test globs
- identify build, test, lint, type-check, and smoke-test commands
- decide whether research, documentation, security, or hooks solve a real problem

## Immediately after scaffolding
- open `docs/agentic-workflow/README.md`
- confirm the selected profile is correct
- replace or tighten repository-specific instructions
- trim files the team will not actually use
- fill in architecture and workflow docs with real repository facts

## First-week adoption
- use the generated prompts on one real task
- keep the first task bounded and reviewable
- check whether the chosen profile felt too heavy or too light
- record friction, ignored files, and missing commands
- adjust bundle selection before wider rollout

## Signals to simplify
- the team ignores plan or conformance artifacts
- prompts are used but agents are not
- review is happening outside the generated workflow
- strict-governance roles are mostly empty ritual

## Signals to harden
- repeated drift between plan and implementation
- architecture misunderstandings keep causing churn
- specs or ADRs need stronger review
- security review is repeatedly late or informal
- command policy needs executable enforcement

## Exit criteria for a healthy rollout
- at least one real task completed with the kit
- profile choice justified by observed usage, not intuition alone
- unused files removed or consciously retained
- validation and smoke tests pass after local customization


## Maintenance after first rollout
- run `scripts/audit_existing_kit.py` after the first few real tasks
- use `scripts/profile_diff.py` before escalating or de-escalating profile
- use `scripts/migrate_profile.py` when the team decides to actually change profile or bundle posture
- use `scripts/repair_kit.py` if managed files were deleted or partially drifted
