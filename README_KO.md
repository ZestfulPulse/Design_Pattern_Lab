# Design Pattern Lab

> **AI 코딩 에이전트를 위한 전역 디자인 총괄 시스템**  
> 제품 철학을 먼저 읽고, 필요한 디자인 지식만 골라 쓰며, 실제 렌더 결과로 검증합니다.

<p align="center">
  <strong>한 번의 호출. 하나의 디자인팀. 제품 철학이 최우선.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> · <strong>한국어</strong>
</p>

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘.
```

**Design Pattern Lab(DPL)**은 컴포넌트 모음집도 아니고, 또 하나의 거대한 스타일 라이브러리도 아닙니다.

DPL은 현재 **Codex용으로 패키징되고 문서화된 product-first 디자인 오케스트레이션 계층**입니다. 구조 자체는 다른 코딩 에이전트에도 확장할 수 있지만, 아직 그 호환성을 문서화하거나 검증하지는 않았습니다.

DPL은 현재 작업 중인 제품을 먼저 읽고, 실제 디자인 문제가 무엇인지 판단한 뒤, 필요한 내부 능력과 외부 전문 소스만 선택합니다. 그 다음 하나의 일관된 방향으로 구현하고, 실제 렌더 결과를 검증합니다.

---

## 왜 DPL이 필요한가

AI가 만든 제품이 자꾸 비슷해지는 이유 중 하나는 **컴포넌트는 많이 주면서 디자인 판단 기준은 주지 않기 때문**입니다.

DPL은 순서를 반대로 둡니다.

```text
일반적인 스타일 라이브러리
        ↓
      제품
```

대신:

```text
제품 철학
        ↓
현재 UX / 토큰 / 동작
        ↓
Design Team
        ↓
정말 필요한 디자인 지식만 선택
        ↓
구현
        ↓
렌더 증거
```

**라이브러리가 제품을 결정하지 않습니다. 제품이 디자인을 결정합니다.**

---

## 어떻게 동작하나

```text
사용자
  ↓
"디자인팀"
  ↓
현재 제품 분석
  ↓
실제 디자인 문제 진단
  ↓
내장 능력 + 필요한 전문 소스 선택
  ↓
하나의 방향으로 통합
  ↓
현재 제품 저장소에 구현
  ↓
Visual Release Review
  ↓
