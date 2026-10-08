# Design Exploration Board

Design Exploration Board is a P0 orchestration module inside Design Team. It is not a separate user-facing skill.

Its purpose is to prevent premature convergence on the first plausible visual direction.

## When to run

| Change tier | Exploration |
|---|---|
| Minor repair / polish | Skip by default |
| New screen or materially new surface | Create 2 meaningfully different directions |
| Major redesign | Create 3 meaningfully different directions |
| Brand-defining or new-product surface | Create 3 directions and prototype the strongest candidates when practical |

The Design Team may reduce the count when product truth already determines the direction. Record why exploration was skipped or narrowed.

## Philosophy input

Exploration must start from the Product Intent Contract when one exists.

Each direction should reference the principle IDs it emphasizes and must respect every applicable `must` / `avoid` constraint. A direction that scores well aesthetically but violates a must principle is not a viable candidate.

When two directions trade off competing principles, record that tension explicitly rather than hiding it in an average score.

## Direction contract

Each direction must differ structurally, not just by accent color.

Record:

- thesis
- product-philosophy fit
- hierarchy
- typography
- color/material
- layout/composition
- interaction/motion
- candidate pattern sources
- expected strengths
- risks
- implementation cost
- what remains unchanged

Do not create decorative variants that share the same information architecture and interaction model.

## Selection rubric

Score each direction from 0 to 5 on:

- philosophy_fit
- task_clarity
- differentiation
- accessibility_risk
- implementation_cost
- maintainability

For positive dimensions, higher is better. For `accessibility_risk` and `implementation_cost`, lower is better.

The numeric score is a decision aid, not a substitute for design judgment. The selected direction must include a short written rationale.

## Prototype rule

A prototype is required only when comparing the directions verbally would hide a meaningful visual or interaction difference.

Use the cheapest faithful representation available:

1. existing component composition;
2. standalone HTML fixture;
3. SwiftUI/Compose preview;
4. static visual mock only when interaction is not material.

Do not add dependencies merely to produce exploration artifacts.

## User approval

Ordinary design requests do not need repeated confirmation for every exploration step.

Ask the user to choose only when two or more directions remain materially viable and choosing between them changes product identity or behavior. Otherwise Design Team selects the strongest direction and records why.

## Evidence

When exploration affects a release-significant redesign, store the board under the product repository's `.dpl/` directory if that repository uses structured DPL artifacts.

Suggested path:

```text
.dpl/exploration-board.yaml
```

Use [EXPLORATION_BOARD.yaml](../templates/EXPLORATION_BOARD.yaml) as the starting structure.
