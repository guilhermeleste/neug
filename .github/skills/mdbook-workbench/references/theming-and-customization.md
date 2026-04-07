# Theming and customization

Use this reference when the request involves presentation, branding, theme overrides, CSS, JavaScript, HTML output options, or navigation polish.

## Core rule

Start with the HTML renderer options and light CSS before reaching for full theme overrides.

The goal is to improve the reading experience without making the book fragile to maintain.

## Customization ladder

Use this escalation order:

1. chapter structure and naming
2. HTML renderer configuration in `book.toml`
3. `additional-css`
4. `additional-js`
5. selective overrides in `theme/`
6. deeper template-level changes

Do not jump directly to template overrides when spacing, colors, or minor UI changes are enough.

## HTML renderer options worth using first

Commonly useful options in `[output.html]`:
- `default-theme`
- `preferred-dark-theme`
- `additional-css`
- `additional-js`
- `no-section-label`
- `git-repository-url`
- `git-repository-icon`
- `edit-url-template`
- `site-url`
- `input-404`
- `sidebar-header-nav`
- `smart-punctuation`
- `definition-lists`
- `admonitions`

Use these before advising structural theme changes.

## Light branding with CSS

Recommend `additional-css` when the user wants:
- color tuning
- typography changes
- spacing adjustments
- smaller visual polish
- minor layout refinements

Starter example:

```toml
[output.html]
additional-css = ["custom.css"]
```

Then place `custom.css` under the source tree where the book can include it.

## Adding behavior with JavaScript

Recommend `additional-js` only when the user truly needs extra client-side behavior and can maintain it.

Starter example:

```toml
[output.html]
additional-js = ["custom.js"]
```

## Theme directory overrides

The default HTML renderer theme can be selectively overridden by creating a `theme/` directory next to `src/` and replacing only the files that need to change.

Important override targets:
- `index.hbs`
- `head.hbs`
- `header.hbs`
- `book.js`
- `css/chrome.css`
- `css/general.css`
- `css/print.css`
- `css/variables.css`

Prefer selective overrides. Do not fork more files than needed.

## Practical guidance by need

### Need: more professional docs look

Usually recommend:
- improve chapter names and grouping first
- set `default-theme` and `preferred-dark-theme`
- add `custom.css`
- add repository and edit links if useful

### Need: stronger brand identity

Usually recommend:
- `additional-css`
- `head.hbs` only if custom meta or assets are required
- selective variable overrides before template surgery

### Need: top-level layout change

Only then recommend:
- `index.hbs`
- `header.hbs`
- deeper CSS overrides

### Need: improve discoverability

Consider:
- better nav structure
- `no-section-label` if numbering is cluttering a reader-facing book
- repository/edit links
- 404 page and site-url hygiene for hosted books

## Anti-patterns

Avoid:
- overriding templates for simple color changes
- mixing heavy JS custom behavior into a simple docs site without need
- treating visual polish as a substitute for poor chapter architecture
- copying large chunks of the default theme without knowing what changed

## Review checklist

When reviewing customization choices, ask:
- did the user solve structure before styling?
- could `additional-css` handle this need?
- are template overrides minimal and deliberate?
- are repository or edit links useful for the audience?
- does the hosting config match `site-url` and 404 needs?
- is dark theme behavior intentional?

## Strong recommendation

For most teams, the sustainable default is:
- better structure
- modest HTML renderer options
- one `custom.css`
- minimal template overrides
