# Evidence and Verdict Contract

DPL treats a design verdict as a claim that must be bounded by evidence.

This contract strengthens the existing rule that build/lint success is not visual QA. It does not make the internal tools mandatory for every design pass, and it does not replace human visual judgment.

## Verdict states

- `PASS` — the requested design scope was verified with sufficient rendered evidence.
- `PASS_WITH_WARNING` — the main goal is supported, but relevant evidence, coverage, comparability, or judgment is incomplete.
- `FAIL` — a required design check failed, a scope boundary was violated, or a provenance claim is false.
- `NOT_VERIFIED` — there is no rendered evidence sufficient to assess the visual result.

`NOT_VERIFIED` means "not enough evidence to judge", not "the design is bad".

## Important boundary

The absence of the DPL evidence harness does **not** automatically mean `NOT_VERIFIED`.

If Design Team has real rendered evidence such as simulator screenshots, browser captures, device output, or another inspectable render and performs an explicit Visual Release Review, the existing evidence-based verdict path remains valid.

The structured harness is a stronger, machine-checkable path when available. It is not the only legitimate source of rendered evidence.

## Structured evidence path

When a product uses `.dpl/`, keep derived artifacts only:

```text
<product-repo>/.dpl/
├─ philosophy.checks.yaml
├─ capture.plan.yaml
├─ assumptions.yaml
└─ runs/<run-id>/
   ├─ captures/
   ├─ a11y/
   ├─ evidence.json
   ├─ ledger.json
   └─ verdict.json
```

The product's philosophy remains in the product's own authoritative document. DPL must not copy the philosophy body into `.dpl/`.

## Evidence rules

1. Rendered evidence is required for a visual `PASS`.
2. Build, lint, typecheck, and test results may support engineering confidence but never raise a visual verdict.
3. Before/After comparisons should use comparable data. If fixture hashes differ, cap the result at `PASS_WITH_WARNING`.
4. If network activity can mutate the compared data and is not controlled, record the risk and cap the result at `PASS_WITH_WARNING`.
5. Absence from an incomplete accessibility/layout dump is not proof of absence.
6. Dirty-tree evidence should include a worktree diff hash when the structured gate is used.
7. A claimed external engine must have invocation proof in the run ledger.
8. A changed file that matches a declared scope denylist fails unless an explicit exception exists.
9. Referenced evidence artifacts must exist and match their recorded SHA-256 hashes.

## Verdict Gate

`tools/dpl/verdict_gate.py` computes the strongest verdict supported by structured evidence.

Exit codes:

- `0` — `PASS`
- `10` — `PASS_WITH_WARNING`
- `20` — `FAIL`
- `30` — `NOT_VERIFIED`
- `2` — invalid evidence input

The agent may record `declared_verdict`, but it must never report a result higher than the gate's `computed` verdict when the gate is used.

If the gate records `overclaim: true`, report it. Do not rewrite or soften the gate reasons.

## Run Ledger

The ledger separates what was available from what was actually used.

Recommended event types:

- `source_consulted`
- `engine_invoked`
- `engine_unavailable`
- `capability_run`
- `decision`

An engine counts as invoked only when the event records `invoked: true` and concrete proof such as the command or tool action used.

## Scope of automation

The current repository includes the verdict gate and philosophy check runner as internal tools. Platform capture adapters are intentionally not claimed as complete.

Web and native capture automation should be added only after each adapter can produce reliable, reproducible evidence without weakening product boundaries.
