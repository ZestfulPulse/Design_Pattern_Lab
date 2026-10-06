# Source Attribution and Inspiration

DPL is an orchestration and decision layer. It does not claim authorship of external design systems, libraries, or reference projects.

External sources are used in one of three ways:

- **Tool / engine** — invoked when it is actually installed and useful.
- **Reference** — consulted for patterns or principles.
- **Inspiration** — informed a DPL capability, without bundling or copying the upstream project.

Availability does not mean usage. A showcase must list only the sources actually used.

## Sources that informed DPL

| Source | Role in DPL | Relationship |
|---|---|---|
| Component Gallery | Component-state comparison and completeness | Inspiration for Component State Auditor |
| DESIGNmd | Machine-readable external design-system input | Inspiration for Design System Ingestor |
| Refero / Refero Styles | Real-product reference research | Optional research source; not bundled |
| emilkowalski/skills | Interaction detail, motion, direct-manipulation thinking | Inspiration for Interaction Physics |
| addyosmani/web-quality-skills | Accessibility and web-quality review concepts | Inspiration for Accessibility Gate |
| Superfuture/design-review | Rendered design review and release-check workflow | Inspiration for Visual Release Review |
| jakubkrehel/skills | Evidence-first interface review and smallest-effective-fix thinking | Operating-principle reference |
| pbakaus/impeccable | Responsive/adaptation and systematic UI review ideas | Operating-principle reference |
| shadcn/ui | Implementation primitives for compatible web stacks | Implementation library only, not a DPL design authority |
| Anime.js | Motion implementation option for compatible web projects | Implementation library only, not a DPL design authority |

## Existing specialist sources

DPL may also route to the specialist sources documented in [DESIGN_ENGINES.md](DESIGN_ENGINES.md), including Huashu Design, UI UX Pro Max, Hallmark-inspired checks, Infographic tooling, and Refero when available.

## Boundaries

- Do not copy an upstream skill wholesale when a small principle is sufficient.
- Do not redistribute external assets, screenshots, code, or datasets unless their license or terms allow it.
- Do not claim an upstream tool ran unless it actually ran.
- Do not claim an upstream project's license applies to DPL itself.
- Product-local philosophy, tokens, behavior, and approved decisions remain higher authority than every external source.
