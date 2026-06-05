# Oh My OpenAgent

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-20
**Tags:** orchestration, harness, agent
**Type:** reference
**Level:** intermediate

## Description
Oh My OpenAgent (previously oh-my-opencode) is an agent harness and operating system for AI coding assistants. It provides multi-agent orchestration, specialized discipline agents, and advanced tooling to dramatically improve development workflows across OpenCode, Codex, Claude Code, and Pi.

Install it. Type `ultrawork` (or `ulw`). Done. Everything activates. Agents don't stop until done.

## Installation
```bash
# Fetch and let your agent install it
curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md
```

## Discipline Agents (Orchestrated Ensemble)
- **Sisyphus** (main orchestrator): Plans, delegates to specialists, drives tasks to completion. Uses `claude-opus-4-7`, `kimi-k2.6`, or `glm-5.1`.
- **Hephaestus** (autonomous deep worker): Explores codebase, researches patterns, executes end-to-end. Uses `gpt-5.5`.
- **Prometheus** (strategic planner): Interview mode, asks questions, identifies scope, builds plan before code. Uses `claude-opus-4-7` or `kimi-k2.6`.

## Team Mode (v4.0)
Lead agent orchestrates a team of up to 8 category-specialized members, all running in parallel with dedicated `team_*` tools:
- `team_create`, `team_send_message`, `team_task_create`, `team_status`
- Real-time tmux visualization with focus + grid windows
- **hyperplan**: 5 hostile critics tear apart your plan from orthogonal angles
- **security-research**: 3 vulnerability hunters + 2 PoC engineers audit codebase in parallel

## Key Features
- **`ultrawork` / `ulw`**: single command activates all agents and continues until task completion
- **[Hash-Anchored Edit Tool](../glossary.md)**: `LINE#ID` content hash validates every change. Zero stale-line errors. Inspired by oh-my-pi. Success rate: 6.7% → 68.3% on Grok Code Fast.
- **LSP + AST-Grep**: Workspace rename, pre-build diagnostics, AST-aware rewrites
- **Built-in MCPs**: [Exa](https://exa.ai/) (web search), [Context7](../protocols/context7.md) (official docs), [Grep.app](https://grep.app/) (GitHub search)
- **Skill-Embedded MCPs**: Skills carry their own MCP servers that spin up on demand
- **Ralph Loop**: `/ulw-loop` — self-referential, doesn't stop until 100% done
- **Todo Enforcer**: Agent idle? System pulls it back
- **Comment Checker**: No AI slop in comments
- **Claude Code Compatible**: Hooks, commands, skills, MCPs, plugins all work
- **`/init-deep`**: Generates hierarchical AGENTS.md files automatically
- **IntentGate**: Pre-flight validation before expensive agent runs
- **TypeScript / Bun** built, MIT License, 58.7k stars, very active

## Agent Orchestration
Category → Model mapping (no manual juggling):
- `visual-engineering` → Frontend, UI/UX
- `deep` → Autonomous research + execution
- `quick` → Single-file changes
- `ultrabrain` → Hard logic, architecture (GPT-5.5 xhigh)

## Author's Philosophy
"I burned through $24K in LLM tokens on personal projects. Tried every tool. Configured everything to death. OpenCode won. This plugin is the distillation: take the best, ship it here, open source it."

### Notable Claim
> Anthropic [blocked OpenCode because of us](https://x.com/thdxr/status/2010149530486911014). The future isn't picking one winner; it's orchestrating them all.

### Loved By Professionals At
Indent, Google, Microsoft, Vercel, ELESTYLE, Deepgram

## Links
- [Repository](https://github.com/code-yeongyu/oh-my-openagent)
- [Website](https://ohmyopenagent.com/)
- [Docs](https://github.com/code-yeongyu/oh-my-openagent/tree/dev/docs)
- [Discord](https://discord.gg/PUwSMR9XNk)
- [Source Summary](../sources/oh-my-openagent-repo.md)

## Related Pages
- [Paseo](paseo.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Opencode Ensemble](opencode-ensemble.md)
- [Opencode Dynamic Context Pruning](../skills/opencode-dynamic-context-pruning.md)
- [Caveman](../skills/caveman.md)
- [Graphify](../protocols/graphify.md)