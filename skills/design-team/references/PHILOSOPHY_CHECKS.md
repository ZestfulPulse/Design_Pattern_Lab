# Philosophy Checks

DPL can translate a small subset of product philosophy into machine-checkable rules.

The goal is not to turn taste into pseudo-math. Only objectively testable claims should become automatic checks.

## Rule classes

| Kind | Suitable claim | Typical evidence |
|---|---|---|
| `order` | elements must appear in a specific vertical order | normalized layout/accessibility frames |
| `first_viewport` | an element must be sufficiently visible without scrolling | frame vs viewport |
| `presence` | required elements must render | complete layout/accessibility dump |
| `absence` | forbidden elements must not render | complete layout/accessibility dump |
| `judgment` | a qualitative principle that cannot be mechanically asserted | rendered evidence + explicit rationale |

## Compile procedure

1. Read the product-owned philosophy/design source.
2. Extract only statements that express order, required presence, prohibited presence, or another objectively testable condition.
3. Classify non-mechanical principles as `judgment` instead of pretending they are automatic checks.
4. Record `source_ref` for every rule.
5. Record the source document SHA-256 so stale rules can be detected later.
6. If creating or materially changing checks requires interpretation of the product philosophy, show the rule list once for approval before treating it as authoritative.

The approval is for the interpretation, not for every future run.

## Product instrumentation

Prefer existing accessibility labels/identifiers and semantic hooks.

If reliable checking requires adding identifiers such as iOS `accessibilityIdentifier` or web `data-dpl-role`, treat that as a one-time DPL setup change in the product repository. Do not silently add instrumentation when the requested design scope does not authorize source changes of that kind.

## Assumptions

If the product philosophy is silent on a decision that materially affects the design, record the assumption rather than presenting it as product truth.

Open assumptions may guide exploration but should not become blocker-level philosophy checks until approved or promoted into the product's own source of truth.

See `templates/ASSUMPTIONS.yaml`.

## Freshness

Structured evidence should carry both the hash recorded when the checks were compiled and the current authoritative document hash:

```json
{
  "philosophy": {
    "source_doc": "docs/product-design.md",
    "compiled_doc_sha256": "...",
    "current_doc_sha256": "..."
  }
}
```

If the two hashes differ, the verdict gate records `CHECKS_STALE` and caps the result at `PASS_WITH_WARNING`. A stale check set may still be useful as a warning signal, but it must not support an unqualified `PASS`.
