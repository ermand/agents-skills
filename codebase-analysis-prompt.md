# Codebase Analysis & Documentation Generation Prompt

> **Purpose:** Use this prompt with Claude Code to analyze an existing codebase and generate comprehensive documentation for onboarding new engineers and enabling AI coding agents to work at senior-engineer level.
>
> **Usage:**
> ```bash
> # Option 1: Interactive mode
> claude-code
> > /read prompts/codebase-analysis-prompt.md
>
> # Option 2: Direct execution
> claude-code --print "$(cat prompts/codebase-analysis-prompt.md)"
>
> # Option 3: Scoped to a specific module
> claude-code --print "Focus on src/modules/payments/ only. $(cat prompts/codebase-analysis-prompt.md)"
> ```

---

## Role & Objective

You are a **principal engineer** tasked with deeply analyzing this codebase and producing comprehensive, high-quality documentation. Your output will serve two distinct audiences:

1. **New engineers** joining the team who need to become productive within their first week.
2. **AI coding agents** (Claude Code, Copilot, Cursor, etc.) who need precise, structured context to make senior-level contributions without hallucinating patterns or conventions.

All generated documents must go into a `./docs/` directory at the project root. If the directory doesn't exist, create it.

---

## Phase 1: Discovery & Architecture Analysis

Thoroughly explore the project structure before writing anything. Read config files, entry points, route definitions, model files, migration files, Dockerfiles, CI configs, and READMEs.

---

### 1.1 — `docs/ARCHITECTURE.md`

Produce a document covering:

- **System overview:** What this project does in 2–3 sentences.
- **High-level architecture:** Draw ASCII or Mermaid diagrams showing major components and how they connect.
- **Service boundaries:** Identify if it's a monolith, modular monolith, or microservices. Document how services/modules communicate (REST, gRPC, message queues, events, direct imports).
- **Request lifecycle:** Trace a typical user request end-to-end through the system — from HTTP entry point through middleware, controllers, services, repositories, database, and back.
- **Infrastructure dependencies:** List every external dependency — databases (PostgreSQL, MongoDB, etc.), caches (Redis, Memcached), message brokers (RabbitMQ, Kafka, SQS), search engines (Elasticsearch), external APIs, CDNs, object storage (S3).
- **Deployment topology:** How is this deployed? (Docker Compose, Kubernetes, serverless, VPS, PaaS). Note any staging/production environment differences.
- **Async processing:** Background jobs, queues, cron jobs, scheduled tasks — what runs outside the request cycle.

**Mermaid diagram requirements:**
```
Include at minimum:
- A system context diagram (C4 Level 1)
- A container diagram (C4 Level 2) if multiple services exist
- A request flow sequence diagram for the most common user action
```

---

### 1.2 — `docs/TECH_STACK.md`

Produce a document covering:

