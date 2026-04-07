# Decision engine

## First question: what is the user actually trying to accomplish?

Classify the request by engineering outcome before choosing any Copilot mechanism.

- **Discovery**: understand a codebase, architecture, or unfamiliar technology.
- **Implementation**: build a feature or fix.
- **Transformation**: refactor, modernize, upgrade, reduce debt.
- **Review**: improve review quality or review AI-generated code.
- **Governance**: enforce policy, create guardrails, improve predictability.
- **Adoption**: pilot coding agent, standardize team usage, choose models.

## Then classify the minimum persistent surface needed

- **Project-wide behavior** -> repository instructions.
- **Scoped behavior** -> path-specific instructions.
- **Reusable task text** -> prompt file.
- **Role-specific autonomy** -> custom agent.
- **Specialized repeatable procedure** -> agent skill.
- **External system access** -> MCP.
- **Terminal policy enforcement** -> CLI hooks.

## Heuristics

### Prefer repository instructions when
- the rule should shape almost every chat request
- it is about coding conventions, architecture constraints, review expectations, or repository norms

### Prefer path-specific instructions when
- the rule only applies to frontend, tests, docs, migrations, infra, or a narrow file pattern
- the repo contains multiple conventions that would conflict if made global

### Prefer prompt files when
- the task is repeatable but not a permanent policy
- you want a reusable, named entry point for a task
- the task should remain explicit and user-invoked

### Prefer custom agents when
- the workflow needs a dedicated persona
- the agent should have restricted tools
- the workflow benefits from clear instructions around planning, subagents, or review style

### Prefer a skill when
- the procedure is too large or too specialized to repeat ad hoc
- the agent benefits from bundled references, scripts, or templates
- the same specialized flow will be reused many times

### Prefer MCP when
- the missing capability is external to the workspace
- the agent needs live access to systems, APIs, docs, or organization tools
- the gain is not just “more context” but a real integration capability

## Combination patterns

- repository instructions + path-specific instructions
- path-specific instructions + prompt file
- custom agent + prompt file
- plan agent + testing instructions
- custom agent + subagents
- custom agent + MCP
- coding agent + Spaces + review rubric
- CLI hooks + repository instructions

## Never choose mechanisms just because they are available

Choose them because they solve a concrete gap in the workflow.
