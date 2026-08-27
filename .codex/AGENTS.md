# Agent Skills (Codex)

Append this file to your global `~/.codex/AGENTS.md` after running the install steps from the project README. It teaches the Codex agent about the installed skills and how to load them.

---

## Agent Skills

A library of engineering workflows is installed at `~/.codex/skills/`. Each skill lives in `~/.codex/skills/<skill-name>/SKILL.md` and encodes a specific process (TDD, code review, debugging, shipping, etc.).

### When to load a skill

When the user's task matches a skill's purpose, **read the skill file before responding** and follow it. Match the task to the skill by intent, not exact wording.

| If the task is… | Read |
|---|---|
| Refining a vague idea | `~/.codex/skills/idea-refine/SKILL.md` |
| Writing a spec / requirements | `~/.codex/skills/spec-driven-development/SKILL.md` |
| Breaking work into tasks | `~/.codex/skills/planning-and-task-breakdown/SKILL.md` |
| Implementing a feature | `~/.codex/skills/incremental-implementation/SKILL.md` |
| High-stakes / unfamiliar code | `~/.codex/skills/doubt-driven-development/SKILL.md` |
| Writing or running tests | `~/.codex/skills/tdd/SKILL.md` |
| Browser / DOM testing | `~/.codex/skills/browser-testing-with-devtools/SKILL.md` |
| Debugging or fixing a bug | `~/.codex/skills/debugging-and-error-recovery/SKILL.md` |
| Hard bug or perf regression | `~/.codex/skills/diagnosing-bugs/SKILL.md` |
| Reviewing code | `~/.codex/skills/code-review/SKILL.md` |
| Security review | `~/.codex/skills/security-and-hardening/SKILL.md` |
| Package release-age gate config | `~/.codex/skills/package-release-age-gates/SKILL.md` |
| Performance work | `~/.codex/skills/performance-optimization/SKILL.md` |
| API or interface design | `~/.codex/skills/api-and-interface-design/SKILL.md` |
| Building UI | `~/.codex/skills/frontend-ui-engineering/SKILL.md` |
| Simplifying code | `~/.codex/skills/code-simplification/SKILL.md` |
| Git / branching / commits | `~/.codex/skills/git-workflow-and-versioning/SKILL.md` |
| CI/CD setup | `~/.codex/skills/ci-cd-and-automation/SKILL.md` |
| Writing ADRs / docs | `~/.codex/skills/documentation-and-adrs/SKILL.md` |
| Deprecation / migration | `~/.codex/skills/deprecation-and-migration/SKILL.md` |
| Pre-launch checklist | `~/.codex/skills/shipping-and-launch/SKILL.md` |
| Documenting a codebase | `~/.codex/skills/analysing-codebase/SKILL.md` |
| Writing a PRD | `~/.codex/skills/write-a-prd/SKILL.md` |
| PRD → issues | `~/.codex/skills/prd-to-issues/SKILL.md` |
| Triaging issues | `~/.codex/skills/triage/SKILL.md` |

### Rules

1. **Check before answering.** If a skill applies, read it before drafting your response.
2. **Process skills first.** When several apply, run the process skill (debugging, TDD, brainstorming) before any implementation skill.
3. **Follow exactly.** Skills are workflows, not suggestions. Don't skip verification steps.
4. **Surface assumptions.** Before non-trivial work, list the assumptions you're making and ask for correction.
5. **Verify, don't assume.** A task is complete only when verification (passing tests, build output, runtime data) confirms it.

### Slash commands

The following prompts (in `~/.codex/prompts/`) wire common workflows to slash commands:

- `/spec` — start a spec
- `/plan` — break work into tasks
- `/build` — implement next task with TDD
- `/test` — TDD workflow / Prove-It pattern
- `/review` — five-axis code review
- `/code-review` — multi-axis review with prioritized output
- `/code-simplify` — reduce complexity, preserve behavior
- `/security-age-gate` — add package release-age gate config
- `/ship` — pre-launch checklist
- `/pr-open` — branch, commit staged, push, PR
- `/interview` — interview-driven spec generation
