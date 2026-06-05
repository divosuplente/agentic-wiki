# Graphify

**Category:** protocols
**Status:** active
**Added:** 2026-05-20
**Last verified:** 2026-05-20
**Tags:** context, mcp, tool
**Type:** reference
**Level:** intermediate

## Description
Graphify is an open-source platform that helps AI coding assistants understand multi-modal codebases by building a queryable knowledge graph from code, docs, papers, and diagrams. By combining Tree-sitter static analysis with LLM-driven semantic extraction, it turns an entire repository into an interactive graph explaining both what code does and why it was designed that way.

## Key Features
- **Multi-modal extraction**: parses code (`.py`, `.js`, `.go`, `.java`, etc.), Markdown, PDFs, and images using Tree-sitter for ASTs and LLMs for semantic concepts
- **Knowledge graph building**: merges extracted nodes/edges into a NetworkX graph and applies the Leiden algorithm for community detection
- **God node detection**: identifies [god nodes](../glossary.md) (high-degree nodes) and unexpected cross-file/domain connections
- **Interactive outputs**: `graph.html`, `graph.json`, `GRAPH_REPORT.md` with EXTRACTED/INFERRED/AMBIGUOUS audit trail
- **Assistant integration**: `/graphify`, `/graphify query`, `/graphify path`, `/graphify explain` commands for Claude Code, Codex, and OpenCode
- **Token efficiency**: up to 71.5x token reduction vs. naive approaches (reported on ~92k-word corpus: ~1.7k avg query vs. ~123k naive)
- **Security**: input validation against SSRF, injection, and XSS; only semantic descriptions (never raw source) sent to the LLM
- **MCP server**: built-in MCP-protocol server (`serve.py`) for agent tool integration
- **Python 3.10+**; install via PyPI: `pip install graphifyy`; CLI: `graphify`
- MIT License, maintained by Safi Shamsi

## Installation
```bash
pip install graphifyy
```

## Links
- [Official Website](https://graphify.net/)
- [GitHub](https://github.com/safishamsi/graphify)
- [Source Summary](../sources/graphify-website.md)
- [Glossary: God Nodes](../glossary.md)
- [Glossary: Semantic Extraction](../glossary.md)

## Related Pages
- [CodeGraph](codegraph.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Context7](context7.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
