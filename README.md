# ZestfulPulse Design Pattern Lab

A reusable, product-first design workflow for ZestfulPulse apps and websites.

This repository separates **how we design** from **what each product is**:

- `skills/product-design-workflow/SKILL.md` defines the repeatable design process.
- `skills/product-design-workflow/templates/` provides optional starting points for product-specific design records.
- Each app's own GitHub repository remains the source of truth for its product philosophy, UX, visual system, and implementation decisions.

## Principles

1. Define the product's character and philosophy before choosing its visual style.
2. Keep product-specific decisions in that product's repository.
3. Read existing documentation before creating or changing design documents. Extend the current source of truth; do not create competing copies.
4. Keep design work separate from implementation and deployment unless the user asks for implementation.
5. Research real references when doing substantial visual work; adapt their useful traits rather than copying a screen.
6. Use the lightest process that can answer the design question. Do not manufacture A/B/C options for a clear brief.
7. Treat Supabase, Cloudflare, GitHub, and signing as implementation/deployment concerns, not design authorities.

## Install on Windows

Install the one skill globally for Codex on the Windows development PC. See [Windows setup](docs/WINDOWS_SETUP.md) for the private-repository clone and update commands.

## Product project layout

Use the templates only when the product repository lacks an equivalent authoritative document. A small project can start with `PRODUCT_FOUNDATION.md` and add other records as the design matures.

Suggested locations (adapt to the repository's existing conventions):

```text
design/
  PRODUCT_FOUNDATION.md
  EXPERIENCE_SPEC.md
  VISUAL_SYSTEM.md
  DECISION_LOG.md
  IMPLEMENTATION_HANDOFF.md
```

Do not copy the templates into an app automatically. Keep app-specific decisions with that app's source.
