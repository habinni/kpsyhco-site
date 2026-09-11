# -*- coding: utf-8 -*-
"""
한국심리건강진흥원 정적 사이트 빌더
- Wix 사이트(plymind3.wixsite.com/my-site)의 콘텐츠를 그대로 옮겨
  GitHub Pages 배포용 정적 HTML을 생성한다.
"""
import os

ROOT = "/home/claude/site"

# ------------------------------------------------------------------
# 내비게이션 정의
# ------------------------------------------------------------------
MAIN_NAV = [
    ("홈", "/", []),
    ("진흥원소개", "/about/", [
        ("설립목적", "/about/purpose/"),
        ("이사장프로필", "/about/ceo/"),
        ("정관", "/about/articles/"),
        ("연혁", "/about/history/"),
        ("조직 및 구성", "/about/organization/"),
        ("오시는 길", "/about/location/"),
    ]),
    ("주요사업안내", "/programs/", []),
    ("자격검정", "/certifications/", []),
    ("협력기관", "/partners/", []),
    ("공지사항", "/notice/", []),
]

CERTS = [
    dict(slug="psychology-counselor", title="심리상담사", code="2018-003749",
         definition="심리적 부적응을 경험하는 개인들을 개인 또는 집단으로 심리상담하며, 개인 또는 집단으로 심리평가하고, 집단 인간관계 자문 및 심리교육 등을 수행할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 심리상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리, 심리평가의 이해",
                 exam="필기-상담심리, 심리평가의 이해 / 실기-상담심리, 교육관",
                 train="심리상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 심리상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리학개론, 심리검사",
                 exam="필기-상담심리학개론, 심리검사 / 실기-상담자로서의 소양, 교육관",
                 train="심리상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)")),
    dict(slug="emotional-labor-counselor", title="감정노동상담사", code="2018-000750",
         definition="감정노동자들을 위한 상담을 진행할 수 있고, 감정노동자의 심리적 어려움을 상담을 통해 해결할 수 있는 상담사를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 감정노동 상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리 이론의 실제, 심리평가",
                 exam="필기-상담심리 이론의 실제, 심리평가 / 실기-상담의 실제, 교육관",
                 train="감정노동 상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 감정노동 상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리 이론, 성격심리",
                 exam="필기-상담심리 이론, 성격심리 / 실기-감정노동상담사로서의 소양, 교육관",
                 train="감정노동 상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)")),
    dict(slug="sports-psychology-coach", title="스포츠심리코칭전문가", code="2018-000301",
         definition="스포츠심리학과 운동학에 대한 이해를 바탕으로 전문가 수준의 스포츠심리코칭 상담, 운동 스타일 진단 및 개선 등을 수행할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 학사이상, 스포츠심리코칭 관련 교육과정 45시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)",
                 subj="스포츠심리, 운동학의 이해",
                 exam="필기-스포츠심리, 운동학의 이해 / 실기-학습코칭, 교육관",
                 train="스포츠심리코칭 관련 교육과정 45시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 스포츠심리코칭 관련 교육과정 30시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)",
                 subj="스포츠심리학개론, 코칭의 이해와 실제",
                 exam="필기-스포츠심리학개론, 코칭의 이해와 실제 / 실기-학습코칭, 교육관",
                 train="스포츠심리코칭 관련 교육과정 30시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)")),
    dict(slug="music-psychologist", title="음악심리사", code="2014-2064",
         definition="음악치료의 기초이론을 습득하고, 다양한 임상 대상자의 병리적 특성을 이해하여 기본적인 치료 계획 및 평가를 수립할 수 있는 전문가를 말한다.",
         basis="전문학사이상, 교육 20시간 2급 / 교육 40시간 1급",
         l1=dict(req="20대 이상, 전문학사이상, 음악치료관련 40시간의 일정한 교육과정을 수료",
                 subj="음악치료 개론, 이상심리학",
                 exam="필기-음악치료 개론, 이상심리학 / 실기-음악치료 계획서 작성 및 실시",
                 train="음악치료관련 40시간의 일정한 교육과정을 수료"),
         l2=dict(req="20대 이상, 전문학사이상, 음악치료관련 20시간의 일정한 교육과정을 수료",
                 subj="음악치료 개론",
                 exam="필기-음악치료 개론 / 실기-음악치료 계획서 작성",
                 train="음악치료관련 20시간의 일정한 교육과정을 수료")),
    dict(slug="art-psychology-counselor", title="미술심리상담사", code="2018-000628",
         definition="미술심리상담의 기초이론을 습득하고 기본적인 상담 계획 및 평가를 수립할 수 있으며, 다양한 임상 대상자의 병리적 특성을 이해하여 상담을 진행할 수 있는 상담사를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 미술심리상담 관련 교육과정을 40시간 이상 수료한 자",
                 subj="미술심리상담 실제, 이상심리학, 상담이론",
                 exam="필기-미술심리상담 실제, 이상심리학, 상담이론 / 실기-미술심리상담 계획서 작성 및 실시",
                 train="미술심리상담 관련 교육과정을 40시간 이상 수료한 자"),
         l2=dict(req="20대 이상, 학사이상, 미술심리상담 관련 교육과정을 20시간 이상 수료한 자",
                 subj="미술심리상담 개론",
                 exam="필기-미술심리상담 개론 / 실기-미술심리상담 계획서 작성",
                 train="미술심리상담 관련 교육과정을 20시간 이상 수료한 자")),
    dict(slug="couples-counselor", title="부부상담전문가", code="2018-000487",
         definition="남편과 아내 각각의 개인이 가진 특성을 이해하고, 부부가 가진 심리적 어려움을 해결하기 위한 부부상담을 진행할 수 있는 상담사를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 부부상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리, 부부상담의 이해",
                 exam="필기-상담심리, 부부상담의 이해 / 실기-상담의 실제, 교육관",
                 train="부부상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 부부상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리 이론, 게슈탈트 이론",
                 exam="필기-상담심리 이론, 게슈탈트 이론 / 실기-부부상담자로서의 소양, 교육관",
                 train="부부상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)")),
    dict(slug="parent-counselor", title="부모상담사", code="2018-000488",
         definition="부모 자녀간의 심리적 어려움뿐만 아니라 부모의 심리적인 어려움을 해결하기 위한 부모 상담을 진행할 수 있는 상담사를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 부모상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리, 부모상담의 이해",
                 exam="필기-상담심리, 부모상담의 이해 / 실기-상담의 실제, 교육관",
                 train="부모상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 부모상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)",
                 subj="상담심리 이론, 발달심리",
                 exam="필기-상담심리 이론, 발달심리 / 실기-부모상담자로서의 소양, 교육관",
                 train="부모상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단 4시간은 레포트로 대체가능)")),
    dict(slug="gifted-creativity-instructor", title="영재창의지도사", code="2014-0871",
         definition="창의력 이론, CPS(Creative Problem Solving) 및 CYT(Creative Ability and You Tail)의 단계 및 개발과정 이해하고, 아동 및 청소년 창의력 집단 프로그램 실시 및 기업에서의 창의력 활용, 수퍼비전 및 수련감독으로 역할을 할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 창의력 이론 45시간강의(단 4시간은 레포트로 대체가능)",
                 subj="창의력 이론과 개발, 사고력 교육, 수퍼비전",
                 exam="필기-창의력 이론과 개발, 사고력 교육, 수퍼비전 / 실기-창의력, 교사관",
                 train="창의력 이론 45시간 강의(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 창의력 이론 30시간강의(단 4시간은 레포트로 대체가능)",
                 subj="창의력 개론, CYT 이론과 실제, 문제이해와 글쓰기",
                 exam="필기-창의력 개론, CYT 이론과 실제, 문제이해와 글쓰기 / 실기-창의력, 교사관",
                 train="창의력 이론 30시간 강의(단 4시간은 레포트로 대체가능)")),
    dict(slug="senior-psychology-counselor", title="어르신 심리상담사", code="2018-004247",
         definition="심리적 부적응을 겪는 노인들을 개인 또는 집단으로 심리상담, 노인을 개인 또는 집단으로 심리평가, 노인집단의 인간관계 자문 및 심리교육, 노인의 심리적부적응 예방교육, 노인상담 및 노인심리에 관한 연구의 업무를 수행할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 대학 및 대학 평생교육원 심리상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단, 4시간은 레포트로 대체 가능)",
                 subj="노인상담심리, 심리평가의 이해",
                 exam="필기-노인상담심리, 심리평가의 이해 / 실기-노인상담심리, 교육관",
                 train="대학 및 대학 평생교육원 심리상담관련 45시간의 일정한 교육과정을 수료한 후에 응시가능(단, 4시간은 레포트로 대체 가능)"),
         l2=dict(req="20대 이상, 학사이상, 대학 및 대학 평생교육원 심리상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단, 4시간은 레포트로 대체 가능)",
                 subj="노인상담심리학개론, 심리검사",
                 exam="필기-노인상담심리학개론, 심리검사 / 실기-노인상담자로서의 소양, 교육관",
                 train="대학 및 대학 평생교육원 심리상담관련 30시간의 일정한 교육과정을 수료한 후에 응시가능(단, 4시간은 레포트로 대체 가능)")),
    dict(slug="disabled-children-art-counselor", title="장애아동미술심리상담사", code="2018-003754",
         definition="장애아동의 심리적 어려움을 개인 또는 집단으로 미술심리상담, 장애아동의 정서문제를 평가, 장애아동의 정서·인지·신체발달 자극, 장애아동의 부모 교육, 장애아동의 심리발달에 관한 연구, 장애아동의 특성과 발달을 위한 부모상담의 업무를 수행할 수 있는 전문가를 말한다.",
         basis="학사이상, 교육 40시간 후 2급 / 2급 취득 후 50시간 교육 후 1급",
         l1=dict(req="20대 이상, 2급 취득 후 장애아동 미술심리상담 관련 50시간의 일정한 교육과정을 수료한 후에 응시가능",
                 subj="미술치료이론, 장애진단",
                 exam="필기-미술치료, 장애아동의 특성(심리적, 인지적, 신체적), 부모상담 / 실기-장애별로 프로그램 구성",
                 train="2급 취득 후 장애아동 미술심리상담 관련 50시간의 일정한 교육과정을 수료한 후에 응시가능"),
         l2=dict(req="20대 이상, 학사이상, 장애아동 미술심리상담 관련 40시간의 일정한 교육과정을 수료한 후에 응시가능",
                 subj="미술치료이론, 장애진단",
                 exam="필기-미술치료이론, 장애진단 / 실기-장애아동의 진단",
                 train="장애아동 미술심리상담 관련 40시간의 일정한 교육과정을 수료한 후에 응시가능")),
    dict(slug="learning-coach", title="학습코칭전문가", code="2014-0870",
         definition="아동·청소년 및 부모 학습상담, 학습 스타일 진단 및 개선의 자질과 의무를 수행할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 석사이상, 45시간 강의(단 4시간은 레포트로 대체가능)",
                 subj="학습심리, 심리상담, 고급 독서이해와 글쓰기",
                 exam="필기-학습심리, 심리상담, 고급 독서이해와 글쓰기 / 실기-학습심리, 교사관",
                 train="45시간 강의(단 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 30시간 강의(단 4시간은 레포트로 대체가능)",
                 subj="심리학개론, 학습 코칭의 이해와 실제, 독서이해와 글쓰기",
                 exam="필기-심리학개론, 학습 코칭의 이해와 실제, 독서이해와 글쓰기 / 실기-학습코칭, 교사관",
                 train="30시간 강의(단 4시간은 레포트로 대체가능)")),
    dict(slug="career-aptitude-counselor", title="진로적성상담사", code="2017-005853",
         definition="진로탐색 이론, 진로검사 및 적성검사의 단계 및 개발과정 이해를 바탕으로 진로직업 지도에서의 관련 검사 활용, 아동 및 청소년 진로집단프로그램 진행, 수퍼비전 및 수련감독으로서의 업무를 수행할 수 있는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="20대 이상, 학사이상, 진로관련 강의 45시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)",
                 subj="진로 이론과 개발, 적성검사 교육, 수퍼비전",
                 exam="필기-진로 이론과 개발, 적성검사 교육, 수퍼비전 / 실기-진로적성에 대한 코칭능력, 교사관",
                 train="진로관련 강의 45시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)"),
         l2=dict(req="20대 이상, 학사이상, 진로관련 강의 30시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)",
                 subj="진로이론, 적성 이론과 실제, 검사활용",
                 exam="필기-진로이론, 적성 이론과 실제, 검사활용 / 실기-진로적성에 대한 코칭능력, 교사관",
                 train="진로관련 강의 30시간 이상 수료한 자(단, 4시간은 레포트로 대체가능)")),
    dict(slug="marine-guide", title="해양지도사", code="2020-003869",
         definition="갯벌·염지하수·해양생물과 같은 해양자원 특성(경관, 소리, 향기, 촉감 등의 자극)을 활용해 건강의 유지를 돕고, 면역을 증진하는 활동을 개인 또는 집단으로 지원 및 교육하는 업무를 수행할 수 있는 자를 말한다.",
         basis="연령 20세 이상 · 학력 고등학교 졸업에 준하는 자 이상 (단일 등급)",
         l1=dict(req="연령 20세 이상 · 학력 고등학교 졸업에 준하는 자 이상 · 해양지도관련 30시간의 일정한 교육과정을 수료한 자 (수산계고교 출신자는 고등교육과정을 교육시간으로 인정)",
                 subj="해양자원을 이용한 건강학개론, 해양자원의 이해",
                 exam="필기-해양자원을 이용한 건강학개론, 해양자원의 이해 / 실기-해양지도사로서의 소양, 해양지도사로서의 교육관",
                 train="해양지도관련 30시간의 일정한 교육과정을 수료한 자"),
         l2=None),
    dict(slug="marine-care-instructor", title="해양케어지도사", code="2020-003868",
         definition="생리적·심리적 부적응을 경험하는 개인 또는 집단을 대상으로 갯벌·염지하수·해양생물과 같은 해양자원 특성(경관, 소리, 향기, 촉감 등의 자극)을 매체로 활용해 생리적·심리적 건강을 증진하는 활동을 개인 또는 집단으로 실시하며, 평가·자문·교육의 업무를 수행하는 전문가를 말한다.",
         basis="학사이상은 2급 / 석사이상은 1급",
         l1=dict(req="연령 20세 이상 · 석사 학위가 있는 자 · 매체케어관련과 해양케어관련 교육과정을 각각 40시간 이상 이수한 자 (수산계·해양관련학과 졸업 교육과정 인정 / 2급 취득 후 실무 3년 이상 종사자)",
                 subj="매체를 활용한 건강케어의 실제, 통합검사의 이해",
                 exam="필기-매체를 활용한 건강케어의 실제, 통합검사의 이해 / 실기-매체를 활용한 건강케어 실습평가, 해양케어지도사 교육관",
                 train="매체케어관련과 해양케어관련 교육과정을 각각 40시간 이상 이수한 자"),
         l2=dict(req="연령 20세 이상 · 학사 학위가 있는 자 · 매체케어관련과 해양케어관련 교육과정을 각각 20시간 이상 이수한 자 (수산계·해양관련학과 졸업 교육과정 인정 / 해양지도사 자격 취득 후 실무 4년 이상 종사자)",
                 subj="해양자원을 활용한 건강학개론, 통합검사",
                 exam="필기-해양자원을 활용한 건강학개론, 통합검사 / 실기-해양케어지도사로서의 소양, 해양케어지도사 교육관",
                 train="매체케어관련과 해양케어관련 교육과정을 각각 20시간 이상 이수한 자")),
]

