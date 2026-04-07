# Testing and TDD workflows

## Treat testing as a first-class workflow

Do not bolt tests onto the end of the implementation.

## TDD flow

1. Clarify behavior and constraints.
2. Write or scaffold failing tests.
3. Implement the smallest change that makes them pass.
4. Refactor safely.
5. Re-run targeted verification.

## Recommended mechanisms

- repository or path-specific testing instructions
- custom test-focused agent if the project benefits from a dedicated testing persona
- prompt files for recurring tasks such as generating a test plan or covering edge cases
- browser agent tools when UI behavior is the subject of the test

## Handoff model

For stronger control, separate:
- planning of tests
- generation of tests
- implementation against tests
- review of resulting changes

## Avoid

- one giant agent run that writes tests, implements code, and self-approves without structured checkpoints
- UI testing without browser-aware verification when the UI is the risk surface
