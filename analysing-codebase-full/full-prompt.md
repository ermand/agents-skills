# Codebase Analysis & Documentation — Full Reference

> Complete per-document instructions for all 12 documents. Read alongside `SKILL.md`.

---

## Phase 1: Discovery & Architecture Analysis

Thoroughly explore the project structure before writing anything. Read config files, entry points, route definitions, model files, migration files, Dockerfiles, CI configs, and READMEs.

---

### 1.1 — `docs/ARCHITECTURE.md`

- **System overview:** What this project does in 2–3 sentences.
- **High-level architecture:** ASCII or Mermaid diagrams showing major components and how they connect.
- **Service boundaries:** Monolith, modular monolith, or microservices. How services/modules communicate (REST, gRPC, message queues, events, direct imports).
- **Request lifecycle:** Trace a typical user request end-to-end — HTTP entry point through middleware, controllers, services, repositories, database, and back.
- **Infrastructure dependencies:** Every external dependency — databases, caches, message brokers, search engines, external APIs, CDNs, object storage.
- **Deployment topology:** Docker Compose, Kubernetes, serverless, VPS, PaaS. Note staging/production differences.
- **Async processing:** Background jobs, queues, cron jobs, scheduled tasks.

**Mermaid diagram requirements:**
- A system context diagram (C4 Level 1)
- A container diagram (C4 Level 2) if multiple services exist
- A request flow sequence diagram for the most common user action

---

### 1.2 — `docs/TECH_STACK.md`

- **Languages & versions:** Read from `package.json`, `composer.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `.tool-versions`, `Dockerfile`, or equivalent.
- **Frameworks:** Primary framework and version (e.g., NestJS 10.x, Laravel 11.x, FastAPI 0.100+).
- **Key libraries & rationale:** List significant dependencies and infer WHY they were chosen based on usage patterns.
- **Database & ORM:** Which database engine, which ORM/query builder, migration tool.
- **Build & dev tools:** Bundlers (Webpack, Vite, esbuild), task runners, monorepo tools (Turborepo, Nx, Lerna).
- **Testing stack:** Test runner, assertion library, mocking tools, e2e framework.
- **CI/CD pipeline:** Read from `.github/workflows/`, `Jenkinsfile`, `.gitlab-ci.yml`, `bitbucket-pipelines.yml`, or equivalent. Document every pipeline stage.
- **Code quality tools:** Linters (ESLint, PHPStan, Ruff), formatters (Prettier, Black), pre-commit hooks.
- **Notable dev dependencies:** Code generators, seed scripts, CLI tools.

---

### 1.3 — `docs/DATA_MODELS.md`

- **Complete schema inventory:** Every table/collection with all columns/fields, types, defaults, constraints.
- **Source of truth:** Read from migration files, ORM model definitions, or raw SQL schemas — state which source you used.
- **Relationships:** For every foreign key or reference, document the relationship type (1:1, 1:N, M:N) and the related entity.
- **Entity-relationship diagram:** Mermaid ER diagram covering all entities.
- **Special patterns:**
  - Soft deletes (`deleted_at`, `is_active`)
  - Polymorphic relations
  - JSON/JSONB columns (document their expected shape)
  - Enums (list all possible values)
  - Audit columns (`created_at`, `updated_at`, `created_by`)
  - Multi-tenancy patterns (tenant_id, organization scoping)
- **Data integrity:** Which rules are enforced at DB level (constraints, triggers) vs. application level (validation, middleware).
- **Indexes:** All non-primary indexes and their purpose.

---

## Phase 2: Domain & Business Logic Mapping

---

### 2.1 — `docs/DOMAIN_MAP.md`

- **Bounded contexts:** All distinct domain areas in the codebase.
- **For each domain/module:**
  - Purpose and responsibility (1–2 sentences)
  - Key entities and value objects
  - Business rules and invariants
  - Events produced or consumed
  - External integrations
- **Directory ownership:** Map which directories/modules own which domain.
- **Domain dependency graph:** Mermaid diagram showing which domains depend on which others.
- **Ubiquitous language glossary:**

```markdown
| Term | Definition | Used In |
|------|-----------|---------|
| Coefficient | The odds multiplier applied to a bet | `src/modules/betting/` |
```

---

### 2.2 — `docs/API_REFERENCE.md`

- **Every endpoint:** Method, path, description, authentication requirement.
- **Request shape:** Headers, query params, path params, body schema (with types and required/optional).
- **Response shape:** Success response structure, error response structure, status codes.
- **Grouping:** Organize by domain area, not by controller file.
- **Authentication & authorization:** Which endpoints need auth? What roles/permissions are required?
- **Pagination patterns:** Cursor, offset, or page-based.
- **Error conventions:** Standard error response shape, error codes, validation error format.
- **Rate limits:** Document per-endpoint or globally if any rate limiting exists.
- **Websocket/SSE endpoints:** Event types and payload shapes if real-time endpoints exist.

Source: Read from route files, controller decorators/annotations, middleware, OpenAPI/Swagger specs if they exist.

---

### 2.3 — `docs/BUSINESS_RULES.md`

- **Rule inventory:** Every non-trivial business rule from the codebase.
- **For each rule:**
  - **What:** Plain English description
  - **Where:** File path(s) and line number(s) where it's enforced
  - **When:** What triggers this rule (user action, cron, event, state change)
  - **Edge cases:** How edge cases are handled
  - **Dependencies:** Other rules or state this rule depends on
- **Validation logic:** All input validation rules, grouped by entity/endpoint.
- **State machines:** Mermaid state diagram for any entity with a lifecycle (e.g., order: pending → confirmed → shipped → delivered).
- **Permission & authorization rules:** Full RBAC/ABAC model.
- **Scattered rules warning:** Flag any business rule duplicated or scattered across multiple files with `> ⚠️ NOTE:`.

---

## Phase 3: Developer Experience & Patterns

---

### 3.1 — `docs/PATTERNS_AND_CONVENTIONS.md`

- **Architectural patterns:** Repository pattern, service layer, DTOs, CQRS, event sourcing — document with real examples from the codebase.
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
- **Troubleshooting:** At least 5 "if you see X, do Y" entries. Infer from Dockerfile workarounds, README notes, setup scripts, error handling.
- **IDE setup:** Recommended extensions, settings, debug configurations if they exist.

---

### 3.3 — `docs/TESTING_GUIDE.md`

- **Testing philosophy:** Testing trophy, testing pyramid, or other strategy.
- **Test types and locations:**
  - Unit tests: where they live, what they cover
  - Integration tests: where they live, what they cover
  - E2E tests: where they live, what they cover
- **How to write a new test:** Step-by-step guide following existing patterns, with a real example.
- **Test utilities:** Factories, fixtures, builders, custom matchers, test helpers — where they live and how to use them.
- **Mocking strategy:** How external services, databases, and time are mocked.
- **Test database:** How the test DB is managed (in-memory, Docker, transactions).
- **Coverage:** Current coverage metrics if available, areas with good coverage vs gaps.
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
[List 5–10 critical patterns]

## Patterns You Must AVOID
1. **Don't [anti-pattern]:** [Why and what to do instead]
[List 3–5 common mistakes]

## Common Pitfalls
- [Non-obvious side effect or dependency]
- [Thing that looks right but breaks in production]
- [Gotcha specific to this project's setup]

## Domain Glossary
- **[Term]:** [Definition in this project's context]
[10–20 most important terms]

## Before Making Changes
1. Read the relevant module's tests to understand expected behavior
2. Check if the entity has a state machine in `docs/BUSINESS_RULES.md`
3. Run `[lint command]` before committing
4. If touching DB schema, create a migration — never modify existing migrations
```

