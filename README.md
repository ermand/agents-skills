# @ermand/agent-skills

Production-grade engineering skills for AI coding agents (Claude Code, OpenCode, Codex, Cursor).

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

## Commands

```text
   DEFINE         PLAN           BUILD          VERIFY         REVIEW         SHIP

 ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
 │  Idea  │ ──> │  Spec  │ ──> │  Code  │ ──> │  Test  │ ──> │   QA   │ ──> │   Go   │
 │ Refine │     │  PRD   │     │  Impl  │     │ Debug  │     │  Gate  │     │  Live  │
 └────────┘     └────────┘     └────────┘     └────────┘     └────────┘     └────────┘
   /spec          /plan          /build         /test         /review         /ship
```

7 slash commands that map to the development lifecycle. Each one activates the right skills automatically.

| What you're doing | Command | Key principle |
|-------------------|---------|---------------|
| Define what to build | `/spec` | Spec before code |
| Plan how to build it | `/plan` | Small, atomic tasks |
| Build incrementally | `/build` | One slice at a time |
| Prove it works | `/test` | Tests are proof |
| Review before merge | `/review` | Improve code health |
| Simplify the code | `/code-simplify` | Clarity over cleverness |
| Ship to production | `/ship` | Faster is safer |

Skills also activate automatically based on what you're doing — designing an API triggers `api-and-interface-design`, building UI triggers `frontend-ui-engineering`, and so on.

## Install

### Install Commands & Hooks

**For Claude Code:**
```bash
cp -r node_modules/@ermand/agent-skills/.claude/commands ~/.claude/
```
```bash
cp -r node_modules/@ermand/agent-skills/hooks ~/.claude/
```

**For OpenCode:**
```bash
cp -r node_modules/@ermand/agent-skills/.opencode/commands ~/.config/opencode/
```

### Install Skills

**All skills:**
```bash
npx skills@latest add ermand/agents-skills
```

**Individual skills (examples):**
```bash
npx skills@latest add ermand/agents-skills --skill analysing-codebase
```
```bash
npx skills@latest add ermand/agents-skills --skill code-review
```

## Skills

| Skill | Description |
|-------|-------------|
| `analysing-codebase` | Analyzes an existing codebase and generates structured documentation for onboarding engineers and AI agents. Use when asked to document a codebase, onboard to a new project, create CLAUDE.md or AGENTS.md, or generate architecture, API, or domain documentation. |
| `analysing-codebase-full` | Comprehensive 4-phase codebase analysis generating 12 documentation files including architecture, data models, business rules, API reference, and AI agent context files. Use when thorough onboarding documentation is needed, when the compact version lacks sufficient detail, or for large/complex codebases. |
| `api-and-interface-design` | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or establishing boundaries between frontend and backend. |
| `brainstorming` | "You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation." |
| `browser-testing-with-devtools` | Tests in real browsers. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors, analyze network requests, profile performance, or verify visual output with real runtime data via Chrome DevTools MCP. |
| `ci-cd-and-automation` | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies. |
| `code-review` | Performs comprehensive code reviews with structured, prioritized feedback. Use when asked to review code, a file, a PR, or a diff — checks for bugs, security vulnerabilities, performance issues, missing tests, and style violations. |
| `code-review-and-quality` | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch. |
| `code-simplification` | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulated unnecessary complexity. |
| `context-engineering` | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and context for a project. |
| `debugging-and-error-recovery` | Guides systematic root-cause debugging. Use when tests fail, builds break, behavior doesn't match expectations, or you encounter any unexpected error. Use when you need a systematic approach to finding and fixing the root cause rather than guessing. |
| `deprecation-and-migration` | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when deciding whether to maintain or sunset existing code. |
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `documentation-and-adrs` | Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase. |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill. |
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `frontend-ui-engineering` | Builds production-quality UIs. Use when building or modifying user-facing interfaces. Use when creating components, implementing layouts, managing state, or when the output needs to look and feel production-quality rather than AI-generated. |
| `git-workflow-and-versioning` | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need to organize work across multiple parallel streams. |
| `grill-me` | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". |
| `idea-refine` | Refines ideas iteratively. Refine ideas through structured divergent and convergent thinking. Use "idea-refine" or "ideate" to trigger. |
| `improve-codebase-architecture` | Explore a codebase to find opportunities for architectural improvement, focusing on making the codebase more testable by deepening shallow modules. Use when user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more AI-navigable. |
| `incremental-implementation` | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to write a large amount of code at once, or when a task feels too big to land in one step. |
| `performance-optimization` | Optimizes application performance. Use when performance requirements exist, when you suspect performance regressions, or when Core Web Vitals or load times need improvement. Use when profiling reveals bottlenecks that need fixing. |
| `planning-and-task-breakdown` | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible. |
| `prd-to-issues` | Break a PRD into independently-grabbable GitHub issues using tracer-bullet vertical slices. Use when user wants to convert a PRD to issues, create implementation tickets, or break down a PRD into work items. |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `security-and-hardening` | Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when building any feature that accepts untrusted data, manages user sessions, or interacts with third-party services. |
| `shipping-and-launch` | Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy. |
| `source-driven-development` | Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters. |
| `spec-driven-development` | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements are unclear, ambiguous, or only exist as a vague idea. |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `tdd` | Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development. |
| `test-driven-development` | Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing functionality. |
| `using-agent-skills` | Discovers and invokes agent skills. Use when starting a session or when you need to discover which skill applies to the current task. This is the meta-skill that governs how all other skills are discovered and invoked. |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |
| `write-a-prd` | Create a PRD through user interview, codebase exploration, and module design, then submit as a GitHub issue. Use when user wants to write a PRD, create a product requirements document, or plan a new feature. |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

