#!/usr/bin/env python3
"""DPL Product Intent Guard.

Validates philosophy-to-design contracts and emits the Pattern Selector profile.
It verifies traceability and contract hygiene, not subjective design correctness.
"""
import argparse
import json
import sys
import yaml

PROVENANCE = {"explicit", "inferred", "approved_assumption"}
STRENGTH = {"must", "prefer", "avoid"}


class ContractError(ValueError):
    pass


def _require(condition, message):
    if not condition:
        raise ContractError(message)


def validate(contract):
    _require(contract.get("version") == 1, "unsupported product-intent version")
    product = contract.get("product") or {}
    for key in (
        "name", "platform", "product_type", "audience", "job_to_be_done",
        "identity_statement", "success_definition"
    ):
        _require(key in product, "product missing '%s'" % key)

    source_docs = contract.get("source_docs")
    _require(isinstance(source_docs, list), "source_docs must be a list")
    for doc in source_docs:
        _require(doc.get("path"), "source doc missing path")
        _require(doc.get("sha256"), "source doc missing sha256")

    principles = contract.get("principles") or []
    _require(principles, "at least one principle is required")
    ids = [p.get("id") for p in principles]
    _require(all(ids), "principle missing id")
    _require(len(ids) == len(set(ids)), "duplicate principle id")

    warnings = []
    known = set(ids)
    for p in principles:
        _require(p.get("statement"), "%s missing statement" % p["id"])
        _require(p.get("source_ref"), "%s missing source_ref" % p["id"])
        _require(p.get("provenance") in PROVENANCE, "%s invalid provenance" % p["id"])
        _require(p.get("strength") in STRENGTH, "%s invalid strength" % p["id"])
        implications = p.get("implications") or {}
        for layer in ("structure", "visual", "interaction", "content"):
            _require(isinstance(implications.get(layer), list), "%s implications.%s must be a list" % (p["id"], layer))
        if p.get("strength") == "must" and p.get("provenance") == "inferred":
            warnings.append({
                "code": "INFERRED_MUST",
                "principle": p["id"],
                "message": "durable must rule is inferred; seek approval or downgrade"
            })

    profile = contract.get("pattern_profile") or {}
    _require(profile.get("platform"), "pattern_profile.platform required")
    _require("product_type" in profile, "pattern_profile.product_type required")
    _require(isinstance(profile.get("needs"), list), "pattern_profile.needs must be a list")
    traits = profile.get("traits") or {}
    for name, value in traits.items():
        _require(isinstance(value, (int, float)) and not isinstance(value, bool), "trait %s must be numeric" % name)
        _require(0 <= value <= 5, "trait %s must be between 0 and 5" % name)

    for decision in contract.get("decisions", []):
        _require(decision.get("id"), "decision missing id")
        _require(decision.get("change"), "%s missing change" % decision["id"])
        _require("supports" in decision and isinstance(decision["supports"], list), "%s supports must be a list" % decision["id"])
        _require(decision.get("rationale"), "%s missing rationale" % decision["id"])
        unknown = sorted(set(decision["supports"]) - known)
        _require(not unknown, "%s cites unknown principles: %s" % (decision["id"], ", ".join(unknown)))
        if not decision["supports"]:
            warnings.append({
                "code": "UNGROUNDED_DECISION",
                "decision": decision["id"],
                "message": "decision has no supporting philosophy principle; justify as user instruction, platform convention, or usability repair"
            })

    tensions = contract.get("tensions") or []
    for tension in tensions:
        if isinstance(tension, dict) and not tension.get("resolution"):
            warnings.append({
                "code": "UNRESOLVED_TENSION",
                "tension": tension.get("id", ""),
                "message": "product-principle tension has no resolution"
            })

    return warnings


def pattern_profile(contract):
    validate(contract)
    profile = dict(contract["pattern_profile"])
    if not profile.get("platform"):
        profile["platform"] = contract["product"]["platform"]
    if not profile.get("product_type"):
        profile["product_type"] = contract["product"]["product_type"]
    return profile


def load(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ContractError("product-intent document must be an object")
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate DPL product-intent contract")
    parser.add_argument("--intent", required=True)
    parser.add_argument("--profile", action="store_true", help="emit Pattern Selector profile")
    args = parser.parse_args(argv)
    try:
        contract = load(args.intent)
        warnings = validate(contract)
        result = {
            "schema": "dpl.intent-validation/1",
            "valid": True,
            "warnings": warnings,
        }
        if args.profile:
            result["pattern_profile"] = pattern_profile(contract)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ContractError, OSError, yaml.YAMLError) as exc:
        print(json.dumps({
            "schema": "dpl.intent-validation/1",
            "valid": False,
            "error": str(exc),
        }, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    sys.exit(main())
