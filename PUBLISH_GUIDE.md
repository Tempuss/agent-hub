# Skills Publishing Guide

> **최종 업데이트**: 2025-11-06
> **배포 상태**: ✅ 8/8 스킬 배포 가능
> **Author**: Tempuss | **License**: MIT

이 가이드는 agent-hub의 skills 패키지를 PRPM 레지스트리에 publish하는 방법을 설명합니다.

## 🎯 빠른 시작

```bash
# 전체 배포 전 검증
./scripts/publish-all-skills.sh --dry-run

# 전체 배포
./scripts/publish-all-skills.sh

# 개별 스킬 배포
./scripts/publish-skill.sh ai-persona-creator
```

## 📦 패키지 구조

```
skills/
├── ai-persona-creator/          ✅ prpm.json (v2.0.0, 17.32KB)
├── thinking-framework/          ✅ prpm.json (v2.0.0, 22.28KB)
├── web-research/               ✅ prpm.json (v1.0.0, 24.33KB)
├── doc-organizer/              ✅ prpm.json (v1.0.0, 4.70KB)
├── template-generator/         ✅ prpm.json (v1.0.0, 7.51KB)
├── market-strategy/            ✅ prpm.json (v1.0.0, 8.98KB)
├── roi-analyzer/               ✅ prpm.json (v1.0.0, 7.96KB)
└── toss-patterns/              ✅ prpm.json (v1.0.0, 14.80KB)
```

**총 8개의 독립적인 skill 패키지**

### 📋 메타데이터

- **Author**: Tempuss (모든 스킬 통일)
- **License**: MIT (모든 스킬 통일)
- **Format**: claude
- **Subtype**: skill
- **배포 상태**: ✅ 8/8 스킬 배포 가능

## 🚀 Publishing 방법

### 방법 1: 개별 패키지 Publish (추천)

**자동화 스크립트 사용:**
```bash
# Dry-run으로 검증
./scripts/publish-skill.sh web-research --dry-run

# 실제 publish
./scripts/publish-skill.sh web-research

# Beta 태그로 publish
./scripts/publish-skill.sh web-research --tag beta
```

**수동 publish:**
```bash
# 패키지 디렉토리로 이동
cd skills/web-research

# Dry-run 검증
prpm publish --dry-run

# Publish
prpm publish

# 특정 태그로 publish
prpm publish --tag beta
```

### 방법 2: 전체 패키지 한 번에 Publish

```bash
# 모든 패키지 dry-run 검증
./scripts/publish-all-skills.sh --dry-run

# 모든 패키지 publish
./scripts/publish-all-skills.sh

# 모든 패키지를 beta 태그로 publish
./scripts/publish-all-skills.sh --tag beta
```

## 📝 워크플로우

### 일반적인 개발 → Publish 워크플로우

1. **패키지 수정**
   ```bash
   vim skills/web-research/SKILL.md
   ```

2. **버전 업데이트**
   ```bash
   vim skills/web-research/prpm.json
   # version을 예: "1.0.0" → "1.0.1"로 변경
   ```

3. **검증 (Dry-run)**
   ```bash
   ./scripts/publish-skill.sh web-research --dry-run
   ```

4. **Publish**
   ```bash
   ./scripts/publish-skill.sh web-research
   ```

5. **Git Commit**
   ```bash
   git add skills/web-research/
   git commit -m "Update web-research skill v1.0.1"
   git push
   ```

### 새 패키지 추가 시

1. **패키지 디렉토리 생성**
   ```bash
   mkdir -p skills/new-skill
   ```

2. **prpm.json 생성**
   ```bash
   cd skills/new-skill
   prpm init
   # 또는 기존 패키지의 prpm.json을 복사 후 수정
   ```

3. **prpm.json 필수 필드 설정**
   ```json
   {
     "name": "new-skill",
     "version": "1.0.0",
     "description": "상세한 설명 (최소 100자 권장)",
     "author": "Tempuss",
     "license": "MIT",
     "format": "claude",
     "subtype": "skill",
     "tags": ["tag1", "tag2"],
     "files": [
       "SKILL.md",
       "README.md"
     ]
   }
   ```

4. **파일 경로 주의사항**
   - ✅ 패키지 디렉토리 기준 상대 경로: `"SKILL.md"`, `"README.md"`
   - ❌ 절대 경로 사용 금지: `"skills/new-skill/SKILL.md"`
   - ✅ 하위 디렉토리: `"reference/guide.md"`

5. **Publish 스크립트 업데이트**
   ```bash
   vim scripts/publish-all-skills.sh
   # PACKAGES 배열에 "new-skill" 추가

   vim prpm.json
   # packages 배열에 "skills/new-skill/prpm.json" 추가
   ```

## 🎯 사용 가능한 패키지 목록

| 패키지명 | 버전 | 크기 | Author | 설명 |
|---------|------|------|--------|------|
| ai-persona-creator | 2.0.0 | 17.32KB | Tempuss | 심리학 기반 페르소나 분석 (7개 프레임워크) |
| thinking-framework | 2.0.0 | 22.28KB | Tempuss | 14가지 사고 프레임워크 |
| web-research | 1.0.0 | 24.33KB | Tempuss | OSINT 웹 리서치 프레임워크 |
| doc-organizer | 1.0.0 | 4.70KB | Tempuss | 문서 조직화 도구 |
| template-generator | 1.0.0 | 7.51KB | Tempuss | 템플릿 생성 시스템 |
| market-strategy | 1.0.0 | 8.98KB | Tempuss | 시장 전략 분석 |
| roi-analyzer | 1.0.0 | 7.96KB | Tempuss | ROI 분석 프레임워크 |
| toss-patterns | 1.0.0 | 14.80KB | Tempuss | Toss 스타일 개발 패턴 |

