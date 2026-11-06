#!/usr/bin/env python3
"""Generates the ParaguayNext wireframe pages (DRAFT). Run: python3 _build/build.py
Writes the 8 pages into ../site/."""
import pathlib, html
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
SKOOL = "https://www.skool.com/paraguaynext-6232"
CTA = "Join the free community"
DISCLAIMER = ("This is general information, not legal, tax, or financial advice. Rules change; "
              "check with a licensed professional in Paraguay before you act. "
              "ParaguayNext is not an immigration agency.")

def ph(text, tag="COPY"):
    return f'<span class="ph"><span class="ph-tag">[{tag}]</span>{text}</span>'

def cta(cls="btn--primary", extra=""):
    return f'<a class="btn {cls} {extra}" href="{SKOOL}" rel="noopener">{CTA}</a>'

NAV = [("guides.html","Guides"),("community.html","Community"),("events.html","Events"),("about.html","About")]
SOCIAL = ["X","Instagram","TikTok","Snapchat","Telegram","WhatsApp"]

GUIDES = [  # working titles from /workspace/pm/paraguaynext-plan.md section 2
  # (title, tags, disclaimer, image_slug, alt)
  ("Moving to Paraguay: the step-by-step plan", ["plan"], False,
   "guide-01-moving-to-paraguay-web-800x412",
   "Illustrated cover for Moving to Paraguay: packing crates and a map of Paraguay"),
  ("Your first 30 days in Paraguay", ["arr"], False,
   "guide-02-first-30-days-web-800x412",
   "Illustrated cover for Your first 30 days: calendar and everyday Paraguay errands"),
  ("Cost of living in Paraguay", ["plan","arr"], False,
   "guide-03-cost-of-living-web-800x412",
   "Illustrated cover for Cost of living: market produce and everyday expenses"),
  ("Tax and residency basics (general information)", ["plan","money"], True,
   "guide-04-tax-and-residency-basics-web-800x412",
   "Illustrated cover for Tax and residency basics: documents and a residence stamp"),
  ("Making money and starting a business in Paraguay", ["money"], False,
   "guide-05-making-money-web-800x412",
   "Illustrated cover for Making money: laptop workspace and local business motifs"),
]
TAGNAME = {"plan":"Planning to move","arr":"Just arrived","money":"Money and business"}

SECTIONS = ["Move planning","New arrivals","Meetups","Events","Tech","Business ideas","Making money","Tax and investments"]
SYMBOL = "assets/brand/symbol/lapacho-symbol-lapacho.svg"

def social(label_note=True):
    items = "".join(f'<a href="#" data-placeholder="social-{s.lower()}" title="Placeholder link — URL not supplied">{s} <small>[LINK]</small></a>' for s in SOCIAL)
    return f'<div class="social">{items}</div>'

import re as _re
def email_box(title="Get the free guides by email"):
    eid = _re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")  # deterministic id (was id(title))
    return f'''<div class="email-box" aria-label="Email signup placeholder">
  <label for="email-ph-{eid}">{title}</label>
  <div class="email-row">
    <input id="email-ph-{eid}" type="email" placeholder="you@example.com" disabled aria-disabled="true">
    <button class="btn btn--ghost btn--sm" type="button" disabled>{ph("Button label","COPY")}</button>
  </div>
  <p class="note">PLACEHOLDER — not connected. No form is submitted and no data is collected. Email provider not chosen yet (Roger's decision; plan: double opt-in, welcome email linking to Skool).</p>
</div>'''

def guide_card(i, g):
    title, tags, dis, img_slug, alt = g
    t = "".join(f'<span class="tag">{TAGNAME[x]}</span>' for x in tags)
    cls = " ".join(f"t-{x}" for x in tags)
    # Guide cards sit below the fold on home and guides; lazy-load.
    return f'''<article class="card {cls}">
  <picture class="card-media">
    <source type="image/webp" srcset="assets/images/guide-cards/{img_slug}.webp">
    <img src="assets/images/guide-cards/{img_slug}.jpg" alt="{html.escape(alt)}" width="800" height="412" loading="lazy" decoding="async">
  </picture>
  <div class="tags">{t}</div>
  <h3>{html.escape(title)}</h3>
  <p class="microcopy">Working title from plan</p>
  <p>{ph("One-line summary of the guide.")}</p>
  <a class="more" href="guide-template.html">Read the guide →</a>
</article>'''


def cta_block():
    return f'''<section class="cta-block section" aria-label="Join the community">
  <div class="wrap"><div class="cta-inner">
    <img src="{SYMBOL}" alt="" width="72" height="72">
    <div><h2>{ph("CTA headline, e.g. a short invitation to join.")}</h2>
      <p>{ph("One supporting line about what members get.")}</p></div>
    <div>{cta()}</div>
  </div></div>
</section>'''

