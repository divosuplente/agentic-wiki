# Update Index Agent Prompt

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-18
**Tags:** skill, tool
**Type:** reference
**Level:** all

## Description
Reusable prompt template for updating the master catalog (`wiki/index.md`) after adding or editing pages anywhere in the wiki. Ensures the index stays complete, categorized, and accurately described.

## Usage

After adding new wiki pages, run this prompt against your agent to refresh the index in one pass.

## Prompt Template

```
Update `wiki/index.md` to reflect all current pages in the wiki.

1. List every page under its correct category:
   - Execution Surfaces
   - Governance
   - Protocols
   - Ecosystem
   - Specs
   - Skills
   - Learning
   - Source Summaries

2. For each page, include a one-line description extracted from its own content (prefer the first sentence of the `## Description` section).

3. Ensure all relative markdown links are correct and point to existing files.

4. Preserve any existing heading structure and alphabetical ordering within categories.
```

## Category Mapping

| Folder | Index Heading |
|---|---|
| `wiki/execution-surfaces/` | Execution Surfaces |
| `wiki/governance/` | Governance |
| `wiki/protocols/` | Protocols |
| `wiki/ecosystem/` | Ecosystem |
| `wiki/specs/` | Specs |
| `wiki/skills/` | Skills |
| `wiki/learning/` | Learning |
| `wiki/sources/` | Source Summaries |

## Description Extraction Rule

Pull the first sentence of the `## Description` section from each target page. If no Description section exists, fall back to the first sentence under the page title (`# <Title>`). Keep the summary to a single line (≤ 120 characters).

## Related Pages
- [Ingest Source](ingest-source.md)
- [Lint Wiki](lint-wiki.md)
- [Wiki README](../README.md)
- [OpenCode](opencode.md)
