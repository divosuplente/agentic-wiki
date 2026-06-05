# Fallow GitHub Repository

**Category:** sources
**Type:** reference
**Level:** all
**Origin:** other-material
**Added:** 2026-06-04
**Raw:** `https://github.com/fallow-rs/fallow`

## Summary
Fallow (`fallow-rs/fallow`) is a deterministic codebase intelligence engine for TypeScript and JavaScript, written in Rust. It provides a free static-analysis layer (unused code, duplication, circular dependencies, complexity hotspots, architecture boundaries, dependency hygiene) and an optional paid runtime layer that merges production execution evidence (V8/Istanbul coverage) into health reports. Its "no AI inside the analyzer" stance produces stable, graph-based, machine-actionable findings that humans and AI agents can trust.

## Key Entities
- [Fallow](../protocols/fallow.md)
- [Deterministic Codebase Intelligence](../glossary.md)
- [Audit Verdict](../glossary.md)
- [Typed Output Contract](../glossary.md)
- [MCP Server](../glossary.md)

## Notable Links
- [Fallow GitHub Repository](https://github.com/fallow-rs/fallow) — source code, releases, README, framework plugins, and self-dogfooding pipeline
- [Fallow on npm](https://www.npmjs.com/package/fallow) — `fallow` package wrapping CLI, LSP, MCP server, and version-matched Agent Skill
- [Fallow on crates.io](https://crates.io/crates/fallow-cli) — `fallow-cli` Rust binary
- [Fallow GitHub Action](https://github.com/marketplace/actions/fallow-codebase-intelligence) — `fallow-rs/fallow@v2` for CI integration
- [Fallow Documentation](https://docs.fallow.tools) — official docs site covering MCP integration, runtime coverage, and static vs runtime intelligence