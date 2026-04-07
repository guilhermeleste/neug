# Subagents

## Purpose

Subagents are for isolated, focused subtasks.

## Use subagents when

- a task benefits from context isolation
- multiple analyses can run in parallel
- you want a main agent to delegate research or review
- a custom agent should act as a specialist helper

## Good subagent tasks

- analyze one subsystem
- review a diff against a rubric
- research a dependency upgrade path
- inspect tests or logs independently

## Guidance

- define subagent use in custom agent instructions when you need consistent behavior
- keep the subtask narrow and the expected output explicit
- do not delegate everything; reserve subagents for real isolation wins

## Control points for custom agents

When designing custom agents that may act as subagents, explicitly think about:
- whether the agent should be user-invocable
- whether it should be callable by other agents
- which tools it really needs
