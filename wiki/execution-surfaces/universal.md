# Universal Agent Patterns

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-18
**Tags:** agent, standard
**Type:** reference
**Level:** all

## Description

Universal Agent Patterns are the practices, conventions, and schema designs that make AI-assisted development workflows portable across different coding agents such as OpenCode, Claude Code, GitHub Copilot, Cursor, and others. The core idea is that a team’s accumulated expertise—prompts, skills, harnesses, and context—should not be locked into a single vendor’s ecosystem. By standardizing on plain Markdown, relative links, and a shared directory structure, any team can ensure that any agent can consume and contribute to the same knowledge graph. This reduces context-rebuilding cost when switching tools, enables parallel adoption of multiple agents, and future-proofs the investment in agent infrastructure. The Universal Agent concept is the philosophical backbone of the `AGENTS.md` schema: one file that any AI assistant reads first, regardless of its brand.

## Key Principles

1. **Agent-agnostic markdown instructions** — Every page is plain Markdown with YAML-style frontmatter. There is no vendor-specific DSL, no proprietary JSON schema, and no executable code hidden in the instructions. This is why `AGENTS.md` exists: it is the single source of truth that any LLM can parse.

2. **Portable skill definitions** — Skills are self-contained Markdown files with a `TRIGGER` section, not IDE extensions or Python packages. They live in `wiki/skills/` and can be read by any agent that can read files.

3. **Shared context and harness patterns** — Context (domain knowledge, standards, templates) and harnesses (orchestration recipes) are stored as flat Markdown files in `wiki/`. Any agent can load them via simple file reads, no API integration required.

4. **Avoiding vendor lock-in in workflow design** — Workflows are expressed as step-by-step Markdown instructions, not as GitHub Actions, VS Code tasks, or Cursor rules. This keeps the workflow logic in the repository and under version control, decoupled from any single tool’s execution engine.

## Setup

How to apply universal patterns in practice:

- **Write prompts in plain English with clear structure** — Use section headers, numbered lists, and imperative voice. Avoid jargon or tool-specific shortcuts that another agent might not understand.
- **Store shared context in flat markdown files** — Keep domain knowledge in `wiki/`, `docs/`, or `CONTEXT.md`. Flat files are the lowest-common-denominator storage that every agent can read.
- **Use relative links for cross-references** — Link to other wiki pages with `label(path.md)` so that links remain valid regardless of which agent is browsing the file tree.
- **Follow the Karpathy pattern** — Maintain a pipeline of `raw sources → human schema → AI-maintained wiki`. Raw links go in `docs/`, `poc/`, `benchmark/`, `workshop/`, or `other-material/`, the schema is `AGENTS.md`, and the AI-maintained synthesis lives in `wiki/`.

## Configuration

- **`AGENTS.md`** — The single schema that every agent reads on entry. It defines directory layout, page types, and workflow rules.
- **`wiki/`** — The shared knowledge graph. All pages are Markdown, all cross-references are relative, and the directory structure mirrors the mental model of the domain.
- **`other-material/`** — The immutable raw input boundary. Drop new links, notes, or screenshots here; do not edit them after ingestion. They serve as the ground truth for wiki updates.

## Links

- [Official docs — none, this is an internal standard](../../AGENTS.md)
- [AGENTS.md schema](../../AGENTS.md)
- [OpenCode](opencode.md)
- [GitHub Copilot](github-copilot.md)

## Related Pages

- [OpenCode](opencode.md)
- [Pi Coding Agent](pi-coding-agent.md)
- [Warp](warp.md)
- [GitHub Copilot](github-copilot.md)
- [BMAD Method](../specs/bmad-method.md)
- [Spec-Kit](../specs/spec-kit.md)
- [Agent Skills Directory](../skills/agent-skills-directory.md)
