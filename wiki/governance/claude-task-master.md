# Claude Task Master

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** orchestration, harness, sdd
**Type:** reference
**Level:** intermediate

## Description
An AI-powered task-management system you can drop into Cursor, Lovable, Windsurf, Roo, and others. Works with Claude and is designed for seamless AI-driven development.

Taskmaster lets your AI agent parse PRDs, generate tasks, track progress, and research fresh information — all within your editor.

## Quick Start — MCP Recommended

### One-Click Install for Cursor 1.0+
Use Cursor's MCP install badge, then add API keys.

### Claude Code Quick Install
```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
```

## Common Commands
- `Initialize taskmaster-ai in my project`
- `Parse my PRD at scripts/prd.txt`
- `What's the next task I should work on?`
- `Can you help me implement task 3?`
- `Research the latest best practices for JWT authentication with Node.js`

## Tool Loading Optimization
| Mode | Tools | Context Usage | Use Case |
|------|-------|--------------|----------|
| `all` (default) | 36 | ~21,000 tokens | Complete feature set |
| `standard` | 15 | ~10,000 tokens | Common operations |
| `core` / `lean` | 7 | ~5,000 tokens | Essential workflow |
| `custom` | Variable | Variable | Specific tools |

## Requirements
One of the following provider keys:
- Anthropic API key (Claude)
- OpenAI API key
- Google Gemini API key
- Perplexity API key (research model)
- Claude Code / Codex CLI (no API key)

## Licensing
MIT with Commons Clause:
- ✅ Use for any purpose, modify, distribute
- ❌ Sell Task Master itself, offer as hosted service, or create competing products

## GitHub
- Owner: eyaltoledano
- Stars: 27.2k | Forks: 2.5k
- By: @eyaltoledano & @RalphEcom
- Primary Languages: JavaScript 51.6%, TypeScript 43.8%

## Links
- [Repository](https://github.com/eyaltoledano/claude-task-master)
- [Documentation](https://tryhamster.com/docs/taskmaster)
- [Discord](https://discord.gg/taskmasterai)

## Related Pages
- [OpenSpec](../specs/openspec.md)
- Cursor
- Windsurf
- Taskmaster AI
