---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Grill Me

## Overview
This skill provides a structured approach to interviewing the user relentlessly about a plan or design until reaching shared understanding.

## When to Use
Use when the user wants to stress-test a plan, get grilled on their design, or explicitly mentions "grill me".

## Process
Interview the user relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Common Rationalizations
Agents often attempt to rationalize skipping strict processes under pressure. Watch out for:
- "The plan looks good enough, I don't need to ask more questions."
- "I'll just implement it and fix issues later."
**Reality:** Skipping the interview phase leads to misaligned expectations and wasted effort.

## Red Flags
**STOP and restart the process if you see any of these:**
- Accepting vague requirements without probing.
- Asking multiple unrelated questions in a single response instead of resolving one branch at a time.
