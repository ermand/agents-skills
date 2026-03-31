---
name: code-review
description: Performs comprehensive code reviews with structured, prioritized feedback. Use when asked to review code, a file, a PR, or a diff — checks for bugs, security vulnerabilities, performance issues, missing tests, and style violations.
---

# Code Review

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
