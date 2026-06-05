# ARCHITECTURE.md

**Category:** ecosystem
**Status:** active
**Added:** 2026-05-18
**Last verified:** 2026-05-19
**Tags:** standard, context
**Type:** reference
**Level:** intermediate

## Description
A system template for rapid codebase comprehension — designed to be filled in by your agent so it understands your repo's architecture from day one. ARCHITECTURE.md provides a standardized, AI-readable format for documenting software architecture that coding agents can consume as context.

> "Have your agent fill this in for your repo."

## Template Sections

### 1. Project Structure
High-level overview of directory and file structure, categorized by architectural layer or major functional area. Essential for quickly navigating the codebase, locating relevant files, and understanding separation of concerns.

### 2. High-Level System Diagram
Block diagram or text-based description of major components and their interactions. Focus on data flow, service communication, and key architectural boundaries.

### 3. Core Components
For each major component:
- **Name** — e.g., Web App, API Gateway, Data Processing Service
- **Description** — primary purpose, key functionalities, interaction patterns
- **Technologies** — React, Node.js, Go, PostgreSQL, etc.
- **Deployment** — Vercel, Kubernetes, AWS Lambda, etc.

### 4. Data Stores
List databases, caches, queues, and persistent storage with:
- Name, Type (PostgreSQL, Redis, Kafka, S3)
- Purpose and key schemas/collections

### 5. External Integrations / APIs
Third-party services the system interacts with:
- Service name, purpose, integration method (REST API, SDK, webhook)

### 6. Deployment & Infrastructure
- Cloud provider, key services, CI/CD pipeline
- Monitoring & logging stack

### 7. Security Considerations
- Authentication (OAuth2, JWT, API Keys)
- Authorization (RBAC, ACLs)
- Data encryption (TLS in transit, AES-256 at rest)

### 8. Development & Testing Environment
- Local setup instructions
- Testing frameworks (Jest, Pytest, JUnit)
- Code quality tools (ESLint, SonarQube)

### 9. Future Considerations / Roadmap
Known architectural debts, planned changes, significant future features

### 10. Project Identification
- Project name, repository URL, primary contact, last update date

### 11. Glossary / Acronyms
Project-specific terms and acronyms defined

## Philosophy
ARCHITECTURE.md complements README.md and DESIGN.md conventions. While README is for humans, ARCHITECTURE.md is optimized for agent consumption — structured, comprehensive, and machine-parseable.

## License
Released under MIT License.

## Links
- [Official site](https://architecture.md)/)
- [GitHub](https://github.com/timajwilliams/architecture)
- [Creator: @timajwilliams](https://twitter.com/timajwilliams)

## Related Pages
- [Stitch](../execution-surfaces/stitch.md)
- [Google Antigravity](google-antigravity.md)
- [One to All – Plain Agents Jam](one-to-all-plain-agents-jam.md)
