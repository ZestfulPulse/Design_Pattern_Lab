# ZestfulPulse Design Pattern Lab

A global product-first **Design Team** workflow for ZestfulPulse apps and websites.

## Core idea

The user should only need one call:

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘
```

Design Team is the global front door. It inspects the active product repository, routes the task to the most relevant available design specialists, synthesizes one product-specific direction, implements it, verifies the result, and iterates from feedback.

```text
User
  ↓
Design Team
  ↓
DPL / Huashu / UI UX Pro Max / Hallmark / Infographic / reference research
  ↓
One coherent product direction
  ↓
Implementation in the active product repository
```

## Environment model

Design Team is environment-agnostic.

It can run from:

- Codex on a Windows product repository;
- Codex running on a Mac mini reached through SSH;
- another supported Codex environment that can access the product repository.

The active Codex session and active product repository define where implementation happens.

Signing-specific work still belongs on macOS.

## Design authority

1. The product's approved philosophy and current source of truth.
2. Existing routes, behavior, tokens, components, and content.
3. Design Team synthesis.
4. Specialist design engines and references.
5. Generic style defaults.

Product truth always wins over a design catalog.

## Specialist routing

Design Team may selectively consult:

- **DPL** for orchestration and design synthesis;
- **Huashu Design** for expressive visual direction;
- **UI UX Pro Max** for design-system and stack-aware guidance;
- **Hallmark-inspired checks** for web quality review;
- **Infographic tooling** for dense information visualization;
- **Refero or other research tools** for real-product reference research.

Not every engine is used on every task.

See [Design engine routing](skills/design-team/references/DESIGN_ENGINES.md).

## Installation

Install the single `design-team` skill globally in every environment where Codex will directly edit product repositories.

Windows instructions are in [Windows setup](docs/WINDOWS_SETUP.md).

For Mac/SSH workflows, install the same global Design Team skill in the Mac user environment that actually runs Codex.

Specialist engines may remain separate global tools. Design Team discovers and uses them when available.

## Product documents

Product-specific philosophy, design tokens, and approved decisions remain inside each product repository.

Use templates only when the product repository lacks equivalent authoritative documents.

```text
design/
  PRODUCT_FOUNDATION.md
  EXPERIENCE_SPEC.md
  VISUAL_SYSTEM.md
  DECISION_LOG.md
  IMPLEMENTATION_HANDOFF.md
```

Templates are under `skills/design-team/templates/`. Do not create duplicate sources of truth.
