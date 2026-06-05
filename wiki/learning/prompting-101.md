# Prompting 101: Write Your First Effective Prompt

**Category:** learning
**Type:** tutorial
**Status:** active
**Added:** 2026-05-28
**Last verified:** 2026-05-28
**Tags:** beginner, tutorial, prompting
**Level:** beginner

## Description
A beginner-friendly tutorial on crafting prompts that get reliable results from AI coding agents like OpenCode, Claude Code, and GitHub Copilot.

## The Four-Part Framework

### 1. Objective (What, not How)
State the desired outcome, not the implementation steps.

**Weak:** "Open file X, find function Y, add try-catch around Z"  
**Strong:** "Fix the validationToken middleware crash when receiving expired JWTs"

### 2. Context (What the Agent Needs to Know)
Project-specific information the agent can't infer.

Examples:
- "We use Zod for validation, not Joi"
- "This is a Next.js 15 app with App Router"
- "Tests are in `__tests__/` directories next to source files"

### 3. Constraints (Guardrails)
Explicit boundaries about what the agent should NOT do.

Examples:
- "Don't modify the database schema"
- "Keep backward compatibility with the v2 API"
- "Don't install new dependencies without asking first"

### 4. Verification (How to Check Success)
Concrete, automated ways to confirm completion.

Examples:
- "Run `pnpm test` after making changes"
- "Verify the build passes with `pnpm build`"

## Before/After Examples

### Example 1: Authentication
**❌ Before:** "Add authentication to my app"

**✅ After:**
```markdown
## GOAL
Implement JWT-based authentication for the REST API so only verified users can access protected endpoints.

## SCOPE
- Files: `src/routes/auth.js`, `src/middleware/auth.js`, `src/utils/token.js`
- Do NOT touch: database schema, frontend code, or existing user registration flow

## CONTEXT
- We use Express.js with a PostgreSQL database via Prisma
- Existing `User` model has `email` and `passwordHash` fields
- Passwords are hashed with bcrypt (already installed)
- We use `jsonwebtoken` (already installed)

## CONSTRAINTS
- Do not install new npm packages
- Keep all changes within the existing `src/` directory
- Maintain backward compatibility with the current login endpoint (`POST /login`)

## FORMAT
- Return a diff-style summary of changes
- Use standard Express middleware patterns
- Name the JWT verification middleware `requireAuth`

## ACCEPTANCE
- `POST /login` returns a valid JWT on correct credentials
- `GET /profile` with a missing/invalid token returns 401
- `GET /profile` with a valid token returns the user object
- Run `npm test` and confirm the auth test suite passes
```

### Example 2: CSV Parser
**❌ Before:** "Create a function to parse CSV data"

**✅ After:**
```markdown
## TASK
Write a utility function `parseCSV(input)` that converts a CSV string into an array of objects.

## CONTEXT
- This runs in a Node.js 18+ environment
- Input will be raw CSV text from file uploads, not streams
- We already use `zod` for validation elsewhere in the project

## CONSTRAINTS
- Do not use external CSV parsing libraries (no `csv-parser`, `papaparse`, etc.)
- Max file size handled elsewhere; assume input string is ≤ 1 MB
- Handle CRLF (`\r\n`) and LF (`\n`) line endings
- Assume the first line is always the header row

## FORMAT
- Export a single default function from `src/utils/parseCSV.js`
- Return type: `Array<Record<string, string>>`
- Strip surrounding whitespace from each cell
- Skip completely empty lines

## EXAMPLES
Input:
```
name,age,city
Alice,30,New York
Bob,25,Los Angeles
```

Expected output:
```json
[
  { "name": "Alice", "age": "30", "city": "New York" },
  { "name": "Bob", "age": "25", "city": "Los Angeles" }
]
```

## ACCEPTANCE
- `parseCSV` correctly parses the example above
- Returns an empty array for empty input
- Handles quoted fields with commas inside: `"New York, NY"`
- Add a test file `src/utils/parseCSV.test.js` with 5 test cases
- Run `npm test` and confirm all tests pass
```

