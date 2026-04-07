# MCP extension authoring in VS Code

## Scope

This module is only for extension-authoring tasks, not ordinary workspace use.

## When to use

Use this reference when the user explicitly wants to build or expose MCP server definitions from a VS Code extension.

## Core idea

Register MCP server definitions through the VS Code extension API so the editor can discover and resolve MCP server configurations.

## Design concerns

- which server definitions are exposed
- how configuration is resolved
- activation and lifecycle of the provider
- how users authenticate or configure the integration
- what safety boundaries exist around the exposed capability

## Not for

- ordinary project-level Copilot customization
- basic use of MCP servers already available in the workspace
