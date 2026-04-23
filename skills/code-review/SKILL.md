---
name: code-review
description: Use when asked to review code, a file, a PR, or a diff — checks for bugs, security vulnerabilities, performance issues, missing tests, and style violations.
---

# Code Review

## Overview

This skill establishes standard practices and workflows for Code Review.

## When to Use

Use when asked to review code, a file, a PR, or a diff — checks for bugs, security vulnerabilities, performance issues, missing tests, and style violations.

Perform a comprehensive code review with structured, prioritized feedback.

## Usage

```
/code-review [file, path, or PR]
```

## Behavior

1. Analyze the code changes or file(s)
2. Check for:
   - Logic errors and bugs
   - Security vulnerabilities
   - Performance issues
   - Code style violations
   - Missing tests
3. Provide actionable feedback with `file:line` citations

## Review Categories

### Critical
Issues that must be fixed before merging:
- Security vulnerabilities
- Data loss risks
- Breaking changes

### Important
Issues that should be addressed:
- Performance problems
- Logic errors
- Missing error handling

### Suggestions
Nice-to-have improvements:
- Code style
- Better naming
- Refactoring opportunities

## Output Format

```
## Code Review Summary

### Critical Issues
- [file:line] Description

### Important Issues
- [file:line] Description

### Suggestions
- [file:line] Description

### What's Good
- Positive feedback
```


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