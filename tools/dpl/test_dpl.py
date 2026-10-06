import hashlib
import os
import tempfile
import unittest

import checks_runner as cr
import verdict_gate as vg


def sha(data):
    return hashlib.sha256(data).hexdigest()


def make_run(mutate=None, ledger=None):
    directory = tempfile.mkdtemp()
    os.makedirs(os.path.join(directory, "captures"))

    png = b"SYNTHETIC-PLACEHOLDER"
    with open(os.path.join(directory, "captures", "after_top.png"), "wb") as f:
        f.write(png)

    evidence = {
        "schema": "dpl.evidence/1",
        "review_mode": "harness",
        "product": {"head": "abc123", "dirty": False},
        "baseline": {"ref": "3a1cf16"},
        "fixture": {
            "id": "stable",
            "sha256_before": "f1",
            "sha256_after": "f1",
            "network": "blocked",
        },
        "captures": [
            {
                "id": "after_top",
                "path": "captures/after_top.png",
                "sha256": sha(png),
            }
        ],
        "a11y_dumps": [],
        "checks": [
            {
                "id": "C1",
                "status": "pass",
                "severity": "blocker",
                "evidence": ["after_top"],
            }
        ],
        "unverified_areas": [],
        "build_checks": {"build": "pass", "tests": "not_run"},
        "declared_verdict": "PASS",
    }

    if mutate:
        mutate(evidence)

    return directory, evidence, ledger


def gate(mutate=None, ledger=None):
    directory, evidence, ledger = make_run(mutate, ledger)
    return vg.compute(evidence, ledger, directory)


def codes(result):
    return {reason["code"] for reason in result["reasons"]}


