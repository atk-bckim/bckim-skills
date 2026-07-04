# Planning and Requirements Guide

Use this reference for project plans, product briefs, feature specs, and requirements documents. Start with the shell in `detail-doc-guide.md`, then choose the relevant body sections below.

Apply the skill language policy. Localize headings, table labels, priority labels, status values, and prose into the target document language. Keep requirement IDs, feature IDs, file paths, API paths, and technical identifiers ASCII where practical.

## Product or Project Plan Body Sections

```markdown
## Overview

| Field | Value |
|---|---|
| Project | [Project name] |
| Purpose | [One-sentence purpose] |
| Timeframe | YYYY-MM-DD to YYYY-MM-DD |
| Owner | [Team or person] |
| Status | Draft |

## Background and Goals

- **Background**: [Why this work exists.]
- **Goals**: [What this work should achieve.]
- **Expected impact**: [What changes when this succeeds.]

## Scope

### In Scope

| Item | Description |
|---|---|
| [Feature or work item] | [What is included] |

### Out of Scope

| Item | Reason |
|---|---|
| [Excluded item] | [Why it is excluded] |

## Requirements

| ID | Requirement | Priority | Owner | Status |
|---|---|---|---|---|
| REQ-001 | [Requirement] | Must | [Owner] | Not started |
| REQ-002 | [Requirement] | Should | [Owner] | Not started |

## Milestones

| Phase | Work | Start | End | Owner |
|---|---|---|---|---|
| Planning | Requirements and scope | YYYY-MM-DD | YYYY-MM-DD | [Owner] |
| Design | Technical design | YYYY-MM-DD | YYYY-MM-DD | [Owner] |
| Build | Implementation | YYYY-MM-DD | YYYY-MM-DD | [Owner] |
| Test | QA and validation | YYYY-MM-DD | YYYY-MM-DD | [Owner] |
| Release | Production rollout | YYYY-MM-DD | YYYY-MM-DD | [Owner] |

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [Risk] | Medium | High | [Mitigation plan] |
```

## Feature Requirements Body Sections

```markdown
## Purpose

[Explain what this feature should accomplish in one or two paragraphs.]

## Users and Use Cases

| User | Goal | Notes |
|---|---|---|
| [User type] | [Goal] | [Context or constraints] |

## Functional Requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| F-001 | [Specific behavior] | Must | Not started |
| F-002 | [Specific behavior] | Should | Not started |

## Requirement Details

### F-001. [Requirement Name]

| Field | Value |
|---|---|
| Priority | Must |
| Users | [Target users] |
| Status | Not started |

**Description**

[Describe the required behavior and expected outcome.]

**Acceptance Criteria**

| # | Criterion |
|---|---|
| 1 | [Observable acceptance criterion] |
| 2 | [Observable acceptance criterion] |

**Edge Cases**

| Case | Expected Handling |
|---|---|
| [Condition] | [Expected behavior] |

## Non-Functional Requirements

| Area | Requirement | Notes |
|---|---|---|
| Performance | [Performance target] | [Measurement context] |
| Security | [Security requirement] | [Auth, data, or compliance notes] |
| Compatibility | [Browser, OS, API, or migration requirement] | [Supported range] |
```

## Status and Priority Values

Use plain text values, localized when appropriate:

| Category | Suggested values |
|---|---|
| Status | Not started, In progress, Blocked, Done, Canceled |
| Priority | Must, Should, Could, Won't |
| Risk likelihood | Low, Medium, High |
| Risk impact | Low, Medium, High |

## Planning Checklist

- [ ] Capture purpose, scope, owner, and status.
- [ ] Separate in-scope and out-of-scope work.
- [ ] Use requirement IDs consistently.
- [ ] Write acceptance criteria as observable outcomes.
- [ ] Mark unknown dates, owners, and constraints with `[TODO: ...]`.
- [ ] Link related technical designs, API docs, ERDs, and meeting notes through the related-documents section.
