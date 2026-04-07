# Profile scenarios

Use this guide to choose the smallest profile and the smallest optional bundles that still make the workflow reliable.

## Lean

Use lean when:
- the team is small
- most changes are local
- developers will not maintain extra governance roles
- the main need is bounded code generation plus tests and patch review

Typical repositories:
- small internal APIs
- early-stage services
- utility backends with straightforward test surfaces

Good bundle pairings:
- no bundles by default
- documentation bundle only if docs drift is already painful
- security bundle only for clearly sensitive surfaces

## Standard

Use standard when:
- work benefits from explicit planning
- changes often touch multiple modules
- the team wants a frozen plan but not a heavy governance graph
- regressions usually come from plan drift rather than missing deep context

Typical repositories:
- medium backend services
- APIs with regular feature work
- projects where plan -> implement -> test is already the normal habit

Good bundle pairings:
- research bundle when external docs, specs, or verified claims are frequently needed
- documentation bundle when ADR or spec review is a recurring need
- security bundle when the repo exposes external APIs, authn/authz, tenant boundaries, or regulated data

## Rigorous

Use rigorous when:
- multi-file drift is common
- architecture misunderstanding is a recurring source of waste
- destructive review and conformance checks are actually used by the team
- the repository has high coordination cost or repeated review failures

Typical repositories:
- large backends
- multi-team services
- systems with strong compatibility or release discipline
- repositories where security or auditability materially shapes engineering work

Good bundle pairings:
- research bundle when spikes, specifications, and source-backed verification are normal work
- documentation bundle when parity docs or ADR review is part of done-done
- security bundle when security review must happen before release, not as an afterthought
- hooks only when guidance has already failed and executable policy is justified

## Escalation rules

Move from lean to standard when:
- developers keep needing explicit frozen plans
- changes are no longer purely local
- review repeatedly asks for a plan that was never written down

Move from standard to rigorous when:
- architecture misunderstanding causes repeated churn
- destructive review keeps finding drift too late
- the team benefits from separate context, architecture, and conformance phases

Do not move upward just because the project feels important.

## De-escalation rules

Move from rigorous back to standard when:
- strict-governance roles are rarely used
- conformance and redteam artifacts are mostly empty ritual
- the team ignores context and architecture docs in practice

Move from standard back to lean when:
- planning artifacts are rarely consulted
- the codebase is small enough that the plan is obvious from the patch itself
- process overhead exceeds coordination benefit
