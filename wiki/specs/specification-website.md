# Website Specification (specification.website)

**Category:** specs
**Status:** active
**Added:** 2026-06-05
**Last verified:** 2026-06-05
**Tags:** web-standards, accessibility, security, seo, mcp
**Type:** standard
**Level:** all

## Description
A platform-agnostic website specification that collects the layer cake of web standards (WHATWG HTML, WCAG, IETF, MDN, W3C, schema.org, llmstxt.org) into one sourced reference. Authored by Joost de Valk (Yoast). Every page cites at least one primary source. Built with Astro + TypeScript, deployed on Cloudflare Pages, and ships a bundled MCP server that exposes the spec to MCP-aware agents.

## Rules / Requirements

The spec is organized into 10 categories. Each rule carries a status level:

- **Required** — the web platform contract breaks without it
- **Recommended** — modern sites should do it
- **Optional** — depends on context
- **Avoid** — outdated, harmful, or actively superseded

### Categories

1. **Foundations** — HTML, head, document basics
2. **SEO** — search visibility
3. **Accessibility** — WCAG-aligned rules
4. **Security** — headers, transport, policies
5. **Well-Known URIs** — agreed paths under `/.well-known/`
6. **Agent Readiness** — making a site legible to AI agents (including `llms.txt`)
7. **Performance** — Core Web Vitals, caching, fonts
8. **Privacy** — consent, signals, respecting choice
9. **Resilience** — graceful failure
10. **Internationalisation** — language, locale, direction

## Key Properties
- **Platform-agnostic** — describes outcomes, not framework-specific implementation
- **Fully sourced** — every page cites primary sources (WHATWG, MDN, WCAG, IETF RFCs, Google Search Central, web.dev, Yoast, etc.)
- **Opinionated where standards are silent** — explicit "no settled standard" markers
- **No tracking / no marketing** — aggregate Plausible analytics only, no cookies or newsletter capture
- **MCP server** — Cloudflare Worker in `mcp/` exposes the spec to agents
- **Auto-generated derivatives** — `/spec/`, `/checklist/`, `/llms.txt`, `/llms-full.txt`, `/sitemap-index.xml`, `/rss.xml`, per-page `.md` endpoints, Pagefind search index, and MCP server data are all derived from the source markdown
- **Content** CC BY 4.0 / **Code** MIT

## Sources Drawn Upon
- WHATWG HTML Living Standard
- MDN Web Docs
- WCAG 2.2 and Understanding documents
- IETF RFCs (protocol-level items)
- sitemaps.org, schema.org, llmstxt.org
- Google Search Central, web.dev
- Yoast Developer Portal
- Equalize Digital Accessibility Checker docs
- WP Accessibility Knowledge Base
- Is It Agent Ready?, Overlay Fact Sheet

## Adding or Changing a Spec Page
1. Find the right category under `src/content/spec/<category>/`
2. Copy an existing `.md` file (e.g. `src/content/spec/foundations/title.md`)
3. Fill in frontmatter: `title`, `summary`, `category`, `status`, `order`, `sources`
4. Write the body using sections: `## What it is`, `## Why it matters`, `## How to implement`, `## Common mistakes`, `## Verification`
5. Open a PR — the build fails if the schema is invalid (intentional)

## Links
- [Live Site](https://specification.website)
- [GitHub Repository](https://github.com/jdevalk/specification.website)
- [MCP Server](https://mcp.specification.website/mcp)
- [Source Summary](../sources/specification-website-repo.md)

## Related Pages
- [Modern Web Guidance](../skills/modern-web-guidance.md) — Google Chrome's evergreen skill package for web dev (complementary reference)
- [Master Index](../index.md)
