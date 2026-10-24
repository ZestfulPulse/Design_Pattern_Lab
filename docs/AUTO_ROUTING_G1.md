# DPL G1: Automatic design routing (opt-in per product)

## Intent

DPL is the one design-team entry point. A project should not need its owner to repeat
"디자인팀 가동" for every UI request. This integration is **instruction-driven**, not
a continuously running background service or a GitHub push trigger.

## Router contract

Run `python tools/dpl/auto_router.py "REQUEST" --path "CHANGED_PATH"`.
The result is JSON with `route`, `reason`, and `evidence`.

- `design_team`: load the global Design Team skill, inspect the product repository
  and philosophy, choose the smallest specialist set, implement and verify.
- `inspect`: inspect the diff and product context first; invoke Design Team only
  when work changes visual, UX, interaction, motion, responsive or accessibility behavior.
- `skip`: continue the normal engineering task; do not falsely report DPL usage.

Routing must not change product code, configurations or approval gates on its own.
No UI term can authorize unrelated backend, routes, billing, secrets, dependencies,
production deploy or destructive modifications.

## Product-repo setup (future, separate reviewed rollout)

1. Install DPL global Design Team on the development machine following README_KO.
2. Add the below instruction to that product's agent configuration, only after
   inspecting existing instructions and avoiding conflicts.
3. Validate with both UI and backend requests; record invocation evidence.

### Suggested product-agent instruction

> For requests that create or change UI, visual hierarchy, navigation,
> interaction, responsive layout, or accessibility, automatically invoke the
> installed DPL Design Team skill without waiting for the phrase "디자인팀".
> Preserve approved product philosophy and existing user flows. For ambiguous
> code-only changes, inspect first. Backend-only or data-only tasks do not need
> DPL. Record route reason, skill availability, actual usage, render evidence,
> and PASS/FAIL/NOT_VERIFIED. Never claim DPL ran if unavailable.

## Verification and evidence

Record `request`, `changed_paths`, `route`, `reason`,
`dpl_installed`, `dpl_invoked`, `checks`, `render_evidence`, `verdict`.
A routing verdict alone is never proof of execution. Visual Quality,
Interaction Quality, Error Recovery and Accessibility remain separate gates.
Do not claim PASS from unit tests alone.

## Rollout boundaries

G1 changes only the DPL repository. It does not install a global skill on
remote machines, modify MONA/SPRAY/THE GEAR or make any deployment.
Apply to product repos in a separate reviewed PR, with preview checks.
