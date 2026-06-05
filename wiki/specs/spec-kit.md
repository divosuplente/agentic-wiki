# Spec Kit

**Category:** specs
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** sdd, standard
**Type:** reference
**Level:** intermediate

## Description
A GitHub-native specification-driven development framework. Spec Kit integrates tightly with GitHub repos and issue tracking to provide structured planning for coding agents.

## Philosophy
Spec Kit is GitHub-first: your specs live alongside your code, issues reference specs, and agents can read specs directly from the repo. This tight integration means:
- Specs are version-controlled with your codebase
- Issues can link to specs for context
- Agents read specs from the repo without external dependencies
- PRs can reference spec compliance

## Positioning
Spec Kit sits between GSD (lighter) and Taskmaster AI (heavier) in the SDD spectrum:
- More structure than GSD
- Less ceremony than Taskmaster AI
- More GitHub-native than OpenSpec

## How It Works
1. Write specs in a structured format (Markdown with YAML frontmatter)
2. Store specs in `.github/specs/` or a `specs/` directory
3. Reference specs in issues and PRs via spec IDs
4. Agents read specs during planning and report compliance
5. CI can validate that changes match their referenced specs

## GitHub
- Owner: github
- [Repository](https://github.com/github/spec-kit)

## Links
- [Repository](https://github.com/github/spec-kit)
- [GitHub Blog: Spec-Driven Development](https://github.blog/)

## Prerequisites
- Understanding of [OpenSpec](openspec.md) or general spec-driven development

## Next Steps
- [ASDLC for industrial standards](asdlc.md)
- [Compare SDD frameworks](../learning/agentic-coding-sdd-comparison.md)

## Related Pages
- [OpenSpec](openspec.md)
- [BMAD-METHOD](bmad-method.md)
- [GSD](get-shit-done.md)
- [Agentic Coding SDD Comparison](../learning/agentic-coding-sdd-comparison.md)
- [Claude Task Master](../governance/claude-task-master.md)
- [OpenCode](../execution-surfaces/opencode.md)
