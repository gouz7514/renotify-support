# 알림함(Renotify) 지원 사이트

App Store에 제출하는 **지원 URL**과 **개인정보 처리방침 URL**이 가리키는 정적 사이트이자, 앱이 쓰는 **단축어 링크**를 관리하는 곳이다.
GitHub Pages로 배포되며, `main`에 푸시하면 몇 분 안에 반영된다.

- 지원: https://gouz7514.github.io/renotify-support/
- 개인정보 처리방침: https://gouz7514.github.io/renotify-support/privacy.html

## 구성

| 파일 | 용도 |
|---|---|
| `index.html` | 지원 페이지 (FAQ, 한국어 + 영어) |
| `privacy.html` | 개인정보 처리방침 (한국어 + 영어) |
| `style.css` | 애플 기본 앱 톤, 라이트/다크 자동 (pinit-support와 같음) |
| `logo.png` | 앱 아이콘 128px |
| `src/support.md`, `src/privacy.md` | 지원·처리방침 원문 (한국어 + 영어) |
| `build.py` | md → HTML 변환 |
| `links.json` | 언어별 단축어 iCloud ID. 앱(`ShortcutLink`)이 읽는다 |
| `shortcut/ko/`, `shortcut/en/` | 앱 밖에서 공유하는 단축어 열기 페이지 |
| `guide/ko/1~5.webp`, `guide/en/1~5.webp` | 앱 설정의 자동화 가이드 이미지. 앱(`SetupScreen`)이 읽는다 |

지원·처리방침 페이지에는 JS가 없다. 원문은 이 저장소의 `src/support.md`, `src/privacy.md`이고, HTML은 `build.py`로 만든다.

## 내용을 고칠 때

`src/`의 md를 고친 뒤 스크립트를 돌리고 결과 HTML을 함께 커밋·푸시한다.

```sh
python3 build.py
```

처리방침 본문을 바꾸면 위쪽 최종 수정일도 함께 고칠 것.

## 단축어를 다시 공유했을 때

`links.json`의 iCloud ID를 바꿔 푸시한다. 앱 업데이트는 필요 없다. 앱의 `ShortcutLink.fallbackIDs`도 같은 값으로 맞춰 둔다.

## 가이드 이미지를 바꿀 때

같은 파일 이름으로 덮어써 푸시하면 앱 업데이트 없이 바뀐다. 폭 900px WebP로 맞춘다.

```sh
cwebp -q 80 -resize 900 0 원본.png -o guide/ko/1.webp
```

이미지 개수나 각 단계의 설명 문구는 앱에 들어 있으므로, 단계 자체가 바뀌면 앱도 고쳐야 한다.
