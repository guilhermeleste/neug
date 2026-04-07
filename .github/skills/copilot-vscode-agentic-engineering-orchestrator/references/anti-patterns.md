# Anti-patterns

## Mechanism anti-patterns

- one giant `copilot-instructions.md` that tries to encode everything
- path-specific files that duplicate global rules with minor wording changes
- prompt files used as hidden policy instead of explicit reusable tasks
- custom agents that exist only because naming feels nice, not because behavior is meaningfully different
- skills created before a custom agent or prompt file has proven insufficient
- MCP added with no concrete missing capability

## Workflow anti-patterns

- skipping planning for risky work
- collapsing research, implementation, review, and verification into one opaque agent run
- asking for “improve the project” without scope or success criteria
- using browser tools as a substitute for deterministic tests
- performing AI code review without a rubric
- modernizing legacy code via full rewrite framing
- upgrading projects without a breaking-change map

## Governance anti-patterns

- depending on memory for canonical repository policy
- adding observability only after agent rollout fails
- adding CLI hooks before defining the policy objective
- logging prompts or tool calls without any redaction strategy