class GateTests(unittest.TestCase):
    def test_clean_pass(self):
        result = gate()
        self.assertEqual(result["computed"], "PASS")
        self.assertFalse(result["overclaim"])

    def test_no_captures_is_not_verified_even_if_build_passes(self):
        result = gate(lambda e: e.update(captures=[], checks=[]))
        self.assertEqual(result["computed"], "NOT_VERIFIED")
        self.assertTrue(result["overclaim"])

    def test_blocker_fail(self):
        result = gate(lambda e: e["checks"][0].update(status="fail", detail="order wrong"))
        self.assertEqual(result["computed"], "FAIL")

    def test_nonblocker_fail_is_warning(self):
        result = gate(lambda e: e["checks"][0].update(status="fail", severity="warning"))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")

    def test_blocker_unverifiable_caps_at_warning_and_flags_overclaim(self):
        result = gate(lambda e: e["checks"][0].update(status="unverifiable"))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")
        self.assertTrue(result["overclaim"])

    def test_unverified_area_caps_at_warning(self):
        result = gate(
            lambda e: e["unverified_areas"].append(
                {"area": "a11y_tree", "reason": "not captured"}
            )
        )
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")

    def test_fixture_mismatch_non_comparable(self):
        result = gate(lambda e: e["fixture"].update(sha256_after="f2"))
        self.assertIn("NON_COMPARABLE_DATA", codes(result))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")

    def test_network_not_blocked(self):
        result = gate(lambda e: e["fixture"].update(network="open"))
        self.assertIn("NETWORK_NOT_BLOCKED", codes(result))

    def test_dirty_tree_needs_diff_hash(self):
        result = gate(lambda e: e["product"].update(dirty=True))
        self.assertIn("DIRTY_TREE_UNPINNED", codes(result))

        result2 = gate(
            lambda e: e["product"].update(
                dirty=True,
                worktree_diff_sha256="x",
            )
        )
        self.assertEqual(result2["computed"], "PASS")

    def test_false_engine_claim_fails(self):
        result = gate(
            lambda e: e.update(claims={"engines_used": ["huashu"]}),
            ledger={"events": []},
        )
        self.assertEqual(result["computed"], "FAIL")
        self.assertIn("FALSE_ENGINE_CLAIM", codes(result))

    def test_false_engine_claim_still_fails_without_render_capture(self):
        def mutate(evidence):
            evidence.update(
                captures=[],
                checks=[],
                claims={"engines_used": ["huashu"]},
            )

        result = gate(mutate, ledger={"events": []})
        self.assertEqual(result["computed"], "FAIL")
        self.assertIn("NO_RENDER_EVIDENCE", codes(result))
        self.assertIn("FALSE_ENGINE_CLAIM", codes(result))

    def test_engine_claim_needs_proof_not_just_flag(self):
        ledger = {
            "events": [
                {
                    "type": "engine_invoked",
                    "name": "huashu",
                    "invoked": True,
                }
            ]
        }
        result = gate(
            lambda e: e.update(claims={"engines_used": ["huashu"]}),
            ledger=ledger,
        )
        self.assertEqual(result["computed"], "FAIL")

    def test_engine_claim_with_proof_ok(self):
        ledger = {
            "events": [
                {
                    "type": "engine_invoked",
                    "name": "huashu",
                    "invoked": True,
                    "proof": {
                        "command": "huashu run x",
                        "exit_code": 0,
                    },
                }
            ]
        }
        result = gate(
            lambda e: e.update(claims={"engines_used": ["huashu"]}),
            ledger=ledger,
        )
        self.assertEqual(result["computed"], "PASS")

    def test_scope_violation_fails_unless_excepted(self):
        scope = {
            "changed_files": [
                "Sources/Views/HomeView.swift",
                "package.json",
            ],
            "denylist_globs": [
                "package.json",
                "*/routes/*",
            ],
            "exceptions": [],
        }
        result = gate(lambda e: e.update(scope=scope))
        self.assertEqual(result["computed"], "FAIL")

        excepted = dict(scope, exceptions=["package.json"])
        self.assertEqual(
            gate(lambda e: e.update(scope=excepted))["computed"],
            "PASS",
        )

    def test_judged_without_evidence_warns(self):
        result = gate(
            lambda e: e["checks"].append(
                {
                    "id": "J1",
                    "status": "judged",
                    "severity": "warning",
                    "evidence": [],
                }
            )
        )
        self.assertIn("JUDGMENT_WITHOUT_EVIDENCE", codes(result))

    def test_expected_check_missing_caps_at_warning(self):
        result = gate(lambda e: e.update(expected_checks=["C1", "C2"]))
        self.assertIn("CHECK_NOT_RUN", codes(result))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")

    def test_all_expected_checks_present_ok(self):
        result = gate(lambda e: e.update(expected_checks=["C1"]))
        self.assertEqual(result["computed"], "PASS")

    def test_pending_judgment_caps_at_warning_even_if_severity_is_warning(self):
        result = gate(
            lambda e: e["checks"].append(
                {
                    "id": "J",
                    "kind": "judgment",
                    "status": "unverifiable",
                    "severity": "warning",
                    "evidence": [],
                }
            )
        )
        self.assertIn("JUDGMENT_PENDING", codes(result))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")

    def test_judged_with_evidence_allows_pass(self):
        result = gate(
            lambda e: e["checks"].append(
                {
                    "id": "J",
                    "kind": "judgment",
                    "status": "judged",
                    "severity": "warning",
                    "evidence": ["after_top"],
                }
            )
        )
        self.assertEqual(result["computed"], "PASS")

    def test_tampered_artifact_is_invalid(self):
        directory, evidence, _ = make_run()
        with open(os.path.join(directory, "captures", "after_top.png"), "ab") as f:
            f.write(b"x")

        with self.assertRaises(vg.InvalidEvidence):
            vg.compute(evidence, None, directory)

    def test_unknown_artifact_ref_is_invalid(self):
        with self.assertRaises(vg.InvalidEvidence):
            gate(lambda e: e["checks"][0].update(evidence=["nope"]))

    def test_harness_without_philosophy_checks_warns(self):
        result = gate(lambda e: e.update(checks=[], expected_checks=[]))
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")
        self.assertIn("NO_PHILOSOPHY_CHECKS", codes(result))

    def test_human_render_without_philosophy_checks_can_pass(self):
        def mutate(e):
            e.update(
                review_mode="human_render",
                checks=[],
                expected_checks=[],
                human_review={
                    "reviewer": "design-team visual reviewer",
                    "environment": "iPhone simulator",
                    "viewport": "1206x2622",
                    "reviewed_capture_ids": ["after_top"],
                    "reviewed_areas": ["home hierarchy", "visible text clipping"],
                },
            )
        result = gate(mutate)
        self.assertEqual(result["computed"], "PASS")
        self.assertNotIn("NO_PHILOSOPHY_CHECKS", codes(result))

    def test_human_render_requires_minimum_review_record(self):
        with self.assertRaises(vg.InvalidEvidence):
            gate(lambda e: e.update(review_mode="human_render", checks=[], human_review={}))

    def test_stale_philosophy_checks_warn(self):
        result = gate(
            lambda e: e.update(
                philosophy={
                    "source_doc": "docs/design.md",
                    "compiled_doc_sha256": "old",
                    "current_doc_sha256": "new",
                }
            )
        )
        self.assertEqual(result["computed"], "PASS_WITH_WARNING")
        self.assertIn("CHECKS_STALE", codes(result))

    def test_fresh_philosophy_checks_do_not_warn(self):
        result = gate(
            lambda e: e.update(
                philosophy={
                    "source_doc": "docs/design.md",
                    "compiled_doc_sha256": "same",
                    "current_doc_sha256": "same",
                }
            )
        )
        self.assertEqual(result["computed"], "PASS")
        self.assertNotIn("CHECKS_STALE", codes(result))

    def test_gate_fields_exist_in_evidence_schema(self):
        schema_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "skills",
            "design-team",
            "schemas",
            "evidence.schema.json",
        )
        with open(os.path.abspath(schema_path), encoding="utf-8") as f:
            schema = __import__("json").load(f)
        self.assertTrue(vg.GATE_EVIDENCE_FIELDS.issubset(set(schema["properties"])))
        self.assertIn("review_mode", schema["required"])