### Example 3: Too Broad
**❌ Before:** "Build a user profile page with editing capabilities"

**✅ After:**
```markdown
## GOAL
Build the backend API endpoint for updating a user's profile.

## SCOPE (In-bounds)
- `src/routes/profile.js` — add `PUT /api/profile`
- `src/services/profileService.js` — business logic for updates
- `src/validators/profileValidator.js` — input validation

## SCOPE (Out-of-bounds)
- Do NOT build any frontend UI
- Do NOT add file upload or avatar handling
- Do NOT modify the auth middleware

## CONTEXT
- Express.js app with Prisma ORM
- User model fields: `id`, `email`, `displayName`, `bio`, `updatedAt`
- Auth middleware already attaches `req.user` with the authenticated user's ID
- Existing `GET /api/profile` returns the current user's profile

## CONSTRAINTS
- Only allow updating `displayName` (max 50 chars) and `bio` (max 500 chars)
- Email is read-only
- Return 400 with clear validation errors for invalid input
- Return 200 with the updated profile on success
- Use Zod for validation (already installed)

## FORMAT
- Follow the existing route/service/validator pattern used in `src/routes/auth.js`
- Return JSON: `{ success: true, profile: { ... } }`

## ACCEPTANCE
- `PUT /api/profile` with valid data updates the DB and returns the new profile
- `PUT /api/profile` with a 60-character displayName returns 400
- `PUT /api/profile` without auth returns 401
- Run `npm test` and confirm the profile update tests pass

## NEXT STEP (separate prompt)
Once this backend is verified, we will build the React frontend form in a follow-up prompt.
```

## Common Mistakes

1. **Micromanaging Implementation** — Give goals, not exact steps
2. **Omitting Verification Steps** — Always include test commands
3. **Assuming Shared Context** — State your business rules explicitly
4. **One Massive Prompt** — Break complex tasks into sequential prompts
5. **Not Using Persistent Rules Files** — Create AGENTS.md or CLAUDE.md
6. **Treating Agents Like Chatbots** — Give complete instructions upfront
7. **Vague Acceptance Criteria** — "Make it robust" → specific testable criteria

## Quick Reference Checklist

Before submitting a prompt, verify it includes:
- [ ] Objective: Clear statement of finished state
- [ ] Context: 2-4 project-specific details
- [ ] Constraints: 3-5 explicit guardrails
- [ ] Format: How output should be structured
- [ ] Acceptance: 1-3 verifiable completion criteria
- [ ] Scope: In-bounds and out-of-bounds files
- [ ] Examples: Sample input/output if applicable
- [ ] No vagueness: Removed "make it better" or "handle edge cases"

## Recommended Next Steps
1. Start small with micro-prompts
2. Build your AGENTS.md rules file
3. Use the validation loop (always check output yourself)
4. Break down work into smallest verifiable pieces
5. Save effective prompts as templates

## Sources
- [The Complete Guide to Prompting AI Coding Agents (2026)](https://sureprompts.com/blog/the-complete-guide-to-prompting-ai-coding-agents-2026) — SurePrompts Team
- [Prompting AI Agents: Instructions That Actually Work](https://fieldguidetoai.com/guides/prompting-ai-agents) — Field Guide to AI (2026)
- [PROMPT_ENGINEERING.md](https://github.com/tweag/agentic-coding-handbook/blob/main/PROMPT_ENGINEERING.md) — Tweag Agentic Coding Handbook

## Prerequisites
- An AI coding agent installed (e.g., [OpenCode](../execution-surfaces/opencode.md))

## Next Steps
- [Build a tiny project end-to-end](first-project-tutorial.md)
- [Caveman for token optimization](../skills/caveman.md)
- [Spec-driven development](../specs/openspec.md)

## Related Pages
- [Karpathy: From Vibe Coding to Agentic Engineering](karpathy-vibe-coding-agentic.md)
- [Comprehension Debt](comprehension-debt.md)
