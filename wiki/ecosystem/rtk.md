# RTK (Rust Token Killer)

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-21
**Tags:** token-optimizer, tool
**Type:** reference
**Level:** intermediate

## Description
CLI proxy written in Rust that reduces LLM token consumption by **60-90%**. Single binary, 100+ commands, <10ms overhead. Smart filtering, grouping, truncation, deduplication.

## Key Features
- Hook-based auto-rewrite for 13+ agents (Claude Code, Copilot, Cursor, Codex, Gemini, OpenCode, etc.)
- 100+ supported commands

## Installation
```bash
curl -fsSL https://rtk.ai/install.sh | sh
rtk init -g
```

## Links
- [GitHub](https://github.com/rtk-ai/rtk)
- [Website](https://rtk.ai/)
- [Source Summary](../sources/rtk-website.md)

## Prerequisites
- Claude Code or another agent with PreToolUse hooks
- Basic understanding of token usage

## Next Steps
- [snip for Go-based filtering](snip.md)
- [tok for Rust auto-rewrite](tok.md)

## Related Pages
- [snip](snip.md)
- [tok](tok.md)
- [ntk](ntk.md)
- [tokf](tokf.md)
- [tkn](tkn.md)
