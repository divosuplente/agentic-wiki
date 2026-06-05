# mmadariaga/prompts (Shared-AI)

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, sdd
**Type:** reference
**Level:** intermediate

## Description
Software development oriented AI commands for a **cost-efficient, spec-first, structured workflow**: spec → plan → implement → review → audits → PR.

Each workflow step produces an artifact in `plans/{feature-name}/` that feeds into the next. Works great on **opencode** with a subscription + any frontier model. Also works on Claude Code and GitHub Copilot (experimental).

## Philosophy
- **You stay in control.** The AI is a peer, not a decision-maker.
- **Knowledge stays in the project.** Every phase produces a written artifact.
- **Spec first, always.** No code without a prior spec.
- **Cost-effective by design.** Each phase uses the cheapest model that can do the job.
- **Testing is not optional.** RED → GREEN for every testable step.

## Sequential Pipeline (Numbered Commands)
| Command | Input | Output |
|---------|-------|--------|
| `/ai-1-spec` | feature description | `plans/{f}/spec.md` |
| `/ai-2-plan` | `spec.md` | `plans/{f}/plan.md` |
| `/ai-3-implement` | `plan.md` | code |
| `/ai-4-review` | `spec.md` + diff | `plans/{f}/review.md` |
| `/ai-5-security` | `spec.md` + diff | `plans/{f}/security.md` |
| `/ai-6-performance` | `spec.md` + diff | `plans/{f}/performance.md` |
| `/ai-7-accessibility` | `spec.md` + diff | `plans/{f}/accessibility.md` |

## On-Demand Commands
- `/ai-commit` — Conventional Commits from `git diff --cached`
- `/ai-pr` — PR title + body from spec/plan/review/audits

## Key Principles
- **Isolation Mode** — every command starts with zero inherited context
- **Spec First** — spec drives the task and is kept as a living artifact
- **Single Responsibility** — each phase produces exactly one artifact
- **RED → GREEN** — failing test before minimal implementation
- **No Self-Review Bias** — review uses a different model than planning
- **Ubiquitous Language** — domain terms captured in `GLOSSARY.md`
- **Multi-Pass Review** — 9 distinct passes: Domain, Correctness, Security, Performance, Maintainability, Testing, Consistency, Language, Documentation

## Cost-Effective Strategies
- **Caveman Communication** — default lite mode; `--full-caveman` for aggressive abbreviation
- **Task-Matched Model Selection** — frontier for spec, mid-range for plan/review, fast for implement
- **Explore Sub-Agent** — research delegated to cheap models with output contracts

## Installation
### OpenCode (Global)
```bash
mkdir -p ~/.config/opencode/commands
cp opencode/commands/*.md ~/.config/opencode/commands/
mkdir -p ~/.config/opencode/instructions
cp instructions/*.md ~/.config/opencode/instructions/
```

### Claude Code
See [INSTALL.claude.md](https://github.com/mmadariaga/prompts/blob/main/INSTALL.claude.md)

## GitHub
- Owner: mmadariaga
- Stars: 3 | Forks: 0
- Forked from: grojeda/prompts

## Links
- [Repository](https://github.com/mmadariaga/prompts)

## Related Pages
- [Caveman](caveman.md)
- [Opencode Dynamic Context Pruning](opencode-dynamic-context-pruning.md)
- [OpenSpec](../specs/openspec.md)
- [OpenCode](../execution-surfaces/opencode.md)
