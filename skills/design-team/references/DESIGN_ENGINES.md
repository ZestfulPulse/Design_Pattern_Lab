# Design engine routing

This reference defines the Design Team's specialist routing model.

The active product repository remains the authority. The Design Team is the single decision maker. Specialist engines contribute bounded expertise only when relevant and available.

## Routing principles

1. Read the active product first.
2. Use the smallest number of specialist engines that materially improve the result.
3. Do not call every tool by default.
4. Never let a style source override product philosophy.
5. Never claim an engine ran unless it actually ran.
6. Resolve conflicts centrally in Design Team.

## DPL — orchestration and product-design synthesis

Role: broad product-design orchestration when a local DPL toolset is available.

Typical use:

- deciding which specialist design sources are relevant;
- reconciling multiple design references;
- converting product philosophy into a coherent visual/UX direction;
- maintaining consistency across screens and platforms.

DPL should not compete with Design Team. Treat DPL as an internal orchestration source under Design Team.

If DPL is unavailable in the active environment, continue with other available sources and product-local evidence.

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
| App-wide redesign | DPL + UI UX Pro Max |
| Web landing redesign | DPL + UI UX Pro Max + Hallmark |
| Strong visual/art direction | DPL + Huashu |
| Analytics/dashboard redesign | DPL + UI UX Pro Max + Infographic |
| Small component fix | Product-local system first |
| Native app screen | DPL + UI UX Pro Max, no Hallmark macrostructure |
| Brand-heavy marketing page | DPL + Huashu + Hallmark |
| Dense explanatory page | DPL + Infographic + Hallmark |

## Conflict resolution

When specialist guidance conflicts:

1. product philosophy wins;
2. current product behavior and approved tokens come next;
3. Design Team chooses one coherent direction;
4. specialist preferences are discarded when they weaken product consistency.

Never create multiple competing design systems inside one product.
