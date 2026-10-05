# Design engine routing

This file defines how Design Team uses ideas from upstream design repositories without installing multiple competing design authorities. Design Team stays the single entry point and the product repository remains the authority.

## UI UX Pro Max — broad system and stack guidance

Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT).

Use its design-system-first method when the task needs a new visual system or substantial redesign:

1. Identify product type, audience, product character, platform, and implementation stack from the brief and repository.
2. Generate or derive a system for that specific context: layout pattern, visual style, semantic colors, typography, effects, and anti-patterns.
3. Use platform/stack guidance when implementation details matter.
4. Compare each recommendation with the product foundation and existing tokens. Preserve aligned recommendations; adapt or reject conflicts.

Do not apply a generic recommendation as a product decision. Keep product-specific visual tokens and page rules in the product repository. When the upstream skill or CLI is actually installed and available, use it for searches; otherwise perform this reasoning with repository evidence and available craft references. Never imply the upstream engine ran when it did not.

## Hallmark — web visual quality and anti-pattern review

Source: [Nutlope/hallmark](https://github.com/Nutlope/hallmark) (MIT).

Use its principles as an additional review pass for web pages:

- avoid interchangeable hero/features/CTA page rhythms when the product calls for a distinct structure;
- preserve existing project tokens and inspect the codebase before editing;
- use clear type hierarchy, semantic color tokens, responsive layouts, and complete component states;
- reject invented metrics, fake product chrome, inaccessible micro-text, and decorative effects without a product purpose;
- test relevant narrow and wide viewports.

Hallmark is a web-focused quality lens here. Do not let a preset theme or layout catalog override the product philosophy. Do not ask for a full creative brief when the repository already answers it. Do not apply web page patterns to native app screens.

## Combining guidance

Do not run both sources as independent design generators or produce two competing systems. Use one product-specific direction. UI UX Pro Max contributes breadth and stack-aware system choices; Hallmark contributes a focused web quality check. The Design Team skill owns synthesis, implementation, and iteration.

For a small UI fix, skip unnecessary catalog searches and use the existing design system plus the relevant quality checks.
