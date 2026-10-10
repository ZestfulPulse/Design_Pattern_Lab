import unittest

import capability_expansion as ce


class PhaseAContractTests(unittest.TestCase):
    def test_opendots_is_not_a_dpl_source(self):
        self.assertNotIn("opendots", ce.DPL_SOURCE_REGISTRY)
        self.assertEqual(ce.DPL_SOURCE_REGISTRY["refs_gallery"]["scope"], "site-level")

    def test_reference_lock_requires_all_translation_fields(self):
        lock = ce.make_reference_lock(
            primary_reference="refs.gallery/project/example",
            preserve_traits=["editorial pacing"],
            borrowed_details=["section rhythm"],
            rejected_patterns=["single-site cloning"],
            product_translation="Use pacing for the product's own evidence flow.",
        )
        self.assertEqual(
            set(lock),
            {
                "PRIMARY_REFERENCE",
                "PRESERVE_TRAITS",
                "BORROWED_DETAILS",
                "REJECTED_PATTERNS",
                "PRODUCT_TRANSLATION",
            },
        )
        self.assertTrue(ce.validate_reference_lock(lock).valid)

    def test_reference_research_separates_site_and_screen_roles(self):
        research = ce.build_reference_research(
            refs_gallery=["https://refs.gallery/projects/example"],
            refero=["screen:settings/preferences"],
            user_supplied=[],
        )
        self.assertEqual(research["refs_gallery"][0]["scope"], "site-level")
        self.assertEqual(research["refero"][0]["scope"], "screen-level")
        self.assertNotEqual(research["refs_gallery"][0]["scope"], research["refero"][0]["scope"])

    def test_taste_reject_blocks_implementation(self):
        review = ce.evaluate_taste(
            {
                "generic_ai_saas": True,
                "typography_reasoned": False,
                "layout_derived": False,
                "color_intentional": False,
                "excessive_patterns": ["bento", "gradient"],
                "decorative_interaction": True,
                "mobile_logic_consistent": False,
            }
        )
        self.assertEqual(review["verdict"], "TASTE_REJECT")
        self.assertFalse(ce.implementation_allowed(review))

    def test_taste_warning_allows_implementation_with_warning(self):
        review = ce.evaluate_taste(
            {
                "generic_ai_saas": False,
                "typography_reasoned": True,
                "layout_derived": True,
                "color_intentional": True,
                "excessive_patterns": [],
                "decorative_interaction": False,
                "mobile_logic_consistent": None,
            }
        )
        self.assertEqual(review["verdict"], "TASTE_PASS_WITH_WARNING")
        self.assertTrue(ce.implementation_allowed(review))

    def test_clean_taste_pass(self):
        review = ce.evaluate_taste(
            {
                "generic_ai_saas": False,
                "typography_reasoned": True,
                "layout_derived": True,
                "color_intentional": True,
                "excessive_patterns": [],
                "decorative_interaction": False,
                "mobile_logic_consistent": True,
            }
        )
        self.assertEqual(review["verdict"], "TASTE_PASS")

    def test_velora_requires_decision_and_interaction_requirement(self):
        self.assertEqual(
            ce.resolve_velora_candidate({}, {"id": "button"})["status"],
            "REJECTED",
        )
        accepted = ce.resolve_velora_candidate(
            {
                "design_decision": "compact action feedback",
                "interaction_requirement": "show save completion without text shift",
                "product_fit": True,
                "reduced_motion_checked": True,
                "keyboard_checked": True,
                "mobile_touch_checked": True,
                "accessibility_checked": True,
            },
            {"id": "animated-save-button"},
        )
        self.assertEqual(accepted["status"], "CANDIDATE")

    def test_velora_rejects_decorative_only_rationale(self):
        result = ce.resolve_velora_candidate(
            {
                "design_decision": "make it prettier",
                "interaction_requirement": "decorative glow",
                "product_fit": True,
            },
            {"id": "glow"},
        )
        self.assertEqual(result["status"], "REJECTED")

    def test_heroicon_policy_requires_semantic_meaning_and_motion_checks(self):
        rejected = ce.validate_heroicon_motion(
            {"meaning": "decoration", "continuous": True, "reduced_motion_checked": True}
        )
        self.assertEqual(rejected["status"], "REJECTED")
        accepted = ce.validate_heroicon_motion(
            {
                "meaning": "confirmation",
                "continuous": False,
                "static_icon_preferred": False,
                "reduced_motion_checked": True,
                "keyboard_checked": True,
                "mobile_touch_checked": True,
                "accessibility_checked": True,
            }
        )
        self.assertEqual(accepted["status"], "ALLOWED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
