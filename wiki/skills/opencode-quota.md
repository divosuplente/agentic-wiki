# Opencode Quota

**Category:** skills
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** skill, token-optimizer
**Type:** reference
**Level:** intermediate

## Description
Quota, usage, and token visibility for OpenCode with **zero context window pollution**. Supports 20+ providers including OpenCode Go, Cursor, GitHub Copilot, OpenAI, Kimi Code, Alibaba Coding Plan, Chutes AI, Google Antigravity, Z.ai Coding Plan, and more.

## Install
```bash
npx @slkiser/opencode-quota init
```
Requires OpenCode ≥ 1.4.3 and Node.js ≥ 18.

## What You Get
- Quota Sidebar panel in the TUI
- Popup quota toasts
- Compact status line
- `/quota` and `/quota_status` slash commands
- Token reports: `/tokens_today`, `/tokens_weekly`, `/tokens_monthly`, `/tokens_session`
- Provider diagnostics for auth, quota sources, and pricing

## Supported Providers
Anthropic (Claude), GitHub Copilot, OpenAI, Cursor, Qwen Code, Alibaba Coding Plan, MiniMax, Kimi Code, Chutes AI, Crof.ai, Synthetic, Z.ai, Zhipu, NanoGPT, Google Antigravity, Gemini CLI, OpenCode Go

## Commands
| Command | What it shows |
|---------|--------------|
| `opencode-quota show` | Terminal quick glance |
| `/quota` | Detailed report |
| `/quota_status` | Config, auth, pricing diagnostics |
| `/pricing_refresh` | Refresh pricing data |
| `/tokens_today` / `_weekly` / `_monthly` / `_all` / `_session` | Token usage reports |

## Troubleshooting
- Run `/quota_status` first
- Companion auth plugins must be loaded before `@slkiser/opencode-quota`
- Token reports require `opencode.db` (created after first OpenCode run)

## GitHub
- Owner: slkiser
- Stars: 466 | Forks: 35
- License: MIT
- Primary Languages: TypeScript 96.8%

## Links
- [Repository](https://github.com/slkiser/opencode-quota)
- [npm](https://www.npmjs.com/package/@slkiser/opencode-quota)

## Related Pages
- [Opencode Dynamic Context Pruning](opencode-dynamic-context-pruning.md)
- [OpenCode](../execution-surfaces/opencode.md)
