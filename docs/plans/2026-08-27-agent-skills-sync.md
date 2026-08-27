# Agent skills synchronization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Synchronize the 22 local skills shared with Addy Osmani's repository and make Matt Pocock's overlapping workflows the automatic defaults without removing any skill files.

**Architecture:** Treat Addy's pinned tree as the source for the 22 matching skill directories. Preserve every local-only directory and unrelated worktree change. Apply a small local invocation policy after synchronization, then update the Codex routing table to select the Matt workflows.

**Tech Stack:** Git, Markdown frontmatter, Codex `AGENTS.md`, Node.js one-off verification script.

---

## Constraints

- Upstream commit: `7cb7a20bb38b199728d456999c725a0488490ab6`.
- Do not add `interview-me` or `observability-and-instrumentation`.
- Do not modify commands, README files, hooks, references, package metadata, or local-only skill directories.
- Existing uncommitted changes are user work. Do not stage or revert them.
- The current `.codex/AGENTS.md` has unrelated uncommitted additions. Stage only the routing hunk from that file.
- Apply `disable-model-invocation: true` only to the three documented alternatives.

## Task 1: Reconfirm the pinned source and clean target boundary

**Files:**

- Read: `skills/` tree
- Read: `.codex/AGENTS.md`

**Step 1: Refresh the upstream ref**

Run:

```bash
git fetch --quiet upstream main
```

**Step 2: Confirm the revision is unchanged**

Run:

```bash
git rev-parse upstream/main
```

Expected: `7cb7a20bb38b199728d456999c725a0488490ab6`.

If the result differs, stop and do not broaden the synchronization source.

**Step 3: Confirm no target has new user edits**

Run:

```bash
git status --short -- skills/api-and-interface-design skills/browser-testing-with-devtools skills/ci-cd-and-automation skills/code-review-and-quality skills/code-simplification skills/context-engineering skills/debugging-and-error-recovery skills/deprecation-and-migration skills/documentation-and-adrs skills/doubt-driven-development skills/frontend-ui-engineering skills/git-workflow-and-versioning skills/idea-refine skills/incremental-implementation skills/performance-optimization skills/planning-and-task-breakdown skills/security-and-hardening skills/shipping-and-launch skills/source-driven-development skills/spec-driven-development skills/test-driven-development skills/using-agent-skills
```

Expected: no output. If any target is modified or untracked, stop and preserve that work for manual merging.

## Task 2: Synchronize the matching Addy skill trees

**Files:**

- Modify: the 22 target directories listed in Task 1
- Do not modify: all other paths

**Step 1: Restore the pinned upstream files into the worktree**

Run:

```bash
git restore --source=7cb7a20bb38b199728d456999c725a0488490ab6 --worktree -- \
  skills/api-and-interface-design \
  skills/browser-testing-with-devtools \
  skills/ci-cd-and-automation \
  skills/code-review-and-quality \
  skills/code-simplification \
  skills/context-engineering \
  skills/debugging-and-error-recovery \
  skills/deprecation-and-migration \
  skills/documentation-and-adrs \
  skills/doubt-driven-development \
  skills/frontend-ui-engineering \
  skills/git-workflow-and-versioning \
  skills/idea-refine \
  skills/incremental-implementation \
  skills/performance-optimization \
  skills/planning-and-task-breakdown \
  skills/security-and-hardening \
  skills/shipping-and-launch \
  skills/source-driven-development \
  skills/spec-driven-development \
  skills/test-driven-development \
  skills/using-agent-skills
```

The source and local matching trees currently have identical path sets. If Git reports a path-set problem, stop instead of deleting files or adding new upstream skills implicitly.

**Step 2: Inspect the content diff**

Run:

```bash
git diff --stat -- skills/api-and-interface-design skills/browser-testing-with-devtools skills/ci-cd-and-automation skills/code-review-and-quality skills/code-simplification skills/context-engineering skills/debugging-and-error-recovery skills/deprecation-and-migration skills/documentation-and-adrs skills/doubt-driven-development skills/frontend-ui-engineering skills/git-workflow-and-versioning skills/idea-refine skills/incremental-implementation skills/performance-optimization skills/planning-and-task-breakdown skills/security-and-hardening skills/shipping-and-launch skills/source-driven-development skills/spec-driven-development skills/test-driven-development skills/using-agent-skills
```