- **Languages & versions:** Read from `package.json`, `composer.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `.tool-versions`, `Dockerfile`, or equivalent.
- **Frameworks:** Primary framework and version (e.g., NestJS 10.x, Laravel 11.x, FastAPI 0.100+).
- **Key libraries & rationale:** List significant dependencies and infer WHY they were chosen based on usage patterns. Don't just list — explain.
- **Database & ORM:** Which database engine, which ORM/query builder, migration tool.
- **Build & dev tools:** Bundlers (Webpack, Vite, esbuild), task runners, monorepo tools (Turborepo, Nx, Lerna).
- **Testing stack:** Test runner, assertion library, mocking tools, e2e framework.
- **CI/CD pipeline:** Read from `.github/workflows/`, `Jenkinsfile`, `.gitlab-ci.yml`, `bitbucket-pipelines.yml`, or equivalent. Document every pipeline stage.
- **Code quality tools:** Linters (ESLint, PHPStan, Ruff), formatters (Prettier, Black), pre-commit hooks.
- **Notable dev dependencies:** Anything a new developer needs to know about — code generators, seed scripts, CLI tools.

---

### 1.3 — `docs/DATA_MODELS.md`

Produce a document covering:

- **Complete schema inventory:** Every table/collection with all columns/fields, types, defaults, constraints.
- **Source of truth:** Read from migration files, ORM model definitions, or raw SQL schemas — state which source you used.
- **Relationships:** For every foreign key or reference, document the relationship type (1:1, 1:N, M:N) and the related entity.
- **Entity-relationship diagram:** Generate a Mermaid ER diagram covering all entities.
- **Special patterns:** Identify and document:
  - Soft deletes (`deleted_at`, `is_active`)
  - Polymorphic relations
  - JSON/JSONB columns (document their expected shape)
  - Enums (list all possible values)
  - Audit columns (`created_at`, `updated_at`, `created_by`)
  - Multi-tenancy patterns (tenant_id, organization scoping)
- **Data integrity:** Note which rules are enforced at DB level (constraints, triggers) vs. application level (validation, middleware).
- **Indexes:** List all non-primary indexes and their purpose (performance, uniqueness, full-text search).

---

## Phase 2: Domain & Business Logic Mapping

---

### 2.1 — `docs/DOMAIN_MAP.md`

Produce a document covering:

- **Bounded contexts:** Identify all distinct domain areas in the codebase.
- **For each domain/module:**
  - Purpose and responsibility (1–2 sentences)
  - Key entities and value objects
  - Business rules and invariants
  - Events produced or consumed
  - External integrations
- **Directory ownership:** Map which directories/modules own which domain.
- **Domain dependency graph:** Which domains depend on which others? Generate a Mermaid diagram.
- **Ubiquitous language glossary:** Define every domain-specific term as it is used in THIS codebase. Format:

```markdown
| Term | Definition | Used In |
|------|-----------|---------|
| Coefficient | The odds multiplier applied to a bet | `src/modules/betting/` |
```

---

### 2.2 — `docs/API_REFERENCE.md`

Produce a document covering:

- **Every endpoint:** Method, path, description, authentication requirement.
- **Request shape:** Headers, query params, path params, body schema (with types and required/optional).
- **Response shape:** Success response structure, error response structure, status codes.
- **Grouping:** Organize by domain area, not by controller file.
- **Authentication & authorization:** Which endpoints need auth? What roles/permissions are required?
- **Pagination patterns:** How does the API paginate? (cursor, offset, page-based)
- **Error conventions:** Standard error response shape, error codes, validation error format.
- **Rate limits:** If any rate limiting exists, document it per-endpoint or globally.
- **Websocket/SSE endpoints:** If any real-time endpoints exist, document their event types and payload shapes.

**Source:** Read from route files, controller decorators/annotations, middleware, OpenAPI/Swagger specs if they exist.

---

### 2.3 — `docs/BUSINESS_RULES.md`

Produce a document covering:

- **Rule inventory:** Extract every non-trivial business rule from the codebase.
- **For each rule:**
  - **What:** Plain English description of the rule
  - **Where:** File path(s) and line number(s) where it's enforced
  - **When:** What triggers this rule (user action, cron, event, state change)
  - **Edge cases:** How edge cases are handled
  - **Dependencies:** Other rules or state this rule depends on
- **Validation logic:** Document all input validation rules, grouped by entity/endpoint.
- **State machines:** If any entity has a lifecycle (e.g., order: pending → confirmed → shipped → delivered), document it with a Mermaid state diagram.
- **Permission & authorization rules:** Who can do what? Document the full RBAC/ABAC model.
- **Scattered rules warning:** Flag any business rule that is duplicated or scattered across multiple files — these are refactoring candidates.

---

## Phase 3: Developer Experience & Patterns

---

### 3.1 — `docs/PATTERNS_AND_CONVENTIONS.md`

Produce a document covering:

- **Architectural patterns:** Repository pattern, service layer, DTOs, CQRS, event sourcing — whatever is used, document it with real examples from the codebase.
- **Naming conventions:**
  - File naming (kebab-case, PascalCase, etc.)
  - Class/function naming
  - Database column naming (snake_case, camelCase)
  - API endpoint naming
  - Environment variable naming
- **Error handling strategy:**
  - Custom exception classes and hierarchy
  - How errors propagate (thrown → caught where?)
  - Error logging approach
  - User-facing vs internal error messages
- **Authentication & authorization patterns:** How auth is implemented, where guards/middleware live, how to protect a new endpoint.
- **Configuration management:** How `.env`, config files, and secrets are organized and loaded.
- **Dependency injection:** How DI is configured and used.
- **Logging & observability:** Logging library, log levels, structured logging format, tracing.
- **Code organization within a module:** Standard file structure for a new feature/module.

For every pattern, include a **real code snippet** from the codebase as the canonical example.

---

### 3.2 — `docs/GETTING_STARTED.md`

Produce a document covering:

- **Prerequisites:** Exact versions of Node.js, PHP, Python, Docker, etc. required.
- **Setup steps:** Numbered, copy-pasteable commands from clone to running app.
- **Environment variables:** List EVERY `.env` key with:
  - Description
  - Example value
  - Whether it's required or optional
  - Where to obtain it (e.g., "Get from AWS console", "Ask team lead")
- **Database setup:** How to create the DB, run migrations, seed data.
- **Running the app:** Dev server, watch mode, debug mode.
- **Running tests:** Unit, integration, e2e — separate commands for each.
- **Common tasks:** How to add a new migration, generate boilerplate, clear caches.
- **Troubleshooting:** Infer common issues from Dockerfile workarounds, README notes, setup scripts, or error handling. Include at least 5 "if you see X, do Y" entries.
- **IDE setup:** Recommended extensions, settings, debug configurations if they exist in `.vscode/` or equivalent.

---

### 3.3 — `docs/TESTING_GUIDE.md`

Produce a document covering:

- **Testing philosophy:** What's the testing strategy? (Testing trophy, testing pyramid, etc.)
- **Test types and locations:**
  - Unit tests: where they live, what they cover
  - Integration tests: where they live, what they cover
  - E2E tests: where they live, what they cover
- **How to write a new test:** Step-by-step guide following existing patterns, with a real example.
- **Test utilities:** Factories, fixtures, builders, custom matchers, test helpers — where they live and how to use them.
- **Mocking strategy:** How external services, databases, and time are mocked.
- **Test database:** How the test DB is managed (in-memory, Docker, transactions).
- **Coverage:** Current coverage metrics if available, which areas have good coverage vs gaps.
- **CI integration:** How tests run in CI, any flaky test handling.

---

## Phase 4: AI Agent Context Files

These are the highest-leverage documents. They directly determine how effective AI coding agents will be.

---

### 4.1 — `CLAUDE.md` (at project root, NOT in docs/)

This file is automatically read by Claude Code on every session. Keep it tight, opinionated, and actionable. Structure:

```markdown
# Project: [Actual Project Name]

