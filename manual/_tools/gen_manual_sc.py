# -*- coding: utf-8 -*-
"""구조·토목 계산서 통합 포털 사용자 매뉴얼 생성기 (MANMIN 매뉴얼 공통 엔진 v-mh1 · 안내형 도구 — 계산 예제 없음)
   실행: MANUAL_DIR=<manual 폴더> python gen_manual_sc.py  →  <manual>/index.html
   도구·근거 데이터는 ../../_tools/build_portal.py 의 TOOLS · GROUPS · LAWS 를 그대로 읽는다(단일 원천).
   근거(LawMCP 대조 2026-10-30): 건축법(2026-02-27) 제48조 · 시행령(2026-10-06) 제32조 · 건축물의 구조기준 등에 관한 규칙(2024-12-17)
   제56조 · 제58조 · 별표 11 · 12 · 시설물안전법 시행령(2026-09-15) 별표 1 제8호. KDS 명칭은 각 계산서 표기(국가건설기준센터 현행본 확인)."""
import os, sys, io, runpy, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from manual_engine import fig, T, render, B, MARKS

with contextlib.redirect_stdout(io.StringIO()):
    D = runpy.run_path(os.path.join(HERE, '..', '..', '_tools', 'build_portal.py'))
TOOLS, GROUPS, LAWS, APPVER, CHECKED = D['TOOLS'], D['GROUPS'], D['LAWS'], D['VER'], D['CHECKED']

VER, DATE = 'Ver-1.0', '2026-10-30'
PDF = '구조토목통합포털_사용자매뉴얼_Ver-1.0.pdf'
APP_URL = 'https://manminkim-eng.github.io/struct-civil-portal/'
APP = '구조·토목 계산서 통합 포털'
G = 'https://manminkim-eng.github.io/'
def F(sid, cap, legend=None, **kw):
    if legend is None:
        legend = [k['label'] for k in MARKS.get(sid, {}).get('marks', [])] or None
    return fig(sid, cap, legend, **kw)
K = lambda t: '<div class="k1">' + t + '</div>'
BR = lambda t: '<div class="brk">' + t + '</div>'
EXTRA_CSS = """<style>
#fig-s07_card{max-width:420px}
#fig-s13_install_bar{max-width:640px}
.k1 td:first-child,.k1 th:first-child{white-space:nowrap}
.lawt td,.lawt th{word-break:keep-all}.lawt td:nth-child(2){white-space:nowrap}.lawt td:first-child{min-width:9em}
.tri{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start}
@media (max-width:760px){.tri{grid-template-columns:1fr}}
@media print{
  figure.shot{max-width:none!important}
  figure.shot .frame{width:fit-content;max-width:100%}
  figure.shot img{width:auto;height:auto;max-width:100%;max-height:118mm}
  figure.narrow img{max-height:105mm}
  #fig-s13_install_bar .frame{width:120mm!important}#fig-s13_install_bar img{width:120mm!important;max-height:none}
  .tri{grid-template-columns:repeat(3,1fr)}
  .brk .tbl{break-inside:auto}.brk tr{break-inside:avoid}.brk thead{display:table-header-group}
}
</style>"""
GNAME = {g: n for g, n, _ in GROUPS}
NG = {g: sum(1 for t in TOOLS if t[1] == g) for g, _, _ in GROUPS}
tool_rows = [[GNAME[t[1]], ('S · ' if t[1]=='struct' else 'C · ')+t[0], f'<a href="{G}{t[4]}/" target="_blank" rel="noopener">{t[2]}</a>', 'Ver ' + t[5], ' · '.join(t[8]),
              f'<a href="{G}{t[4]}/manual/" target="_blank" rel="noopener">매뉴얼</a>'] for t in TOOLS]