FOOTER_ORG = (
    "한국심리건강진흥원 대표: 정혜인 · 대구광역시 달서구 용산로141(용산동, 그랜드 M타워) 13층 · "
    "문의 02-2295-5575 · 사업자등록번호 503-82-13276"
)

# ------------------------------------------------------------------
# 템플릿
# ------------------------------------------------------------------

def rel(path_from, path_to):
    """path_from, path_to 는 '/about/purpose/' 형태(사이트 루트 기준). 상대경로 계산 없이 절대경로 사용."""
    return path_to

def render_nav(active_path):
    items = []
    for label, href, children in MAIN_NAV:
        is_active = active_path == href or (href != "/" and active_path.startswith(href))
        li_class = ' class="active"' if is_active else ""
        if children:
            sub = "".join(f'<li><a href="{c_href}">{c_label}</a></li>' for c_label, c_href in children)
            items.append(
                f'<li{li_class}><a href="{href}">{label}</a><ul class="submenu">{sub}</ul></li>'
            )
        else:
            items.append(f'<li{li_class}><a href="{href}">{label}</a></li>')
    return "".join(items)


def base_page(title, active_path, body_html, description="", subnav_html="", main_class=""):
    nav_html = render_nav(active_path)
    full_title = f"{title} | 한국심리건강진흥원" if title != "한국심리건강진흥원" else title
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="preconnect" href="https://hangeul.pstatic.net">
<link href="https://hangeul.pstatic.net/hangeul_static/css/nanum-barun-pen.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<a class="skip-link" href="#main">본문 바로가기</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/img/logo.png" alt="한국심리건강진흥원 로고"><span>(사) 한국심리건강진흥원</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-label="메뉴 열기">메뉴 ☰</button>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <ul>{nav_html}</ul>
  </nav>
