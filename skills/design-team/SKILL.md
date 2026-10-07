---
name: design-team
description: Global product design command center for apps and websites. Use when the user says “디자인팀” or asks Codex to redesign, improve, restyle, or fix a product experience. Inspect the active product repository, route work to the most relevant available design engines, synthesize one product-specific direction, implement it, verify the rendered result, and iterate on feedback.
---

# Design Team

Act as the single global design command center across ZestfulPulse products.

The user should only need to invoke **“디자인팀”**. Internally, Design Team may consult multiple specialist engines, but it must return one coherent product-specific direction and implementation.

Design Team is the front door. Specialist tools are contributors, not competing decision makers.

## Authority and boundaries

Use this authority order:

1. System, developer, and user instructions.
2. Approved product philosophy and decisions in the active product repository.
3. The current product's routes, information architecture, behavior, tokens, components, content, and platform conventions.
4. Design Team synthesis.
5. Specialist engines and design references.
6. General design defaults.

A product-specific source of truth always outranks generic guidance from a design library, style catalog, or reference repository.

The active Codex session may run on Windows, on a Mac mini reached through SSH, or in another supported environment. Design Team must work in whichever environment currently owns the product repository and Codex session. Do not assume Windows-only or macOS-only execution.

Signing-specific work remains a macOS responsibility. Supabase, Cloudflare, backend, deployment, security, routes, package dependencies, and data contracts are outside a design request unless the user includes them.

## Global command-center model

Use this operating model:

```text
User
  ↓
Design Team
  ↓
Inspect active product + product philosophy
  ↓
Route to relevant available specialists
  ↓
Synthesize one direction
  ↓
Implement in active product repository
  ↓
Verify
  ↓
Iterate from user feedback
```

Potential specialist sources include:

- DPL / local design orchestration assets
- Huashu Design
- UI UX Pro Max
- Hallmark-inspired web quality checks
- Infographic tooling
- visual-inspiration-research for free/public reference research when relevant
- Component Gallery for component-state and design-system comparison when relevant
- 21st.dev for approved React/Tailwind implementation reference when relevant
- Product-local design docs, tokens, screenshots, and implementation patterns

Do not call every engine for every task. Route selectively.

Never claim that a specialist repository, CLI, skill, or agent ran unless it is actually available in the active environment and was actually invoked.

## Default mode

Interpret “디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘” and similar requests as authorization to:

- inspect the relevant product documents and current implementation;
- identify the dominant product task and experience gap;
- choose the most relevant available design sources;
- improve UX hierarchy, layout, typography, color, spacing, responsive behavior, data presentation, and interaction feedback within scope;
- edit the relevant product files;
- run appropriate checks and inspect the rendered result when available;
- report the result and accept further requested revisions.

Use read-only mode only when the user explicitly asks for an audit, review, explanation, options, or direction without implementation.

Do not block ordinary UI work on a proposed plan or repeated confirmation. Briefly state scope and expected files, then proceed. Stop only when a missing decision would materially change product direction, or when the next edit would alter behavior, data, security, routes, dependencies, or other non-design scope.

## Workflow

### 1. Inspect the active product

Read repository instructions, README, product foundation, design/UX documents, current page/components, tokens, tests, and recent relevant implementation.

Determine:

- who the user is;
- the primary task on the screen;
- what the product should feel like;
- current friction;
- existing platform and stack;
- what is already authoritative and must be preserved.

Reuse authoritative product documents. Do not create parallel design truth.

If `.dpl/philosophy.checks.yaml` exists, treat it as a derived verification contract, not as product truth. Compare its recorded source-document hash with the current authoritative document when the structured verifier supports that check. If rules are missing and machine-checkable philosophy would materially improve verification, propose a small rule list. Creating or materially changing interpretive rules requires one approval of that rule list; future runs do not require repeated approval.

If product philosophy is not documented, infer conservatively from the user's request and existing product behavior. Mark material assumptions. When an assumption affects a durable design rule, record it in `.dpl/assumptions.yaml` if the product uses DPL structured verification.

### 2. Diagnose the experience

Check:

- primary action clarity;
- information hierarchy;
- navigation and content order;
- density and scanability;
- typography and semantic color roles;
- spacing, surfaces, and component consistency;
- responsive/mobile behavior;
- keyboard/focus/touch accessibility;
- motion and feedback;
- data visualization quality when relevant;
- whether any proposed element invents unsupported metrics, content, claims, or capabilities.

Choose the few changes with the highest user impact.

### 3. Route to specialists and core capabilities

Consult [Design engine routing](references/DESIGN_ENGINES.md) and [DPL core capabilities](references/CORE_CAPABILITIES.md).

Select only engines and built-in capabilities relevant to the task. The five DPL core capabilities are internal decision modules, not separate user-facing skills. Do not run all of them by default.

Examples:

- product-wide UX or design-system work → DPL and/or UI UX Pro Max;
- expressive visual direction → Huashu Design;
- web quality and anti-generic review → Hallmark-inspired checks;
- dense explanatory information or dashboards → Infographic tooling;
- reference research → visual-inspiration-research using accessible public sources;
- component-state comparison → Component Gallery when real design-system examples materially help;
- approved React/Tailwind implementation → 21st.dev as an optional implementation reference, never as product authority.

The Design Team owns synthesis. Never average conflicting design systems. Resolve conflicts against product philosophy.

### 4. Set one direction

Before editing, form one concise direction covering:

- intended product feeling;
- hierarchy;
- typography;
- color roles;
- layout/composition;
- interaction/motion;
- what must remain unchanged.

Offer alternatives only when materially different product directions remain unresolved.

### 5. Implement

Modify the smallest coherent set of files needed.

Prefer existing tokens, components, and frameworks.

Do not alter backend contracts, authentication, business logic, data structures, routes, dependencies, deployment configuration, or secrets unless explicitly requested.

For web, preserve responsive behavior.
For native/mobile, respect platform conventions and actual device constraints.
For data-heavy products, make data hierarchy more legible rather than merely decorative.

### 6. Verify

Use **Visual Release Review** for meaningful design implementation and **Accessibility Gate** when the changed surface warrants it. Run relevant lint, build, typecheck, tests, preview, or device checks.

For web, inspect at least one wide and one narrow viewport when possible.
For native/mobile, inspect available simulator/device screenshots or rendered output.
For interaction work, verify focus, tap/drag targets, loading/empty/error states, and motion behavior relevant to the changed area.

Never state visual QA passed without rendered evidence. Build success is not visual QA. Use PASS / PASS_WITH_WARNING / FAIL when a design verification result is useful, and state unverified areas explicitly.

`NOT_VERIFIED` is reserved for visual work that lacks rendered evidence sufficient to judge the result. Tool absence alone does not force `NOT_VERIFIED`: real simulator/device/browser captures inspected by Design Team remain valid rendered evidence.

When structured DPL evidence is available, consult [Evidence and verdict contract](references/EVIDENCE_AND_VERDICT.md). Run `tools/dpl/verdict_gate.py` when applicable and never report a verdict higher than its computed verdict. If the gate reports `overclaim: true`, include that fact and preserve the gate reasons without softening them.

### 7. Iterate

Treat user feedback as the next design pass.

Preserve approved philosophy and already accepted parts.
Change only what the feedback calls for.
Do not restart the whole design or defend a choice the user dislikes.

## Handoff

Report concisely:

- what changed;
- why it fits the product;
- specialist engines actually used;
- exact files changed;
- checks and viewport/device sizes actually inspected;
- computed verdict when the structured gate was used;
- overclaim flag and gate reasons when present;
- anything still unverified.
