# Thinking + Research Framework

> **증거 기반 체계적 문제 해결 시스템**

[thinking-framework](https://github.com/tempuss/thinking-framework)의 15가지 체계적 사고법과 [web-research](https://github.com/tempuss/web-research)의 증거 기반 검증을 결합한 통합 컬렉션입니다.

---

## 🎯 핵심 개념

### 문제: 불완전한 분석
```
❌ 논리만으로 분석  →  현실과 맞지 않는 결정
❌ 데이터만으로 분석  →  의미 있는 구조 부족
```

### 해결: 증거 기반 체계적 사고
```
✅ 사고법(구조) + 연구(증거)  →  신뢰도 높은 결정
   thinking-framework  +  web-research  =  thinking-research-framework
```

---

## 📦 설치

### 옵션 1: 통합 컬렉션 설치 (권장)

한 번에 thinking-framework + web-research를 함께 설치:

```bash
prpm install collections/thinking-research-framework
```

**이상적인 경우:**
- 신규 프로젝트 시작
- 증거 기반 의사결정이 중요한 팀
- 완벽한 문제 해결 시스템 원함

---

### 옵션 2: 개별 설치 (선택적)

필요한 것만 개별 설치:

```bash
# 사고법만 사용
prpm install thinking-framework

# 연구만 사용
prpm install web-research

# 둘 다 개별 설치
prpm install thinking-framework web-research
```

**이상적인 경우:**
- 기존 프로젝트에 추가
- 특정 기능만 필요
- 유연한 구성 선호

---

## 🚀 빠른 시작

### 1단계: 사고법으로 분석

예: 고객 이탈 문제 해결

```
① Problem Definition: 문제를 정확히 정의
   → "이탈율 8%인데 업계 평균 3%"
   → "중점 고객층의 약한 온보딩이 원인"

② 적절한 사고법 선택: 프로세스 개선 (Pareto)
   → 이탈 원인 분석: 온보딩 60%, 기능 35%, 지원 20%

③ Action Plan: 증거 기반 우선순위
   → 온보딩 개선 (가장 높은 영향도)
```

### 2단계: 연구로 검증

```
④ Research: 증거 수집 (선택사항)
   → 온보딩 개선의 실제 효과 (업계 사례: 70% 성공률)
   → 현실적인 목표 설정 (단순 추측이 아닌 데이터 기반)

⑤ Confidence Scoring: 신뢰도 평가
   → 방법 신뢰도: 85% (Pareto 분석 정확도)
   → 증거 신뢰도: 75% (업계 벤치마크)
   → 최종 신뢰도: 64% (의사결정 자신감)
```

### 3단계: 확신을 가지고 실행

```
⑥ Execution: 데이터 기반 의사결정
   → "75% 신뢰로 온보딩 개선에 집중"
   → 실패 위험은 있지만 근거 있는 선택
```

---

## 📚 문서 구조

```
thinking-research-framework/
├── README.md                          # ← 지금 보는 파일
├── GUIDE.md                           # 실용적 사용 가이드
├── prpm.json                          # 컬렉션 정의
│
├── reference/
│   ├── research-tips.md               # 사고법별 연구 팁
│   └── confidence-scoring.md          # 신뢰도 계산 가이드
│
├── templates/
│   ├── research-strategy-worksheet.md # 리서치 계획 워크시트
│   └── research-combined-workflow.md  # 통합 워크플로우 템플릿
│
└── examples/
    ├── 01-market-entry.md            # 시장 진출 전략
    ├── 02-performance-optimization.md # 성능 최적화
    ├── 03-customer-retention.md       # 고객 유지 전략
    └── 04-technology-selection.md     # 기술 선택
```

---

## 🎓 사용 패턴

### 패턴 1: 빠른 의사결정 (1-2시간)

```
문제 정의 → 적절한 사고법 선택 → 빠른 분석 → 의사결정
(연구 최소화, 시간 중심)
```

**예:** "이번 분기 기능 우선순위 정하기"
- 사고법: Pareto (20/80 원칙)
- 연구: 내부 데이터만 활용
- 신뢰도: 중간 (내부 정보만)

---

### 패턴 2: 전략적 의사결정 (1-3일)

```
문제 정의 → 시장/경쟁 연구 → 사고법 적용 → 신뢰도 평가 → 의사결정
(충분한 증거, 정확도 중심)
```

**예:** "새로운 시장에 진출할 것인가?"
- 사고법: SWOT + GAP Analysis
- 연구: 시장 규모, 경쟁사, 규제 환경
- 신뢰도: 높음 (Tier 1 출처 활용)

---

### 패턴 3: 혁신/문제 해결 (3-7일)

```
문제 정의 → 기술 연구 → 사용자 리서치 → 사고법 적용 → 신뢰도 평가 → 실행
(포괄적 증거, 신뢰도 높음)
```

**예:** "신제품 개발 가능성 평가"
- 사고법: Design Thinking + First Principles
- 연구: 사용자 니즈, 기술 제약, 경쟁 동향
- 신뢰도: 매우 높음 (다층 검증)

---

## 🔑 주요 기능

### 1️⃣ 15가지 증명된 사고법
- **근본원인 분석**: 5 Why, Fishbone Diagram
- **혁신**: SCAMPER, TRIZ, Design Thinking, First Principles
- **전략 계획**: SWOT, GAP Analysis
- **프로세스 개선**: Pareto, PDCA, DMAIC
- **의사결정**: OODA Loop, Kepner-Tregoe
- **종합**: Dialectic Synthesis

### 2️⃣ 연구 기반 검증
- 사고법별 최적화된 리서치 전략
- 출처 신뢰도 계층화 (Tier 1-4)
- 신뢰도 점수 계산 시스템
- 의사결정 자신감 평가

### 3️⃣ 실제 사용 사례
- 시장 진출 전략
- 성능 최적화
- 고객 유지
- 기술 선택
- 조직 변화

### 4️⃣ 템플릿과 워크시트
- 리서치 전략 계획 양식
- 통합 워크플로우 템플릿
- 신뢰도 평가 체크리스트

---

## 💡 핵심 가치

### thinking-framework만 사용하면?
✅ 체계적 분석
❌ 외부 맥락 부족
❌ 중간 신뢰도

### web-research만 사용하면?
✅ 풍부한 증거
❌ 분석 구조 부족
❌ 실행 어려움

### 둘을 함께 사용하면?
✅ 체계적 분석 + 외부 증거
✅ 높은 신뢰도
✅ 실행 가능한 인사이트
✅ **진정한 증거 기반 의사결정**

---

## 🎯 누가 사용하나?

| 대상 | 이상적인 경우 |
|------|-------------|
| **신규 팀** | "우리 팀의 표준 문제 해결 프로세스를 만들고 싶다" |
| **스타트업** | "제한된 데이터로 빠르고 확실한 의사결정을 해야 한다" |
| **제품팀** | "사용자 니즈와 시장 데이터를 기반으로 개발하고 싶다" |
| **경영진** | "신뢰할 수 있는 전략 수립 프로세스를 원한다" |
| **엔지니어** | "기술 선택을 데이터 기반으로 하고 싶다" |

---

## 📖 다음 단계

1. **[GUIDE.md](GUIDE.md)** 읽기 - 실용적 사용 방법
2. **[examples/](examples/)** 검토 - 실제 사용 사례 학습
3. **[templates/](templates/)** 활용 - 워크시트로 직접 적용
4. **[reference/](reference/)** 참고 - 상세 가이드

---

## 🔗 관련 스킬

- **[thinking-framework](https://github.com/tempuss/thinking-framework)** - 15가지 사고법
- **[web-research](https://github.com/tempuss/web-research)** - 증거 기반 연구

---

## 📝 라이선스

MIT

---

**Version**: 1.0.0
**Last Updated**: 2025-11-07
**Maintained by**: @tempuss
