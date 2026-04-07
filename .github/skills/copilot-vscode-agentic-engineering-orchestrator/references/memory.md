# Memory design

## Two memory layers

### Local memory tool in VS Code
Use for:
- user preferences
- repository-scoped workspace knowledge
- session-scoped temporary context

### Copilot Memory
Use for:
- repository-specific insights that should help multiple Copilot surfaces
- cross-surface continuity across coding agent, review, and CLI

## Design rules

- Use local memory for working continuity inside VS Code.
- Use explicit repository artifacts for durable policy and standards.
- Treat Copilot Memory as cross-surface operational memory, not the main repository policy mechanism.

## Good memory content

- build commands
- repository conventions
- short architectural reminders
- recurring troubleshooting notes

## Bad memory content

- full policies better stored in instructions
- sprawling design docs
- temporary chatter that should remain session-local
