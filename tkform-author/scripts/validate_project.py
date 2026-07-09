#!/usr/bin/env python3
"""Validate a tkform project file (.tkform.json) using the bundled engine.

Usage:
    python validate_project.py path/to/project.tkform.json
    python validate_project.py - < project.tkform.json
    cat project.tkform.json | python validate_project.py -

Exit code 0 if there are no error-severity diagnostics, 1 otherwise.
Output:
    - On success: "OK" (plus any warnings/errors counts as a heads-up).
    - On failure: one line per diagnostic: "severity · code · path · message".

This wrapper uses the SAME engine the VS Code extension uses
(`tkform_engine.cli` validate command — see src/extension/pythonEngineClient.ts),
so results match what the designer shows.
"""

import json
import os
import sys


def _engine_root():
    # Skill lives at <repo>/.agents/skills/tkform-author/scripts/validate_project.py.
    # Engine lives at <repo>/python/tkform_engine/.
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, "..", "..", "..", ".."))
    engine_python = os.path.join(repo_root, "python")
    if os.path.isdir(os.path.join(engine_python, "tkform_engine")):
        return engine_python
    # Fallback: maybe the script was copied elsewhere. Try TKFORM_ENGINE_PYTHON env.
    env_root = os.environ.get("TKFORM_ENGINE_PYTHON")
    if env_root and os.path.isdir(os.path.join(env_root, "tkform_engine")):
        return env_root
    raise SystemExit(
        "Could not locate the tkform_engine package. Expected it at "
        "<repo>/python/tkform_engine. Set TKFORM_ENGINE_PYTHON to the directory "
        "containing tkform_engine if the engine lives elsewhere."
    )


def _read_payload(path_arg):
    if path_arg == "-" or path_arg is None:
        raw = sys.stdin.read()
    else:
        with open(path_arg, "r", encoding="utf-8") as handle:
            raw = handle.read()
    return json.loads(raw or "{}")


def main(argv):
    path_arg = argv[1] if len(argv) > 1 else None
    if not path_arg:
        sys.stderr.write(__doc__)
        return 2

    sys.path.insert(0, _engine_root())

    # Imported after sys.path is set up.
    from tkform_engine.models import Project  # noqa: E402
    from tkform_engine.project_limits import project_limit_diagnostics  # noqa: E402
    from tkform_engine.project_validation import validate_project  # noqa: E402

    payload = _read_payload(path_arg)
    project = Project.from_dict(payload)

    diagnostics = []
    diagnostics.extend(project_limit_diagnostics(project))
    diagnostics.extend(validate_project(project))

    errors = [d for d in diagnostics if d.severity == "error"]
    warnings = [d for d in diagnostics if d.severity == "warning"]

    if not diagnostics:
        print("OK")
        return 0

    for d in diagnostics:
        location = getattr(d, "path", "") or ""
        widget_id = getattr(d, "widget_id", None)
        widget_name = getattr(d, "widget_name", None)
        suffix = ""
        if widget_name:
            suffix = " (widget: %s)" % widget_name
        elif widget_id:
            suffix = " (widget id: %s)" % widget_id
        print("%s · %s · %s · %s%s" % (d.severity, d.code, location, d.message, suffix))

    sys.stderr.write("\n%d error(s), %d warning(s)\n" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
