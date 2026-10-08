# MengTo Web Pattern Pack

DPL may use a curated subset of [MengTo/Skills](https://github.com/MengTo/Skills) as an optional web implementation-pattern library.

The upstream repository is MIT licensed. DPL does not vendor the upstream demos, assets, or skill code. The skills remain independently installed specialist inputs.

## Why this pack exists

DPL already decides product direction, hierarchy, accessibility, interaction intent, and release evidence. MengTo/Skills adds a different capability: concrete, runnable implementation patterns with matching demos and recreation/remix prompts.

Use the pack only **after** product direction is established.

```text
Product truth
  ↓
DPL diagnosis
  ↓
One approved direction
  ↓
Select the smallest relevant MengTo pattern
  ↓
Adapt to product tokens / content / behavior
  ↓
Implement
  ↓
Visual Release Review
```

Never reverse this order.

## Curated skills

| Skill | DPL role | Use when |
|---|---|---|
| `design-first-ui-prompting` | Direction specification | Turn a vague UI idea into a constrained design brief before implementation |
| `landing-page` | Page composition | A marketing/product landing page needs proven section structure |
| `build-awwwards-quality-sites` | High-bar web art direction | The user explicitly wants premium, cinematic, highly authored web presentation |
| `clean-minimal-beige-light-mode` | Visual language pattern | Warm minimal light-mode direction fits the approved product philosophy |
| `framed-tech-dark-border-gradient` | Visual language pattern | Technical, framed, dark-system presentation fits the product |
| `editorial-tech` | Layout / typography pattern | Editorial hierarchy and technical information need to coexist |
| `dark-glass-clean-layout` | Visual language pattern | Restrained dark glass is already consistent with the chosen direction |
| `agency-grid-layout-minimal` | Layout pattern | A disciplined grid-driven presentation is appropriate |
| `cinematic-scroll-storytelling` | Motion / narrative pattern | Scroll itself carries product narrative or sequence |
| `gsap-scrolltrigger-storytelling` | Motion implementation pattern | GSAP ScrollTrigger is already allowed and scroll-linked animation is justified |
| `product-proof-saas` | Evidence / conversion composition | SaaS/product pages need proof, explanation, and conversion structure without invented claims |
| `stitched-full-page-capture` | Render evidence | Lazy/animated/WebGL pages need reliable full-page visual evidence |
| `audit-reference-originality` | Originality guard | External references materially influenced the result and overlap risk should be checked |

## Selection rules

1. Product-local philosophy, current tokens, platform constraints, and approved behavior always outrank MengTo patterns.
2. Do not combine multiple visual-style skills merely because they are available.
3. Prefer one layout pattern + at most one visual-language pattern + one motion pattern when the task genuinely needs all three.
4. `build-awwwards-quality-sites` is not a default. Use it only when the requested product direction genuinely calls for a high-concept marketing experience.
5. Motion skills do not authorize adding GSAP, Lenis, WebGL, or other dependencies. Existing DPL scope rules still apply.
6. Demo HTML and screenshots are references, not product assets.
7. Do not copy upstream brand identity, proprietary imagery, text, or distinctive layouts wholesale.
8. When upstream instructions conflict with product truth or DPL boundaries, discard the upstream instruction.
9. Record which MengTo skills were actually invoked. Availability is not usage.
10. Validate the rendered result through DPL Visual Release Review.

## Suggested bundles

| Product need | Suggested pattern |
|---|---|
| Clean product/portfolio landing | `design-first-ui-prompting` + `landing-page` + one approved visual-language skill |
| Technical developer product | `editorial-tech` or `framed-tech-dark-border-gradient` |
| Minimal lifestyle/product site | `clean-minimal-beige-light-mode` or `agency-grid-layout-minimal` |
| Premium brand/campaign site | `build-awwwards-quality-sites` + one justified motion skill |
| Narrative scroll page | `cinematic-scroll-storytelling` or `gsap-scrolltrigger-storytelling` |
| SaaS evidence/conversion page | `product-proof-saas` |
| Reference-heavy redesign | `audit-reference-originality` after implementation |
| Complex animated page QA | `stitched-full-page-capture` before final visual verdict |

## Demo contract

MengTo/Skills demos commonly include:

```text
SKILL.md
demo/index.html
demo/PROMPT.md
demo/preview.jpg
```

This is useful because the Design Team can inspect both the operating instructions and a rendered implementation reference. DPL should extract relationships such as hierarchy, spacing, composition, motion logic, and component anatomy rather than blindly reproducing the demo.

## Installation

Install the curated pack with the helper scripts in this repository:

- Windows: `scripts/install-mengto-pack.ps1`
- macOS/Linux: `scripts/install-mengto-pack.sh`

The scripts install the skills globally for Codex from the upstream MengTo/Skills repository.
