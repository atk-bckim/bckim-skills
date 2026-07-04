# Technical API Guide

Use this reference for REST, RPC, webhook, and integration API documents. Start with `detail-doc-guide.md` for the document shell.

Apply the skill language policy. Localize human-facing headings and descriptions, but keep methods, paths, status codes, field names, JSON keys, headers, commands, and code identifiers unchanged.

## Body Sections

````markdown
## Overview

- **Purpose**: [What API surface this document defines.]
- **Base URL**: `/api`
- **Authentication**: [None | JWT | Session | API key]

## Endpoint Summary

| Method | Path | Description | Auth |
|---|---|---|---|
| GET | `/api/users` | List users | Required |
| POST | `/api/users` | Create user | Required |

## Endpoint Details

### `GET /api/users`

**Purpose**

[Explain what this endpoint returns.]

**Request**

| Field | Location | Type | Required | Description |
|---|---|---|---|---|
| page | Query | integer | No | Page number |
| page_size | Query | integer | No | Items per page |

**Response**

```json
{
  "items": [],
  "total": 0
}
```

**Errors**

| Status | Code | Condition |
|---|---|---|
| 401 | UNAUTHORIZED | Missing or invalid credentials |
| 500 | INTERNAL_ERROR | Unexpected server failure |
````

## Checklist

- [ ] Verify methods, paths, parameters, and responses against source/routes when available.
- [ ] Mark unknown auth, payload, or error behavior with `[TODO: ...]`.
- [ ] Link related ERD, architecture, and requirements docs through the related-documents section.
