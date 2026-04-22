---
description: Perform a comprehensive code review — analyze logic, security, performance, and style
---

Invoke the agent-skills:code-review skill.

Review the changes comprehensively. For each review:

1. Analyze logic for bugs, edge cases, and requirement mismatches
2. Verify security for vulnerabilities, sensitive data exposure, and unsafe practices
3. Assess performance for bottlenecks, memory leaks, and inefficient operations
4. Check quality for code style consistency, naming clarity, and modularity
5. Review tests to confirm coverage for new behavior and guard against regressions

Format the feedback as follows:

## Code Review Summary

### Critical Issues
- [file:line] Issues that must be fixed (Security, Data Loss, Breaking Changes).

### Important Issues
- [file:line] Issues that should be addressed (Performance, Logic Errors, Error Handling).

### Suggestions
- [file:line] Nice-to-have improvements (Style, Naming, Refactoring).

### What's Good
- Positive feedback on well-implemented parts.

If review context is incomplete or findings are ambiguous, state the assumption explicitly before giving feedback.
