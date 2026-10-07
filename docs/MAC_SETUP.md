# Mac / SSH setup

Use this setup when the active product repository and Codex session run on a Mac, including the common workflow where Windows is the control surface and the Mac mini is reached through SSH.

## Preflight

These checks are read-only:

```bash
echo "=== GLOBAL AGENT SKILLS ==="
find ~/.agents/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null

echo
echo "=== DESIGN TOOLS ==="
command -v uipro || true
python3 --version
node --version
npm --version
```

A pre-existing `design-team` skill should be reviewed before reinstalling. Other skill names can coexist under `~/.agents/skills`.

## Install or update Design Team

The repository is public, so a normal HTTPS clone does not require repository access credentials:

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

Verify:

```bash
find ~/.agents/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null
```

Expected entry:

```text
~/.agents/skills/design-team/SKILL.md
```

## visual-inspiration-research

Install the free/public reference-research specialist used by DPL in place of Refero:

```bash
npx skills remove refero-design --global --agent codex -y
npx skills add https://github.com/Eldergenix/Codex-Design --skill visual-inspiration-research --global --agent codex
```

If `refero-design` is not installed, the remove command may simply report that there is nothing to remove. Use public/free sources by default. Paid or partly paid galleries mentioned upstream are optional, not DPL dependencies.

## UI UX Pro Max

If `uipro` is not already available on the Mac user that runs Codex:

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai universal --global
```

Verify:

```bash
command -v uipro
uipro --version
```

## Existing local design tools

Design Team is the single user-facing command. Existing specialist tools may remain where they are, including local tools under `~/projects/tools`.

Recommended hierarchy:

```text
User
  ↓
Design Team
  ↓
DPL orchestration
  ├─ Huashu Design
  ├─ UI UX Pro Max
  ├─ visual-inspiration-research
  ├─ Hallmark-inspired checks
  ├─ Infographic tooling
  └─ other available design references
  ↓
Active product repository
```

Do not duplicate or relocate specialist repositories merely to install Design Team. Design Team should discover and selectively use what is available in the active environment.

## Use over SSH

Example:

```bash
ssh <host>
cd ~/projects/<product-repository>
codex
```

Then invoke:

> 디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘. 제품 문서와 현재 구현을 먼저 읽고, 필요한 디자인 엔진만 선택해서 수정한 뒤 실제 렌더 결과를 검증해줘.

The active product repository remains the source of truth. Design Team should not create a parallel design system when authoritative product documents already exist.

## Safety boundary

An ordinary design request may edit UI and front-end presentation, but it must not silently change backend contracts, authentication, data structures, routes, dependencies, deployment configuration, secrets, or production infrastructure.

Signing-specific work still requires macOS. Mac mini may also be the normal development host for SSH-based products.
