#!/usr/bin/env python3
"""DPL Verdict Gate.

Computes the maximum verdict that structured evidence supports and compares it
with the verdict the agent declared. Build/lint/test results are recorded but
never upgrade a visual verdict.

Exit codes: 0 PASS | 10 PASS_WITH_WARNING | 20 FAIL | 30 NOT_VERIFIED | 2 invalid evidence
"""
import argparse
import fnmatch
import hashlib
import json
import os
import sys

RANK = {"FAIL": 0, "NOT_VERIFIED": 1, "PASS_WITH_WARNING": 2, "PASS": 3}
EXIT = {"PASS": 0, "PASS_WITH_WARNING": 10, "FAIL": 20, "NOT_VERIFIED": 30}
EXIT_INVALID = 2
CHECK_STATUSES = {"pass", "fail", "unverifiable", "judged"}
REVIEW_MODES = {"harness", "human_render"}
GATE_EVIDENCE_FIELDS = {
    "schema", "review_mode", "human_review", "product", "baseline", "philosophy",
    "fixture", "captures", "a11y_dumps", "expected_checks", "checks",
    "unverified_areas", "build_checks", "claims", "scope", "declared_verdict",
}


class InvalidEvidence(Exception):
    pass


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _require(cond, msg):
    if not cond:
        raise InvalidEvidence(msg)


def _load_artifacts(evidence, base_dir):
    artifacts = {}
    for item in evidence.get("captures", []) + evidence.get("a11y_dumps", []):
        for key in ("id", "path", "sha256"):
            _require(key in item, "artifact missing '%s': %s" % (key, item))
        _require(item["id"] not in artifacts, "duplicate artifact id: %s" % item["id"])
        path = os.path.join(base_dir, item["path"])
        _require(os.path.isfile(path), "artifact file not found: %s" % item["path"])
        _require(_sha256(path) == item["sha256"], "sha256 mismatch: %s" % item["path"])
        artifacts[item["id"]] = item
    return artifacts


def _invoked_engines(ledger):
    names = set()
    for event in (ledger or {}).get("events", []):
        proof = event.get("proof") or {}
        if (
            event.get("type") == "engine_invoked"
            and event.get("invoked") is True
            and proof.get("command")
        ):
            names.add(event.get("name"))
    return names


