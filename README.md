# Design Pattern Lab

<p align="right"><a href="README_KO.md">한국어</a> · <strong>English</strong></p>

> **A global design command center for AI coding agents.**  
> 제품 철학을 먼저 읽고, 필요한 디자인 지식만 골라 쓰고, 실제 화면으로 검증하는 전역 디자인 총괄팀.

<p align="center">
  <strong>One command. One design team. Product truth first.</strong>
</p>

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘.
```

Design Pattern Lab, or **DPL**, is not a component dump and not another giant style library.

It is a product-first orchestration layer currently packaged and documented for **Codex**. The architecture is portable to other coding agents, but those integrations are not yet documented or verified. DPL reads the active product, decides what kind of design help is actually needed, selectively routes to relevant specialists, implements the smallest coherent change, and verifies the rendered result.

---

## Why DPL exists

AI-generated products often start to look alike when the model is given lots of components but no clear design authority.

DPL reverses that order.

```text
Generic style library
        ↓
      product
```

becomes:

```text
Product philosophy
        ↓
Current UX / tokens / behavior
        ↓
Design Team
        ↓
Only the design knowledge actually needed
        ↓
Implementation
        ↓
Rendered evidence
```

**The product decides the design. The library does not.**

---

## How it works

```text
User
  ↓
"디자인팀"
  ↓
Inspect active product
  ↓
Find the actual design problem
  ↓
Choose built-in capabilities + optional specialist sources
  ↓
Synthesize one direction
  ↓
Implement in the active repository
  ↓
Visual Release Review
  ↓
PASS / PASS_WITH_WARNING / FAIL / NOT_VERIFIED
```

The user should not have to choose between five overlapping design agents.

**Design Team is the front door.** Specialist tools are contributors, not competing decision makers.

---

## Five focused capabilities

DPL deliberately keeps its internal capability set small.

| Capability | What it does |
|---|---|
| **Component State Auditor** | Checks relevant default, focus, loading, error, empty, overflow, responsive, keyboard and touch states |
| **Design System Ingestor** | Reads external `DESIGN.md` or style systems and classifies guidance as **KEEP / ADAPT / REJECT** |
| **Interaction Physics** | Makes motion explain causality, continuity, direct manipulation and feedback instead of decorating the screen |
| **Accessibility Gate** | Reviews semantics, focus, contrast, reflow, target size, reduced motion and platform accessibility concerns |
| **Visual Release Review** | Inspects the actual rendered result and reports **PASS / PASS_WITH_WARNING / FAIL / NOT_VERIFIED** with evidence |

These are built into Design Team. They are **not five more skills to install or invoke**.

→ [Read the core capability spec](skills/design-team/references/CORE_CAPABILITIES.md)

---

## Evidence that can push back

DPL can now use an optional structured verification path that turns parts of the product philosophy into checks, records rendered evidence, tracks which engines actually ran, and computes the strongest verdict the evidence supports.

The important distinction is simple:

- **human-rendered evidence still counts** — real browser/simulator/device output inspected by Design Team remains valid and can be recorded as `review_mode: human_render` with reviewer, environment, viewport, reviewed capture IDs, reviewed areas, and any unverified areas;
- **structured verification is stronger when available** — it can catch overclaims, incomparable Before/After data, missing evidence, false engine-use claims, and scope violations;
- **NOT_VERIFIED** means there is not enough rendered evidence to judge the visual result. It does not mean a verification tool was merely unavailable.
- **Harness mode without philosophy checks** is capped at `PASS_WITH_WARNING` (`NO_PHILOSOPHY_CHECKS`), while a complete `human_render` review can still reach `PASS`.
- **Stale philosophy checks** are detected through source-document hashes and cap the result at `PASS_WITH_WARNING` (`CHECKS_STALE`).

Internal tools live under `tools/dpl/`. They are part of Design Team, not new user-facing skills.

→ [Evidence and verdict contract](skills/design-team/references/EVIDENCE_AND_VERDICT.md)  
→ [Philosophy checks guide](skills/design-team/references/PHILOSOPHY_CHECKS.md)

---

## Product truth wins

DPL uses this authority order:

1. User instruction
2. Approved product philosophy and decisions
3. Current routes, behavior, tokens, components and content
4. Design Team synthesis
5. Specialist design engines and references
6. Generic design defaults

A mature product should not be restyled just because a new design library was discovered.

When an external design system is useful, DPL translates it into the current product rather than replacing the product with it.

---

## Specialist routing

DPL can selectively consult external tools and references when they materially improve the task.

| Source | Role |
|---|---|
| **Huashu Design** | Expressive visual direction and concept exploration |
| **UI UX Pro Max** | Design-system and stack-aware guidance |
| **Hallmark-inspired checks** | Web quality and anti-generic review |
| **Infographic tooling** | Dense information, comparison and process visualization |
| **Refero** | Real-product reference research when available |
| **Product-local design docs** | Highest-value source when the product already has a defined philosophy |

Using several engines is **not** the goal.

For a small hierarchy problem, DPL may use no external design engine at all. For a larger redesign, it may combine several. The Design Team owns the final synthesis.

→ [Design engine routing](skills/design-team/references/DESIGN_ENGINES.md)

---

## Showcase 01 · Legs of Steel

**Product:** precision running analysis and coaching app  
**Design intervention:** Home information hierarchy  
**Result:** `PASS_WITH_WARNING`  
**Evidence warning:** the After screenshot confirms Goal is first, but does **not** visually prove the full Goal → Workout → Month sequence. The activity dataset also changed between captures.

The product philosophy defined the intended order as:

```text
Goal gap
→ Today's training and safety
→ Supporting statistics
```

The previous Home hierarchy was:

```text
Monthly stats
→ Today's workout
→ Goal progress
```

The design pass moved goal progress to the first position while preserving the existing visual system, business logic and data flow.

<table>
  <tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
  </tr>
  <tr>
    <td><img src="showcase/01-legs-of-steel/before.png" alt="Legs of Steel Home before Design Team hierarchy change"></td>
    <td><img src="showcase/01-legs-of-steel/after.png" alt="Legs of Steel Home after Design Team hierarchy change"></td>
  </tr>
</table>

### What this case proves

This is intentionally **not** a showcase about throwing many design engines at a screen.

The actual sources used were:

- LoS product philosophy
- existing LoS design tokens
- Design Team's product-first and rendered-evidence rules

DPL, Huashu, UI UX Pro Max, Hallmark and Refero were **not used** to make the original LoS change.

That restraint is part of the system.

→ [Read the full Legs of Steel case study](showcase/01-legs-of-steel/README.md)

---

## Use it

In any product repository where Design Team is installed globally:

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘.
```

