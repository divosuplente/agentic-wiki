# Plannotator

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** tool, agent
**Type:** reference
**Level:** intermediate

## Description
Plan and code review for your AI coding agents. Annotate agent plans before they run. Review agent-written code with a full diff viewer. Share with your team. Your feedback goes straight back to the agent.

Runs locally | natively integrates with agents | free & open source

## Install
```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```
One command. Hooks into your agent automatically. Zero learning curve.

## Supported Agents
Claude Code, Codex, Copilot, Gemini, OpenCode, Pi, VS Code

## Plan Review
Annotate the plan before it executes:
- Select text, mark for deletion, add a comment, or write a replacement
- Inline comments on any section
- Mark deletions to remove scope
- Version history tracks every revision (plan diffs)
- Diff view shows what changed between iterations
- Annotations export as structured feedback that the agent understands

## Code Review
Review the diff before you commit:
- Run `/plannotator-review` for a PR-style diff viewer
- Side-by-side or unified diff view
- File tree navigation
- Line-level annotations with code suggestions
- Stage or unstage files before committing

## How It Works
1. **Use your agent normally** — work with your coding agent as you do today. When it proposes a plan, Plannotator intercepts the approval step automatically.
2. **Review on a real surface** — instead of squinting at terminal text, get a proper review workspace. Annotate inline, mark what needs to change, then approve or deny with structured feedback.
3. **Feedback flows back** — your annotations are sent directly to the agent as structured feedback. No copy-pasting, no retyping. The agent revises based on exactly what you said.

## Commands
- **Plan review** — automatic: hooks into your agent's plan step
- `/plannotator-annotate <file|dir|url>` — annotate any markdown, spec/plan, folder, or URL and send feedback
- `/plannotator-last` — annotate the agent's last message
- `/plannotator-review <null|pr-url>` — code review for local changes or GitHub and GitLab PRs

## Features
- **Runs locally** — plans never leave your machine
- **Encrypted sharing** — share plans via URL; data lives in the link itself
- **Version history** — every plan revision saved, with diffs between versions
- **Draft auto-save** — annotations survive server crashes and restarts

## Integrations
- **VS Code** — open plans in editor tabs, diff view, editor annotations
- **Obsidian** — auto-save plans to vault with frontmatter and tags
- **Bear** — save plans with nested tags and project metadata
- **GitHub PRs** — review pull requests by URL with full diff annotations
- Integrations for Claude Code, OpenCode, Pi, Codex, and VS Code

## License
Dual-licensed under MIT or Apache 2.0, at your option.

## GitHub
- Owner: backnotprop
- Stars: (see GitHub badge)
- [Repository](https://github.com/backnotprop/plannotator)

## Links
- [Official site](https://plannotator.ai/)
- [Docs](https://plannotator.ai/docs/getting-started/installation/)
- [GitHub](https://github.com/backnotprop/plannotator)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- [Vibe Kanban](vibe-kanban.md)
- [OpenSpec](../specs/openspec.md)
