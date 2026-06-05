# Encoding Experience into AI Skills

**Category:** learning
**Type:** article
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** learning, skill
**Level:** advanced

## Summary
Eduardo Ferro's deep reflection on how senior engineers can distil domain expertise into reusable AI skills (prompt packages, context rules, and decision trees) so that junior developers and agents alike benefit from institutional knowledge. Built on top of Lada Kesseler's skill-factory, extended with 11 additional skills for complexity management and incremental delivery.

**Author:** Eduardo Ferro
**Date:** March 1, 2026

## The Problem with CLAUDE.md
If you use Claude Code, you already know about CLAUDE.md — a file where you put instructions the agent reads at the start of every conversation. It works, but it has a problem: **everything is always loaded**. Your TDD guidelines, Docker best practices, refactoring workflow — all competing for the agent's limited context window, whether relevant or not.

## What Skills Are (And Why They Matter)
Skills are packaged knowledge that **activates only when relevant**. You type `/mutation-testing` and the agent gains deep expertise about finding weak tests through mutation analysis. You type `/complexity-review` and it becomes a technical reviewer that challenges your proposals against 30 dimensions of complexity. The rest of the time, that knowledge stays out of the way.

Think of it as **progressive disclosure for AI context**. The agent gets what it needs, when it needs it.

## The Discovery: Lada Kesseler's Skill Factory
Lada Kesseler built [skill-factory](https://github.com/lexler/skill-factory) — 315 commits of carefully crafted skills covering serious engineering ground:
- TDD, Nullables (James Shore's pattern for testing without mocks)
- Approval tests (Java, Python, Node.js with scrubbers, reporters, inline patterns)
- Refactoring (Llewellyn Falco's approach)
- Hexagonal architecture, event modeling, collaborative design

Lada also co-created [augmented-coding-patterns](https://lexler.github.io/augmented-coding-patterns/) — a catalog of 43 patterns, 14 obstacles, and 9 anti-patterns for working effectively with AI coding tools.

## The Fork as Extension
Eduardo Ferro forked and extended Lada's work with 11 additional skills (27 total), covering the practices he kept explaining repeatedly:

### Testing Rigor
| Skill | Purpose |
|-------|---------|
| **test-desiderata** | Kent Beck's 12 properties that make tests valuable. Evaluates tests against each property and suggests concrete improvements. |
| **mutation-testing** | The question code coverage can't answer: "Would my tests catch this bug?" Coverage tells you what your tests execute; mutation testing tells you what they'd detect. |

### Delivering Incrementally and Managing Complexity
These five skills work as a **pipeline**:

| Skill | Role in Pipeline |
|-------|-----------------|
| **story-splitting** | Detects linguistic red flags ("and", "or", "manage", "handle", "including") and applies splitting heuristics. |
| **hamburger-method** | When a story doesn't have obvious split points, applies Gojko Adzic's Hamburger Method: slice into layers, generate 4-5 implementation options per layer, compose thinnest vertical slices. |
| **small-safe-steps** | The implementation planner. Breaks work into 1-3 hour increments. Core belief: **risk grows faster than the size of the change**. |
| **complexity-review** | Reviews technical proposals against 30 dimensions of complexity across 6 categories. Pushes for the simplest viable approach. |
| **code-simplifier** | Reduces complexity in existing code without changing behavior. The cleanup crew after a feature is done. |

**Pipeline:** `story-splitting` → `hamburger-method` → `small-safe-steps` for delivery planning, with `complexity-review` as a gate before implementation and `code-simplifier` as a sweep after.

### Practical Tools and Team Workflows
| Skill | Purpose |
|-------|---------|
| **thinkies** | Kent Beck's creative thinking habits. When stuck, applies patterns like "What would I do if I had infinite resources?", "What's the opposite of my current approach?" |
| **traductor-bilingue** | Technical translation between English and Spanish that keeps terms like "deploy", "pull request", "pipeline" in English. |
| **dockerfile-review** | Reviews Dockerfiles for build performance, image size, and security. |
| **modern-cli-design** | Principles for scalable CLIs: object-command architecture, LLM-optimized help text, JSON output, concurrency patterns. |

## A Skill in Action: Delivery Planning Pipeline
Story: *"As a user, I want to manage my notification preferences including email, SMS, and push notifications with scheduling and quiet hours."*

1. **Invoke `/story-splitting`** — flags "manage", "including", the conjunction "and". Suggests splitting into at least 4 stories: one per notification channel plus quiet hours.
2. **Invoke `/hamburger-method`** on "email notification preferences" — breaks into layers (UI, API, business logic, persistence), generates options per layer, composes thinnest slice: single toggle + API endpoint + database flag.
3. **Invoke `/small-safe-steps`** — produces 1-3 hour increments: add database column with migration, add API endpoint with tests, add UI toggle, wire together. Each deployable independently.

No single skill does everything. They **compose**. That's the point.

## How to Get Started
1. **Fork the repo**: [eferro/skill-factory](https://github.com/eferro/skill-factory) (27 skills) or [lexler/skill-factory](https://github.com/lexler/skill-factory) (16 original skills)
2. **Install skills**: Run `./skills toggle` to browse and select skills for Claude Code
3. **Use them**: Type `/skill-name` in Claude Code
4. **Make your own**: The repo includes documentation and tooling for creating new skills

## Key Takeaways
- Skills are the new documentation: executable, versioned, and tested.
- Progressive disclosure beats monolithic instruction files (CLAUDE.md vs. targeted skills).
- Skills compose into pipelines for complex workflows.
- Encoding heuristics reduces ramp-up time for new team members.
- Maintain a skill library alongside your codebase for consistent agent behaviour.
- **"What knowledge do you find yourself repeating to your AI agents? What practices would you encode as skills?"**

## Recommended Audience
Senior engineers, staff engineers, and team leads building internal agent toolchains. Anyone who finds themselves repeating the same advice to AI agents.

## Links
- [Read](https://www.eferro.net/2026/03/encoding-experience-into-ai-skills.html)
- [Eduardo Ferro's Skill Factory Fork](https://github.com/eferro/skill-factory) — 27 skills
- [Original Skill Factory by Lada Kesseler](https://github.com/lexler/skill-factory) — 16 foundational skills
- [Augmented Coding Patterns](https://lexler.github.io/augmented-coding-patterns/) — 43 patterns, 14 obstacles, 9 anti-patterns
- [Mutation Testing Blog Post](https://www.eferro.net/2025/11/mutation-testing-when-good-enough-tests.html)

## Related Pages
- [Building Senior Staff Engineer](building-senior-staff-engineer-claude.md)
- [Comprehension Debt](comprehension-debt.md)
- [Anthropics Skill Creator](../skills/anthropics-skill-creator.md)
- [Caveman](../skills/caveman.md)
- [OpenCode](../execution-surfaces/opencode.md)
