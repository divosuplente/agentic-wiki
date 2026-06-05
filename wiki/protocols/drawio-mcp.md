# Draw.io MCP

**Category:** protocols
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** mcp, tool
**Type:** reference
**Level:** intermediate

## Description
The official draw.io MCP (Model Context Protocol) server that enables LLMs to create and open diagrams in the draw.io editor. Four approaches for integrating draw.io with AI assistants.

## Four Ways to Create Diagrams

| Approach | How It Works | Output | Install | Best For |
|----------|--------------|--------|---------|----------|
| **MCP App Server** | Renders diagrams inline in chat | Interactive viewer in conversation | No install (hosted at `mcp.draw.io`) | Inline previews |
| **MCP Tool Server** | Opens diagrams in browser | draw.io editor in new tab | `npx @drawio/mcp` | Local desktop workflows |
| **Skill + CLI** | Generates `.drawio` files | `.drawio`, PNG, SVG, PDF | Copy skill file | Local development |
| **Project Instructions** | Claude generates draw.io URLs | Clickable link to draw.io | No install — just paste | Quick setup |

### MCP App Server (Inline Preview)
Hosted endpoint at `https://mcp.draw.io/mcp`. Add as remote MCP server in Claude.ai or any MCP Apps-compatible host.

**Tools:**
- `create_diagram` — renders draw.io XML as interactive diagram inline
- `search_shapes` — searches 10,000+ shapes across all draw.io libraries (AWS, Azure, GCP, P&ID, electrical, Cisco, Kubernetes, UML, BPMN)

### MCP Tool Server (Browser Editor)
```bash
npx @drawio/mcp
```
- Supports XML, CSV, Mermaid.js formats
- Lightbox and dark mode options
- Published as `@drawio/mcp` on npm

### Skill + CLI (File Generation)
No MCP setup required. Copy a skill file into Claude Code.

- Generates native `.drawio` files
- Optional export to PNG, SVG, PDF (embedded XML keeps files editable)
- Desktop CLI: `drawio --embed-diagram`

### Project Instructions (No Install)
Add instructions to a Claude Project teaching Claude to generate draw.io URLs via Python. Zero installation.

## XML Reference
Single source of truth: `shared/xml-reference.md`
- Edge routing, containers, layers, tags, metadata
- Dark mode, style properties, XML well-formedness
- All four approaches use this file for LLM prompts

## Shape Search Index
Pre-built index of all draw.io shapes, generated from draw.io client source code. Captures 10,000+ shapes across all stencil libraries.

## GitHub
- Owner: jgraph
- Stars: 3.9k | Forks: 239
- License: Apache-2.0
- Primary Language: JavaScript 99.9%

## Links
- [Repository](https://github.com/jgraph/drawio-mcp)
- [npm](https://www.npmjs.com/package/@drawio/mcp)
- [draw.io](https://www.draw.io)
- [MCP Specification](https://modelcontextprotocol.io/)

## Related Pages
- [MCP Server](../glossary.md)
- [OpenCode](../execution-surfaces/opencode.md)
