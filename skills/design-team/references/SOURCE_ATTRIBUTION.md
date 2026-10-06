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
| Component Gallery | Component-state comparison, naming, accessibility guidance, and real design-system examples | Reference + inspiration for Component State Auditor; not bundled |
| DESIGNmd | Machine-readable external design-system input | Inspiration for Design System Ingestor |
| Refero / Refero Styles | Real-product reference research | Optional research source; not bundled |
| emilkowalski/skills | Interaction detail, motion, direct-manipulation thinking | Inspiration for Interaction Physics |
| addyosmani/web-quality-skills | Accessibility and web-quality review concepts | Inspiration for Accessibility Gate |
| Superfuture/design-review | Rendered design review and release-check workflow | Inspiration for Visual Release Review |
| jakubkrehel/skills | Evidence-first interface review and smallest-effective-fix thinking | Operating-principle reference |
| pbakaus/impeccable | Responsive/adaptation and systematic UI review ideas | Operating-principle reference |
| 21st.dev | React/Tailwind component discovery and implementation reference | Optional implementation reference; never a product-philosophy authority and never bundled wholesale |
| shadcn/ui | Implementation primitives for compatible web stacks | Implementation library only, not a DPL design authority |
| Anime.js | Motion implementation option for compatible web projects | Implementation library only, not a DPL design authority |

## Internal verification proposal provenance

The structured evidence/verdict work was informed by a **user-supplied DPL design proposal and reference prototype (2026-10-06)**. DPL adopted the evidence-contract, philosophy-check, run-ledger, assumption-register, and verdict-gate ideas selectively rather than treating the proposal as a new user-facing skill.

The integrated verifier code was reviewed, adapted, and extended in this repository. In particular, DPL keeps manual rendered evidence as a valid verification path and fixes a combined-condition verdict edge case so provenance/scope failures can still produce `FAIL` when render evidence is absent.

This attribution records design provenance; it does not claim an upstream external software license for the supplied prototype.

## Existing specialist sources

DPL may also route to the specialist sources documented in [DESIGN_ENGINES.md](DESIGN_ENGINES.md), including Huashu Design, UI UX Pro Max, Hallmark-inspired checks, Infographic tooling, and Refero when available.

## Boundaries

- Do not copy an upstream skill wholesale when a small principle is sufficient.
- Do not redistribute external assets, screenshots, code, or datasets unless their license or terms allow it.
- Do not claim an upstream tool ran unless it actually ran.
- Do not claim an upstream project's license applies to DPL itself.
- Product-local philosophy, tokens, behavior, and approved decisions remain higher authority than every external source.
