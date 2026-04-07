# SUMMARY.md design guide

Use this reference when the request involves chapter order, hierarchy, book structure, missing chapters, or navigation quality.

## Why this file matters

`SUMMARY.md` is the navigation spine of an mdBook. It determines which chapters appear, in what order, and at what hierarchy. If the navigation is weak, the book feels weak even when the chapter text is good.

## Mental model

Treat `SUMMARY.md` as a reader-facing table of contents, not as a dump of all files.

A good `SUMMARY.md` should answer:
- what should be read first?
- what belongs together?
- what is optional reference versus mainline reading?
- what is introductory versus advanced?

## Design priorities

1. **Reader order first**
   The order should reflect how the reader discovers or uses the material, not how the files happened to be written.

2. **Clean grouping**
   Group by purpose or mental model, not only by implementation detail.

3. **Stable chapter names**
   Titles should be descriptive enough that a reader can predict what is inside before clicking.

4. **Shallow by default**
   Do not create depth unless it improves navigation.

## Practical structure patterns

### Pattern A: Intro + sections

Use when the book has a clear reader journey.

Example shape:
- introduction
- getting started
- concepts
- guides
- reference
- troubleshooting

### Pattern B: Part-based book

Use when the book has clearly different domains or audiences.

Example shape:
- Product overview
- User workflows
- Admin workflows
- Reference

### Pattern C: Tutorial-first book

Use when the main goal is guided learning.

Example shape:
- what you will build
- prerequisites
- lesson 1
- lesson 2
- lesson 3
- recap

## Prefix chapters

Use prefix chapters for material that should come before the main numbered sections, such as:
- introduction
- foreword
- quick start

Do not nest prefix chapters.

## Anti-patterns

Avoid these common problems:

### Flat overload

Too many root entries with no grouping.

Symptom:
- navigation feels like a file list instead of a book

Correction:
- introduce section headers or regroup by function

### Deep maze

Too many nested levels for modest content.

Symptom:
- users hunt for pages instead of reading

Correction:
- flatten one or two levels

### Mixed modes

Tutorials, concepts, and reference mixed together under the same parent.

Symptom:
- readers do not know what kind of page they are opening

Correction:
- regroup by reading mode

### Placeholder sprawl

Too many empty or near-empty chapters just because the tree was planned in advance.

Symptom:
- navigation looks complete but the book is thin and frustrating

Correction:
- merge placeholders until there is enough content to justify splitting

## Review checklist

When reviewing a `SUMMARY.md`, ask:
- is the first page clearly the right entry point?
- do chapter titles describe their contents?
- are concepts separated from procedures?
- is reference material clearly marked as reference?
- does nesting improve comprehension or only reflect folder structure?
- are there tiny chapters that should be merged?
- are there huge chapters that should be split?

## Refactor strategy

When fixing a weak `SUMMARY.md`:
1. identify the reader journey
2. classify each chapter by purpose
3. reorder chapters around the journey
4. regroup siblings by role
5. simplify names
6. only then worry about styling or folder cosmetics
