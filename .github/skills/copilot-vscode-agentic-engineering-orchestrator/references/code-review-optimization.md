# Optimizing code review with Copilot

## Goal

Improve review signal, not just review speed.

## Use custom instructions for review when

- the team has explicit review priorities
- certain paths need stricter scrutiny
- AI review should focus on security, reliability, performance, or maintainability

## Review workflow

1. establish review criteria in instructions
2. generate or use a focused review prompt or agent
3. review diffs against repository context
4. summarize findings by severity and confidence
5. require human judgment on consequential changes

## Better review prompts focus on

- correctness
- edge cases
- architectural fit
- regressions
- test adequacy
- maintainability
