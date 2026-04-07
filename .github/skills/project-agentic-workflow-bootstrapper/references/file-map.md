# File map

## Lean profile
- `.github/copilot-instructions.md`
- `.github/agents/developer.agent.md`
- `.github/agents/test-engineer.agent.md`
- `.github/instructions/backend.instructions.md`
- `.github/instructions/testing.instructions.md`
- `.github/instructions/review.instructions.md`
- `.github/prompts/focused-backend-change.prompt.md`
- `.github/prompts/generate-backend-tests.prompt.md`
- `.github/prompts/review-ai-patch.prompt.md`
- `docs/agentic-workflow/README.md`
- `docs/agentic-workflow/ONBOARDING.md`
- `docs/agentic-workflow/ARCHITECTURE.md`
- `docs/agentic-workflow/SKILL_ROUTING.md`
- `docs/agentic-workflow/00_goal.md`
- `docs/agentic-workflow/06_test_spec.md`
- `docs/agentic-workflow/07_execution_log.md`
- `docs/agentic-workflow/10_closure_report.md`
- `docs/agentic-workflow/KIT_DRIFT_REPORT.md` (optional output of the audit script, not scaffolded)
- `docs/agentic-workflow/PROFILE_MIGRATION_REPORT.md` (optional output of the migration script, not scaffolded)
- `docs/agentic-workflow/ROLLBACK_REPORT.md` (optional output of the rollback script, not scaffolded)

## Standard profile additions
- `.github/agents/planner.agent.md`
- `.github/prompts/plan-backend-change.prompt.md`
- `.github/prompts/implement-from-plan.prompt.md`
- `docs/agentic-workflow/02_plan.md`
- `docs/agentic-workflow/04_plan_frozen.md`

## Rigorous profile additions
- `.github/agents/context-researcher.agent.md`
- `.github/agents/architecture-synthesizer.agent.md`
- `.github/agents/critical-judge.agent.md`
- `.github/agents/plan-verifier.agent.md`
- `.github/prompts/redteam-plan.prompt.md`
- `.github/prompts/check-plan-conformance.prompt.md`
- `.github/prompts/synthesize-architecture.prompt.md`
- `docs/agentic-workflow/01_context_pack.md`
- `docs/agentic-workflow/01c_architecture_overview.md`
- `docs/agentic-workflow/03_plan_redteam.md`
- `docs/agentic-workflow/08_conformance_report.md`
- `docs/agentic-workflow/09_patch_redteam.md`

## Optional research bundle
- `.github/agents/official-docs-researcher.agent.md`
- `.github/agents/academic-literature-researcher.agent.md`
- `.github/agents/research-technical-spike.agent.md`
- `.github/agents/specification.agent.md`
- `.github/agents/doublecheck.agent.md`
- `.github/prompts/research-technical-spike.prompt.md`
- `.github/prompts/write-or-update-specification.prompt.md`
- `.github/prompts/doublecheck-claims.prompt.md`
- `docs/agentic-workflow/01a_official_docs_memo.md`
- `docs/agentic-workflow/01b_academic_memo.md`
- `docs/agentic-workflow/01d_technical_spike.md`
- `spec/spec-task.md`

## Optional documentation bundle
- `.github/agents/gem-documentation-writer.agent.md`
- `.github/agents/technical-content-evaluator.agent.md`
- `.github/prompts/review-specification.prompt.md`
- `.github/prompts/review-adr-or-doc.prompt.md`
- `.github/prompts/update-parity-documentation.prompt.md`
- `docs/adr/ADR-template.md`
- `docs/agentic-workflow/02b_spec_review.md`
- `docs/agentic-workflow/10a_documentation_closeout.md`
- `docs/agentic-workflow/10b_documentation_review.md`

## Optional security bundle
- `.github/agents/security-review-lead.agent.md`
- `.github/agents/security-threat-modeler.agent.md`
- `.github/agents/security-api-reviewer.agent.md`
- `.github/agents/security-web-reviewer.agent.md`
- `.github/agents/security-asvs-governor.agent.md`
- `.github/prompts/security-threat-model.prompt.md`
- `.github/prompts/review-api-surface-security.prompt.md`
- `.github/prompts/review-web-surface-security.prompt.md`
- `.github/prompts/build-asvs-evidence-matrix.prompt.md`
- `docs/agentic-workflow/01e_security_scope.md`
- `docs/agentic-workflow/01f_threat_register.md`
- `docs/agentic-workflow/02c_security_requirements.md`
- `docs/agentic-workflow/03c_security_redteam.md`
- `docs/agentic-workflow/08c_security_conformance_report.md`
- `docs/agentic-workflow/10c_security_evidence_matrix.md`
- `docs/agentic-workflow/10d_security_release_gates.md`

## Optional hooks bundle
- `.github/hooks/settings.example.json`
- `.github/hooks/scripts/session-banner.sh`
- `.github/hooks/scripts/log-prompt.sh`
- `.github/hooks/scripts/pre-tool-policy.sh`


## Maintenance scripts
- `scripts/validate_scaffold.py`
- `scripts/audit_existing_kit.py`
- `scripts/repair_kit.py`
- `scripts/profile_diff.py`
- `scripts/migrate_profile.py`
- `scripts/rollback_migration.py`
- `scripts/smoke_test_workflow.py`
