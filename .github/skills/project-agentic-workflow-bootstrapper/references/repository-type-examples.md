# Repository-type examples

Use these examples to choose a starting profile quickly. Treat them as defaults to challenge, not rules to follow blindly.

## 1. Small internal REST API
Recommended profile: `lean`

Why:
- small team
- local changes dominate
- process overhead must stay low

Add bundles only if needed:
- `--include-security-agents` when the API exposes external users, authn/authz, or regulated data
- `--include-doc-agents` when docs drift is already painful

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile lean
```

## 2. Medium backend service with regular feature work
Recommended profile: `standard`

Why:
- explicit planning helps
- changes often touch multiple modules
- the team benefits from a frozen plan but not full governance

Add bundles only if needed:
- `--include-research-agents` when external docs, specs, or verified claims are common
- `--include-security-agents` when the service owns external APIs, tenancy, secrets, or sensitive data

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile standard
```

## 3. Multi-team platform service or core backend
Recommended profile: `rigorous`

Why:
- architecture misunderstanding is expensive
- drift control matters
- red-team style review is worth the extra cost

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile rigorous
```

## 4. API-first repository with OpenAPI or GraphQL contracts
Recommended profile: `standard`

Why:
- contracts benefit from planning and review
- security and specification work are often justified

Likely bundle pairings:
- `--include-research-agents`
- `--include-security-agents`

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile standard --include-research-agents --include-security-agents
```

## 5. Regulated or high-risk service
Recommended profile: `rigorous`

Why:
- evidence, conformance, and release gates matter
- security review must happen before release, not after

Likely bundle pairings:
- `--include-security-agents`
- `--include-doc-agents`
- `--include-research-agents` when claim verification is common

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile rigorous --include-security-agents --include-doc-agents
```

## 6. Library or package repository
Recommended profile: `lean`

Why:
- there may be no persistent backend runtime
- planning and testing are still useful, but governance may be overkill

Adjustments:
- set backend/test globs explicitly
- consider docs bundle if usage docs or ADRs matter more than execution flow docs

Typical start command:
```bash
python scripts/scaffold_agentic_kit.py /repo --profile lean --backend-glob "src/**" --test-glob "tests/**"
```

## Selection rule

When two profiles seem plausible, start lower and escalate only after you see real coordination pain.