More specific requests are also fine:

```text
디자인팀, 현재 정보 구조는 유지하고
이 화면이 정밀한 분석 도구처럼 느껴지도록 개선해줘.
기능과 데이터 흐름은 바꾸지 말고 실제 렌더까지 검증해줘.
```

Or ask for review only:

```text
디자인팀, 구현은 하지 말고 이 화면의 UX 문제만 검토해줘.
```

---

## Install

### Windows

```powershell
$repoPath = "$env:USERPROFILE\projects\Design_Pattern_Lab"

if (Test-Path $repoPath) {
  Set-Location $repoPath
  git pull --ff-only
} else {
  git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git $repoPath
  Set-Location $repoPath
}

npx skills add . --skill design-team --global --agent codex
```

→ [Windows setup](docs/WINDOWS_SETUP.md)

### Mac / SSH host

```bash
repo_path="$HOME/projects/Design_Pattern_Lab"

if [ -d "$repo_path/.git" ]; then
  cd "$repo_path"
  git pull --ff-only
else
  git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git "$repo_path"
  cd "$repo_path"
fi

npx skills add . --skill design-team --global --agent codex
```

→ [Mac / SSH setup](docs/MAC_SETUP.md)

If Codex edits a Windows-local product, invoke Design Team from that Windows session.

If Windows is only the control surface and the product repository lives on a Mac mini reached through SSH, invoke Design Team from the Mac Codex session.

**Same team. Same rules. Different workbench.**

---

## Optional specialist engine

UI UX Pro Max can be installed separately and used when its guidance is actually relevant:

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai universal --global
```

DPL does not require every specialist tool to be installed.

---

## Repository structure

```text
Design_Pattern_Lab/
├─ README.md
├─ LICENSE
├─ docs/
│  ├─ WINDOWS_SETUP.md
│  └─ MAC_SETUP.md
├─ showcase/
│  └─ 01-legs-of-steel/
└─ skills/
   └─ design-team/
      ├─ SKILL.md
      ├─ agents/
      ├─ references/
      │  ├─ CORE_CAPABILITIES.md
      │  ├─ DESIGN_ENGINES.md
      │  └─ SOURCE_ATTRIBUTION.md
      └─ templates/
```

Product-specific philosophy, tokens and approved decisions remain in each product repository. DPL should not create a second source of truth.

---

## External sources & attribution

DPL does not claim ownership of the external design systems, libraries or reference projects it learns from or routes to.

External sources are classified as:

- **Tool / engine** — actually invoked when installed and useful
- **Reference** — consulted for patterns or principles
- **Inspiration** — informed a DPL capability without bundling the upstream project

Examples include Component Gallery, DESIGNmd, Refero, Huashu Design, UI UX Pro Max, Hallmark, Emil Kowalski's design skills, Addy Osmani's web-quality skills, Impeccable, shadcn/ui and Anime.js.

**Available does not mean used.** Every showcase must list only the sources actually used.

→ [Source attribution and inspiration](skills/design-team/references/SOURCE_ATTRIBUTION.md)

---

## Design boundaries

DPL is allowed to improve presentation and interaction within the user's requested scope.

It must not silently change:

- backend contracts
- authentication
- business logic
- data structures
- routes
- dependencies
- deployment configuration
- secrets

It also must not claim:

- that an external engine ran when it did not
- that accessibility passed without evidence
- that visual QA passed because build or lint passed
- that an external project's license applies to DPL itself

---

## Design philosophy

DPL is deliberately opinionated about a few things:

**Use fewer sources, better.**  
More design engines do not automatically produce better design.

**Preserve product identity.**  
An external style guide is input, not authority.

**Motion should explain something.**  
If removing an animation does not reduce understanding, it may be decoration.

**Accessibility is release quality.**  
Not an optional polish pass.

**Rendered evidence beats declarations.**  
A successful build does not prove a successful design.

---

## Status

**DPL v1 baseline**

- One global Design Team
- Five built-in capabilities
- Selective specialist routing
- Explicit source attribution
- Cross-platform Windows / Mac SSH workflow
- Rendered-evidence verification
- Optional machine-checkable verdict gate and run provenance
- Public case-study structure

Future capabilities should be added only when they close a clearly identified gap without duplicating an existing one.

**Current agent support:** Codex is the documented and verified installation target. Other coding-agent integrations are architectural possibilities, not current compatibility claims.

---

## License

Design Pattern Lab is released under the [MIT License](LICENSE).

External tools, repositories, services and assets remain subject to their own licenses and terms.
