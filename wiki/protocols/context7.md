# Context7

**Category:** protocols
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** context, mcp, tool
**Type:** reference
**Level:** intermediate

## Description
Context7 pulls up-to-date, version-specific documentation and code examples for any library directly into Cursor, Claude Code, Windsurf, and other AI coding tools.

Unlike static training data, Context7 queries live, version-specific documentation and code examples for any programming library or framework. This eliminates hallucinations caused by outdated knowledge and provides exact API signatures, config options, and examples.

## Key Features
- Up-to-date documentation for LLMs and AI code editors
- Version-specific docs retrieval
- Code examples included
- Compatible with Cursor, Claude Code, Windsurf, OpenCode, and other AI coding tools

## Usage (Context7 API)
```bash
# 1. Resolve library ID
npx ctx7@latest library "library-name" "your query"

# 2. Fetch docs
npx ctx7@latest docs "/org/project" "your detailed question"
```

## GitHub
- [upstash/context7](https://github.com/upstash/context7)

## Integration Example
Many agent harnesses integrate Context7 as a built-in MCP, including oh-my-openagent. It serves as a research sub-agent for external doc lookups.

## Prerequisites
- An MCP-compatible agent (OpenCode, Claude Code, etc.)

## Next Steps
- [Draw.io MCP](drawio-mcp.md)
- [CodeGraph](codegraph.md)

## Related Pages
- [MCP Server](../glossary.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