Expected: changes only in the 19 previously divergent matching trees. No local-only path may appear.

**Step 3: Commit only synchronized skill files**

Run:

```bash
git add skills/api-and-interface-design skills/browser-testing-with-devtools skills/ci-cd-and-automation skills/code-review-and-quality skills/code-simplification skills/context-engineering skills/debugging-and-error-recovery skills/deprecation-and-migration skills/documentation-and-adrs skills/doubt-driven-development skills/frontend-ui-engineering skills/git-workflow-and-versioning skills/idea-refine skills/incremental-implementation skills/performance-optimization skills/planning-and-task-breakdown skills/security-and-hardening skills/shipping-and-launch skills/source-driven-development skills/spec-driven-development skills/test-driven-development skills/using-agent-skills
git diff --cached --check
git diff --cached --name-only
git commit -m "chore: sync matching upstream agent skills"
```

Expected staged paths: only files below the 22 matching skill directories.

## Task 3: Apply the local invocation policy

**Files:**

- Modify: `skills/code-review-and-quality/SKILL.md`
- Modify: `skills/test-driven-development/SKILL.md`
- Modify: `skills/diagnose/SKILL.md`

**Step 1: Add explicit-only metadata**

Insert `disable-model-invocation: true` in each YAML frontmatter block immediately after its `description` line. Do not alter the synchronized skill bodies or any other frontmatter.

**Step 2: Verify the three metadata changes**

Run:

```bash
git diff -- skills/code-review-and-quality/SKILL.md skills/test-driven-development/SKILL.md skills/diagnose/SKILL.md
git diff --check
```

Expected: one added frontmatter field in each file and no other change.

**Step 3: Commit the invocation policy**

Run:

```bash
git add skills/code-review-and-quality/SKILL.md skills/test-driven-development/SKILL.md skills/diagnose/SKILL.md
git diff --cached --check
git commit -m "chore: make Matt skills canonical defaults"
```

## Task 4: Update Codex routing without staging user edits

**Files:**

- Modify: `.codex/AGENTS.md`

**Step 1: Change only the three workflow rows**

Use the existing routing table and make these replacements:

```text
Writing or running tests  -> ~/.codex/skills/tdd/SKILL.md
Hard bug or perf regression -> ~/.codex/skills/diagnosing-bugs/SKILL.md
Reviewing code -> ~/.codex/skills/code-review/SKILL.md
```

Keep all other rows and the user's existing `unslop` additions unchanged.

**Step 2: Verify the worktree diff**

Run:

```bash
git diff -- .codex/AGENTS.md
git diff --check
```

Expected: the three routing replacements plus the two pre-existing user additions. No other changes.

**Step 3: Stage only the routing hunk**

Run interactive staging:

```bash
git add -p .codex/AGENTS.md
```

Accept the hunk containing the three routing replacements. Reject the hunk containing the pre-existing `unslop` additions.

Confirm the staged patch before committing:

```bash
git diff --cached -- .codex/AGENTS.md
```

Expected: only the three routing replacements.

**Step 4: Commit the routing update**

Run:

```bash
git commit -m "chore: route Codex to canonical skills"
```

## Task 5: Run structural verification

**Files:**

- Read: pinned upstream tree and local `skills/` tree
- Read: `.codex/AGENTS.md`

**Step 1: Check committed diffs**

Run:

```bash
git diff --check HEAD~3..HEAD
git show --stat --oneline HEAD~2..HEAD
```

Expected: no whitespace errors; the two implementation commits contain only the planned skill and routing paths. The design and plan commits may also be present in the recent history.

**Step 2: Compare synchronized files to the pinned source**

Run a Node.js verification script that:

1. Enumerates files under the 22 target directories from the pinned tree.
2. Reads each corresponding local file.
3. Compares bytes with `git show 7cb7a20bb38b199728d456999c725a0488490ab6:<path>`.
4. Excludes only `skills/code-review-and-quality/SKILL.md` and `skills/test-driven-development/SKILL.md` from byte equality because their local invocation field is intentional.
5. Confirms the two excluded files contain exactly one `disable-model-invocation: true` field.
6. Confirms `skills/diagnose/SKILL.md` contains exactly one `disable-model-invocation: true` field.
7. Reports zero mismatches outside the two documented upstream overrides.

