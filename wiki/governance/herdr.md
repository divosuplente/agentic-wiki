# Herdr

**Category:** governance
**Status:** active
**Added:** 2026-05-20
**Last verified:** 2026-05-20
**Tags:** terminal, orchestration, harness
**Type:** reference
**Level:** intermediate

## Description
Herdr is an agent runtime that runs inside your terminal, providing tmux-style persistence with agent-aware features: mouse-native panes, semantic agent state tracking (blocked/working/done/idle), and a runtime API that agents use to orchestrate their workspace.

## Key Features
- Runs real terminal processes in PTYs with layout, click targets, state, persistence, automation
- Survives disconnects via background session server
- Works locally, over SSH, or as thin client to remote hosts
- Mouse-native TUI with clickable panes, tabs, workspaces, menus
- Semantic agent state tracking visible in sidebar: blocked, working, done, idle, unknown
- Direct agent attach capability and orchestration through CLI and socket API
- Workspace rollups showing most urgent agent state for scanning
- Integrations: Claude Code, Codex, OpenCode, and other agents
- Responsive TUI works over SSH from mobile devices
- CLI commands: `herdr workspace create`, `herdr tab create`, `herdr pane split`, `herdr pane run`, `herdr wait agent-status`

## Links
- [Official Site](https://herdr.dev/)
- [Source Summary](../sources/herdr-website.md)

## Related Pages
- [claude-task-master](claude-task-master.md) — harness for orchestrating Claude Code sub-agents
- [opencode-ensemble](opencode-ensemble.md) — multi-agent team harness for OpenCode
- [Oh My OpenAgent](oh-my-openagent.md) — agent harness with discipline agents
- [Glossary](../glossary.md)
