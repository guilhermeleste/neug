# Customization architecture

## Canonical progression

Use the smallest customization mechanism that fits the need.

1. **Repository instructions**: project-wide standards.
2. **Path-specific instructions**: scoped conventions.
3. **Prompt files**: reusable task entry points.
4. **Custom agents**: role-specific workflows with tool discipline.
5. **MCP**: external capability.
6. **Agent skills**: specialized reusable procedures.

## Repository instructions

Use `.github/copilot-instructions.md` for:
- coding standards
- import style
- repository structure assumptions
- architectural constraints
- review expectations

Tip: VS Code can bootstrap this file with `/init`, then you refine it.

## Path-specific instructions

Use `.github/instructions/*.instructions.md` for:
- frontend-only rules
- test-writing rules
- docs conventions
- infra or migration standards
- any area that would pollute global instructions if made repository-wide

## Prompt files

Use prompt files when:
- the task is reusable
- the user should invoke it explicitly
- the content is task-oriented, not policy-oriented

Examples:
- create a test plan
- prepare a refactor brief
- review AI-generated patch
- document a feature

## Custom agents

Use a custom agent when:
- a named persona helps users and other agents
- tools should be narrowed
- delegation and subagent behavior should be specified
- a workflow needs strong internal instructions but should remain easy to invoke

Important:
- keep the agent focused
- define the outcome, scope boundaries, and when to hand off or stop
- do not grant extra tools without a concrete reason

## Agent skills

Use a skill when:
- the procedure is complex and reused often
- the agent needs bundled references and templates
- you want another ChatGPT/Copilot instance to reuse a precise workflow
