# Glossary

**Type:** reference
**Level:** all
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-06-04


- **Agent** — An AI coding agent that interprets natural-language instructions, plans multi-step edits, and executes them across a codebase. Examples include [OpenCode](./execution-surfaces/opencode.md), [Claude Code](./execution-surfaces/claude-code.md), [Pi](./execution-surfaces/pi-coding-agent.md), and [Warp](./execution-surfaces/warp.md).
- **Agent Harness** — A tool or framework that orchestrates and manages AI coding agents, often enabling multi-agent workflows or simplifying agent CLI usage. Examples include [AgentCraft](./governance/agentcraft.md) and [opencode-ensemble](./governance/opencode-ensemble.md).
- **Agent Skill (Fallow)** — A version-matched instruction package bundled with the `fallow` npm install, teaching agents how to consume Fallow's structured JSON, MCP tools, and audit verdicts. A core component of [Fallow](./protocols/fallow.md).
- **Audit Verdict** — A pass/warn/fail signal emitted by `fallow audit` for changed-code PR gates, with exit code 0 for pass/warn and 1 for fail, plus gate-aware attribution between PR-introduced and pre-existing findings. Implemented by [Fallow](./protocols/fallow.md).
- **Skill** — A reusable set of instructions, prompts, or capabilities that extend an AI agent's behavior, packaged for easy installation and sharing.
- **MCP Server** — A Model Context Protocol server that allows external tools and services to expose capabilities to AI agents programmatically, such as [Context7](./protocols/context7.md) or [Draw.io MCP](./protocols/drawio-mcp.md).
- **SDD (Spec-Driven Development)** — A development methodology where specifications drive agent behavior and code generation, using lightweight spec frameworks like [OpenSpec](./specs/openspec.md) or [Spec Kit](./specs/spec-kit.md).
- **Vibe Coding** — A playful, prompt-driven approach to coding where developers describe what they want in natural language rather than typing code manually. See [Karpathy on Vibe Coding](learning/karpathy-vibe-coding-agentic.md).
- **Spec-Kit** — A specification kit developed by GitHub for defining agent-driven development workflows and standards.
- **OpenSpec** — A lightweight, spec-driven framework for coding agents and CLIs — universal, open source, and requiring no API keys or MCP servers.
- **Context Pruning** — The practice of intelligently removing irrelevant context from an agent's context window to optimize token usage and reduce API costs.
- **Dynamic Context** — Context that changes during an agent session based on relevance, often managed through pruning or retrieval mechanisms.
- **Orchestration** — The coordination and management of multiple AI agents to collaborate on complex software engineering tasks.
- **Ensemble** — A multi-agent team configuration where agents run in parallel with messaging between them, such as [opencode-ensemble](./governance/opencode-ensemble.md).
- **Token Optimization** — Strategies and techniques to reduce the number of tokens consumed by AI agents during conversations, such as the [Caveman skill](skills/caveman.md) or [dynamic context pruning](skills/opencode-dynamic-context-pruning.md).
- **Declarative Filter DSL** — A domain-specific language expressed in declarative configuration (e.g., YAML) that defines rules for filtering, transforming, or compressing data. Used by tools like [snip](./ecosystem/snip.md) to extend command output filtering without recompilation.
- **Deterministic Codebase Intelligence** — Repository analysis that produces stable, reproducible findings from graph-based static evidence without invoking LLMs inside the analyzer, so agents can trust the output. The core principle of [Fallow](./protocols/fallow.md).
- **Token Reduction Proxy** — A CLI intermediary that intercepts shell command output and compresses or filters it before it reaches an AI agent's context window, reducing LLM token consumption by 60–90%. Examples include [RTK](./ecosystem/rtk.md) and [snip](./ecosystem/snip.md).
- **Typed Output Contract** — A versioned TypeScript type (e.g., `CheckOutput`) shipped with a tool that pins the exact JSON schema, enabling agents to import and consume outputs without runtime parsing. A core principle of [Fallow](./protocols/fallow.md).
- **YAML Filter Engine** — A filtering system that applies declarative YAML-defined rules to process and compress data, enabling extensible token reduction without code changes. A core component of [snip](./ecosystem/snip.md).
- **Semantic Compression** — AI-driven compression of command output that understands meaning before reducing tokens. A core capability of [NTK](./ecosystem/ntk.md).
- **BPE Path Shortening** — Tokenizer-aware compression that shortens file paths based on Byte Pair Encoding token counts.
- **Hook-Based Auto-Rewrite** — Agent integration pattern where shell commands are transparently rewritten (e.g., `git status` → `rtk git status`) before execution.
- **Copilot Instructions** — Reusable prompt templates and instruction files for enhancing GitHub Copilot's behavior across different development scenarios.
- **DESIGN.md** — A design-system document that AI agents consume to generate consistent UI across a project, codifying tokens, components, and layout rules.
- **Knowledge Graph** — A structured representation of information and relationships, often used by agents to navigate and reason about complex domains.
- **Prompt Engineering** — The practice of crafting and structuring prompts to guide Large Language Models in generating more reliable and consistent code.
- **Sub-agent** — A specialized agent instance delegated to handle a specific task or role within a larger multi-agent team, such as in [claude-task-master](./governance/claude-task-master.md).
- **Plan Validation** — The process of reviewing agent plans before execution, such as with [Plannotator](./governance/plannotator.md), to ensure correctness and alignment with user intent.
- **Ingest** — A cross-agent skill that reads raw source files and produces structured, interlinked wiki pages while preventing self-ingestion loops. See [Ingest Skill](skills/ingest.md).
- **Query** — A cross-agent skill that answers questions by reading the wiki index and relevant pages, synthesizing cited answers grounded in ingested knowledge. See [Query Skill](skills/query.md).
- **Code Knowledge Graph** — A pre-indexed structured representation of code entities and relationships that enhances AI coding agents with semantic code intelligence locally, such as [CodeGraph](./protocols/codegraph.md).
- **PROSE Framework** — Five architectural constraints for reliable, verifiable, and maintainable AI agent output, introduced in [The Agentic SDLC Handbook](learning/agentic-sdlc-handbook.md).
- **God Nodes** — High-degree nodes in a knowledge graph representing central components of a system. Identified by tools such as [Graphify](./protocols/graphify.md) to reveal architectural hubs and unexpected cross-domain connections.
- **Hash-Anchored Edits** — Content-hash-based line identification that prevents stale-line modification errors (e.g., `LINE#ID`). Used by harnesses such as [Oh My OpenAgent](./governance/oh-my-openagent.md) to validate every edit and eliminate misaligned patches.
- **Discipline Agents** — Specialized agent roles (orchestrator, deep worker, strategic planner) operating in a coordinated harness. Examples include Sisyphus, Hephaestus, and Prometheus in [Oh My OpenAgent](./governance/oh-my-openagent.md).
- **Semantic Extraction** — LLM-driven extraction of meaning and concepts from documents and code, transforming raw source material into structured, queryable knowledge graphs. A core capability of [Graphify](./protocols/graphify.md).
- **Factory Architecture** — The orchestration pillar of ASDLC's agent-driven development model, coordinating agent workflows as part of the Three Pillars framework.
- **Agent Development Environment (ADE)** — An integrated terminal-editor-terminal workspace built for AI coding agents, not human-first IDEs.
- **Notification Ring** — Visual UI indicator in a terminal that alerts when an AI agent requires human attention.
- **PTY (Pseudo-Terminal)** — A virtual terminal interface used by tools like Herdr and Terax to run real shell processes with programmatic control.
- **Agent State Tracking** — Semantic monitoring of agent progress (e.g., blocked, working, done, idle) as implemented by Herdr.

