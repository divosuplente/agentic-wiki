# CanIRun.ai

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** tool, platform
**Type:** reference
**Level:** beginner

## Description
Can your machine run AI models? Detect your hardware and find out which AI models you can run locally. GPU, CPU, and RAM analysis in your browser.

## How It Works
Hardware detection runs in the browser via Web APIs. Estimates GPU VRAM, bandwidth, RAM, and CPU cores to determine model compatibility.

## Model Database
Comprehensive directory of local AI models across providers:

### Popular Models
| Model | Provider | Params | VRAM | License | Tasks |
|-------|----------|--------|------|---------|-------|
| Llama 3.1 8B | Meta | 8B | 4.6 GB | Llama 3.1 Community | chat, code, reasoning |
| Qwen 3.5 9B | Alibaba | 9B | 5.1 GB | Apache 2.0 | chat, vision |
| Phi-4 14B | Microsoft | 14B | 7.7 GB | MIT | reasoning, code |
| GPT-OSS 20B | OpenAI | 21B | 11.3 GB | Apache 2.0 | chat, reasoning, code |
| Mistral Small 24B | Mistral AI | 24B | 12.8 GB | Apache 2.0 | chat, vision, code |
| Gemma 3 27B | Google | 27B | 14.3 GB | Gemma | chat, vision, reasoning |
| Qwen 2.5 Coder 32B | Alibaba | 32B | 16.9 GB | Apache 2.0 | code |
| Llama 3.3 70B | Meta | 70B | 36.4 GB | Llama 3.3 Community | chat, reasoning, code |
| Llama 4 Scout | Meta | 109B | 56.3 GB | Llama 4 Community | chat, vision, reasoning |
| GPT-OSS 120B | OpenAI | 117B | 60.4 GB | Apache 2.0 | chat, reasoning, code |
| Devstral 2 123B | Mistral AI | 123B | 63.5 GB | MRL | code |
| DeepSeek R1 | DeepSeek | 671B | 344.2 GB | MIT | reasoning |
| Kimi K2 | Moonshot AI | 1T | 512.7 GB | Kimi | chat, reasoning, code |

### Filtering Options
- **Grades**: Runs great (S/A/B) | Tight fit (C/D) | Too heavy (F)
- **Tasks**: Chat, Code, Reasoning, Vision, Edge
- **Providers**: 20+ including Meta, OpenAI, Google, Alibaba, Mistral, DeepSeek, NVIDIA

## Features
- Hardware auto-detection via browser APIs
- Real-time compatibility estimation
- Supports quantized formats: Q2_K, Q3_K_M, Q4_K_M, Q5_K_M, Q6_K, Q8_0, F16
- Context window sizes shown per model
- Architecture badges: Dense, MoE
- Active parameter counts for MoE models

## Links
- [Official site](https://www.canirun.ai/)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md)
- Ollama
