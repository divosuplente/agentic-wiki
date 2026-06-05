# Fallow

**Category:** protocols
**Status:** active
**Added:** 2026-06-04
**Last verified:** 2026-06-04
**Tags:** codebase-intelligence, mcp, lsp, typescript, javascript, rust
**Type:** reference
**Level:** intermediate

## Description
Fallow is a deterministic codebase intelligence engine for TypeScript and JavaScript, written in Rust and shipped as `fallow` (npm), `fallow-cli` (crates.io), and a GitHub Action (`fallow-rs/fallow@v2`). It analyzes a repository as a system — not just a list of files — and connects static structure, dependency relationships, duplication, complexity, architecture boundaries, package hygiene, and (optionally) runtime evidence into one quality report. Its explicit "no AI inside the analyzer" stance means findings are stable, graph-based, and reproducible, which makes the output trustworthy for downstream tools and agents that need evidence instead of guesses.

Fallow has two layers. The **free static layer** (open source) ships 108 framework plugins and runs zero-config out of the box: it detects unused code (files, exports, dependencies, types, enum/class members), code duplication in four modes (strict, mild, weak, semantic), circular dependencies and boundary violations, complexity hotspots, and dependency hygiene. The **optional paid runtime layer** (Fallow Runtime) uses V8 or Istanbul coverage to merge production execution evidence into health reports — exposing hot paths, cold code, runtime-weighted health, and stale feature-flag branches.

Fallow is built for agents as a first-class consumer. A single `npm install --save-dev fallow` ships the CLI, an MCP server, an LSP server, and a version-matched Agent Skill. The MCP server answers questions like "who imports this symbol?", "why is this export used/unused?", "what changed in this PR?", and "what action is safest?". Every JSON issue carries a machine-actionable `actions` array with an `auto_fixable` flag, and the typed output contract `import type { CheckOutput } from "fallow/types"` pins the schema to the installed CLI version. Output formats include `json`, `sarif`, `codeclimate`, `markdown`, `compact`, `badge`, `pr-comment-github`, `pr-comment-gitlab`, `review-github`, `review-gitlab`, and `annotations`. A `fallow audit` PR gate returns a verdict of `pass` / `warn` / `fail` with attribution between PR-introduced and pre-existing findings.

## Key Features
- **108 framework plugins** with zero-config first run; no Node.js runtime required for static analysis
- **Static layer (free, MIT):** unused code, duplication (4 modes), circular dependencies, boundary violations, complexity hotspots, dependency hygiene, architecture presets (bulletproof, layered, hexagonal, feature-sliced)
- **Runtime layer (optional, paid):** V8/Istanbul coverage → hot paths, cold code, runtime-weighted health, stale feature flags, coverage_intelligence verdict block
- **Agent integration:** bundled MCP server, LSP server, and version-matched Agent Skill — `npm install` ships them all
- **Typed output contract:** `import type { CheckOutput } from "fallow/types"` pins the JSON schema to the installed CLI version
- **Machine-actionable findings:** every JSON issue has an `actions` array with `auto_fixable` flag, enabling agents to self-correct
- **Audit verdict:** `pass` / `warn` / `fail` with gate-aware attribution between PR-introduced and pre-existing findings
- **CI-ready:** GitHub Action, GitLab CI template (typed `review-gitlab` envelope v2), generic CLI flags for any CI
- **Per-analysis production mode:** CLI flags > env vars > config; CLI only enables, env/config can also disable (clean CI templates)
- **Adopt incrementally:** `{ "rules": { "unused-files": "error", "unused-exports": "warn", "circular-dependencies": "off" } }`
- **Deterministic:** no LLM inside the analyzer — stable, reproducible findings
- **Self-dogfooding:** Fallow analyzes its own shipped JS/TS surfaces (VS Code extension, npm wrapper) in CI on every change

## Installation

```bash
# npm (wraps CLI, LSP, MCP server, and version-matched Agent Skill)
npm install --save-dev fallow
# or: pnpm add -D fallow
# or: yarn add -D fallow
# or: bun add -d fallow

# one-off CLI use
npx fallow audit

# Rust
cargo install fallow-cli

# Programmatic Node API
npm install @fallow-cli/fallow-node
```

## MCP Configuration

Add Fallow's bundled MCP server to your agent's config:

```json
{
  "mcpServers": {
    "fallow": {
      "type": "stdio",
      "command": "npx",
      "args": ["fallow", "mcp"]
    }
  }
}
```

## Common Commands

```bash
fallow                       # Full codebase analysis: cleanup + duplication + health
fallow audit                 # PR risk gate (verdict: pass/warn/fail)
fallow health --score        # 0-100 health score with letter grade
fallow health --hotspots     # Riskiest files (churn × complexity)
fallow health --targets      # Ranked refactoring recommendations
fallow dead-code             # Unused files, exports, dependencies, types
fallow dupes --mode semantic # Duplication with renamed-variable detection
fallow fix --dry-run         # Preview automatic cleanup
fallow impact                # Local trend tracking (opt-in, gitignored)
fallow watch                 # Re-analyze on file change
fallow explain unused-export # Explain a rule without analyzing
fallow telemetry inspect     # Inspect telemetry payload (off by default)
```

## Links
- [GitHub](https://github.com/fallow-rs/fallow)
- [npm](https://www.npmjs.com/package/fallow)
- [crates.io](https://crates.io/crates/fallow-cli)
- [GitHub Action](https://github.com/marketplace/actions/fallow-codebase-intelligence)
- [Documentation](https://docs.fallow.tools)
- [Source Summary](../sources/fallow-repo.md)

## Related Pages
- [CodeGraph](codegraph.md)
- [Graphify](graphify.md)
- [Context7](context7.md)
- [Draw.io MCP](drawio-mcp.md)
- [MCP Server](../glossary.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Claude Code](../execution-surfaces/claude-code.md)
- [Knowledge Graph](../glossary.md)