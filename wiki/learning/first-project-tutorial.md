# Build a Tiny Project: URL Title Extractor CLI

**Category:** learning
**Type:** tutorial
**Status:** active
**Added:** 2026-05-28
**Last verified:** 2026-05-28
**Tags:** beginner, tutorial, hands-on, nodejs
**Level:** beginner

## Description
A 30-45 minute hands-on project that teaches core agent interaction patterns by building a CLI tool that takes a URL and prints the page title. No external API keys required.

## What You'll Build
A Node.js CLI tool that:
- Accepts a URL as a command-line argument
- Fetches the page HTML
- Extracts the `<title>` tag content
- Prints the title (or a friendly error message)

## Prerequisites
- [OpenCode installed](../execution-surfaces/opencode.md) (or Claude Code / Warp)
- Node.js ≥ 18
- Basic terminal familiarity
- (optional) [Prompting 101](prompting-101.md)

## Project Setup

### Step 1: Initialize the project
Prompt your agent:
> "Create a new Node.js project in `~/projects/url-title`. Initialize a git repo, create package.json with a `start` script, and set up a basic directory structure with `src/` and `bin/` folders."

### Step 2: Implement the core fetcher
Prompt your agent:
> "In `src/fetcher.js`, write a function `fetchHTML(url)` that uses the built-in `https` module to fetch HTML from a URL. Handle redirects (301/302), 404 errors, and network timeouts (5 seconds). Return the HTML as a string."

### Step 3: Extract the title
Prompt your agent:
> "In `src/extractor.js`, write a function `extractTitle(html)` that extracts the content of the `<title>` tag using a lightweight regex or string parsing (no external libraries). Handle missing titles gracefully. Return the title string or null."

### Step 4: Build the CLI
Prompt your agent:
> "In `bin/cli.js`, create a CLI that: accepts a URL argument from `process.argv[2]`, calls the fetcher and extractor, prints the title, and exits with code 0 on success or 1 on error. Add friendly error messages for invalid URLs or network failures."

### Step 5: Wire it together
Prompt your agent:
> "Create `src/index.js` that exports both `fetchHTML` and `extractTitle`. Update `package.json` so `npm start` runs `bin/cli.js` with the URL argument passed through."

### Step 6: Test and debug
Test against these URLs:
```bash
npm start -- https://example.com
npm start -- https://github.com
npm start -- https://nonexistent.domain.xyz
npm start -- "not-a-url"
```

For any failures, prompt your agent:
> "The tool fails on [specific case]. The error is [paste error]. Fix it."

### Step 7: Polish
Prompt your agent:
> "Add a README.md with installation instructions, usage examples, and a note about handling encoding issues. Add a simple test script in `test/basic.test.js` that checks the extractor against known HTML strings."

## Key Learning Outcomes

### Agent Patterns Practiced:
1. **Prompt refinement** — breaking "build a CLI" into concrete steps
2. **Iterative development** — one feature per prompt with verification
3. **Debugging with the agent** — "it fails on X, fix it"
4. **Code verification** — testing each step before continuing

### Technical Concepts:
- HTTP requests with Node.js `https`
- HTML parsing (lightweight)
- CLI argument handling
- Error handling and exit codes
- Project structure for maintainability

## Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Over-engineering | Start with minimal fetch + regex, add features later |
| Ignoring edge cases | Explicitly test: missing title, invalid URL, timeout, non-HTML |
| Poor error handling | Ask agent for "user-friendly error messages" |
| No input validation | Have agent validate URL format before fetching |
| Hard-to-test code | Structure with separable functions (fetch, parse, CLI) |

## Extension Ideas
Once the basic tool works, try:
- Add JSON output mode (`--json` flag)
- Extract meta description alongside title
- Add a cache to avoid re-fetching the same URL
- Support multiple URLs in one command
- Add color output with `chalk`

## Sources
- Reference implementation: [sindresorhus/article-title-cli](https://github.com/sindresorhus/article-title-cli)
- Python implementation: [impredicative/urltitle](https://github.com/impredicative/urltitle/)
- OpenCode beginner guide: [ivern.ai](https://ivern.ai/blog/how-to-use-opencode-beginner-guide)

## Next Steps
- [Agent Customizer path](../paths/agent-customizer.md) — learn to install and write skills
- [Caveman for token optimization](../skills/caveman.md)
- [Spec-driven development](../specs/openspec.md)

## Related Pages
- [Prompting 101](prompting-101.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [First-Time Agent User Path](../paths/first-time-agent-user.md)