def compute(evidence, ledger, base_dir):
    _require(evidence.get("schema") == "dpl.evidence/1", "unsupported evidence schema")
    artifacts = _load_artifacts(evidence, base_dir)
    checks = evidence.get("checks", [])
    review_mode = evidence.get("review_mode", "harness")
    _require(review_mode in REVIEW_MODES, "invalid review_mode")

    if review_mode == "human_render":
        review = evidence.get("human_review") or {}
        for key in ("reviewer", "environment", "viewport", "reviewed_capture_ids", "reviewed_areas"):
            _require(review.get(key), "human_render requires human_review.%s" % key)
        known_capture_ids = {item.get("id") for item in evidence.get("captures", [])}
        for ref in review.get("reviewed_capture_ids", []):
            _require(ref in known_capture_ids, "human_review cites unknown capture '%s'" % ref)

    for check in checks:
        _require(
            check.get("status") in CHECK_STATUSES,
            "check %s has invalid status" % check.get("id"),
        )
        for ref in check.get("evidence", []):
            _require(
                ref in artifacts,
                "check %s cites unknown artifact '%s'" % (check.get("id"), ref),
            )

    reasons = []
    state = {"verdict": "PASS"}

    def add(code, severity, message):
        reasons.append({"code": code, "severity": severity, "message": message})

    def lower(to):
        if RANK[to] < RANK[state["verdict"]]:
            state["verdict"] = to

    # No rendered capture means visual QA cannot be verified.
    if not evidence.get("captures"):
        add(
            "NO_RENDER_EVIDENCE",
            "not_verified",
            "no rendered capture recorded; build/lint/test cannot substitute",
        )
        lower("NOT_VERIFIED")
    else:
        # R10: zero philosophy checks is only a warning for harness mode.
        # Human-render review may still PASS when its required review record is complete.
        if review_mode == "harness" and not checks:
            add(
                "NO_PHILOSOPHY_CHECKS",
                "warn",
                "harness review has no philosophy checks; visual evidence exists but product-philosophy compliance is not machine-checked",
            )
            lower("PASS_WITH_WARNING")

        philosophy = evidence.get("philosophy") or {}
        compiled_hash = philosophy.get("compiled_doc_sha256")
        current_hash = philosophy.get("current_doc_sha256")
        if compiled_hash and current_hash and compiled_hash != current_hash:
            add(
                "CHECKS_STALE",
                "warn",
                "philosophy checks were compiled from a different source document hash",
            )
            lower("PASS_WITH_WARNING")

        for check in checks:
            cid = check.get("id")
            status = check["status"]
            blocker = check.get("severity", "warning") == "blocker"

            if status == "fail":
                add(
                    "CHECK_FAILED",
                    "fail" if blocker else "warn",
                    "%s: %s" % (cid, check.get("detail", "")),
                )
                lower("FAIL" if blocker else "PASS_WITH_WARNING")
            elif status == "unverifiable" and check.get("kind") == "judgment":
                add(
                    "JUDGMENT_PENDING",
                    "warn",
                    "%s: judgment-type principle not yet judged with evidence" % cid,
                )
                lower("PASS_WITH_WARNING")
            elif status == "unverifiable":
                add(
                    "CHECK_UNVERIFIABLE",
                    "warn" if blocker else "info",
                    "%s: %s" % (cid, check.get("detail", "")),
                )
                if blocker:
                    lower("PASS_WITH_WARNING")
            elif status == "judged" and not check.get("evidence"):
                add(
                    "JUDGMENT_WITHOUT_EVIDENCE",
                    "warn",
                    "%s: judgment cites no evidence" % cid,
                )
                lower("PASS_WITH_WARNING")

        reported = {check.get("id") for check in checks}
        for cid in evidence.get("expected_checks", []):
            if cid not in reported:
                add("CHECK_NOT_RUN", "warn", "%s was expected but has no result" % cid)
                lower("PASS_WITH_WARNING")

        for area in evidence.get("unverified_areas", []):
            add(
                "UNVERIFIED_AREA",
                "warn",
                "%s: %s" % (area.get("area"), area.get("reason")),
            )
            lower("PASS_WITH_WARNING")

        fixture = evidence.get("fixture")
        if evidence.get("baseline"):
            if not fixture or fixture.get("sha256_before") != fixture.get("sha256_after"):
                add(
                    "NON_COMPARABLE_DATA",
                    "warn",
                    "before/after fixtures differ or are missing",
                )
                lower("PASS_WITH_WARNING")

        if fixture and fixture.get("network") != "blocked":
            add(
                "NETWORK_NOT_BLOCKED",
                "warn",
                "network not blocked; data may drift between captures",
            )
            lower("PASS_WITH_WARNING")

        product = evidence.get("product", {})
        if product.get("dirty") and not product.get("worktree_diff_sha256"):
            add(
                "DIRTY_TREE_UNPINNED",
                "warn",
                "built from a dirty tree without worktree_diff_sha256",
            )
            lower("PASS_WITH_WARNING")

    # Provenance and scope checks apply even when visual evidence is missing.
    claimed = set(evidence.get("claims", {}).get("engines_used", []))
    missing = sorted(claimed - _invoked_engines(ledger))
    if missing:
        add(
            "FALSE_ENGINE_CLAIM",
            "fail",
            "claimed but no invocation proof in ledger: %s" % ", ".join(missing),
        )
        lower("FAIL")

    scope = evidence.get("scope")
    if scope:
        for path in scope.get("changed_files", []):
            hit = any(fnmatch.fnmatch(path, pattern) for pattern in scope.get("denylist_globs", []))
            excepted = any(fnmatch.fnmatch(path, pattern) for pattern in scope.get("exceptions", []))
            if hit and not excepted:
                add("SCOPE_VIOLATION", "fail", "changed out-of-scope file: %s" % path)
                lower("FAIL")

    build_checks = evidence.get("build_checks", {})
    if build_checks:
        add(
            "BUILD_CHECKS_RECORDED",
            "info",
            "build/lint/tests recorded (%s); they never raise the verdict"
            % json.dumps(build_checks),
        )

    declared = evidence.get("declared_verdict")
    computed = state["verdict"]
    return {
        "schema": "dpl.verdict/1",
        "computed": computed,
        "declared": declared,
        "overclaim": bool(declared in RANK and RANK[declared] > RANK[computed]),
        "reasons": reasons,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="DPL Verdict Gate")
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--ledger")
    parser.add_argument("--out")
    args = parser.parse_args(argv)

    try:
        with open(args.evidence, encoding="utf-8") as f:
            evidence = json.load(f)

        ledger = None
        if args.ledger:
            with open(args.ledger, encoding="utf-8") as f:
                ledger = json.load(f)

        result = compute(
            evidence,
            ledger,
            os.path.dirname(os.path.abspath(args.evidence)),
        )
    except (InvalidEvidence, ValueError, OSError) as exc:
        print(json.dumps({"schema": "dpl.verdict/1", "error": str(exc)}, ensure_ascii=False))
        return EXIT_INVALID

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)
    return EXIT[result["computed"]]


if __name__ == "__main__":
    sys.exit(main())
