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
| `build.py` | md → HTML 변환 |
| `links.json` | 언어별 단축어 iCloud ID. 앱(`ShortcutLink`)이 읽는다 |
| `shortcut/ko/`, `shortcut/en/` | 앱 밖에서 공유하는 단축어 열기 페이지 |

지원·처리방침 페이지에는 JS가 없다. 원문은 앱 저장소의 `docs/support.md`, `docs/privacy.md`이고, HTML은 `build.py`로 만든다.

## 내용을 고칠 때

md를 고친 뒤 이 저장소에서 스크립트를 돌리고 결과 HTML을 커밋·푸시한다. 앱 저장소가 옆 폴더(`../Renotify`)에 있다고 가정한다.

```sh
python3 build.py              # 또는 python3 build.py <앱 저장소>/docs
```

처리방침 본문을 바꾸면 위쪽 최종 수정일도 함께 고칠 것.

## 단축어를 다시 공유했을 때

`links.json`의 iCloud ID를 바꿔 푸시한다. 앱 업데이트는 필요 없다. 앱의 `ShortcutLink.fallbackIDs`도 같은 값으로 맞춰 둔다.
