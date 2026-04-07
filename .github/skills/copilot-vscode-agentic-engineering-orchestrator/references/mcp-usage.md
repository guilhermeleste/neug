# MCP usage in workflows

## Use MCP for capability, not novelty

MCP is justified when the workflow needs access to tools, systems, or information outside the local workspace.

## Common reasons

- internal documentation or knowledge systems
- ticketing systems
- deployment or operations tools
- product APIs or data sources
- structured organization knowledge

## Design checklist

- what capability gap exists without MCP?
- which server or tool closes that gap?
- which agent or prompt should use it?
- what is the smallest safe tool surface?
- how will the user verify results from MCP-backed actions?

## Good pattern

Pair MCP with:
- a custom agent for scoped usage
- a plan for when the external system should be consulted
- an audit or review step if the tool can cause change
