# Ingest Source Agent Prompt

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-18
**Tags:** skill, tool
**Type:** reference
**Level:** all

## Description
Reusable prompt template for ingesting a new source file from any raw source folder (`docs/`, `poc/`, `benchmark/`, `workshop/`, or `other-material/`) into the wiki. Any AI agent (OpenCode, Claude Code, Copilot, Cursor, etc.) can be handed this prompt verbatim to perform a full ingest cycle.

## Usage

Drop a file into `docs/`, `poc/`, `benchmark/`, `workshop/`, or `other-material/` and run this prompt, substituting both `<folder>` and `<filename>`.

## Prompt Template

```
Ingest the new source `<folder>/<filename>` into the wiki.
Follow the Ingest Workflow defined in AGENTS.md:
1. Read the raw source from `<folder>/<filename>`.
2. Create/update a source summary in `wiki/sources/<folder>-<filename>.md`.
3. For each distinct platform, skill, harness, standard, learning resource, or agent mentioned, create or update the relevant page in `wiki/<category>/`.
4. Update `wiki/index.md`.
5. Update `wiki/overview.md` if the big picture changed.
6. Update `wiki/glossary.md` with new terms.
7. Log activity in `wiki/log.md`.
8. IMPORTANT: Ensure you NEVER ingest files from `wiki/`, `.git/`, `node_modules/`, or other generated/output directories. Only ingest from `docs/`, `poc/`, `benchmark/`, `workshop/`, or `other-material/`.
```

## Source Folders

| Folder | Typical Content |
|---|---|
| `docs/` | Design documents, architecture decisions, meeting notes |
| `poc/` | Proof-of-concept code, experiments, prototypes |
| `benchmark/` | Benchmark results, performance tests, comparisons |
| `workshop/` | Workshop materials, notes, outcomes |
| `other-material/` | Curated links, articles, references |

## Template Variables

| Variable | Description | Example |
|---|---|---|
| `<folder>` | Source folder the file was placed in | `docs` |
| `<filename>` | Name of the file placed in the source folder | `architecture-decisions.md` |

## Deduplication Rules

- If a page already exists for a given tool, skill, or concept, **merge and update** it instead of creating a duplicate.
- Preserve existing `Added:` dates; only update `Last verified:` to today.
- When merging, append new links or features that do not already exist.
- Re-use existing page titles unless the source explicitly introduces a new canonical name.

## Infinite Loop Prevention
- The `wiki/` folder is the AI-maintained output layer. It must NEVER be ingested as raw material.
- The ingest prompt should explicitly abort if the source path starts with `wiki/`.
- When generating source summary filenames in `wiki/sources/`, do not create paths that reference `wiki/` itself (e.g., do not create `wiki/sources/wiki-index-md.md`).

## Validation Checklist

Before considering the ingest complete, ensure every newly created or updated page has:

- [ ] **Frontmatter** — `Category`, `Status`, `Added`, `Last verified` (per AGENTS.md standard)
- [ ] **Related Pages** — at least one relative markdown link to another wiki page
- [ ] **Links** — at least one external or internal resource link
- [ ] **Cross-references** — all relative markdown links resolve to existing files
- [ ] **Log entry** — a line appended to `wiki/log.md` noting what was changed

## Related Pages
- [Update Index](update-index.md)
- [Lint Wiki](lint-wiki.md)
- [Wiki README](../README.md)
- [OpenCode](opencode.md)
