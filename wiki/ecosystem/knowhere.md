# Knowhere

**Category:** ecosystem
**Status:** active
**Added:** 2026-06-05
**Last verified:** 2026-06-05
**Tags:** rag, document-ingestion, ai-agents, open-source
**Type:** tool
**Level:** intermediate

## Description
Knowhere is the memory layer between complex, dirty documents and AI agents. It ingests unstructured documents and produces persistent, navigable memory: parsing, hierarchy extraction, multi-modal structuring, and graph construction in a single pipeline. Designed for agentic RAG, vector-based RAG, or any LLM workflow that needs traceable, well-contextualized evidence from messy source material.

## Key Features
- **Multi-modal parsing** — high-fidelity extraction from PDF, Office (docx/pptx/xlsx/csv), images (jpg/png), Markdown, text, and JSON
- **Tree-like hierarchy reconstruction** — proprietary algorithm preserves full document structure instead of flattening to a chunk sequence, preventing semantic fragmentation
- **Lightweight memory graph** — links documents and chunks for cross-document relationship understanding
- **Agentic retrieval** — hybrid engine combining keyword/path/content/semantic signals (RRF) with autonomous agent navigation through section trees
- **Evidence-based citations** — every result returns source document, section, chunk, and linked assets
- **Multi-modal assets** — images and tables run through VLMs for summarization and feature extraction, then linked back to source chunks
- **Model-agnostic** — default DeepSeek (text) + Qwen-VL (vision); swap OpenAI, DashScope, Zhipu, or Volcengine via env vars
- **Self-hostable** — Docker Compose stack bundles API, worker, and dashboard
- **Apache 2.0 licensed**, open source since May 7, 2026
- **Stack** — Python 3.11+, FastAPI, PostgreSQL, Redis, S3-compatible storage, MinerU (default PDF parser)

## Performance vs Baselines
Internal evaluation on identical agentic RAG tasks (vs raw documents and parser output fed directly to agents):
- **+36%** first-try accuracy
- **+11%** recall
- **79%** accuracy with feedback loop (vs ~53% ceiling on raw docs)

## Links
- [GitHub Repository](https://github.com/Ontos-AI/knowhere)
- [Cloud (managed)](https://knowhereto.ai)
- [Documentation](https://docs.knowhereto.ai/)
- [Source Summary](../sources/knowhere-repo.md)

## Related Pages
- [CodeGraph](../protocols/codegraph.md) — pre-indexed code knowledge graph for code intelligence (comparable codebase pattern)
- [Graphify](../protocols/graphify.md) — open-source knowledge graph platform with MCP integration
- [Fallow](../protocols/fallow.md) — deterministic codebase intelligence engine
- [Glossary](../glossary.md)
- [Master Index](../index.md)
