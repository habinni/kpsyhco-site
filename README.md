# 한국심리건강진흥원 정적 사이트

Wix(plymind3.wixsite.com/my-site) 콘텐츠를 그대로 옮긴 정적 HTML 사이트입니다.
GitHub Pages로 무료 호스팅하고, 기존 도메인 `kpsyhco.co.kr`을 그대로 연결할 수 있습니다.

## 1. GitHub에 올리기

```bash
cd site
git init
git add .
git commit -m "정적 사이트 초기 버전"
git branch -M main
git remote add origin https://github.com/<계정명>/<저장소명>.git
git push -u origin main
```

## 2. GitHub Pages 활성화

1. GitHub 저장소 → **Settings → Pages**
2. **Source**: `Deploy from a branch` 선택
3. **Branch**: `main` / `/(root)` 선택 후 저장
4. 잠시 후 `https://<계정명>.github.io/<저장소명>/` 로 접속되면 성공

이 저장소에는 이미 `CNAME` 파일(`kpsyhco.co.kr`)이 들어있어서,
GitHub Pages 설정 화면의 **Custom domain** 칸에도 자동으로 `kpsyhco.co.kr`이 표시됩니다.

## 3. 도메인 네임서버 변경 (후이즈)

지금 `kpsyhco.co.kr`의 네임서버는 `ns2.wixdns.net` / `ns3.wixdns.net` (Wix)로 되어 있습니다.
이걸 GitHub Pages를 가리키도록 등록대행자((주)후이즈) 관리 페이지에서 바꿔야 합니다.

**A. 후이즈에서 DNS를 직접 관리하는 경우 (권장)**

후이즈 도메인 관리 → DNS 설정에서 아래 레코드를 등록:

| 타입 | 호스트 | 값(Value) |
|---|---|---|
| A | @ (또는 공란) | 185.199.108.153 |
| A | @ (또는 공란) | 185.199.109.153 |
| A | @ (또는 공란) | 185.199.110.153 |
| A | @ (또는 공란) | 185.199.111.153 |
| CNAME | www | `<계정명>.github.io` |

**B. 후이즈에서 네임서버 자체를 바꾸는 경우**

네임서버 이전은 DNS를 직접 관리할 수 있는 서비스(예: Cloudflare 무료 플랜)로 옮긴 뒤,
그 서비스에서 위와 같은 A/CNAME 레코드를 등록하는 방식도 가능합니다.

DNS 반영에는 보통 몇 분~최대 48시간이 걸립니다. 반영 후 GitHub 저장소 **Settings → Pages**에서
"Enforce HTTPS"를 켜면 `https://kpsyhco.co.kr`로 안전하게 접속됩니다.

## 4. 폴더 구조

```
/                     홈
/about/               진흥원소개
/about/purpose/       설립목적
/about/ceo/           이사장프로필 (이사장 + 초대 이사장)
/about/articles/      정관
/about/history/       연혁
/about/organization/  조직 및 구성
/about/location/      오시는 길
/programs/            주요사업안내
/certifications/      자격검정 목록 (14종 상세 페이지 포함)
/partners/            협력기관
/notice/              공지사항 (현재 공지 없음 안내)
/privacy/             개인정보처리방침
/terms/               이용약관
/assets/css/style.css 디자인 시스템
/assets/js/nav.js     모바일 메뉴 스크립트
CNAME                 GitHub Pages 커스텀 도메인 설정 파일
```

## 5. 내용 수정하기

모든 페이지는 순수 HTML/CSS라 코드를 몰라도 텍스트 부분만 찾아 고치면 됩니다.
(원한다면 `/mnt/user-data/outputs` 쪽에 build.py 소스도 함께 전달할 수 있어요 —
데이터만 바꾸면 전체 사이트를 다시 생성할 수 있는 스크립트입니다.)

## 참고

- 공지사항(`/notice/`)은 Wix 원본에서 게시판 위젯이 비어 있었던 페이지라 안내 문구만 넣어두었습니다.
  추후 실제 공지가 생기면 `notice/index.html`에 항목을 추가하면 됩니다.
