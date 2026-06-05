# Claude Code

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-21
**Last verified:** 2026-05-21
**Tags:** agent, terminal
**Type:** reference
**Level:** beginner

## Description
Claude Code is Anthropic's official CLI-based AI coding agent. It runs directly in the terminal, integrates deeply with the filesystem and shell, and can read, write, and execute code across entire codebases. It uses Claude 3.5 Sonnet (or newer) under the hood and supports tool use including Bash, Read, Grep, Glob, and more.

## Setup
Installation via pip/uv or as a standalone binary. See official docs for latest instructions.

## Configuration
- PreToolUse hooks for CLI proxies (RTK, snip, tok, etc.)
- `.claude/` project directory for context files
- `CLAUDE.md` for project-specific instructions

## Key Features
- Terminal-native AI pair programmer
- Tool use: Bash, Read, Grep, Glob, LS, View, Edit
- PreToolUse hook system for command interception
- Supports Claude 3.5 Sonnet, Claude 3 Opus, and newer models
- Context window: 200K tokens

## Links
- [Official docs](https://docs.anthropic.com/en/docs/claude-code/overview)
- [GitHub](https://github.com/anthropics/claude-code) (if public)

## Prerequisites
- Basic terminal familiarity
- (optional) [What is an AI coding agent?](../learning/karpathy-vibe-coding-agentic.md)

## Next Steps
- [Install CLI proxies for token reduction](../skills/caveman.md)
- [Set up multi-agent workflows](../governance/claude-task-master.md)
- [Compare with other agents](opencode.md)

## Related Pages
- [RTK](../ecosystem/rtk.md)
- [snip](../ecosystem/snip.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Caveman](../skills/caveman.md)
- [ntk](../ecosystem/ntk.md)
