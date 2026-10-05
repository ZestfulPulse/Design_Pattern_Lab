# Windows setup

## Install Design Team for Codex

Run these commands in PowerShell on the Windows PC where Codex is used. Clone through your normal GitHub authentication; this repository is private.

```powershell
git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git "$env:USERPROFILE\projects\Design_Pattern_Lab"
cd "$env:USERPROFILE\projects\Design_Pattern_Lab"
npx skills add . --skill design-team --global --agent codex
```

The [Skills CLI](https://github.com/vercel-labs/skills) supports choosing a single skill, global installation, and targeting Codex. The skill becomes available across projects for that Windows user; it does not install anything on the Mac mini.

## Update Design Team

From the cloned repository:

```powershell
git pull
npx skills add . --skill design-team --global --agent codex
```

Keep the canonical skill in this repository. Avoid separately editing copies in agent-specific skill directories.

## Use it during development

In a product repository, say for example:

> 디자인팀, 이 웹페이지를 Enough의 제품 철학에 맞춰 수정해줘. 현재 UX 문서와 디자인 토큰을 먼저 읽고, 필요한 시각 변경을 구현한 뒤 모바일과 데스크톱에서 확인해줘.

Design Team will inspect the existing product source of truth, implement ordinary UI/UX changes within the request, verify what it can, and report evidence. Say “검토만 해줘” or “시안만 보여줘” when you want a read-only critique or options without implementation.

Keep the app's product-specific documents in that app's own GitHub repository. Design Team uses the templates in `skills/design-team/templates/` only when the app lacks an equivalent authoritative document.

## Environment boundary

The skill guides design and front-end work. It does not require local macOS development, Supabase access, Cloudflare credentials, or signing tools. Use the Mac mini only for signing tasks that require it.
