# DPL Capability Expansion Proposal

Status: PROPOSAL / implementation sequence defined
Baseline: `origin/main` at `df7412ddbc7d8e06431aaa6f2a7001d8157a3606`
Date: 2026-10-10

## Decision

Extend Design Pattern Lab through small, auditable contracts. Do not vendor or merge the external repositories into DPL. Product Philosophy / Product SSOT remains authoritative.

```text
Product Philosophy / Product SSOT
  ↓
Reference Research
  ├─ Plain text: user-provided research brief
  ├─ Refs Gallery: site-level visual direction/storytelling/interaction/type/composition
  ├─ user-supplied URLs
  └─ public/free reference sources
  ↓
Reference Lock
  ↓
Taste Critic / Anti-Slop Gate
  ↓
DPL Design Orchestrator
  ↓
Specialist Engine Selection
  ↓
Component Resolver
  ├─ Velora UI: candidate only, never automatic
  └─ existing approved libraries
  ↓
Micro Interaction
  └─ Heroicons Animated: semantic state/action asset only
  ↓
Implementation
  ↓
Actual Render
  ↓
Visual Release Review
```

Refero remains registered only as `OPTIONAL_DISABLED` metadata. It is not a
default Reference Research input. A future activation would require a separate
approval; this Phase A contract does not invoke or depend on it.

The DPL contract and Product SSOT remain the authorities for product truth,
design decisions, implementation admission, and verdicts. Reference sources
provide evidence and methodology only; they do not become a clone engine,
design system, runtime, or acceptance authority. No external repository is
vendored or copied into DPL.

OpenDots is explicitly outside this architecture. It receives no dependency, source copy, adapter, registry entry, or runtime route in DPL. Any future review belongs in a separate TOPIA/SPRAY proposal.

## Ownership and authority

| Layer | DPL owner | External source role | Must not own |
|---|---|---|---|
| Product truth | Product repo / Product SSOT | none | external style rules |
| Reference research | DPL Reference Research | plain text, Refs Gallery, user URLs, public/free refs | implementation decision |
| Reference Lock | DPL | evidence from references | copied site direction |
| Taste gate | DPL Taste Critic adapter | Taste Skill principles | final design authority |
| Orchestration | DPL Design Team | approved specialist inputs | product truth |
| Components | DPL Component Resolver | Velora candidates | automatic insertion |
| Micro interaction | DPL policy | Heroicons Animated assets | decorative motion |
| Acceptance | DPL Visual Release Review | rendered evidence | build-only PASS |

## External source contracts

### Taste Skill

Source: <https://github.com/Leonxlnx/taste-skill>
License signal: MIT, to be rechecked before any vendoring.

DPL extracts principles only through an adapter/reference contract. It does not copy the external skill into the global DPL rules. The adapter produces one of:

```text
TASTE_PASS
TASTE_PASS_WITH_WARNING
TASTE_REJECT
```

The review must inspect:

- generic AI/SaaS convergence;
- reasoned typography;
- product-derived layout family;
- intentional color selection;
- excessive card/grid/bento/gradient/glow use;
- decorative versus necessary interaction;
- mobile consistency.

`TASTE_REJECT` blocks implementation and requires a new design direction.

### Refs Gallery

Source: <https://refs.gallery/>
Role: site-level reference research. It is a gallery/site, not a code dependency.

Every research result must be transformed into a Reference Lock:

```text
PRIMARY_REFERENCE
PRESERVE_TRAITS
BORROWED_DETAILS
REJECTED_PATTERNS
PRODUCT_TRANSLATION
```

A single site cannot be the complete design direction. Refero is retained only
as disabled compatibility metadata and is not part of the Phase A research
pipeline.

### Velora UI

Source: <https://github.com/ColorlibHQ/velora-ui>
License signal: MIT. No source is vendored in this phase.

Velora is a Component Source, Motion Primitive Source, and Interaction Implementation Source. It can be selected only after:

```text
DPL design decision
→ interaction requirement
→ component search
→ Velora candidate
→ product-style adaptation
```

The contract rejects automatic use and records why an interaction serves the product. Candidates must be checked for reduced motion, keyboard, touch/mobile behavior, and accessibility.
Velora remains opt-in and never becomes a default source or authority.

### Heroicons Animated

Source: <https://github.com/heroicons-animated/heroicons-animated>
License signal: MIT. No source is vendored in this phase.

Registered only as a Micro Interaction Asset. Allowed meanings are action feedback, state transition, confirmation, direction/navigation, and loading/progress. Continuous decorative animation and default animation of every icon are prohibited. Static icons win when they communicate better.

## Phase sequence

### Phase A — Reference Research + Taste

Add the smallest contract for:

```text
Plain text / Refs Gallery / user-supplied URLs / public-free references
→ Reference Lock
→ Taste Gate
```

Acceptance:

- Reference Lock schema is explicit.
- approved Reference Research source buckets remain separated;
- Refero is `OPTIONAL_DISABLED` and absent from default research;
- Taste outputs exactly the three allowed verdicts.
- `TASTE_REJECT` blocks implementation in the contract test.
- No external repository is installed or copied.

### Phase B — Velora candidate resolver

Add a candidate record and resolver policy. Automatic selection must fail closed. The resolver requires a product decision and interaction requirement before returning a candidate.

Acceptance:

- no product decision → rejected;
- no interaction requirement → rejected;
- decorative-only rationale → rejected;
- accessibility/motion checks recorded;
- selected candidate remains an implementation suggestion, not authority.

### Phase C — Heroicons Animated policy

Add a semantic asset policy. The policy permits only approved interaction meanings and rejects decorative continuous animation and unnecessary motion.

Acceptance:

- static icon preference is represented;
- reduced-motion behavior is required;
- forbidden animation categories are rejected;
- policy does not become a design engine.

### Phase D — real-project regression

Use `MYOK` first if the repository and runnable render path are available, otherwise use `Enough` or `blog`. Compare the existing path with the expanded path. The expanded path must demonstrate:

```text
approved Reference Research inputs
+ Taste Critic
+ selectively opted-in Velora candidate (if approved)
```

No visual PASS is possible without inspected desktop and mobile actual renders,
render comparison QA, interaction QA, accessibility, and motion evidence.

## Verification contract

DPL verdict vocabulary remains:

```text
PASS
PASS_WITH_WARNING
FAIL
NOT_VERIFIED
```

The external Taste result is an input gate, not a replacement for DPL's verdict gate. Build success, unit tests, or a reference record cannot produce visual PASS. Actual rendered evidence is mandatory.

Required final evidence:

- architecture documented;
- roles separated;
- no duplicate authority;
- Taste Gate operational;
- reference path operational;
- Velora automatic use prohibited;
- Heroicons policy documented;
- OpenDots excluded;
- existing DPL tests pass;
- real project actual render inspected;
- render comparison QA gate passed;
- desktop PASS;
- mobile PASS;
- accessibility/motion PASS;
- local `main` synchronized with `origin/main` after approved publication workflow.

## Rollback

Rollback is contract removal only. Since no external code is vendored and no runtime dependency is added, revert the DPL expansion files and remove their registry/route references. Existing Design Team, pattern selector, evidence gate, and product repositories remain unchanged.

## Initial decision

Proceed with Phase A only after this proposal is recorded. Do not promote any external source to a DPL authority. Do not declare DPL PASS until Phase D actual rendered QA is independently inspected.
