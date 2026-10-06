# DPL Core Capabilities

These are built-in decision capabilities of Design Team. They are not separate user-facing skills and they do not need to be installed independently.

The user still invokes one command: **디자인팀**.

## 1. Component State Auditor

Purpose: prevent attractive but incomplete UI components.

Use when a task creates or changes interactive components such as buttons, tabs, dialogs, accordions, forms, lists, cards with actions, editors, or navigation.

Check only states relevant to the component:

- default
- hover when a pointer exists
- pressed / active
- keyboard focus
- disabled
- loading / pending
- success
- validation / error
- empty / zero state
- overflow / long content
- narrow viewport / reflow
- touch target sizing
- keyboard operation and escape behavior where applicable

Do not invent states that the product does not need. Prefer the product's existing component behavior and platform conventions.

Reference inspiration may include Component Gallery and established design systems. Use Component Gallery for concrete comparison of relevant states, semantics, accessibility guidance, and mature component patterns when that comparison materially improves the audit. Product-local behavior and platform conventions remain authoritative.

## 2. Design System Ingestor

Purpose: absorb useful external design guidance without replacing product identity.

Use when the user provides DESIGN.md, a design system, reference repository, screenshot set, theme, or external style guide.

For every meaningful rule classify it as:

- **KEEP** — compatible with product philosophy and existing system.
- **ADAPT** — useful idea, but must be translated into current tokens, components, platform, or brand.
- **REJECT** — conflicts with product philosophy, accessibility, behavior, platform conventions, or already-approved decisions.

Never paste an external design system wholesale into a mature product.

Prefer mapping external concepts to existing semantic roles rather than introducing duplicate tokens.

Record only durable accepted decisions in the product's own source of truth.

## 3. Interaction Physics

Purpose: make motion communicate causality, continuity, direct manipulation, and system response rather than decoration.

Use when motion, gestures, drag, swipe, expansion, navigation transitions, loading feedback, or tactile interaction materially affect usability.

Evaluate:

- what user action caused the motion;
- what spatial or state relationship the motion explains;
- latency between input and response;
- whether interaction can be interrupted or reversed naturally;
- whether easing or spring behavior matches the physical metaphor;
- whether optical alignment matters more than mathematical centering;
- whether reduced-motion users receive an equivalent understandable experience;
- whether removing the animation would make the interaction less understandable.

If motion exists only to make the screen feel impressive, remove or reduce it.

Implementation technology is project-specific: CSS, Web Animations API, Anime.js, Motion, SwiftUI, native Android animation, or another existing stack may be used when appropriate. Do not add a dependency solely because this capability exists.

## 4. Accessibility Gate

Purpose: treat accessibility as release quality, not optional polish.

Use for substantial UI changes and before declaring a design pass complete.

Check what is applicable:

- semantic name / role / value;
- keyboard navigation;
- visible focus;
- focus order and focus return;
- contrast and non-color cues;
- text scaling / reflow;
- touch or pointer target size;
- reduced motion;
- screen-reader reading order;
- labels, instructions, errors, and validation;
- modal/dialog focus containment and dismissal;
- platform accessibility APIs for native interfaces.

Use WCAG 2.2 concepts for web where applicable, but do not claim conformance without appropriate testing evidence.

Report unverified accessibility areas explicitly.

## 5. Visual Release Review

Purpose: independently inspect the rendered product after implementation and catch issues that code review alone misses.

Run after the design change, not instead of product design.

Review the rendered result for:

- information hierarchy;
- typography;
- spacing rhythm;
- alignment;
- density;
- truncation / clipping / overflow;
- responsive behavior;
- component-state completeness;
- semantic color use;
- visual consistency with product philosophy;
- accidental generic-AI patterns;
- interaction feedback relevant to the task.

Use actual rendered evidence whenever possible.

For meaningful visual changes, compare before and after when evidence exists.

A release review result must distinguish:

- **PASS** — requested visual scope verified with sufficient evidence.
- **PASS_WITH_WARNING** — main goal verified, but relevant evidence or coverage is incomplete.
- **FAIL** — requested design goal is not achieved, a required check fails, or a material provenance/scope violation is established.
- **NOT_VERIFIED** — rendered evidence is insufficient to judge the visual result.

Never mark PASS because build or lint passed. Visual QA requires rendered evidence.

## Capability selection

Do not run all five by default.

| Situation | Capability |
|---|---|
| New or substantially changed interactive component | Component State Auditor |
| External DESIGN.md / style guide / design system supplied | Design System Ingestor |
| Gesture, drag, transition, spring, or interaction feel | Interaction Physics |
| Substantial UI change or pre-release design check | Accessibility Gate |
| Any meaningful design implementation before completion | Visual Release Review |

Capabilities may be combined when the task genuinely spans several concerns.

The Design Team owns final synthesis. These capabilities do not override product philosophy, approved product decisions, or platform constraints.
