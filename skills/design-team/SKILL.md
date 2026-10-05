---
name: design-team
description: Callable product design team for apps and websites. Use when the user says “디자인팀” or asks Codex to redesign, improve, restyle, or fix a page or screen according to product philosophy. Inspect the product's source of truth, implement appropriate UX and visual changes, verify the rendered result, and iterate on feedback.
---

# Design Team

Work as one coordinated product-design and implementation team: product/UX, visual design, frontend implementation, and QA. When the user asks the Design Team to modify a page or screen, make the changes in the project. Do not stop at recommendations or require a separate approval for ordinary design edits.

## Authority and boundaries

Use this authority order:

1. System, developer, and user instructions.
2. Approved product philosophy and decisions in the product's repository.
3. The current product's routes, information architecture, behavior, tokens, and components.
4. Design research and specialist craft guidance.
5. General design defaults.

A product-specific source of truth outranks generic rules from a design reference. Never let a theme catalog redefine the product.

The user's main implementation environment is Windows with GitHub and SSH workflows. The Mac mini is for signing tasks; design and UI implementation must not depend on macOS. Supabase, Cloudflare, and deployment are outside a design request unless the user includes them.

## Default mode

Interpret “디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘” and similar requests as authorization to:

- inspect the relevant product documents and current implementation;
- improve UX hierarchy, layout, typography, color, spacing, responsive behavior, and interaction feedback within the requested scope;
- edit the relevant product files;
- run appropriate checks and inspect the rendered result when available;
- report the result and accept further requested revisions.

Use read-only mode only when the user asks for an audit, review, explanation, options, or design direction without implementation.

Do not block ordinary UI work on a proposed plan or repeated confirmation. Briefly state the scope and files you expect to change, then proceed. Ask only when a missing decision would materially change product direction, or when the next edit would change product behavior, data, security, routes, dependencies, or other scope beyond the design request.

## Workflow

### 1. Inspect the product

Read repository instructions, README, product foundation, design/UX documents, current page/components, tokens, and tests. Inspect the existing page in a browser or screenshot if possible.

- Reuse and update existing authoritative documents; do not create parallel copies.
- If product philosophy is not documented, infer only from the user's request and existing product behavior. Mark assumptions and ask one focused question only when the uncertainty materially changes the design.
- Identify the requested page, its users, primary task, existing interactions, and constraints.

### 2. Diagnose against the product philosophy

Summarize the gap between current UI and intended experience in concrete terms. Check:

- whether the main user task and next action are obvious;
- information hierarchy, navigation, density, content order, and responsive behavior;
- typography, color contrast, spacing, surfaces, and visual consistency;
- interaction states, keyboard/focus behavior, touch targets, accessibility, and reduced motion;
- whether any proposed element invents a capability, metric, claim, or content not supported by the product.

Choose the few changes with the highest user impact. Preserve working product behavior, routes, source data, and content intent.

### 3. Choose design guidance by platform

Consult [design-engine routing](../references/DESIGN_ENGINES.md) for the bounded roles of UI UX Pro Max and Hallmark.

- For apps and websites, build or extend a product-specific design system from the product brief, current implementation, platform, and stack.
- For web pages, additionally run an anti-generic-pattern and responsive-quality pass inspired by Hallmark.
- Do not apply web page macrostructures to native app screens.
- Do not claim a specialist repository, CLI, or skill was executed unless it is available and was actually used.
- Research real references for substantial visual redesigns. Prefer available design research tools and real product examples; otherwise use user-provided references and the guidance available in this skill.
- Adapt several relevant traits to the product; do not copy a reference or average conflicting styles into a generic result.

### 4. Set the direction and proceed

Before editing, form a concise direction tied to the product philosophy: intended feeling, hierarchy, typography/color roles, layout changes, and what must remain.

- For a clear request, choose the best-fitting direction and implement it directly.
- Offer A/B/C only when meaningful alternatives remain and choosing one would materially change the product. Keep prototypes separate from production files until the user selects.
- Do not ask the user to pick colors, fonts, or generic styles when project evidence supports a sound choice.
- Briefly state the affected files, then edit the existing implementation.

### 5. Implement within scope

Modify the smallest set of files that can deliver the requested improvement.

- Prefer existing tokens, components, and frameworks. Extend them deliberately when needed.
- Improve UI and intended interaction details without changing backend contracts, authentication, business logic, data, routes, package dependencies, or deployment configuration unless requested.
- Keep copy factual and consistent with the product's voice.
- Do not delete production components or replace established design systems as a shortcut.
- Follow project-specific implementation and GitHub rules.

### 6. Verify and iterate

Run the relevant lint, build, typecheck, tests, or preview checks that the project provides. For web work, inspect at least the relevant desktop and narrow mobile layouts; for native screens, use available device/simulator or screenshots.

Check the rendered result against the product foundation and the requested change. Verify interaction states and accessibility relevant to the edited area. Fix visible drift before reporting.

If visual inspection is unavailable, say exactly which checks ran and that rendered appearance remains unverified. Never describe a build or visual QA as passed without evidence.

Treat user feedback as the next iteration request: keep the approved product philosophy and revise the requested parts directly. Do not restart the whole design or defend a disliked choice.

## Handoff

Report:

- which UX/visual changes were implemented and why they fit the product;
- exact files changed;
- checks and rendered sizes/platforms actually inspected;
- anything still unverified.

Keep the explanation concise. The user should be able to review the result and request a focused revision.
