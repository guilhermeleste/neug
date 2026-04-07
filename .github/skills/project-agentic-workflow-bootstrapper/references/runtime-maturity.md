# Runtime maturity and drift control

Use this guide when the scaffold already exists and the main question is whether the kit still matches real repository use.

## Drift symptoms
- profile is heavier than actual team usage
- optional bundles were added but are rarely exercised
- prompts or agents exist without corresponding documents
- templates still contain placeholders
- managed directories contain local files that no longer match the kit model
- security, documentation, or research artifacts exist only as ritual paperwork

## Recommended audit loop
1. infer the current profile and bundles
2. compare expected vs present files
3. look for partial bundles and orphaned artifacts
4. detect placeholders and unmanaged files in managed directories
5. classify each issue as repair, simplify, quarantine, migrate, or ignore
6. decide whether to de-escalate, keep, or harden the kit

## Default tool
Use `scripts/audit_existing_kit.py` to generate a markdown drift report.

Example:
```bash
python scripts/audit_existing_kit.py /path/to/repo --output /path/to/repo/docs/agentic-workflow/KIT_DRIFT_REPORT.md
```

## Simplification rule
Prefer deleting an unused role or bundle over keeping it as symbolic process overhead.

## Hardening rule
Only harden after repeated real failures justify the added role, prompt, or bundle.


## Repair loop
Use `scripts/audit_existing_kit.py` first, then use `scripts/repair_kit.py` conservatively.

Recommended order:
1. audit the kit and read the drift report
2. decide the target profile and bundles
3. restore missing managed files
4. rewrite unresolved placeholders only when the repository naming and path globs are known
5. prune managed extras only after reviewing local customizations
6. re-run validation and the audit

Do not use repair mode as a substitute for repository judgment. Restore first, prune second.

## Rollback loop
When a migration simplified or hardened the kit too aggressively:
1. identify the relevant `.agentic-quarantine/profile-migration-*` directory
2. run `scripts/rollback_migration.py` in preview mode first
3. restore the target profile and bundles
4. quarantine conflicting current files instead of overwriting them silently
5. re-run validation and the audit

Prefer rollback over hand-copying files back into place when a migration was the source of drift.

## Profile migration
Use `scripts/profile_diff.py` before changing profile or bundle posture.
Use `scripts/migrate_profile.py` when the change should be applied in a controlled way.

Use it to answer:
- what files will be added?
- what files will be removed?
- is this migration simplifying the kit or hardening it?
- does the team actually need the new surface area?
