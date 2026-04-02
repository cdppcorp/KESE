# Contributing to KESE-KIT

## 새 가이드라인 추가 방법

KESE-KIT은 **스킬 4개 고정 + 3-디렉터리 확장** 구조입니다. 새 보안 가이드라인을 추가할 때 스킬 파일을 수정할 필요 없이 `references/`, `templates/`, `scripts/` 디렉터리에 파일을 추가하면 됩니다.

### Step 1: 원본 문서 준비

```
authorkit/new pdf/           ← PDF 파일 배치
```

### Step 2: PDF를 Markdown으로 변환

```bash
python authorkit/convert_pdf.py "authorkit/new pdf/가이드라인.pdf" authorkit/converted/ref-XXX ref-XXX
```

### Step 3: References / Templates / Scripts 파일 작성

`skills-ko/kesekit-start-ko/` 아래 3개 디렉터리에 새 가이드라인 파일을 생성합니다:

```
skills-ko/kesekit-start-ko/
├── SKILL.md
├── references/new-guideline/   ← 순수 설명/기준 문서
│   ├── overview.md
│   ├── category-1.md
│   └── category-2.md
├── templates/new-guideline/    ← 별지 서식, 체크리스트 테이블
│   ├── assessment-table.md
│   └── checklist.md
└── scripts/new-guideline/      ← 실행 가능한 점검/수정 스크립트
    ├── check-linux.sh
    ├── check-windows.ps1
    └── fix-linux.sh
```

#### 디렉터리별 콘텐츠 배치 기준

| 디렉터리 | 들어가는 내용 | 예시 |
|-----------|--------------|------|
| `references/` | 순수 설명, 위협 기술, 가이드라인 본문, 판단 기준 (양호/취약) | 위협 시나리오 설명, 보안 요구사항 해설 |
| `templates/` | `코드\|항목\|중요도` 평가 항목 테이블, `□` 체크리스트, 채점 기준표 | 별지 서식, 컴플라이언스 체크리스트 |
| `scripts/` | 실행 가능한 bash/powershell/sql 점검·수정 명령어 | `check-linux.sh`, `fix-windows.ps1` |

> **참고**: 모든 가이드라인이 3개 디렉터리를 모두 사용하지는 않습니다.
> - `ai-security`, `space-security` 등은 `references/`를 사용합니다.
> - CII 등 체크리스트 중심 가이드라인은 `templates/`와 `scripts/`를 주로 사용합니다.
> - 새 가이드라인의 성격에 맞게 필요한 디렉터리만 생성하면 됩니다.

#### references/ 파일 작성 시 포함 사항
- 위협 설명 및 보안 요구사항
- 판단 기준 (양호/취약)
- 관련 표준·규격 출처

#### templates/ 파일 작성 시 포함 사항
- 항목 코드, 이름, 중요도 (`코드|항목|중요도` 테이블)
- 체크리스트 (`□` 형식)
- 채점·평가 기준표

#### scripts/ 파일 작성 시 포함 사항
- 점검 명령어 (bash/powershell/sql)
- 조치(수정) 명령어
- OS/환경별 분리 (linux/windows 등)

### Step 4: SKILL.md 라우터 업데이트

`skills-ko/kesekit-start-ko/SKILL.md`의 가이드라인 선택 테이블에 새 가이드라인을 추가합니다:

```markdown
| 3 | **새 가이드라인** | 설명 | 항목 수 |
```

그리고 새 분기 섹션을 추가합니다:

```markdown
## 새 가이드라인 분기 시

`references/new-guideline/`, `templates/new-guideline/`, `scripts/new-guideline/` 디렉터리에서 해당 파일을 읽어 평가합니다.
```

**4개 스킬 (kesekit-start, kesekit-check, kesekit-fix, kesekit-guide) 모두 동일하게 업데이트합니다.**

### Step 5: References / Templates / Scripts 복사

모든 스킬 디렉터리에 3개 디렉터리를 복사합니다:

