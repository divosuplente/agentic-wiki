# Paseo

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** orchestration, harness, platform
**Type:** reference
**Level:** advanced

## Description
One interface for all your Claude Code, Codex, and OpenCode agents. Run agents in parallel on your own machines. Ship from your phone or your desk.

Paseo runs a local daemon managing coding agents. Clients (desktop app, mobile app, web app, CLI) connect to it. Self-hosted, privacy-first, cross-device.

## Key Features
- **Self-hosted**: Agents run on your machine with your full dev environment
- **Multi-provider**: Claude Code, Codex, and OpenCode through same interface
- **Voice control**: Dictate tasks or talk through problems hands-free
- **Cross-device**: iOS, Android, desktop, web, and CLI
- **Privacy-first**: No telemetry, tracking, or forced log-ins
- **Team skills**: handoff, loop, advisor, committee

## Getting Started

### Desktop App (Recommended)
Download from [paseo.sh/download](https://paseo.sh/download). Daemon starts automatically.

### CLI
```bash
npm install -g @getpaseo/cli
paseo
```

## CLI Commands
```bash
paseo run --provider claude/opus-4.6 "implement user authentication"
paseo run --provider codex/gpt-5.4 --worktree feature-x "implement feature X"
paseo ls                           # list running agents
paseo attach abc123                # stream live output
paseo send abc123 "also add tests" # follow-up
paseo --host workstation.local:6767 run "run tests"
```

## Skills
```bash
npx skills add getpaseo/paseo
```

- `/paseo-handoff` — hand off work between agents (e.g., plan with Claude, implement with Codex)
- `/paseo-loop` — loop agent against clear acceptance criteria with verifier
- `/paseo-advisor` — single agent as advisor for second opinion
- `/paseo-committee` — committee of two contrasting agents for root cause analysis

## Development (Monorepo)
- `packages/server` — Paseo daemon (orchestration, WebSocket API, MCP server)
- `packages/app` — Expo client (iOS, Android, web)
- `packages/cli` — `paseo` CLI
- `packages/desktop` — Electron desktop app
- `packages/relay` — Remote connectivity
- `packages/website` — Marketing site and docs

## Configuration
Self-hosted relays use `ws://` by default. TLS requires:
```
PASEO_RELAY_ENDPOINT=127.0.0.1:8080
PASEO_RELAY_PUBLIC_ENDPOINT=relay.example.com:443
PASEO_RELAY_USE_TLS=true
```

## GitHub
- Owner: getpaseo
- Stars: 6.4k | Forks: 593
- License: AGPL-3.0
- Primary Languages: TypeScript 98.4%

## Links
- [Repository](https://github.com/getpaseo/paseo)
- [Website](https://paseo.sh)
- [Docs](https://paseo.sh/docs)

## Related Pages
- [Oh My OpenAgent](oh-my-openagent.md)
- [Vibe Kanban](../governance/vibe-kanban.md)
- [OpenCode](../execution-surfaces/opencode.md)
