# Tutorials and course material in mdBook

Use this reference when the user wants guided learning, onboarding journeys, workshops, or course-style documentation.

## Core rule

Treat tutorials and course material as **learning sequences**, not as flat documentation trees.

The reader should always know:
- where to start
- what they need first
- what step comes next
- how to verify success
- what to do if something fails

## When mdBook is a strong fit

mdBook works especially well when the material benefits from:
- chapter-by-chapter progression
- clear left-nav hierarchy
- local preview while authoring
- lightweight static publishing
- code snippets and included files

## Tutorial architecture

Use this pattern when the goal is hands-on learning:
- introduction
- prerequisites
- setup
- lesson 1
- lesson 2
- lesson 3
- recap
- troubleshooting
- next steps

### Tutorial design rules

- Keep chapters short.
- Each chapter should have one dominant learning outcome.
- Put checkpoints near the end of each chapter.
- Put common mistakes where the reader will hit them, not only in a global appendix.
- Avoid long conceptual detours in the middle of a procedural sequence.

## Course architecture

Use this pattern when the material is broader and more modular:
- course introduction
- module 1
  - lesson 1
  - lesson 2
  - exercise
- module 2
  - lesson 1
  - lesson 2
  - exercise
- review / recap
- glossary / appendix

### Course design rules

- Use predictable naming for modules and lessons.
- Preserve a visible progression in the nav.
- Put exercises under the module they reinforce.
- Keep optional readings clearly separate from required path material.

## Split concepts from steps

A common failure mode is mixing:
- explanatory theory
- procedural steps
- reference facts

Recommended fix:
- keep the main tutorial chapters procedural
- move reusable theory into concept chapters or appendices
- move stable reference material into a separate section

## Good chapter shape for tutorials

Use a chapter template like this:
- goal
- prerequisites
- steps
- checkpoint
- common mistakes
- next chapter

## Good chapter shape for lessons

Use a lesson template like this:
- learning objective
- explanation
- worked example
- exercise or prompt
- recap

## Anti-patterns

Avoid:
- chapters that combine multiple unrelated tasks
- lesson titles that do not describe the outcome
- long unbroken chapters with no checkpoints
- deep nesting for a short tutorial
- burying setup requirements inside lesson 3
- mixing optional enrichment material into the main path without labeling it

## Suggested starter tree: tutorial

```text
src/
  introduction.md
  prerequisites.md
  setup.md
  lesson-1.md
  lesson-2.md
  lesson-3.md
  troubleshooting.md
  next-steps.md
```

## Suggested starter tree: course

```text
src/
  introduction.md
  module-1/
    overview.md
    lesson-1.md
    lesson-2.md
    exercise.md
  module-2/
    overview.md
    lesson-1.md
    lesson-2.md
    exercise.md
  recap.md
  glossary.md
```

## Review checklist

When reviewing tutorial or course material, ask:
- is the entry point obvious?
- is the learning path visible in the nav?
- does each chapter have one clear purpose?
- are prerequisites early and explicit?
- are checkpoints present?
- are exercises attached to the right module?
- is troubleshooting placed where learners actually need it?

## Strong recommendation

If the book's main value is guided learning, optimize the nav for progression first and reference completeness second.
