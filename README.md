# ZestfulPulse Design Pattern Lab

A product-first **Design Team** workflow for ZestfulPulse apps and websites.

## How it works

- Invoke “디자인팀” or `$design-team` in Codex.
- Design Team reads the target app's product philosophy and existing design rules, then improves the requested UX and visual implementation.
- It checks the rendered result when tools are available and revises against the user's feedback.
- Product-specific decisions stay in each app's GitHub repository. This repository contains the reusable skill and optional templates only.

## Design authority

1. The product's approved philosophy and current source of truth.
2. Existing routes, behavior, tokens, and components.
3. Design research and platform-specific craft.
4. Generic style suggestions.

The Design Team workflow includes a concise synthesis of UI UX Pro Max system/stack guidance and Hallmark's web quality checks. It does not bundle either complete upstream repository. If their tools are available in the active Codex environment, Design Team may use them for those bounded roles; otherwise it applies the included guidance and verifies it does not claim an upstream tool ran. See [design engine routing](skills/design-team/references/DESIGN_ENGINES.md).

## Install on Windows

Install the one Design Team skill globally for Codex on the Windows development PC. Follow [Windows setup](docs/WINDOWS_SETUP.md).

## Product documents

Use templates only when the product repository lacks equivalent authoritative documents. Do not create duplicate sources.

```text
design/
  PRODUCT_FOUNDATION.md
  EXPERIENCE_SPEC.md
  VISUAL_SYSTEM.md
  DECISION_LOG.md
  IMPLEMENTATION_HANDOFF.md
```

Templates are under `skills/design-team/templates/`. Product-specific philosophy, design tokens, and decisions belong in the app's own GitHub repository.
