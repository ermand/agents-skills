---
name: package-release-age-gates
description: Use when hardening JavaScript npm dependencies against fresh package publishes, supply-chain attacks, typosquatting windows, compromised package updates, or configuring minimum release age gates for npm, pnpm, Yarn, or Bun.
---

# Package Release Age Gates

## Overview

Add package-manager cooldowns so installs avoid versions published minutes or hours ago. This reduces blast radius from newly compromised npm packages; it does not replace lockfiles, audits, provenance checks, or review.

## When to Use

- User mentions npm/package security, dependency supply chain, compromised releases, newly published packages, or package update hardening.
- User asks to add package-manager configs from the release-age gate article.
- Repo has npm, pnpm, Yarn, or Bun config/lock files and lacks the relevant age gate.

## Quick Reference

Default to 7 days unless the user requests another value.

| Manager | Detect | File | Setting |
| --- | --- | --- | --- |
| pnpm | `pnpm-lock.yaml`, `pnpm-workspace.yaml` | `pnpm-workspace.yaml` | `minimumReleaseAge: 10080` |
| Yarn | `yarn.lock`, `.yarnrc.yml` | `.yarnrc.yml` | `npmMinimalAgeGate: "7d"` |
| Bun | `bun.lock`, `bun.lockb`, `bunfig.toml` | `bunfig.toml` | `[install]` then `minimumReleaseAge = 604800` |
| npm | `package-lock.json`, `.npmrc` | `.npmrc` | `min-release-age=7` |

Units differ by manager:
- pnpm: minutes, so 7 days is `10080`.
- Yarn: minutes or duration string, prefer `"7d"`.
- Bun: seconds, so 7 days is `604800`.
- npm: days, so 7 days is `7`.

## Workflow

1. Detect package managers from lock/config files.
2. Update each detected manager's config; if multiple managers are present, mention that ambiguity.
3. Preserve existing config and comments. Update an existing age-gate key instead of adding a duplicate.
4. Create the config file only when the manager is detected and the file is missing.
5. Do not run installs or audits unless the user asks.

## Config Patterns

### pnpm

`pnpm-workspace.yaml`:

```yaml
minimumReleaseAge: 10080 # 7 days
```

### Yarn

`.yarnrc.yml`:

```yaml
npmMinimalAgeGate: "7d"
```

### Bun

`bunfig.toml`:

```toml
[install]
minimumReleaseAge = 604800 # 7 days
```

If `[install]` already exists, add `minimumReleaseAge` inside it.

### npm

`.npmrc`:

```ini
min-release-age=7
```

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using npm `minimum-release-age=10080` | Use `min-release-age=7`; npm uses days. |
| Using pnpm value `7` | Use `10080`; pnpm uses minutes. |
| Putting Bun `minimumReleaseAge` at TOML root | Put it under `[install]`. |
| Replacing config files wholesale | Preserve unrelated settings and comments. |
| Treating this as complete security | Still audit, review lockfile changes, and investigate known vulnerabilities. |

## Reporting

Summarize:
- detected package manager(s)
- file(s) changed or created
- configured age gate and units
- any ambiguity, such as multiple lockfiles
