# DPL Expansion QA Evidence — 2026-10-10

## Scope

Candidate project: MYOK
Source path: `/Users/j.a.r.v.i.s/projects/myok`
QA worktree: `/tmp/myok-dpl-qa-20261010`
Baseline commit: `266a7663dd57c60800bcd943e08e613f1240472a`

The source checkout had pre-existing dirty changes. They were not reset, stashed,
cleaned, or modified. QA ran from a detached clean worktree.

## DPL Contract Path

```text
Reference Research
→ Reference Lock
→ Taste Gate
→ Design decision
→ interaction requirement
→ optional Component Resolver candidate
→ Micro Interaction policy
→ actual render review
```

External sources remain links and normalized contracts. No external repository was
vendored. OpenDots is excluded from the DPL registry.

## Automated Evidence

- DPL regression: `64 passed`
- DPL Python compile: `PASS`
- DPL diff check: `PASS`
- MYOK web build: `PASS` (`flutter build web --no-pub`)
- MYOK iOS simulator no-sign build: `PASS`
- MYOK focused source-entry suite: `29 passed`
- MYOK full baseline suite: `1412 run, 79 failed` on the clean baseline worktree
- MYOK source checkout was unchanged by QA

The full-suite failures are baseline project failures, not DPL source changes. The
focused suite passed the relevant capture surface, iPhone 13 mini width, keyboard,
Dynamic Type, reduced-motion, and accessibility-label checks.

## Actual Render Evidence

Mobile:

- Device: MONA Visual QA — iPhone 13 mini
- UDID: `41AB4531-0A77-426F-A6CC-587C6727B8BB`
- Install: `PASS`
- Launch: `PASS`
- Screenshot: `qa-artifacts/dpl-expansion-20261010/myok-iphone13mini.png`
- Image size: `1080x2340` RGBA PNG

Desktop:

- Web compilation: `PASS`
- macOS Flutter actual launch: `PASS` (`MYOK` process, VM service, runtime identity, workspace visible)
- Actual desktop capture: user-provided screenshot, `PASS`
- Human visual inspection: no clipping or overlapping elements, `PASS`
- Chrome Flutter launch reached debug-service connection, then Dart compiler exited
- Browser DOM inspection: unavailable because the Browser Use Chromium runtime was not installed
- Automated vision inspection: unavailable (`404` for local image path)
- macOS Accessibility tree inspection: GUI Terminal verification succeeded
- macOS Accessibility window probe: `true, 1, MYOK`
- macOS Accessibility roles observed: `AXGroup`, `AXButton` × 3, `AXStaticText`, `AXText`, window controls
- macOS focused element API: reachable; initial focus reported as `AXGroup`
- macOS Tab traversal probe: 5 consecutive probes remained `AXGroup | missing value`
- macOS individual-control focus order: `NOT_VERIFIED`
- Visual QA result: `PASS_WITH_WARNING`

## Accessibility and Motion

- iPhone 13 mini layout checks: `PASS`
- Keyboard-open capture checks: `PASS`
- Largest supported Dynamic Type checks: `PASS`
- Reduced Motion transition check: `PASS`
- Automated semantic label duplication check: `PASS`
- macOS Accessibility tree reachability: `PASS`
- macOS window/role inspection: `PASS`
- macOS individual-control keyboard focus traversal: `NOT_VERIFIED`
- Physical accessibility inspection: `PASS_WITH_WARNING`

## Verdict

```text
Architecture: PASS
External role separation: PASS
Taste gate contract: PASS
Reference research contract: PASS
Velora automatic usage prohibition: PASS
Heroicons semantic-motion policy: PASS
OpenDots excluded: PASS
DPL regression: PASS
Mobile actual render: PASS (captured; user/human review and automated checks)
Desktop actual render: PASS_WITH_WARNING (human review; automated vision unavailable)
Visual inspection: PASS_WITH_WARNING
Overall DPL: PASS_WITH_WARNING
```

Automated vision inspection was unavailable, but the user inspected the actual
 desktop capture and confirmed no clipping or overlapping elements. macOS
Accessibility tree reachability and window/role inspection are now verified. The
individual-control keyboard focus order remains `NOT_VERIFIED`, so the final
result is not a strict `PASS`.
