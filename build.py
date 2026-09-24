"""앱 저장소의 docs/support.md, docs/privacy.md로 index.html, privacy.html을 만든다.

    python3 build.py [앱 저장소 docs 경로]   # 기본값: ../Renotify/docs
"""
import re, sys, html
from pathlib import Path

OUT = Path(__file__).resolve().parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT.parent / "Renotify" / "docs"

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return t

def blocks(text):
    out = []
    for chunk in [c for c in text.strip().split("\n\n") if c.strip()]:
        lines = chunk.strip().split("\n")
        if all(l.startswith("- ") for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lines) + "</ul>")
        else:
            out.append("<p>" + "<br>".join(inline(l) for l in lines) + "</p>")
    return "\n".join(out)

def render(part, anchor):
    head, *secs = re.split(r"^## ", part.strip(), flags=re.M)
    hl = head.strip().split("\n\n")
    h = [f'<h1 id="{anchor}">{inline(hl[0][2:])}</h1>']
    for c in hl[1:]:
        c = c.strip()
        first, _, rest = c.partition("\n")
        if first.startswith("**") and first.endswith("**"):
            h.append(f'<p class="lead">{inline(first[2:-2])}</p>')
            if rest.strip():
                h.append(f'<div class="intro">{blocks(rest)}</div>')
        elif re.match(r"^(최종 수정일|Last updated)", c):
            h.append(f'<p class="meta">{inline(c)}</p>')
        else:
            h.append(f'<div class="intro">{blocks(c)}</div>')
    for s in secs:
        title, body = s.split("\n", 1)
        h.append(f"<h2>{inline(title)}</h2>")
        subs = re.split(r"^### ", body.strip(), flags=re.M)
        if subs[0].strip():
            h.append(f'<div class="card">{blocks(subs[0])}</div>')
        for q in subs[1:]:
            qt, qb = q.split("\n", 1)
            h.append(f'<div class="card"><h3>{inline(qt)}</h3>{blocks(qb)}</div>')
    return "\n".join(h)

PAGES = [
    ("support.md", "index.html", "알림함 지원 · Renotify Support", "알림함 앱 사용 중 자주 묻는 질문과 문의처 · FAQ and contact for Renotify"),
    ("privacy.md", "privacy.html", "알림함 개인정보 처리방침 · Renotify Privacy Policy", "알림함은 개인정보를 수집하지 않아요 · Renotify does not collect any personal data"),
]
for md, out, title, desc in PAGES:
    ko, en = open(SRC / md).read().split("\n---\n")
    nav = "".join(
        f'<a href="{o}"{" aria-current=\"page\"" if o == out else ""}>{label}</a>'
        for o, label in [("index.html", "지원 · Support"), ("privacy.html", "개인정보 · Privacy")])
    page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="logo.png">
<link rel="apple-touch-icon" href="logo.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><div class="wrap">
<img src="logo.png" alt="">
<span class="name">알림함 · Renotify</span>
<nav>{nav}</nav>
</div></header>
<main class="wrap">
<p class="lang"><a href="#ko">한국어</a> · <a href="#en">English</a></p>
{render(ko, "ko")}
<hr>
<div lang="en">
{render(en, "en")}
</div>
</main>
<footer>© 2026 Renotify</footer>
</body>
</html>
"""
    open(OUT / out, "w").write(page)
