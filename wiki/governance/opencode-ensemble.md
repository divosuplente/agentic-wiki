# OpenCode Ensemble

**Category:** governance
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** orchestration, harness, agent
**Type:** explanation
**Level:** advanced

## Description
Agent teams for OpenCode. Run multiple agents in parallel with messaging between them. Turns single-agent OpenCode workflows into orchestrated teams.

## Key Features
- **Multi-agent teams** — spawn multiple OpenCode agents with different roles
- **Parallel execution** — agents work simultaneously on different parts of a task
- **Inter-agent messaging** — agents communicate results and coordinate
- **Dynamic team composition** — add or remove agents mid-session
- **Conflict resolution** — when agents disagree, the ensemble resolves or escalates
- **Scales single-agent workflows** — existing OpenCode workflows work in ensemble mode

## Use Case
A complex feature requiring frontend, backend, and database changes:
1. Spawn three agents: frontend agent, backend agent, database agent
2. Each agent reads the shared spec and tackles their domain
3. Agents message each other when their work intersects
4. Database agent notifies backend agent when schema changes
5. Backend agent notifies frontend agent when API is ready
6. Ensemble completes when all agents report done

## GitHub
- Owner: hueyexe
- [Repository](https://github.com/hueyexe/opencode-ensemble)

## Links
- [GitHub](https://github.com/hueyexe/opencode-ensemble)

## Prerequisites
- [OpenCode installed](../execution-surfaces/opencode.md)
- Familiarity with running a single agent session

## Next Steps
- [Herdr for terminal persistence](herdr.md)
- [Vibe Kanban for task management](vibe-kanban.md)

## Related Pages
- [Oh My OpenAgent](oh-my-openagent.md)
- [Paseo](paseo.md)
- [AgentCraft](../governance/agentcraft-platform.md)
- [Vibe Kanban](../governance/vibe-kanban.md)
- [Gastown](gastown.md)
- [OpenCode](../execution-surfaces/opencode.md)
