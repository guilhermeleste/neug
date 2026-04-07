# Observability for agentic workflows

## Principle

If agents will be used repeatedly, you need visibility into what they do.

## Minimum observability posture

- know which workflows are invoked
- know which tools are used
- know where runs fail or stall
- know the rough token and execution footprint
- know how to correlate prompts, tool calls, and outcomes

## VS Code guidance

Use OpenTelemetry-backed monitoring for Copilot Chat agent interactions when you need repeatable visibility into agent behavior.

Track at least:
- traces of agent runs
- metrics around volume and latency
- events around tool execution or failure

## Apply this to design

When you design a workflow, decide:
- which runs matter enough to instrument
- whether prompt or tool content should be captured
- which backend will receive OTel output
- who will review the telemetry

## Use cases

- piloting coding agent usage
- evaluating custom agents
- debugging tool-heavy agent flows
- auditing cost and latency patterns