PASS / PASS_WITH_WARNING / FAIL / NOT_VERIFIED
```

사용자가 서로 겹치는 여러 디자인 에이전트 중 하나를 직접 고를 필요가 없습니다.

**Design Team이 단 하나의 진입점**입니다. 외부 도구는 의사결정자가 아니라 필요한 순간에 호출되는 전문 기여자입니다.

---

## 5개의 핵심 내장 능력

DPL은 내부 능력을 의도적으로 작고 명확하게 유지합니다.

| 능력 | 역할 |
|---|---|
| **Component State Auditor** | default, focus, loading, error, empty, overflow, responsive, keyboard, touch 등 필요한 UI 상태 누락을 점검 |
| **Design System Ingestor** | 외부 `DESIGN.md`나 디자인 시스템을 읽고 **KEEP / ADAPT / REJECT**로 분류 |
| **Interaction Physics** | 모션이 단순 장식이 아니라 인과관계, 연속성, 직접 조작감, 피드백을 설명하도록 판단 |
| **Accessibility Gate** | semantics, focus, contrast, reflow, target size, reduced motion, 플랫폼 접근성 요소를 점검 |
| **Visual Release Review** | 실제 렌더 결과를 보고 증거에 따라 **PASS / PASS_WITH_WARNING / FAIL / NOT_VERIFIED** 판정 |

이 5개는 Design Team 내부에 들어 있는 능력입니다. **사용자가 별도로 설치하거나 호출하는 5개의 스킬이 아닙니다.**

→ [핵심 능력 명세](skills/design-team/references/CORE_CAPABILITIES.md)

---

## 증거가 Design Team의 판단에 제동을 걸 수 있습니다

DPL은 선택적으로 **구조화된 검증 경로**를 사용할 수 있습니다.

제품 철학의 일부를 검사 규칙으로 바꾸고, 실제 렌더 증거를 기록하고, 어떤 엔진을 실제로 사용했는지 추적하며, 최종적으로 **증거가 허용하는 최대 판정**을 계산합니다.

중요한 구분은 다음과 같습니다.

- **사람이 실제 렌더를 검토한 증거도 유효합니다.** 브라우저, 시뮬레이터, 실제 기기 등의 렌더 결과를 Design Team이 직접 확인한 경우 `review_mode: human_render`로 기록할 수 있습니다.
- `human_render`는 최소한 reviewer, environment, viewport, reviewed capture IDs, reviewed areas를 기록해야 합니다.
- **구조화 검증을 사용할 수 있다면 더 강한 검증이 가능합니다.** 과장된 판정, Before/After 데이터 불일치, 누락된 증거, 거짓 엔진 사용 주장, 범위 위반 등을 잡을 수 있습니다.
- **`NOT_VERIFIED`는 렌더 증거가 부족해 판단할 수 없다는 뜻**입니다. 검증 도구가 없다는 뜻이 아닙니다.
- **harness 모드에서 철학 검사가 하나도 없으면** `NO_PHILOSOPHY_CHECKS`로 최대 `PASS_WITH_WARNING`입니다.
- 완전한 `human_render` 기록은 철학 검사가 없어도 `PASS`에 도달할 수 있습니다.
- 철학 검사 작성 시점의 문서 해시와 현재 문서 해시가 다르면 `CHECKS_STALE`로 최대 `PASS_WITH_WARNING`입니다.

내부 검증 도구는 `tools/dpl/` 아래에 있습니다. 이 도구들은 Design Team의 내부 구성요소이며, 새로운 사용자용 스킬이 아닙니다.

→ [Evidence and Verdict 계약](skills/design-team/references/EVIDENCE_AND_VERDICT.md)  
→ [Philosophy Checks 가이드](skills/design-team/references/PHILOSOPHY_CHECKS.md)

---

## 제품의 진실이 항상 우선합니다

DPL은 다음 우선순위를 따릅니다.

1. 사용자 지시
2. 승인된 제품 철학과 결정
3. 현재 routes, behavior, tokens, components, content
4. Design Team의 종합 판단
5. 전문 디자인 엔진과 레퍼런스
6. 일반적인 디자인 기본값

이미 정체성이 잡힌 제품을 새 디자인 라이브러리를 발견했다는 이유만으로 다시 꾸미지 않습니다.

외부 디자인 시스템이 유용한 경우에도 제품을 그 시스템으로 교체하지 않고, **현재 제품 언어로 번역해서 필요한 부분만 흡수**합니다.

---

## 전문 소스 라우팅

DPL은 작업에 실제 도움이 될 때만 외부 도구와 레퍼런스를 선택적으로 사용합니다.

| 소스 | 역할 |
|---|---|
| **Huashu Design** | 표현력 높은 비주얼 방향과 컨셉 탐색 |
| **UI UX Pro Max** | 디자인 시스템 및 구현 스택에 맞춘 가이드 |
| **Hallmark-inspired checks** | 웹 품질과 획일적인 AI UI 패턴 점검 |
| **Infographic tooling** | 밀도 높은 정보, 비교, 프로세스 시각화 |
| **visual-inspiration-research** | 대규모 디자인 변경 전 무료·공개 비주얼 레퍼런스를 조사 |
| **Component Gallery** | 컴포넌트 상태, 의미 구조, 성숙한 디자인 시스템 사례 비교 |
| **21st.dev** | 디자인 방향이 승인된 뒤 React/Tailwind 구현 참고에 선택적으로 사용 |
| **MengTo Web Pattern Pack** | 제품 방향 결정 후에만 사용하는 웹 레이아웃·시각 스타일·모션·증거·캡처 구현 패턴 묶음 |
| **제품 내부 디자인 문서** | 제품 철학이 이미 정의되어 있다면 가장 중요한 소스 |

여러 엔진을 많이 쓰는 것이 목표가 아닙니다.

작은 정보 위계 문제라면 외부 디자인 엔진을 하나도 쓰지 않을 수 있습니다. 큰 리디자인이라면 여러 소스를 조합할 수 있습니다. 최종 방향은 항상 Design Team이 하나로 통합합니다.

→ [디자인 엔진 라우팅](skills/design-team/references/DESIGN_ENGINES.md)

---

## Showcase 01 · Legs of Steel

**제품:** 정밀 러닝 분석 및 코칭 앱  
**디자인 개입:** 홈 화면 정보 위계  
**결과:** `PASS_WITH_WARNING`  
**증거 경고:** After 캡처는 Goal이 첫 번째라는 사실은 확인하지만, 전체 Goal → Workout → Month 순서를 시각적으로 증명하지는 못합니다. Before/After의 활동 데이터도 서로 달랐습니다.

제품 철학에서 의도한 순서는 다음과 같습니다.

```text
목표 격차
→ 오늘의 훈련과 안전
→ 보조 통계
```

기존 홈 순서는:

```text
이번 달
→ 오늘의 워크아웃
→ 목표까지
```

디자인 패스에서는 기존 비주얼 시스템, 비즈니스 로직, 데이터 흐름을 유지하면서 **목표 진행 정보를 첫 번째 위치로 이동**했습니다.

<table>
  <tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
  </tr>
  <tr>
    <td><img src="showcase/01-legs-of-steel/before.png" alt="Design Team 정보 위계 변경 전 Legs of Steel Home"></td>
    <td><img src="showcase/01-legs-of-steel/after.png" alt="Design Team 정보 위계 변경 후 Legs of Steel Home"></td>
  </tr>
</table>

### 이 사례가 보여주는 것

이 사례는 여러 디자인 엔진을 한 화면에 쏟아붓는 것을 보여주기 위한 사례가 아닙니다.

실제로 사용한 소스는:

- LoS 제품 철학
- 기존 LoS 디자인 토큰
- Design Team의 product-first 및 rendered-evidence 원칙

원래 LoS 변경을 만들 때 **DPL, Huashu, UI UX Pro Max, Hallmark, Refero는 사용하지 않았습니다.**

필요하지 않은 개입을 하지 않는 것 역시 Design Team의 능력입니다.

→ [Legs of Steel 전체 사례](showcase/01-legs-of-steel/README.md)

---

## 사용법

Design Team이 전역 설치된 제품 저장소에서 이렇게 말하면 됩니다.

```text
디자인팀, 이 화면을 제품 철학에 맞춰 수정해줘.
```

좀 더 구체적으로 요청해도 됩니다.

```text
디자인팀, 현재 정보 구조는 유지하고
이 화면이 정밀한 분석 도구처럼 느껴지도록 개선해줘.
기능과 데이터 흐름은 바꾸지 말고 실제 렌더까지 검증해줘.
```

구현 없이 검토만 요청할 수도 있습니다.

```text
디자인팀, 구현은 하지 말고 이 화면의 UX 문제만 검토해줘.
```

---

## 설치

### Windows

```powershell
$repoPath = "$env:USERPROFILE\projects\Design_Pattern_Lab"

