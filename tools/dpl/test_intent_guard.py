import os
import tempfile
import unittest

import intent_guard as ig


def valid_contract():
    return {
        "version": 1,
        "product": {
            "name": "Example",
            "platform": "web",
            "product_type": "developer_tool",
            "audience": "operators",
            "job_to_be_done": "understand system state",
            "identity_statement": "precise, calm operational tool",
            "success_definition": "critical state is understood quickly",
        },
        "source_docs": [{"path": "docs/product.md", "sha256": "abc"}],
        "principles": [
            {
                "id": "P-01",
                "statement": "critical state before secondary statistics",
                "source_ref": "docs/product.md#priority",
                "provenance": "explicit",
                "strength": "must",
                "implications": {
                    "structure": ["critical state first"],
                    "visual": ["strong primary hierarchy"],
                    "interaction": [],
                    "content": [],
                },
            }
        ],
        "tensions": [],
        "must_preserve": [],
        "pattern_profile": {
            "platform": "web",
            "product_type": "developer_tool",
            "needs": ["technical"],
            "traits": {"precision": 5, "minimal": 4},
        },
        "decisions": [
            {
                "id": "D-01",
                "change": "move critical status to first section",
                "supports": ["P-01"],
                "rationale": "matches explicit product priority",
            }
        ],
    }


class IntentGuardTests(unittest.TestCase):
    def test_valid_contract(self):
        self.assertEqual(ig.validate(valid_contract()), [])

    def test_inferred_must_warns(self):
        c = valid_contract()
        c["principles"][0]["provenance"] = "inferred"
        warnings = ig.validate(c)
        self.assertEqual(warnings[0]["code"], "INFERRED_MUST")

    def test_unknown_decision_principle_fails(self):
        c = valid_contract()
        c["decisions"][0]["supports"] = ["P-999"]
        with self.assertRaises(ig.ContractError):
            ig.validate(c)

    def test_ungrounded_decision_warns(self):
        c = valid_contract()
        c["decisions"][0]["supports"] = []
        warnings = ig.validate(c)
        self.assertEqual(warnings[0]["code"], "UNGROUNDED_DECISION")

    def test_trait_out_of_range_fails(self):
        c = valid_contract()
        c["pattern_profile"]["traits"]["precision"] = 6
        with self.assertRaises(ig.ContractError):
            ig.validate(c)

    def test_profile_emits_selector_shape(self):
        profile = ig.pattern_profile(valid_contract())
        self.assertEqual(profile["platform"], "web")
        self.assertEqual(profile["product_type"], "developer_tool")
        self.assertIn("traits", profile)


if __name__ == "__main__":
    unittest.main(verbosity=2)