## Quick Context
[2–3 sentences: what this project does, who it serves, core technology]

## Commands
- **Install:** `[exact command]`
- **Dev server:** `[exact command]`
- **Build:** `[exact command]`
- **Test (all):** `[exact command]`
- **Test (unit):** `[exact command]`
- **Test (single file):** `[exact command with placeholder]`
- **Lint:** `[exact command]`
- **Format:** `[exact command]`
- **Migrate:** `[exact command]`
- **Seed:** `[exact command]`

## Architecture in 30 Seconds
[Brief paragraph: monolith/microservices, main framework, how a request flows
through the system in one sentence, database, cache, queue]

## Key Directories
- `src/modules/` — Feature modules, each self-contained with controller/service/repo
- `src/common/` — Shared utilities, decorators, guards, pipes
- `src/config/` — Configuration files loaded at bootstrap
- `database/migrations/` — Chronological schema migrations
- `test/` — Integration and e2e tests
[Adjust to actual structure]

## Patterns You MUST Follow
1. **[Pattern name]:** [One-line description]. See `path/to/canonical/example.ts`.
2. **[Pattern name]:** [One-line description]. See `path/to/canonical/example.ts`.
3. **[Pattern name]:** [One-line description]. See `path/to/canonical/example.ts`.
[List 5–10 critical patterns]

## Patterns You Must AVOID
1. **Don't [anti-pattern]:** [Why and what to do instead]
2. **Don't [anti-pattern]:** [Why and what to do instead]
[List 3–5 common mistakes]

