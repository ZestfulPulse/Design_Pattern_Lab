# DPL Capability Expansion Contract

This document defines the local DPL adapter boundary for the approved external design sources. It is a reference contract, not a copy of any external skill or repository.

## Source roles

- Taste Skill: critic and anti-slop input after Reference Lock.
- Refs Gallery: site-level research for visual direction, storytelling, interaction, typography, and experimental composition.
- Refero: screen-level research for components, UX patterns, states, and flows.
- Velora UI: candidate component/motion/interaction implementation source only.
- Heroicons Animated: semantic micro-interaction asset source only.
- OpenDots: excluded from DPL; separate TOPIA/SPRAY proposal only.

## Reference Lock contract

Every combined reference study records:

```text
PRIMARY_REFERENCE
PRESERVE_TRAITS
BORROWED_DETAILS
REJECTED_PATTERNS
PRODUCT_TRANSLATION
```

The lock is a synthesis artifact. It must not reproduce a site or become an external design system.

## Taste Gate contract

The gate runs after Reference Lock and before implementation. It returns exactly:

```text
TASTE_PASS
TASTE_PASS_WITH_WARNING
TASTE_REJECT
```

`TASTE_REJECT` blocks implementation. The gate checks generic AI/SaaS convergence, typography rationale, product-derived layout, intentional color, excessive card/grid/bento/gradient/glow usage, interaction purpose, and mobile consistency.

## Component Resolver contract

Velora candidates require a recorded DPL design decision, an interaction requirement, product fit, and completed reduced-motion, keyboard, mobile/touch, and accessibility checks. A candidate is never auto-applied and never becomes product authority.

## Micro Interaction contract

Heroicons Animated is allowed only for action feedback, state transition, confirmation, direction/navigation, and loading/progress. Continuous decorative animation is rejected. A static icon is preferred when it communicates the state more clearly.

## Evidence boundary

The external source being available is not proof that it was invoked. Any claimed use requires a run ledger event with invocation proof. DPL visual PASS still requires inspected actual desktop and mobile renders, interaction QA, and accessibility/motion evidence.
