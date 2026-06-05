# Lint Wiki Skill Reference

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, tool
**Type:** reference
**Level:** all

## Description
Documents the reusable `lint` cross-agent skill located at `.agents/skills/lint/SKILL.md`. This skill audits the entire wiki for contradictions, dead links, stale claims, orphan pages, format violations, and self-ingestion artifacts. Designed to be executed periodically or before major releases to maintain structural integrity and consistency.

> **Note:** This skill is now available as a proper `.agents/skills/` skill file in addition to this prompt template. Agents that support skill directories should load `.agents/skills/lint/SKILL.md` rather than copying the prompt below verbatim.

## Usage

Run periodically or before major releases to catch drift, dead links, and schema violations. Copy the prompt below into any agent that supports prompt-based execution, or invoke the `lint` skill directly if your agent supports skill directories.

## Prompt Template

```
Lint the wiki according to the Lint Workflow in AGENTS.md:

1. Check for contradictions between pages.
2. Check for orphan pages with no incoming links.
3. Check for stale claims ("Last verified" dates older than 90 days).
4. Check for missing cross-references.
5. Check relative markdown links for dead links.
6. Check format compliance (frontmatter on every page).
7. Check for accidental self-ingestion:
   - Are there any source summary pages in `wiki/sources/` that reference `wiki/` as their `**Raw**` file or `**Origin**`?
   - Are there any `## Key Entities` links that point back to `wiki/` itself (e.g., `../../wiki/index.md`)?
   - Flag and remove any infinite-loop artifacts.

Report findings and propose fixes. Log any TODOs in `wiki/log.md`.
```

## Check Details

| # | Check | What to look for | Severity |
|---|---|---|---|
| 1 | **Contradictions** | Two or more pages making conflicting claims about the same tool, standard, or agent | High |
| 2 | **Orphan pages** | Pages in `wiki/` with zero incoming links from `index.md`, `overview.md`, or any other wiki page | Medium |
| 3 | **Stale claims** | `Last verified:` dates older than 90 days with no explanatory note | Low |
| 4 | **Missing cross-references** | Entity pages lacking a `Related Pages` section with at least one link | Medium |
| 5 | **Dead links** | Relative markdown links that do not resolve to an existing file | High |
| 6 | **Format compliance** | Pages missing the standard frontmatter (`Category`, `Status`, `Added`, `Last verified`) | High |

## Reporting Format

Structure your findings as:

```
## Lint Report — YYYY-MM-DD

### High
- `path/to/page.md`: <issue description>

### Medium
- `path/to/page.md`: <issue description>

### Low
- `path/to/page.md`: <issue description>

### Proposed Fixes
1. <actionable fix>
2. <actionable fix>
```

Then append a summary line to `wiki/log.md`:

```
YYYY-MM-DD — Lint pass: X issues found (H/M/L). TODOs logged.
```

## Related Pages
- [Ingest Source](ingest-source.md)
- [Update Index](update-index.md)
- [Lint Skill](../skills/lint.md)
- [Wiki README](../README.md)
- [OpenCode](opencode.md)
