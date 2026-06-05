# Lint Skill

**Category:** skills
**Status:** active
**Added:** 2026-05-19
**Last verified:** 2026-05-19
**Tags:** skill, tool
**Type:** reference
**Level:** all

## Description

Cross-agent skill for running a health-check audit over a Karpathy-pattern LLM wiki. Works with any AI assistant (OpenCode, Claude Code, GitHub Copilot, Cursor, Pi, etc.) that can read markdown files, resolve relative links, and compare page content.

The skill checks for contradictions, orphan pages, stale claims, missing cross-references, dead links, format compliance violations, and accidental self-ingestion artifacts. It produces a severity-ranked report and appends a summary to the wiki log.

## Installation

1. Copy the skill directory into your agent's skills folder:

```bash
cp -r chapter-devex/.agents/skills/lint ~/.agents/skills/lint
# or for OpenCode specifically:
cp -r chapter-devex/.agents/skills/lint ~/.config/opencode/skill/lint
```

2. Ensure the skill is discoverable by your agent's configuration (e.g., `AGENTS.md`, `CLAUDE.md`, or `.cursor/skills/` depending on the agent).

3. Invoke the skill with a trigger phrase when you want to audit wiki integrity.

## Usage

Trigger phrases:
- "lint the wiki"
- "audit the wiki"
- "run wiki health check"
- "check wiki integrity"
- "wiki quality check"

## Links

- [Lint Skill Source](../../.agents/skills/lint/SKILL.md)
- [Ingest Skill](ingest.md) — companion skill for ingesting sources
- [Query Skill](query.md) — companion skill for querying the wiki
- [AGENTS.md](../../AGENTS.md) — wiki schema and conventions

## Related Pages

- [Ingest](ingest.md)
- [Query](query.md)
- [Lint Wiki Skill Reference](../execution-surfaces/lint-wiki.md)
- [Wiki README](../README.md)
