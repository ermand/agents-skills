---
name: analysing-codebase-full
description: Comprehensive 4-phase codebase analysis generating 12 documentation files including architecture, data models, business rules, API reference, and AI agent context files. Use when thorough onboarding documentation is needed, when the compact version lacks sufficient detail, or for large/complex codebases.
---

# Analysing Codebase (Full)

## Overview

This skill establishes standard practices and workflows for Analysing Codebase Full.

## When to Use

Use when thorough onboarding documentation is needed for large or complex codebases, or when the compact analysis lacks sufficient detail.

A 4-phase, 12-document deep analysis of a codebase. Produces documentation for both new engineers and AI coding agents.

For complete per-document instructions, see [full-prompt.md](full-prompt.md).

---

## Document Generation Order

| # | Document | Phase | Priority |
|---|----------|-------|----------|
| 1 | `docs/ARCHITECTURE.md` | Discovery | Critical |
| 2 | `docs/TECH_STACK.md` | Discovery | Critical |
| 3 | `docs/DATA_MODELS.md` | Discovery | Critical |
| 4 | `docs/DOMAIN_MAP.md` | Domain | Critical |
| 5 | `docs/PATTERNS_AND_CONVENTIONS.md` | Domain | High |
| 6 | `docs/API_REFERENCE.md` | Domain | High |
| 7 | `docs/BUSINESS_RULES.md` | Domain | High |
| 8 | `docs/GETTING_STARTED.md` | DX | High |
| 9 | `docs/CODEBASE_MAP.md` | AI Context | Critical |
| 10 | `CLAUDE.md` (root) | AI Context | Critical |
| 11 | `docs/TESTING_GUIDE.md` | DX | Medium |
| 12 | `docs/DECISION_LOG.md` | AI Context | Medium |

Generate in order. Pause after each document for confirmation before proceeding.

---

## Agent Context Files

After generating `CLAUDE.md` (doc #10), also create agent-specific variants so every tool picks up the project context automatically:

| Tool | File | Notes |
|------|------|-------|
| Claude Code / OpenCode | `CLAUDE.md` | Already done above |
| Codex | `AGENTS.md` | Same content as CLAUDE.md |
| Cursor | `.cursor/rules/<project-name>.mdc` | Add frontmatter: `description: Project rules` and `alwaysApply: true` |
| Copilot / VS Code | `.github/copilot-instructions.md` | Same content as CLAUDE.md |

`CLAUDE.md` is the source of truth. Copy its content into each variant — do not abbreviate.

---

## Core Rules

1. **Read before writing.** Spend at least 30% of effort exploring before generating anything.
2. **Be specific.** Reference actual file paths, class names, function signatures, env var names.
3. **Cite line numbers.** Business rules: `src/modules/auth/auth.service.ts:42-67`.
4. **Flag gaps.** Use `> ⚠️ NOTE:` for tech debt, inconsistencies, duplicated logic.
5. **Mark uncertainty.** Use `[VERIFY]` — never guess.
6. **Validate claims.** If you say a pattern is universal, check at least 5 instances.
7. **Use Mermaid** for architecture, ER diagrams, state machines, domain dependencies.
8. **Cross-reference** with relative markdown links between docs.
9. **Write for scanning** — tables, bullets, headers over prose.
10. **Prioritize accuracy over completeness.** 80% accurate beats 100% with guesses.

---

## Quality Checklist

Before marking any document complete:

- [ ] Every file path referenced actually exists
- [ ] Every code snippet is from the actual codebase (not fabricated)
- [ ] Every business rule cites its source location
- [ ] Mermaid diagrams render correctly
- [ ] No placeholder text (use `[VERIFY]` only for genuinely uncertain items)
- [ ] Cross-references use correct relative paths
- [ ] An AI agent reading only `CLAUDE.md` + `CODEBASE_MAP.md` could make a correct PR for a simple feature


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