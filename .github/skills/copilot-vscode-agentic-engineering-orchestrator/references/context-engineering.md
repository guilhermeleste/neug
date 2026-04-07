# Context engineering

## Purpose

Context engineering is the disciplined process of supplying targeted, durable project context to agents so they can plan and implement with less drift.

## Default flow

1. Curate project-wide context.
2. Create an implementation plan.
3. Generate implementation code against that plan.
4. Verify with tests and review.

## Practical guidance

- Put durable project standards in `copilot-instructions.md`.
- Put bounded, domain-specific rules in path-specific instruction files.
- For complex work, use the plan agent first and make the plan explicit.
- If the plan becomes important beyond one chat session, save it as a repository document rather than relying only on session memory.
- Split long work into discrete sessions when the context window would become noisy.

## Good context artifacts

- architecture principles
- coding standards
- implementation plans
- review rubrics
- project conventions
- common commands and validation steps

## Bad context artifacts

- giant undifferentiated dumps of docs
- temporary task chatter in permanent instruction files
- duplicate rules across many files
- policy text that does not change agent behavior
