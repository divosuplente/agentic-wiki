# Anthropics Skill Creator

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, framework
**Type:** reference
**Level:** all

## Description
Skill definition file for Anthropics' skill-creator in the `anthropics/skills` repository. Provides a complete framework and guidelines for creating, testing, and iterating on new skills for Claude Code, ensuring consistency and best practices across the skill ecosystem.

The skill-creator defines the full lifecycle: capture intent → draft SKILL.md → run test cases → evaluate qualitatively and quantitatively → iterate based on feedback → package and present.

## Core Loop
1. **Capture Intent** — understand what the skill should do, when it should trigger, and expected output format
2. **Interview and Research** — ask about edge cases, formats, success criteria, dependencies
3. **Write SKILL.md** — fill in name, description (the primary triggering mechanism), compatibility, and instructions
4. **Run Test Cases** — spawn parallel runs (with-skill vs baseline) via subagents
5. **Evaluate** — qualitative review via eval viewer + quantitative benchmark assertions
6. **Iterate** — improve based on feedback, rerun, repeat until satisfied
7. **Package** — generate `.skill` file for distribution

## Skill Anatomy
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    — Executable code for deterministic/repetitive tasks
    ├── references/ — Docs loaded into context as needed
    └── assets/     — Files used in output (templates, icons, fonts)
```

## Progressive Disclosure
Three-level loading system:
1. **Metadata** (name + description) — Always in context (~100 words)
2. **SKILL.md body** — In context whenever skill triggers (<500 lines ideal)
3. **Bundled resources** — As needed (unlimited, scripts execute without loading)

## Key Guidelines
- **Description is the trigger** — include both what the skill does AND specific contexts for when to use it. Make it "pushy" to combat Claude's tendency to undertrigger.
- **Progressive disclosure** — keep SKILL.md under 500 lines; use reference files for large docs
- **Explain the why** — use theory of mind; avoid heavy-handed MUSTs and ALL-CAPS rules
- **Test with baselines** — always compare with-skill vs without-skill runs
- **Bundle repeated work** — if test runs reinvent similar helper scripts, bundle them in `scripts/`
- **Description optimization** — after creating a skill, generate 20 trigger eval queries and run an optimization loop to improve triggering accuracy

## Quantitative Evals
Save test cases to `evals/evals.json`. For each test case, capture:
- **Timing data** (`total_tokens`, `duration_ms`) from task notifications
- **Grading** via assertions in `grading.json` (fields: `text`, `passed`, `evidence`)
- **Benchmark aggregation** with `pass_rate`, time, and tokens per configuration
- **Analyst pass** — surface non-discriminating assertions, high-variance evals, time/token tradeoffs

## Environment-Specific Notes
- **Claude Code**: full workflow with subagents, browser reviewer, and `claude -p` for description optimization
- **Claude.ai**: no subagents — run test cases inline, skip baselines, present results directly in conversation
- **Cowork**: has subagents but no browser — use `--static <output_path>` for the eval viewer

## GitHub
- Owner: anthropics
- Stars: 137k | Forks: 16.2k
- [Repository](https://github.com/anthropics/skills)

## Links
- [Skill Definition](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [Anthropics Skills Repo](https://github.com/anthropics/skills)

## Related Pages
- [Caveman](caveman.md)
- [The Agent Skills Directory](agent-skills-directory.md)
- [OpenCode](../execution-surfaces/opencode.md)