def page(fname, title, body, current=None):
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h==current else ""}>{l}</a>' for h,l in NAV)
    mnav = nav + f'<a class="btn btn--primary" href="{SKOOL}" rel="noopener">{CTA}</a>'
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{html.escape(title)} — ParaguayNext [WIREFRAME DRAFT]</title>
<meta name="description" content="[COPY] Meta description placeholder.">
<link rel="icon" href="assets/brand/favicon/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/brand/favicon/favicon.ico" sizes="16x16 32x32">
<link rel="apple-touch-icon" href="assets/brand/favicon/apple-touch-icon-180.png">
<link rel="stylesheet" href="assets/css/wireframe.css">
</head>
<body>
<div class="wf-banner"><b>WIREFRAME DRAFT</b> · not published · placeholder copy is marked [COPY], [IMAGE], [LINK]</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/brand/lockup/lockup-serif-horizontal-light.svg" alt="ParaguayNext" width="168" height="44"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <span class="header-cta">{cta("btn--primary","btn--sm")}</span>
    <details class="menu"><summary>Menu</summary><nav aria-label="Main (mobile)">{mnav}</nav></details>
  </div>
</header>
<main>
{body}
{cta_block()}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <img src="assets/brand/lockup/lockup-serif-horizontal-dark.svg" alt="ParaguayNext" width="152" height="40">
        <p>{ph("Short footer line about ParaguayNext.")}</p>
        {cta()}
      </div>
      <div><h4>Site</h4><ul>
        <li><a href="guides.html">Guides</a></li><li><a href="community.html">Community</a></li>
        <li><a href="events.html">Events and meetups</a></li><li><a href="about.html">About</a></li>
        <li><a href="sponsors.html">Sponsors</a></li></ul>
        <h4 style="margin-top:20px">Legal</h4><ul>
        <li><a href="legal.html#privacy">Privacy</a></li><li><a href="legal.html#terms">Terms</a></li><li><a href="legal.html#disclaimer">Disclaimer</a></li></ul>
      </div>
      <div><h4>Follow</h4>{social()}</div>
    </div>
    <p class="footer-disclaimer">{DISCLAIMER}</p>
  </div>
</footer>
</body>
</html>
'''
    (OUT/fname).write_text(doc, encoding="utf-8")

def mobile_cta():
    return ""  # top CTA on mobile lives in the hero/page intro (header CTA hidden <720px)

def intro(eyebrow, h1, lead, show_cta=True):
    c = f'<div class="cta-row">{cta()}</div>' if show_cta else ""
    return f'''<section class="hero"><div class="wrap" style="grid-template-columns:1fr">
  <div class="hero-card"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p>{c}</div>
</div></section>'''

# 1 Home
cards = "".join(guide_card(i+1,g) for i,g in enumerate(GUIDES))
secs = "".join(f'<article class="card"><img class="icon" src="assets/brand/symbol/lapacho-symbol-on-green.svg" alt=""><h3>{s}</h3><p>{ph("One line on what this section offers.")}</p></article>' for s in SECTIONS)
home = f'''<section class="hero"><div class="wrap">
  <div class="hero-card">
    <span class="eyebrow">For expats moving to and living in Paraguay</span>
    <h1>{ph("One-line promise (headline).")}</h1>
    <p class="lead">{ph("Supporting sentence: information hub and free community for expats in Paraguay.")}</p>
    <div class="cta-row">{cta()}<span class="microcopy">{ph("Microcopy, e.g. what happens after you click.")}</span></div>
  </div>
  <picture class="hero-media">
    <source type="image/webp" srcset="assets/images/hero/B-red-earth-lapacho-road-1280x360.webp">
    <img src="assets/images/hero/B-red-earth-lapacho-road-1280x360.jpg" alt="Illustrative scene of a red-earth road under pink lapacho trees in Paraguay" width="1280" height="360" decoding="async">
  </picture>
</div></section>
<section class="section band-yerba"><div class="wrap">
  <span class="eyebrow">Inside the free community</span>
  <h2>What you get in the community</h2>
  <p class="lead">{ph("Intro line for the community sections.")}</p>
  <div class="grid grid--4" style="margin-top:28px">{secs}</div>
  <div class="cta-row">{cta("btn--on-dark")}</div>
</div></section>
<section class="section section--tight"><div class="wrap">
  <!-- Fix P1: email signup moved out of the hero, below the community band -->
  {email_box()}