## How Skills Work

Skills act as specialized workflows that agents follow to complete tasks more effectively. While some skills establish behavioral patterns (like TDD or systematic debugging), others generate artifacts.

For example, using the `analysing-codebase-full` skill generates the following documentation:

**Agent context files** (auto-read by each tool):

| Tool | File |
|------|------|
| Claude Code / OpenCode | `CLAUDE.md` |
| Codex | `AGENTS.md` |
| Cursor | `.cursor/rules/<project-name>.mdc` |
| Copilot / VS Code | `.github/copilot-instructions.md` |

**Documentation** (in `./docs/`):

- `ARCHITECTURE.md` — system overview, C4 diagrams, request lifecycle, infrastructure
- `DATA_MODELS.md` — full schema, ER diagram, relationships, indexes
- `DOMAIN_MAP.md` — bounded contexts, ubiquitous language glossary
- `API_REFERENCE.md` — every endpoint, grouped by domain
- `BUSINESS_RULES.md` — rules with file:line citations, state machines
- `PATTERNS_AND_CONVENTIONS.md` — architectural patterns with real code examples
- `GETTING_STARTED.md` — clone-to-running-app guide, every .env key
- `CODEBASE_MAP.md` — navigation index and change impact map for AI agents
- `TECH_STACK.md` *(full only)* — languages, frameworks, CI/CD, tooling
- `TESTING_GUIDE.md` *(full only)* — test strategy, factories, mocking, coverage
- `DECISION_LOG.md` *(full only)* — architectural decisions and trade-offs

## Commands and Hooks

This repository also includes custom Slash Commands and Tool Hooks for **Claude Code** and **OpenCode**. These provide structured workflows (e.g. `/plan`, `/review`, `/ship`) and automatic triggers (e.g. run linters, play sounds, send notifications) to enhance your agent's capabilities.

### For Claude Code

Claude Code supports custom user-defined commands and tool hooks to orchestrate workflows.

**Install Commands:**
Copy the commands from the `.claude/commands` directory into your project's or global `.claude` directory:
```bash
# Global installation (recommended)
cp -r node_modules/@ermand/agent-skills/.claude/commands ~/.claude/

# Or per-project installation
mkdir -p .claude
cp -r node_modules/@ermand/agent-skills/.claude/commands .claude/
```

**Install Hooks:**
If you want to use the included Python hooks (for MacOS notifications, audio cues, linting, etc.):
```bash
cp -r node_modules/@ermand/agent-skills/hooks ~/.claude/
```
*Note: Make sure to review the Python hooks and adjust any hardcoded paths or requirements as needed for your local environment.*

### For OpenCode

OpenCode shares a similar command architecture and can utilize custom personas/commands.

**Install Commands:**
Copy the commands from the `.opencode/commands` directory into your global opencode configuration directory:
```bash
cp -r node_modules/@ermand/agent-skills/.opencode/commands ~/.config/opencode/
```

### Available Commands

Once installed, you can trigger these workflows directly in your CLI by typing `/` followed by the command name:

- `/plan` - Initiates a structured planning phase before writing any code.
- `/spec` - Generates a detailed specification document.
- `/build` - Guides the agent through the implementation phase.
- `/test` - Enforces a testing workflow (e.g., TDD).
- `/review` - Triggers a self-review or peer-review of the written code.
- `/ship` - Prepares the code for deployment or merging (linting, tests, finalizing PRs).
- `/code-simplify` - Refactors code to reduce complexity and improve readability.
- `/code-review` - Performs a multi-axis code review on the current diff or files.
- `/interview` / `/pr-open` - Facilitates user interviews for requirements or drafts PR descriptions.

## License

MIT © [Ermand Durro](https://github.com/ermand)
