# API documentation in mdBook

Use this reference when the user wants to use mdBook for API documentation or for a hybrid of API guides and technical reference.

## Core rule

Use mdBook for **editorial API documentation**, not as a raw schema dump.

A strong mdBook API site explains:
- what the API is for
- how to authenticate
- what conventions apply
- how common workflows work end to end
- what errors mean in practice
- where to find stable reference pages

If the user mainly wants machine-generated endpoint reference, suggest pairing mdBook with a dedicated schema or reference generator instead of forcing mdBook to do all the work.

## Recommended information architecture

A strong default shape is:
- introduction
- authentication
- conventions
- main resources or domains
- common workflows / recipes
- errors and troubleshooting
- reference appendix

This works well because readers usually need context before raw endpoint detail.

## Recommended chapter roles

### Overview

Use for:
- what the API does
- who it is for
- base concepts
- versioning model
- environment overview

### Authentication

Use for:
- credentials
- token flow
- headers
- environment separation
- permission model at a practical level

### Conventions

Use for:
- naming rules
- pagination
- filtering
- sorting
- idempotency
- timestamps
- request / response conventions
- status code patterns

### Resources or domains

Group by business object or bounded context, not by random endpoint order.

Examples:
- projects
- users
- media assets
- invoices
- organizations

Each section should explain the model before enumerating actions.

### Workflows and recipes

Use for:
- multi-step integrations
- common use cases
- onboarding flows
- error recovery patterns
- recommended sequence of calls

This section is often more valuable than endpoint-by-endpoint repetition.

### Errors and troubleshooting

Separate this from endpoint reference.

Use for:
- authentication failures
- validation failures
- rate limits
- permission failures
- partial failure handling
- retry guidance

### Reference appendix

Use for:
- stable field descriptions
- enums
- object schemas
- headers
- reusable error shapes
- compact endpoint summaries

## Good mdBook patterns for API docs

### Pattern: concept before endpoint

Prefer this order:
1. explain the object or domain
2. explain common tasks
3. show examples
4. give compact reference details

### Pattern: workflow-first onboarding

If the audience is integration-focused, start with a happy-path recipe before a full reference tree.

### Pattern: resource families

Group related operations under one resource chapter instead of creating one nav entry per endpoint unless the API is very small.

## Anti-patterns

Avoid:
- one chapter per trivial endpoint
- mixing auth, conventions, and endpoint details randomly
- copying raw OpenAPI material without editorial cleanup
- burying common workflows under a giant reference section
- putting troubleshooting only inside endpoint pages

## Suggested starter tree

```text
src/
  introduction.md
  authentication.md
  conventions.md
  resources/
    projects.md
    users.md
    organizations.md
  workflows/
    create-and-publish.md
    sync-data.md
  errors.md
  reference/
    objects.md
    enums.md
    headers.md
```

## Suggested SUMMARY.md shape

```md
# Summary

- [Introduction](introduction.md)
- [Authentication](authentication.md)
- [Conventions](conventions.md)

- [Resources](#)
  - [Projects](resources/projects.md)
  - [Users](resources/users.md)
  - [Organizations](resources/organizations.md)

- [Workflows](#)
  - [Create and Publish](workflows/create-and-publish.md)
  - [Sync Data](workflows/sync-data.md)

- [Errors and Troubleshooting](errors.md)

- [Reference](#)
  - [Objects](reference/objects.md)
  - [Enums](reference/enums.md)
  - [Headers](reference/headers.md)
```

## Review checklist

When reviewing API docs in mdBook, ask:
- is onboarding possible without reading every page?
- are conventions separated from endpoint detail?
- are resource chapters grouped by business meaning?
- do workflows exist for common tasks?
- is reference material clearly marked as reference?
- are errors centralized enough to be reusable?

## Strong recommendation

For most teams, the best mdBook API docs combine:
- one conceptual entry point
- one conventions layer
- one workflow layer
- one compact reference layer

Do not let the navigation become a mirror of the router table.
