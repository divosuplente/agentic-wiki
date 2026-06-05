# Query Skill

**Category:** skills
**Status:** active
**Added:** 2026-05-19
**Last verified:** 2026-05-19
**Tags:** skill, tool
**Type:** reference
**Level:** intermediate

## Description

Cross-agent skill for querying a Karpathy-pattern LLM wiki. Works with any AI assistant (OpenCode, Claude Code, GitHub Copilot, Cursor, Pi, etc.) that can read markdown files and synthesize answers with citations.

The skill reads the wiki index first, locates relevant pages, synthesizes a grounded answer with inline citations, and optionally files the answer as a new analysis page.

## Installation

1. Copy the skill directory into your agent's skills folder:

```bash
cp -r chapter-devex/.agents/skills/query ~/.agents/skills/query
# or for OpenCode specifically:
cp -r chapter-devex/.agents/skills/query ~/.config/opencode/skill/query
```

2. Ensure the skill is discoverable by your agent's configuration (e.g., `AGENTS.md`, `CLAUDE.md`, or `.cursor/skills/` depending on the agent).

3. When you want an answer grounded in the wiki, invoke the skill with your question.

## Links

- [Query Skill Source](../../.agents/skills/query/SKILL.md)
- [Ingest Skill](ingest.md) — companion skill for ingesting sources
- [AGENTS.md](../../AGENTS.md) — wiki schema and conventions

## Related Pages

- [Ingest](ingest.md)
- [Karpathy: From Vibe Coding to Agentic Engineering](../learning/karpathy-vibe-coding-agentic.md)
- [Community Skills Repository](plainconcepts-skills.md)
