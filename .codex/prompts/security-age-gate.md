---
description: Add or update package release-age gate configs for npm, pnpm, Yarn, or Bun
---

Read and follow `~/.codex/skills/package-release-age-gates/SKILL.md`.

Detect the active JavaScript package manager from lock/config files, add or update missing release-age gate config, and preserve existing settings and comments.

Do not run installs or audits unless explicitly requested.

Report detected package manager(s), changed files, configured age gate, units, and any ambiguity such as multiple lockfiles.
