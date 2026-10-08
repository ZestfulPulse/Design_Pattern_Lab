# Pattern Selector

Pattern Selector is a deterministic helper used by Design Team after product direction is understood.

It reduces source sprawl by ranking candidate implementation patterns against a small product profile.

## Product Intent integration

The preferred input is the derived `pattern_profile` from `.dpl/product-intent.yaml`.

Generate/validate that profile with:

```bash
python tools/dpl/intent_guard.py --intent .dpl/product-intent.yaml --profile
```

Then pass the emitted profile to Pattern Selector. This keeps pattern ranking downstream of product philosophy instead of inventing style traits independently.

## Input

A product profile may include:

- `platform`
- `product_type`
- `needs`
- `traits` scored 0–5

Example:

```json
{
  "platform": "web",
  "product_type": "developer_tool",
  "needs": ["technical", "editorial", "low_motion"],
  "traits": {
    "precision": 5,
    "minimal": 4,
    "editorial": 5,
    "playful": 1,
    "warmth": 2
  }
}
```

## Ranking

`tools/dpl/pattern_selector.py` scores each candidate using:

1. platform compatibility;
2. product-type fit;
3. need overlap;
4. trait similarity;
5. explicit avoid conditions.

A platform mismatch is a hard rejection.

Avoid conditions can strongly penalize otherwise attractive candidates.

The selector returns a ranked list with score and reasons. It never authorizes a pattern by itself.

## Authority

The ranking is subordinate to:

1. user instruction;
2. product philosophy;
3. approved product behavior/tokens;
4. Design Team judgment.

Pattern Selector answers **"which references are worth reading?"**, not **"what should the product become?"**

## Source metadata

Platform catalogs live at:

```text
skills/design-team/patterns/web-patterns.json
skills/design-team/patterns/native-patterns.json
```

Add new pattern metadata only after the source has been inspected.

Do not add a source merely because it is visually attractive. Every entry needs a bounded role, best-fit product types, traits, and avoid conditions.

## Native routing

For Apple-platform work, use `native-patterns.json`. Native profiles may use platform-specific traits such as `native_fidelity`, `interaction_rigor`, `accessibility`, `adaptability`, `visual_expression`, `motion_intensity`, and `information_density`.

The selector treats `mobile` patterns as compatible with `ios` and `android`, but native platform authority still comes from the applicable platform guidance, not the score.
