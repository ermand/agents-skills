---
description: Create branch, commit staged changes, push, and open PR
---

Create a new branch, commit only staged changes, push, and open a pull request.

Inputs (optional): `$ARGUMENTS`
- If provided, interpret as: `<branch-name> | <commit-message> | <pr-title>`.
- If any required value is missing, ask one concise follow-up.

Then:

1. Verify there are staged changes. If none, stop and tell me to stage files first.
2. Do not stage files automatically. Never run `git add`.
3. Create or switch to the target branch.
4. Commit staged changes only.
5. Push the branch with upstream (`git push -u origin <branch>`).
6. Create the PR with `gh pr create`.
7. Choose the base branch from `origin/HEAD` when available; otherwise use `main`.
8. Return the branch name, commit SHA, and PR URL.

PR body format:
- `## Summary`
- 1-3 bullets, concise, based on staged diff.
