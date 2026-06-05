# OpenCode

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** agent, terminal
**Type:** reference
**Level:** beginner

## Description
OpenCode is an open-source coding agent designed to run in any terminal. It interprets natural-language instructions, plans multi-step edits, and executes them across your codebase. Common use cases include rapid prototyping, refactoring large files, and acting as a harness for custom skills.

## Facts
- **160K+ GitHub Stars**
- **900+ Contributors**
- **7.5M+ Monthly Developers**
- **13,000+ Commits**
- Privacy-first: does not store any code or context data

## Setup
1. Install the CLI:
   ```bash
   curl -fsSL https://opencode.ai/install | bash
   # or npx opencode / npm install -g opencode
   ```
2. Authenticate with your LLM provider (OpenAI, Anthropic, GitHub Copilot, etc.)
3. Run `opencode` in any repository to start an interactive session.

## Configuration
- `opencode.json` / `opencode.jsonc` — project-level config for models, agents, and MCP servers
- `~/.config/opencode/` — global user settings and skill directories
- Environment variables: `OPENCODE_PROVIDER`, `OPENCODE_MODEL`, `OPENCODE_API_KEY`

## Key Features
- **LSP Enabled**: Automatically loads the right LSPs for the LLM
- **Multi-session**: Start multiple agents in parallel on the same project
- **Any Model**: 75+ LLM providers through Models.dev, including local models
- **Any Editor**: Terminal interface, desktop app, and IDE extension
- **Share Links**: Share a link to any session for reference or to debug

## Extensions
The OpenCode ecosystem includes plugins for:
- **Quota management** — [Opencode Quota](../skills/opencode-quota.md)
- **Dynamic context pruning** — [Opencode Dynamic Context Pruning](../skills/opencode-dynamic-context-pruning.md)
- **Harnesses** — [Oh My OpenAgent](../governance/oh-my-openagent.md), [Paseo](../governance/paseo.md)

## Links
- [Official docs](https://opencode.ai/docs)
- [GitHub](https://github.com/anomalyco/opencode)
- [Configuration reference](https://opencode.ai/docs/configuration)
- [Changelog](https://opencode.ai/changelog)
- [Discord](https://opencode.ai/discord)

## Prerequisites
- Basic terminal familiarity
- (optional) Read [What is an AI coding agent?](../learning/karpathy-vibe-coding-agentic.md)

## Next Steps
- [Install your first skill](../skills/agent-skills-directory.md)
- [Optimize token usage with Caveman](../skills/caveman.md)
- [Explore alternatives: Claude Code](claude-code.md) or [Warp](warp.md)

## Related Pages
- [Pi Coding Agent](pi-coding-agent.md)
- [Warp](warp.md)
- [OpenCode (Platform)](../execution-surfaces/opencode-platform.md)
- [OpenCode Course](../learning/midudev-opencode-course.md)
- [GSD vs Spec Kit](../learning/agentic-coding-sdd-comparison.md)
- [Opencode Quota](../skills/opencode-quota.md)
- [Opencode Dynamic Context Pruning](../skills/opencode-dynamic-context-pruning.md)