### 4.1a — Agent-Specific Context File Variants

After generating `CLAUDE.md`, create variants for every tool so each picks up project context automatically:

| Tool | File | Notes |
|------|------|-------|
| Claude Code / OpenCode | `CLAUDE.md` | Already done above |
| Codex | `AGENTS.md` | Same content as CLAUDE.md |
| Cursor | `.cursor/rules/<project-name>.mdc` | Add frontmatter: `description: Project rules` and `alwaysApply: true` |
| Copilot / VS Code | `.github/copilot-instructions.md` | Same content as CLAUDE.md |

`CLAUDE.md` is the source of truth. Copy its content into each variant — do not abbreviate.

---

### 4.2 — `docs/CODEBASE_MAP.md`

A navigational index optimized for AI agents:

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

## Execution Rules

1. **Read before writing.** Explore the full project tree first. Spend at least 30% of effort on reading.
2. **Be specific, not generic.** Reference actual file paths, class names, function signatures, env var names. If a document could apply to any project, it's too generic — rewrite it.
3. **Cite line numbers** when documenting business rules and complex logic: `src/modules/auth/auth.service.ts:42-67`.
4. **Flag gaps and issues.** Use `> ⚠️ NOTE:` for undocumented, inconsistent, or tech-debt items.
5. **Generate documents one at a time.** Pause after each for confirmation before proceeding.
6. **Keep each document self-contained** but cross-reference with relative markdown links.
7. **Use Mermaid diagrams liberally** for architecture, data flows, state machines, entity relationships.
8. **Validate your findings.** If you document that "all services extend BaseService," check at least 5 services.
9. **Prioritize accuracy over completeness.** Mark anything uncertain with `[VERIFY]`.
10. **Write for scanning.** Use tables, bullet points, and headers.