</div></section>
<section class="section"><div class="wrap">
  <span class="eyebrow">Free guides</span><h2>Start with the guides</h2>
  <p class="lead">{ph("Intro line for the guides.")}</p>
  <div class="grid grid--3" style="margin-top:28px">{cards}
    <article class="card" style="justify-content:center;align-items:flex-start"><h3>All guides</h3><p>Filter by Planning to move, Just arrived, or Money and business.</p><a class="btn btn--ghost" href="guides.html">Browse the guides</a></article>
  </div>
</div></section>
<section class="section--tight section"><div class="wrap">
  <span class="eyebrow">Follow ParaguayNext</span><h2>Find us on social</h2>
  {social()}
  <p class="note">Social URLs not supplied yet — all links are placeholders (href="#").</p>
</div></section>'''
page("index.html","Home",home)

# 2 Guides hub
hub = intro("Guides","Guides for moving to and living in Paraguay", ph("Intro line for the guides hub."))
hub += f'''<section class="section"><div class="wrap" style="position:relative">
  <input class="filter-state" type="radio" name="f" id="f-all" checked>
  <input class="filter-state" type="radio" name="f" id="f-plan">
  <input class="filter-state" type="radio" name="f" id="f-arr">
  <input class="filter-state" type="radio" name="f" id="f-money">
  <div class="filters" role="group" aria-label="Filter guides">
    <label for="f-all">All</label><label for="f-plan">Planning to move</label><label for="f-arr">Just arrived</label><label for="f-money">Money and business</label>
  </div>
  <div class="grid grid--3">{cards}</div>
  <p class="note">Filters are CSS-only (no JavaScript). Guide-to-filter mapping is a wireframe assumption — see README.</p>
</div></section>'''
page("guides.html","Guides",hub,"guides.html")

# 3 Guide template
toc = ["Section 1","Section 2","Section 3","Section 4","Sources"]
art_secs = "".join(f'''<section id="s{i}"><h2>{ph(f"Section {i} heading")}</h2>
  <p>{ph("Body copy. Every key fact needs a cited, dated source.")}</p>
  <div class="ph-lines"><span style="width:96%"></span><span style="width:88%"></span><span style="width:92%"></span><span style="width:60%"></span></div>
</section>''' for i in range(1,5))
guide = f'''<section class="section"><div class="wrap">
  <p class="crumbs"><a href="guides.html">Guides</a> / {ph("Guide title")}</p>
  <div class="tags" style="margin-bottom:12px"><span class="tag">{ph("Filter tag","TAG")}</span></div>
  <h1>{ph("Guide title")}</h1>
  <div class="meta"><span><b>Last checked:</b> YYYY-MM-DD</span><span>{ph("Author / reviewer","TBD")}</span></div>
  <p class="lead">{ph("Intro: who this guide is for and what it covers.")}</p>
  <div class="cta-row">{cta()}</div>
  <div class="disclaimer-box" role="note"><strong>Please read</strong>{DISCLAIMER}
    <div class="note" style="margin-bottom:0">Template rule: this box appears on tax, residency and investment guides (e.g. "Tax and residency basics"). Remove it on other guides.</div></div>
  <div class="guide-layout" style="margin-top:36px">
    <aside class="toc"><b>On this page</b><ol>{"".join(f'<li><a href="#{"s"+str(i+1) if t!="Sources" else "sources"}">{t}</a></li>' for i,t in enumerate(toc))}</ol></aside>
    <div class="article">
      {art_secs}
      <section id="sources"><h2>Sources</h2>
        <p class="microcopy">Official sources first, then our guides, then community posts.</p>
        <ol class="sources">
          <li>{ph("Official source name — URL — accessed YYYY-MM-DD","SOURCE")}</li>
          <li>{ph("Official source name — URL — accessed YYYY-MM-DD","SOURCE")}</li>
          <li>{ph("Related ParaguayNext guide or community post","SOURCE")}</li>
        </ol></section>
      <section class="band-yerba" style="border-radius:var(--radius);padding:28px">
        <h3>{ph("Guide-end CTA headline")}</h3>
        <p>{ph("One line linking this guide to the matching Skool section.")}</p>
        {cta("btn--on-dark")}
      </section>
      {email_box()}
    </div>
  </div>
</div></section>'''
page("guide-template.html","Guide template",guide,"guides.html")

# 4 Community
csecs = "".join(f'<article class="card"><img class="icon" src="{SYMBOL}" alt=""><h3>{s}</h3><p>{ph("What members find in this section.")}</p></article>' for s in SECTIONS)
comm = intro("Community","The free ParaguayNext community on Skool", ph("Intro: what the community is and who it is for."))
comm += f'''<section class="section"><div class="wrap">
  <h2>Sections in the community</h2>
  <div class="grid grid--4" style="margin-top:24px">{csecs}</div>
