# What is DESIGN.md — Stitch Docs

**Category:** learning
**Type:** documentation
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** learning, standard
**Level:** intermediate

## Summary
Google Stitch introduces DESIGN.md, a design-system document that AI agents consume to generate consistent UI across a project. It codifies tokens, components, and layout rules in a machine-readable format.

## DESIGN.md Format
A markdown file at the root of your project that defines:
- **Design tokens** — colors, typography, spacing scales
- **Component catalog** — reusable UI components with props and variants
- **Layout rules** — grid systems, breakpoints, responsive behavior
- **Theme support** — light/dark mode, custom theme variables

## Key Takeaways
- DESIGN.md acts as a contract between design and AI-generated code.
- Supports themes, responsive breakpoints, and component variants.
- Compatible with Stitch and other agents that parse structured design specs.
- Placed at project root, consumed by agents before generating UI code.

## Recommended Audience
Design engineers, front-end leads, and teams scaling AI-generated UI.

## Links
- [Read docs](https://stitch.withgoogle.com/docs/design-md/overview)
- [Stitch platform](https://stitch.withgoogle.com/)

## Related Pages
- [Stitch Platform](../execution-surfaces/stitch.md)
- [ARCHITECTURE.md](../ecosystem/architecture-md.md)
- [OpenCode](../execution-surfaces/opencode.md)
- [Pi Coding Agent](../execution-surfaces/pi-coding-agent.md)
