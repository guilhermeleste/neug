# Rollback and restore

Use this guide when a controlled migration or aggressive repair needs to be undone without relying on Git alone.

## When rollback is justified
- a profile migration removed roles or documents the team still needs
- a de-escalation to lean or standard happened too early
- a migration left the repository in a valid but operationally worse state
- managed files were quarantined correctly and should be restored

## Default rollback sequence
1. find the relevant `.agentic-quarantine/profile-migration-*` directory
2. preview rollback first with `scripts/rollback_migration.py`
3. confirm the target profile and bundles
4. apply rollback and write `ROLLBACK_REPORT.md`
5. validate the restored target state
6. re-run the drift audit

## Default command
```bash
python scripts/rollback_migration.py /path/to/repo --apply --report-output /path/to/repo/docs/agentic-workflow/ROLLBACK_REPORT.md
```

## Conflict rule
If rollback would overwrite current files, move the current files into a rollback conflict quarantine instead of silently deleting them.

## Prune rule
After restore, prune only the managed files that are outside the rollback target state. Prefer quarantine over deletion unless the repository history is easy to recover and the change is trivial.
