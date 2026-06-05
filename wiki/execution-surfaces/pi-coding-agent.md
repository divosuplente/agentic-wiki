# Pi Coding Agent

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** agent, terminal, harness
**Type:** reference
**Level:** beginner

## Description
Pi is a **minimal terminal coding harness** by Earendil Inc. It adapts to your workflows, not the other way around. Customize with extensions, skills, prompt templates, and themes. Bundle them as packages and share via npm or git.

> "There are many agent harnesses, but this one is yours."

## Install
```bash
curl -fsSL https://pi.dev/install.sh | sh
# or
npm install -g @earendil-works/pi-coding-agent
```

## Why Pi?
Pi ships with powerful defaults but skips features like sub-agents and plan mode. Ask Pi to build what you want, or install a package that does it your way. Four modes: interactive, print/JSON, RPC, and SDK.

## Key Features
- **15+ Providers, Hundreds of Models**: Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi, MiniMax, OpenRouter, Ollama
- **Switch Models Mid-Session**: `/model` or `Ctrl+L`. Cycle favorites with `Ctrl+P`
- **Tree-Structured, Shareable History**: Sessions stored as trees. `/tree` to navigate, `/export` to HTML, `/share` to GitHub gist
- **Context Engineering**: `AGENTS.md` loaded at startup, `SYSTEM.md` for prompt override, customizable compaction
- **Steer or Follow Up**: `Enter` sends steering message (interrupts current tool), `Alt+Enter` sends follow-up
- **Four Modes**: Interactive TUI, Print/JSON, RPC, SDK (see OpenClaw for real-world integration)
- **Primitives, Not Features**: Build sub-agents, plan mode, permission gates, SSH execution, sandboxing, MCP integration, custom editors, status bars, overlays via extensions

## What Pi Didn't Build (and Why)
| Feature | Pi's Approach |
|---------|--------------|
| MCP | Build CLI tools with skills, or install an extension |
| Sub-agents | Spawn via tmux, or build/import an extension |
| Permission popups | Run in container or build confirmation flow |
| Plan mode | Write plans to files, or build/import |
| Built-in to-dos | Use TODO.md or build an extension |
| Background bash | Use tmux — full observability |

## Extensions
50+ examples in the repo. Bundle extensions, skills, prompts, and themes as packages. Install from npm or git:
```bash
pi install npm:@foo/pi-tools
pi install git:github.com/user/pi-doom
```

## Links
- [Official site](https://pi.dev/)
- [Docs](https://pi.dev/docs/latest)
- [GitHub](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [npm](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
- [Packages](https://pi.dev/packages)
- [Blog](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)

## Related Pages
- [OpenCode](opencode.md)
- [Warp](warp.md)
- [Oh My OpenAgent](../governance/oh-my-openagent.md)
- [Agent Skills Directory](../skills/agent-skills-directory.md)
