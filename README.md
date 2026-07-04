# bc's skills

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X5U822ISS0)
[![sponsors/atk-bckim](https://img.shields.io/badge/sponsors%2Fatk--bckim-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/atk-bckim)

A personal collection of reusable Codex skills.

## Skills

| Skill | Path | Purpose |
|---|---|---|
| documentation | `documentation-skill/` | Create, update, organize, and check project documentation under `docs/`, using the user's language for new documents and preserving existing document language on updates. |

## Structure

Each skill is kept in its own folder:

```text
skill-folder/
+-- SKILL.md
+-- references/
    +-- supporting-guide.md
```

`SKILL.md` contains the trigger metadata and core workflow. Reference files hold detailed templates or guidance that should be loaded only when needed.

## Usage

Use the skill folders from this repository as personal Codex skills. Keep each skill self-contained, with only the files required for the agent to perform the task.

When updating a skill:

1. Keep the frontmatter `name` stable unless the skill is intentionally renamed.
2. Keep `description` focused on when the skill should trigger.
3. Prefer concise `SKILL.md` files and move detailed templates into `references/`.
4. Validate the skill before committing changes.