```bash
# 한국어 스킬
cp -r skills-ko/kesekit-start-ko/references/new-guideline skills-ko/kesekit-check-ko/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills-ko/kesekit-check-ko/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills-ko/kesekit-check-ko/scripts/

cp -r skills-ko/kesekit-start-ko/references/new-guideline skills-ko/kesekit-fix-ko/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills-ko/kesekit-fix-ko/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills-ko/kesekit-fix-ko/scripts/

cp -r skills-ko/kesekit-start-ko/references/new-guideline skills-ko/kesekit-guide-ko/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills-ko/kesekit-guide-ko/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills-ko/kesekit-guide-ko/scripts/

# 영문 스킬
cp -r skills-ko/kesekit-start-ko/references/new-guideline skills/kesekit-start/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills/kesekit-start/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills/kesekit-start/scripts/

cp -r skills-ko/kesekit-start-ko/references/new-guideline skills/kesekit-check/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills/kesekit-check/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills/kesekit-check/scripts/

cp -r skills-ko/kesekit-start-ko/references/new-guideline skills/kesekit-fix/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills/kesekit-fix/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills/kesekit-fix/scripts/

cp -r skills-ko/kesekit-start-ko/references/new-guideline skills/kesekit-guide/references/
cp -r skills-ko/kesekit-start-ko/templates/new-guideline skills/kesekit-guide/templates/
cp -r skills-ko/kesekit-start-ko/scripts/new-guideline skills/kesekit-guide/scripts/
```

### Step 6: marketplace.json 업데이트

`.claude-plugin/marketplace.json`의 `keywords`와 `description`에 새 가이드라인 관련 키워드를 추가합니다.

### Step 7: README 업데이트

`README.md`와 `docs/` 아래 각 언어별 README에 새 가이드라인 정보를 추가합니다.

### Step 8: 검증 스크립트 실행

PR을 올리기 전에 아래 검증 스크립트를 실행하세요:

```bash
node scripts/validate-content.mjs
```

이 스크립트는 다음을 검사합니다:
- README / SKILL / reference 간 항목 수 정합성
- `start/check/fix/guide` 간 references/templates/scripts 파일 목록 및 내용 드리프트
- Robot Security 라우터 분기 누락 여부

GitHub Actions에서도 동일한 검증이 자동 실행됩니다.

---

## 콘텐츠 파일 작성 가이드

### 스킬 디렉터리 구조

```
skill-name/
├── SKILL.md
├── references/    ← 순수 설명/기준 문서
├── templates/     ← 별지 서식, 체크리스트 테이블
└── scripts/       ← 실행 가능한 점검/수정 스크립트
```

### references/ 파일 구조 예시

```markdown
# [시스템명] 보안 가이드라인

> 출처 정보

## 1. 카테고리명

위협 설명, 보안 요구사항, 판단 기준 등 순수 설명 콘텐츠
```

### templates/ 파일 구조 예시

```markdown
# [시스템명] 취약점 분석·평가 항목

## 1. 카테고리명 (N항목)

| 코드 | 항목 | 중요도 |
|------|------|:------:|
| XX-01 | 항목명 | 상 |

### 체크리스트
- □ 항목 1 확인
- □ 항목 2 확인
```

### scripts/ 파일 구조 예시

```bash
#!/bin/bash
# XX-01: 항목명 점검
result=$(command_here)
if [ "$result" == "expected" ]; then
    echo "[양호] XX-01"
else
    echo "[취약] XX-01"
fi
```

### 원칙

1. **Progressive Disclosure**: SKILL.md < 500줄, reference는 무제한
2. **자기 완결적**: reference 파일만 읽어도 평가 가능해야 함
3. **실용적**: 점검 명령어와 조치 방법을 반드시 포함
4. **한국어 기준**: 원본 가이드의 용어를 그대로 사용

### 파일 크기 가이드

| 항목 수 | 권장 줄 수 |
|:------:|:---------:|
| ~20개 | 100~200줄 |
| ~50개 | 200~400줄 |
| ~100개 | 400~600줄 |
| 100+개 | 분할 권장 |

---

## 버전 관리

- `marketplace.json`의 `version` 필드를 업데이트
- `README.md`의 변경 이력에 기록
- 커밋 메시지: `feat: Add [가이드라인명] security guideline`