law_rows = [[n, k, d, a, t] for n, k, d, a, t in LAWS]
TOC = [
 ('ch0', '0. 이 매뉴얼에 대하여', []),
 ('ch1', '1. 한눈에 보기', [('s1-1', '화면 구성'), ('s1-2', f'연결 계산서 {len(TOOLS)}종')]),
 ('ch2', '2. 1분 따라하기', []),
 ('ch3', '3. 화면별 기능', [('s3-1', '머리'), ('s3-2', '분류 탭'), ('s3-3', '계산서 카드'), ('s3-4', '구조'), ('s3-5', '토목'), ('s3-6', '근거 법령·설계기준'), ('s3-7', '휴대전화 화면'), ('s3-8', '앱 설치')]),
 ('ch4', '4. 근거 해설', [('s4-1', '근거 체계'), ('s4-2', 'KDS 확인과 구조 검토'), ('s4-3', '포털과 계산서의 역할')]),
 ('ch5', '5. 문제 해결·FAQ', []),
 ('ch6', '부록', [('a1', '버전 변경 내역'), ('a2', '용어')]),
]
S_ = []
S_.append(f"""{EXTRA_CSS}<section class="ch" id="ch0"><h2><span class="n">00</span>이 매뉴얼에 대하여</h2>
<p class="lead">{APP}은 내진설계 의무대상 판정 · 건축물 설계하중 · 단지 우수·오수 배관 · 옹벽 안전성 검토까지 <b>MANMIN 구조 · 토목 계산서 {len(TOOLS)}종의 진입 화면</b>입니다. 포털은 계산하지 않습니다. 카드를 눌러 계산서로 들어가고, 계산서마다 적용한 근거 법령과 설계기준(KDS)을 한 화면에서 확인합니다.</p>
{K(T([
 ['대상 프로그램', f'{APP} <b>Ver {APPVER}</b>'],
 ['접속 주소', f'<a href="{APP_URL}" target="_blank" rel="noopener">manminkim-eng.github.io/struct-civil-portal</a>'],
 ['매뉴얼 판', f'<b>{VER}</b> · {DATE} · 작성 김만민 건축사(㈜대성건축사사무소)'],
 ['내려받기', f'<a href="{PDF}" download>PDF(A4)</a> · <a href="../index.html">포털 열기</a>'],
 ['근거 대조', f'국가법령정보(LawMCP) {CHECKED} — 법령은 현행 시행일 · 조문 제목. KDS 명칭은 각 계산서 표기이며 원문 · 개정 이력은 국가건설기준센터에서 확인'],
 ['범위', '안내 · 연결 도구 — 수치 기준과 계산은 각 계산서에서 합니다'],
], ['항목', '내용']))}
<div class="note"><b>표기</b>그림 위 주황색 번호(①②…)는 그림 아래 범례 번호와 같습니다. 그림을 누르면 크게 볼 수 있습니다.</div>
<div class="warn"><b>책임 한계</b>포털은 근거 조문 · 시행일만 안내합니다. 하중 · 계수 · 관경 · 안전율 등 수치 기준과 판정은 각 계산서의 산출근거표와 법령 · KDS 원문으로 확인하고, 최종 구조 설계값은 구조기술사 · 토목 설계자의 검토를 받으십시오.</div>
</section>""")
S_.append(f"""<section class="ch" id="ch1"><h2><span class="n">01</span>한눈에 보기</h2>
<p class="lead">설치 없이 브라우저에서 바로 열리는 단일 페이지(PWA)입니다. 입력값이 없고, 연결과 근거 안내만 합니다.</p>
<h3 id="s1-1">1-1. 화면 구성</h3>
{F('s01_overview', '첫 화면')}
{K(T([
 ['머리', '근거 조문 대조일, 포털 이름, 설명'],
 ['요약 5칸', f'계산서 {len(TOOLS)}종(구조 {NG["struct"]} · 토목 {NG["civil"]}) · KDS 41 건축구조기준 · KDS 61 · 11 하수도 · 옹벽 · PWA · A4'],
 ['탭 막대', '전체 · 구조 · 토목 / 근거 법령·기준 / 사용자 매뉴얼 / 앱 설치(설치할 수 있는 브라우저에서만)'],
 ['계산서 카드', '카드를 누르면 계산서, 「사용자 매뉴얼」을 누르면 그 계산서의 매뉴얼(새 창)'],
 ['근거 법령 · 설계기준', f'법령 · KDS {len(LAWS)}행 — 현행 시행일 · 관련 조문 · 코드 · 적용 도구, 아래에 안내'],
], ['영역', '내용']))}
<h3 id="s1-2">1-2. 연결 계산서 {len(TOOLS)}종</h3>
{BR(K(T(tool_rows, ['분류', '번호', '계산서', '버전', '근거 기준', '매뉴얼'])))}
</section>""")
S_.append(f"""<section class="ch" id="ch2"><h2><span class="n">02</span>1분 따라하기</h2>
<p class="lead">예: 단지 안 옹벽과 우수 배관을 함께 검토하는 현장 — 포털에서 계산서를 찾아 들어가고 근거를 확인하는 순서입니다.</p>
<ol class="steps">
<li><b class="t">① 포털 열기</b>manminkim-eng.github.io/struct-civil-portal — 탭 막대의 「앱 설치」로 홈 화면에 설치할 수 있습니다(<a href="#s3-8">3-8</a>).</li>
<li><b class="t">② 분류</b>「토목」 탭을 누르면 단지 우수 · 오수 배관과 옹벽 안전성 검토 카드 2장만 남습니다(<a href="#s3-2">3-2</a>).</li>
<li><b class="t">③ 근거 확인</b>옹벽 카드의 칩 「KDS 11 80 05」 「시설물안전법 시행령 별표 1 제8호」를 확인합니다(<a href="#s3-5">3-5</a>).</li>
<li><b class="t">④ 매뉴얼</b>카드 아래 「사용자 매뉴얼」 — 그 계산서의 매뉴얼이 새 창으로 열립니다.</li>
<li><b class="t">⑤ 계산서</b>카드를 누르면 계산서로 이동해 옹벽의 전도 · 활동 · 지지력을 검토하고, 같은 방법으로 배관 계산서에서 관경과 유속을 정합니다.</li>
<li><b class="t">⑥ 시행일 확인</b>포털 아래 「근거 법령 · 설계기준」 표에서 현행 시행일과 KDS 코드를 확인합니다(<a href="#s3-6">3-6</a>).</li>
</ol>
{F('s09_civil_tab', '「토목」 탭')}
</section>""")
S_.append(f"""<section class="ch" id="ch3"><h2><span class="n">03</span>화면별 기능</h2>
<h3 id="s3-1">3-1. 머리</h3>
{F('s02_header', '머리')}
<p>맨 위 표시줄은 근거 조문을 국가법령정보와 대조한 날짜({CHECKED})입니다.</p>
<h3 id="s3-2">3-2. 분류 탭</h3>
{F('s03_tabs', '탭 막대')}
<p>「전체 {len(TOOLS)}」 · 「구조 {NG['struct']}」 · 「토목 {NG['civil']}」은 누르면 해당 묶음만 보여 줍니다. 「근거 법령·기준」은 아래 근거표로 이동하고, 「사용자 매뉴얼」은 이 문서를 새 창으로 엽니다(온라인 전용). 「앱 설치」는 설치할 수 있는 브라우저에서만 나타납니다(<a href="#s3-8">3-8</a>).</p>
<h3 id="s3-3">3-3. 계산서 카드</h3>
{F('s07_card', '계산서 카드 구성')}
<p>카드 위 번호 「S · 45」 · 「C · 50」은 홈페이지 도구 허브의 공종 표기(S 구조 · C 토목)와 개발 폴더 번호입니다. 버전은 계산서의 현재 판이고, 칩은 그 계산서가 산출근거로 인용하는 법령 · KDS입니다.</p>
<h3 id="s3-4">3-4. 구조</h3>
{F('s04_struct', f'구조 카드 {NG["struct"]}장')}
<p>내진설계 의무대상 판정은 <b>허가 신청일 시점의 법령 연혁</b>으로 판정하므로, 계산서에는 지금은 삭제된 옛 조문(예: 1992-06-01 시행 구조기준 규칙 제7조의2)이 근거로 나올 수 있습니다. 포털 근거표는 현행 조문만 적습니다.</p>
<h3 id="s3-5">3-5. 토목</h3>
{F('s05_civil', f'토목 카드 {NG["civil"]}장')}
<h3 id="s3-6">3-6. 근거 법령 · 설계기준</h3>
{F('s08_law', '근거 법령 · 설계기준 표')}
<p>표 아래 안내문은 포털의 원칙(근거 · 시행일만 안내, 수치 기준은 계산서)과 구조 검토 확인 사항입니다. KDS 원문과 개정 이력은 국가건설기준센터에서 확인합니다(<a href="#s4-2">4-2</a>).</p>
<h3 id="s3-7">3-7. 휴대전화 화면</h3>
<div class="tri"><div>{fig('s10_mobile_top', '첫 화면', narrow=True)}</div><div>{fig('s11_mobile_card', '카드', narrow=True)}</div><div>{fig('s12_mobile_law', '근거표', narrow=True)}</div></div>
<p>좁은 화면에서는 카드가 한 줄씩 쌓이고, 근거표는 좌우로 밀어서 봅니다.</p>
<h3 id="s3-8">3-8. 앱 설치</h3>
{F('s13_install_bar', '첫 방문 설치 안내 띠')}
{K(T([
 ['크롬 · 엣지 · 삼성인터넷 등', '탭 막대 「앱 설치」 또는 안내 띠의 「설치」 → 브라우저 설치 창에서 설치'],
 ['아이폰 · 아이패드', '「앱 설치」를 누르면 안내 상자 — 공유 단추 → 「홈 화면에 추가」 → 「추가」'],
 ['안내 띠', '첫 방문 2초 뒤 한 번 표시 — 「닫기」를 누르면 그 세션 동안 다시 띄우지 않음'],
 ['나타나지 않는 경우', '이미 설치한 앱 화면 · 설치를 지원하지 않는 브라우저(데스크톱 파이어폭스 등) · 설치를 막 거절한 직후'],
 ['설치 범위', '이 포털(/struct-civil-portal/)만 설치됩니다 — 카드에서 연 계산서는 앱 안의 브라우저 창으로 열리고, 계산서도 앱으로 쓰려면 각 계산서에서 설치합니다'],
], ['구분', '방법']))}
<div class="tri"><div>{fig('s14_ios_guide', '아이폰 설치 안내', narrow=True)}</div><div></div><div></div></div>
</section>""")
S_.append(f"""<section class="ch" id="ch4"><h2><span class="n">04</span>근거 해설</h2>
<h3 id="s4-1">4-1. 근거 체계</h3>
<div class="lawt">{BR(T(law_rows, ['법령 · 기준', '구분', '현행', '관련 조문 · 코드', '적용 도구']))}</div>
<h3 id="s4-2">4-2. KDS 확인과 구조 검토</h3>
{K(T([
 ['KDS 코드', 'KDS(국가건설기준 설계기준)는 국가법령정보가 아니라 국가건설기준센터(kcsc.re.kr)에서 고시 · 개정됩니다. 포털은 코드와 명칭만 적고 개정 연도 · 고시 번호는 각 계산서 표기를 따릅니다'],
 ['구조 안전 확인', '건축법 제48조제2항 · 시행령 제32조에 따라 건축 · 대수선 시 설계자가 구조 안전을 확인하고, 시행령 제32조제2항 대상은 착공신고 때 확인 서류를 냅니다(구조기준 규칙 제58조 서식)'],
 ['옹벽 시설물', '지면 노출 높이 5 m 이상 부분의 합이 100 m 이상인 옹벽은 시설물안전법 시행령 별표 1 제8호의 제2종시설물입니다 — 계산서는 해당 여부를 안내합니다'],
 ['최종 검토', '계산서 결과는 설계 검토 자료입니다. 최종 구조 설계값은 구조기술사 · 토목 설계자의 검토를 받으십시오'],
], ['구분', '내용']))}
<h3 id="s4-3">4-3. 포털과 계산서의 역할</h3>
{K(T([
 ['포털', '계산서 진입 · 분류 · 근거 법령과 시행일 · KDS 코드 안내 — 수치 기준을 싣지 않습니다'],
 ['계산서', '입력 · 계산 · 판정 · 산출근거표 · A4 계산서 — 수치 기준과 조항은 계산서가 정본입니다'],
 ['갱신', '법령이 바뀌면 계산서를 먼저 고치고, 포털 근거표는 시행일 · 번호만 고칩니다(데이터 단일 원천 _tools/build_portal.py)'],
], ['구분', '역할']))}
</section>""")
S_.append(f"""<section class="ch" id="ch5"><h2><span class="n">05</span>문제 해결·FAQ</h2>
{K(T([
 ['포털에서 계산이 되나요', '아닙니다 — 카드를 눌러 각 계산서에서 계산합니다'],
 ['「사용자 매뉴얼」이 안 열려요', '매뉴얼은 온라인 전용입니다(오프라인 캐시에서 제외)'],
 ['수치 기준은 어디 있나요', '각 계산서의 산출근거표와 A4 계산서에 있습니다 — KDS 원문은 국가건설기준센터에서 확인합니다'],
 ['「앱 설치」 단추가 안 보여요', '이미 설치했거나, 설치를 지원하지 않는 브라우저입니다 — 크롬 · 엣지에서 열어 보십시오(<a href="#s3-8">3-8</a>)'],
 ['설치한 앱에서 계산서가 브라우저 창으로 열려요', '정상입니다 — 설치 범위가 포털뿐이라서입니다. 계산서도 각자 설치할 수 있습니다'],
 ['계산서마다 디자인이 달라요', '계산서는 각각 별도 저장소의 도구라 헤드 색과 판이 다를 수 있습니다'],
 ['화면이 예전 판이에요', '새로 고침(Ctrl+F5) 또는 앱을 닫았다 다시 여십시오 — 판이 바뀌면 캐시 이름이 바뀝니다'],
], ['증상', '해결']))}
</section>""")
S_.append(f"""<section class="ch" id="ch6"><h2><span class="n">부록</span></h2>
<h3 id="a1">A1. 버전 변경 내역</h3>
{K(T([
 [f'Ver {APPVER} · 매뉴얼 {VER} ({DATE})', f'신설 — 계산서 {len(TOOLS)}종 · 분류 2(구조 · 토목) · 근거 법령 · 설계기준표 · 앱 설치 단추 · 사용자 매뉴얼'],
], ['버전', '내용']))}
<h3 id="a2">A2. 용어</h3>
{BR(K(T([
 ['구조 안전의 확인', '건축법 제48조제2항 · 시행령 제32조 — 설계자가 구조기준에 따라 구조 안전(지진 포함)을 확인하는 절차'],
 ['중요도 · 내진등급', '구조기준 규칙 별표 11(중요도 및 중요도계수) · 별표 12(건축물의 내진등급기준)'],
 ['KDS', '국가건설기준 설계기준(Korean Design Standard) — 국가건설기준센터 고시'],
 ['합리식', '강우강도 · 유출계수 · 배수면적으로 우수 유출량을 구하는 식'],
 ['PWA', '홈 화면에 설치해 오프라인에서도 여는 웹앱'],
], ['용어', '뜻'])))}
</section>""")
html = render(title=f'{APP} 사용자 매뉴얼 {VER} · MANMIN',
              desc=f'{APP} 사용자 매뉴얼 — 연결 계산서 {len(TOOLS)}종, 근거 법령 · 설계기준 안내',
              eyebrow='MANMIN ENGINEERING · USER MANUAL', h1=f'{APP} 사용자 매뉴얼',
              sub='카드 → 계산서 · 매뉴얼 → 분류 → 근거 법령 · 시행일', ver=VER, date=DATE, app_name='통합 포털',
              pdf=PDF, toc=TOC, sections=S_, foot_note='건축법 제48조 · 시행령 제32조 · 구조기준 규칙 · 시설물안전법 시행령 · KDS 41 · 61 · 11 — 대조 2026-10-30')
html = html.replace('화면 대응 개정 2026-10-12', '화면 대응 개정 ' + DATE)
open(os.path.join(B, 'index.html'), 'w', encoding='utf-8').write(html)
print('manual ok', len(html))
