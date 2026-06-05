# Modern Web Guidance

**Category:** skills
**Status:** active
**Added:** 2026-05-22
**Last verified:** 2026-05-22
**Tags:** skill, web, accessibility, performance, security
**Type:** reference
**Level:** intermediate

## Description
Modern Web Guidance is an evergreen, expert-vetted skill package from Google Chrome that guides AI coding agents across common web-development use cases. It helps agents build modern web experiences that are accessible, performant, and secure by default. The package installs via standard skill registries and integrates directly with Claude Code, GitHub Copilot CLI, Antigravity CLI, and Vercel Skills.

## Installation

### Vercel Skills
```bash
npx skills add GoogleChrome/modern-web-guidance
```

### Claude Code
```
/plugin marketplace add GoogleChrome/modern-web-guidance
```

### GitHub Copilot CLI
Use the same plugin marketplace command as Claude Code.

### Antigravity CLI
```bash
agy plugin install https://github.com/GoogleChrome/modern-web-guidance
```

### Generic (npx)
```bash
npx modern-web-guidance@latest install
```

## Key Topics
- **Accessibility** — WCAG-compliant patterns, semantic HTML, ARIA best practices
- **Performance** — Core Web Vitals, lazy loading, image optimization, bundle size
- **CSS and UI** — Modern layout (Flexbox, Grid), container queries, custom properties
- **Privacy and Security** — CSP, HTTPS, cookie best practices, secure credential handling
- **Identity** — Passkeys, federated identity, OAuth/OIDC integration
- **Payments** — Payment Request API, digital wallet integration
- **Progressive Web Apps** — Service workers, offline support, installability, manifest
- **Web Components and Frameworks** — Reusable components, interoperability, SSR guidance
- **Baseline Conformance** — Cross-browser feature availability and progressive enhancement

## How It Works
1. Install the skill via your agent's preferred CLI or marketplace
2. The skill injects expert-vetted guidelines into the agent's context
3. When generating or reviewing code, the agent references the skill for accessibility, performance, security, and Baseline conformance
4. Keeps agents aligned with evergreen web standards as the platform evolves

## Links
- [Official Documentation](https://developer.chrome.com/docs/modern-web-guidance)
- [GitHub Repository](https://github.com/GoogleChrome/modern-web-guidance)
- [Vercel Skills Directory](https://skills.sh/)

## Related Pages
- [Vercel Skills](vercel-skills.md)
- [Claude Code](../execution-surfaces/claude-code.md)
- [GitHub Copilot](../execution-surfaces/github-copilot.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [FastAPI Skill](fastapi.md)
