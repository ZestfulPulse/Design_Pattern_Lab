"""Conservative DPL UI-task router. No side effects or network calls."""
from dataclasses import dataclass
import re

UI_TERMS = (
    "ui", "ux", "design", "layout", "responsive", "accessibility",
    "screen", "component", "typography", "spacing", "animation",
    "mobile", "interface", "디자인", "화면", "레이아웃", "반응형",
    "접근성", "컴포넌트", "모바일", "버튼", "탭", "가독성",
    "스타일", "색상", "애니메이션", "인터랙션", "네비게이션",
)
NON_UI_TERMS = ("database", "migration", "sql", "backend", "api", "deploy",
                "secret", "billing", "security", "db", "데이터베이스",
                "마이그레이션", "배포", "보안", "결제", "서버")
UI_EXTENSIONS = (".tsx", ".jsx", ".css", ".scss", ".vue", ".svelte", ".swift",
                 ".kt", ".xml")
UI_DIRS = ("components/", "screens/", "views/", "app/", "pages/", "ui/")
IGNORED_PATHS = ("node_modules/", "dist/", "build/", ".next/", "vendor/")

@dataclass(frozen=True)
class RoutingDecision:
    route: str
    reason: str
    evidence: tuple[str, ...]

def _mentions(text, terms):
    value = text.casefold()
    return tuple(term for term in terms if re.search(
        r"(?<![a-z])" + re.escape(term) + r"(?![a-z])" if term.isascii()
        else re.escape(term), value))

def classify_task(request: str, changed_paths=(), explicit_design=False) -> RoutingDecision:
    """Return design_team, inspect, or skip. Path inference never authorizes edits."""
    if not isinstance(request, str):
        raise TypeError("request must be a string")
    paths = tuple(str(p).replace("\\", "/").lstrip("./") for p in changed_paths)
    paths = tuple(p for p in paths if not any(p.startswith(d) for d in IGNORED_PATHS))
    hits = _mentions(request, UI_TERMS)
    backend = _mentions(request, NON_UI_TERMS)
    ui_paths = tuple(p for p in paths if p.lower().endswith(UI_EXTENSIONS)
                     and ("/" in p or p.lower().endswith((".css", ".scss", ".swift", ".kt"))))
    if explicit_design or hits:
        return RoutingDecision("design_team", "explicit UI/design intent", hits or ("explicit_design",))
    if ui_paths and not backend:
        return RoutingDecision("inspect", "UI files changed; determine if changes are visual", ui_paths)
    if ui_paths and backend:
        return RoutingDecision("inspect", "mixed backend and UI paths; inspect scope", ui_paths + backend)
    if backend:
        return RoutingDecision("skip", "non-design task", backend)
    return RoutingDecision("skip", "no UI signal", ())

if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("--path", action="append", default=[])
    parser.add_argument("--explicit-design", action="store_true")
    args = parser.parse_args()
    result = classify_task(args.request, args.path, args.explicit_design)
    print(json.dumps({"route": result.route, "reason": result.reason,
                      "evidence": result.evidence}, ensure_ascii=False))
