import json
import os
import unittest

import pattern_selector as ps


def catalog():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "skills",
        "design-team",
        "patterns",
        "web-patterns.json",
    )
    with open(os.path.abspath(path), encoding="utf-8") as f:
        return json.load(f)


class PatternSelectorTests(unittest.TestCase):
    def test_platform_mismatch_rejected(self):
        profile = {
            "platform": "ios",
            "product_type": "developer_tool",
            "needs": ["technical"],
            "traits": {"precision": 5},
        }
        ranked = ps.rank_patterns(profile, catalog(), 20)
        self.assertTrue(all("web" not in item["id"] for item in ranked))
        self.assertEqual([x["id"] for x in ranked], [
            "design-first-ui-prompting",
            "audit-reference-originality",
        ])

    def test_technical_web_prefers_editorial_or_framed(self):
        profile = {
            "platform": "web",
            "product_type": "developer_tool",
            "needs": ["technical", "editorial", "structured"],
            "traits": {
                "precision": 5,
                "minimal": 4,
                "editorial": 5,
                "playful": 1,
                "warmth": 2,
                "motion": 1,
            },
        }
        ids = [x["id"] for x in ps.rank_patterns(profile, catalog(), 3)]
        self.assertIn("editorial-tech", ids)
        self.assertIn("framed-tech-dark-border-gradient", ids)

    def test_avoid_penalty_demotes_cinematic_for_low_motion(self):
        profile = {
            "platform": "web",
            "product_type": "marketing",
            "needs": ["cinematic", "low_motion"],
            "traits": {"motion": 1},
        }
        ranked = ps.rank_patterns(profile, catalog(), 20)
        scores = {x["id"]: x["score"] for x in ranked}
        self.assertLess(
            scores["build-awwwards-quality-sites"],
            scores["landing-page"],
        )

    def test_catalog_schema_required(self):
        with self.assertRaises(ValueError):
            ps.rank_patterns({}, {"schema": "wrong", "patterns": []})


if __name__ == "__main__":
    unittest.main(verbosity=2)
