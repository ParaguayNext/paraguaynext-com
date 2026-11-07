#!/usr/bin/env python3
"""Preview-build checks. Run: python3 build/check.py  (exit 1 on any failure).
- every page has <meta name="robots" content="noindex, nofollow">
- robots.txt disallows everything
- .htaccess sends X-Robots-Tag: noindex
- no <script>, no iframes, no forms
- no external images or other subresources
- external links are plain (no affiliate or tracking query params)
- every local href/src/srcset resolves to a file in site/
- primary CTA (Skool) is present on every page
- affiliate disclosure is in every page footer
- Cloudflare Web Analytics snippet is not emitted
- brand files are byte-identical to the locked originals (when the originals folder exists)
"""
import pathlib, re, sys, hashlib, html.parser, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
SKOOL = "https://www.skool.com/paraguaynext-6232"
AFFILIATE = ("Some links are affiliate links; we may earn a commission at no extra cost to you. "
             "We only list services we would point a friend to.")
PAGES = [
    "index.html",
    "guides.html",
    "guides/moving-to-paraguay.html",
    "guides/first-30-days.html",
    "guide-template.html",
    "community.html",
    "events.html",
    "about.html",
    "sponsors.html",
    "legal.html",
]
LOCKED = pathlib.Path("/workspace/brand/logo-alt-lapacho")
TRACKING_KEYS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "utm_id",
    "fbclid", "gclid", "msclkid", "mc_eid", "mc_cid", "igshid", "yclid", "twclid",
    "ref", "affiliate", "aff", "aff_id", "_ga",
}
errs = []

class P(html.parser.HTMLParser):
    def __init__(s):
        super().__init__()
        s.refs = []  # (attr, value)
        s.ids = set()
        s.tags = set()
        s.robots = None
    def handle_starttag(s, t, a):
        a = dict(a)
        s.tags.add(t)
        if "id" in a:
            s.ids.add(a["id"])
        if t == "meta" and a.get("name") == "robots":
            s.robots = a.get("content")
        for k in ("href", "src"):
            if a.get(k):
                s.refs.append((k, a[k]))
        if a.get("srcset"):
            for part in a["srcset"].split(","):
                bits = part.strip().split()
                if bits:
                    s.refs.append(("srcset", bits[0]))

def local_ok(page, ref):
    path = urllib.parse.urlparse(ref).path
    if not path:
        return True
    target = (page.parent / path).resolve()
    try:
        target.relative_to(SITE.resolve())
    except ValueError:
        return False
    return target.is_file()

def tracking(url):
    u = urllib.parse.urlparse(url)
    if "utm_" in url.lower():
        return True
    qs = urllib.parse.parse_qs(u.query, keep_blank_values=True)
    for key in qs:
        if key.lower() in TRACKING_KEYS or key.lower().startswith("utm_"):
            return True
    return False

for name in PAGES:
    f = SITE / name
    if not f.exists():
        errs.append(f"missing page {name}")
        continue
    txt = f.read_text(encoding="utf-8")
    p = P()
    p.feed(txt)
    if p.robots != "noindex, nofollow":
        errs.append(f"{name}: robots meta = {p.robots!r}")
    for bad in ("script", "iframe", "form"):
        if bad in p.tags:
            errs.append(f"{name}: contains <{bad}>")
    if "cloudflareinsights" in txt or "YOUR_TOKEN" in txt:
        errs.append(f"{name}: analytics snippet was emitted")
    if SKOOL not in [v for k, v in p.refs]:
        errs.append(f"{name}: no Skool CTA link")
    if AFFILIATE not in txt:
        errs.append(f"{name}: missing affiliate disclosure")
    if "Events and meetups" in txt.split("<footer", 1)[-1]:
        errs.append(f"{name}: footer still says Events and meetups")
    for attr, r in p.refs:
        u = urllib.parse.urlparse(r)
        if u.scheme in ("http", "https"):
            if attr in ("src", "srcset"):
                errs.append(f"{name}: external resource {r}")
            elif tracking(r):
                errs.append(f"{name}: tracking or affiliate param in {r}")
            continue
        if u.scheme:
            errs.append(f"{name}: unsupported URL scheme {r}")
            continue
        if r.startswith("#"):
            frag = r[1:]
            if frag and frag not in p.ids:
                errs.append(f"{name}: dangling anchor {r}")
            continue
        if urllib.parse.urlparse(r).path and not local_ok(f, r):
            errs.append(f"{name}: broken local ref {r}")

