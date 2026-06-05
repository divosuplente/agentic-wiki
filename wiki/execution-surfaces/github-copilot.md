# GitHub Copilot

**Category:** execution-surfaces
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-18
**Tags:** agent, ide
**Type:** reference
**Level:** beginner

## Description

GitHub Copilot is an AI pair-programmer powered by OpenAI models that provides inline code suggestions, whole-function generation, and chat-based assistance directly inside your IDE. Copilot is widely used as a low-friction daily-driver for developers who want assistance without switching contexts: it lives inside VS Code, JetBrains, Vim, and Visual Studio, and integrates natively with GitHub pull requests, commits, and CLI workflows.

## Setup

1. **Get a license**
   - GitHub Copilot is available through GitHub Individual, Business, or Enterprise accounts. If your organization already has a Copilot Business license, request access from your org admin.
   - If you do not have an organization license, you can start with a [free trial](https://github.com/settings/copilot) using your personal GitHub account.

2. **Install the extension**
   - **VS Code:** Open the Extensions view (`Cmd+Shift+X`), search "GitHub Copilot" and install both **GitHub Copilot** and **GitHub Copilot Chat**. Sign in with your GitHub account when prompted.
   - **JetBrains:** Go to *Settings > Plugins > Marketplace*, search "GitHub Copilot", and restart the IDE.
   - **Visual Studio:** Install the extension from the Visual Studio Marketplace.

3. **Enable in the CLI (optional but recommended)**
   - Install [GitHub CLI](https://cli.github.com), then run:
     ```bash
     gh auth login
     gh extension install github/gh-copilot
     gh copilot --version
     ```

4. **Basic usage**
   - Start typing in any file; Copilot will show ghost-text suggestions. Press `Tab` to accept.
   - Use inline chat (`Cmd+I` in VS Code) to ask questions about the current file.
   - Use the Copilot Chat panel for broader conversations and to generate tests, refactor code, or explain legacy logic.

## Configuration

- **Custom instructions**  
  You can provide global or repository-level instructions so Copilot adheres to your team's coding standards, naming conventions, and preferred frameworks. Create a file named `.github/copilot-instructions.md` in the repository root:
  ```markdown
  ## Context
  This is a .NET 8 microservice using DDD patterns.

  ## Rules
  - Prefer early-return guard clauses.
  - Use `CancellationToken` in all async methods.
  - Write integration tests with xUnit and WebApplicationFactory.
  ```
  These instructions are sent with every request Copilot makes on that repository.

- **VS Code settings (JSON)**  
  ```json
  "github.copilot.enable": {
    "*": true,
    "plaintext": false
  },
  "github.copilot.editor.enableAutoCompletions": true,
  "github.copilot.advanced": {
    "debug.testOverrideProxyUrl": null,
    "authProvider": "github"
  }
  ```

- **Keyboard shortcuts**  
  - Accept suggestion: `Tab`  
  - Accept next word: `Ctrl+Right Arrow` (`Cmd+Right Arrow` on macOS)  
  - Open inline chat: `Ctrl+Cmd+I` (macOS) / `Ctrl+Alt+I` (Windows/Linux)  
  - Open Copilot Chat: `Ctrl+Cmd+I` in the panel  

- **Ignoring files**  
  If you have sensitive files or generated code you do not want Copilot to analyze, add patterns to `.copilotignore` (similar syntax to `.gitignore`).

## Links

- [Official docs](https://docs.github.com/en/copilot)
- [Awesome Copilot](../skills/awesome-copilot.md) — community resources
- [Copilot CLI for Beginners](../skills/copilot-cli-for-beginners.md)
- Our internal setup (internal link removed)

## Related Pages

- [OpenCode](opencode.md)
- [Warp](warp.md)
- [Vercel Skills](../skills/vercel-skills.md)
- [FastAPI Skill](../skills/fastapi.md)
- [Awesome Copilot](../skills/awesome-copilot.md)
- [Copilot CLI for Beginners](../skills/copilot-cli-for-beginners.md)
- [PlaiinConcepts Skills](../skills/plainconcepts-skills.md)
