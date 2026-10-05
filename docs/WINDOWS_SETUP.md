# Windows setup

## Install the design workflow skill for Codex

Run these commands in PowerShell on the Windows PC where Codex is used. The first command clones the private source through your normal GitHub authentication; then the Skills CLI installs only this skill globally for Codex.

```powershell
git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git "$env:USERPROFILE\projects\Design_Pattern_Lab"
cd "$env:USERPROFILE\projects\Design_Pattern_Lab"
npx skills add . --skill product-design-workflow --global --agent codex
```

This makes the skill available across projects for that Windows user. It does not install anything on the Mac mini.

## Update the skill

From the cloned repository, pull the latest version and rerun the install command:

```powershell
git pull
npx skills add . --skill product-design-workflow --global --agent codex
```

Keep the canonical copy in this GitHub repository. Do not independently edit copies in agent-specific skill directories.

## Use in a product repository

1. Keep the app's code and product-specific design documents in its own GitHub repository.
2. For a design task, invoke `product-design-workflow` and ask it to inspect that repository's existing design source of truth.
3. Add only missing documents from `skills/product-design-workflow/templates/`.
4. Keep approved product-specific decisions in that product's repository.

## Environment boundary

The skill guides design work. It does not require local macOS development, Supabase access, Cloudflare credentials, or signing tools. Use the Mac mini only for signing tasks that require it.