def dump(elements, complete, viewport_h=2622):
    return {
        "artifact_id": "dump_home",
        "dump": {
            "complete": complete,
            "viewport": {"w": 1206, "h": viewport_h},
            "elements": elements,
        },
    }


def element(role, y, height):
    return {
        "role": role,
        "frame": {
            "x": 0,
            "y": y,
            "w": 1206,
            "h": height,
        },
    }


ORDER = {
    "id": "O",
    "kind": "order",
    "scope": {"screen": "home"},
    "severity": "blocker",
    "assert": {
        "order": [
            "goal_progress",
            "today_workout",
            "monthly_summary",
        ]
    },
}


class CheckTests(unittest.TestCase):
    def run1(self, check, data):
        return cr.run_one(check, {"home": data})

    def test_order_pass(self):
        data = dump(
            [
                element("goal_progress", 100, 500),
                element("today_workout", 700, 500),
                element("monthly_summary", 1300, 400),
            ],
            True,
        )
        self.assertEqual(self.run1(ORDER, data)["status"], "pass")

    def test_order_fail(self):
        data = dump(
            [
                element("goal_progress", 100, 500),
                element("monthly_summary", 700, 400),
                element("today_workout", 1200, 500),
            ],
            True,
        )
        result = self.run1(ORDER, data)
        self.assertEqual(result["status"], "fail")
        self.assertIn("actual", result["detail"])

    def test_missing_role_incomplete_dump_is_unverifiable_not_fail(self):
        data = dump(
            [
                element("goal_progress", 100, 500),
                element("monthly_summary", 700, 400),
            ],
            False,
        )
        self.assertEqual(
            self.run1(ORDER, data)["status"],
            "unverifiable",
        )

    def test_missing_role_complete_dump_is_fail(self):
        data = dump(
            [
                element("goal_progress", 100, 500),
                element("monthly_summary", 700, 400),
            ],
            True,
        )
        self.assertEqual(self.run1(ORDER, data)["status"], "fail")

    def test_first_viewport(self):
        check = {
            "id": "V",
            "kind": "first_viewport",
            "scope": {"screen": "home"},
            "assert": {
                "role": "today_workout",
                "min_visible_ratio": 0.3,
            },
        }
        below = dump([element("today_workout", 2500, 500)], True)
        self.assertEqual(self.run1(check, below)["status"], "fail")

        near = dump([element("today_workout", 2200, 500)], True)
        self.assertEqual(self.run1(check, near)["status"], "pass")

    def test_absence(self):
        check = {
            "id": "A",
            "kind": "absence",
            "scope": {"screen": "home"},
            "assert": {"roles": ["fake_metric"]},
        }
        self.assertEqual(
            self.run1(
                check,
                dump([element("fake_metric", 0, 10)], False),
            )["status"],
            "fail",
        )
        self.assertEqual(
            self.run1(check, dump([], False))["status"],
            "unverifiable",
        )
        self.assertEqual(
            self.run1(check, dump([], True))["status"],
            "pass",
        )

    def test_unknown_kind_raises(self):
        with self.assertRaises(ValueError):
            cr.run_one(
                {
                    "id": "x",
                    "kind": "vibes",
                    "scope": {"screen": "home"},
                },
                {"home": dump([], True)},
            )

    def test_sample_yaml_loads_and_kinds_valid(self):
        doc = cr.load_checks(
            os.path.join(
                os.path.dirname(__file__),
                "philosophy.checks.sample.yaml",
            )
        )
        self.assertTrue(
            all(check["kind"] in cr.KINDS for check in doc["checks"])
        )
        self.assertEqual(
            len({check["id"] for check in doc["checks"]}),
            len(doc["checks"]),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
