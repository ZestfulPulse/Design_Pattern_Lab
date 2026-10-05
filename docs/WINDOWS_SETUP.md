# Windows setup

## Install the design workflow skill for Codex

Run this in PowerShell on the Windows PC where Codex is used:

```powershell
npx skills add ZestfulPulse/Design_Pattern_Lab --skill product-design-workflow --global --agent codex
```

The Skills CLI supports selecting one skill, installing it globally, and targeting Codex. The source repository must be accessible to your GitHub account. This keeps the skill available across projects on that Windows user account; it does not install the skill on the Mac mini.

## Update after changes

Re-run the same install command when the skill changes. Keep the canonical version in this repository; avoid maintaining separate edited copies in multiple agent directories.

## Use in a project

1. Keep the app's code and product-specific design documents in its own GitHub repository.
2. At the start of a design task, ask Codex to use `product-design-workflow` and inspect that repository's existing design source of truth.
3. Add only missing documents from this repository's `skills/product-design-workflow/templates/`.
4. Commit approved product-specific design decisions to that product's repository.

## Environment boundary

The skill guides design work. It does not require local macOS development, Supabase access, Cloudflare credentials, or signing tools. Use the Mac mini only for the signing tasks that require it.