</div></section>
<section class="section band-yerba"><div class="wrap grid grid--2" style="align-items:center">
  <div><h2>How joining works</h2>
    <ol><li>{ph("Step 1")}</li><li>{ph("Step 2")}</li><li>{ph("Step 3")}</li></ol>
    <p>{ph("Community rules / tone line.")}</p>
    {cta("btn--on-dark")}</div>
  <div class="ph-img" style="min-height:260px">[IMAGE] Screenshot of the Skool group (Roger to supply)</div>
</div></section>'''
page("community.html","Community",comm,"community.html")

# 5 Events
ev = intro("Events and meetups","Events and meetups", ph("Placeholder until the first real event exists."))
evcard = f'''<article class="card"><span class="tag" style="align-self:flex-start">{ph("Date","TBD")}</span>
  <h3>{ph("Event name","TBD")}</h3><p>{ph("City / venue","TBD")}</p><p>{ph("Short description","TBD")}</p>
  <a class="more" href="{SKOOL}" rel="noopener">Details in the community →</a></article>'''
ev += f'''<section class="section"><div class="wrap">
  <div class="card" style="text-align:center;padding:40px;margin-bottom:28px"><h2>No events yet</h2>
    <p>{ph("Message: events and meetups are announced in the community first.")}</p><div>{cta()}</div></div>
  <h3>Event card layout (for later)</h3>
  <div class="grid grid--3" style="margin-top:16px">{evcard*3}</div>
  <p class="note">Card layout only. No real events, dates or venues are listed.</p>
</div></section>'''
page("events.html","Events and meetups",ev,"events.html")

# 6 About
ab = intro("About","About ParaguayNext", "ParaguayNext is an information hub and community, not an immigration agency.")
ab += f'''<section class="section"><div class="wrap grid grid--2" style="align-items:start">
  <div><h2>Who runs it</h2>
    <p>{ph("Who runs ParaguayNext and why (Roger to supply).")}</p>
    <p>{ph("Background / connection to Paraguay (Roger to supply).")}</p>
    <h2 style="margin-top:28px">What we do and don't do</h2>
    <p>{ph("What ParaguayNext offers: guides, community, events.")}</p>
    <div class="disclaimer-box" role="note"><strong>Not an immigration agency</strong>{DISCLAIMER}</div>
  </div>
  <div class="ph-img" style="min-height:360px">[IMAGE] Photo of the person(s) running ParaguayNext (Roger to supply)</div>
</div></section>'''
page("about.html","About",ab,"about.html")

# 7 Sponsors
sp = intro("Sponsors","Partner with ParaguayNext", ph("Placeholder: sponsors come later."))
sp += f'''<section class="section"><div class="wrap">
  <div class="grid grid--3">{"".join(f'<article class="card"><h3>{ph(f"Partnership option {i}","TBD")}</h3><p>{ph("Description","TBD")}</p></article>' for i in (1,2,3))}</div>
  <div class="card" style="margin-top:28px"><h3>Get in touch</h3>
    <p>{ph("Contact method for sponsors (not chosen yet)","TBD")}</p>
    <p class="note">PLACEHOLDER — no contact form. No sponsor names, audience figures or prices are shown until Roger supplies them.</p></div>
</div></section>'''
page("sponsors.html","Sponsors",sp)

# 8 Legal
lg = intro("Legal","Privacy, terms and disclaimer", ph("Short intro line."), show_cta=False)
lg = lg.replace('</p></div>\n</div></section>', '</p><div class="cta-row">'+cta()+'</div></div>\n</div></section>',1)
lg += f'''<section class="section legal"><div class="wrap">
  <nav class="subnav" aria-label="Legal sections"><a class="btn btn--ghost btn--sm" href="#privacy">Privacy</a><a class="btn btn--ghost btn--sm" href="#terms">Terms</a><a class="btn btn--ghost btn--sm" href="#disclaimer">Disclaimer</a></nav>
  <section id="privacy"><h2>Privacy policy</h2><p>{ph("Privacy policy text — to be written and reviewed before the email signup goes live (depends on the email provider).","LEGAL")}</p>
    <p class="microcopy">Last updated: YYYY-MM-DD</p></section>
  <section id="terms"><h2>Terms of use</h2><p>{ph("Terms of use text — to be written and reviewed.","LEGAL")}</p>
    <p class="microcopy">Last updated: YYYY-MM-DD</p></section>
  <section id="disclaimer"><h2>Disclaimer</h2>
    <div class="disclaimer-box" role="note"><strong>Disclaimer</strong>{DISCLAIMER}</div>
    <p>{ph("Any longer disclaimer text — to be written and reviewed.","LEGAL")}</p></section>
</div></section>'''
page("legal.html","Legal",lg)
print("built")
