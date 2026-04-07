# Refactoring workflows

## Use refactoring as controlled transformation

A refactor workflow should preserve behavior while improving structure.

## Recommended sequence

1. understand the current behavior
2. add or verify tests
3. define the refactor goal
4. make small changes with checkpoints
5. re-run verification after each meaningful step
6. document any new architectural rules

## Good refactor prompts

- separate concerns in this module without changing behavior
- extract a reusable abstraction and keep existing tests passing
- reduce duplication while preserving the public API
