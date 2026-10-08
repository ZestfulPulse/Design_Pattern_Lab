$ErrorActionPreference = "Stop"

$skills = @(
  @{
    Repo = "https://github.com/ZHUOLIN0928/swiftui-interface-design-skill"
    Skill = "design-swiftui-interfaces"
  },
  @{
    Repo = "https://github.com/flatoy/swift-ui-design"
    Skill = "swift-ui-design"
  }
)

foreach ($item in $skills) {
  Write-Host "Installing $($item.Skill)..."
  npx skills add $item.Repo --skill $item.Skill --global --agent codex
  if ($LASTEXITCODE -ne 0) {
    throw "Failed to install $($item.Skill)"
  }
}

Write-Host ""
Write-Host "Native / SwiftUI Pattern Pack installed."
Get-ChildItem "$env:USERPROFILE\.agents\skills" -Directory |
  Where-Object { $_.Name -in @("design-swiftui-interfaces", "swift-ui-design") } |
  Select-Object -ExpandProperty Name
