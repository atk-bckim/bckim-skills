# index.md Guide

`docs/index.md` is the entry point for project documentation. Keep it short: it should help people and agents find the right detail document, not repeat the detail document.

Apply the skill language policy. Localize headings, labels, descriptions, and category names into the target document language. Keep paths and filenames ASCII/lowercase kebab-case where practical.

## Template

```markdown
---
last_updated: YYYY-MM-DD
version: v1.0
---

# [Project Name]

> [Two or three concise sentences explaining what the project is, who it serves, and the main technical stack.]

## Contents

### [Feature or Domain Category]
- [Document Title](./feature-folder/document-name.md) - [Short purpose]
- [Document Title](./feature-folder/document-name.md) - [Short purpose]

### [Feature or Domain Category]
- [Document Title](./another-feature/document-name.md) - [Short purpose]
```

## Writing Rules

- Keep the project description to two or three sentences.
- Group links by feature or domain, for example `User Authentication`, `Orders`, `Payments`, `Database`, or localized equivalents.
- Order categories by core product areas first, then supporting areas.
- Use link text that matches the document title.
- Use relative paths beginning with `./`.
- Keep each link description to one short phrase.
- Do not include detailed tables, code, diagrams, endpoint lists, or long explanations.

## Update Rules

When adding a document:
1. Add it to the most relevant category.
2. Create a new category only when none fits.
3. Update `last_updated`.
4. Verify the new path exists.

When deleting or moving a document:
1. Remove or update the index entry.
2. Update `last_updated`.
3. Search for links to the old path in other docs.

After any index edit, verify every markdown link in `docs/index.md`. If a target cannot be confirmed, append `[VERIFY PATH]`.

```markdown
- [ERD](./db/erd.md) - Database tables and relationships [VERIFY PATH]
```

## Example

```markdown
---
last_updated: 2026-07-05
version: v1.1
---

# StockManager

> StockManager is a real-time inventory management service for small retailers.
> The frontend uses Vite, React, and TypeScript; the backend uses .NET and MSSQL.

## Contents

### Database
- [ERD](./database/erd.md) - Tables and relationships
- [Index Strategy](./database/index-strategy.md) - Query performance indexes

### User Authentication
- [Authentication Flow](./user-auth/auth-flow.md) - Login and token lifecycle
- [Permission Policy](./user-auth/permissions.md) - Role-based access rules

### Inventory
- [Inventory API](./inventory/api.md) - Inventory CRUD endpoints
- [Low-Stock Alerts](./inventory/alerts.md) - Alerting rules and thresholds
```