</header>
{subnav_html}
<main id="main" class="{main_class}">
{body_html}
</main>
<footer class="site-footer">
  <div class="wrap">
    <ul class="footer-links">
      <li><a href="/privacy/">개인정보처리방침</a></li>
      <li><a href="/terms/">이용약관</a></li>
    </ul>
    <p class="footer-meta"><strong>한국심리건강진흥원 &nbsp; 대표: 정혜인 &nbsp; 대구광역시 달서구 용산로141(용산동, 그랜드 M타워) 13층 &nbsp; 문의: 02-2295-5575 &nbsp; 사업자등록번호: 503-82-13276</strong><br>
    Copyright 한국심리건강진흥원. All rights reserved.</p>
    <p class="footer-credit">Icon designed by Freepik, JunGSa, Icongeek26</p>
  </div>
</footer>
<script src="/assets/js/nav.js"></script>
</body>
</html>
"""


def subnav(crumbs, siblings, active_href):
    """crumbs: [(label, href|None)], siblings: [(label, href)]"""
    crumb_html = " / ".join(
        f'<a href="{href}">{label}</a>' if href else label for label, href in crumbs
    )
    sibs = "".join(
        f'<li{" class=\"active\"" if href == active_href else ""}><a href="{href}">{label}</a></li>'
        for label, href in siblings
    )
    return f"""<div class="subnav"><div class="wrap">
  <p class="crumb">{crumb_html}</p>
  <ul class="sib-list">{sibs}</ul>
</div></div>"""


def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


ABOUT_SIBLINGS = [
    ("소개", "/about/"),
    ("설립목적", "/about/purpose/"),
    ("이사장프로필", "/about/ceo/"),
    ("정관", "/about/articles/"),
    ("연혁", "/about/history/"),
    ("조직 및 구성", "/about/organization/"),
    ("오시는 길", "/about/location/"),
]

print("templates ready")

# ------------------------------------------------------------------
# 홈
# ------------------------------------------------------------------
home_body = """
<section class="hero"><div class="wrap">
<img class="hero-pc" src="/assets/img/hero.svg" alt="한국심리건강진흥원 메인 배너"><img class="hero-mo" src="/assets/img/hero-mobile.svg" alt="한국심리건강진흥원 메인 배너">
</div></section>
<section class="feature-band"><div class="wrap">
  <div class="feature"><div class="icon"><img src="/assets/img/band-info.svg" alt=""></div><h3>소개</h3><a class="more" href="/about/">| 자세히 |</a></div>
  <div class="feature"><div class="icon"><img src="/assets/img/band-check.svg" alt=""></div><h3>주요사업</h3><a class="more" href="/programs/">| 자세히 |</a></div>
  <div class="feature"><div class="icon"><img src="/assets/img/band-star.svg" alt=""></div><h3>자격검정</h3><a class="more" href="/certifications/">| 자세히 |</a></div>
  <div class="feature"><div class="icon"><img src="/assets/img/band-plus.svg" alt=""></div><h3>협력기관</h3><a class="more" href="/partners/">| 자세히 |</a></div>
</div></section>
"""
write("/index.html", base_page("한국심리건강진흥원", "/", home_body, main_class="home",
      description="사단법인 한국심리건강진흥원 공식 홈페이지"))

# ------------------------------------------------------------------
# 진흥원소개
# ------------------------------------------------------------------
about_body = """
<div class="page-hero"><div class="wrap"><h1>진흥원소개</h1></div></div>
<div class="wrap"><div class="two-col"><div class="prose">
<p>여러분, 반갑습니다. 한국심리건강진흥원입니다.</p>
<p>육체적인 건강 못지않게 정신적 안녕은 개인과 사회를 지탱하는 기본이 되지만
우리의 현실은 심리건강을 저해하는 요소들이 너무나 많아 개인과 사회를 위협하고 있습니다.
이러한 우려는 최근의 사회병리적 현상들과 함께 분명하게 드러나고 있습니다.</p>
<p>한국심리건강진흥원은 한국사회에 심리건강과 관련한 문제들을 온오프라인(플리마인드·새미래심리건강연구소)을
통해 통합적으로 접근하여 지역사회와 국가 안녕에 기여하고자 합니다.</p>
<p>더욱이 환경에 취약한 장애인이나 저소득층 같은 사회적 소외계층을 위하여 연구 및 프로그램 개발과
서비스에 힘쓰고자 합니다. 이 작은 노력이 우리사회를 보다 건강한 것으로 만드는 일에 씨앗이 되어
좋은 열매를 맺길 바랍니다.</p>
<p>뜻 있는 분들과 함께 이루어 가기를 기대하며 관심과 조언을 부탁드립니다.</p>
</div>
<div class="name-card">
  <img src="/assets/img/logo.png" alt="">
  <p class="name-card-title">초대 이사장 손명자<br>이사장 정혜인</p>
  <a href="/about/ceo/">프로필 보기 →</a>
</div>
</div></div>
"""
write("/about/index.html", base_page("진흥원소개", "/about/", about_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", None)], ABOUT_SIBLINGS, "/about/")))

# ------------------------------------------------------------------
# 설립목적
# ------------------------------------------------------------------
# (x, y, 색상클래스, 아이콘, 텍스트)  — 660x440 캔버스 기준 원 중심 좌표
PURPOSE_BUBBLES = [
    (110,  70, "g1", "p-hand-w.svg",      "심리건강을<br>증진하기 위한<br>연구"),
    (270, 120, "y",  "p-light-w.svg",     "사회 각 분야의<br>현안에 대한<br>심리건강프로그램<br>개발 및 보급"),
    (440,  40, "o",  "p-notes-w.svg",     "전문인력의<br>양성"),
    ( 90, 220, "g2", "p-butterfly-w.svg", "국가의 정신건강<br>복지정책 사업활동에<br>적극 참여"),
    (270, 270, "b",  "p-clover-w.svg",    "심리건강 증진을 위한<br>예방·상담·재활<br>프로그램 보급"),
    (440, 200, "g1", "p-leaf-w.svg",      "정신장애인들을 위한<br>장애재활프로그램의<br>개발과 보급"),
    ( 80, 360, "g2", "p-world-w.svg",     "다양한 연구기관 및<br>해외 연구자와의<br>교류협력, 공동연구"),
    (270, 400, "g1", "p-arrow-w.svg",     "회원간 정보공유<br>및 인적 교류확대<br>의 추진"),
    (450, 340, "b",  "p-drop.svg",        "법인의 목적 달성을<br>위해 필요한<br>모든사항"),
]
LINKS = [(0,1),(1,2),(1,3),(3,4),(2,5),(4,5),(3,6),(6,7),(7,8),(5,8),(4,7)]
line_svg = "".join(
    f'<line x1="{PURPOSE_BUBBLES[a][0]}" y1="{PURPOSE_BUBBLES[a][1]}" x2="{PURPOSE_BUBBLES[b_][0]}" y2="{PURPOSE_BUBBLES[b_][1]}"/>'
    for a, b_ in LINKS)
bubbles_html = "".join(
    f'<div class="bubble {cls}" style="left:{x}px;top:{y}px;"><img src="/assets/img/{icon}" alt=""><p>{text}</p></div>'
    for x, y, cls, icon, text in PURPOSE_BUBBLES)
purpose_body = f"""
<div class="wrap">
<div class="purpose-banner">
  <h1>한국심리건강진흥원은</h1>
  <p>심리적 건강을 관리하는 노력이 절실히 요구되고 있는 현 사회적 상황을<br>
  인식하고 심리건강증진을 위한 제 활동을 하는 것을 목적으로 한다.</p>
</div>
<div class="purpose-scene">
  <div class="balloon"><img src="/assets/img/balloon.svg" alt=""></div>
  <div class="bubble-map">
    <svg class="links" viewBox="0 0 660 440" preserveAspectRatio="none">{line_svg}</svg>
    {bubbles_html}
  </div>
