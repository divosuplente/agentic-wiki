# Gastown

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** orchestration, harness, agent
**Type:** explanation
**Level:** advanced

## Description
Gas Town is a multi-agent orchestration system for Claude Code, GitHub Copilot, Codex, and other AI agents — with persistent work tracking. Created by Steve Yegge (ex-Google, ex-Amazon), it solves the fundamental problem of agents losing context on restart by persisting work state in git-backed hooks.

> Scale comfortably to 20-30 agents instead of losing control at 4-10.

## Core Concepts

| Concept | Role |
|---------|------|
| **Mayor 🎩** | Primary AI coordinator (Claude Code instance with full workspace context). Start here. |
| **Town 🏘️** | Workspace directory (e.g., `~/gt/`) containing all projects, agents, and config |
| **Rig 🏗️** | Project container wrapping a git repository and its associated agents |
| **Crew Member 👤** | Your personal workspace within a rig — where you do hands-on work |
| **Polecat 🦨** | Worker agent with persistent identity but ephemeral sessions. Spawned for tasks; session ends on completion; identity and work history persist |
| **Hook 🪝** | Git worktree-based persistent storage for agent work. Survives crashes and restarts |
| **Convoy 🚚** | Work tracking unit bundling multiple beads. `mountain`-labeled convoys get autonomous stall detection and smart skip logic |
| **Beads 📿** | Git-backed issue tracking system. Bead IDs use prefix + 5-char alphanumeric (`gt-abc12`) |
| **Refinery 🏭** | Per-rig merge queue processor. Bors-style bisecting queue — polecats never push directly to main |

## Three-Tier Watchdog Chain
```
Daemon (Go process) ← heartbeat every 3 min
    └── Boot (AI agent) ← intelligent triage
        └── Deacon (AI agent) ← continuous patrol
            └── Witnesses & Refineries ← per-rig agents
```

## Install
```bash
brew install gastown              # Homebrew (recommended)
npm install -g @gastown/gt        # npm
go install github.com/steveyegge/gastown/cmd/gt@latest  # From source

gt install ~/gt --git
cd ~/gt
gt rig add myproject https://github.com/you/repo.git
gt crew add yourname --rig myproject
gt mayor attach
```

## Prerequisites
- Go 1.25+, Git 2.25+, Dolt 1.82.4+, beads 0.55.4+
- tmux 3.0+ (recommended)
- Claude Code CLI (default) / Codex CLI / GitHub Copilot CLI (optional)

## Key Commands

### Agent Operations
- `gt agents` — list active agents
- `gt sling <bead-id> <rig>` — assign work to agent
- `gt mayor attach` — start Mayor session
- `gt feed` — real-time activity feed TUI dashboard
- `gt feed --problems` — stuck agent detection view

### Convoy (Work Tracking)
- `gt convoy create <name> [issues...]` — create convoy
- `gt convoy list` — list all convoys
- `gt convoy show [id]` — show convoy details

### Monitoring & Health
- `gt escalate -s HIGH "description"` — escalate a blocker
- `gt seance` — discover and query previous agent sessions
- `gt scheduler status` — show scheduler state

## Activity Feed
`gt feed` launches an interactive terminal dashboard:
- **Agent Tree** — hierarchical view grouped by rig and role
- **Convoy Panel** — in-progress and recently-landed convoys
- **Event Stream** — chronological feed of creates, completions, slings, nudges

Navigation: `j`/`k` scroll, `Tab` switch panels, `?` help, `q` quit. Press `p` for problems view.

## Dashboard
Web dashboard at port 8080 (configurable):
```bash
gt dashboard --port 3000 --open
```
Single-page overview: agents, convoys, hooks, queues, issues, escalations. Auto-refreshes via htmx. Command palette for running `gt` commands from browser.

## Supported Runtimes
Claude Code, Codex, Cursor, Gemini, Auggie, Amp, OpenCode, Copilot, Pi, Omp — plus custom presets via `gt config agent set`.

## Wasteland Federation
Federated work coordination network linking Gas Towns through DoltHub:
- `gt wl join <remote>` — join a wasteland
- `gt wl browse` — view wanted board
- `gt wl claim <id>` — claim work from another town
- Portable reputation via multi-dimensional stamps (quality, speed, complexity)

## Telemetry (OpenTelemetry)
Emits all agent operations as structured logs/metrics to any OTLP-compatible backend:
- Events: session lifecycle, agent state changes, mail operations, sling/nudge/done workflows
- Metrics: `gastown.session.starts.total`, `gastown.polecat.spawns.total`, `gastown.done.total`

## GitHub
- Owner: gastownhall
- Stars: 15.4k | Forks: 1.4k
- License: MIT
- Primary Language: Go 95.0%

## Links
- [GitHub](https://github.com/gastownhall/gastown)
- [Docs: Architecture](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md)
- [Docs: Glossary](https://github.com/gastownhall/gastown/blob/main/docs/glossary.md)

## Related Pages
- [OpenCode Ensemble](opencode-ensemble.md)
- [Claude Task Master](claude-task-master.md)
- [AgentCraft](../governance/agentcraft-platform.md)
