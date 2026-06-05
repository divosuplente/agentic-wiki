# First-Time Agent User

**Category:** learning
**Status:** active
**Added:** 2026-05-28
**Last verified:** 2026-05-28
**Tags:** beginner, path, opencode, claude-code

## Description
A beginner-friendly learning path that takes you from zero AI-coding experience to running your first agent and understanding how it works. Approximately 8 modules, 95 minutes total (excluding final project).

---

## Step 1: What is an AI coding agent?
**Type:** Explanation | **Estimated time:** 5 min | **Prerequisite:** None

- Read [Karpathy: From Vibe Coding to Agentic Engineering](../karpathy-vibe-coding-agentic.md) — Karpathy explains the evolution from vibe coding to agentic engineering.
- Browse [Awesome Copilot](../../skills/awesome-copilot.md) for context on what agents can do today.

---

## Step 2: Install and run your first agent — OpenCode
**Type:** Tutorial | **Estimated time:** 15 min | **Prerequisite:** Step 1

- Follow the install instructions in [OpenCode](../../execution-surfaces/opencode.md):
  ```bash
  curl -fsSL https://opencode.ai/install | bash
  ```
- Also try Claude Code, Warp, or Pi as alternatives once OpenCode is running.

---

## Step 3: Write your first effective prompt
**Type:** Tutorial | **Estimated time:** 10 min | **Prerequisite:** Step 2

> 📖 Follow [Prompting 101: Write Your First Effective Prompt](../prompting-101.md) — a 10-minute tutorial covering the four-part framework, before/after examples, and a quick checklist.

---

## Step 4: Install a skill and see it work
**Type:** Tutorial | **Estimated time:** 10 min | **Prerequisite:** Step 2

- Use the [Agent Skills Directory](../../skills/agent-skills-directory.md) to find a skill:
  ```bash
  npx skills add owner/repo
  ```
- Or explore [Vercel Skills](../../skills/vercel-skills.md) — Vercel Skills CLI.
- Copilot users should check [Awesome Copilot](../../skills/awesome-copilot.md) for Copilot-specific skills.

---

## Step 5: Understand what the agent actually did
**Type:** Explanation | **Estimated time:** 10 min | **Prerequisite:** Step 3, Step 4

- Read [Karpathy: From Vibe Coding to Agentic Engineering](../karpathy-vibe-coding-agentic.md) again, focusing on the agentic engineering section.
- Study [The Agentic SDLC Handbook](../agentic-sdlc-handbook.md) for the PROSE framework and how agents build software.

---

## Step 6: Avoid comprehension debt
**Type:** Explanation | **Estimated time:** 10 min | **Prerequisite:** Step 5

- Read [Comprehension Debt](../comprehension-debt.md) — Addy Osmani's article on the hidden costs of AI-generated code.
- Read [Mo Bitar: No Skill in AI Coding](../mo-bitar-no-skill-ai-coding.md) — deskilling risks and how to prevent them.

---

## Step 7: Explore alternatives
**Type:** Reference | **Estimated time:** 5 min | **Prerequisite:** Step 2

- [Claude Code](../../execution-surfaces/claude-code.md)
- [Warp](../../execution-surfaces/warp.md)
- [Pi](../../execution-surfaces/pi-coding-agent.md)
- [GitHub Copilot](../../execution-surfaces/github-copilot.md)
- [Codex CLI](../../execution-surfaces/codex-cli.md)

---

## Step 8: Build a tiny project end-to-end
**Type:** Tutorial | **Estimated time:** 30 min | **Prerequisite:** Steps 3–7

> 📖 Follow [Build a Tiny Project: URL Title Extractor CLI](../first-project-tutorial.md) — a 30-45 minute hands-on project that teaches prompt refinement, iterative development, and debugging with an agent.

---

## Progress Checklist
- [ ] Step 1: What is an AI coding agent?
- [ ] Step 2: Install and run OpenCode
- [ ] Step 3: Write your first effective prompt
- [ ] Step 4: Install a skill and see it work
- [ ] Step 5: Understand what the agent actually did
- [ ] Step 6: Avoid comprehension debt
- [ ] Step 7: Explore alternatives
- [ ] Step 8: Build a tiny project end-to-end

## Related Pages
- [Prompting 101](../prompting-101.md)
- [Build a Tiny Project: URL Title Extractor CLI](../first-project-tutorial.md)
- [Learning Paths](README.md)
- [Skill Tree](skill-tree.md)
- [Master Index](../../index.md)