## Common Pitfalls
- [Non-obvious side effect or dependency]
- [Thing that looks right but breaks in production]
- [Gotcha specific to this project's setup]

## Domain Glossary
- **[Term]:** [Definition in this project's context]
- **[Term]:** [Definition in this project's context]
[10–20 most important terms]

## Before Making Changes
1. Read the relevant module's tests to understand expected behavior
2. Check if the entity has a state machine in `docs/BUSINESS_RULES.md`
3. Run `[lint command]` before committing
4. If touching DB schema, create a migration — never modify existing migrations
```

---

### 4.2 — `docs/CODEBASE_MAP.md`

A navigational index optimized for AI agents. Structure:

- **Module index:** For each feature/module:
  - Entry point file
  - Key files to read (ordered by importance)
  - Internal dependencies (other modules it imports from)
  - External dependencies (third-party services it calls)
- **Change impact map:** "If you need to change X, you must also update Y and Z"
  - Schema change → migration + model + DTOs + tests
  - New endpoint → route + controller + service + validation + tests + API docs
  - New module → module registration + DI config + integration test setup
- **Cross-cutting concerns:** Where do these live?
  - Authentication/Authorization
  - Logging
  - Caching
  - Validation
  - Error handling
  - Event dispatching
  - Rate limiting
- **File naming decoder:** How to find what you're looking for:
  - `*.controller.ts` → HTTP handlers
  - `*.service.ts` → Business logic
  - `*.repository.ts` → Data access
  - `*.dto.ts` → Request/response shapes
  - `*.entity.ts` → ORM models
  - `*.guard.ts` → Authorization checks
  - `*.spec.ts` → Tests
  [Adjust to actual naming]

---

### 4.3 — `docs/DECISION_LOG.md`

Document architectural decisions found in the codebase:

- **For each significant decision:**
  - **Decision:** What was decided
  - **Context:** Why this choice was made (infer from code comments, commit messages, README notes, or the implementation itself)
  - **Consequences:** What trade-offs this creates
  - **Status:** Active, deprecated, or superseded
- **Examples:** Framework choice, database choice, auth strategy, API versioning approach, monorepo vs polyrepo, testing strategy, deployment platform.

---

## Execution Instructions

Follow these rules strictly:

1. **Read before writing.** Explore the full project tree first. Read config files, entry points, route definitions, model/migration files, test files, and READMEs before generating any document. Spend at least 30% of your effort on reading.

2. **Be specific, not generic.** Reference actual file paths, actual class names, actual function signatures, actual environment variable names. If a document could apply to any project, it's too generic — rewrite it.

3. **Cite line numbers** when documenting business rules and complex logic. Use format: `src/modules/auth/auth.service.ts:42-67`.

4. **Flag gaps and issues.** If something is undocumented, inconsistent, or smells like tech debt, call it out:
   > ⚠️ **NOTE:** This business rule is duplicated in `order.service.ts:89` and `payment.service.ts:134` with slightly different logic. This should be consolidated.

5. **Generate documents one at a time.** After completing each document, pause and ask for confirmation before proceeding to the next. This allows for review and course correction.

6. **Keep each document self-contained** but cross-reference other docs with relative markdown links: `See [Data Models](./DATA_MODELS.md) for schema details.`

7. **Use Mermaid diagrams liberally** for architecture, data flows, state machines, and entity relationships. Prefer visual over textual when explaining structure.

8. **Validate your findings.** If you document that "all services extend BaseService," verify by checking at least 5 services. If you document an API endpoint, verify the route exists.

9. **Prioritize accuracy over completeness.** It's better to document 80% of the system accurately than 100% with guesses. Mark anything uncertain with `[VERIFY]`.

10. **Write for scanning.** Use tables, bullet points, and headers. Developers don't read docs linearly — they search and scan.

---

## Document Generation Order

Generate in this order (each builds on knowledge from the previous):

| # | Document | Depends On | Priority |
|---|----------|-----------|----------|
| 1 | `ARCHITECTURE.md` | — | 🔴 Critical |
| 2 | `TECH_STACK.md` | — | 🔴 Critical |
| 3 | `DATA_MODELS.md` | — | 🔴 Critical |
| 4 | `DOMAIN_MAP.md` | Architecture, Data Models | 🔴 Critical |
| 5 | `PATTERNS_AND_CONVENTIONS.md` | Architecture | 🟡 High |
| 6 | `API_REFERENCE.md` | Domain Map, Data Models | 🟡 High |
| 7 | `BUSINESS_RULES.md` | Domain Map, Data Models | 🟡 High |
| 8 | `GETTING_STARTED.md` | Tech Stack | 🟡 High |
| 9 | `CODEBASE_MAP.md` | All above | 🔴 Critical |
| 10 | `CLAUDE.md` (root) | All above | 🔴 Critical |
| 11 | `TESTING_GUIDE.md` | Patterns | 🟢 Medium |
| 12 | `DECISION_LOG.md` | All above | 🟢 Medium |

---

## Quality Checklist

Before considering a document complete, verify:

- [ ] Every file path referenced actually exists
- [ ] Every code snippet is from the actual codebase (not fabricated)
- [ ] Every business rule cites its source location
- [ ] Mermaid diagrams render correctly
- [ ] No placeholder text like `[TODO]` or `[FILL IN]` (use `[VERIFY]` only for genuinely uncertain items)
- [ ] Cross-references to other docs use correct relative paths
- [ ] The document is useful on day 1 for a new engineer — not after a week of context gathering
- [ ] An AI agent reading only `CLAUDE.md` + `CODEBASE_MAP.md` could make a correct PR for a simple feature