</div>
<ul class="purpose-fallback">
{''.join('<li>' + t.replace('<br>', ' ') + '</li>' for *_, t in PURPOSE_BUBBLES)}
</ul>
</div>
"""
write("/about/purpose/index.html", base_page("설립목적", "/about/purpose/", purpose_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("설립목적", None)], ABOUT_SIBLINGS, "/about/purpose/")))

# ------------------------------------------------------------------
# 이사장프로필
# ------------------------------------------------------------------
def profile_tabs(active):
    a1 = ' class="active"' if active == "ceo" else ""
    a2 = ' class="active"' if active == "founder" else ""
    return f'''<div class="profile-tabs">
  <a href="/about/ceo/"{a1}>이사장 프로필</a>
  <a href="/about/ceo/founder/"{a2}>초대 이사장 프로필</a>
</div>'''

def profile_section(title, items):
    return f'''<section class="profile-sec">
  <h3>{title}</h3>
  <ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>
</section>'''

CEO_SECTIONS = [
    ("약력", [
        "2005.02 : 현재 창의력 한국 FPSP 현곡 R&amp;D 연구위원",
        "2007.09 : 현재 새미래심리건강연구소 부소장",
        "2008.09 ~ 2013.02 : 나사렛대학교 상담교수",
        "2009.09 : 현재 휴신경정신과 슈퍼바이저",
        "2010.09 ~ 2013.10 : (주)이오공감 부설 심리연구소 심리척도 및 심리프로그램 R&amp;D 소장",
        "2012.09 ~ 2015.10 : (사단법인)한국심리건강진흥원 이사",
        "2013.03 ~ 2016.02 : 선문대학교 통합의학대학원 임상심리상담학과 주임교수",
        "2013.03 ~ 2016.02 : 선문대학교 평생교육원 학점은행제 전공교수",
        "2014.09 : 현재 태안군 정책자문위원",
        "2014.10 ~ 2016.02 : 선문대학교 휴먼 AND 크리에이티브 R&amp;D 소장",
        "2015.10 : 현재 플리마인드 대표",
        "2015.11 : 현재 (사단법인)한국심리건강진흥원 이사장",
    ]),
    ("자격", [
        "상담심리전문가 (상담심리학회)",
        "가족상담전문가 (가족상담학회)",
        "창의력전문가 (창의력 한국 FPSP 현곡R&amp;D)",
        "모래놀이치료전문가 (한국모래놀이치료학회)",
        "기업상담전문가 (상담심리학회)",
        "중독상담슈퍼바이저 (한국도박문제관리센터)",
    ]),
    ("특허", [
        "저작권 : C-2008-011337",
        "출원사실증명원 : 특허-2008-0040927",
    ]),
    ("검사출판물", [
        "학습·정서·행동 적응성검사(초등 저학년용/고학년용) : (주)이오공감",
        "성격유능성검사-청소년 : (주)이오공감",
        "창의력진단검사 : (주)이오공감",
        "SEAT(STUDY EMOTION ACTIVITY TEST) : FOR PRIMARY SCHOOL CHILDREN (HIGH GRADE LEVEL) : (주)이오공감",
        "SEAT(STUDY EMOTION ACTIVITY TEST) : FOR PRIMARY SCHOOL CHILDREN (LOW GRADE LEVEL) : (주)이오공감",
        "PERSONALITY COMPETENCE TEST : ADOLESCENT (PCT-A) : (주)이오공감",
        "DIAGNOSTIC TEST OF CREATIVITY, LANGUAGE CREATIVITY : (주)이오공감",
    ]),
    ("수상", [
        "사회서비스 기획인력양성 1등 창의상 (한국보건복지인력개발원장상)",
    ]),
]
FOUNDER_SECTIONS = [
    ("약력", [
        "1982 : 계명대학교 사회과학대학 심리학과 전임교수",
        "1988 : 한양대학교 의과대학 신경정신과 교환교수",
        "1989 ~ 1990 : 대구광역시 여성의 전화(구 애린회) 공동 대표",
        "1995 ~ 2002 : (현)사단법인 대구 경북정신보건가족협회 자문교수",
        "1996 : 미국 BOSTON 대학교 재활상담학과 연구교수",
        "2002 ~ 2005 : 대구광역시 정신장애인 가족협회 부설 대구재활센터 원장",
        "2005 : (현)계명대학교 사회과학대학 심리학과 교수 은퇴 · 명예교수",
        "2005 : (현)새미래 심리건강연구소 소장",
    ]),
    ("자격", [
        "2005 : 한국 심리학회 1급 임상심리전문가 자격",
        "1995 : 현실치료법 전문가 자격",
        "1997 : 정신보건전문요원(임상심리사) 1급 자격",
        "2009 : 중독 심리전문가 1급",
    ]),
]

def profile_page(title, sections, active):
    secs = '<hr class="dashed">'.join(profile_section(t, items) for t, items in sections)
    return f"""
<div class="profile-wrap"><div class="wrap">
{profile_tabs(active)}
<div class="profile-body">
  <h1>{title}</h1>
  {secs}
</div>
</div></div>
"""

write("/about/ceo/index.html", base_page("이사장프로필", "/about/ceo/",
      profile_page("이사장 프로필", CEO_SECTIONS, "ceo"), main_class="flush",
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("이사장프로필", None)], ABOUT_SIBLINGS, "/about/ceo/")))
write("/about/ceo/founder/index.html", base_page("초대 이사장 프로필", "/about/ceo/",
      profile_page("초대 이사장 프로필", FOUNDER_SECTIONS, "founder"), main_class="flush",
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("이사장프로필", "/about/ceo/"), ("초대 이사장 프로필", None)], ABOUT_SIBLINGS, "/about/ceo/")))

print("home / about / purpose / ceo done")

# ------------------------------------------------------------------
# 정관
# ------------------------------------------------------------------
articles_body = """
<div class="page-hero"><div class="wrap"><h1>정관</h1></div></div>
<div class="wrap prose">

<h2>제1장 총칙</h2>
<p><strong>제1조 (명칭)</strong> 이 법인은 "사단법인 한국심리건강진흥원"(이하 "법인"이라 한다)이라 한다.</p>
<p><strong>제2조 (목적)</strong> 이 법인의 목적은 다음 각 호와 같다.</p>
<ul>
<li>현대인(특히 소외계층)의 심리건강을 증진하기 위한 연구</li>
<li>대구광역시의 발전을 위해 사회 각 분야의 현안에 대한 심도 있는 분석과 연구를 통한 심리건강 프로그램 개발 및 보급</li>
<li>다양한 연구기관 및 해외 연구자와의 교류협력, 공동연구</li>
<li>회원 간 정보 공유 및 인적 교류확대의 추진</li>
<li>법인의 목적 달성을 위하여 필요한 모든 사항</li>
</ul>
<p><strong>제3조 (사무소의 소재지)</strong> 이 법인의 주된 사무소는 대구광역시 달서구 용산로 141에 둠을 원칙으로 한다.
필요한 경우 전국의 주요지역에 연락사무소(사무소)를 둘 수 있다.</p>
<p><strong>제4조 (사업)</strong> 법인은 제2조의 목적을 달성하기 위하여 다음 각 호의 사업을 수행한다.</p>
<ul>
<li>사회적 소외계층과 현대인의 심리건강에 관한 연구, 프로그램 개발 및 보급사업</li>
<li>심리건강 증진을 위한 예방, 상담, 재활 프로그램 개발 및 보급사업</li>
<li>심리건강 관련 전문가 인력 양성 사업</li>
<li>심리건강에 관련한 지역적, 국제적 상호교류 협력사업</li>
<li>국책사업(도박중독, 인터넷 중독, 바우처 연계, 교육복지투자 지원 사업 등) 수행</li>
<li>소외계층(장애인, 저소득층 등) 및 교육복지투자 지원사업</li>
<li>심리건강 관련 유전자 연구 및 검사 분석 사업</li>
<li>구직자 및 퇴직자 심리건강에 관련한 연구 및 지원 사업</li>
<li>기타 법인의 목적 달성에 필요한 사업</li>
</ul>

<h2>제2장 회원</h2>
<p><strong>제5조 (회원의 종류 및 자격)</strong> ① 법인의 회원은 제2조의 목적과 설립취지에 찬성하여 정해진 가입절차를
마친 자(공공기관, 단체)로 한다. ② 법인의 회원이 되고자 하는 자는 정해진 회원가입 신고서를 법인에 제출하여야 한다.
③ 회원의 자격, 가입회비 등에 관한 세부사항은 총회에서 별도의 규정으로 정한다.</p>
<p><strong>제6조 (회원의 권리)</strong> 총회 참여 및 발언권, 의결권 행사, 법인이 수행하는 연구·토론·개발 참여, 기타
정관 및 부속 규정에 의한 권리.</p>
<p><strong>제7조 (회원의 의무)</strong> 정관 및 규정 준수, 사업 및 연구 참여, 총회·이사회 결의사항 이행, 회비 및
부담금 납부.</p>
<p><strong>제8조 (회원의 탈퇴 및 제명)</strong> 회원은 자유롭게 탈퇴할 수 있으며, 의무를 다하지 않거나 명예를
실추시킨 회원은 이사회 의결을 거쳐 제명하거나 권리를 정지할 수 있다. 탈퇴·제명 시 납부한 회비 등에 대한 권리는
요구할 수 없다.</p>

