# VS Code Agent Hooks

**Category:** learning
**Type:** documentation
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** learning, ide, agent
**Level:** intermediate

## Summary
Official Visual Studio Code documentation on agent hooks — custom shell commands executed at key lifecycle points during Copilot Chat agent sessions. Enables automation, validation, and policy enforcement inside the editor.

## Lifecycle Hooks
Hooks fire at specific stages of a Copilot Chat agent session:
- **Pre-prompt** — before the prompt is sent to the model (e.g., inject context, prepend instructions)
- **Post-response** — after the model responds (e.g., validate output, trigger side effects)
- **File-write** — when the agent proposes writing or modifying a file (e.g., lint-on-save, format check)
- **Tool execution** — before/after the agent invokes a tool

## Configuration
Declarative JSON configuration in `.vscode/copilot-hooks.json`:
```json
{
  "prePrompt": ["./scripts/inject-context.sh"],
  "postResponse": ["./scripts/validate-output.sh"],
  "fileWrite": ["npm run lint", "npm run format -- --check"]
}
```

No extension coding required — hooks are shell commands configured via JSON.

## Use Cases
- **Lint-on-save** — run ESLint/Prettier before the agent writes files
- **Policy checks** — validate that generated code meets security or naming conventions
- **Automated commit messages** — generate conventional commits from agent changes
- **Context injection** — prepend project-specific instructions to every prompt

## Key Takeaways
- Hooks fire at pre-prompt, post-response, and file-write stages.
- Ideal for lint-on-save, policy checks, or automated commit messages.
- Declarative JSON configuration; no extension coding required.
- Brings CI-like quality gates into the agent's real-time workflow.

## Recommended Audience
VS Code power users, platform teams, and compliance-minded organisations.

## Links
- [Read docs](https://code.visualstudio.com/docs/copilot/customization/hooks)

## Related Pages
- [PyCharm 2026.1](pycharm-whats-new-2026-1.md)
- [GitHub Copilot Skill from Scratch](gerald-versluis-copilot-skill-scratch.md)
- [VS Code](https://code.visualstudio.com/)
- [OpenCode](../execution-surfaces/opencode.md)
