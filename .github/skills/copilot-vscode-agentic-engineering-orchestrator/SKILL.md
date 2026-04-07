---
name: copilot-vscode-agentic-engineering-orchestrator
description: decide, design, review, and scaffold end-to-end github copilot engineering workflows for visual studio code insiders. use when chatgpt needs to choose or combine context engineering, repository instructions, path-specific instructions, prompt files, custom agents, agent skills, planning, testing, browser agent tools, debugging, monitoring, memory, subagents, mcp, coding agent operations, spaces, model comparison, codebase exploration, refactoring, code review optimization, technical debt reduction, modernization, project upgrades, or cli hooks; and generate the smallest correct artifact or playbook for the requested engineering outcome.
---

# Copilot VS Code Agentic Engineering Orchestrator

## Overview

Use this skill to architect and operationalize GitHub Copilot workflows in VS Code Insiders.

Treat VS Code Insiders as the normative environment. Do not spend time warning about stable-vs-preview maturity. Focus on the best available mechanism in the current Copilot + VS Code ecosystem.

This skill is for four types of work:

1. **Mechanism selection**: choose between `copilot-instructions.md`, path-specific instruction files, prompt files, custom agents, agent skills, MCP, planning, memory, subagents, browser agent tools, debugging flows, monitoring, Spaces, and CLI hooks.
2. **Workflow design**: assemble those mechanisms into a coherent engineering flow.
3. **Artifact scaffolding**: generate the smallest correct artifact or playbook for the requested outcome.
4. **Architecture audit**: review an existing Copilot setup and identify overlap, omissions, mis-scoped instructions, or missing guardrails.

## Core rule

Always determine the **engineering outcome** first, and only then choose the Copilot mechanisms.

Do not start from “use prompt files” or “use custom agents.” Start from outcomes such as:

- explore a codebase
- implement a feature
- write tests
- refactor safely
- reduce technical debt
- review AI-generated code
- modernize legacy code
- upgrade dependencies or frameworks
- pilot coding agent in a team
- enforce CLI execution policy

## Operating model

Follow this sequence unless the user explicitly asks for only one artifact.

1. **Classify the request by outcome**
   - discovery
   - implementation
   - transformation
   - review
   - governance
   - adoption
   - strategy

2. **Classify the request by phase**
   - context
   - planning
   - implementation
   - verification
   - debugging
   - observability
   - memory / delegation
   - integration

3. **Pick the smallest sufficient mechanism**
   - repository-wide rule -> `assets/templates/copilot-instructions.md.template`
   - scoped rule -> `assets/templates/path.instructions.md.template`
   - reusable task prompt -> `assets/templates/prompt-file.prompt.md.template`
   - specialized persona -> `assets/templates/custom-agent.agent.md.template`
   - repeatable specialized procedure -> `assets/templates/skill-template/SKILL.md`
   - external tool or system access -> MCP
   - multi-step implementation -> planning + execution
   - terminal policy enforcement -> CLI hooks

4. **Add secondary mechanisms only if they materially improve the workflow**
   - Example: `copilot-instructions.md` + path-specific instruction file.
   - Example: plan agent + testing instructions + browser agent tools.
   - Example: custom agent + MCP + subagents.

5. **Produce the smallest useful deliverable**
   - an architecture recommendation
   - a single artifact template
   - a compact playbook
   - an audit report with concrete corrections

## Decision matrix

Use this decision matrix as the default routing logic.

### A. Persistent project behavior
Use when the user wants ongoing project conventions, architecture constraints, coding rules, review expectations, or team defaults.

- Project-wide -> see `references/customization-architecture.md` and `assets/templates/copilot-instructions.md.template`
- Path-specific -> see `references/customization-architecture.md` and `assets/templates/path.instructions.md.template`

### B. Reusable task execution
Use when the user wants a repeatable prompt-driven workflow.

- Prompt files -> see `references/customization-architecture.md` and `assets/templates/prompt-file.prompt.md.template`

### C. Specialized agent behavior
Use when the user wants a role-specific agent with its own tools, model behavior, or delegation rules.

- Custom agents -> see `references/customization-architecture.md` and `assets/templates/custom-agent.agent.md.template`
- Subagents -> see `references/subagents.md`
- Agent skills -> see `references/decision-engine.md` and `assets/templates/skill-template/SKILL.md`

### D. Context-heavy work
Use when success depends on curated project context, plans, memory, or repository knowledge.

- Context engineering -> `references/context-engineering.md`
- Planning / todos -> `references/planning-and-todos.md`
- Memory -> `references/memory.md`
- Codebase discovery -> `references/codebase-exploration.md`
- Spaces acceleration -> `references/spaces-acceleration.md`

### E. Transformation work
Use when the user wants concrete engineering outcomes.

- Write tests -> `references/testing-and-tdd.md`, `references/test-generation.md`
- Refactor -> `references/refactoring.md`
- Reduce technical debt -> `references/technical-debt-reduction.md`
- Modernize legacy code -> `references/modernization.md`
- Upgrade projects -> `references/project-upgrades.md`
- Improve a project with coding agent -> `references/coding-agent-operations.md`

