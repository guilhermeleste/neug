---
name: mdbook-workbench
description: use this skill when chatgpt needs to create, structure, review, refactor, customize, troubleshoot, or publish documentation projects built with mdbook; especially for product documentation, api documentation, tutorials, course material, handbooks, or other markdown-first documentation that needs clean navigation, summary-driven hierarchy, book.toml configuration, theme customization, preprocessors, renderers, or html output workflows.
---

# mdbook workbench

Use this skill as an editorial and operational workbench for mdBook.

mdBook is strongest when the user needs a clean, chapter-based documentation site with explicit hierarchy, local preview, and lightweight customization. Treat `SUMMARY.md` as the spine of the project and `book.toml` as the configuration center.

## Workflow decision tree

1. Classify the request into one of these intents:
   - `create`: start a new mdBook from scratch
   - `structure`: turn loose markdown or a docs folder into an mdBook structure
   - `review`: assess an existing mdBook for quality, clarity, and fit
   - `refactor`: reorganize chapters, sections, or naming
   - `style`: improve theme, navigation, presentation, or customization strategy
   - `debug`: diagnose build, preview, theme, summary, or config problems
   - `publish`: prepare the book for final build, hosting, or CI

2. Identify the document type:
   - `product-docs`
   - `api-docs`
   - `tutorials`
   - `course-material`
   - `handbook`
   - `general-tech-book`

3. Identify the project state:
   - `idea-only`
   - `empty-folder`
   - `markdown-loose`
   - `mdbook-existing`
   - `repo-existing`
   - `partial-artifacts`

4. Deliver the smallest useful output:
   - `plan`: editorial architecture and recommendation
   - `scaffold`: tree, `book.toml`, `SUMMARY.md`, and starter chapter set
   - `audit`: structural review with concrete problems and a reorganization proposal
   - `files`: ready-to-copy file contents
   - `steps`: operational checklist or troubleshooting sequence

Ask follow-up questions only when the answer would materially change the book structure or the output format. Prefer making a strong first proposal over opening with a large questionnaire.

## Core operating rules

- Start with information architecture before visual customization.
- Separate tutorial flow, conceptual explanation, and reference content when that improves navigation.
- Keep chapter names concrete and predictable.
- Use shallow, readable hierarchies unless the content volume clearly justifies deeper nesting.
- Recommend `additional-css` for light styling changes before suggesting full template overrides.
- Treat preprocessors and custom renderers as advanced features; only surface them when the use case actually needs them.
- For debugging, inspect in this order: project structure, `SUMMARY.md`, `book.toml`, theme/customization, preprocessors/renderers.

## Intent-specific workflows

### create

Use when the user is starting from an idea, empty folder, or rough plan.

1. Decide whether mdBook is a good fit.
2. Choose the most suitable documentation pattern using `references/content-architecture.md`.
3. Propose a chapter map before discussing styling.
4. Generate a starter `SUMMARY.md` and `book.toml`.
5. If the user wants implementation-ready output, provide starter chapter files.

Default output:
- `plan` for exploratory requests
- `scaffold` or `files` when the user wants to start immediately

### structure

Use when the user has loose markdown, an existing docs folder, or a repository with mixed documentation.

1. Group content by purpose: tutorial, concept, task, reference, policy, appendix.
2. Propose a navigation model and chapter order.
3. Convert the proposed structure into a `SUMMARY.md`.
4. Identify missing chapters, redundant chapters, and mixed-scope chapters.

Consult:
- `references/content-architecture.md`
- `references/summary-design.md`
- `references/api-docs.md` when the material is API-facing
- `references/tutorials-and-courses.md` when the material is guided learning

Default output:
- `plan` or `scaffold`

### review

Use when the user wants assessment rather than generation.

Review these dimensions:
- whether the book matches the correct documentation mode
- fit between audience and structure
- clarity of chapter grouping
- navigation quality in `SUMMARY.md`
- misuse of deep nesting
- mixture of tutorial and reference in the same section
- configuration clarity in `book.toml`
- sustainability of styling/customization choices

Default output:
- `audit`

### refactor

Use when the user already has an mdBook but its structure is weak.

1. Diagnose structural problems.
2. Preserve working content where possible.
3. Reframe the hierarchy using `references/summary-design.md`.
4. Return either an improved `SUMMARY.md` or a full revised chapter tree.

Default output:
- `audit`
- `files` when the user wants replacement content

### style

Use when the user wants stronger presentation or light branding.

1. Determine whether the need is light CSS, HTML renderer configuration, or full theme override.
2. Prefer `additional-css` and renderer options first.
3. Recommend theme overrides only when the user needs layout-level or template-level changes.
4. Explain sustainability tradeoffs when custom templates are introduced.

Consult:
- `references/book-toml-cookbook.md`
- `references/theming-and-customization.md`

Default output:
- `plan`
- `files` for concrete config or CSS snippets

### debug

Use when the book does not build, render, preview, or behave as expected.

Check in this order:
1. Does the project have the expected mdBook shape?
2. Is `SUMMARY.md` valid, strict, and complete?
3. Do all referenced chapter files exist?
4. Does `book.toml` contain conflicting or incorrect build/output settings?
5. Did theme changes break rendering?
6. Are preprocessors or custom renderers involved?

Default output:
- `steps`

### publish

Use when the user wants a clean final build or hosting readiness.

1. Confirm the book builds successfully.
2. Confirm output assumptions such as build directory and site URL.
3. Identify whether the user needs only static output or CI/hosting guidance.
4. Keep the answer concrete and operational.
5. Use `references/publishing-and-debugging.md` for final preview, build, and failure isolation guidance.

Default output:
- `steps`
- `plan` for CI or deployment architecture

## Output contracts

### plan

Use this structure:
- brief diagnosis
- recommended mdBook strategy
- proposed section and chapter layout
- why this structure fits the content
- next implementation step

### scaffold

Use this structure:
- project tree
- `book.toml`
- `src/SUMMARY.md`
- starter chapter list with each chapter's purpose

### audit

Use this structure:
- what is working
- structural problems
- navigation problems
- configuration or styling concerns
- proposed reorganization
- specific replacement outline or file changes

### files

When providing file contents, always label each block with its path.

### steps

Use this structure:
- probable cause
- checks in order
- correction
- validation command or final verification step

## References

Load these references only when needed for the active task:

- `references/content-architecture.md`
- `references/summary-design.md`
- `references/book-toml-cookbook.md`
- `references/api-docs.md`
- `references/tutorials-and-courses.md`
- `references/theming-and-customization.md`
- `references/publishing-and-debugging.md`
- `references/output-contracts.md`