Expected output: `synchronized files: ok; invocation policy: ok`.

**Step 3: Confirm local-only skills remain present**

Run:

```bash
for skill in analysing-codebase analysing-codebase-full brainstorming codebase-design diagnose diagnosing-bugs dispatching-parallel-agents domain-modeling executing-plans find-skills finishing-a-development-branch grill-me grill-with-docs grilling handoff improve-codebase-architecture package-release-age-gates prd-to-issues prototype receiving-code-review requesting-code-review setup-matt-pocock-skills subagent-driven-development systematic-debugging tdd teach to-issues to-prd triage unslop using-git-worktrees using-superpowers verification-before-completion write-a-prd writing-great-skills writing-plans writing-skills; do
  test -d "skills/$skill" || { echo "missing local skill: $skill"; exit 1; }
done
echo "local-only skills: present"
```

Expected output: `local-only skills: present`.

**Step 4: Confirm upstream-only skills were not added**

Run:

```bash
test ! -d skills/interview-me && test ! -d skills/observability-and-instrumentation && echo "upstream-only skills: excluded"
```

Expected output: `upstream-only skills: excluded`.

**Step 5: Confirm user changes remain unstaged**

Run:

```bash
git status --short
```

Expected: the pre-existing user changes remain, plus no unexpected files from synchronization. Do not stage or revert them.

Use `@verification-before-completion` for the final evidence review and `@git-workflow-and-versioning` for any staging or commit ambiguity.
## Review-driven follow-up tasks

### Task 6: Restore the required shared reference

**Files:**

- Create: `references/definition-of-done.md`

Copy only `references/definition-of-done.md` from upstream commit `7cb7a20bb38b199728d456999c725a0488490ab6`. Do not update the existing shared references. Verify the new file matches the pinned upstream blob, then commit:

```bash
git add references/definition-of-done.md
git diff --cached --check
git commit -m "docs: add shared definition of done"
```

### Task 7: Remove unavailable router entries

**Files:**

- Modify: `skills/using-agent-skills/SKILL.md`

Remove only the three references to `observability-and-instrumentation`:

1. The discovery-flow row.
2. The lifecycle-sequence row.
3. The quick-reference row.

Do not change any other upstream-synchronized content. Verify no occurrence remains, run `git diff --check`, then commit:

```bash
git add skills/using-agent-skills/SKILL.md
git diff --cached --check
git commit -m "chore: remove unavailable skill routes"
```

### Task 8: Re-run final verification

Repeat Task 5 after Tasks 6 and 7. The synchronized files must match upstream except for:

- `disable-model-invocation: true` in the two Addy alternatives.
- The three removed unavailable-router entries.

The new `references/definition-of-done.md` must match upstream byte-for-byte. Confirm all local-only skills remain present, both excluded upstream-only directories remain absent, target skill paths have no uncommitted changes, and the pre-existing user worktree changes remain unstaged.
### Task 9: Align the local meta-router

**Files:**

- Modify: `skills/using-agent-skills/SKILL.md`

The previous cleanup removed only observability entries. Complete the local router alignment:

1. Remove `interview-me` from discovery, lifecycle, and quick-reference sections.
2. Keep `observability-and-instrumentation` absent from all sections.
3. Replace `test-driven-development` with `tdd` in discovery, lifecycle, bug-fix guidance, and quick reference.
4. Replace `code-review-and-quality` with `code-review` in discovery, lifecycle, bug-fix guidance, and quick reference.
5. Renumber the remaining lifecycle steps consecutively after removing the two unavailable steps.

Preserve every other synchronized line. Run `git diff --check`, inspect the diff, stage only this file, and commit:

```bash
git add skills/using-agent-skills/SKILL.md
git diff --cached --check
git commit -m "chore: align local skill router"
```

### Task 10: Re-run final verification

Repeat Task 8 after Task 9. In addition to the earlier checks, confirm the local `using-agent-skills` router contains no unavailable `interview-me` or `observability-and-instrumentation` entries and names Matt's `tdd` and `code-review` defaults consistently.
