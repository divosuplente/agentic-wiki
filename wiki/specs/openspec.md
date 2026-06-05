# OpenSpec

**Category:** specs
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** sdd, standard
**Type:** reference
**Level:** intermediate

## Description
OpenSpec is a lightweight, spec-driven framework for coding agents and CLIs — **universal, open source, no API keys, no MCP required**.

Unlike a chat prompt, an OpenSpec is a document that agents read and write. When an agent needs context about how a feature should work, it reads the spec. When a new developer joins, they can browse the library to understand the system. Context doesn't disappear when a chat session ends or someone leaves the team.

## Philosophy
- **Review intent, not just code.** Each OpenSpec change produces a spec delta showing how requirements change — reviewers understand the change without digging through code.
- **Context that persists.** Specs live in your repository alongside your code, organized by capability.
- **Something to review in seconds.** Describe a change, OpenSpec generates: a proposal document, broken-down implementation tasks, technical design decisions, and spec deltas.

## Install
```bash
npm install -g @fission-ai/openspec@latest
```

## How It Works
1. Describe a change: `/openspec:proposal Add remember me checkbox with 30-day sessions`
2. OpenSpec reads existing specs, searches codebase, creates plan
3. Review `openspec/changes/{id}/`:
   - `proposal.md` — describe the change
   - `design.md` — technical decisions
   - `tasks.md` — implementation tasks
   - `specs/` — spec deltas

## Supported Agents
Claude Code, Cursor, Codex, GitHub Copilot, OpenCode, Windsurf, Gemini CLI, Antigravity, Cline, RooCode, Amazon Q, Qwen Code, and 16+ more.

## Key Differentiators
1. **Lightweight.** Minimal steps, minimal process.
2. **Brownfield-first.** Designed for mature codebases, not greenfield.
3. **Specs live in your code.** Other tools throw away requirements after planning; OpenSpec preserves them as living documentation.

## FAQ Highlights
- **"Is this just waterfall?"** No — waterfall fails because of rigid plans and months of upfront planning. OpenSpec wants you to get to a good enough plan and start coding.
- **"Where do specs live?"** In your codebase, checked in, providing visibility into how the system works and the intent it was built with.
- **"What if I switch agents?"** OpenSpec is designed as a universal planning layer you can bring with you anywhere.

## Coming Soon
- **Workspaces** — team planning for large codebases, multi-repo systems, microservices

## Links
- [Official site](https://openspec.dev/)
- [GitHub](https://github.com/Fission-AI/OpenSpec/)
- [Discord](https://discord.gg/YctCnvvshC)

## Prerequisites
- Familiarity with spec-driven development concepts
- (optional) [Agentic SDLC Handbook](../learning/agentic-sdlc-handbook.md)

## Next Steps
- [Spec Kit](spec-kit.md)
- [BMAD-METHOD](bmad-method.md)
- [GSD framework](get-shit-done.md)

## Related Pages
- [Spec Kit](spec-kit.md)
- [BMAD-METHOD](bmad-method.md)
- [GSD vs Spec Kit](../learning/agentic-coding-sdd-comparison.md)
- [OpenCode](../execution-surfaces/opencode.md)
