# Browser agent tools

## When to use

Use browser agent tools when the correctness of the change depends on the actual browser experience.

Typical cases:
- end-to-end validation of UI flows
- form interactions
- navigation behavior
- verifying visible errors or broken rendering
- collecting screenshots or confirming outcomes after an implementation

## Typical loop

1. Start or identify the app entry point.
2. Ask the agent to exercise the flow in the integrated browser.
3. Capture failures precisely.
4. Patch the code.
5. Re-run the flow.

## Good uses

- regression checks after refactors
- validating a feature walkthrough
- reproducing a bug before fixing it
- smoke-testing a user path

## Bad uses

- replacing all deterministic unit and integration tests with browser automation
- browsing aimlessly without a test objective
