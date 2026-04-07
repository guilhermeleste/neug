# Content architecture for mdBook

Use this reference when the main task is deciding how to shape documentation into chapters, parts, and navigation.

## Core rule

Do not start with theme or styling. Start by deciding what kind of reading experience the documentation needs.

The most common failure mode in mdBook is not technical. It is mixing different kinds of content into a navigation tree that makes sense to the author but not to the reader.

## Decide whether mdBook fits

mdBook is a good fit when the user needs:
- chapter-based reading
- explicit left-nav hierarchy
- markdown-first authoring
- local preview while writing
- a static HTML output
- light or moderate customization

mdBook is a weaker fit when the user primarily needs:
- auto-generated API reference as the main product
- a heavy CMS workflow
- complex multi-version portal behavior out of the box
- rich database-backed knowledge management

## Separate content by reading mode

When possible, separate these modes instead of mixing them in one section:

- **Overview / orientation**: what this project or product is
- **Concepts**: how the system is organized and how to think about it
- **Tasks / guides**: how to perform concrete actions
- **Tutorials**: a sequential learning path with preconditions and checkpoints
- **Reference**: stable facts, conventions, configuration, endpoints, commands
- **Troubleshooting**: common failure cases and recovery steps
- **Appendices**: glossary, changelog, migration notes, contributor notes

If the user's current docs mix all of these in one flat tree, recommend splitting them first.

## Recommended patterns by document type

### Product documentation

Default shape:
- Introduction
- Getting started
- Core concepts
- Key workflows
- Feature guides
- Troubleshooting
- FAQ or reference appendix

Good for readers who need both orientation and action.

### API documentation

Default shape:
- Overview
- Authentication
- Conventions
- Main resources or objects
- Common workflows and recipes
- Error handling
- Curated endpoint or operation reference

Important: mdBook is best for editorial API documentation, not raw schema dumps. Encourage explanatory structure instead of mechanically copying every endpoint without context.

### Tutorials

Default shape:
- What the reader will build or learn
- Prerequisites
- Sequential steps
- Checkpoints or verification
- Common mistakes
- Next steps

Keep tutorial chapters short and linear.

### Course material

Default shape:
- Course introduction
- Modules
- Lessons inside each module
- Exercises
- Suggested readings
- Review or recap material

Prefer predictable lesson naming and steady progression.

### Handbook / internal docs

Default shape:
- Orientation
- Policies or principles
- Operational playbooks
- Role-specific guides
- Troubleshooting or exceptions
- Appendices

Useful when readers need a stable reference and repeatable procedures.

## Navigation design rules

- Keep root-level sections meaningful; avoid dumping dozens of chapters at the root.
- Use parts or section headers to signal major reading modes.
- Prefer shallow trees over deep trees until deeper nesting becomes unavoidable.
- If a section is mostly procedural, group it under guides or workflows rather than concepts.
- If a section is mostly stable facts, group it under reference.
- Avoid naming chapters with vague titles such as `misc`, `notes`, `stuff`, or `advanced` unless the scope is clear.

## When to split a chapter

Split a chapter when:
- it serves multiple reading modes
- its title no longer matches its contents
- it forces excessive scrolling
- it contains many unrelated subheadings that deserve navigation entries
- it has become both tutorial and reference at the same time

## When to merge chapters

Merge chapters when:
- two chapters are too small to justify separate nav entries
- a child chapter has no independent reader value
- the distinction between sibling chapters is unclear
- the user would navigate better with one task page instead of many fragments

## Strong default recommendation

For most real projects, organize in this order:
1. orientation
2. getting started or first task
3. concepts
4. main guides
5. reference
6. troubleshooting
7. appendices

Adapt the labels to the user's domain, but preserve the editorial logic.