home = (SITE / "index.html").read_text(encoding="utf-8") if (SITE / "index.html").exists() else ""
if "Meetups" in home:
    errs.append("home still mentions Meetups")
if ">Coming soon<" not in home:
    errs.append("home cost-of-living card is missing Coming soon")
if re.search(r"US\$|Gs\.", home):
    errs.append("home contains a price figure")

g2 = SITE / "guides" / "first-30-days.html"
if g2.exists():
    g2txt = g2.read_text(encoding="utf-8")
    if g2txt.count(AFFILIATE) < 2:
        errs.append("guide 2: affiliate disclosure must appear in the footer and next to the eSIM links")
    if "Airalo" not in g2txt:
        errs.append("guide 2: missing eSIM section")

for css in SITE.glob("assets/css/*.css"):
    t = css.read_text()
    for m in re.findall(r"url\(([^)]+)\)", t):
        m = m.strip("'\"")
        if m.startswith(("http:", "https:", "//")):
            errs.append(f"{css.name}: external url {m}")
        elif not (css.parent / m).resolve().exists():
            errs.append(f"{css.name}: broken url {m}")
    if "@import" in t:
        errs.append(f"{css.name}: @import found")

rb = (SITE / "robots.txt").read_text() if (SITE / "robots.txt").exists() else ""
if not re.search(r"(?m)^User-agent:\s*\*\s*$", rb) or not re.search(r"(?m)^Disallow:\s*/\s*$", rb):
    errs.append("robots.txt is not disallow-all")
ht = (SITE / ".htaccess").read_text() if (SITE / ".htaccess").exists() else ""
if not re.search(r"X-Robots-Tag", ht) or "noindex" not in ht or "nofollow" not in ht:
    errs.append(".htaccess missing X-Robots-Tag noindex, nofollow")

partial = ROOT / "build" / "partials" / "cf-web-analytics.html"
build_src = (ROOT / "build" / "build.py").read_text(encoding="utf-8")
if "ANALYTICS_ENABLED = False" not in build_src:
    errs.append("build.py ANALYTICS_ENABLED is not False")
if not partial.exists():
    errs.append("missing build/partials/cf-web-analytics.html")
else:
    pt = partial.read_text(encoding="utf-8")
    if "YOUR_TOKEN" not in pt or "static.cloudflareinsights.com" not in pt:
        errs.append("analytics partial is missing the switched-off Cloudflare snippet")
    if re.search(r'"token":\s*"(?!YOUR_TOKEN")[^"]+"', pt):
        errs.append("analytics partial contains a token other than YOUR_TOKEN")

if LOCKED.exists():
    n = 0
    for f in (SITE / "assets" / "brand").rglob("*"):
        if f.is_file():
            rel = f.relative_to(SITE / "assets" / "brand")
            o = LOCKED / ("README.md" if str(rel) == "LOGO-README.md" else rel)
            if not o.exists() or hashlib.sha256(o.read_bytes()).digest() != hashlib.sha256(f.read_bytes()).digest():
                errs.append(f"brand file differs from locked original: {rel}")
            n += 1
    print(f"brand: {n} files compared byte-for-byte with {LOCKED}")
else:
    print("brand: locked originals not present on this machine, skipped byte compare")

if errs:
    print("FAIL")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print("analytics: disabled, snippet not emitted")
print(f"PASS: {len(PAGES)} pages checked")
