# Activity Log

**Type:** meta
**Level:** all
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-06-05

## 2026-06-05

- **Company-agnostic strip pass: removed all "Plain Concepts" mentions from wiki prose, in preparation for publishing the wiki to a public repository under `divosuplente/agentic-wiki`.**
  - Rewrote 4 dedicated pages to be company-agnostic: `wiki/skills/plainconcepts-skills.md`, `wiki/skills/francho-copilot.md`, `wiki/ecosystem/one-to-all-plain-agents-jam.md`, `wiki/governance/spike-openspec-flow.md`.
  - Updated 17 in-place files (README, indexes, landing pages, learning path, tasks, sources) to drop "Plain Concepts" framing in descriptions, summaries, and back-links.
  - Per user direction, kept factual references to the real GitHub org `PlainConcepts` inside `wiki/skills/plainconcepts-skills.md` (page title, clone URL, GitHub section) — these are not brand mentions but the actual repo path being documented.
  - Verified: zero "Plain Concepts" (with space) references remain in `wiki/`. Five `PlainConcepts` references remain, all of them either the actual GitHub path in `wiki/skills/plainconcepts-skills.md` or a single back-link in `wiki/skills/agent-skills-directory.md`.

- **Ingested 3 GitHub repositories into the wiki.**
  - **Freestyle** (`freestyle-voice/freestyle`) — Free, open-source, local-first voice-to-text dictation app. Hold-to-record hotkey pastes cleaned text at the cursor; multi-provider STT (OpenAI, Groq, Anthropic, Google, Deepgram, ElevenLabs, BYO key); post-processing for grammar/punctuation, custom phrase dictionaries, and contextual correction (auto-formatting by target app). Cross-platform (macOS, Windows, Linux), MIT licensed.
    - Source summary: `wiki/sources/freestyle-repo.md`
    - Entity page: `wiki/ecosystem/freestyle.md`
  - **Knowhere** (`Ontos-AI/knowhere`) — Open-source document memory layer for AI agents and RAG. Ingests PDFs, Office files, images, tables, Markdown, and text into structured chunks with hierarchy reconstruction (tree-like algorithm preserves full document structure, prevents semantic fragmentation) and a cross-document memory graph. Agentic retrieval combines keyword/path/content/semantic signals (RRF) with autonomous navigation through section trees; every result returns traceable evidence (source, section, chunk, linked assets). Model-agnostic (default DeepSeek + Qwen-VL). Apache 2.0; open-sourced May 7, 2026. Internal benchmarks: +36% first-try accuracy, +11% recall vs raw docs and parser output.
    - Source summary: `wiki/sources/knowhere-repo.md`
    - Entity page: `wiki/ecosystem/knowhere.md`
  - **specification.website** (`jdevalk/specification.website`) — Platform-agnostic website specification by Joost de Valk (Yoast) collecting the layer cake of web standards (WHATWG HTML, WCAG 2.2, IETF, MDN, W3C, schema.org, llmstxt.org) into one sourced reference. 10 categories: Foundations, SEO, Accessibility, Security, Well-Known URIs, Agent Readiness, Performance, Privacy, Resilience, Internationalisation. Status levels: Required / Recommended / Optional / Avoid. Built with Astro + TypeScript on Cloudflare Pages; ships a bundled MCP server. Content CC BY 4.0, code MIT.
    - Source summary: `wiki/sources/specification-website-repo.md`
    - Entity page: `wiki/specs/specification-website.md`
  - **Updated indexes:** `wiki/ecosystem/index.md`, `wiki/specs/index.md`, `wiki/sources/index.md`
  - **Updated master index:** `wiki/index.md` (Last updated: 2026-06-05)
  - **Categorization rationale:** Freestyle and Knowhere placed in `ecosystem` (developer tools that augment workflows); specification.website placed in `specs` (it is literally a specification document with status levels matching the specs category format).

## 2026-06-04

- **Ingested Fallow repository into the wiki.**
  - **Fallow** (`fallow-rs/fallow`) — Deterministic Rust-native codebase intelligence engine for TypeScript and JavaScript. Free static layer (unused code, duplication, circular deps, complexity hotspots, architecture boundaries, dependency hygiene; 108 framework plugins; zero config) plus optional paid runtime layer (V8/Istanbul coverage → hot-path/cold-path evidence). Bundled MCP server, LSP server, and version-matched Agent Skill. "No AI inside the analyzer" — produces stable, machine-actionable JSON (typed `CheckOutput` contract, `actions` array per issue with `auto_fixable` flag). Distributions: npm (`fallow`), crates.io (`fallow-cli`), GitHub Action (`fallow-rs/fallow@v2`), VS Code extension. Key commands: `fallow audit` (PR risk gate with pass/warn/fail verdict), `fallow health --score`, `fallow dead-code`, `fallow dupes` (4 modes), `fallow fix --dry-run`, `fallow impact`. CI integration: GitHub Action, GitLab CI template (typed `review-gitlab` envelope v2), generic CLI flags for any CI.
    - Source summary: `wiki/sources/fallow-repo.md`
    - Entity page: `wiki/protocols/fallow.md`
  - **Updated indexes:** `wiki/protocols/index.md`, `wiki/sources/index.md`
  - **Updated master index:** `wiki/index.md` (Last updated: 2026-06-04)
  - **Added glossary terms:** Agent Skill (Fallow), Audit Verdict, Deterministic Codebase Intelligence, Typed Output Contract

## 2026-05-28

- **Major wiki reorganization: learning paths, role entry points, task-based guide, and frontmatter enrichment.**
  - Created `wiki/learning/paths/` with four learning paths and a skill-tree diagram.
    - [First-Time Agent User](learning/paths/first-time-agent-user.md) — 8-module beginner path.
    - [Agent Customizer](learning/paths/agent-customizer.md) — 10-module intermediate path.
    - [Multi-Agent Orchestrator](learning/paths/multi-agent-orchestrator.md) — 12-module advanced path.
    - [Spec-Driven Developer](learning/paths/spec-driven-developer.md) — 8-module intermediate–advanced path.
    - [Skill Tree](learning/paths/skill-tree.md) — Mermaid diagram linking all paths.
  - Rewrote `wiki/README.md` as a role-based entry point (USE / CUSTOMIZE / ORCHESTRATE / SET standards).
  - Created `wiki/tasks.md` for task-based navigation ("I want to ___" format).
  - Added `**Type:**` and `**Level:**` frontmatter fields to all 8 category indices and 4 root pages.
  - Updated `wiki/learning/index.md` with learning paths section.

## 2026-05-22

- **Ingested Chrome Modern Web Guidance into the wiki.**
  - **Modern Web Guidance** — Google Chrome's evergreen, expert-vetted skill package that guides AI coding agents across common web-development use cases (accessibility, performance, security, PWAs, web components, Baseline conformance).
    - Source summary: `wiki/sources/modern-web-guidance.md`
    - Entity page: `wiki/skills/modern-web-guidance.md`
  - **Updated indexes:** `wiki/skills/index.md`, `wiki/sources/index.md`
  - **Updated master index:** `wiki/index.md` (Last updated: 2026-05-22)
  - **Updated overview:** Added mention of Modern Web Guidance as an industry-vetted skill package bridging browser vendor expertise and AI-assisted development
  - **Next steps:** Run `lint-wiki.md` audit to check cross-references and link health.
