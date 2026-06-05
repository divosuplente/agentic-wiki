# Opencode Dynamic Context Pruning

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, token-optimizer
**Type:** reference
**Level:** intermediate

## Description
Dynamic context pruning plugin for OpenCode — intelligently manages conversation context to optimize token usage. Automatically reduces token usage by managing conversation context with compression, deduplication, and error purging.

## How It Works

### Compress
A tool exposed to the model that replaces closed, stale conversation content with high-fidelity technical summaries. Two modes:
- **Range mode** (default): compresses contiguous spans into block summaries
- **Message mode** (experimental): compresses individual messages

When a new compression overlaps an earlier one, the earlier summary is nested inside the new one so information is preserved through layers.

### Deduplication
Identifies repeated tool calls (same tool, same arguments) and keeps only the most recent output.

### Purge Errors
Prunes inputs from errored tool calls after a configurable number of turns (default: 4). Error messages preserved; potentially large input content removed.

## Commands
- `/dcp` — available commands
- `/dcp context` — token usage breakdown by category
- `/dcp stats` — cumulative pruning statistics
- `/dcp sweep` — prunes all tools since last user message
- `/dcp compress [focus]` — trigger single compress
- `/dcp decompress <n>` — restore compression by ID
- `/dcp manual [on|off]` — toggle manual mode

## Configuration
| Location | Path |
|----------|------|
| Global | `~/.config/opencode/dcp.jsonc` |
| Custom | `$OPENCODE_CONFIG_DIR/dcp.jsonc` |
| Project | `.opencode/dcp.jsonc` |

## Protected Tools (Default)
`task`, `skill`, `todowrite`, `todoread`, `compress`, `batch`, `plan_enter`, `plan_exit`, `write`, `edit`

## Impact on Prompt Caching
- Cache hit rates approximately 85% with DCP vs 90% without
- Trade-off: lose some cache reads but gain token savings and fewer hallucinations
- No impact for request-based billing (GitHub Copilot) or uniform pricing (Cerebras)

## Supported Providers
OpenCode Go, Cursor, GitHub Copilot, OpenAI, Kimi Code, Alibaba Coding Plan, Chutes AI, Google Antigravity, Z.ai Coding Plan, and more.

## GitHub
- Owner: Opencode-DCP
- Stars: 2.9k | Forks: 154
- License: AGPL-3.0-or-later
- Primary Languages: TypeScript 85.3%, Python 11.1%

## Links
- [Repository](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)
- [npm](https://www.npmjs.com/package/@tarquinen/opencode-dcp)

## Prerequisites
- [OpenCode installed](../execution-surfaces/opencode.md)
- Familiarity with token usage and context windows

## Next Steps
- [Caveman for output compression](caveman.md)
- [Multi-session management with ensembles](../governance/opencode-ensemble.md)

## Related Pages
- [Caveman](caveman.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