**배포 상태**: ✅ 모든 패키지 배포 준비 완료 (dry-run 테스트 통과)

## 🔧 스크립트 상세

### publish-skill.sh

개별 패키지를 publish하는 스크립트

**사용법:**
```bash
./scripts/publish-skill.sh <package-name> [options]

Options:
  --dry-run    실제 publish 없이 검증만 수행
  --tag TAG    특정 태그로 publish (예: beta, latest)
```

**예시:**
```bash
./scripts/publish-skill.sh ai-persona-creator --dry-run
./scripts/publish-skill.sh web-research --tag beta
./scripts/publish-skill.sh market-strategy
```

### publish-all-skills.sh

모든 패키지를 한 번에 publish하는 스크립트

**사용법:**
```bash
./scripts/publish-all-skills.sh [options]

Options:
  --dry-run    모든 패키지를 실제 publish 없이 검증
  --tag TAG    모든 패키지를 특정 태그로 publish
```

**예시:**
```bash
# 전체 검증
./scripts/publish-all-skills.sh --dry-run

# 전체 publish
./scripts/publish-all-skills.sh

# 전체 beta publish
./scripts/publish-all-skills.sh --tag beta
```

## 🔐 인증

Publish 전에 PRPM에 로그인해야 합니다:

```bash
prpm login
```

현재 로그인 상태 확인:
```bash
prpm whoami
```

## 📊 Publish 후 확인

```bash
# 레지스트리에서 패키지 검색
prpm search web-research

# 패키지 정보 확인
prpm info web-research

# 설치 테스트
prpm install web-research
```

## ⚠️ 주의사항

1. **버전 관리**
   - Semantic Versioning 사용 (major.minor.patch)
   - 이미 publish된 버전은 덮어쓸 수 없음
   - 새로운 버전을 publish하려면 prpm.json의 version을 증가시켜야 함

2. **파일 경로**
   - prpm.json의 files 배열은 패키지 디렉토리 기준 상대 경로
   - 절대 경로나 `skills/` prefix 사용 금지

3. **메타데이터 통일**
   - Author: **Tempuss** (모든 스킬 통일)
   - License: **MIT** (모든 스킬 통일)
   - Format: **claude**, Subtype: **skill**

4. **Description 작성**
   - 최소 100자 이상 권장
   - 스킬의 사용 시점, 해결하는 문제 포함
   - Claude의 자동 활성화를 위한 키워드 포함

5. **Dry-run 필수**
   - 실제 publish 전에 항상 `--dry-run`으로 검증
   - 오류 확인 및 수정 후 publish

6. **Git Workflow**
   - Publish 후 반드시 git commit
   - 버전 태그 생성 권장: `git tag v1.0.1`

## ✅ 배포 전 체크리스트

```bash
# 1. 모든 스킬 dry-run 테스트
./scripts/publish-all-skills.sh --dry-run

# 2. Author 및 License 확인
for f in skills/*/prpm.json; do
  echo "$f: $(jq -r '.author, .license' $f | paste -sd ' ' -)"
done

# 3. 파일 존재 여부 확인
python3 scripts/verify-packages.py  # (옵션)

# 4. 최종 확인
- [ ] 모든 prpm.json의 author가 "Tempuss"
- [ ] 모든 prpm.json의 license가 "MIT"
- [ ] 모든 파일이 존재함 (files 배열 검증)
- [ ] dry-run 테스트 통과
- [ ] 버전 번호 확인
```

## 📊 최신 검증 결과 (2025-11-06)

```bash
$ ./scripts/publish-all-skills.sh --dry-run

✅ ai-persona-creator@2.0.0 (17.32KB) - Ready
✅ thinking-framework@2.0.0 (22.28KB) - Ready
✅ web-research@1.0.0 (24.33KB) - Ready
✅ doc-organizer@1.0.0 (4.70KB) - Ready
✅ template-generator@1.0.0 (7.51KB) - Ready
✅ market-strategy@1.0.0 (8.98KB) - Ready
✅ roi-analyzer@1.0.0 (7.96KB) - Ready
✅ toss-patterns@1.0.0 (14.80KB) - Ready

📊 Summary: ✅ Successful: 8/8
```

**모든 스킬이 배포 가능합니다!** 🎉

## 🐛 트러블슈팅

### "No manifest file found" 에러

**원인:** 패키지 디렉토리가 아닌 곳에서 실행
**해결:** 패키지 디렉토리로 이동하거나 스크립트 사용

### "File not found" 경고

**원인:** prpm.json의 files 경로가 잘못됨
**해결:** 패키지 디렉토리 기준 상대 경로로 수정

### 버전 충돌

**원인:** 동일한 버전이 이미 publish됨
**해결:** prpm.json의 version을 증가시키고 다시 publish

## 📚 참고 자료

- [PRPM 공식 문서](https://docs.prpm.dev)
- [PRPM GitHub](https://github.com/prompt-package-manager/prpm)
- [Semantic Versioning](https://semver.org/)
