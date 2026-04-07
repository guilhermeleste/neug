# Technical debt reduction

## Treat debt reduction as a program, not a vague cleanup request

## Workflow

1. identify debt categories
2. prioritize a bounded slice
3. define the expected engineering gain
4. implement in small reviewable increments
5. track residual debt and follow-up items

## Common debt categories

- duplication
- outdated dependencies
- flaky or missing tests
- obsolete abstractions
- poor module boundaries
- unclear commands and setup

## Good asks to Copilot

- identify the highest-value debt in this subsystem
- propose a three-step burn-down plan
- group debt by risk and effort
- implement only the first tranche and verify it
