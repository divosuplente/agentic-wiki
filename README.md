# Agentic Coding Wiki

A structured, interlinked knowledge base about AI coding agents, skills, harnesses, standards, and ecosystem tools.

## What's inside

The `wiki/` folder contains the curated content:

- **[wiki/README.md](wiki/README.md)** — entry point with role-based navigation
- **[wiki/index.md](wiki/index.md)** — flat master index of all pages by category
- **[wiki/overview.md](wiki/overview.md)** — narrative overview of the agentic-coding landscape
- **[wiki/glossary.md](wiki/glossary.md)** — domain terms and definitions
- **[wiki/log.md](wiki/log.md)** — chronological activity log
- **[wiki/categories/](wiki/)** — pages grouped by Execution Surfaces, Governance, Protocols, Ecosystem, Specs, Skills, Learning, Sources

## Structure

The wiki follows the [Karpathy pattern](https://github.com/karpathy) of three layers:

1. **Raw sources** — uncurated links, notes, and references (immutable)
2. **Schema** — `AGENTS.md` defines the wiki structure, page types, and conventions
3. **AI-maintained wiki** — agents ingest sources, create/update pages, and keep cross-references consistent

Pages use plain Markdown with simple YAML frontmatter. Every entity page has a `Related Pages` section with relative links, and the wiki is navigable from any starting point.

## License

This repository uses a dual-license scheme:

- **Wiki content** (the textual content under `wiki/`, including markdown pages and embedded prose/diagrams) is released under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). See [`LICENSE-CC-BY-4.0`](LICENSE-CC-BY-4.0) for the full text.
- **Code samples, scripts, configuration, and other machine-readable artifacts** (the `README.md` and `.gitignore` at the root, plus any code blocks within wiki pages) are released under the [MIT License](https://opensource.org/licenses/MIT). See [`LICENSE`](LICENSE) for the full text.
