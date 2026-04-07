# Reviewing AI-generated code

## Principle

AI-generated code deserves a stricter, more explicit rubric than ordinary code review.

## Review sequence

1. verify the code actually solves the requested problem
2. inspect assumptions, hidden defaults, and edge cases
3. check for unnecessary complexity or invented abstractions
4. inspect dependencies, APIs, and external calls
5. verify tests or add missing ones
6. look for maintainability, readability, and consistency issues

## What AI often gets wrong

- plausible but incorrect edge handling
- misuse of existing project patterns
- over-generalization
- redundant abstractions
- incomplete verification

## Recommended deliverable

Use a compact checklist or rubric so review findings stay consistent across sessions.
