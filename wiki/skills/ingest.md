# Ingest Skill

**Category:** skills
**Status:** active
**Added:** 2026-05-19
**Last verified:** 2026-05-19
**Tags:** skill, tool
**Type:** reference
**Level:** intermediate

## Description

Cross-agent skill for ingesting raw source material into a Karpathy-pattern LLM wiki. Works with any AI assistant (OpenCode, Claude Code, GitHub Copilot, Cursor, Pi, etc.) that can read markdown files and write to the filesystem.

The skill enforces source path validation, prevents infinite self-ingestion loops, generates source summaries, creates entity pages, and keeps the wiki index, overview, glossary, and log synchronized.

## Installation

1. Copy the skill directory into your agent's skills folder:

```bash
cp -r chapter-devex/.agents/skills/ingest ~/.agents/skills/ingest
# or for OpenCode specifically:
cp -r chapter-devex/.agents/skills/ingest ~/.config/opencode/skill/ingest
```

2. Ensure the skill is discoverable by your agent's configuration (e.g., `AGENTS.md`, `CLAUDE.md`, or `.cursor/skills/` depending on the agent).

3. When a new raw source appears in `docs/`, `poc/`, `benchmark/`, `workshop/`, or `other-material/`, invoke the skill with the source path.

## Links

- [Ingest Skill Source](../../.agents/skills/ingest/SKILL.md)
- [Query Skill](query.md) — companion skill for querying the wiki
- [AGENTS.md](../../AGENTS.md) — wiki schema and conventions

## Related Pages

- [Query](query.md)
- [Karpathy: From Vibe Coding to Agentic Engineering](../learning/karpathy-vibe-coding-agentic.md)
- [Community Skills Repository](plainconcepts-skills.md)
