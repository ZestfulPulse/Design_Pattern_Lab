# DPL Capability Expansion Contract

This document defines the local DPL adapter boundary for the approved external design sources. It is a reference contract, not a copy of any external skill or repository.

## Source roles and authority

- Taste Skill: critic and anti-slop input after Reference Lock.
- Plain text: user-provided research brief.
- Refs Gallery: site-level research for visual direction, storytelling, interaction, typography, and experimental composition.
- User-supplied URLs: explicit references supplied for the current task.
- Public/free references: publicly or freely available reference sources.
- Refero: `OPTIONAL_DISABLED` compatibility metadata only; not a default input.
- Velora UI: candidate component/motion/interaction implementation source only.
- Heroicons Animated: semantic micro-interaction asset source only.
- OpenDots: excluded from DPL; separate TOPIA/SPRAY proposal only.

DPL and the Product SSOT retain authority over product truth, design decisions,
implementation admission, and verdicts. Sources contribute evidence or
methodology only. No source is vendored, copied into DPL, or used to create a
clone engine or replacement design system.

Reference Research order:

```text
Plain text → Refs Gallery → user-supplied URLs → public/free references
→ Reference Lock → Taste Gate
```

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

Velora is opt-in. Candidates require a recorded DPL design decision, an
interaction requirement, product fit, and completed reduced-motion, keyboard,
mobile/touch, and accessibility checks. A candidate is never auto-applied and
never becomes product authority.

## Micro Interaction contract

Heroicons Animated is allowed only for action feedback, state transition, confirmation, direction/navigation, and loading/progress. Continuous decorative animation is rejected. A static icon is preferred when it communicates the state more clearly.

## Evidence boundary

The external source being available is not proof that it was invoked. Any
claimed use requires a run ledger event with invocation proof. DPL visual PASS
still requires inspected actual desktop and mobile renders, render comparison
QA, interaction QA, and accessibility/motion evidence.
