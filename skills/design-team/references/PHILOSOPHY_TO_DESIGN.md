# Philosophy-to-Design Contract

This module turns product philosophy into an explicit design contract before exploration or implementation.

It does **not** invent product truth. It structures what the product already says and clearly labels inference.

## Purpose

A philosophy document is often too abstract to drive implementation directly.

For example:

```text
"Precise personal running analysis, not a generic fitness app."
```

needs to become design consequences such as:

```text
structure:
- prioritize personal performance gap before broad activity summaries
- keep analytical evidence close to recommendations

visual:
- precise, restrained hierarchy
- avoid generic wellness decoration

interaction:
- feedback should feel instrumental, not playful for its own sake
```

The contract makes that translation explicit and reviewable.

## Pipeline

```text
Authoritative product sources
  ↓
Extract explicit principles
  ↓
Separate inference from source truth
  ↓
Translate principles into implications
  ├─ structure
  ├─ visual
  ├─ interaction
  └─ content
  ↓
Resolve tensions / record assumptions
  ↓
Build product profile for Pattern Selector
  ↓
Explore / implement
  ↓
Trace design decisions back to principle IDs
  ↓
Verify
```

## Source discipline

Every principle must carry:

- `id`
- `statement`
- `source_ref`
- `provenance`: `explicit`, `inferred`, or `approved_assumption`
- `strength`: `must`, `prefer`, or `avoid`
- design implications

Rules:

1. `explicit` means the source directly supports the principle.
2. `inferred` means Design Team derived it from product evidence. It must never be presented as quoted product truth.
3. `approved_assumption` means a previously inferred rule was approved by the user/product owner.
4. A durable `must` rule should normally be explicit or approved, not merely inferred.
5. Conflicting principles must be surfaced in `tensions`, not silently averaged.

## Design implication layers

### Structure

Translate philosophy into information architecture:

- what appears first;
- what is grouped together;
- what is secondary;
- what may be omitted;
- what should remain persistent;
- what should be progressive disclosure.

### Visual language

Translate philosophy into:

- hierarchy;
- typography character;
- density;
- semantic color roles;
- surface/material treatment;
- imagery;
- iconography;
- visual restraint or expressiveness.

Avoid converting adjectives directly into trendy styles. "Premium" does not automatically mean dark glass. "Technical" does not automatically mean monospace everywhere.

### Interaction

Translate philosophy into:

- directness;
- feedback latency;
- motion character;
- gesture vocabulary;
- interruption/reversibility;
- haptics where platform-appropriate;
- error recovery.

### Content

Translate philosophy into:

- tone;
- terminology;
- evidence/claim requirements;
- amount of explanation;
- prohibited generic or unsupported language.

## Product profile

The contract includes a small `pattern_profile` used by Pattern Selector:

- platform
- product_type
- needs
- traits scored 0–5

This profile is **derived** from the contract. It is not a new source of product truth.

`tools/dpl/intent_guard.py --profile` can emit the profile for Pattern Selector.

## Decision trace

Meaningful design decisions should record which principle IDs they support.

Example:

```yaml
decisions:
  - id: D-01
    change: "Move goal progress above monthly summary"
    supports: [P-01, P-03]
    rationale: "The product prioritizes actionable personal performance gap over retrospective totals."
```

A decision with no supporting principle is not automatically wrong, but it is **ungrounded** and must be justified as platform convention, usability repair, or user instruction.

## Verification

`tools/dpl/intent_guard.py` checks:

- required contract fields;
- unique principle IDs;
- principle provenance and strength;
- source references;
- `must` rules that are only inferred;
- decision references to unknown principles;
- ungrounded meaningful decisions;
- unresolved tensions;
- valid 0–5 pattern traits.

It does not judge whether prose interpretation is philosophically correct. That remains a Design Team/user-review responsibility.

Use [PRODUCT_INTENT.yaml](../templates/PRODUCT_INTENT.yaml) as the starting point.
