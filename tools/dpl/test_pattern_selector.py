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


def native_catalog():
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "skills",
        "design-team",
        "patterns",
        "native-patterns.json",
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
        self.assertEqual(
            {x["id"] for x in ranked},
            {"design-first-ui-prompting", "audit-reference-originality"},
        )

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

    def test_ios_native_profile_prefers_correctness_and_hig(self):
        profile = {
            "platform": "ios",
            "product_type": "fitness",
            "needs": ["swiftui", "state_stability", "adaptive_layout", "accessibility"],
            "traits": {
                "native_fidelity": 5,
                "interaction_rigor": 5,
                "accessibility": 5,
                "adaptability": 5,
                "visual_expression": 2,
                "motion_intensity": 2,
                "information_density": 3,
            },
        }
        ids = [x["id"] for x in ps.rank_patterns(profile, native_catalog(), 3)]
        self.assertIn("design-swiftui-interfaces", ids)
        self.assertIn("apple-hig", ids)

    def test_native_visual_expression_can_surface_visual_specialist(self):
        profile = {
            "platform": "ios",
            "product_type": "consumer_app",
            "needs": ["swiftui", "visual_direction", "tokens", "distinctive_ui"],
            "traits": {
                "native_fidelity": 4,
                "interaction_rigor": 3,
                "accessibility": 4,
                "adaptability": 4,
                "visual_expression": 5,
                "motion_intensity": 4,
                "information_density": 2,
            },
        }
        ids = [x["id"] for x in ps.rank_patterns(profile, native_catalog(), 2)]
        self.assertIn("swift-ui-design", ids)

    def test_catalog_schema_required(self):
        with self.assertRaises(ValueError):
            ps.rank_patterns({}, {"schema": "wrong", "patterns": []})


if __name__ == "__main__":
    unittest.main(verbosity=2)
