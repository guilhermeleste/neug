# Debugging with Copilot

## Default approach

Use Copilot to turn a vague failure into a bounded diagnosis.

## Workflow

1. Reproduce the problem.
2. Make the failing surface explicit.
3. Use `copilot-debug` when starting the app through a command-line entry point is the right path.
4. Inspect stack traces, logs, failing tests, and runtime symptoms.
5. Ask for root-cause hypotheses ranked by evidence.
6. Patch the smallest fix.
7. Re-run the failing scenario.

## Good prompts

- explain the most likely cause of this stack trace
- identify where state becomes invalid
- compare the failing and expected control flow
- suggest the smallest patch and how to verify it

## Avoid

- asking for a fix before reproducing the problem clearly
- skipping the re-run after the patch
