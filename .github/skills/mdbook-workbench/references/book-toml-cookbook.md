# book.toml cookbook

Use this reference when the request involves mdBook configuration, build behavior, HTML output, watch behavior, or light customization.

## Working principle

Treat `book.toml` as the central configuration file for the book. Reach for it whenever the user needs to control build output, watching, preprocessors, renderers, or HTML behavior.

## Safe default starter

Use this as a minimal starter when creating a new book:

```toml
[book]
title = "Project Documentation"
authors = ["Your Team"]
description = "Documentation built with mdBook"
language = "en"

[build]
build-dir = "book"
create-missing = true
use-default-preprocessors = true
extra-watch-dirs = []

[output.html]
default-theme = "light"
preferred-dark-theme = "navy"
additional-css = []
additional-js = []
```

Adjust only what the user actually needs.

## Most useful sections

### [book]

Use for metadata and source assumptions.

Common keys:
- `title`
- `authors`
- `description`
- `language`
- `src`

Use `src` only when the user intentionally wants a non-default source directory.

### [build]

Use for build behavior.

Most useful keys:
- `build-dir`: choose output directory
- `create-missing`: create chapter files listed in `SUMMARY.md` if they do not exist
- `use-default-preprocessors`: disable built-in preprocessors only when the user has a reason
- `extra-watch-dirs`: watch external directories that feed the book

Recommend `extra-watch-dirs` when the book includes snippets or assets from outside `src/`.

### [output.html]

Use for the main HTML output behavior.

Most useful keys:
- `default-theme`
- `preferred-dark-theme`
- `additional-css`
- `additional-js`
- `theme`
- `site-url`
- `git-repository-url`
- `edit-url-template`
- `input-404`
- `smart-punctuation`
- `definition-lists`
- `admonitions`

## Configuration guidance by task

### Light visual customization

Prefer this first:

```toml
[output.html]
additional-css = ["custom.css"]
```

Recommend this when the user wants:
- spacing adjustments
- font tweaks
- minor branding
- color tuning
- small layout refinements

### Full theme override

Use `theme = "path/to/theme"` only when the user needs template-level changes or a deliberate custom theme directory.

Do not suggest a full theme override for simple CSS tweaks.

### External snippet workflow

If the user depends on files outside `src/`, recommend:

```toml
[build]
extra-watch-dirs = ["../snippets", "../shared"]
```

### Strict build discipline

If the user wants failures instead of silent file creation, recommend:

```toml
[build]
create-missing = false
```

This is useful once the project is mature and the team wants stronger discipline around missing pages.

### Disabling default preprocessors

Only recommend this when the user knows they do not want the built-in `links` and `index` behavior.

```toml
[build]
use-default-preprocessors = false
```

Explain the tradeoff before recommending it.

## Good defaults versus advanced changes

### Good defaults
- keep `build-dir = "book"`
- keep built-in preprocessors enabled
- use `additional-css` before full theme override
- use `site-url` only when the book will actually be hosted under a known path

### Advanced changes
- custom preprocessors
- custom renderers
- theme template overrides
- large JS additions

Surface advanced changes only when the use case demands them.

## Review checklist

When reviewing a `book.toml`, check:
- does it solve a real need, or is it prematurely complex?
- are theme changes lighter than they need to be?
- is `create-missing` set appropriately for the team's stage?
- are external snippet directories watched when needed?
- does hosting configuration match the actual publish target?

## Common recommendation patterns

### Recommendation: product docs starter

```toml
[book]
title = "Product Documentation"
description = "Guides, concepts, and reference"
language = "en"

[build]
build-dir = "book"
create-missing = true

[output.html]
default-theme = "light"
preferred-dark-theme = "navy"
additional-css = ["custom.css"]
```

### Recommendation: tutorial book

```toml
[book]
title = "Tutorial"
description = "Step-by-step learning path"
language = "en"

[build]
build-dir = "book"
create-missing = true

[output.html]
default-theme = "light"
preferred-dark-theme = "navy"
```

### Recommendation: stricter mature docs

```toml
[book]
title = "Team Handbook"
description = "Operational reference"
language = "en"

[build]
build-dir = "book"
create-missing = false
extra-watch-dirs = ["../shared"]

[output.html]
default-theme = "light"
preferred-dark-theme = "navy"
additional-css = ["custom.css"]
```
