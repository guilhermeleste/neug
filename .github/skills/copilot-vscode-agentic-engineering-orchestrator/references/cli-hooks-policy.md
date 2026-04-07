# CLI hooks as executable policy

## Use hooks when guidance is not enough

CLI hooks let you enforce or observe behavior at runtime.

## Strong uses

- show a policy banner at session start
- log prompts for audit
- inspect tool calls before execution
- deny or warn on risky commands

## Design questions

- what policy are you trying to enforce?
- what should always be logged?
- what should always be blocked?
- what should only warn?
- where do hook logs live?

## Minimal repository structure

- `.github/hooks/*.json`
- `.github/hooks/scripts/`
- `.github/hooks/logs/` (usually ignored)

## Good implementation posture

- start with visible, low-risk policies
- test deny rules deliberately
- keep scripts small and auditable
- redact sensitive data in logs
