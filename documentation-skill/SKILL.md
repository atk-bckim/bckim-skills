---
name: documentation
description: Use when creating, updating, organizing, or checking project docs in docs/, including ERD, architecture, API, requirements, planning, meeting notes, link checks, and documentation updates after feature work.
---

# Documentation Skill

## Purpose

Create and maintain project documentation under `docs/` with a lightweight `index.md`, focused detail documents, valid links, and document language that matches the user's intent.

## Language Policy

- New documents: use the language explicitly requested by the user. If none is specified, match the language of the user's latest request.
- Existing documents: preserve the document's current language unless the user asks to translate or rewrite it.
- Mixed-language projects: follow the surrounding document or section language unless the user gives a stronger instruction.
- Keep folder names, filenames, anchors, code identifiers, API paths, table names, column names, commands, and other technical literals in ASCII where practical.
- Use lowercase kebab-case for feature folders and markdown filenames, for example `user-auth/auth-flow.md`.

## Layout

```text
docs/
+-- index.md
+-- feature-name/
|   +-- detail-document.md
|   +-- another-detail.md
+-- another-feature/
    +-- detail-document.md
```

Organize by feature or domain, not by document type. Keep `docs/index.md` current when documents are added, renamed, moved, or deleted.

## Reference Routing

Read the matching reference before writing or changing docs:

| Task | Reference |
|---|---|
| Create or update `docs/index.md` | `references/index-guide.md` |
| Create or update any detail document shell | `references/detail-doc-guide.md` |
| ERD, architecture, API, system design | `references/technical-design.md` |
| Planning docs, product briefs, requirements | `references/planning.md` |
| Meeting notes and action items | `references/meeting-notes.md` |

For a type-specific document, read `detail-doc-guide.md` plus the relevant type-specific reference.

## Workflow

Create:
1. Determine the target language from the Language Policy.
2. Inspect `docs/index.md` if it exists.
3. Create the feature folder using lowercase kebab-case if needed.
4. Create the detail document from `detail-doc-guide.md` and any type-specific reference.
5. Validate related-document links.
6. Add or update the `docs/index.md` entry and validate index links.

Update:
1. Preserve the existing language unless translation is requested.
2. Update body content, metadata such as `last_updated`, and anchor-based contents.
3. Preserve and recalculate line-number contents only when the existing document already uses them.
4. Validate related-document links.
5. Update `docs/index.md` if title, path, category, or summary changed.

Delete or move:
1. Remove or update the `docs/index.md` entry.
2. Search for references to the old path.
3. Update valid replacements, or mark unresolved references with `[VERIFY PATH]`.
4. Report unresolved references to the user.

## Validation and Missing Info

Validate every markdown link in `docs/index.md` after index edits, and every related-document link after detail document edits. If a path cannot be verified, keep the link visible and append `[VERIFY PATH]`.

Ask only for information required to avoid misleading docs. If the user wants progress without answering, use `[TODO: ...]` placeholders.

| Document type | Required context |
|---|---|
| First `docs/index.md` | Project name and short project description |
| Technical design | Feature or system name, stack, main components |
| Meeting notes | Meeting date, attendees, agenda or topic |
| Planning or requirements | Project or feature name, purpose, core scope |

## Common Mistakes

- Do not force Korean or English when the user language or existing document language says otherwise.
- Do not duplicate detail content inside `docs/index.md`.
- Do not create document-type folders such as `erd/` or `meetings/` unless the project already does.
- Do not use emoji status markers; use text values such as `Not started`, `In progress`, `Done`, `Blocked`, or `Canceled`.
- Do not require line-number contents for new documents.
