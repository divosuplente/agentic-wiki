# Claude Code Source Code Leak

**Category:** learning
**Type:** social
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** learning
**Level:** all

## Summary
midudev reports that Claude Code's full source was accidentally leaked via an uploaded `.map` file on npm, allowing the code to be reconstructed legibly and with comments intact. A cautionary tale about build-artifact hygiene.

## What Happened
- Anthropic accidentally included a **source map (`.map`)** file in the Claude Code npm package
- Source maps map minified code back to original source — including comments and structure
- Anyone who downloaded the npm package could reconstruct the full source
- The leak was reported by midudev and quickly went viral in the Spanish-speaking dev community

## Key Takeaways
- Ensure `.map` files and sourcemaps are excluded from npm packages.
- CI/CD pipelines should scan for accidental source leakage.
- Security reviews must include build artifacts, not just source code.
- `.npmignore` and build-tool configuration need regular audits.

## Recommended Audience
DevOps, security engineers, and package maintainers.

## Links
- [Read](https://www.linkedin.com/posts/midudev_se-ha-filtrado-todo-el-c%C3%B3digo-fuente-de-share-7444686303591415808-kbDo)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- [Claude Agent SDK in CI/CD](claude-agent-sdk-ci-cd.md)
- [Comprehension Debt](comprehension-debt.md)
