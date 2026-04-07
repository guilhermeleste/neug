# Role bundles

## Lean profile
Use for low-friction adoption:
- developer
- test-engineer

## Standard profile
Add when explicit planning is justified:
- planner

## Rigorous profile
Add only when strict governance is justified:
- context-researcher
- architecture-synthesizer
- critical-judge
- plan-verifier

## Optional research bundle
Add when repository reading alone is not enough or when plans depend on durable behavioral artifacts or source-backed claims:
- official-docs-researcher
- academic-literature-researcher
- research-technical-spike
- specification
- doublecheck

## Optional documentation bundle
Add when the repository needs documentation parity, ADR/spec review, or source-backed technical-text evaluation:
- gem-documentation-writer
- technical-content-evaluator

## Optional security bundle
Add when the repository exposes security-sensitive surfaces, external APIs, browser-facing flows, tenant or privilege boundaries, regulated data, or release gates that must be backed by evidence:
- security-review-lead
- security-threat-modeler
- security-api-reviewer
- security-web-reviewer
- security-asvs-governor

## Optional hooks bundle
Add only when command policy, prompt logging, or runtime enforcement solves a real governance gap.

## Decision rule
Prefer the smallest profile that the team will actually use. Start with standard unless there is a strong reason to go lean or rigorous. Add optional bundles only when they solve a concrete repository problem.


## Migration note
Use `scripts/profile_diff.py` before moving between lean, standard, and rigorous. Use `scripts/migrate_profile.py` to apply a controlled migration with optional quarantine of removed managed files. Use `scripts/repair_kit.py` when the repository drifted away from an intended profile and you need to restore missing managed files.
