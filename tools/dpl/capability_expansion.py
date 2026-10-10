"""Bounded DPL capability-expansion contracts.

External sources remain references. This module owns only DPL's normalized
research, Taste gate, and implementation-admission decisions.
"""

from dataclasses import dataclass
from typing import Any


REFERENCE_LOCK_FIELDS = (
    "PRIMARY_REFERENCE",
    "PRESERVE_TRAITS",
    "BORROWED_DETAILS",
    "REJECTED_PATTERNS",
    "PRODUCT_TRANSLATION",
)
TASTE_VERDICTS = {
    "TASTE_PASS",
    "TASTE_PASS_WITH_WARNING",
    "TASTE_REJECT",
}
DPL_SOURCE_REGISTRY = {
    "taste_skill": {
        "url": "https://github.com/Leonxlnx/taste-skill",
        "role": "taste-critic",
        "scope": "reference-adapter",
    },
    "refs_gallery": {
        "url": "https://refs.gallery/",
        "role": "site-level-reference-research",
        "scope": "site-level",
    },
    "refero": {
        "role": "screen-level-reference-research",
        "scope": "screen-level",
    },
    "velora_ui": {
        "url": "https://github.com/ColorlibHQ/velora-ui",
        "role": "component-motion-candidate",
        "scope": "resolver-candidate",
    },
    "heroicons_animated": {
        "url": "https://github.com/heroicons-animated/heroicons-animated",
        "role": "micro-interaction-asset",
        "scope": "semantic-asset",
    },
}


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...] = ()


def make_reference_lock(
    *,
    primary_reference: str,
    preserve_traits: list[str],
    borrowed_details: list[str],
    rejected_patterns: list[str],
    product_translation: str,
) -> dict[str, Any]:
    return {
        "PRIMARY_REFERENCE": primary_reference,
        "PRESERVE_TRAITS": list(preserve_traits),
        "BORROWED_DETAILS": list(borrowed_details),
        "REJECTED_PATTERNS": list(rejected_patterns),
        "PRODUCT_TRANSLATION": product_translation,
    }


def validate_reference_lock(lock: dict[str, Any]) -> ValidationResult:
    errors = []
    for field in REFERENCE_LOCK_FIELDS:
        if field not in lock:
            errors.append("missing field: %s" % field)
    if "PRIMARY_REFERENCE" in lock and not isinstance(lock["PRIMARY_REFERENCE"], str):
        errors.append("PRIMARY_REFERENCE must be a string")
    for field in ("PRESERVE_TRAITS", "BORROWED_DETAILS", "REJECTED_PATTERNS"):
        if field in lock and not isinstance(lock[field], list):
            errors.append("%s must be a list" % field)
    if "PRODUCT_TRANSLATION" in lock and not isinstance(lock["PRODUCT_TRANSLATION"], str):
        errors.append("PRODUCT_TRANSLATION must be a string")
    return ValidationResult(not errors, tuple(errors))


def _reference_items(values: list[str], scope: str, role: str) -> list[dict[str, str]]:
    return [{"reference": value, "scope": scope, "role": role} for value in values]


def build_reference_research(
    *, refs_gallery: list[str], refero: list[str], user_supplied: list[str]
) -> dict[str, list[dict[str, str]]]:
    return {
        "refs_gallery": _reference_items(
            refs_gallery, "site-level", "visual direction/storytelling/interaction/typography/composition"
        ),
        "refero": _reference_items(
            refero, "screen-level", "component/UX pattern/interaction state/flow"
        ),
        "user_supplied": _reference_items(user_supplied, "user-supplied", "explicit reference input"),
    }


def evaluate_taste(observations: dict[str, Any]) -> dict[str, Any]:
    reject_reasons: list[str] = []
    warnings: list[str] = []

    if observations.get("generic_ai_saas"):
        reject_reasons.append("generic AI/SaaS convergence")
    for key, label in (
        ("typography_reasoned", "typography lacks rationale"),
        ("layout_derived", "layout family is not product-derived"),
        ("color_intentional", "color selection is unintentional"),
        ("mobile_logic_consistent", "mobile design logic is inconsistent"),
    ):
        value = observations.get(key)
        if value is False:
            reject_reasons.append(label)
        elif value is None:
            warnings.append(label)

    excessive = observations.get("excessive_patterns") or []
    if excessive:
        warnings.append("excessive patterns: %s" % ", ".join(excessive))
    if observations.get("decorative_interaction"):
        reject_reasons.append("interaction is decorative rather than product-relevant")

    if reject_reasons:
        verdict = "TASTE_REJECT"
    elif warnings:
        verdict = "TASTE_PASS_WITH_WARNING"
    else:
        verdict = "TASTE_PASS"
    return {
        "verdict": verdict,
        "reject_reasons": reject_reasons,
        "warnings": warnings,
    }


def implementation_allowed(review: dict[str, Any]) -> bool:
    return review.get("verdict") in {"TASTE_PASS", "TASTE_PASS_WITH_WARNING"}


def resolve_velora_candidate(
    decision: dict[str, Any], candidate: dict[str, Any]
) -> dict[str, Any]:
    required = (
        "design_decision",
        "interaction_requirement",
        "product_fit",
        "reduced_motion_checked",
        "keyboard_checked",
        "mobile_touch_checked",
        "accessibility_checked",
    )
    missing = [field for field in required if not decision.get(field)]
    requirement = str(decision.get("interaction_requirement", "")).lower()
    if "decorative" in requirement or "make it prettier" in str(
        decision.get("design_decision", "")
    ).lower():
        missing.append("non-decorative interaction rationale")
    if missing:
        return {"status": "REJECTED", "reasons": missing, "candidate": candidate}
    return {
        "status": "CANDIDATE",
        "reasons": [],
        "candidate": candidate,
        "automatic_use": False,
    }


def validate_heroicon_motion(observation: dict[str, Any]) -> dict[str, Any]:
    allowed = {"action feedback", "state transition", "confirmation", "direction/navigation", "loading/progress"}
    meaning = observation.get("meaning")
    reasons = []
    if meaning not in allowed:
        reasons.append("meaning is not an approved semantic interaction")
    if observation.get("continuous"):
        reasons.append("continuous decorative animation is prohibited")
    if observation.get("static_icon_preferred"):
        reasons.append("static icon is preferred")
    for field in ("reduced_motion_checked", "keyboard_checked", "mobile_touch_checked", "accessibility_checked"):
        if not observation.get(field):
            reasons.append("missing check: %s" % field)
    return {
        "status": "REJECTED" if reasons else "ALLOWED",
        "reasons": reasons,
        "asset_role": "micro-interaction-asset",
    }
