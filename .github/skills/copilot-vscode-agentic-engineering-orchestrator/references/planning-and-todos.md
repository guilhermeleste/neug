# Planning and todo management

## Use planning by default for non-trivial work

For features, refactors, bugfixes with risk, modernization, or upgrade work:
- start with the plan agent
- answer clarifying questions
- iterate on the plan until the verification steps are explicit

## Good plans contain

- outcome and constraints
- affected areas of the codebase
- implementation steps
- verification steps
- rollback or risk notes when relevant

## Todo discipline

Use todos when the task has multiple steps, branching risk, or long execution time.

The todo list should reflect:
- investigation
- implementation
- verification
- follow-up cleanup

## Practical pattern

- use `/plan` to create the plan
- refine until the plan is implementation-ready
- execute in the same session for continuity, or start a new implementation session if you want a cleaner execution context
- when needed, preserve the plan as a repository document or prompt file instead of leaving it only in session memory
