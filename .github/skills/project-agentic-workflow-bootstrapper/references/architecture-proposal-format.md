# Architecture proposal format

Use this structure before generating or updating files.

# Proposed Copilot workflow for [project]

## Project reading
- what the project appears to be
- key backend and testing surfaces
- important constraints, invariants, risky interfaces, and major flows
- whether existing workflow artifacts should be preserved

## Recommended profile
- lean / standard / rigorous
- which concrete repository scenario this profile matches
- why this is the smallest sufficient profile
- what was deliberately left out of the default profile

## Recommended optional bundles
- note explicitly when the documentation bundle is review-only rather than broad authoring
- research bundle: justified or omitted, and why
- documentation bundle: justified or omitted, and why
- security bundle: justified or omitted, and why
- hooks bundle: justified or omitted, and why

## Role graph
- visible entrypoint
- internal roles actually needed
- strict-governance roles only if rigorous is justified
- write permissions and stop conditions

## Workflow summary
- how work moves from goal to closure
- where planning happens
- where destructive review happens
- where conformance is checked, if at all
- how deviations are recorded without excess paperwork

## Skill routing
- skill
- role that should invoke it
- why
- why alternative skills were rejected or deferred

## Intentional omissions
- what mechanisms are not being added yet
- why they would be premature, redundant, or noisy
