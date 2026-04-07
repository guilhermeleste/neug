# Update playbook

Use this workflow when the repository already has some agentic workflow files.

1. inventory the current files
2. classify each as keep, update, merge, remove, quarantine, or migrate
3. preserve local conventions, commands, and path scopes whenever they still make sense
4. choose the smallest viable profile first: lean, standard, or rigorous
5. update only the minimal set of agents, prompts, and instructions needed
6. add optional bundles only when they solve a recurring repository problem
7. regenerate architecture, routing, and workflow docs if the role graph or enforcement changed
8. run `scripts/validate_scaffold.py` against the chosen profile and bundles
9. run `scripts/audit_existing_kit.py` to generate a drift report before and after larger edits
10. mention deliberate non-updates in the final summary

## Common update cases
- collapse strict-governance roles back to standard when they are not being used
- merge redundant research roles back into repository reading when external evidence is rarely needed
- remove standalone paperwork files when their content can live inside the plan or closure report
- add rigorous only when drift, multi-file confusion, or repeated review failures justify it
- add the research bundle when specs, spikes, or verified claims become necessary
- add the documentation bundle when documentation parity, ADR review, or specification review is a recurring problem
- add the security bundle when the repository has real security-sensitive surfaces or evidence-backed release requirements
- add hooks only when there is a concrete governance gap


## Repair and migration tools
- use `scripts/profile_diff.py` before changing profile or bundle posture
- use `scripts/migrate_profile.py` when a profile or bundle change should actually be applied
- use `scripts/rollback_migration.py` to restore a previous state from quarantine without relying on Git alone
- use `scripts/repair_kit.py` to restore missing managed files after drift or partial deletions
- quarantine removed managed files by default when simplifying the kit
- use `--prune-managed-extras` only after auditing local modifications inside managed directories
- prefer repair, migration, or rollback toward a named target profile instead of ad hoc file copying
