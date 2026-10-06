# Design engine routing

This reference defines the Design Team's specialist routing model.

The active product repository remains the authority. The Design Team is the single decision maker. Specialist engines contribute bounded expertise only when relevant and available.

## Routing principles

1. Read the active product first.
2. Use the smallest number of specialist engines that materially improve the result.
3. Do not call every tool by default.
4. Prefer a built-in DPL capability over adding another overlapping external skill.
5. Never let a style source override product philosophy.
6. Never claim an engine ran unless it actually ran.
7. Resolve conflicts centrally in Design Team.

## Built-in DPL capabilities

DPL has five focused internal capabilities. They are part of Design Team and are not separately installed:

- **Component State Auditor** — checks relevant interaction states, reflow, overflow, keyboard and touch completeness.
- **Design System Ingestor** — classifies external design-system guidance as KEEP / ADAPT / REJECT against product truth.
- **Interaction Physics** — evaluates causality, latency, interruptibility, easing/springs, optical feedback and reduced motion.
- **Accessibility Gate** — checks applicable semantics, focus, contrast, reflow, targets and assistive-technology concerns.
- **Visual Release Review** — inspects actual rendered evidence and reports PASS / PASS_WITH_WARNING / FAIL.

See [DPL Core Capabilities](CORE_CAPABILITIES.md).

## DPL — this repository's built-in orchestration layer

**DPL means Design Pattern Lab itself**, specifically the Design Team workflow plus the five built-in capabilities documented in [CORE_CAPABILITIES.md](CORE_CAPABILITIES.md). It is not a separate hidden toolset and does not require another DPL installation.

Its role is to:

- decide which specialist design sources are relevant;
- reconcile multiple references against product truth;
- convert product philosophy into one coherent visual/UX direction;
- apply the five built-in capabilities when relevant;
- maintain consistency across screens and platforms;
- require rendered evidence before declaring visual completion.

When a routing example says **DPL + UI UX Pro Max**, it means **Design Team using DPL's built-in orchestration/capabilities, with UI UX Pro Max as an optional specialist input**.

## Huashu Design — expressive visual direction

Role: higher-creativity visual exploration when the task benefits from stronger art direction, composition, atmosphere, or distinctive visual language.

Use selectively for:

- landing pages;
- brand-forward screens;
- editorial or campaign-like moments;
- visual concept exploration.

Do not use Huashu guidance to override usability, accessibility, platform conventions, or product hierarchy.

## UI UX Pro Max — design-system and stack guidance

Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT).

Use for product-specific visual-system and stack recommendations on substantial app or web design work:

1. Identify product type, audience, character, platform, and actual implementation stack.
2. Derive layout, semantic colors, typography, effects, component patterns, and anti-patterns.
3. Use stack/platform guidance where implementation details matter.
4. Compare every recommendation with current product tokens and philosophy.

Recommendations are inputs, not decisions.

For small UI fixes, preserve the existing design system and use only relevant guidance.

## Hallmark — web quality review

Source: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) (MIT).

Use Hallmark-inspired checks as a focused web review pass:

- avoid interchangeable hero/features/CTA rhythms when the product calls for a distinct structure;
- inspect the existing codebase and tokens first;
- maintain clear type hierarchy and semantic color roles;
- ensure complete component states and responsive layouts;
- reject invented metrics, fake product chrome, inaccessible micro-text, and decoration without purpose;
- inspect relevant narrow and wide viewports.

The full Hallmark repository does not need to be bundled. Do not claim Hallmark itself ran unless it actually did.

Do not apply web macrostructure guidance to native app screens.

## Infographic tooling — information visualization

Role: clarify dense information, comparisons, process flows, reports, dashboards, and explanatory product surfaces.

Use when the design problem is primarily about:

- relationships;
- sequence;
- hierarchy;
- comparison;
- quantitative or structured information.

Do not turn ordinary product screens into posters. Use infographic logic only where information density benefits from it.

## Component and implementation references

These sources help Design Team inspect real component patterns or implementation options. They are references, not product-design authorities.

### Component Gallery

Use Component Gallery selectively when Component State Auditor needs stronger real-world comparison for:

- relevant interaction states;
- component naming and semantics;
- accessibility/usage guidance;
- established design-system patterns;
- platform or implementation differences.

Do not copy a component merely because another design system includes it. Product-local behavior and platform conventions remain authoritative.

### 21st.dev

Use 21st.dev as an optional implementation reference for compatible React/Tailwind web work when Design Team needs:

- concrete component candidates;
- implementation patterns that can accelerate an approved direction;
- examples of AI-assisted interface implementation;
- a bridge from an already-decided design direction to working UI code.

Do **not** use 21st.dev as product philosophy, as a wholesale design-system replacement, or as permission to add dependencies without explicit scope. Treat any retrieved component code under its applicable upstream terms.

Neither source needs to be installed or consulted for ordinary work. Availability does not imply use.

## Reference-research tools

Use Refero or other available research tools when a substantial redesign benefits from real product references.

Prefer several relevant traits from real products over copying one design wholesale.

Reference research should answer a concrete design question, such as:

- how comparable products structure dense analytics;
- how premium running apps express performance data;
- how mobile creation tools handle layered editing.

## Suggested routing examples

| Task | Primary sources |
|---|---|
| App-wide redesign | DPL built-in capabilities + UI UX Pro Max |
| Web landing redesign | DPL built-in capabilities + UI UX Pro Max + Hallmark |
| Strong visual/art direction | DPL built-in capabilities + Huashu |
| Analytics/dashboard redesign | DPL built-in capabilities + UI UX Pro Max + Infographic |
| Small component fix | Product-local system first; Component Gallery only when state/pattern comparison materially helps |
| Native app screen | DPL built-in capabilities + UI UX Pro Max, no Hallmark macrostructure |
| Brand-heavy marketing page | DPL built-in capabilities + Huashu + Hallmark |
| Dense explanatory page | DPL built-in capabilities + Infographic + Hallmark |
| React/Tailwind component implementation | Product-local system first + 21st.dev when concrete implementation reference is useful |

## Conflict resolution

When specialist guidance conflicts:

1. product philosophy wins;
2. current product behavior and approved tokens come next;
3. Design Team chooses one coherent direction;
4. specialist preferences are discarded when they weaken product consistency.

Never create multiple competing design systems inside one product.

## Source transparency

External inspirations and operating-principle references are documented in [Source Attribution](SOURCE_ATTRIBUTION.md). DPL should absorb narrowly useful principles rather than accumulate overlapping general-purpose design systems.
