# tkform-author Skill

The `tkform-author` skill is built for AI-assisted authoring of `*.tkform.json` files: JSON project files that describe Tkinter GUIs for the tkform VS Code extension.

The practical goal is to keep agents from guessing Tkinter JSON structure from scratch. Instead, the skill gives Codex a small routing hub, focused reference files, a bundled JSON Schema, and a validator that mirrors the extension engine.

## Purpose

The skill helps Codex create, edit, extend, and fix tkform project files.

It is designed to:

- generate starter windows, dialogs, menus, forms, settings panels, and data-browser style UIs
- add widgets, Tk variables, events, menus, non-visual components, and image resources
- keep `.tkform.json` files structurally valid against `tkform.schema.json`
- validate behavioral rules with `scripts/validate_project.py`
- avoid loading every Tkinter rule when only one focused construct is needed

It is not a generic Tkinter code-generation skill. The source of truth is the tkform JSON format, not raw Python.

## Why Tokens Matter

Tkinter GUI authoring has many small rules: widget prop allow-lists, ttk styling constraints, event handler shape, variable references, menu structure, layout-manager limits, image resource wiring, and cross-widget bindings.

If all of those rules are loaded on every request, the agent spends context before it has even read the target `.tkform.json` file. This skill is split so the common path stays smaller:

- `SKILL.md` gives the mental model, traps, workflow, and routing table
- `references/widgets.md` is loaded when widget types or props matter
- `references/events.md` is loaded only for event wiring
- `references/layout.md` is loaded only for placement/grid issues
- other references are loaded only for their matching feature area

For vibe coding, this matters because UI requests often start broad but only need one rule set:

- "Add a Save button that prints the form values."
- "Make this settings panel use variables."
- "Add a table with a scrollbar."
- "Why does this tkform file fail validation?"

The skill should route to the smallest useful reference before editing.

## Structure

```text
tkform-author/
+-- SKILL.md
+-- tkform.schema.json
+-- scripts/
|   +-- validate_project.py
+-- references/
    +-- widgets.md
    +-- complex-widgets.md
    +-- events.md
    +-- variables.md
    +-- layout.md
    +-- menus.md
    +-- non-visuals.md
    +-- resources.md
    +-- validation.md
```

`SKILL.md` is the router. It gives the 30-second model, minimal valid project, traps, workflow, and a reference selection table.

`tkform.schema.json` provides structural shape for `.tkform.json` files.

`scripts/validate_project.py` validates a project with the same engine behavior that the tkform extension uses, when the engine package is available.

## Token-Saving Behavior

Current word counts:

| File | Role | Words |
|---|---:|---:|
| `tkform-author/SKILL.md` | Router, mental model, traps, workflow | 1052 |
| `references/widgets.md` | Widget fields and prop allow-list | 1379 |
| `references/complex-widgets.md` | Treeview, Notebook, PanedWindow, Canvas, Toplevel, Scrollbar | 721 |
| `references/events.md` | Event forms, bindings, handler rules | 848 |
| `references/variables.md` | Tk variable declarations and references | 532 |
| `references/layout.md` | `place` vs `grid`, parent rules | 496 |
| `references/menus.md` | Menu bar and menu item structure | 569 |
| `references/non-visuals.md` | Timer, FileDialog, ColorChooser, MessageBox | 632 |
| `references/resources.md` | Embedded image resources | 373 |
| `references/validation.md` | Diagnostics and limits | 1039 |
| `tkform.schema.json` | JSON Schema | 1561 |
| `scripts/validate_project.py` | Validator wrapper | 361 |

Typical load paths:

| Task | What the agent should load |
|---|---|
| Create a small form | `SKILL.md`, then `widgets.md` if props are non-trivial |
| Add button behavior | `SKILL.md`, `events.md` |
| Add variables to a settings panel | `SKILL.md`, `variables.md`, relevant widget rows from `widgets.md` |
| Add a Treeview with scrollbars | `SKILL.md`, `complex-widgets.md`, `widgets.md` |
| Fix a validation error | `SKILL.md`, `validation.md`, then the specific referenced guide |
| Add a menu bar | `SKILL.md`, `menus.md`, `events.md` if menu commands run code |
| Add embedded images | `SKILL.md`, `resources.md`, relevant widget rows from `widgets.md` |

The full skill is about 9.5k words including schema and validator wrapper. The intended behavior is not to load that full set by default.

## Validation Workflow

The expected loop is:

1. Read the existing `.tkform.json` file, or start from the minimal valid project in `SKILL.md`.
2. Load only the reference file that matches the feature being changed.
3. Edit the JSON while preserving existing style and ids.
4. Run the validator:

```bash
python tkform-author/scripts/validate_project.py path/to/file.tkform.json
```

When the skill is installed into an agent skill directory, use the validator path from that installed location.

Validation matters because JSON Schema only catches shape. The validator catches cross-references, unsupported props, invalid commands, layout conflicts, missing variables, missing resources, and Python handler compile errors.

## Good Fit

Use this skill when the user asks for:

- a `.tkform.json` GUI project
- a Tkinter UI managed by the tkform VS Code extension
- form, dialog, menu, settings panel, or data-browser JSON in tkform format
- widget/event/variable/resource updates to an existing tkform project
- validation fixes for tkform diagnostics

## Not a Good Fit

Do not use this skill when the user wants:

- raw Tkinter `.py` code
- changes to the tkform extension implementation itself
- general GUI design that is not targeting the tkform JSON format

In those cases, normal coding or a more specific UI skill is a better fit.

## Design Principle

This skill is useful when it keeps the agent honest and narrow:

- author the source JSON, not exported Python
- use the schema for structure
- use the validator for behavior
- read focused references on demand
- report success only after validation passes

The value is not just faster generation. It is fewer invalid GUI files, less context waste, and a repeatable path from user intent to validated tkform project JSON.
