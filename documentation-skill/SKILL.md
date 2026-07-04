---
name: documentation
description: Use when creating, updating, organizing, checking, reading or navigating project docs in a user-selected folder, including ERD, architecture, API, requirements, planning, meeting notes, link checks, and feature-doc updates.
---

# Documentation Skill

Use for project docs in the user's selected folder. Keep `index.md` lightweight, detail docs focused, links valid, and language aligned with user intent.

## Language Policy

- New docs: use requested language, otherwise match the user's latest request.
- Existing docs: preserve language unless translation or rewrite is requested.
- Mixed-language docs: follow surrounding document or section language unless told otherwise.
- Keep filenames, anchors, code identifiers, API paths, table/column names, commands, and literals in ASCII where practical.
- Use lowercase kebab-case for folders and markdown filenames, for example `user-auth/auth-flow.md`.

## Documentation Root

- Use the folder requested by the user.
- If no folder is requested, preserve the existing documentation root when clear.
- If no root is clear, ask before creating one.
- Refer to it as `<doc-root>`.

## Read or Navigate Docs

For requests to understand, summarize, inspect, or navigate docs:

1. Start with `<doc-root>/index.md` when it exists.
2. Read only linked documents relevant to the question.
3. Do not load template references unless creating or editing.
4. If no root is clear, search markdown files with `rg --files -g '*.md'`.

## Create or Edit Docs

Read only matching references:

| Task | Reference |
|---|---|
| `<doc-root>/index.md` | `references/index-guide.md` |
| Detail document shell | `references/detail-doc-guide.md` |
| ERD or database schema | `references/technical-erd.md` |
| Architecture or system design | `references/technical-architecture.md` |
| API docs | `references/technical-api.md` |
| Planning, briefs, requirements | `references/planning.md` |
| Meeting notes, action items | `references/meeting-notes.md` |

For type-specific detail docs, read `detail-doc-guide.md` plus the type reference.

Create: determine language and `<doc-root>`, inspect `<doc-root>/index.md`, create a kebab-case feature folder if needed, draft from references, validate related links, then update the index.

Update: preserve language, update content, `last_updated`, and anchor contents, validate links, and update the index if title, path, category, or summary changed. Recalculate line-number contents only when already used.

Delete or move: update the index, search references to the old path, then update replacements or mark unresolved references with `[VERIFY PATH]`.

## Validation and Missing Info

After index edits, validate every markdown link in `<doc-root>/index.md`. After detail edits, validate every related-document link. Append `[VERIFY PATH]` to unverifiable links.

Ask only for information required to avoid misleading docs. If the user wants progress anyway, use `[TODO: ...]`.

| Document type | Required context |
|---|---|
| First `<doc-root>/index.md` | Documentation folder name, project name, short description |
| Technical design | Feature or system name, stack, main components |
| Meeting notes | Meeting date, attendees, agenda or topic |
| Planning or requirements | Project or feature name, purpose, core scope |

Avoid forcing a language or root folder against context, duplicating details in the index, creating document-type folders unless established, using emoji statuses, or requiring line-number contents for new docs.
