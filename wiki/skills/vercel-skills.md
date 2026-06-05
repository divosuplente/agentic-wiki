# Vercel Skills

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, platform
**Type:** reference
**Level:** intermediate

## Description
Vercel's skills ecosystem: a CLI for installing and managing agent "skill packages." Add a skill package with `npx skills add <package>`, with more commands planned. This ecosystem allows developers to share and reuse agent capabilities across projects.

## Install
```bash
npx skills add <package>
```

## Key Features
- **CLI-first** — install skills via npx, no global setup required
- **Open ecosystem** — publish and share skills across the community
- **Versioned packages** — skills are versioned npm packages
- **Framework-aware** — skills can detect project type and adapt behavior
- **Planned expansion** — more management commands (list, update, remove) coming

## How It Works
1. Find a skill on the registry or npm
2. Run `npx skills add <package>` in your project
3. The skill integrates with your agent's context and triggering rules
4. Use the skill's commands (e.g., `/skill-name`) in agent sessions

## Links
- [Documentation](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem)
- [The Agent Skills Directory](https://skills.sh/)

## Related Pages
- [The Agent Skills Directory](agent-skills-directory.md)
- [Awesome Copilot](awesome-copilot.md)
- [FastAPI Skill](fastapi.md)
- [OpenCode](../execution-surfaces/opencode.md)