<h2>제3장 임원</h2>
<p><strong>제9조 (임원의 종류 및 정수)</strong> 이사장 1인, 이사(이사장 포함) 5인 이상 10인 이내, 감사 2인.</p>
<p><strong>제10조 (임원의 선임)</strong> 임원은 총회에서 선출하며, 이사장은 이사 중에서 호선한다. 임기만료
2월 이내 후임자를 선출한다.</p>
<p><strong>제11조 (임원의 해임)</strong> 목적 위배, 분쟁·회계부정, 업무 방해 행위 시 총회 의결로 해임할 수 있다.</p>
<p><strong>제12조 (임원의 결격사유)</strong> 미성년자, 파산선고 후 미복권자, 자격 상실·정지자, 금고 이상의 형을
선고받은 자 등은 임원이 될 수 없다.</p>
<p><strong>제13조 (임원의 임기 및 보선)</strong> 이사 임기 3년, 감사 임기 2년, 연임 가능. 결원 시 보궐선거 원칙,
후임자 임기는 전임자 잔여기간.</p>
<p><strong>제14조 (임원의 직무)</strong> 이사장은 법인을 대표하고 총회를 소집하며 운영을 총괄한다. 이사는 이사회에서
사업 운영을 심의·의결한다. 감사는 재산·업무 감사 및 총회 보고 의무를 진다.</p>
<p><strong>제15조 (임원의 보수)</strong> 임원에게는 보수를 지급하지 아니하며, 예산 범위 내 실비만 지급할 수 있다.</p>
<p><strong>제16조 (고문)</strong> 사회 각계 원로 등으로부터 자문을 얻기 위해 고문을 위촉할 수 있다.</p>

<h2>제4장 총회</h2>
<p><strong>제17조 (총회의 구성과 지위)</strong> 총회는 전체 회원으로 구성된 최고 의결 기구다.</p>
<p><strong>제18조 (총회의 구분과 소집)</strong> 정기총회는 매 회계연도 개시 1월 전까지, 임시총회는 필요 시 소집한다.</p>
<p><strong>제19조 (총회소집의 특례)</strong> 재적이사 과반수 또는 재적회원 3분의 1 이상의 요구가 있을 때 20일
이내에 총회를 소집하여야 한다.</p>
<p><strong>제20조 (총회의 의결사항)</strong> 임원의 선출·해임, 해산·정관변경, 기본재산 처분, 예산·결산 승인,
사업계획 승인 등.</p>
<p><strong>제21조 (의결정족수)</strong> 재적회원 5분의 1 이상 출석으로 개회하며, 출석회원 과반수 찬성으로 의결한다.</p>
<p><strong>제22조 (의결제척사유)</strong> 자신의 임원 선출·해임이나 이해가 상반되는 사안에는 의결에 참여할 수 없다.</p>

<h2>제5장 이사회</h2>
<p><strong>제23조 (이사회의 구성)</strong> 이사장과 이사로 구성하며 법인 운영에 관한 사업을 총괄·추진한다.</p>
<p><strong>제24조 (이사회의 소집)</strong> 정기이사회는 연 2회, 임시이사회는 필요 시 소집한다.</p>
<p><strong>제25조 (이사회의 의결사항)</strong> 업무집행, 사업계획 운영, 예산·결산서 작성, 정관변경, 재산관리 등.</p>
<p><strong>제26조 (의결정족수)</strong> 재적이사 과반수 출석, 출석위원 과반수 찬성으로 의결한다.</p>
<p><strong>제27조 (서면결의 금지)</strong> 이사회의 의결은 서면결의에 의할 수 없다.</p>
<p><strong>제28조 (이사회 회의록)</strong> 의사의 경과·요령·결과를 기재하고 의장과 참석 이사가 기명날인한다.</p>

<h2>제6장 재산과 회계</h2>
<p><strong>제29조 (재산의 구분)</strong> 기본재산과 보통재산으로 구분한다.</p>
<p><strong>제30조 (재산의 관리)</strong> 기본재산의 매도·증여·임대·교환·담보제공 등은 총회 의결을 거쳐야 한다.</p>
<p><strong>제31조 (재원)</strong> 회비, 정부 및 지방자치단체 보조금, 기부금, 기본재산 과실금 등.</p>
<p><strong>제32조 (회계연도)</strong> 법인의 회계연도는 정부의 회계연도에 따른다.</p>
<p><strong>제33조 (예산편성 및 결산)</strong> 회계연도 1월전 사업계획 및 예산안을 이사회 의결·총회 승인을 거친다.</p>
<p><strong>제34조 (회계감사)</strong> 감사는 회계감사를 연 2회 이상 실시한다.</p>
<p><strong>제35조 (업무보고)</strong> 사업계획서·예산서와 사업실적서·수지결산서를 회계연도 종료 후 2월 이내 주무관청에
보고한다.</p>
<p><strong>제36조 (임원의 보수)</strong> 임원에게 보수를 지급하지 아니하되, 업무수행에 필요한 실비는 지급할 수 있다.</p>

<h2>제7장 사무부서</h2>
<p><strong>제37조 (사무국)</strong> 이사장의 지시를 받아 법인의 사무를 처리하기 위하여 사무국을 두며, 사무국장
1인과 필요한 직원을 둘 수 있다.</p>

