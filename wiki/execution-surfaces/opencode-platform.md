# OpenCode

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** agent, platform
**Type:** reference
**Level:** beginner

## Description
OpenCode is an open source AI coding agent that helps you write code in your terminal, IDE, or desktop. Common use cases include rapid prototyping, refactoring large files, and acting as a harness for custom skills.

## Key Facts
- **160K+ GitHub Stars**
- **900+ Contributors**
- **7.5M+ Monthly Developers**
- **13,000+ Commits**

## Key Features
- **LSP Enabled**: Automatically loads the right LSPs for the LLM
- **Multi-session**: Start multiple agents in parallel on the same project
- **Share Links**: Share a link to any session for reference or debugging
- **GitHub Copilot**: Log in with GitHub to use your Copilot account
- **ChatGPT Plus/Pro**: Log in with OpenAI to use your Plus/Pro account
- **Any Model**: 75+ LLM providers through Models.dev, including local models
- **Any Editor**: Terminal interface, desktop app, and IDE extension
- **Privacy First**: Does not store any code or context data

## Install
```bash
curl -fsSL https://opencode.ai/install | bash
```
Also available via npm, bun, brew, paru.

## Products
- **OpenCode** — open source agent (CLI, desktop app beta on macOS/Windows/Linux)
- **Zen** — access to handpicked, benchmarked AI models for coding agents
- **Go** — enterprise offering

## Provider Directory (75+)
OpenCode uses the AI SDK and Models.dev to support 75+ LLM providers and local models:

### Cloud Providers
Anthropic (Claude), OpenAI (ChatGPT Plus/Pro), GitHub Copilot, Azure OpenAI, Google Vertex AI, Amazon Bedrock, DeepSeek, xAI, Moonshot AI (Kimi), MiniMax, Cerebras, Groq, Fireworks AI, Together AI, OpenRouter, Nebius, Baseten, IO.NET, IO.NET, 302.AI, FrogBot, Cortecs, Deep Infra, Z.AI

### Local / Self-Hosted
Ollama, Ollama Cloud, LM Studio, llama.cpp, Atomic Chat, NVIDIA (build.nvidia.com + NIM on-prem)

### Enterprise / Platform
Azure Cognitive Services, SAP AI Core, GitLab Duo, Cloudflare AI Gateway, Cloudflare Workers AI, DigitalOcean Inference Engine, Vercel AI Gateway, Helicone, ZenMux, STACKIT, OVHcloud AI Endpoints, Scaleway, Venice AI, LLM Gateway

### OpenCode Native
- **OpenCode Zen** — tested and verified models provided by the OpenCode team
- **OpenCode Go** — low-cost subscription for popular open coding models

### Quick Provider Setup
```bash
/connect              # Add a provider's API keys
/models               # Select a model
```

## Configuration
- `opencode.json` / `opencode.jsonc` — project-level config for models, agents, and MCP servers
- `~/.config/opencode/` — global user settings and skill directories
- Environment variables: `OPENCODE_PROVIDER`, `OPENCODE_MODEL`, `OPENCODE_API_KEY`

## Extensions
The OpenCode ecosystem includes plugins for:
- **Quota management** — [Opencode Quota](../skills/opencode-quota.md)
- **Dynamic context pruning** — [Opencode Dynamic Context Pruning](../skills/opencode-dynamic-context-pruning.md)
- **Harnesses** — [Oh My OpenAgent](../governance/oh-my-openagent.md), [Paseo](../governance/paseo.md)

## Links
- [Official site](https://opencode.ai/)
- [GitHub](https://github.com/anomalyco/opencode)
- [Docs](https://opencode.ai/docs)
- [Changelog](https://opencode.ai/changelog)
- [Discord](https://opencode.ai/discord)
- [Providers Docs](https://opencode.ai/docs/providers)

## Related Pages
- [OpenCode Agent Setup](../execution-surfaces/opencode.md)
- [Pi Coding Agent](../execution-surfaces/pi-coding-agent.md)
- [Warp](warp.md)
- [Context7](../protocols/context7.md)
- [RTK](../ecosystem/rtk.md)