if (Test-Path $repoPath) {
  Set-Location $repoPath
  git pull --ff-only
} else {
  git clone https://github.com/ZestfulPulse/Design_Pattern_Lab.git $repoPath
  Set-Location $repoPath
}

npx skills add . --skill design-team --global --agent codex
```

→ [Windows 설치 가이드](docs/WINDOWS_SETUP.md)

### Mac / SSH 환경

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

→ [Mac / SSH 설치 가이드](docs/MAC_SETUP.md)

Codex가 Windows 로컬 제품을 직접 수정한다면 Windows Codex 세션에서 Design Team을 호출합니다.

Windows가 단순 제어 화면이고 실제 제품 저장소가 SSH로 접속한 Mac에 있다면, Mac 쪽 Codex 세션에서 Design Team을 호출합니다.

**같은 팀. 같은 규칙. 다른 작업대.**

---

## 선택형 전문 엔진

### 비주얼 레퍼런스 조사 스킬

DPL은 Refero의 유료 레퍼런스 조사 역할을 `visual-inspiration-research`로 교체합니다. Refero 구독은 필요하지 않습니다.

```bash
npx skills remove refero-design --global --agent codex -y
npx skills add https://github.com/Eldergenix/Codex-Design --skill visual-inspiration-research --global --agent codex
```

기본적으로 무료·공개 접근 가능한 레퍼런스 소스를 우선합니다. 상류 스킬이 유료 또는 부분 유료 갤러리를 언급하더라도 사용자가 이미 접근권을 가진 경우가 아니면 DPL의 필수 경로로 사용하지 않습니다.

### MengTo Web Pattern Pack

DPL은 [MengTo/Skills](https://github.com/MengTo/Skills)에서 웹 구현에 직접 도움이 되는 스킬만 골라 선택적으로 사용할 수 있습니다. 상류 저장소는 MIT 라이선스입니다.

선별 패키지 설치:

**Windows**

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-mengto-pack.ps1
```

**Mac / Linux**

```bash
bash scripts/install-mengto-pack.sh
```

이 패키지는 제품 철학을 결정하는 권한이 없습니다. DPL이 먼저 제품 방향을 하나로 정한 뒤, 필요한 구현 패턴만 최소한으로 선택합니다.

→ [MengTo Web Pattern Pack 라우팅](skills/design-team/references/MENGTO_WEB_PATTERNS.md)

### UI UX Pro Max

UI UX Pro Max는 필요할 때 별도로 설치해 사용할 수 있습니다.

```bash
npm install -g ui-ux-pro-max-cli
uipro init --ai universal --global
```

DPL은 모든 전문 도구가 설치되어 있어야 동작하는 구조가 아닙니다.

---

## 저장소 구조

