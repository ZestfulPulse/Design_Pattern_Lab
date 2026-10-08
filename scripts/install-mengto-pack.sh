#!/usr/bin/env bash
set -euo pipefail

repo="https://github.com/MengTo/Skills"
skills=(
  design-first-ui-prompting
  landing-page
  build-awwwards-quality-sites
  clean-minimal-beige-light-mode
  framed-tech-dark-border-gradient
  editorial-tech
  dark-glass-clean-layout
  agency-grid-layout-minimal
  cinematic-scroll-storytelling
  gsap-scrolltrigger-storytelling
  product-proof-saas
  stitched-full-page-capture
  audit-reference-originality
)

for skill in "${skills[@]}"; do
  echo "Installing $skill..."
  npx skills add "$repo" --skill "$skill" --global --agent codex
done

echo
echo "MengTo Web Pattern Pack installed."
for skill in "${skills[@]}"; do
  if [ -f "$HOME/.agents/skills/$skill/SKILL.md" ]; then
    echo "$skill"
  fi
done
