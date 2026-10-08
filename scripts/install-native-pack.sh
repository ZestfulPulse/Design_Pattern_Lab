#!/usr/bin/env bash
set -euo pipefail

echo "Installing design-swiftui-interfaces..."
npx skills add https://github.com/ZHUOLIN0928/swiftui-interface-design-skill --skill design-swiftui-interfaces --global --agent codex

echo "Installing swift-ui-design..."
npx skills add https://github.com/flatoy/swift-ui-design --skill swift-ui-design --global --agent codex

echo
echo "Native / SwiftUI Pattern Pack installed."
for skill in design-swiftui-interfaces swift-ui-design; do
  if [ -f "$HOME/.agents/skills/$skill/SKILL.md" ]; then
    echo "$skill"
  fi
done
