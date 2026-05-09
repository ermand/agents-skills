---
name: analysing-codebase
description: Analyzes an existing codebase and generates structured documentation for onboarding engineers and AI agents. Use when asked to document a codebase, onboard to a new project, create CLAUDE.md or AGENTS.md, or generate architecture, API, or domain documentation.
---

# Analysing Codebase

## Overview

This skill establishes standard practices and workflows for Analysing Codebase.

## When to Use

Use when asked to document a codebase, onboard to a new project, create CLAUDE.md, or generate architecture documentation.

You are a principal engineer. Analyze this codebase and generate the following documents in `./docs/`. Read the full project structure, configs, routes, models, and migrations before writing anything. Be specific — reference actual file paths, class names, and line numbers. No placeholders, no generic content.

Generate documents in this order, pausing after each for confirmation.

---

## 1. `CLAUDE.md` (project root — not in docs/)

The most important file. Keep it under 150 lines. Structure exactly as:

```
# Project: [Name]

## Quick Context
[2–3 sentences: what it does, who it serves, core tech]

## Commands
- Install: `...`
- Dev: `...`
- Build: `...`
- Test: `...`
- Lint: `...`
- Migrate: `...`

## Architecture in 30 Seconds
[One paragraph: service type, framework, request flow, DB, cache, queues]

## Key Directories
[8–12 lines mapping dirs to responsibilities]

## Patterns You MUST Follow
[5–10 numbered rules with file references to canonical examples]

## Patterns You Must AVOID
[3–5 anti-patterns with reasons]

## Common Pitfalls
[5+ non-obvious gotchas specific to this project]

## Domain Glossary
[10–20 terms with definitions as used in THIS codebase]
```

---

## 2. `docs/ARCHITECTURE.md`

- System overview (2–3 sentences)
- Mermaid diagram: system context (C4 Level 1)
- Mermaid diagram: request lifecycle sequence for the most common user action
- Service boundaries and communication patterns
- Infrastructure dependencies (DBs, caches, queues, external APIs)
- Async processing: background jobs, crons, scheduled tasks
- Deployment topology

---

## 3. `docs/DATA_MODELS.md`

- Every table/collection: columns, types, constraints, relationships
- Source: read from migrations or ORM models (state which)
- Mermaid ER diagram
- Flag: soft deletes, JSON columns (document their shape), enums (list values), polymorphic relations
- DB-level vs app-level integrity rules
- Key indexes and their purpose

---

## 4. `docs/DOMAIN_MAP.md`

- Bounded contexts / domain areas with directory ownership
- For each domain: purpose, key entities, business rules, events
- Mermaid dependency graph between domains
- Ubiquitous language glossary table: Term | Definition | Location

---

## 5. `docs/API_REFERENCE.md`

- Every endpoint: method, path, auth, request/response shapes
- Grouped by domain
- Pagination, error conventions, rate limits
- Read from route files, controllers, OpenAPI specs

---

## 6. `docs/BUSINESS_RULES.md`

- Every non-trivial rule: what, where (file:line), when triggered, edge cases
- Mermaid state diagrams for any entity with a lifecycle
- Permission/authorization model
- Flag scattered or duplicated rules with ⚠️ warnings

---

## 7. `docs/PATTERNS_AND_CONVENTIONS.md`

- Architectural patterns with real code snippets as canonical examples
- Naming conventions (files, classes, DB columns, endpoints, env vars)
- Error handling strategy and exception hierarchy
- Auth patterns, DI approach, config management
- Standard file structure for adding a new module/feature

---

## 8. `docs/GETTING_STARTED.md`

- Prerequisites with exact versions
- Clone-to-running-app steps (numbered, copy-pasteable)
- Every .env key: description, example value, required/optional, where to get it
- DB setup, migrations, seeding
- Running tests (unit, integration, e2e)
- 5+ troubleshooting entries: "if you see X, do Y"

---

## 9. `docs/CODEBASE_MAP.md`

Navigation index for AI agents:
- Module index: entry point, key files, internal/external dependencies
- Change impact map: "if you change X, also update Y and Z"
- Cross-cutting concerns: where auth, logging, caching, validation, errors live
- File naming decoder: what each suffix/pattern means

---

## Agent Context Files

After generating `CLAUDE.md`, also create agent-specific variants so every tool picks up the project context automatically:

| Tool | File | Notes |
|------|------|-------|
| Claude Code / OpenCode | `CLAUDE.md` | Already done above |
| Codex | `AGENTS.md` | Same content as CLAUDE.md |
| Cursor | `.cursor/rules/<project-name>.mdc` | Add frontmatter: `description: Project rules` and `alwaysApply: true` |
| Copilot / VS Code | `.github/copilot-instructions.md` | Same content as CLAUDE.md |

`CLAUDE.md` is the source of truth. Copy its content into each variant — do not abbreviate.

---

## Rules

1. **Read 30%, write 70%.** Explore thoroughly before generating.
2. **Cite sources.** Business rules get `file:line` references. Patterns get canonical example paths.
3. **Flag issues.** Use `> ⚠️ NOTE:` for tech debt, inconsistencies, duplication.
4. **Mark uncertainty.** Use `[VERIFY]` for anything you can't confirm — never guess.
5. **Validate.** If you claim a pattern is universal, check at least 5 instances.
6. **Cross-reference.** Link between docs with relative paths.
7. **Use Mermaid** for architecture, ER diagrams, state machines, and domain dependencies.


## Common Rationalizations

Agents often attempt to rationalize skipping strict processes under pressure. Watch out for:
- "This task is too small or simple to need the full process."
- "I can just quickly do it without the checklist."
- "I already know how this works, so I don't need to verify."
**Reality:** These rationalizations lead to regressions, broken code, and context loss. Follow the process regardless of perceived simplicity.

## Red Flags

**STOP and restart the process if you see any of these:**
- Skipping mandatory steps in the checklist.
- Failing to verify outputs before asserting success.
- Proceeding without user approval when required.
- Writing code before planning or testing (if dictated by the skill).