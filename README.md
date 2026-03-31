# @ermand/agent-skills

Skills for AI coding agents that analyze codebases and generate documentation for engineers and agents alike.

## Install

```bash
# Both skills
npx skills@latest add ermand/agents-skills

# Compact only (default)
npx skills@latest add ermand/agents-skills --skill analysing-codebase

# Full version only
npx skills@latest add ermand/agents-skills --skill analysing-codebase-full
```

Once published to npm:

```bash
npx skills@latest add @ermand/agent-skills
```

## Skills

| Skill | When to use | Docs generated |
|-------|-------------|----------------|
| `analysing-codebase` | Quick analysis of any codebase — generates the 9 highest-value docs | 9 |
| `analysing-codebase-full` | Deep 4-phase analysis for large or complex codebases | 12 |

## What gets generated

**Agent context files** (auto-read by each tool):

| Tool | File |
|------|------|
| Claude Code / OpenCode | `CLAUDE.md` |
| Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/<project-name>.mdc` |
| Copilot / VS Code | `.github/copilot-instructions.md` |

**Documentation** (in `./docs/`):

- `ARCHITECTURE.md` — system overview, C4 diagrams, request lifecycle, infrastructure
- `DATA_MODELS.md` — full schema, ER diagram, relationships, indexes
- `DOMAIN_MAP.md` — bounded contexts, ubiquitous language glossary
- `API_REFERENCE.md` — every endpoint, grouped by domain
- `BUSINESS_RULES.md` — rules with file:line citations, state machines
- `PATTERNS_AND_CONVENTIONS.md` — architectural patterns with real code examples
- `GETTING_STARTED.md` — clone-to-running-app guide, every .env key
- `CODEBASE_MAP.md` — navigation index and change impact map for AI agents
- `TECH_STACK.md` *(full only)* — languages, frameworks, CI/CD, tooling
- `TESTING_GUIDE.md` *(full only)* — test strategy, factories, mocking, coverage
- `DECISION_LOG.md` *(full only)* — architectural decisions and trade-offs

## License

MIT © [Ermand Durro](https://github.com/ermand)
