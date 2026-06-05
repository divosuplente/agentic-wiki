# midudev/autoskills

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill
**Type:** reference
**Level:** advanced

## Description
One command. Your entire AI skill stack. Installed.

`autoskills` scans your project, detects your tech stack, and installs curated AI agent skills automatically. No config needed. Security-checked by maintainers before entering the registry.

## Installation
```bash
npx autoskills
```

## How It Works
1. Run `npx autoskills` in your project root
2. `package.json`, Gradle files, and config files are scanned to detect technologies
3. The best matching AI agent skills are selected from the audited autoskills registry
4. Only selected skill files are downloaded from the registry and verified before writing locally
5. Writes `skills-lock.json` with installed source and bundle hash

## Security Model
**Zero live downloads from random upstream at runtime.**
- Skills synced by maintainers into repo-local registry
- Scanned for prompt-injection and supply-chain risks
- SHA-256 hashes recorded in manifest
- Only needed skills downloaded from curated registry, verified against manifest

## Supported Tech Stacks
- **Frontend & UI:** React, Next.js, Vue, Nuxt, Svelte, Angular, Astro, Tailwind CSS, shadcn/ui, GSAP, Three.js
- **Languages:** TypeScript, Node.js, Go, Bun, Deno, Dart
- **Backend & APIs:** Express, Hono, NestJS, Spring Boot
- **Mobile & Desktop:** Expo, React Native, Flutter, SwiftUI, Android, Tauri, Electron
- **Data & Storage:** Supabase, Neon, Prisma, Drizzle ORM, Zod, React Hook Form
- **Auth & Billing:** Better Auth, Clerk, Stripe
- **Testing:** Vitest, Playwright
- **Cloud & Infra:** Vercel, Vercel AI SDK, Cloudflare, Durable Objects, AWS, Azure, Terraform
- **Media & AI:** Remotion, ElevenLabs

## Options
- `-y, --yes` — skip confirmation
- `--dry-run` — show what would install without installing

## Requirements
Node.js ≥ 22

## GitHub
- Owner: midudev
- Stars: 5.6k | Forks: 524
- License: CC BY-NC 4.0
- Primary Languages: Ruby 95.8%, TypeScript 1.7%

## Links
- [Repository](https://github.com/midudev/autoskills)
- [Website](https://autoskills.sh)

## Related Pages
- [The Agent Skills Directory](agent-skills-directory.md)
- [Vercel Skills](vercel-skills.md)
- [Community Skills Repository](plainconcepts-skills.md)
