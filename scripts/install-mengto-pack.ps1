$ErrorActionPreference = "Stop"

$repo = "https://github.com/MengTo/Skills"
$skills = @(
  "design-first-ui-prompting",
  "landing-page",
  "build-awwwards-quality-sites",
  "clean-minimal-beige-light-mode",
  "framed-tech-dark-border-gradient",
  "editorial-tech",
  "dark-glass-clean-layout",
  "agency-grid-layout-minimal",
  "cinematic-scroll-storytelling",
  "gsap-scrolltrigger-storytelling",
  "product-proof-saas",
  "stitched-full-page-capture",
  "audit-reference-originality"
)

foreach ($skill in $skills) {
  Write-Host "Installing $skill..."
  npx skills add $repo --skill $skill --global --agent codex
  if ($LASTEXITCODE -ne 0) {
    throw "Failed to install $skill"
  }
}

Write-Host ""
Write-Host "MengTo Web Pattern Pack installed."
Get-ChildItem "$env:USERPROFILE\.agents\skills" -Directory |
  Where-Object { $_.Name -in $skills } |
  Select-Object -ExpandProperty Name