- 도메인 자체의 등록/유지비(후이즈에 내는 연 비용)는 이번 변경과 무관하게 계속 발생합니다.
  없어지는 것은 Wix 호스팅 구독료뿐입니다.

## 이미지 안내

로고, 메인 배너 일러스트, 아이콘은 모두 `assets/img/` 폴더에 들어있는 **자체 제작 SVG**입니다.
외부(Wix) 서버에 의존하지 않으므로 Wix를 해지해도 그대로 유지되며, 저작권 문제도 없습니다.

- `logo.png` — 로고(원본 PNG, 배경 투명 처리) · `logo-1000.png` — 인쇄용 고해상도
- `hero.svg` — 메인 배너 일러스트(가족·집·식물)
- `band-*.svg` — 홈 4칸 띠 아이콘
- `p-*.svg` — 설립목적 8개 아이콘
- `c-*.svg` — 자격검정 14개 아이콘

협력기관 로고와 이사장 사진, 임원회/자문위원 명단 이미지는 실물 로고·사진을 임의로 그릴 수 없어
텍스트로 대체했습니다. 실제 파일을 넣고 싶으시면 `assets/img/`에 추가하고 해당 HTML만 교체하면 됩니다.

## 협력기관 로고

`assets/img/partners/` 폴더에 10개 기관 로고가 모두 들어있습니다.
플리마인드(2종)·새미래심리건강연구소는 SVG, 나머지 7곳은 원본 사이트 화면에서 잘라낸 PNG입니다.
더 선명한 원본 로고 파일이 있으면 같은 파일명으로 덮어쓰면 됩니다.

## 공지사항 올리는 방법 (GitHub 웹에서 바로)

공지는 `_notices/` 폴더에 글 하나당 파일 하나로 관리합니다. 파일을 추가하면
목록(`/notice/`)과 상세 페이지가 GitHub Pages에서 자동으로 만들어집니다 (1~2분 소요).

1. GitHub 저장소 → `_notices` 폴더 클릭
2. 오른쪽 위 **Add file → Create new file**
3. 파일 이름: `2026-09-15-제목.md` 형식 (날짜-영문또는한글제목.md)
4. 내용은 아래 형식으로 작성:

```
---
title: 2026년 하반기 자격검정 일정 안내
date: 2026-09-15
---

여기부터 본문입니다. 줄바꿈은 빈 줄로 구분합니다.

- 목록은 이렇게
- **굵게**, *기울임* 가능

[링크 텍스트](https://example.com)
```

5. 아래 **Commit changes** 버튼 클릭 → 끝

- 사진을 넣으려면 `assets/img/notice/` 폴더에 이미지를 올린 뒤 본문에
  `![설명](/assets/img/notice/파일명.jpg)` 형태로 적으면 됩니다.
- 글을 지우려면 `_notices/`에서 해당 파일을 열고 휴지통 아이콘 → Commit.
- `_notices/2026-09-01-sample.md` 는 예시 파일이니 지워도 됩니다.

## 폰트 저작권

- 사이트명(헤더 "(사) 한국심리건강진흥원"): **KBIZ한마음고딕** (중소기업중앙회 배포, 무료·상업 사용 가능. `assets/fonts/KBIZHanmaumGothic.woff` 포함)
- 제목·메뉴·버튼 등: **경기천년제목** (경기도청 배포, 무료·상업 사용 가능·로고 사용 가능. 폰트 파일 `assets/fonts/GyeonggiTitleM.woff` 를 사이트에 직접 포함)
- 본문: **나눔바른펜** (네이버 배포, SIL OFL — 무료·상업 사용 가능. 네이버 웹폰트 서버에서 불러옴)

둘 다 별도 비용이나 표기 의무가 없습니다.

## 점검 완료 항목 (2026-09-11)

- 31개 HTML 페이지 내부 링크·이미지 경로 전수 검사 — 깨진 링크 없음
- 외부 의존: Pretendard 폰트(CDN), 구글맵 임베드, 협력기관 외부 링크만 있음 (Wix 의존 없음)
- 데스크톱(1280px)·모바일(390px) 실제 브라우저 렌더링 확인
- 모바일 메뉴 열기/닫기, 2단 배치(홈 안내띠·자격검정 아이콘) 확인
