# Change control

Use this guide when the repository already has a working kit and the question is not “what should we scaffold?” but “how should we change the kit safely?”

## Change-control sequence
1. audit the current kit
2. inspect the profile and bundle delta
3. decide whether the change is hardening, simplification, or recovery
4. apply a controlled migration or repair
5. validate the resulting state
6. keep a migration report when the change is non-trivial

## Default tools
- `scripts/audit_existing_kit.py`
- `scripts/profile_diff.py`
- `scripts/migrate_profile.py`
- `scripts/rollback_migration.py`
- `scripts/repair_kit.py`
- `scripts/validate_scaffold.py`

## Quarantine rule
When simplifying a kit, prefer quarantine over deletion for managed files that are leaving the active profile or bundle set.

Quarantine is useful when:
- the team is de-escalating from rigorous to standard or lean
- documentation or research bundles are being removed
- the repository contains uncertain local customization inside managed files
- the team wants rollback without relying on Git history alone

## Deletion rule
Delete removed managed files only when:
- the migration is small and well-understood
- the repository history is trusted and easy to recover
- quarantine would add unnecessary clutter

## Suggested report outputs
- `docs/agentic-workflow/KIT_DRIFT_REPORT.md`
- `docs/agentic-workflow/PROFILE_MIGRATION_REPORT.md`
- `docs/agentic-workflow/ROLLBACK_REPORT.md`
