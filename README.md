# 아주소중한딥러닝챌린지

> TODO: 한 줄 소개 — 예) 범용 LLM(Qwen2.5-3B-Instruct 등)을 수학 문제 풀이에 특화된 모델로
> 파인튜닝하는 대학생 딥러닝 챌린지 프로젝트입니다.

## 📌 프로젝트 개요

- **목표**: TODO
- **기간**: TODO
- **참여**: TODO (개인 / 팀명)
- **베이스 모델**: TODO (예: Qwen2.5-3B-Instruct)

## 🗂 데이터

| 파일 | 행 수 | 컬럼 | 설명 |
|---|---|---|---|
| `data/deep_chal_math_train.csv` | 25,840 | `id, question, answer` | 학습용. 정답 포함 |
| `data/deep_chal_math_leaderboard.csv` | 1,739 | `id, question` | 평가용. 정답 미포함(제출 후 채점) |

- **문제 유형**: 대수/방정식 응용문제, 비율·확률 계산 등 텍스트로 서술된 수학 문제
  (예: *"What is the molecular weight of..."*, *"Two of the roots of the cubic equation..."*)
- **출처**: TODO — 챌린지 주최 측 제공 데이터인지, 공개 데이터셋(GSM8K 등) 기반인지 명시
- **전처리**: TODO — 토크나이징/프롬프트 포맷(예: instruction 템플릿), 필터링 여부 등

## 🔧 접근 방법

- TODO: 파인튜닝 기법 (Full FT / LoRA / QLoRA 등), 학습 설정, 사용한 프레임워크

## 📊 결과

- TODO: 정량 결과 (스코어/정확도), 베이스라인 대비 개선 폭, 표/그래프

## 🚀 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/test.py
```

## 🧠 회고

- TODO: 시행착오, 배운 점, 아쉬운 점

## 📁 구조

```
.
├── data/       # 학습/리더보드 데이터
├── src/        # 학습·추론 코드
├── models/     # (git 미포함) 체크포인트 — 다운로드 링크는 아래 참고
├── outputs/    # 실험 결과물
└── docs/       # 실험 기록, 발표자료
```
