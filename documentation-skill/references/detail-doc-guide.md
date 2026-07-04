# Detail Document Guide

Use this guide for the common shell of any detail document. For ERD, architecture, API, planning, requirements, or meeting notes, combine this shell with the matching type-specific reference.

Apply the skill language policy. Localize all human-facing headings, metadata labels, table headers, status values, and prose into the target document language. Keep filenames, anchors, code identifiers, API paths, table names, column names, commands, and technical literals ASCII where practical.

## Standard Structure

Use this order:

1. Metadata block.
2. Document title.
3. Anchor-based contents.
4. Body sections.
5. Related documents.
6. Change history, when useful for the project.

Do not create line-number contents for new documents. If an existing document already uses line numbers, preserve that convention and recalculate them after edits.

## Generic Template

```markdown
---
title: [Document Title]
document_type: [Design | API | ERD | Requirements | Meeting Notes | Other]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
version: v1.0
status: Draft
tags: [tag-one, tag-two]
---

# [Document Title]

## Contents

- [Overview](#overview)
- [Section Name](#section-name)
- [Related Documents](#related-documents)
- [Change History](#change-history)

## Overview

[Summarize the purpose, scope, and audience in two or three sentences.]

## [Section Name]

[Write the document body.]

## Related Documents

| Document | Path | Relationship |
|---|---|---|
| [Document Title] | `../feature/document.md` | [Why this document is related] |

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| v1.0 | YYYY-MM-DD | [Name or team] | Initial draft |
```

## Contents Rules

- Use anchor links that match the rendered markdown heading.
- Keep contents to major `##` sections unless the document is long.
- Update contents whenever section names change.
- For new documents, do not include line numbers.
- For existing line-number contents, update the numbers after edits.

## Related Documents Rules

- Use paths relative to the current document.
- Explain why each document is related.
- Verify paths after adding or editing links.
- If a target path cannot be verified, append `[VERIFY PATH]` in the path or relationship cell and report it to the user.

```markdown
| Authentication Flow | `../user-auth/auth-flow.md` | Token rules used by this API |
| Billing API | `../billing/api.md` [VERIFY PATH] | Referenced by payment callbacks |
```

## Metadata Guidance

- Use metadata keys consistently within the project.
- If the project already uses localized metadata labels, preserve them.
- Use `last_updated` for edits and `created` for the original creation date.
- Use text status values such as `Draft`, `In review`, `Approved`, `Deprecated`, or localized equivalents.

## Update Checklist

- [ ] Preserve or intentionally change the document language.
- [ ] Update `last_updated`.
- [ ] Update anchor contents.
- [ ] Recalculate line numbers only if the document already uses them.
- [ ] Verify related-document links.
- [ ] Check whether `<doc-root>/index.md` needs a title, path, category, or summary update.
