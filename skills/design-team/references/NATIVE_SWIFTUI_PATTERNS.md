# Native / SwiftUI Pattern Pack

DPL uses a curated Native / SwiftUI pack for Apple-platform work.

The pack is deliberately different from the Web Pattern Pack. Native design begins with platform semantics, state correctness, adaptive layout, accessibility, and interaction behavior before visual styling.

## Authority order

For Apple-platform work:

1. Product philosophy and approved product decisions.
2. Current product behavior, tokens, deployment target, and platform constraints.
3. Apple official Human Interface Guidelines and current SDK documentation.
4. DPL Philosophy-to-Design Contract.
5. Native / SwiftUI specialist skills and references.
6. General visual defaults.

A visually attractive third-party pattern never overrides Apple platform behavior or product truth.

## Curated sources

| Source | Role | Relationship |
|---|---|---|
| Apple Human Interface Guidelines | Native platform authority | Official source; consult relevant current pages |
| `design-swiftui-interfaces` | SwiftUI correctness, state stability, navigation, gestures, adaptive layout, accessibility, motion, runtime validation | Installed specialist; MIT |
| `swift-ui-design` | Product-specific visual direction, reusable SwiftUI tokens, atmosphere, materials, motion | Installed specialist; MIT |
| `barbaramartina/swiftuicatalog` | Concrete SwiftUI controls, layouts, containers, modifiers, accessibility examples | Reference-only; MIT |

## Sources not installed by default

### dickwu/apple-design-skill

Useful HIG-oriented reviewer, but DPL does not install it by default because the inspected repository does not expose a standalone project license file and its README notes that reproduced HIG text belongs to Apple Inc.

DPL instead treats Apple's official HIG as the authority.

### twostraws/SwiftUI-Agent-Skill

A strong SwiftUI agent skill, but its main correctness role overlaps substantially with `design-swiftui-interfaces`. Keep it as a future comparison candidate rather than adding two competing correctness engines.

## Native workflow

```text
Product philosophy
  ↓
Philosophy-to-Design Contract
  ↓
platform = ios / ipad / macos / apple
  ↓
Apple HIG / SDK constraints
  ↓
Native Pattern Selector
  ↓
SwiftUI correctness skeleton
  ↓
Visual direction only when useful
  ↓
Component/reference lookup
  ↓
Implementation
  ↓
Simulator/device review
  ↓
Accessibility + Visual Release Review
```

## Native design order

### 1. Stable structure first

Before visual styling, establish:

- navigation model;
- state ownership;
- semantic controls;
- safe areas;
- adaptive containers;
- loading / empty / error states;
- keyboard and focus behavior where applicable;
- device/window adaptation.

### 2. Interaction correctness

For gestures and motion, verify:

- causality;
- interruption;
- reversal;
- cancellation;
- rapid repeated input;
- navigation back-and-forth;
- reduced-motion equivalent;
- haptics only where meaningful.

### 3. Accessibility

Check:

- Dynamic Type;
- VoiceOver names, roles, values, and reading order;
- touch target sizes;
- contrast and non-color cues;
- Reduce Motion;
- Reduce Transparency;
- Differentiate Without Color;
- keyboard/focus where applicable.

### 4. Visual direction

Only after the native skeleton is sound, choose a visual direction that follows the Product Intent Contract.

Do not translate adjectives mechanically:

- "premium" does not automatically mean glass;
- "technical" does not automatically mean monospace;
- "minimal" does not automatically mean low information density;
- "expressive" does not authorize non-native interaction semantics.

## Pattern Selector metadata

Native patterns live at:

```text
skills/design-team/patterns/native-patterns.json
```

Native profiles may use traits such as:

- native_fidelity
- interaction_rigor
- accessibility
- adaptability
- visual_expression
- motion_intensity
- information_density

Pattern Selector accepts arbitrary 0–5 traits, so Native profiles do not need to reuse Web-only aesthetic axes.

## Installation

Install the curated specialist skills:

- Windows: `scripts/install-native-pack.ps1`
- macOS/Linux: `scripts/install-native-pack.sh`

The SwiftUI Catalog remains reference-only and is not installed as a global agent skill.
