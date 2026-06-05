# OpenWork

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** platform, agent
**Type:** reference
**Level:** intermediate

## Description
The open-source alternative to Claude Cowork, powered by OpenCode. OpenWork is designed around the idea that you can easily ship your agentic workflows for your team as a repeatable, productized process.

> "Local-first, cloud-ready. Composable. Ejectable. Sharing is caring."

## Core Philosophy
- **Local-first, cloud-ready** — runs on your machine in one click. Send a message instantly.
- **Composable** — desktop app, Slack/Telegram connector, or server. Use what fits, no lock-in.
- **Ejectable** — powered by OpenCode, so everything OpenCode can do works in OpenWork, even without a UI.
- **Sharing is caring** — start solo on localhost, then explicitly opt into remote sharing when you need it.

## What's Included
- **Host mode** — runs opencode locally on your computer
- **Client mode** — connect to an existing OpenCode server by URL
- **Sessions** — create/select sessions and send prompts
- **Live streaming** — SSE `/event` subscription for realtime updates
- **Execution plan** — render OpenCode todos as a timeline
- **Permissions** — surface permission requests and reply (allow once / always / deny)
- **Templates** — save and re-run common workflows (stored locally)
- **Debug exports** — copy or export runtime debug report and developer log stream
- **Skills manager** — list installed `.opencode/skills` folders; import local skills

## Architecture
In **Host mode**, OpenWork runs a local host stack:
- Default runtime: `openwork` (installed from `openwork-orchestrator`), which orchestrates `opencode`, `openwork-server`, and optionally `opencode-router`
- Fallback runtime: `direct`, where the desktop app spawns `opencode serve --hostname 127.0.0.1 --port <free-port>`

The UI uses `@opencode-ai/sdk/v2/client` to connect, list/create sessions, send prompts, subscribe to SSE events, read todos, and handle permission requests.

## Alternate UIs
- **OpenWork Orchestrator (CLI host)** — run OpenCode + OpenWork server without the desktop UI
  ```bash
  npm install -g openwork-orchestrator
  openwork start --workspace /path/to/workspace --approval auto
  ```

## Quick Start
Download from [openworklabs.com/download](https://openworklabs.com/download) or latest [GitHub release](https://github.com/different-ai/openwork/releases).
- macOS and Linux downloads available directly
- Windows access currently through paid support plan
- Hosted OpenWork Cloud workers launched from web app after checkout

## Development

### Requirements
- Node.js + pnpm (repo uses `pnpm@10.27.0`)
- Bun 1.3.9+
- Rust toolchain (for Tauri)
- Tauri CLI: `cargo install tauri-cli`
- OpenCode CLI installed and available on PATH

```bash
git checkout dev
git pull --ff-only origin dev
pnpm install --frozen-lockfile
pnpm dev          # Desktop dev mode
pnpm dev:ui       # Web UI only
```

## OpenCode Plugins
Plugins are the native way to extend OpenCode. OpenWork manages them from the Skills tab by reading and writing `opencode.json`:
- **Project scope**: `<workspace>/opencode.json`
- **Global scope**: `~/.config/opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-wakatime"]
}
```

## Supported Languages
App available in: English, French, Spanish, Catalan, Brazilian Portuguese, Japanese, Simplified Chinese, Thai, Vietnamese, Russian.

## Security
- OpenWork hides model reasoning and sensitive tool metadata by default
- Host mode binds to `127.0.0.1` by default

## GitHub
- Owner: different-ai
- Stars: 15.3k | Forks: 1.5k
- License: MIT
- Primary Language: TypeScript 86.3%
- 1,243 releases

## Links
- [GitHub](https://github.com/different-ai/openwork)
- [Download](https://openworklabs.com/download)
- [Enterprise Plan](https://openworklabs.com/enterprise)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- [OpenChamber](openchamber.md)
- [OpenGUI](opengui.md)