```text
Design_Pattern_Lab/
├─ README.md
├─ README_KO.md
├─ LICENSE
├─ .github/workflows/
│  └─ dpl-tests.yml
├─ docs/
│  ├─ WINDOWS_SETUP.md
│  └─ MAC_SETUP.md
├─ showcase/
│  └─ 01-legs-of-steel/
├─ tools/dpl/
│  ├─ verdict_gate.py
│  ├─ checks_runner.py
│  ├─ test_dpl.py
│  └─ philosophy.checks.sample.yaml
├─ evals/
│  └─ README.md
└─ skills/design-team/
   ├─ SKILL.md
   ├─ agents/
   ├─ schemas/
   │  ├─ evidence.schema.json
   │  ├─ ledger.schema.json
   │  └─ philosophy-checks.schema.json
   ├─ references/
   │  ├─ CORE_CAPABILITIES.md
   │  ├─ DESIGN_ENGINES.md
   │  ├─ EVIDENCE_AND_VERDICT.md
   │  ├─ PHILOSOPHY_CHECKS.md
   │  └─ SOURCE_ATTRIBUTION.md
   └─ templates/
```

제품별 철학, 토큰, 승인된 결정은 각각의 제품 저장소에 남습니다.

DPL은 제품 저장소 안에 **두 번째 진실 원천을 만들지 않습니다.**

---

## 외부 소스와 출처

DPL은 참고하거나 라우팅하는 외부 디자인 시스템, 라이브러리, 레퍼런스 프로젝트의 소유권을 주장하지 않습니다.

외부 소스는 다음처럼 구분합니다.

- **Tool / engine**: 실제 설치되어 있고 필요할 때 호출
- **Reference**: 패턴이나 원칙을 참고
- **Inspiration**: 상류 프로젝트를 통째로 포함하지 않고 DPL 능력 설계에 영향을 준 소스

예시는 Component Gallery, 21st.dev, MengTo/Skills, DESIGNmd, visual-inspiration-research, Huashu Design, UI UX Pro Max, Hallmark, Emil Kowalski의 design skills, Addy Osmani의 web-quality skills, Impeccable, shadcn/ui, Anime.js 등입니다.

**사용 가능하다는 것과 실제 사용했다는 것은 다릅니다.** 각 Showcase는 실제 사용한 소스만 명시해야 합니다.

→ [출처 및 영감 목록](skills/design-team/references/SOURCE_ATTRIBUTION.md)

---

## 디자인 작업의 경계

DPL은 사용자가 요청한 범위 안에서 presentation과 interaction을 개선할 수 있습니다.

하지만 다음을 조용히 변경해서는 안 됩니다.

- backend contracts
- authentication
- business logic
- data structures
- routes
- dependencies
- deployment configuration
- secrets

또한 다음을 사실처럼 주장해서도 안 됩니다.

- 실행하지 않은 외부 엔진을 사용했다고 주장
- 증거 없이 접근성 검증이 통과했다고 주장
- build나 lint가 통과했다는 이유만으로 visual QA가 통과했다고 주장
- 외부 프로젝트의 라이선스가 DPL 자체에 적용된다고 주장

---

## DPL의 디자인 철학

DPL은 몇 가지 원칙에 대해서는 분명한 입장을 가집니다.

**소스는 적게, 더 정확하게 사용합니다.**  
디자인 엔진을 많이 쓰는 것이 더 좋은 디자인을 의미하지 않습니다.

**제품의 정체성을 보존합니다.**  
외부 스타일 가이드는 입력일 뿐, 최종 권한이 아닙니다.

**모션에는 이유가 있어야 합니다.**  
애니메이션을 없애도 이해도가 전혀 떨어지지 않는다면 단순 장식일 수 있습니다.

**접근성은 출시 품질입니다.**  
나중에 덧붙이는 장식 단계가 아닙니다.

**선언보다 렌더 증거를 우선합니다.**  
빌드 성공은 디자인 성공의 증거가 아닙니다.

---

## 현재 상태

**DPL v1 기준선**

- 하나의 전역 Design Team
- 5개의 내장 핵심 능력
- 선택적 전문 소스 라우팅
- 명시적인 출처 관리
- Windows / Mac SSH 교차 환경 지원
- 실제 렌더 기반 검증
- 선택적 machine-checkable Verdict Gate 및 Run Provenance
- `human_render` / `harness` 검증 모드
- `NO_PHILOSOPHY_CHECKS` / `CHECKS_STALE` 경고 규칙
- 공개 Showcase 구조
- 내부 검증 도구용 테스트 및 GitHub Actions 구성

새 기능은 기존 능력과 중복되지 않으면서 **명확한 빈틈을 메울 때만** 추가하는 것을 원칙으로 합니다.

**현재 에이전트 지원:** Codex가 문서화되고 검증된 설치 대상입니다. 다른 코딩 에이전트 지원은 구조적으로 가능하지만 현재 호환성 주장에는 포함하지 않습니다.

---

## 라이선스

Design Pattern Lab 자체는 [MIT License](LICENSE)로 공개됩니다.

외부 도구, 저장소, 서비스, 에셋은 각각의 라이선스와 이용 조건을 따릅니다.
