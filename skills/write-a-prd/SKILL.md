---
name: write-a-prd
description: Create a PRD through user interview, codebase exploration, and module design, then submit as a GitHub issue. Use when user wants to write a PRD, create a product requirements document, or plan a new feature.
---

# Write a PRD

## Overview
This skill guides the creation of a Product Requirements Document (PRD) through user interviews, codebase exploration, and module design, culminating in a GitHub issue.

## When to Use
Use when the user wants to write a PRD, create a product requirements document, or plan a new feature.

## Process
This skill will be invoked when the user wants to create a PRD. You may skip steps if you don't consider them necessary.

1. Ask the user for a long, detailed description of the problem they want to solve and any potential ideas for solutions.
2. Explore the repo to verify their assertions and understand the current state of the codebase.
3. Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
4. Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.
5. Once you have a complete understanding of the problem and solution, use the template below to write the PRD. The PRD should be submitted as a GitHub issue.

<prd-template>
## Problem Statement
The problem that the user is facing, from the user's perspective.

## Solution
The solution to the problem, from the user's perspective.

## User Stories
A LONG, numbered list of user stories. Each user story should be in the format of:
1. As an <actor>, I want a <feature>, so that <benefit>

## Implementation Decisions
A list of implementation decisions that were made. This can include:
- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions

## Testing Decisions
A list of testing decisions that were made. Include:
- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests

## Out of Scope
A description of the things that are out of scope for this PRD.

## Further Notes
Any further notes about the feature.
</prd-template>

## Common Rationalizations
Agents often attempt to rationalize skipping strict processes under pressure. Watch out for:
- "The feature is simple, I don't need a full PRD."
- "I'll just write the code instead of writing user stories."
**Reality:** PRDs prevent scope creep and ensure alignment before expensive implementation work begins.

## Red Flags
**STOP and restart the process if you see any of these:**
- Generating a PRD without clarifying the problem statement.
- Skipping the user story format.
- Including specific code snippets or file paths in the PRD.
