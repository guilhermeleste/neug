# Profile migration

Use profile migration deliberately. Do not harden or simplify the kit by intuition alone.

## Before changing profile
- run `scripts/audit_existing_kit.py`
- identify which artifacts are actually used in the last few tasks
- decide whether the migration is simplification or hardening
- run `scripts/profile_diff.py` to preview added and removed files

## Common migrations
### Lean -> Standard
Use when plans are repeatedly reconstructed in chat or implementation drift is increasing.

### Standard -> Rigorous
Use when multi-file changes, review failures, or governance gaps keep recurring.

### Rigorous -> Standard
Use when strict-governance artifacts are rarely touched and the team routes around them.

### Standard -> Lean
Use when the repository is small and most changes are local, low-risk, and test-bounded.

## Migration rule
- restore missing files before pruning extras
- audit before and after the migration
- quarantine removed managed files by default during de-escalation
- explain the migration in the final summary

## Migration command
```bash
python scripts/migrate_profile.py /path/to/repo --to-profile standard --apply --report-output /path/to/repo/docs/agentic-workflow/PROFILE_MIGRATION_REPORT.md
```

Use `--copy-bundles` when you want to keep the current bundle set while changing only the profile.
Use `--keep-removed-managed` when you want a soft migration with no pruning.
Use `--delete-removed-managed` only when quarantine is unnecessary.

## Rollback command
If a migration needs to be undone and the quarantine is still available:
```bash
python scripts/rollback_migration.py /path/to/repo --apply --report-output /path/to/repo/docs/agentic-workflow/ROLLBACK_REPORT.md
```

Use `--target-profile` and bundle flags when you want to override the inferred rollback target from quarantine metadata.
