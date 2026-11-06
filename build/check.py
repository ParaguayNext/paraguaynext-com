#!/usr/bin/env python3
"""Preview-build checks. Run: python3 build/check.py  (exit 1 on any failure).
- every page has <meta name="robots" content="noindex, nofollow">
- robots.txt disallows everything
- no <script>, no iframes, no external requests other than the Skool CTA link
- every local href/src resolves to a file in site/
- primary CTA (Skool) is present on every page
- brand files are byte-identical to the locked originals (when the originals folder exists)"""
import pathlib, re, sys, hashlib, html.parser, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
SKOOL = "https://www.skool.com/paraguaynext-6232"
PAGES = ["index.html","guides.html","guide-template.html","community.html","events.html","about.html","sponsors.html","legal.html"]
LOCKED = pathlib.Path("/workspace/brand/logo-alt-lapacho")
errs = []
class P(html.parser.HTMLParser):
    def __init__(s): super().__init__(); s.refs=[]; s.ids=set(); s.tags=set(); s.robots=None
    def handle_starttag(s, t, a):
        a=dict(a); s.tags.add(t)
        if "id" in a: s.ids.add(a["id"])
        if t=="meta" and a.get("name")=="robots": s.robots=a.get("content")
        for k in ("href","src"):
            if a.get(k): s.refs.append(a[k])
for name in PAGES:
    f = SITE/name
    if not f.exists(): errs.append(f"missing page {name}"); continue
    txt = f.read_text(encoding="utf-8"); p = P(); p.feed(txt)
    if p.robots != "noindex, nofollow": errs.append(f"{name}: robots meta = {p.robots!r}")
    for bad in ("script","iframe","form"):
        if bad in p.tags: errs.append(f"{name}: contains <{bad}>")
    if SKOOL not in p.refs: errs.append(f"{name}: no Skool CTA link")
    for r in p.refs:
        u = urllib.parse.urlparse(r)
        if u.scheme in ("http","https"):
            if r != SKOOL: errs.append(f"{name}: external ref {r}")
            continue
        if r.startswith("#"):
            if r != "#" and r[1:] not in p.ids: errs.append(f"{name}: dangling anchor {r}")
            continue
        path = u.path
        if path and not (SITE/path).exists(): errs.append(f"{name}: broken local ref {r}")
for css in SITE.glob("assets/css/*.css"):
    t = css.read_text()
    for m in re.findall(r"url\(([^)]+)\)", t):
        m = m.strip("'\"")
        if m.startswith(("http:","https:","//")): errs.append(f"{css.name}: external url {m}")
        elif not (css.parent/m).resolve().exists(): errs.append(f"{css.name}: broken url {m}")
    if "@import" in t: errs.append(f"{css.name}: @import found")
rb = (SITE/"robots.txt").read_text() if (SITE/"robots.txt").exists() else ""
if not re.search(r"(?m)^User-agent:\s*\*\s*$", rb) or not re.search(r"(?m)^Disallow:\s*/\s*$", rb):
    errs.append("robots.txt is not disallow-all")
if LOCKED.exists():
    n=0
    for f in (SITE/"assets/brand").rglob("*"):
        if f.is_file():
            rel = f.relative_to(SITE/"assets/brand")
            o = LOCKED/("README.md" if str(rel)=="LOGO-README.md" else rel)
            if not o.exists() or hashlib.sha256(o.read_bytes()).digest()!=hashlib.sha256(f.read_bytes()).digest():
                errs.append(f"brand file differs from locked original: {rel}")
            n+=1
    print(f"brand: {n} files compared byte-for-byte with {LOCKED}")
else:
    print("brand: locked originals not present on this machine, skipped byte compare")
if errs:
    print("FAIL"); [print(" -", e) for e in errs]; sys.exit(1)
print(f"PASS: {len(PAGES)} pages checked")
