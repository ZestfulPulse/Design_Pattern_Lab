# DPL internal verification tools

These tools are internal helpers for **Design Team**. They are not separate user-facing skills.

## Included now

- `verdict_gate.py` — computes the maximum verdict supported by structured evidence.
- `checks_runner.py` — evaluates `order`, `first_viewport`, `presence`, `absence`, and `judgment` philosophy checks against normalized layout/accessibility dumps.
- `philosophy.checks.sample.yaml` — example rule set based on the public Legs of Steel showcase concept.
- `intent_guard.py` — validates the Philosophy-to-Design Product Intent Contract and emits the downstream Pattern Selector profile.
- `pattern_selector.py` — deterministically ranks inspected implementation patterns against a small product profile.
- `test_dpl.py` — unit tests for gate and check-runner behavior.
- `test_pattern_selector.py` — unit tests for Pattern Selector behavior.
- `test_intent_guard.py` — unit tests for Product Intent traceability and profile generation.

## Requirements

The verdict gate uses only Python 3 standard library.

The philosophy check runner additionally requires PyYAML:

```bash
python3 -m pip install -r tools/dpl/requirements.txt
```

## Test

```bash
cd tools/dpl
python3 -m unittest discover -p 'test_*.py'
```

## Current boundary

There is no production web/iOS/Android capture adapter in DPL yet. Do not claim these tools captured a real UI unless an actual adapter or explicit product-specific capture process produced the artifacts.

Manual rendered evidence inspected by Design Team remains valid evidence. The structured tools are an optional stronger verification path, not a replacement for human visual review.

## Provenance

These tools were adapted from a user-supplied DPL verification prototype dated 2026-10-06, then reviewed and modified for DPL's public baseline. The integrated version adds a regression case for the interaction between missing render evidence and false engine-use claims, and preserves manual rendered review as a valid evidence path.