### F. Governance and quality
Use when the user wants review standards, operational guardrails, or quality control.

- Code review optimization -> `references/code-review-optimization.md`
- AI-generated code review -> `references/ai-code-review.md`
- CLI policy hooks -> `references/cli-hooks-policy.md` and `assets/templates/cli-hooks/`
- Monitoring -> `references/observability.md` and `assets/templates/otel-checklist.md`

### G. External capability or system integration
Use when Copilot must reach beyond the local workspace.

- MCP in workflows -> `references/mcp-usage.md`
- MCP extension authoring -> `references/mcp-extension-authoring.md`

### H. Strategy and adoption
Use when the user wants rollout, comparison, or capability planning.

- Pilot coding agent -> `references/coding-agent-pilot.md`
- Compare models -> `references/model-strategy.md`
- Learn a new language with Copilot -> `references/language-learning.md`
- Speed up development work -> `references/spaces-acceleration.md`

## Default output shapes

### 1. Architecture recommendation
Use this shape when the user wants design guidance.

```markdown
# Recommended Copilot workflow

## Outcome
[What the workflow is meant to achieve]

## Primary mechanism
[Smallest sufficient mechanism and why]

## Supporting mechanisms
[Only those that materially improve the flow]

## Artifact(s) to create
[Exact file names or assets]

## Suggested workflow
[Short step sequence]

## Pitfalls to avoid
[Concrete anti-patterns]
```

### 2. Artifact scaffold
Use this shape when the user wants a file or template.

```markdown
# Artifact
[filename]

## Purpose
[What this file controls]

## Suggested contents
[Provide the file]

## Notes
[Scope boundaries, intended use, follow-up artifacts only if needed]
```

### 3. Audit
Use this shape when reviewing an existing setup.

```markdown
# Copilot workflow audit

## What exists
[Summarize current mechanisms]

## What is correct
[Keep]

## What is mis-scoped or redundant
[Fix or remove]

## What is missing
[Add only necessary items]

## Minimal corrected design
[Concrete next state]
```

## Anti-patterns

Always push back on these patterns:

- using project-wide instructions for one-off tasks
- encoding persistent architecture policy in prompt files
- creating a custom agent when a path-specific instruction file is enough
- creating a skill when a custom agent or prompt file is enough
- dumping all team knowledge into one huge instruction file
- adding MCP without a concrete external capability gap
- using memory as the main repository policy mechanism
- doing TDD as one undifferentiated agent step instead of separating phases
- using browser agent tools only after late manual QA instead of as part of the test loop
- adding observability after rollout instead of during workflow design
- treating code review of AI-generated code as ordinary review with no rubric
- adding CLI hooks with no explicit policy objective

See `references/anti-patterns.md`.

## Workflow guides to load on demand

Load only the references that match the task.

- `references/context-engineering.md`
- `references/customization-architecture.md`
- `references/planning-and-todos.md`
- `references/testing-and-tdd.md`
- `references/browser-agent-tools.md`
- `references/debugging.md`
- `references/observability.md`
- `references/memory.md`
- `references/subagents.md`
- `references/mcp-usage.md`
- `references/mcp-extension-authoring.md`
- `references/coding-agent-operations.md`
- `references/coding-agent-pilot.md`
- `references/model-strategy.md`
- `references/spaces-acceleration.md`
- `references/codebase-exploration.md`
- `references/language-learning.md`
- `references/test-generation.md`
- `references/refactoring.md`
- `references/code-review-optimization.md`
- `references/ai-code-review.md`
- `references/technical-debt-reduction.md`
- `references/modernization.md`
- `references/project-upgrades.md`
- `references/cli-hooks-policy.md`

## Bundled templates

Use these templates when the user asks to generate or scaffold a concrete artifact.

- `assets/templates/copilot-instructions.md.template`
- `assets/templates/path.instructions.md.template`
- `assets/templates/review.instructions.md.template`
- `assets/templates/testing.instructions.md.template`
- `assets/templates/prompt-file.prompt.md.template`
- `assets/templates/custom-agent.agent.md.template`
- `assets/templates/skill-template/SKILL.md`
- `assets/templates/plan-agent-playbook.md`
- `assets/templates/codebase-discovery-playbook.md`
- `assets/templates/tech-debt-burndown-playbook.md`
- `assets/templates/modernization-playbook.md`
- `assets/templates/upgrade-playbook.md`
- `assets/templates/ai-code-review-checklist.md`
- `assets/templates/model-comparison-matrix.md`
- `assets/templates/otel-checklist.md`
- `assets/templates/cli-hooks/settings.example.json`
- `assets/templates/cli-hooks/session-banner.sh`
- `assets/templates/cli-hooks/log-prompt.sh`
- `assets/templates/cli-hooks/pre-tool-policy.sh`

## Final rule

Bias toward clarity, small scope, and composability.

A good Copilot engineering workflow uses the fewest mechanisms that still make the outcome reliable, reviewable, and repeatable.
