# bc's skills

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X5U822ISS0)
[![sponsors/atk-bckim](https://img.shields.io/badge/sponsors%2Fatk--bckim-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/atk-bckim)

Reusable Codex skills for AI vibe coders who care about context, token cost, and repeatable workflows.

The goal is simple: keep the agent from reading everything when it only needs the next useful slice.

## Skills

| Skill | Path | What it does | Details |
|---|---|---|---|
| documentation | `documentation-skill/` | Creates, updates, reads, and navigates project documentation in the user's selected folder. | [docs/documentation-skill.md](docs/documentation-skill.md) |
| tkform-author | `TKform-skill/` | Creates and edits validated `.tkform.json` Tkinter GUI projects for the tkform VS Code extension. | [docs/tkform-author.md](docs/tkform-author.md) |

## Why This Exists

AI coding sessions get messy when every request reloads broad instructions, old specs, meeting notes, and unrelated templates. These skills are written to route the agent through small entry points first, then load detailed references only when the task actually needs them.

## Skill Shape

```text
skill-folder/
+-- SKILL.md
+-- references/
    +-- focused-guide.md
```

`SKILL.md` should stay small and act as the router. `references/` should hold focused guides that are loaded only for matching tasks.

## Docs

- [Documentation skill details](docs/documentation-skill.md)
- [tkform-author skill details](docs/tkform-author.md)
