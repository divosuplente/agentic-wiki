# Vibe Kanban

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** orchestration, harness
**Type:** reference
**Level:** intermediate

## Description
Vibe Kanban is a product-management tool built for teams that ship with coding agents. It turns the new bottleneck — **human planning and review** — into a Kanban-style workflow that runs parallel coding agents in the background.

> "Vibe kanban is the biggest increase I've had in productivity since cursor." — Luke Harries, Growth Lead at ElevenLabs

## Workflow: Plan → Prompt → Review
1. **Plan** — break down work into issues and sub-issues on the Kanban board
2. **Prompt** — prompt a coding agent (Claude, ChatGPT, OpenCode, Cursor, etc.) to solve any issue in the background
3. **Review** — review AI-generated code, QA changes, iterate with agents

## Key Features
- **Parallel Agents**: Run multiple Claude Code, Codex, OpenCode, Cursor, Gemini CLI, Amp, Aider, Windsurf agents simultaneously
- **Git Worktrees**: Automates creating git worktrees and running setup scripts for each agent
- **Code Review**: Comment on AI-generated code, see diffs with syntax highlighting
- **QA Changes**: Start dev servers and click to edit components; built-in browser for testing
- **Collaborative Issue Tracking**: Share issue status with your team; statuses update automatically when agents start working or PRs are created/merged
- **PR Review Worktrees**: Launch a dedicated worktree from any PR and iterate with coding agents

## Works With
Claude, ChatGPT, Gemini, OpenCode, Cursor, Amp, Aider, Copilot, Windsurf

## Install
```bash
npx vibe-kanban
```

## Users
30,000+ active users. 100,000+ PRs created.

## GitHub
- Owner: BloopAI
- Stars: 26.3k
- [Repository](https://github.com/BloopAI/vibe-kanban)

## Links
- [Official site](https://www.vibekanban.com/)
- [Docs](https://www.vibekanban.com/docs/getting-started)
- [Blog](https://www.vibekanban.com/blog)

## Related Pages
- [Paseo](../governance/paseo.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
