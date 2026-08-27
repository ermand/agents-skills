# Agent skills synchronization design

## Goal

Keep the local skill library current with Addy Osmani's `agent-skills` repository without deleting local or Matt Pocock skills. Reduce ambiguous automatic invocation by choosing one default for overlapping workflows.

## Baseline

- Addy source: `https://github.com/addyosmani/agent-skills`
- Pinned upstream revision: `7cb7a20bb38b199728d456999c725a0488490ab6`
- Local skill directories: 60
- Addy skill directories: 24
- Matching Addy/local directories: 22
- Addy-only directories excluded from this change: `interview-me`, `observability-and-instrumentation`
- Local-only directories preserved: 38
- Matching trees with content changes: 19
- Matching trees already equal: 3

The worktree has unrelated changes. None overlap the 22 matching Addy skill trees. Those changes must remain untouched.

## Scope

Synchronize every file below the 22 matching directories:

- `api-and-interface-design`
- `browser-testing-with-devtools`
- `ci-cd-and-automation`
- `code-review-and-quality`
- `code-simplification`
- `context-engineering`
- `debugging-and-error-recovery`
- `deprecation-and-migration`
- `documentation-and-adrs`
- `doubt-driven-development`
- `frontend-ui-engineering`
- `git-workflow-and-versioning`
- `idea-refine`
- `incremental-implementation`
- `performance-optimization`
- `planning-and-task-breakdown`
- `security-and-hardening`
- `shipping-and-launch`
- `source-driven-development`
- `spec-driven-development`
- `test-driven-development`
- `using-agent-skills`

Do not change commands, README files, hooks, references, package metadata, or local-only skill directories except for the routing metadata explicitly listed below.

## Canonical routing

Matt Pocock's workflows are the defaults for overlapping local installations:

| Intent | Default skill | Alternative |
|---|---|---|
| Code review | `code-review` | `code-review-and-quality`, explicit-only |
| Test-driven development | `tdd` | `test-driven-development`, explicit-only |
| Ordinary failures | `debugging-and-error-recovery` | None |
| Hard bugs and performance regressions | `diagnosing-bugs` | `diagnose`, explicit-only |

These pairs remain complementary rather than collapsed:

- `idea-refine` and `brainstorming` cover different ideation stages.
- `grill-me` and `grilling` are the explicit entrypoint and model-invoked workflow.
- `codebase-design` and `improve-codebase-architecture` operate at different architectural levels.
- `writing-skills` and `writing-great-skills` are the workflow and its reference.

## Invocation and routing changes

After syncing upstream content:

1. Add `disable-model-invocation: true` to `skills/code-review-and-quality/SKILL.md`.
2. Add `disable-model-invocation: true` to `skills/test-driven-development/SKILL.md`.
3. Add `disable-model-invocation: true` to `skills/diagnose/SKILL.md`.
4. Change the relevant `.codex/AGENTS.md` routing rows to use `code-review`, `tdd`, and `diagnosing-bugs`.

These metadata changes are intentional local policy, not upstream synchronization failures.

## Data flow

1. Fetch and pin the Addy upstream revision.
2. Enumerate the upstream and local skill path sets.
3. Replace files only inside the 22 matching skill directories.
4. Apply the three local invocation metadata overrides.
5. Update only the three corresponding Codex routing rows.
6. Review the path-scoped diff.

## Invariants

- No local-only skill directory is removed or renamed.
- No Addy-only skill is added.
- No unrelated user worktree change is reverted.
- No non-skill file changes occur except the planned `.codex/AGENTS.md` routing rows.
- The only intentional deviations from upstream content are the three invocation metadata fields.

## Verification

- Byte-compare synchronized files with the pinned upstream tree, excluding the three documented metadata overrides.
- Confirm all 38 local-only skill directories remain present.
- Confirm no Addy-only directory was added.
- Confirm the final diff path set contains only the 22 matching skill trees and the planned routing metadata.
- Run available package checks. The repository package has no test, build, or lint scripts, so tree comparison and metadata validation are the primary checks.

## Risks

- Upstream descriptions may still overlap with local skills beyond the identified direct duplicates. Keep the first synchronization narrow and review trigger behavior separately.
- Hosts differ in how they discover frontmatter. The Codex routing update is explicit; other hosts may still index model-invoked descriptions according to their own loaders.
- The upstream revision can advance after this design is written. Implementation must stop if it does not use the pinned revision.
