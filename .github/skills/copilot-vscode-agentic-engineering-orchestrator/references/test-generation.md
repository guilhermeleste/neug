# Test generation

## Goal

Generate tests that are behavior-driven, reviewable, and aligned to project conventions.

## Workflow

1. identify the behavior under test
2. decide the test level: unit, integration, browser, regression
3. capture conventions in testing instructions if the project is large or opinionated
4. generate tests with explicit assertions and realistic setup
5. run, fix, and review the tests before merging

## Review checklist

- does the test assert meaningful behavior?
- is setup minimal and readable?
- are edge cases covered?
- does the test depend on brittle implementation details?
