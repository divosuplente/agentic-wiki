# OpenGUI

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** platform, agent
**Type:** reference
**Level:** intermediate

## Description
Desktop + web command center for coding agents. Run OpenCode, Claude Code, Codex, and Pi across multiple projects with streaming chat, prompt queue, model switching, voice input, and MCP tools.

> "OpenGUI gives coding-agent users desktop and browser workflow for long sessions. Manage multiple projects visually, run different agent backends from one UI, watch responses stream live."

## Why OpenGUI
- **Run multiple agent backends in one app** instead of juggling separate tools
- **Manage multiple projects at once** with separate sessions per workspace
- **See streaming responses live** with token and context usage
- **Queue prompts while agent is busy** instead of waiting to type next step
- **Switch providers, models, agents, and variants** from UI
- **Configure MCP tools and skills** without leaving app
- **Use voice input** with Whisper-compatible transcription endpoint

## Highlights
- **Multi-agent workspace** for OpenCode, Claude Code, Codex, and Pi
- **Multi-project workspaces** for parallel coding sessions
- **Real-time streaming** over SSE with live usage tracking
- **Prompt queue** that auto-dispatches when assistant becomes idle
- **Model, backend, and agent selection** directly from chat workflow
- **Slash commands** from prompt box
- **Syntax highlighting** with Shiki
- **Dark/light theme** with system-aware toggle
- **Desktop, web, and Docker deployment options**
- **Cross-platform builds** for Linux, macOS, and Windows

## Supported Agent Backends
- **OpenCode**
- **Claude Code**
- **Codex**
- **Pi**

Use one backend or switch between them per workflow.

## Download
Prebuilt app from [latest release](https://github.com/akemmanuel/OpenGUI/releases/latest):
- **Linux:** `.deb`
- **macOS:** `.dmg`
- **Windows:** `.exe` installer (unsigned — SmartScreen will warn on first launch)

### Requirements
- OpenCode CLI installed and available in PATH (for OpenCode backend)
- Other backends: local CLI/auth/config for that backend

## Build from Source

### Prerequisites
- Bun v1.2+ runtime
- pnpm 10+ package manager
- Electron (installed through project dependencies)
- At least one supported backend configured locally

```bash
pnpm install
vp run dev          # Electron app with HMR
vp run dev:web     # Web app with local backend API
```

### Docker
Official image: `ghcr.io/akemmanuel/opengui:latest`
Supports contained mode and host-control mode (uses `nsenter` for host CLI access).

### Production
```bash
vp build            # Build frontend bundle
vp run dist:linux   # Build Linux .deb
vp run dist:mac     # Build macOS .dmg
vp run dist:win     # Build Windows .exe
```

## Architecture
```
main.ts              Electron main process
opencode-bridge.ts   IPC bridge to OpenCode SDK
claude-code-bridge.ts IPC bridge to Claude Code SDK
codex-bridge.ts      IPC bridge to Codex SDK
pi-bridge.ts         IPC bridge to Pi runtime
server/web-server.ts Bun runtime backend for browser mode
src/
  frontend.tsx       React entry point
  App.tsx            Main app layout
  hooks/             Central agent/workspace state
  components/        UI components
```

## Configuration
Connection and UI preferences via app settings interface.

**Voice input** requires a Whisper-compatible transcription server. Set endpoint in **Settings > General > Voice transcription endpoint**.

## GitHub
- Owner: akemmanuel
- Stars: 47 | Forks: 6
- License: MIT
- Primary Language: TypeScript 98.7%
- 39 releases

## Links
- [GitHub](https://github.com/akemmanuel/OpenGUI)
- [Releases](https://github.com/akemmanuel/OpenGUI/releases/latest)
- [opengui.io](https://opengui.io)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- [OpenChamber](openchamber.md)
- [Pi Coding Agent](../execution-surfaces/pi-coding-agent.md)
