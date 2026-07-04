# Documentation Skill

The `documentation` skill is built for AI-assisted coding sessions where documentation can quietly become a token sink.

When an agent is asked to "check the docs" or "write the API spec," it often over-reads: project indexes, old meeting notes, architecture drafts, API examples, database notes, and templates that are not relevant to the current task. That burns context before the real work starts.

This skill tries to make documentation work cheaper and more predictable.

## Purpose

The skill helps Codex create, update, read, and navigate project documentation while keeping context focused.

It is designed to:

- respect the documentation folder selected by the user
- preserve existing project documentation structure when clear
- use the user's language for new documents
- preserve existing document language during updates
- keep an `index.md` as a lightweight navigation map
- load task-specific reference files only when needed

It is not meant to be a full documentation framework. It is a context-routing skill.

## Why Tokens Matter

AI agents work inside a context window. Every unrelated document loaded into that window competes with source code, user intent, test output, and the actual reasoning needed to solve the task.

For vibe coding, this matters because sessions often move fast:

- "Summarize the current architecture."
- "Write API docs for this route."
- "Update the requirements after this feature."
- "Create meeting notes from this discussion."

Without routing, each request can pull in too much context. With routing, the agent starts small and reads only what the task needs.

## Structure

```text
documentation-skill/
+-- SKILL.md
+-- references/
    +-- index-guide.md
    +-- detail-doc-guide.md
    +-- technical-api.md
    +-- technical-architecture.md
    +-- technical-erd.md
    +-- planning.md
    +-- meeting-notes.md
```

`SKILL.md` is the router. It tells the agent how to choose a documentation root, when to read an index, and which reference file to load for a writing task.

The reference files are split by task. API documentation does not need to load ERD templates. ERD documentation does not need meeting-note templates. This is the main token-saving design.

## Token-Saving Behavior

Current word counts:

| File | Role | Words |
|---|---:|---:|
| `documentation-skill/SKILL.md` | Router and core rules | 499 |
| `references/index-guide.md` | Index template | 391 |
| `references/detail-doc-guide.md` | Generic document shell | 478 |
| `references/technical-api.md` | API docs only | 239 |
| `references/technical-architecture.md` | Architecture docs only | 294 |
| `references/technical-erd.md` | ERD docs only | 272 |
| `references/planning.md` | Planning and requirements | 631 |
| `references/meeting-notes.md` | Meeting notes | 359 |

Typical load paths:

| Task | What the agent should load |
|---|---|
| Read existing docs | `SKILL.md`, then selected `<doc-root>/index.md`, then only relevant linked docs |
| Create API docs | `SKILL.md`, `detail-doc-guide.md`, `technical-api.md` |
| Create ERD docs | `SKILL.md`, `detail-doc-guide.md`, `technical-erd.md` |
| Create architecture docs | `SKILL.md`, `detail-doc-guide.md`, `technical-architecture.md` |
| Create meeting notes | `SKILL.md`, `detail-doc-guide.md`, `meeting-notes.md` |
| Create requirements | `SKILL.md`, `detail-doc-guide.md`, `planning.md` |

This keeps the common path small. The agent should not load every template just because the user said "docs."

## Documentation Root Policy

The skill does not force a `docs/` folder.

It uses:

1. the folder explicitly requested by the user
2. the existing project documentation root, if one is clear
3. a clarification question before creating a new root when no root is clear

Inside this repository, long-form explanations live in `docs/` because that is the chosen folder for repo-level documentation. That is a repository choice, not a rule imposed by the skill.

## Practical Example

If the user says:

```text
Create API documentation under project-docs for the auth routes.
```

The expected behavior is:

1. use `project-docs/` as the documentation root
2. inspect `project-docs/index.md` if it exists
3. load `detail-doc-guide.md`
4. load `technical-api.md`
5. write the API doc
6. update `project-docs/index.md`

The agent should not load ERD, architecture, planning, or meeting-note templates for that task.

## Design Principle

This skill is not about making documentation bigger. It is about making documentation cheaper to use.

Good documentation for AI agents should act like a map:

- start with a small index
- link to focused details
- avoid duplicating content
- avoid loading unrelated templates
- preserve local project conventions

That is the reason this skill is split into a small router and focused references.
