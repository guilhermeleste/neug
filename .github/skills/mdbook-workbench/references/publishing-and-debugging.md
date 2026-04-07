# Publishing and debugging

Use this reference when the request involves local preview, build output, hosting readiness, missing pages, render failures, watcher behavior, or extension-related failures.

## Core rule

Debug the book in this order:
1. project shape
2. `SUMMARY.md`
3. referenced files
4. `book.toml`
5. theme customizations
6. preprocessors and renderers

Do not start with hosting theory when the local build is not clean.

## Local preview workflow

Recommended local cycle:
1. run `mdbook serve --open`
2. edit content and config
3. confirm the browser refreshes as expected
4. only then move to final build or publishing questions

By default, `serve` runs on `localhost:3000` and watches for changes. It is for previewing HTML output, not for acting as a full production web server.

## Build workflow

Use `mdbook build` when the user needs:
- final static output
- CI validation
- a deployable `book/` directory
- confirmation that the book renders cleanly outside the preview loop

Remember:
- the output directory defaults to the `build.build-dir` value or `./book`
- non-Markdown files under the source tree are copied into the build output

## Common failure classes

### `SUMMARY.md` problems

Suspect this when:
- chapters do not appear
- the order is wrong
- build errors mention parsing or missing files
- the book structure feels disconnected from the filesystem

Check:
- file is named exactly `SUMMARY.md`
- hierarchy is valid
- referenced files exist
- prefix chapters are not nested

### Missing or re-created files

Remember that mdBook can create files listed in `SUMMARY.md` when `create-missing = true`, and `serve` can re-create deleted files that are still listed there.

If the user is confused by files coming back, inspect `SUMMARY.md` and `create-missing` first.

### Watcher issues

If preview rebuilds seem unreliable:
- confirm the user is editing watched paths
- use `extra-watch-dirs` when snippets or content live outside `src/`
- consider watcher backend issues and change the `serve` watcher mode if needed
- remember `.gitignore` entries in the book root can suppress automatic rebuild triggers for matching files

### Theme breakage

Suspect theme issues when:
- pages render without expected elements
- header or head content is malformed
- layout breaks after custom theme work

Check overrides in:
- `theme/index.hbs`
- `theme/head.hbs`
- `theme/header.hbs`
- `theme/book.js`
- CSS overrides

Temporarily reduce customization to isolate the failure.

### Preprocessor or renderer issues

Suspect these when:
- included files do not expand as expected
- custom plugins fail during build
- HTML output differs drastically after introducing an extension

Check:
- whether default preprocessors are disabled
- whether the preprocessor is bound to the correct renderer
- whether the expected external executable exists for custom plugins
- whether using the `markdown` renderer would help inspect post-preprocessor output

## Publishing guidance

For publishing readiness, confirm:
- local `mdbook build` succeeds cleanly
- `build-dir` is intentional
- `site-url` matches the deploy path when needed
- custom 404 behavior is configured only if hosting requires it
- repository/edit links are correct if exposed publicly

## Strong operational checklists

### Quick preview checklist

- run `mdbook serve --open`
- confirm pages appear in the correct order
- confirm links work
- confirm CSS/JS load
- confirm assets render

### Final build checklist

- run `mdbook build`
- inspect the build directory
- confirm non-Markdown assets are present
- spot-check a few pages in the built output
- verify hosting-specific path assumptions

### Extension debugging checklist

- disable recent customization or plugin changes
- rebuild with minimal config
- reintroduce changes one layer at a time
- use the markdown renderer for preprocessor debugging if needed

## Strong recommendation

When something breaks, reduce the book to the simplest working path and add complexity back in layers.
