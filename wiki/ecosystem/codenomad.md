# CodeNomad

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** platform, agent
**Type:** reference
**Level:** intermediate

## Description
The AI Coding Cockpit for OpenCode. CodeNomad transforms OpenCode from a terminal tool into a **premium desktop workspace** built for developers who live inside AI coding sessions for hours and need control, speed, and clarity.

> "OpenCode gives you the engine. CodeNomad gives you the cockpit."

## Key Features
- **Multi-Instance Workspace** — manage multiple OpenCode sessions simultaneously
- **Remote Access** — access your workspace from anywhere
- **Session Management** — persistent sessions with rich state
- **Voice Input & Speech** — talk to your agents
- **Git Worktrees** — automated worktree management
- **Rich Message Experience** — beautiful UI for agent messages
- **SideCars** — open local web tools (VSCode, terminals) as tabs inside CodeNomad
- **Command Palette** — quick access to all features
- **File System Browser** — browse files without leaving the workspace
- **Theming** — customizable UI themes
- **Internationalization** — multi-language support

## SideCars
Open local web tools inside CodeNomad as tabs:
- **VSCode** (OpenVSCode Server) — full IDE inside a tab
- **Terminal** (ttyd) — terminal sessions inside a tab
- Any local HTTP/HTTPS service at `127.0.0.1:<port>`

## Desktop App
Available as both Electron and Tauri builds:
- macOS: DMG, ZIP (Universal: Intel + Apple Silicon)
- Windows: NSIS Installer, ZIP (x64, ARM64)
- Linux: AppImage, deb, tar.gz (x64, ARM64)

## Server Mode
Run as a local server and access via browser:
```bash
npx @neuralnomads/codenomad --launch
```

## Requirements
- OpenCode CLI — must be installed and in your PATH
- Node.js 18+ — for server mode or building from source

## Install
```bash
# Desktop app
curl -fsSL https://codenomad.dev/install.sh | sh

# Server mode
npx @neuralnomads/codenomad --launch

# Dev releases (bleeding edge)
npx @neuralnomads/codenomad-dev --launch
```

## Development
Monorepo packages:
- `packages/server` — Core logic & CLI: workspaces, OpenCode proxy, API, auth, speech
- `packages/ui` — SolidJS frontend: reactive, fast, beautiful
- `packages/electron-app` — Desktop shell: process management, IPC, native dialogs
- `packages/tauri-app` — Tauri desktop shell (experimental)

## GitHub
- Owner: NeuralNomadsAI
- Stars: 1.6k | Forks: 111
- License: MIT
- Primary Languages: TypeScript 88.5%, CSS 6.7%, Rust 2.7%

## Links
- [Repository](https://github.com/NeuralNomadsAI/CodeNomad)
- [Releases](https://github.com/shantur/CodeNomad/releases)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- [OpenChamber](openchamber.md)
- [OpenGUI](opengui.md)
