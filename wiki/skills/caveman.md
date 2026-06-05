# Caveman

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, token-optimizer
**Type:** reference
**Level:** beginner

## Description
A Claude Code skill/plugin (also works with Codex, Gemini, Cursor, Windsurf, Cline, Copilot, and 30+ other agents) that makes agents talk like caveman — cutting approximately **75% of output tokens** while keeping full technical accuracy. The tagline: *"why use many token when few token do trick."*

Caveman only affects **output tokens** — thinking/reasoning tokens are untouched. The biggest win is readability and speed; cost savings are a bonus. A March 2026 paper found that constraining large models to brief responses **improved accuracy by 26 points** on certain benchmarks.

## Installation
```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```
~30 seconds. Needs Node ≥ 18.

## Key Features
- `/caveman [lite|full|ultra|wenyan]` — compress every reply with 4 levels of brevity
- `/caveman-commit` — Conventional Commit messages, ≤50 char subject
- `/caveman-review` — one-line PR comments: `L42: 🔴 bug: user null. Add guard.`
- `/caveman-stats` — real session token usage + lifetime savings + USD
- `/caveman-compress <file>` — rewrite memory files into caveman-speak (~46% input token savings)
- `caveman-shrink` — MCP middleware wrapping any MCP server, compressing tool descriptions
- `cavecrew-*` — caveman sub-agents (investigator/builder/reviewer)

## Benchmarks (Real Token Counts from Claude API)
| Task | Normal | Caveman | Saved |
|------|--------|---------|-------|
| React re-render bug | 1,180 | 159 | 87% |
| Auth middleware | 704 | 121 | 83% |
| Docker multi-stage | 1,042 | 290 | 72% |
| **Average** | **1,214** | **294** | **65%** |

## Caveman Ecosystem
- **caveman** — output compression *(you are here)*
- **cavemem** — cross-agent memory
- **cavekit** — spec-driven build loop
- **cavegemma** — Gemma 4 31B fine-tuned on caveman pairs

## GitHub
- Owner: JuliusBrussee
- Stars: 62.1k | Forks: 3.5k
- License: MIT
- Languages: JavaScript 62.9%, Python 27.6%

## Links
- [Repository](https://github.com/JuliusBrussee/caveman)
- [Website](https://getcaveman.dev/)
- [INSTALL.md](https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md)

## Prerequisites
- An AI coding agent installed
- Basic understanding of token-based LLM billing

## Next Steps
- [Dynamic context pruning for OpenCode](opencode-dynamic-context-pruning.md)
- [Write spec-driven workflows](../specs/openspec.md)

## Related Pages
- [Anthropics Skill Creator](anthropics-skill-creator.md)
- [The Agent Skills Directory](agent-skills-directory.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
- [Opencode Dynamic Context Pruning](opencode-dynamic-context-pruning.md)