<h2>제8장 보칙</h2>
<p><strong>제38조 (정관변경)</strong> 총회에서 재적회원 3분의 2 이상 찬성으로 의결하여 주무관청의 허가를 받아야 한다.</p>
<p><strong>제39조 (해산)</strong> 총회에서 재적회원 4분의 3 이상 찬성으로 의결하여 주무관청에 신고하여야 한다.</p>
<p><strong>제40조 (잔여재산의 처리)</strong> 해산 시 잔여재산은 총회 의결과 주무관청 허가를 얻어 국가, 지방자치단체
또는 유사 목적의 비영리법인에 귀속한다.</p>
<p><strong>제41조 (청산종결의 신고)</strong> 청산인은 청산 종결 시 등기 후 청산종결 신고서를 주무관청에 제출한다.</p>
<p><strong>제42조 (준용규정)</strong> 정관에 규정되지 아니한 사항은 민법 중 사단법인에 관한 규정과 보건복지부 소관
비영리법인의 설립 및 감독에 관한 규칙을 준용한다.</p>
<p><strong>제43조 (규칙제정)</strong> 정관 외 운영에 필요한 사항은 이사회의 의결을 거쳐 규칙으로 정한다.</p>
</div>
"""
write("/about/articles/index.html", base_page("정관", "/about/articles/", articles_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("정관", None)], ABOUT_SIBLINGS, "/about/articles/")))

# ------------------------------------------------------------------
# 연혁
# ------------------------------------------------------------------
history_items = [
    ("1993년", ["정신재활연구회 결성 — 정신장애인 가족 교육 개발 및 실시, 정신장애인 정신재활프로그램 개발 및 실시"]),
    ("1999년", ["새미래 정신재활연구소 개소 — 정신장애인을 위한 정신재활 프로그램 인력 양성 워크숍 실시"]),
    ("2005년", ["계명대학교 부설 심리학과 특별연구소 새미래 심리건강연구소 개소"]),
    ("2006년", ["한국 마사회 UCAN CENTER 산하 습관성 도박 상담기관 지정", "보건복지부 바우처 사업: 중소기업 근로자 심리상담 제공기관"]),
    ("2007년", ["대구 교육복지 투자사업 지정기관"]),
    ("2008년", ["한국 임상심리학회 임상심리전문가 수련기관"]),
    ("2012년", ["근로복지공단 대구 서부지사 산재근로자 심리상담 연계기관", "한국심리건강진흥원 설립허가"]),
]
history_html = "".join(
    f'<div class="year"><h3>{year}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
    for year, items in history_items
)
history_body = f"""
<div class="page-hero"><div class="wrap"><h1>연혁</h1></div></div>
<div class="wrap">
<div class="timeline">
{history_html}
</div>
</div>
"""
write("/about/history/index.html", base_page("연혁", "/about/history/", history_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("연혁", None)], ABOUT_SIBLINGS, "/about/history/")))

# ------------------------------------------------------------------
# 조직 및 구성
# ------------------------------------------------------------------
org_partners = ["새미래심리건강연구소(서울)", "새미래심리건강연구소(대구)", "플리마인드", "FPSP",
                "서울특별시립 브릿지종합지원센터", "사회복지법인 성람재단", "사단법인 월드유스비전",
                "참누리정신건강센터", "한국사이코드라마 소시오드라마학회", "계명대학교 심리학과"]
OFFICERS = [("이사장","정혜인","플리마인드"),("이사","손명자","새미래심리건강연구소"),("이사","정지후","상명대학교"),
            ("이사","권오상","다나웰치과"),("이사","서경민","에듀플렉스"),("감사","고미숙","서산본향복지재단"),
            ("감사","조수은","신당종합사회복지관")]
ADVISORS = [("최윤경","계명대학교 심리학과"),("배경규","대구대학교 심리학과"),("김이영","수성대학교 유아교육과"),
            ("신성만","한동대학교 상담심리사회복지학부"),("임경선","서울사이버대학교 특수심리치료학과"),
            ("옥정","서울사이버대학교 특수심리치료학과"),("유연옥","계명대학교 유아교육학과"),
            ("정여주","한국교원대학교 교육학과"),("이정하","정신장애와 인권 파도손")]
org_body = f"""
<div class="page-hero"><div class="wrap"><h1>조직 및 구성</h1></div></div>
<div class="wrap">
<div class="orgc">
  <svg class="orgc-svg" viewBox="0 0 900 470" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="조직도">
    <defs><style>
      .t{{font-family:GyeonggiTitleM,NanumBarunpen,sans-serif;font-weight:normal;fill:#fff;text-anchor:middle;dominant-baseline:middle}}
      .ln{{stroke:#444;stroke-width:2.5;fill:none}}
    </style></defs>
    <!-- 선 -->
    <line class="ln" x1="450" y1="80" x2="450" y2="120"/>
    <line class="ln" x1="150" y1="120" x2="750" y2="120"/>
    <line class="ln" x1="150" y1="120" x2="150" y2="150"/>
    <line class="ln" x1="450" y1="120" x2="450" y2="150"/>
    <line class="ln" x1="750" y1="120" x2="750" y2="150"/>
    <line class="ln" x1="450" y1="230" x2="450" y2="260"/>
    <line class="ln" x1="450" y1="340" x2="450" y2="370"/>
    <line class="ln" x1="450" y1="450" x2="450" y2="470"/>
    <!-- 박스 -->
    <rect x="360" y="0" width="180" height="80" rx="16" fill="#EFC46A"/>
    <text class="t" x="450" y="41" font-size="22">이사장</text>
    <rect x="70" y="150" width="160" height="80" rx="16" fill="#B9CF8A"/>
    <text class="t" x="150" y="191" font-size="22">감사</text>
    <rect x="370" y="150" width="160" height="80" rx="16" fill="#B9CF8A"/>
    <text class="t" x="450" y="191" font-size="22">이사회</text>
    <rect x="650" y="150" width="200" height="80" rx="16" fill="#B9CF8A"/>
    <text class="t" x="750" y="191" font-size="22">자문위원회</text>
    <rect x="290" y="260" width="320" height="80" rx="16" fill="#E8AE94"/>
    <text class="t" x="450" y="301" font-size="22">(사)한국심리건강진흥원</text>
    <rect x="370" y="370" width="160" height="80" rx="16" fill="#B9CF8A"/>
    <text class="t" x="450" y="411" font-size="22">협력기관</text>
  </svg>
  <div class="orgc-partners">
    {''.join(f'<div class="orgc-tile">{p}</div>' for p in org_partners)}
  </div>
</div>

<div class="org-tables">
  <div>
    <h3 class="dot-title">임원회</h3>
    <table class="org-table">
      <thead><tr><th>직함</th><th>성명</th><th>소속</th></tr></thead>
      <tbody>{''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in OFFICERS)}</tbody>
    </table>
  </div>
  <div>
    <h3 class="dot-title">자문위원</h3>
    <table class="org-table">
      <thead><tr><th>성명</th><th>소속</th></tr></thead>
      <tbody>{''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in ADVISORS)}</tbody>
    </table>
  </div>
</div>
</div>
"""
write("/about/organization/index.html", base_page("조직 및 구성", "/about/organization/", org_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("조직 및 구성", None)], ABOUT_SIBLINGS, "/about/organization/")))

# ------------------------------------------------------------------
# 오시는 길
# ------------------------------------------------------------------
def loc_block(title, addr, tel, bus, subway, car, map_q):
    return f"""
<section class="loc">
  <h2 class="dot-title">{title}</h2>
  <div class="loc-grid2">
    <div class="loc-map">
      <iframe src="https://www.google.com/maps?q={map_q}&z=16&hl=ko&output=embed" width="100%" height="380" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen title="{title} 지도"></iframe>
    </div>
    <dl class="loc-info">
      <dt><span class="ic">📍</span>주소</dt><dd>{addr}</dd>
      <dt><span class="ic">☎</span>전화번호</dt><dd>{tel}</dd>
      <dt><span class="ic">ⓘ</span>일반버스 이용 시</dt><dd>{bus}</dd>
      <dt><span class="ic">ⓘ</span>지하철 이용 시</dt><dd>{subway}</dd>
      <dt><span class="ic">ⓘ</span>자가용 이용 시</dt><dd>{car}</dd>
    </dl>
  </div>
</section>"""

location_body = f"""
<div class="page-hero"><div class="wrap"><h1>오시는 길</h1></div></div>
<div class="wrap">
{loc_block("한국심리건강진흥원 본부",
  "대구광역시 달서구 용산로 141 (용산동, 그랜드M타워) 13층", "02-2295-5574",
  "우방죽전타운 앞 하차 : 202-1, 5027, 달서3<br>성서 홈플러스 앞 하차 : 305, 405, 425, 508, 509, 655, 805, 성서2",
  "지하철 2호선 용산역 하차",
  "달서구 용산동 230-12번지 그랜드M타워 13층 한국심리건강진흥원",
  "대구광역시+달서구+용산로+141")}
<hr class="dashed">
{loc_block("한국심리건강진흥원 서울지부",
  "서울특별시 강남구 언주로168길 15 5층 501호", "02-2295-5574",
  "한양아파트, 압구정로데오역 하차(일지아트홀 방면) :<br>143, 145, 240, 301, 342, 362, 472, 4318, 4412, 4419, 6006<br>한양아파트, 압구정로데오역 하차(압구정파출소 방면) :<br>143, 145, 240, 301, 362, 440, 472, 4318, 4412, 6006",
  "지하철 분당선 압구정로데오역 6번 출구에서 500m",
  "강남구 압구정로 46길 26 태창빌딩 3층",
  "서울특별시+강남구+언주로168길+15")}
</div>
"""
write("/about/location/index.html", base_page("오시는 길", "/about/location/", location_body,
      subnav_html=subnav([("홈", "/"), ("진흥원소개", "/about/"), ("오시는 길", None)], ABOUT_SIBLINGS, "/about/location/")))

print("articles / history / organization / location done")

# ------------------------------------------------------------------
# 주요사업안내
# ------------------------------------------------------------------
programs = [
    "구직자 및 퇴직자 심리건강에 관련한 연구 및 지원사업",
    "현대인의 심리건강에 관한 연구",
    "심리건강 증진을 위한 예방, 상담, 재활프로그램 개발 및 보급사업",
    "심리건강관련 전문가 인력양성사업",
    "심리건강에 관한 지역적, 국제적, 상호교류 협력사업",
    "국책사업(도박중독, 인터넷중독, 바우처사업 등) 수행",
    "사회적 소외계층(장애인, 저소득층 등) 및 교육복지투자지원사업",
    "심리건강관련 유전자 연구 및 검사 분석 사업",
    "기타 법인의 목적 달성에 필요한 사업",
]
programs_body = f"""
<div class="panel-wrap"><div class="wrap">
  <h1 class="panel-title">주요사업안내</h1>
  <div class="panel">
    <h2 class="panel-sub">한국심리건강진흥원의 주요사업을 알려드립니다.</h2>
    <ul class="dot-list">
      {''.join(f'<li class="d-{d}">{p}</li>' for p, d in zip(programs, ['g', 's', 'g', 's', 'g', 's', 'g', 's', 'y']))}
    </ul>
  </div>
</div></div>
"""
write("/programs/index.html", base_page("주요사업안내", "/programs/", programs_body, main_class="flush"))

# ------------------------------------------------------------------
# 자격검정 - 목록
# ------------------------------------------------------------------
CERT_ICONS = {
    "psychology-counselor": "c-psych.svg",
    "emotional-labor-counselor": "c-labor.svg",
    "sports-psychology-coach": "c-sports.svg",
    "music-psychologist": "c-music.svg",
    "art-psychology-counselor": "c-art.svg",
    "couples-counselor": "c-couple.svg",
    "parent-counselor": "c-parent.svg",
    "gifted-creativity-instructor": "c-gifted.svg",
    "senior-psychology-counselor": "c-senior.svg",
    "disabled-children-art-counselor": "c-disabled-art.svg",
    "learning-coach": "c-learning.svg",
    "career-aptitude-counselor": "c-career.svg",
    "marine-guide": "c-marine.svg",
    "marine-care-instructor": "c-marine-care.svg",
}
cert_cards = "".join(
    f'<a href="/certifications/{c["slug"]}/"><div class="icon-wrap"><img src="/assets/img/{CERT_ICONS[c["slug"]]}" alt=""></div><h3>{c["title"]}</h3></a>'
    for c in CERTS
)
cert_index_body = f"""
<div class="page-hero"><div class="wrap"><h1>자격검정</h1>
<p style="color:var(--muted);margin-top:12px;">한국심리건강진흥원이 운영하는 민간자격 검정 과정입니다.</p></div></div>
<div class="wrap">
<div class="cert-list">
{cert_cards}
</div>
</div>
"""
write("/certifications/index.html", base_page("자격검정", "/certifications/", cert_index_body))

# ------------------------------------------------------------------
# 자격검정 - 상세
# ------------------------------------------------------------------
def level_block(label, lv):
    if lv is None:
        return ""
    return f"""<div class="cert-level">
  <p class="cert-level-title">{label}</p>
  <p>자격기준 : {lv['req']}<br>
  이수과목 : {lv['subj']}<br>
  자격시험 : {lv['exam']}<br>
  수련내용 : {lv['train']}</p>
</div>"""

cert_siblings = [(c["title"], f"/certifications/{c['slug']}/") for c in CERTS]

for c in CERTS:
    single_level = c["l2"] is None
    level_label_1 = "자격기준" if single_level else "1급"
    body = f"""
<div class="panel-wrap"><div class="wrap">
  <h1 class="panel-title">자격검정</h1>
  <div class="panel cert-panel">
    <h2 class="cert-title">{c['title']} (민간자격 번호 {c['code']})</h2>
    <p class="cert-sub">{c['title']} (민간자격 번호 {c['code']})</p>
    <p>정의 : {c['definition']}<br>
    수련제도: {c['basis']}</p>
    {level_block(level_label_1, c['l1'])}
    {level_block("2급", c['l2'])}
  </div>
</div></div>
"""
    write(f"/certifications/{c['slug']}/index.html",
          base_page(c["title"], "/certifications/", body, main_class="flush",
                    subnav_html=subnav([("홈", "/"), ("자격검정", "/certifications/"), (c["title"], None)],
                                        cert_siblings, f"/certifications/{c['slug']}/")))

print("programs / certifications done:", len(CERTS))

# ------------------------------------------------------------------
# 협력기관
# ------------------------------------------------------------------
PARTNER_LOGOS = ['f258f5_8a103a2fcdff493aae6d1b535392f356~mv2.jpg', 'f258f5_cb6dd269d44f494c8ec5a42228ff3d82~mv2.png', 'f258f5_d56f5b6839ca4f8a9acb657fd6345e97~mv2.png', 'f258f5_82dc6d3f6a444b2bbd7d8ff67f57b907~mv2.jpg', 'f258f5_f612a4a102924853ab7c1b537faedc42~mv2.jpg', 'f258f5_b4ab33706725490b95ceaa59119dbb66~mv2.jpg', 'f258f5_3d27c24d5bae402da088749de7e360ec~mv2.jpg', 'f258f5_4e99d480125b420eb0eb92d94240791f~mv2.png', 'f258f5_aed4d1370b784c018e9f44ac4285c2bc~mv2.png', 'f258f5_a112b1c8a6e54bdfbdbeb9248fa6c261~mv2.png']
PARTNERS = [
    ("플리마인드 심리건강연구소",
     "아동 및 청소년 개인상담, 성인상담, 부부 및 가족상담, 부모교육, 발달장애아동 치료, 습관성 도박 상담, "
     "인터넷중독 상담, 재활상담, 아동 집단 상담, 학습 클리닉, 임상심리전문가 훈련, 심리건강 관련 연구 및 개발",
     "https://www.semiraemind.com"),
    ("새미래심리건강연구소(대구)",
     "아동 및 청소년 개인상담, 성인상담, 부부 및 가족상담, 부모교육, 발달장애아동 치료, 습관성 도박 상담, "
     "인터넷중독 상담, 재활상담, 아동 집단 상담, 학습 클리닉, 임상심리전문가 훈련, 심리건강 관련 연구 및 개발",
     "http://smphc.org"),
    ("플리마인드 기업부설연구소",
     "온라인 심리지원 서비스를 제공하며 심리건강프로그램을 개발 및 보급하고 교육하는 기관. "
     "온라인 서비스는 화상케어링, 문자케어링, 컨텐츠케어링, 웰빙케어링 운영",
     "https://www.plymind.com"),
    ("FPSP",
     "FPSP(미래 문제 해결 프로그램), 텍스트 이해와 사고력, 창의력 검사 TTCT 및 WKOPAY, "
     "VIEW 창의적 문제해결 스타일 검사, CPS 창의력/혁신 교육 프로그램 운영",
     "http://fpsp.or.kr"),
    ("대구재활센터",
     "정신장애환우들의 사회복귀를 추진시키기 위한 정신장애인 사회복귀시설. 개인상담, 집단상담, 기초교육, "
     "약물증상교육, 스트레스 관리, 대인관계 교육, 직업재활, 가족교육, 가정방문, 사회적응훈련",
     "http://www.dgprc.org"),
    ("서울특별시립브릿지종합지원센터",
     "거리 노숙인들에게 편안하고 안정된 생활공간, 이용자 모두가 환영받고 존중되는, 그리고 이용자들의 욕구를 "
     "먼저 알고 직접적 서비스를 제공",
     "http://www.dropin.or.kr"),
    ("사회복지법인 성람재단",
     "소외되고 열악한 환경에 처해있는 이들에게 전문적 사회복지서비스를 제공함으로써 궁극적으로 사회에 복귀하여 "
     "건강한 삶을 영위하도록 도움",
     "http://www.sungram.or.kr"),
    ("사단법인 월드유스비전",
     "청소년들이 변화하는 청소년, 칭찬받는 청소년, 긍정적이고 건강한 청소년이 되어 “웰빙 청소년”을 이룩하고자 "
     "그에 적합한 서비스를 제공하는 기관",
     "http://www.withyouth.co.kr/"),
    ("참누리정신건강상담센터",
     "정신장애환우들의 사회복귀를 추진시키기 위한 정신장애인 사회복귀시설. 개인상담, 집단상담, 기초교육, "
     "약물증상교육, 스트레스 관리, 대인관계 교육, 직업재활, 가족교육, 가정방문, 사회적응훈련",
     "https://cafe.naver.com/chamnuri00"),
    ("한국사이코드라마소시오드라마학회",
     "사이코드라마와 소시오드라마를 통해 인간의 자발성과 창조성을 증진하며 이에 관련한 연구 및 교육을 매개로 "
     "치료자와 전문가를 양성하는 기관",
     "http://kpsychodrama.com/KOR/main/main.php"),
]
PARTNER_LOGO_FILES = ["plymind-lab.svg", "semirae.png", "plymind-corp.svg", "fpsp.png", "dgprc.png",
                      "dropin.png", "sungram.png", "withyouth.png", "chamnuri.png", "kpsychodrama.png"]
partner_html = "".join(
    f"""<div class="partner2">
  <div class="logo2">
    <img src="/assets/img/partners/{logo}" alt="{name}" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
    <span class="logo-fallback">{name}</span>
  </div>
  <div class="partner2-body">
    <h3>{name}</h3>
    <p>{desc}</p>
    <a class="go-btn" href="{url}" target="_blank" rel="noopener">바로가기</a>
  </div>
</div>""" for (name, desc, url), logo in zip(PARTNERS, PARTNER_LOGO_FILES)
)
partners_body = f"""
<div class="panel-wrap"><div class="wrap">
  <h1 class="panel-title">협력기관</h1>
  <div class="panel">
{partner_html}
  </div>
</div></div>
"""
write("/partners/index.html", base_page("협력기관", "/partners/", partners_body, main_class="flush"))

# ------------------------------------------------------------------
# 공지사항
# ------------------------------------------------------------------
# 공지사항은 Jekyll(_notices/ + _layouts/notice.html)로 처리 — build.py에서 생성하지 않음

# ------------------------------------------------------------------
# 개인정보처리방침
# ------------------------------------------------------------------
privacy_body = """
<div class="page-hero"><div class="wrap"><h1>개인정보 보호정책</h1></div></div>
<div class="wrap prose">
<p>우리 헌법은 국민의 기본권인 사생활의 비밀과 자유 및 통신의 비밀을 보장하고 있으므로 도·감청 등에 의한
개인정보 및 사생활의 은밀한 탐지는 원칙적으로 불법입니다. 그러나 우리 사회에 횡행하는 불법 도청, 통신상의
정보 유출로 인하여 심각한 인권 침해가 나타나고 있고 국민 개개인의 자유로운 생활형성이 위협받고 있습니다.</p>
<p>이러한 기본권 침해의 소지를 원천적으로 제거함으로써 한국심리건강진흥원 회원의 프라이버시를 철저히 보호하여
정보화 사회에서의 통신의 자유를 보장하고자 아래와 같이 개인정보보호정책을 명시합니다. 본 정책은 정부의 법률
및 지침의 변경과 진흥원의 정책 변화에 따라 변경될 수 있습니다.</p>

<h2>1. 개인정보의 수집목적 및 이용</h2>
<p>회원님 개인의 정보를 수집하는 목적은 사이트를 통하여 회원님께 최적의 맞춤화된 서비스를 제공해드리기
위한 것입니다. 제공해주신 개인정보를 바탕으로 보다 유용한 정보를 선택적으로 제공하는 것이 가능하게 됩니다.</p>

<h2>2. 수집하는 개인정보 항목 및 수집방법</h2>
<p>최초 회원가입 시 아이디, 생년월일, 별명, 결혼, 추천인 아이디, 패스워드, 성명, e-mail, 주소, 전화번호,
휴대전화 등을 수집합니다. 특정 서비스 제공을 위해 추가적인 정보제공을 요청할 수 있습니다.</p>

<h2>3. 개인정보의 보유 및 폐기</h2>
<p>서비스를 받는 동안 개인정보는 계속 보유·이용되며, 회원탈퇴 요청 또는 목적 달성 시 재생할 수 없는 방법으로
완전히 삭제되어 어떠한 용도로도 열람 또는 이용할 수 없도록 처리됩니다.</p>

<h2>4. 개인정보의 제공 및 공유</h2>
<p>원칙적으로 회원님의 개인정보를 타인 또는 타기업·기관에 공개하지 않습니다. 다만 회원님이 동의한 경우 또는
법적 조치를 위해 필요한 충분한 근거가 있는 경우는 예외로 합니다. 비즈니스 파트너와 공유하는 경우에도 사전에
동의를 구합니다.</p>

<h2>5. 쿠키(cookie)의 운용 및 활용</h2>
<p>개인화되고 맞춤화된 서비스를 제공하기 위해 쿠키를 사용합니다. 회원님은 브라우저 옵션을 통해 쿠키 허용
여부를 선택할 수 있으며, 다만 쿠키 저장을 거부할 경우 로그인이 필요한 서비스는 이용할 수 없습니다.</p>

<h2>6. 개인정보보호를 위한 기술적/제도적 관리</h2>
<p>비밀번호에 의한 보호, 백신프로그램 운영, 침입탐지시스템 설치, 정기적인 백업 등을 통해 개인정보를
보호하고 있으며, 담당 직원을 최소화하고 정기 교육 및 감사를 실시합니다.</p>

<h2>7. 자신의 개인정보 열람, 정정 및 삭제</h2>
<p>회원님은 언제든지 자신의 개인정보를 열람·정정하거나 아이디 삭제를 요청할 수 있습니다. 문의는
help@한국심리건강진흥원.co.kr 로 접수해 주시면 즉시 조치 후 결과를 통보해 드립니다.</p>

<h2>8. 어린이의 개인정보보호</h2>
<p>만 14세 미만 어린이는 자신에 대한 정보를 다른 사람에게 보내기 전 반드시 부모님의 허락을 받아야 합니다.
비밀번호 보안 유지 책임은 회원 본인에게 있습니다.</p>

<hr class="rule">
<p style="color:var(--muted);font-size:14px;">이 개인정보보호정책은 2007년 1월 1일부터 시행합니다.</p>
</div>
"""
write("/privacy/index.html", base_page("개인정보처리방침", "/privacy/", privacy_body))

# ------------------------------------------------------------------
# 이용약관
# ------------------------------------------------------------------
terms_body = """
<div class="page-hero"><div class="wrap"><h1>이용약관</h1>
<p style="color:var(--muted);margin-top:12px;">한국심리건강진흥원은 공정거래위원회에서 심의한 표준약관(제10023호,
인터넷 사이버몰 이용표준약관)을 사용하고 있습니다.</p></div></div>
<div class="wrap prose">

<h2>제1조 (목적)</h2>
<p>이 약관은 한국심리건강진흥원(전자상거래 사업자)이 운영하는 사이버몰(이하 "몰")에서 제공하는 인터넷 관련
서비스 이용에 있어 사이버몰과 이용자의 권리·의무 및 책임사항을 규정함을 목적으로 합니다.</p>

<h2>제2조 (정의)</h2>
<p>"몰"은 진흥원이 재화 또는 용역을 이용자에게 제공하기 위한 가상의 영업장을 말하며, "이용자"는 몰이 제공하는
서비스를 받는 회원 및 비회원을 말합니다.</p>

<h2>제3조 (약관의 명시와 개정)</h2>
<p>몰은 상호, 대표자 성명, 소재지 주소, 연락처, 사업자등록번호 등을 초기 화면에 게시하며, 관련 법령을 위배하지
않는 범위에서 약관을 개정할 수 있습니다. 개정 시 적용일자 7일 전(불리한 변경은 30일 전)부터 공지합니다.</p>

<h2>제4~5조 (서비스의 제공·변경·중단)</h2>
<p>몰은 재화·용역 정보 제공 및 계약 체결, 배송 등의 업무를 수행하며, 설비 보수·고장 등의 사유로 서비스
제공을 일시 중단할 수 있습니다. 이 경우 이용자 또는 제3자가 입은 손해는 원칙적으로 배상합니다.</p>

<h2>제6~8조 (회원가입 및 통지)</h2>
<p>이용자는 가입 양식에 따라 정보를 기입하고 약관에 동의함으로써 회원가입을 신청하며, 허위 기재 등의 사유가
없는 한 회원으로 등록됩니다. 통지는 등록된 전자우편 또는 게시판 공지로 갈음할 수 있습니다.</p>

<h2>제9~16조 (구매·계약·청약철회)</h2>
<p>구매신청, 계약의 성립, 대금 지급방법, 재화의 공급, 환급, 청약철회 등에 관한 절차와 이용자·몰 각각의
책임범위를 규정합니다. 청약철회는 원칙적으로 수신확인통지를 받은 날부터 7일 이내 가능합니다.</p>

<h2>제17조 (개인정보보호)</h2>
<p>몰은 구매계약 이행에 필요한 최소한의 정보만 수집하며, 이용자 동의 없이 목적 외로 이용하거나 제3자에게
제공하지 않습니다. 이용자는 언제든지 자신의 개인정보 열람 및 오류 정정을 요구할 수 있습니다.</p>

<h2>제18~20조 (몰의 의무 / 회원의 의무)</h2>
<p>몰은 법령과 공서양속에 반하는 행위를 하지 않으며 안정적인 서비스를 제공하기 위해 노력합니다. 회원은
ID·비밀번호 관리 책임을 지며, 허위 등록, 타인 정보 도용, 지적재산권 침해 등의 행위를 해서는 안 됩니다.</p>

<h2>제21~22조 (연결몰 관계 / 저작권)</h2>
<p>하이퍼링크로 연결된 몰 간의 책임 범위를 규정하며, 몰이 작성한 저작물의 저작권은 몰에 귀속됩니다.</p>

<h2>제23~24조 (분쟁해결 / 재판권 및 준거법)</h2>
<p>몰은 피해보상처리기구를 운영하며, 분쟁 발생 시 공정거래위원회 또는 시·도지사가 의뢰하는 분쟁조정기관의
조정에 따를 수 있습니다. 소송은 이용자 주소지 관할 법원에 제기하며 한국법을 적용합니다.</p>

<hr class="rule">
<p style="color:var(--muted);font-size:14px;">※ 전문은 방문 또는 문의를 통해 안내해 드립니다.</p>
</div>
"""
write("/terms/index.html", base_page("이용약관", "/terms/", terms_body))

print("partners / notice / privacy / terms done")
