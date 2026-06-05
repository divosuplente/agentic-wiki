# snip

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-21
**Last verified:** 2026-05-21
**Tags:** token-optimizer, tool
**Type:** reference
**Level:** intermediate

## Description
`snip` is a Go-based CLI proxy that reduces LLM token consumption by **60–90%** on common development commands. Inspired by [RTK](rtk.md) (Rust Token Killer) and rebuilt in Go with a focus on extensibility, snip intercepts shell output from tools like `ls`, `cat`, `git status`, and test runners, then compresses and filters that output through declarative YAML rules before it reaches the AI agent's context window. It supports 13+ AI coding tools out of the box and ships with 126 built-in declarative YAML filters.

Like RTK, snip sits transparently between the AI agent and the shell:
```
Claude --git status--> shell --> git
   ^                  |            |
   |   ~2,000 tokens |            | filter
   +------------------+            +--- snip --> ~200 tokens
```

Where RTK is written in Rust and uses compiled filters, snip differentiates itself with a **declarative YAML filter engine** that makes it easy to add or customize compression rules without recompiling the binary.

## Key Features
- **60–90% token reduction** on common dev commands (`ls`, `cat`, `git status`, `npm test`, etc.)
- **Declarative YAML filters** — 126 built-in rules, easy to extend without recompiling
- **13+ supported AI agents** — Claude Code, Cursor, GitHub Copilot, Gemini CLI, Codex, Windsurf, Cline, Kilo Code, Antigravity, Aider, and OpenCode
- **Pure Go implementation** — static binary output, fast goroutine-based filtering, pure Go SQLite driver
- **Transparent proxy** — hooks intercept commands automatically after `snip init`
- **Cross-platform** — single static binary deployment

## Installation
```bash
# Install via go install
go install github.com/edouard-claude/snip@latest

# Or download a prebuilt static binary from GitHub Releases
# https://github.com/edouard-claude/snip/releases

# Initialize for your AI tool
snip init                    # Claude Code / Copilot (default)
snip init --opencode         # OpenCode
snip init --codex            # Codex
snip init --cursor           # Cursor
snip init --gemini           # Gemini CLI
```

Restart your AI tool after initialization. Once hooked, commands such as `git status` are automatically rewritten through `snip` before entering the agent context.

## Links
- [GitHub](https://github.com/edouard-claude/snip)
- [pkg.go.dev](https://pkg.go.dev/github.com/edouard-claude/snip)
- [Source Summary](../sources/snip-repo.md)

## Related Pages
- [RTK](rtk.md)
- [CodeGraph](../protocols/codegraph.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [OpenCode Platform](../execution-surfaces/opencode-platform.md)
- [Caveman](../skills/caveman.md)
