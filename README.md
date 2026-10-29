# 구조·토목 계산서 통합 포털 (struct-civil-portal) — Ver 1.0.0

- 신설: 2026-10-30 · Engineer KIM MANMIN · ㈜대성건축사사무소
- 성격: 소방(portal) · 기계설비(mech-portal) · 건축(arch-portal) 통합 포털과 같은 형식의 공종 통합 포털 — 구조 2종(45 내진설계 의무대상 · 46 설계하중) · 토목 2종(50 단지 우수·오수 배관 · 51 옹벽) 바로가기 + 근거 법령 · 설계기준 안내
- 원칙: 포털에는 근거 조문 · 시행일만 싣고 수치 기준은 각 계산서에 둔다(2026-10-29 MIN 승인).
- 데이터 단일 원천: `_tools/build_portal.py` 의 TOOLS · LAWS → `python _tools/build_portal.py` 로 index.html 재생성
- 근거 대조(2026-10-30, LawMCP): 건축법(2026-02-27) 제48조 · 같은 법 시행령(2026-10-06) 제32조 · 건축물의 구조기준 등에 관한 규칙(2024-12-17) 제56조 · 제58조 · 별표 11 · 12 · 시설물안전법 시행령(2026-09-15) 별표 1 제8호. KDS 명칭은 각 계산서 표기(국가건설기준센터 현행본 확인).
- 홈페이지 허브: 구조 묶음 S-ALL · 토목 묶음 C-ALL (같은 포털)
- 배포 경로: https://manminkim-eng.github.io/struct-civil-portal/
- 구성: index.html · manifest.json · sw.js(캐시 접두어 manmin-sc-portal-) · icons/ · assets/fonts/(로컬 폴백) · _tools/ · manual/
