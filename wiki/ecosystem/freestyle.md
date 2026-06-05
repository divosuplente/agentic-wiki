# Freestyle

**Category:** ecosystem
**Status:** active
**Added:** 2026-06-05
**Last verified:** 2026-06-05
**Tags:** voice, dictation, desktop, local-first
**Type:** tool
**Level:** all

## Description
Freestyle is a free, open-source, local-first voice-to-text dictation application. Hold a hotkey to record, release to paste cleaned-up text at the cursor position. Multi-provider support (OpenAI, Groq, Anthropic, Google, Deepgram, ElevenLabs) with bring-your-own API key, plus post-processing for grammar/punctuation, custom phrase dictionaries, and contextual correction (auto-formatting by target app).

## Key Features
- **Hold-to-record hotkey** — record while held, paste on release at the current cursor position
- **Multi-provider STT** — OpenAI, Groq, Anthropic, Google, Deepgram, ElevenLabs (BYO API key)
- **Transcription cleanup** — grammar and punctuation post-processing removes "um, oh, but" filler
- **Custom dictionary** — phrase-level replacements applied after transcription (e.g. `"type script"` → `TypeScript`)
- **Contextual correction** — reformat text based on the active app/field (e.g. email body)
- **Local-first** — dictations stay on device; only the chosen STT API is contacted
- **Cross-platform** — macOS (Apple Silicon + Intel), Windows, Linux (AppImage / .deb)
- **MIT licensed**, open source

## Links
- [GitHub Repository](https://github.com/freestyle-voice/freestyle)
- [Official Site](https://freestylevoice.com)
- [Source Summary](../sources/freestyle-repo.md)

## Related Pages
- [OpenCode](../execution-surfaces/opencode.md) — open-source coding agent (comparable local-first dev tooling)
- [Glossary](../glossary.md)
- [Master Index](../index.md)
