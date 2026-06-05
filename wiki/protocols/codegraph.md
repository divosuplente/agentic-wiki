# CodeGraph

**Category:** protocols
**Status:** active
**Added:** 2026-05-20
**Last verified:** 2026-05-20
**Tags:** context, mcp, tool
**Type:** reference
**Level:** intermediate

## Description
CodeGraph is a pre-indexed code knowledge graph that enhances AI coding agents (Claude Code, Cursor, Codex, OpenCode) by providing semantic code intelligence locally. It reduces tool calls by 94% and improves exploration speed by 71% on average across six real-world codebases, operating entirely offline with a SQLite database — no data leaves your machine, no API keys required.

## Key Features
- **Smart Context Building:** One tool call returns entry points, related symbols, and code snippets
- **Framework-Aware Routing:** Recognizes web-framework files and links URL patterns to handlers across 13 frameworks (Django, Flask, FastAPI, Express, Laravel, Rails, Spring, and more)
- **100% Local Operation:** SQLite database — no API keys, no network calls
- **19+ Language Support:** TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Dart, Svelte, Liquid, Pascal/Delphi
- **MCP Server Mode:** `codegraph serve --mcp`

## Installation

```bash
npm install -g @colbymchenry/codegraph
codegraph init -i
```

## MCP Configuration

```json
{
  "mcpServers": {
    "codegraph": {
      "type": "stdio",
      "command": "codegraph",
      "args": ["serve", "--mcp"]
    }
  }
}
```

## Links
- [GitHub](https://github.com/colbymchenry/codegraph)
- [npm](https://www.npmjs.com/package/@colbymchenry/codegraph)
- [Source Summary](../sources/codegraph-repo.md)

## Related Pages
- [Context7](context7.md)
- [MCP Server](../glossary.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Draw.io MCP](drawio-mcp.md)
- [Knowledge Graph](../glossary.md)
