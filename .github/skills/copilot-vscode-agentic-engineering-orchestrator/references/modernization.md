# Modernizing legacy code

## Goal

Improve an old codebase incrementally without losing operational control.

## Suggested pattern

1. map the current state
2. identify modernization seams
3. add safety nets: tests, logs, feature flags, or compatibility layers
4. modernize one seam at a time
5. review and verify each step

## Good modernization targets

- replace deprecated language patterns
- update module structure
- remove obsolete APIs
- improve testability before deeper rewrites

## Avoid

- full rewrites framed as modernization
- migrating everything in one pass without guardrails
