import json
import os
import unittest
import xml.etree.ElementTree as ET

import yaml


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CASE = os.path.join(ROOT, "showcase", "02-legs-of-steel-controlled-native")


class Showcase02Tests(unittest.TestCase):
    def test_fixture_has_identical_before_after_source(self):
        with open(os.path.join(CASE, "fixture.json"), encoding="utf-8") as f:
            fixture = json.load(f)
        self.assertEqual(fixture["schema"], "dpl.showcase-fixture/1")
        self.assertEqual(fixture["dataset"]["monthly_distance_km"], 24.0)
        self.assertEqual(fixture["dataset"]["activity_count"], 5)
        self.assertEqual(fixture["dataset"]["goal_gap_minutes"], 12)

    def test_product_intent_is_traceable(self):
        with open(os.path.join(CASE, "product-intent.yaml"), encoding="utf-8") as f:
            intent = yaml.safe_load(f)
        principle_ids = {p["id"] for p in intent["principles"]}
        self.assertEqual(principle_ids, {"P-01", "P-02"})
        for decision in intent["decisions"]:
            self.assertTrue(set(decision["supports"]).issubset(principle_ids))
        self.assertEqual(intent["pattern_profile"]["platform"], "ios")

    def test_exploration_selects_goal_led_direction(self):
        with open(os.path.join(CASE, "exploration-board.yaml"), encoding="utf-8") as f:
            board = yaml.safe_load(f)
        self.assertEqual(board["selection"]["selected"], "B")
        chosen = next(x for x in board["directions"] if x["id"] == "B")
        self.assertGreater(chosen["scores"]["philosophy_fit"], 4)

    def test_svg_artifacts_are_valid_and_show_same_fixture_values(self):
        required = ["24.0 km", "5 activities", "4:12:00"]
        for name in ("before.svg", "after.svg"):
            path = os.path.join(CASE, name)
            ET.parse(path)
            with open(path, encoding="utf-8") as f:
                content = f.read()
            for value in required:
                self.assertIn(value, content)

    def test_after_shows_complete_intended_order(self):
        with open(os.path.join(CASE, "after.svg"), encoding="utf-8") as f:
            content = f.read()
        goal = content.index("GOAL GAP")
        training = content.index("TODAY'S TRAINING")
        stats = content.index("SUPPORTING STATISTICS")
        self.assertLess(goal, training)
        self.assertLess(training, stats)


if __name__ == "__main__":
    unittest.main(verbosity=2)
