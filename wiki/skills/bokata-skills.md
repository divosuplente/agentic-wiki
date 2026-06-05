# Bokata Skills

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, orchestration
**Type:** reference
**Level:** intermediate

## Description
A public collection of Claude Code skills by Abraham Vallez covering engineering management, product development, and team practices. The skills use the [Vercel Skills CLI](https://github.com/vercel-labs/skills) and are compatible with Claude Code, Cursor, Copilot, Codex, and 40+ other AI agents.

## Installation
```bash
npx skills add abrahamvallez/skills
```

## Skills Included

### `1on1-coach`
**Category:** Management

Analyzes a 1on1 meeting transcript and produces three output documents:
- `outputs/shareable/{date}-{name}-summary.md` — neutral recap, key points, verbatim quotes, action items
- `outputs/coaching/{date}-{name}-analysis.md` — meeting effectiveness, Radical Candor quadrant, risks
- `outputs/coaching/{date}-{name}-coaching.md` — Socratic questions for the manager

**Meeting types:** `check-in` · `career` · `unblocking` · `feedback` · `conflict` · `onboarding` · `mixed`
Language auto-detected. Compatible with Fathom, Otter.ai, and plain text.

### `bokata-research`
**Category:** Product Dev / Bokata Framework

Runs three research phases to produce `feature-context.md` before mapping or slicing features:
1. **Feature Research** — domain vocabulary, actors, existing patterns
2. **Criteria Research** — business rules, permissions, state transitions
3. **Slicer Research** — tech stack, architecture constraints, available libraries

### `bokata-feature-mapper`
Maps a PRD or initiative description into a structured **Features Backbone** using User Story Mapping methodology. Features in `[Actor] [Verb] [Object]` format. Phase 0 discovery asks clarifying questions or documents assumptions.

### `bokata-ac-analyst`
Generates Gherkin acceptance criteria (Given/When/Then) for User Tasks using Rule-first approach. Covers happy path, error states, edge cases, and permission boundaries.

### `bokata-feature-slicer`
Decomposes a feature into a **Walking Skeleton** + **Increments Backlog** using Vertical Slicing (Hamburger Method). Uses 16+ breakdown strategies including Zero/One/Many, Dummy to Dynamic, SPIDR, and Workflow Simplification.

## Bokata Agents (Orchestration Wrappers)
- `bokata-mapper-specialist` — full features pipeline: scaffold folders, invoke research → mapper → analyst
- `bokata-slicer-specialist` — slices a single feature from `features.md`

## GitHub
- Owner: abrahamvallez
- Repo: skills
- Stars: 11 | Forks: 1
- License: MIT
- Primary Language: Shell (100%)

## Credits
Inspired by [eferro/skill-factory](https://github.com/eferro/skill-factory/tree/main).

## Links
- [Repository](https://github.com/abrahamvallez/bokata-skills)

## Related Pages
- [Anthropics Skill Creator](anthropics-skill-creator.md)
- [The Agent Skills Directory](agent-skills-directory.md)
- [Community Skills Repository](plainconcepts-skills.md)
