# Design engine routing

This reference defines one coordinated design workflow. The product repository remains the authority; UI UX Pro Max and Hallmark contribute bounded craft guidance.

## UI UX Pro Max — primary design-system engine

Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT).

Use UI UX Pro Max for product-specific visual-system and stack recommendations on substantial app or web design work:

1. Identify product type, audience, product character, platform, and actual implementation stack from the brief and repository.
2. Generate or derive a design system for that context: layout pattern, style, semantic colors, typography, effects, and relevant anti-patterns.
3. Use platform/stack guidance when implementation details matter.
4. Compare each recommendation with the product foundation and existing tokens. Preserve aligned recommendations; adapt or reject conflicts.

The Design Team owns the final synthesis and implementation. UI UX Pro Max recommendations are inputs, not product decisions. Do not re-ask for information already available in the product documentation. For small UI fixes, preserve the existing design system and use only relevant searches.

The Windows setup guide installs the full UI UX Pro Max engine globally for Codex. If it is absent in another environment, use the product repository and this workflow's design criteria; do not claim the full engine ran.

## Hallmark — web quality review

Source: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) (MIT).

Use the selected Hallmark principles as a focused review pass for web pages:

- avoid interchangeable hero/features/CTA page rhythms when the product calls for a distinct structure;
- preserve current project tokens and inspect the codebase before editing;
- use clear type hierarchy, semantic color roles, responsive layouts, and complete component states;
- reject invented metrics, fake product chrome, inaccessible micro-text, and decorative effects without a product purpose;
- inspect relevant narrow and wide viewports.

The full Hallmark repository is not bundled with Design Pattern Lab. These checks are integrated into the Design Team workflow to keep one product-aware decision maker. Do not claim that Hallmark itself ran. Do not let a theme or macrostructure catalog override product philosophy, and do not apply web page patterns to native app screens.

## Combining guidance

Use one product-specific direction. UI UX Pro Max contributes breadth and stack-aware design-system choices; Hallmark contributes a web quality check. The Design Team owns product interpretation, implementation, and iteration. Never generate or apply two competing design systems.
