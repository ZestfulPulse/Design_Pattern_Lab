# Windows setup

## Install Design Team for Codex

Run these commands in PowerShell on the Windows PC where Codex is used. Clone through your normal GitHub authentication; this repository is private.

```powershell
$repoPath = "$env:USERPROFILE\projects\Design_Pattern_Lab"
if (Test-Path $repoPath) {
  Set-Location $repoPath
  git pull
} else {
  git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git $repoPath
  Set-Location $repoPath
}
npx skills add . --skill design-team --global --agent codex
```

The Skills CLI supports selecting a single skill, global installation, and targeting Codex. Design Team becomes available across projects for that Windows user. See the [Skills CLI](https://github.com/vercel-labs/skills).

## Install the full UI UX Pro Max design engine

This adds its searchable design system and stack guidance globally for Codex. The upstream CLI supports a universal agent-standard installation for all projects:

```powershell
npm install -g ui-ux-pro-max-cli
uipro init --ai universal --global
```

UI UX Pro Max requires Python 3 for its search tools. The Design Team uses it for system and stack recommendations, then checks them against each product's own philosophy and existing tokens.

## Hallmark's role

The Design Team includes a focused synthesis of Hallmark's web quality checks in `skills/design-team/references/DESIGN_ENGINES.md`. The complete Hallmark repository is not bundled or separately installed, so it cannot trigger an independent conflicting design flow. Its web checks guide the Design Team's own page review.

## Update

After Design Pattern Lab changes:

```powershell
Set-Location "$env:USERPROFILE\projects\Design_Pattern_Lab"
git pull
npx skills add . --skill design-team --global --agent codex
```

Update the UI UX Pro Max tool from its own CLI:

```powershell
npm install -g ui-ux-pro-max-cli@latest
uipro update --global
```

## Use it during development

In a product repository, say for example:

> 디자인팀, 이 웹페이지를 Enough의 제품 철학에 맞춰 수정해줘. 현재 UX 문서와 디자인 토큰을 먼저 읽고, 필요한 시각 변경을 구현한 뒤 모바일과 데스크톱에서 확인해줘.

Design Team inspects the product source of truth, implements ordinary UI/UX changes within the request, verifies what it can, and reports evidence. Say “검토만 해줘” or “시안만 보여줘” when you want a read-only critique or options without implementation.

Keep product-specific documents in the app's own GitHub repository. Design Team uses templates only when that repository lacks equivalent authoritative documents.

## Environment boundary

The skill guides design and front-end work in the environment that actually owns the active product repository and Codex session.

- If Codex edits a Windows-local repository, use the Windows global Design Team installation.
- If Windows is only the control surface and Codex runs on a Mac mini through SSH, install and invoke Design Team on that Mac user as well.
- macOS remains required for signing-specific work, but Mac mini is not limited to signing. It may also be the active product-development host.

Supabase, Cloudflare, backend, deployment, security, routes, package dependencies, and data contracts remain outside an ordinary design request unless explicitly included.
