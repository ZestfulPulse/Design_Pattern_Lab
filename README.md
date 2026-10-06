# ZestfulPulse Design Pattern Lab

A global product-first **Design Team** workflow for ZestfulPulse apps and websites.

## Core idea

The user should only need one call:

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘
```

Design Team is the global front door. It inspects the active product repository, selects only useful design sources, makes one product-specific decision, implements it, verifies the rendered result, and iterates from feedback.

```text
User
  ↓
Design Team
  ↓
Product philosophy + selected specialist sources
  ↓
One coherent product direction
  ↓
Implementation in the active product repository
```

Using several engines is not the goal. Product truth and sound source selection matter more than the number of tools involved.

## Environment model

Design Team is environment-agnostic. It can run from Codex on Windows, from Codex on a Mac mini reached through SSH, or in another supported environment that can access the active product repository. The active Codex session and product repository define where implementation happens. Signing-specific work remains on macOS.

## Design authority

1. The product's approved philosophy and current source of truth.
2. Existing routes, behavior, tokens, components, and content.
3. Design Team synthesis.
4. Specialist design engines and references.
5. Generic style defaults.

Product truth always wins over a design catalog.

## External design sources and specialist routing

Design Team may selectively consult these sources when they materially help the product task. The list describes available options; it does not mean every source was used in any particular project or showcase.

| Source | Origin | Role in Design Team | License / access |
|---|---|---|---|
| DPL | [This repository](https://github.com/ZestfulPulse/Design_Pattern_Lab) | Orchestration and synthesis, when the DPL toolset is available in the active environment | Internal ZestfulPulse project; no `LICENSE` file is present in this checkout. |
| Huashu Design | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | Creative direction, high fidelity concepts, and visual exploration | Upstream declares [MIT](https://github.com/alchaincyf/huashu-design/blob/master/LICENSE). Follow its license when using its software or assets. |
| UI UX Pro Max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable UI patterns and stack-aware design-system guidance | Upstream declares [MIT](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/LICENSE). Follow its license when using its software or data. |
| Hallmark | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Focused web quality review; its web macrostructure guidance does not apply to native app screens | Upstream declares [MIT](https://github.com/Nutlope/hallmark/blob/main/LICENSE). DPL may also use its own bounded Hallmark-inspired checklist; do not claim the Hallmark tool ran unless it did. |
| Infographic | [dataprofessor/infographic](https://github.com/dataprofessor/infographic) | Information-visualization examples for dense comparisons, sequences, or quantitative content | No `LICENSE` file was found in the checked upstream checkout; terms are unconfirmed. |
| Refero | [refero.design](https://refero.design/) | Research into real product screens, UI patterns, and visual references | Subscription/authentication gated in the current DPL source boundary. Treat as research-only; do not copy or redistribute screenshots, logos, or proprietary copy. |

These sources are not bundled into this repository by this table. Check the upstream license and service terms before any use that copies or redistributes their code, data, screenshots, or other assets. “Available” does not mean “used.”

See [Design engine routing](skills/design-team/references/DESIGN_ENGINES.md) for selection rules. The Refero research-only boundary is documented in the local DPL source inventory; current availability and service terms must be checked before each use.

## Showcase

### 01 — Legs of Steel

**Product type:** Precision running analysis and coaching app<br>
**Design intervention:** Home information hierarchy<br>
**Before:** 이번 달 → 오늘의 워크아웃 → 목표까지<br>
**After (source order):** 목표까지 → 오늘의 워크아웃 → 이번 달<br>
**Design sources actually used:** Product-local philosophy + existing tokens + Design Team rules<br>
**Result:** `PASS_WITH_WARNING`

[View case study](showcase/01-legs-of-steel/README.md)

The After screenshot visibly shows the monthly card after the goal card and does not show the workout card between them. The source order is documented in the case study, along with this unresolved evidence limitation.

This is not a case study about using many design engines. Design Team prioritized the product document and existing design system, then changed one information-order decision without unnecessary external style input. The case shows that Design Team's value also comes from knowing when a narrow product-led intervention is enough.

## Installation

Install the single `design-team` skill globally in every environment where Codex will directly edit product repositories.

Windows instructions are in [Windows setup](docs/WINDOWS_SETUP.md). Mac and SSH-hosted Codex instructions are in [Mac / SSH setup](docs/MAC_SETUP.md).

Specialist engines may remain separate global tools. Design Team discovers and selects them when available and relevant.

## Product documents

Product-specific philosophy, design tokens, and approved decisions remain inside each product repository. Use templates only when the product repository lacks equivalent authoritative documents.

```text
design/
  PRODUCT_FOUNDATION.md
  EXPERIENCE_SPEC.md
  VISUAL_SYSTEM.md
  DECISION_LOG.md
  IMPLEMENTATION_HANDOFF.md
```

Templates are under `skills/design-team/templates/`. Do not create duplicate sources of truth.
