#!/usr/bin/env python3
"""DPL philosophy-check runner.

Input: philosophy.checks.yaml + normalized per-screen layout/accessibility dumps.
Output: check results in the shape expected by evidence.json.

Absence from an incomplete dump is never proof of absence.
"""

import yaml

KINDS = {"order", "first_viewport", "presence", "absence", "judgment"}


def _result(check, status, detail, evidence):
    return {
        "id": check["id"],
        "kind": check.get("kind"),
        "status": status,
        "severity": check.get("severity", "warning"),
        "evidence": evidence,
        "detail": detail,
    }


def run_one(check, dumps):
    kind = check.get("kind")
    if kind not in KINDS:
        raise ValueError("unknown check kind: %r" % kind)

    screen = check.get("scope", {}).get("screen")
    entry = dumps.get(screen)
    if entry is None:
        return _result(check, "unverifiable", "no dump for screen '%s'" % screen, [])

    evidence = [entry["artifact_id"]]
    dump = entry["dump"]
    complete = bool(dump.get("complete"))
    elements = {element["role"]: element for element in dump.get("elements", [])}
    spec = check.get("assert", {})

    if kind == "judgment":
        return _result(
            check,
            "unverifiable",
            "judgment required: attach evidence + rationale",
            evidence,
        )

    if kind == "absence":
        found = [role for role in spec["roles"] if role in elements]
        if found:
            return _result(check, "fail", "forbidden roles present: %s" % found, evidence)
        if not complete:
            return _result(check, "unverifiable", "dump incomplete; absence not provable", evidence)
        return _result(check, "pass", "forbidden roles absent", evidence)

    if kind == "order":
        needed = spec["order"]
    elif kind == "first_viewport":
        needed = [spec["role"]]
    else:
        needed = spec["roles"]

    missing = [role for role in needed if role not in elements]
    if missing:
        if complete:
            return _result(check, "fail", "roles not rendered: %s" % missing, evidence)
        return _result(
            check,
            "unverifiable",
            "roles absent from incomplete dump: %s" % missing,
            evidence,
        )

    if kind == "presence":
        return _result(check, "pass", "all roles present", evidence)

    if kind == "order":
        actual = sorted(needed, key=lambda role: elements[role]["frame"]["y"])
        if actual == needed:
            return _result(check, "pass", "order matches: %s" % needed, evidence)
        return _result(check, "fail", "expected %s, actual %s" % (needed, actual), evidence)

    frame = elements[spec["role"]]["frame"]
    if frame["h"] <= 0:
        return _result(check, "unverifiable", "element height must be > 0", evidence)

    viewport_h = dump["viewport"]["h"]
    visible = max(
        0,
        min(frame["y"] + frame["h"], viewport_h) - max(frame["y"], 0),
    ) / float(frame["h"])
    required = spec.get("min_visible_ratio", 1.0)
    status = "pass" if visible >= required else "fail"
    return _result(
        check,
        status,
        "visible ratio %.2f (need >= %.2f)" % (visible, required),
        evidence,
    )


def run_checks(checks, dumps):
    return [run_one(check, dumps) for check in checks]


def load_checks(path):
    with open(path, encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    if doc.get("version") != 1:
        raise ValueError("unsupported checks version")
    return doc
