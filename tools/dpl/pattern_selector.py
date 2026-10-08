#!/usr/bin/env python3
"""DPL Pattern Selector.

Ranks inspected pattern metadata against a product profile.
This is a candidate-reading aid, not a design authority.
"""
import argparse
import json
import math

CATALOG_SCHEMA = "dpl.pattern-catalog/1"


def _clamp_trait(value):
    value = float(value)
    return max(0.0, min(5.0, value))


def score_pattern(profile, pattern):
    platform = profile.get("platform")
    platforms = set(pattern.get("platforms", []))
    if platform and platform not in platforms:
        return None

    score = 0.0
    reasons = []

    product_type = profile.get("product_type")
    if product_type and product_type in pattern.get("product_types", []):
        score += 25
        reasons.append("product_type_match")

    needs = set(profile.get("needs", []))
    pneeds = set(pattern.get("needs", []))
    overlap = sorted(needs & pneeds)
    if overlap:
        add = min(30, 10 * len(overlap))
        score += add
        reasons.append("needs:" + ",".join(overlap))

    avoid_hits = sorted(needs & set(pattern.get("avoid", [])))
    if avoid_hits:
        score -= 40 * len(avoid_hits)
        reasons.append("avoid:" + ",".join(avoid_hits))

    traits = profile.get("traits", {})
    ptr = pattern.get("traits", {})
    comparable = sorted(set(traits) & set(ptr))
    if comparable:
        distance = sum(
            abs(_clamp_trait(traits[k]) - _clamp_trait(ptr[k]))
            for k in comparable
        ) / len(comparable)
        similarity = max(0.0, 1.0 - distance / 5.0)
        score += 40.0 * similarity
        reasons.append("trait_similarity:%.2f" % similarity)

    return {
        "id": pattern["id"],
        "source": pattern.get("source"),
        "score": round(score, 2),
        "reasons": reasons,
    }


def rank_patterns(profile, catalog, limit=5):
    if catalog.get("schema") != CATALOG_SCHEMA:
        raise ValueError("unsupported pattern catalog schema")
    ranked = []
    for pattern in catalog.get("patterns", []):
        result = score_pattern(profile, pattern)
        if result is not None:
            ranked.append(result)
    ranked.sort(key=lambda x: (-x["score"], x["id"]))
    return ranked[:limit]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rank DPL implementation patterns")
    parser.add_argument("--profile", required=True, help="product profile JSON")
    parser.add_argument("--catalog", required=True, help="pattern catalog JSON")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args(argv)

    with open(args.profile, encoding="utf-8") as f:
        profile = json.load(f)
    with open(args.catalog, encoding="utf-8") as f:
        catalog = json.load(f)

    result = {
        "schema": "dpl.pattern-ranking/1",
        "candidates": rank_patterns(profile, catalog, args.limit),
        "note": "ranking suggests which references to inspect; product truth remains authoritative",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
