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
- Chrome Flutter launch reached debug-service connection, then Dart compiler exited
- Browser DOM inspection: unavailable because the Browser Use Chromium runtime was not installed
- Desktop screenshot: not captured

## Accessibility and Motion

- iPhone 13 mini layout checks: `PASS`
- Keyboard-open capture checks: `PASS`
- Largest supported Dynamic Type checks: `PASS`
- Reduced Motion transition check: `PASS`
- Automated semantic label duplication check: `PASS`
- Physical accessibility inspection: `NOT_VERIFIED`

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
Mobile actual render: PASS (captured; visual service inspection unavailable)
Desktop actual render: NOT_VERIFIED
Overall DPL: NOT_VERIFIED
```

A build or simulator launch is not treated as a complete DPL visual PASS. Desktop
actual-render evidence and visual accessibility inspection remain required.
