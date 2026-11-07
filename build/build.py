#!/usr/bin/env python3
"""Generates the ParaguayNext preview pages. Run: python3 build/build.py

Signed-off reader copy for the home page and guides 1 and 2 is inlined here.
Editor notes and source annotations from the copy drafts are not rendered.
"""
import pathlib, html, re
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
PARTIAL = pathlib.Path(__file__).resolve().parent / "partials" / "cf-web-analytics.html"
# Switched off. The partial keeps a YOUR_TOKEN placeholder and is never written into pages.
ANALYTICS_ENABLED = False
SKOOL = "https://www.skool.com/paraguaynext-6232"
CTA = "Join the free community"
DISCLAIMER = ("This is general information, not legal, tax, or financial advice. Rules change; "
              "check with a licensed professional in Paraguay before you act. "
              "ParaguayNext is not an immigration agency.")
AFFILIATE = ("Some links are affiliate links; we may earn a commission at no extra cost to you. "
             "We only list services we would point a friend to.")
FOOTER_LINE = "ParaguayNext is a free information hub and community for expats in Paraguay."

def esc(text):
    return html.escape(text, quote=True)

def ph(text, tag="COPY"):
    return f'<span class="ph"><span class="ph-tag">[{tag}]</span>{esc(text)}</span>'

def cta(cls="btn--primary", extra=""):
    return f'<a class="btn {cls} {extra}" href="{SKOOL}" rel="noopener">{CTA}</a>'

def ext(url, label=None):
    label = url if label is None else label
    return f'<a href="{esc(url)}" rel="noopener">{esc(label)}</a>'

NAV = [("guides.html","Guides"),("community.html","Community"),("events.html","Events"),("about.html","About")]
SOCIAL = [
    ("X", "https://x.com/paraguaynext"),
    ("Instagram", "https://www.instagram.com/paraguaynext/"),
    ("TikTok", "https://www.tiktok.com/@paraguaynext"),
    ("Snapchat", "https://www.snapchat.com/add/paraguaynext"),
    ("Telegram channel", "https://t.me/paraguaynext"),
    ("Telegram group", "https://t.me/paraguaynextgroup"),
    ("WhatsApp group", "https://chat.whatsapp.com/KS2tcUxDKSa1N2Bx0l06Yc"),
]

GUIDES = [
    {"title": "Moving to Paraguay: the step-by-step plan", "tags": ["plan"],
     "img": "guide-01-moving-to-paraguay-web-800x412",
     "alt": "Illustrated cover for Moving to Paraguay: packing crates and a map of Paraguay",
     "summary": "A plain overview of what to plan before you relocate, from documents to timeline to common mistakes.",
     "href": "guides/moving-to-paraguay.html", "label": "Read the guide"},
    {"title": "Your first 30 days in Paraguay", "tags": ["arr"],
     "img": "guide-02-first-30-days-web-800x412",
     "alt": "Illustrated cover for Your first 30 days: calendar and everyday Paraguay errands",
     "summary": "An arrival checklist covering paperwork, phone, banking basics, housing, transport, health, and meeting people.",
     "href": "guides/first-30-days.html", "label": "Read the guide"},
    {"title": "Cost of living in Paraguay", "tags": ["plan", "arr"],
     "img": "guide-03-cost-of-living-web-800x412",
     "alt": "Illustrated cover for Cost of living: market produce and everyday expenses",
     "summary": "What to plan for when you budget for life in Paraguay. Sourced figures are coming later.",
     "href": None, "label": "Coming soon"},
    {"title": "Tax and residency basics (general information)", "tags": ["plan", "money"],
     "img": "guide-04-tax-and-residency-basics-web-800x412",
     "alt": "Illustrated cover for Tax and residency basics: documents and a residence stamp",
     "summary": "High-level concepts and questions to ask a professional. Not legal or tax advice.",
     "href": "guide-template.html", "label": "Read the guide"},
    {"title": "Making money and starting a business in Paraguay", "tags": ["money"],
     "img": "guide-05-making-money-web-800x412",
     "alt": "Illustrated cover for Making money: laptop workspace and local business motifs",
     "summary": "Remote work, business ideas, and setup overview at a high level. Not financial advice.",
     "href": "guide-template.html", "label": "Read the guide"},
]
TAGNAME = {"plan": "Planning to move", "arr": "Just arrived", "money": "Money and business"}
# Community page still lists the eight Skool sections. Home omits Meetups.
SECTIONS = ["Move planning", "New arrivals", "Meetups", "Events", "Tech", "Business ideas", "Making money", "Tax and investments"]
SYMBOL = "assets/brand/symbol/lapacho-symbol-lapacho.svg"

def social():
    items = "".join(f'<a href="{esc(url)}" rel="noopener">{esc(label)}</a>' for label, url in SOCIAL)
    return f'<div class="social">{items}</div>'

def email_box(title="Get the free guides by email"):
    eid = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f'''<div class="email-box" aria-label="Email signup placeholder">
  <label for="email-ph-{eid}">{esc(title)}</label>
  <div class="email-row">
    <input id="email-ph-{eid}" type="email" placeholder="you@example.com" disabled aria-disabled="true">
    <button class="btn btn--ghost btn--sm" type="button" disabled>Send me the guides</button>
  </div>
  <p class="note">PLACEHOLDER. MailerLite is the planned provider. The form embed is not connected. No form is submitted and no data is collected.</p>
  <p class="microcopy">We will only email the guides and community updates. No spam. Unsubscribe anytime. Privacy policy will be published before this form goes live.</p>
</div>'''

def guide_card(g):
    tags = "".join(f'<span class="tag">{TAGNAME[x]}</span>' for x in g["tags"])
    cls = " ".join(f"t-{x}" for x in g["tags"])
    if g["href"]:
        more = f'<a class="more" href="{esc(g["href"])}">{esc(g["label"])}</a>'
    else:
        more = f'<span class="more is-soon">{esc(g["label"])}</span>'
    return f'''<article class="card {cls}">
  <picture class="card-media">
    <source type="image/webp" srcset="assets/images/guide-cards/{esc(g["img"])}.webp">
    <img src="assets/images/guide-cards/{esc(g["img"])}.jpg" alt="{esc(g["alt"])}" width="800" height="412" loading="lazy" decoding="async">
  </picture>
  <div class="tags">{tags}</div>
  <h3>{esc(g["title"])}</h3>
  <p>{esc(g["summary"])}</p>
  {more}
</article>'''

def cta_block(pre, headline=None, support=None):
    h = esc(headline) if headline else ph("CTA headline, e.g. a short invitation to join.")
    p = esc(support) if support else ph("One supporting line about what members get.")
    return f'''<section class="cta-block section" aria-label="Join the community">
  <div class="wrap"><div class="cta-inner">
    <img src="{pre}{SYMBOL}" alt="" width="72" height="72">
    <div><h2>{h}</h2>
      <p>{p}</p></div>
    <div>{cta()}</div>
  </div></div>
</section>'''

def analytics_html():
    if not ANALYTICS_ENABLED:
        return ""
    return PARTIAL.read_text(encoding="utf-8")

def page(fname, title, body, current=None, depth=0, desc=None, exact_title=False, cta_h=None, cta_p=None, bottom_cta=True):
    pre = "../" * depth
    def link(path):
        return pre + path
    nav = "".join(
        f'<a href="{link(h)}"{ " aria-current=page" if h==current else ""}>{l}</a>'
        for h, l in NAV)
    mnav = nav + f'<a class="btn btn--primary" href="{SKOOL}" rel="noopener">{CTA}</a>'
    title_html = esc(title) if exact_title else f"{esc(title)} — ParaguayNext [WIREFRAME DRAFT]"
    desc_html = esc(desc) if desc else "[COPY] Meta description placeholder."
    block = cta_block(pre, cta_h, cta_p) if bottom_cta else ""
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title_html}</title>
<meta name="description" content="{desc_html}">
<link rel="icon" href="{pre}assets/brand/favicon/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{pre}assets/brand/favicon/favicon.ico" sizes="16x16 32x32">
<link rel="apple-touch-icon" href="{pre}assets/brand/favicon/apple-touch-icon-180.png">
<link rel="stylesheet" href="{pre}assets/css/wireframe.css">
</head>
<body>
<div class="wf-banner"><b>WIREFRAME DRAFT</b> · not published · placeholder copy is marked [COPY], [IMAGE], [LINK]</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{link("index.html")}"><img src="{pre}assets/brand/lockup/lockup-serif-horizontal-light.svg" alt="ParaguayNext" width="168" height="44"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <span class="header-cta">{cta("btn--primary","btn--sm")}</span>
    <details class="menu"><summary>Menu</summary><nav aria-label="Main (mobile)">{mnav}</nav></details>
  </div>
</header>
<main>
{body}
{block}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <img src="{pre}assets/brand/lockup/lockup-serif-horizontal-dark.svg" alt="ParaguayNext" width="152" height="40">
        <p>{FOOTER_LINE}</p>
        {cta()}
      </div>
      <div><h4>Site</h4><ul>
        <li><a href="{link("guides.html")}">Guides</a></li><li><a href="{link("community.html")}">Community</a></li>
        <li><a href="{link("events.html")}">Events</a></li><li><a href="{link("about.html")}">About</a></li>
        <li><a href="{link("sponsors.html")}">Sponsors</a></li></ul>
        <h4 style="margin-top:20px">Legal</h4><ul>
        <li><a href="{link("legal.html")}#privacy">Privacy</a></li><li><a href="{link("legal.html")}#terms">Terms</a></li><li><a href="{link("legal.html")}#disclaimer">Disclaimer</a></li></ul>
      </div>
      <div><h4>Follow</h4>{social()}</div>
    </div>
    <div class="footer-disclaimer">
      <p>{DISCLAIMER}</p>
      <p class="affiliate-disclosure">{AFFILIATE}</p>
    </div>
  </div>
</footer>
{analytics_html()}</body>
</html>
'''
    dest = OUT / fname
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf-8")

def intro(eyebrow, h1, lead, show_cta=True):
    c = f'<div class="cta-row">{cta()}</div>' if show_cta else ""
    lead_html = lead if lead.startswith("<") else esc(lead)
    return f'''<section class="hero"><div class="wrap" style="grid-template-columns:1fr">
  <div class="hero-card"><span class="eyebrow">{esc(eyebrow)}</span><h1>{esc(h1)}</h1><p class="lead">{lead_html}</p>{c}</div>
</div></section>'''

def home_sections():
    items = [
        ("Move planning", "Checklists, timelines, and peer tips before you book flights or ship boxes."),
        ("New arrivals", "Practical help for your first weeks: paperwork, phone, housing, and getting oriented."),
        ("Events", 'Community events and calls when they are scheduled. Check the <a href="events.html">Events page</a> for the current list.'),
        ("Tech", "Tools, remote work setup, and tech questions from members living in Paraguay."),
        ("Business ideas", "Share and discuss business ideas that fit the local market. Not financial advice."),
        ("Making money", "Remote income, freelancing, and local earning paths members are exploring. Not financial advice."),
        ("Tax and investments", "High-level questions and pointers. Always confirm with a licensed professional in Paraguay. Not tax or investment advice."),
    ]
    cards = []
    for name, text in items:
        body = text if name == "Events" else esc(text)
        cards.append(
            f'<article class="card"><img class="icon" src="assets/brand/symbol/lapacho-symbol-on-green.svg" alt=""><h3>{esc(name)}</h3><p>{body}</p></article>'
        )
    return "".join(cards)

def disclaimer_box():
    return f'<div class="disclaimer-box" role="note"><strong>Please read</strong>{DISCLAIMER}</div>'

def end_band(headline, support):
    return f'''<section class="band-yerba" id="next" style="border-radius:var(--radius);padding:28px">
        <h2>{esc(headline)}</h2>
        <p>{esc(support)}</p>
        {cta("btn--on-dark")}
      </section>'''

def meta_row(tag):
    return f'''<div class="meta"><span><b>Last checked:</b> 2026-11-06</span><span>Author / reviewer: <span class="ph"><span class="ph-tag">[TBD]</span>Roger sign-off required</span></span></div>
  <div class="tags" style="margin-bottom:12px"><span class="tag">{esc(tag)}</span></div>'''

def guide_moving():
    g2 = "first-30-days.html"
    return f'''<section class="section"><div class="wrap">
  <p class="crumbs"><a href="../guides.html">Guides</a> / Moving to Paraguay: the step-by-step plan</p>
  <h1>Moving to Paraguay: the step-by-step plan</h1>
  {meta_row("Planning to move")}
  <p class="lead">Who this is for: people who are seriously planning a move to Paraguay and want a plain overview before they dig into paperwork with professionals.</p>
  <p>What it covers: why people look at Paraguay, how to plan at a high level, money and logistics thinking, common mistakes, and where to get peer support.</p>
  <p>What it does <strong>not</strong> cover: residency categories, document lists, fees, timelines, apostille rules, cédula or RUC steps, proof-of-funds rules, insurance rules for immigration, TIN acceptance, or tax outcomes. ParaguayNext is an information hub and free community, not an immigration agency.</p>
  <div class="cta-row">{cta()}</div>
  {disclaimer_box()}
  <div class="guide-layout" style="margin-top:36px">
    <aside class="toc"><b>On this page</b><ol>
      <li><a href="#why">Why people look at Paraguay</a></li>
      <li><a href="#residency">Residency and paperwork (coming later)</a></li>
      <li><a href="#planning">Planning your move in practice</a></li>
      <li><a href="#timeline">Timeline shape, budget thinking, and common mistakes</a></li>
      <li><a href="#sources">Sources</a></li>
      <li><a href="#next">Next steps in the community</a></li>
    </ol></aside>
    <div class="article">
      <section id="why"><h2>Why people look at Paraguay</h2>
        <p>People considering Paraguay often care about cost of living, climate, location in South America, and a slower pace of life. This guide does not rank countries or publish "best of" lists. Your own priorities matter more than any ranking.</p>
        <p>Your reasons matter more than anyone else's list. Write down what you need for work, family, health, and money before you lock in flights.</p>
        <p>Use this guide as a planning map. Ask questions in the free ParaguayNext community when you want peer context.</p>
        <div class="cta-row">{cta()}</div>
      </section>
      <section id="residency"><h2>Residency and paperwork (coming later)</h2>
        <p>Details on residency categories, document lists, fees, timelines, apostille or legalization rules, cédula, RUC, minimum financial means, and immigration-related insurance are coming later. For now, check with a licensed professional in Paraguay.</p>
        <p>ParaguayNext does <strong>not</strong> file applications, sponsor visas, or promise approvals.</p>
        <h3>How to use this section safely</h3>
        <ul>
          <li>Treat social media summaries about "easy residency" as marketing until a licensed professional confirms what applies to you.</li>
          <li>Do not book irreversible moves (selling a home, quitting a job, shipping everything) until your own professional has confirmed your plan.</li>
          <li>Keep a simple folder (digital and paper) for contracts, tickets, and receipts you already have.</li>
        </ul>
      </section>
      <section id="planning"><h2>Planning your move in practice</h2>
        <h3>Before you travel</h3>
        <ul>
          <li>Decide what "good enough" looks like for work, family, health, and money.</li>
          <li>Talk to a licensed professional in Paraguay about legal and tax steps that apply to you. Details on this are coming later. For now, check with a licensed professional in Paraguay.</li>
          <li>Plan flexible lodging for the first weeks. Avoid long leases until you know the neighborhood.</li>
          <li>Set up money access that does not depend on a single card (see <a href="{g2}#banking">Guide 2</a> banking basics for product facts that are already sourced).</li>
          <li>Keep backup copies of identity documents you already travel with. Path-specific document lists are not published in this draft.</li>
        </ul>
        <h3>After you arrive</h3>
        <ul>
          <li>Follow <a href="{g2}">Guide 2</a> for first-month logistics (phone, housing habits, banking product basics, meeting people).</li>
          <li>Details on local ID, tax registration, and immigration appointments are coming later. For now, check with a licensed professional in Paraguay.</li>
        </ul>
      </section>
      <section id="timeline"><h2>Timeline shape, budget thinking, and common mistakes</h2>
        <h3>Suggested planning phases (structure only)</h3>
        <ol>
          <li><strong>Research:</strong> Read peer guides, talk to a licensed professional, join the free community, and decide if Paraguay fits your life.</li>
          <li><strong>Personal paperwork plan:</strong> Build your own list with a professional. Official category lists and fees are not restated here.</li>
          <li><strong>Money setup:</strong> Open or keep a reliable international account for ATM cash and USD storage if you qualify (<a href="{g2}">Guide 2</a>). Keep a plan for a local Paraguayan bank after arrival.</li>
          <li><strong>Travel and lodging:</strong> Book flexible lodging for the first weeks.</li>
          <li><strong>After arrival:</strong> Phone, banking, housing, and meeting people (<a href="{g2}">Guide 2</a>). Legal ID and tax steps: check with a licensed professional in Paraguay.</li>
        </ol>
        <p>These phases are a personal planning shape, not a government timeline.</p>
        <h3>Budget thinking (no invented numbers)</h3>
        <p>Plan for:</p>
        <ul>
          <li>Flights and excess baggage or shipping</li>
          <li>Temporary lodging</li>
          <li>Local transport and deposits</li>
          <li>Professional fees (lawyer, translator, accountant) if you use them</li>
          <li>A cash buffer for delays</li>
        </ul>
        <p>Details on official immigration fees and sample monthly living budgets are coming later. For now, check with a licensed professional in Paraguay for fee questions.</p>
        <h3>Common mistakes to avoid</h3>
        <ul>
          <li>Treating social media summaries as official rules</li>
          <li>Arriving with only one payment card and no backup</li>
          <li>Signing a long housing contract before you understand the area</li>
          <li>Expecting ParaguayNext or any free community to replace a licensed lawyer or accountant</li>
        </ul>
      </section>
      <section id="sources"><h2>Sources</h2>
        <ol class="sources">
          <li>Related ParaguayNext guide: <a href="{g2}">Your first 30 days in Paraguay</a> (Guide 2)</li>
          <li>Free community: {ext(SKOOL)}</li>
        </ol>
      </section>
      {end_band("Plan your move with other expats", "Ask practical move questions in the Move planning section of the free Skool community.")}
      {email_box()}
    </div>
  </div>
</div></section>'''

def guide_first_30():
    g1 = "moving-to-paraguay.html"
    conatel = "https://www.conatel.gov.py/wp-content/uploads/2026/03/RNST_STMC_05-MAR_2026.pdf"
    mspbs = "https://www.mspbs.gov.py/hospitales-generales.html"
    airalo = "https://www.airalo.com/paraguay-esim"
    holafly = "https://esim.holafly.com/esim-paraguay/"
    saily = "https://saily.com/esim-paraguay/"
    nomad = "https://www.nomadesim.com/paraguay-eSIM"
    bolt = "https://bolt.eu/en/cities/asuncion/"
    decreto = "https://mopc.gov.py/uplmoo9eib8eefou3ooze4y/2024/03/DECRETO-N°710-2023.pdf"
    subsidio = "https://mopc.gov.py/viceministerios/viceministerio-de-transporte/subsidio-transparente/"
    itau = "https://itau.com.py/"
    bnf = "https://bnf.gov.py/"
    schwab_acct = "https://international.schwab.com/us-investing-brokerage-account"
    schwab_price = "https://international.schwab.com/pricing"
    schwab_open = "https://international.schwab.com/open-account-intro"
    schwab_faq = "https://www.schwab.com/checking/faqs"
    schwab_debit = "https://www.schwab.com/checking/debit-card"
    schwab_node = "https://www.schwab.com/node/30716"
    schwab_pdf = "https://disclosures.schwab.com/SchwabDashboard/62667/REG30608.pdf"
    meru = "https://getmeru.com/"
    meru_fees = "https://getmeru.com/fees/"
    meru_terms = "https://getmeru.com/terms-and-conditions/"
    meru_ach = "https://getmeru.com/help/es/articles/14488320-para-que-sirve-la-cuenta-bancaria-en-estados-unidos-que-ofrece-meru"
    meru_min_open = "https://getmeru.com/help/es/articles/14486446-hay-un-monto-minimo-para-empezar-a-usar-mi-cuenta-meru"
    meru_min_keep = "https://getmeru.com/help/es/articles/14486863-existe-un-saldo-minimo-para-que-mi-cuenta-meru-siga-activa"
    meru_countries = "https://getmeru.com/help/es/articles/14489334-que-paises-no-pueden-solicitar-la-cuenta-bancaria-de-ee-uu-en-meru"
    meru_cashback = "https://getmeru.com/help/es/articles/17558394-terminos-y-condiciones-cashback-depositos-paraguay"
    meru_mg = "https://getmeru.com/help/es/articles/8673980-como-funciona-moneygram"
    meru_open = "https://getmeru.com/help/es/articles/8207556-como-solicito-las-cuentas-bancarias"
    play_meru = "https://play.google.com/store/apps/details?id=com.getmeru.app&hl=en"
    play_uz = "https://play.google.com/store/apps/details?id=app.ungr.uzpay&hl=en"
    ops = "TELECEL (Tigo), NÚCLEO (Personal), AMX (Claro), and Nubicom"
    sources = [
        (conatel, "checked 2026-11-06"),
        (mspbs, "checked 2026-11-06"),
        (schwab_acct, "checked 2026-11-06"),
        (schwab_price, "checked 2026-11-06"),
        (schwab_open, "checked 2026-11-06"),
        (schwab_faq, "checked 2026-11-06"),
        (schwab_debit, "checked 2026-11-06"),
        (schwab_node, "checked 2026-11-06"),
        (schwab_pdf, "Jan 2026 guide; checked 2026-11-06"),
        (meru, "checked 2026-11-06"),
        (meru_fees, "agosto 2026 note; checked 2026-11-06"),
        (meru_terms, "checked 2026-11-06"),
        (meru_ach, "checked 2026-11-06"),
        (meru_min_open, "checked 2026-11-06"),
        (meru_min_keep, "checked 2026-11-06"),
        (meru_countries, "checked 2026-11-06"),
        (meru_cashback, "checked 2026-11-06"),
        (meru_mg, "checked 2026-11-06"),
        (meru_open, "checked 2026-11-06"),
        (itau, "checked 2026-11-06"),
        (bnf, "checked 2026-11-06"),
        (play_uz, "checked 2026-11-06"),
        (play_meru, "checked 2026-11-06"),
        (bolt, "checked 2026-11-06"),
        (decreto, "Decreto N° 710/2023; checked 2026-11-06"),
        (subsidio, "checked 2026-11-06"),
    ]
    src_html = "\n".join(f"<li>{ext(url)} ({esc(note)})</li>" for url, note in sources)
    return f'''<section class="section"><div class="wrap">
  <p class="crumbs"><a href="../guides.html">Guides</a> / Your first 30 days in Paraguay</p>
  <h1>Your first 30 days in Paraguay</h1>
  {meta_row("Just arrived")}
  <p class="lead">Who this is for: people who just arrived in Paraguay, or who are packing for arrival next month.</p>
  <p>What it covers: a first-month logistics checklist, phone basics, housing and transport habits, banking product basics, health pointers at a high level, and meeting people.</p>
  <p>What it does <strong>not</strong> cover: residency categories, immigration document lists, fees, timelines, apostille rules, cédula steps, RUC registration, proof-of-funds rules, insurance rules for immigration, TIN acceptance by banks, or cross-border tax advice. ParaguayNext is an information hub and free community, not an immigration agency.</p>
  <div class="cta-row">{cta()}</div>
  {disclaimer_box()}
  <div class="guide-layout" style="margin-top:36px">
    <aside class="toc"><b>On this page</b><ol>
      <li><a href="#checklist">Arrival checklist</a></li>
      <li><a href="#paperwork">Local ID and paperwork (coming later)</a></li>
      <li><a href="#logistics">Phone, internet, housing, transport, and health</a></li>
      <li><a href="#banking">Banking basics for new arrivals</a></li>
      <li><a href="#people">Meeting people</a></li>
      <li><a href="#sources">Sources</a></li>
      <li><a href="#next">Next steps in the community</a></li>
    </ol></aside>
    <div class="article">
      <section id="checklist"><h2>Arrival checklist</h2>
        <p>Use this as a starter logistics list. Legal paperwork steps are not listed here.</p>
        <h3>First 48 hours</h3>
        <ul>
          <li>Confirm temporary lodging and how you will pay (card and cash backup).</li>
          <li>Get a working local number or roaming plan so banks, hosts, and services can reach you. Licensed mobile operators named in CONATEL materials include {ops}. An international eSIM can cover you until then (see section 3).</li>
          <li>Keep digital and paper copies of the identity documents you already travel with.</li>
          <li>Note the address you will use for deliveries and bank letters.</li>
        </ul>
        <h3>First two weeks</h3>
        <ul>
          <li>Open or prepare a local bank relationship for guaraní bills when you qualify (see banking section).</li>
          <li>Learn a few everyday Spanish phrases for taxis, shops, and clinics.</li>
          <li>Introduce yourself in New arrivals inside the free ParaguayNext community.</li>
          <li>Details on immigration appointments, local ID, and tax registration are coming later. For now, check with a licensed professional in Paraguay.</li>
        </ul>
        <h3>First 30 days</h3>
        <ul>
          <li>Stabilize housing (short extension or a careful longer lease).</li>
          <li>Set up a layered money setup (international ATM card + local bank + backup card).</li>
          <li>Find a primary clinic or hospital route near where you stay. Paraguay's Ministry of Health publishes a list of public general hospitals. Emergency ambulance SEME is listed as <strong>141</strong> on that page.</li>
          <li>Meet people through the free ParaguayNext community.</li>
        </ul>
        <div class="cta-row">{cta()}</div>
      </section>
      <section id="paperwork"><h2>Local ID and paperwork (coming later)</h2>
        <p>Details on residency categories, immigration documents, fees, timelines, apostille rules, cédula, RUC, minimum financial means, immigration-related insurance, and what banks accept as a foreign TIN are coming later. For now, check with a licensed professional in Paraguay.</p>
        <h3>Safe framing until that content ships</h3>
        <ul>
          <li>Ask a licensed professional which appointments you need in which order.</li>
          <li>Keep a running folder of receipts and protocol numbers you receive.</li>
          <li>Do not treat ParaguayNext guides as a filing checklist.</li>
        </ul>
      </section>
      <section id="logistics"><h2>Phone, internet, housing, transport, and health</h2>
        <h3>Phone and internet</h3>
        <ul>
          <li>Buy a local SIM or eSIM when you arrive. Licensed mobile operators appearing in the CONATEL RNST STMC register (05 Mar 2026 PDF) include {ops}.</li>
          <li>Local prepaid prices change often, so this guide does not list them. Check the operator's own site or shop.</li>
          <li>Keep your foreign number active during the transition if banks use SMS codes.</li>
          <li>Home internet options vary by building and city. Install timing depends on the provider and the property. This guide does not publish a national install SLA.</li>
        </ul>
        <h4>Option: an international eSIM</h4>
        <p>If your phone supports eSIM, you can buy a travel eSIM in the provider's app before you fly, or when you land. It gives you data right away, before you get a local SIM. These providers list a Paraguay plan. Prices are examples as shown on 2026-11-06 and can change.</p>
        <ul>
          <li><strong>Airalo:</strong> example plan Unlimited data for 3 days, US$19.50. {ext(airalo)}</li>
          <li><strong>Holafly:</strong> example plan Unlimited data for 3 days, US$20.90. {ext(holafly)}</li>
          <li><strong>Saily:</strong> example plan 1 GB for 7 days, US$7.49. {ext(saily)}</li>
          <li><strong>Nomad:</strong> example plan 1 GB for 7 days, US$6. {ext(nomad)}</li>
        </ul>
        <p>Check the provider's page for current prices and coverage before you buy.</p>
        <p class="affiliate-disclosure">{AFFILIATE}</p>
        <h3>Where to live (areas overview)</h3>
        <p>Neighborhood fit depends on budget, noise, commute, and language. A practical approach is to stay short-term at first and walk candidate areas at different times of day. This guide does not publish rent ranges or "best neighborhood" lists.</p>
        <p>Tips:</p>
        <ul>
          <li>Prefer a short first lease when you can.</li>
          <li>Check water pressure, generator backup, and who pays utilities.</li>
          <li>Confirm how you will receive bank cards and letters.</li>
        </ul>
        <h3>Transport</h3>
        <ul>
          <li>In Asunción, Bolt lists ride service as available. {ext(bolt)} Taxis and buses are also common. This draft does not claim Uber availability (Uber Paraguay pages were unreachable on FactCheck day).</li>
          <li>For Área Metropolitana de Asunción passenger bus fares, Decreto N° 710/2023 Art. 18 sets convencional at <strong>Gs. 2.300</strong> and diferencial at <strong>Gs. 3.400</strong> per passenger. Confirm no newer decree before you rely on these figures. {ext(decreto)} {ext(subsidio)}</li>
          <li>If you will drive, learn the local road rules and get car insurance before you drive. Ask your insurer or a licensed professional in Paraguay what cover you need.</li>
        </ul>
        <h3>Health care</h3>
        <ul>
          <li>Locate a nearby clinic and pharmacy in your first week.</li>
          <li>For public general hospitals, see the MSPBS hospital list. {ext(mspbs)}</li>
          <li>Understand whether you will use private insurance, pay out of pocket, or another arrangement for day-to-day care. This guide does not list private hospital prices or rankings.</li>
          <li>Bring a medication list and enough supply for the transition if your doctor agrees.</li>
          <li>Details on whether any insurance is required for immigration or stay are coming later. For now, check with a licensed professional in Paraguay.</li>
        </ul>
      </section>
      <section id="banking"><h2>Banking basics for new arrivals</h2>
        <p>Goal for month one: access cash, receive USD income if you need it, pay local bills in guaraní, and avoid depending on a single card.</p>
        <p>This section covers <strong>product mechanics and published fees</strong> only. It is not tax advice. Details on cross-border tax reporting are coming later. For now, check with a licensed professional in Paraguay.</p>
        <h3>Layered setup (high level)</h3>
        <ol>
          <li><strong>International ATM and USD storage (one option many expats discuss):</strong> Charles Schwab International, if you qualify.</li>
          <li><strong>USD intake and cards (fintech option):</strong> Meru, if you qualify and accept fintech tradeoffs.</li>
          <li><strong>Local Paraguayan bank:</strong> for guaraní bills and local transfers. Sourced examples with live sites on FactCheck day: Itaú Paraguay and Banco Nacional de Fomento (BNF). {ext(itau)} {ext(bnf)} Visión Banco is <strong>not</strong> featured here while its official site remains unreachable.</li>
          <li><strong>Crypto bridge tools:</strong> treat as optional and high risk. <strong>UZPay stays quarantined:</strong> the official site returned HTTP 500 on HTTP and TLS failure on HTTPS on 2026-11-06. Do not soften that warning. Do not fund tools you cannot verify live.</li>
        </ol>
        <p>This is not a recommendation to open any specific account. Eligibility, fees, and product details change. Confirm on each provider's live site.</p>
        <h3>Charles Schwab International (sourced summary)</h3>
        <ul>
          <li>Schwab One International is marketed as a U.S. brokerage account for many residents outside the U.S. {ext(schwab_acct)}</li>
          <li>Online listed U.S. stocks and ETFs are marketed at US$0 commission. Bonds and many mutual funds are not always $0. Check current pricing. {ext(schwab_price)}</li>
          <li>A linked Schwab Bank High Yield Investor Checking account can include a Schwab Bank Visa Platinum Debit Card. {ext(schwab_node)} {ext(schwab_debit)}</li>
          <li>Schwab Bank refunds ATM fees for cash withdrawals with that debit card at the end of the same month. {ext(schwab_faq)}</li>
          <li>Schwab Bank does not assess its own foreign transaction fee on the debit card. Visa network rates still apply. {ext(schwab_faq)} {ext(schwab_pdf, "Schwab Bank Deposit Account Pricing Guide Jan 2026")}</li>
          <li>Always decline Dynamic Currency Conversion (DCC) at ATMs. DCC markups are not treated as ATM fees and are not rebated. {ext(schwab_faq)} {ext(schwab_debit)}</li>
          <li>Paraguay was listed among selectable residences on Schwab's international open-account flow as of 2026-11-06. Confirm before you apply. {ext(schwab_open)}</li>
          <li>Non-U.S. persons generally provide the tax forms and ID materials Schwab lists for international accounts. Details on which Paraguay tax IDs banks accept are coming later. For now, check with a licensed professional in Paraguay, and confirm with Schwab during onboarding. {ext(schwab_acct)}</li>
          <li>International brokerage marketing describes international wire funding with no Schwab transaction fee on that path. Schwab Bank deposit pricing (Jan 2026) states incoming wires are domestic only for bank deposit accounts. Know which rail you use. {ext(schwab_acct)} {ext(schwab_pdf)}</li>
          <li>Schwab is not a Paraguayan bill-pay rail.</li>
        </ul>
        <p>Do <strong>not</strong> use a Gs. 25,000-40,000 ATM operator fee range. No bank tariff or BCP primary for foreign-card operator fees in that band was found in FactCheck (2026-11-06). This guide publishes no ATM operator fee range.</p>
        <h3>Meru (sourced summary)</h3>
        <ul>
          <li>Meru markets a U.S. routing and account number for ACH and wire receipts, plus a European IBAN for SEPA. {ext(meru)}</li>
          <li>Cards: marketing fetched on check day showed Visa physical and virtual cards. Do not claim Mastercard. {ext(meru)} {ext(meru_fees)}</li>
          <li>Published personal fees list ACH deposit (Global / Mexico / Colombia) at US$2 and Global wire at US$15. Page note: last update August 2026. Recheck live fees before you budget. {ext(meru_fees)}</li>
          <li>ACH timing: Meru Help states credits often take 1 to 3 business days depending on transfer origin. {ext(meru_ach)}</li>
          <li>No mandatory minimum balance to open or keep the account active. {ext(meru_min_open)} {ext(meru_min_keep)}</li>
          <li>Meru Help lists U.S. bank-account product unavailability for residents of Venezuela, Nicaragua, Cuba, and El Salvador. Paraguay is not on that exclusion list. Confirm in-app for your case. {ext(meru_countries)}</li>
          <li>Meru also publishes Paraguay deposit cashback T&amp;Cs for users who reside and have their account registered in Paraguay. {ext(meru_cashback)}</li>
          <li>Meru markets platform payouts such as Upwork, Stripe, PayPal, and YouTube. {ext(meru)}</li>
          <li>Meru terms identify the company as R3MIT SOLUTIONS INC., registered as a Money Services Business (MSB) with FinCEN, with services via partners. It is not presenting itself as a bank charter. {ext(meru_terms)}</li>
          <li>Meru-to-Meru transfers: the Meru Play Store listing says you can send between Meru users with "no hidden fees." Prefer that wording. Do not call Meru-to-Meru "free" unless {ext(meru_fees)} later shows an explicit $0 line. {ext(play_meru, "Meru on Google Play")}</li>
          <li>MoneyGram cash-outs are marketed as globally available subject to local service availability. Paraguay is not named in the Help snippet FactCheck quoted. Confirm locally before you rely on it. {ext(meru_mg)}</li>
          <li>Opening fee: Meru Help mentions a US$2 opening cost in the bank-account request flow in some cases (refund language if opening fails after three attempts). The fees page says account opening is free. Both company pages were live on check day. This draft keeps <strong>both</strong> statements and does <strong>not</strong> pick a winner. Confirm in-app which applies to you. {ext(meru_open)} {ext(meru_fees)}</li>
        </ul>
        <h3>UZPay (quarantined)</h3>
        <ul>
          <li>Official site uzpay.io returned HTTP 500 on HTTP and TLS failure on HTTPS on 2026-11-06. Keep this tool quarantined until the site serves readable terms and fees again.</li>
          <li>RDAP showed domain registration still active (expiration 2027-01-19; last change 2026-08-12). A Google Play listing for app.ungr.uzpay (UNISOFT LIMITED) was still reachable. That does not mean the website works or that fees are verified. {ext(play_uz, "UZPay on Google Play")}</li>
          <li>Do not use UZPay as a primary money rail.</li>
        </ul>
        <h3>Practical month-one money habits</h3>
        <ul>
          <li>Keep at least two working cards from different providers.</li>
          <li>Decline DCC at ATMs. {ext(schwab_faq)}</li>
          <li>Use a local bank for utilities and guaraní transfers when you can.</li>
          <li>Do not keep all funds in one fintech app.</li>
        </ul>
      </section>
      <section id="people"><h2>Meeting people</h2>
        <p>Arrival is easier when you have humans to ask.</p>
        <ul>
          <li>Introduce yourself in the <strong>New arrivals</strong> section of the free ParaguayNext community.</li>
          <li>Check <strong><a href="../events.html">Events</a></strong> in the community for calls and events when they are posted.</li>
          <li>Language exchanges, coworking spaces, and hobby groups can help too. Availability varies by city. This guide does not publish a directory.</li>
        </ul>
        <p>Be kind, verify advice that affects money or legal status, and never send funds to someone who pressures you.</p>
        <div class="cta-row">{cta()}</div>
      </section>
      <section id="sources"><h2>Sources</h2>
        <ol class="sources">
          {src_html}
          <li>Related guide: <a href="{g1}">Moving to Paraguay: the step-by-step plan</a> (Guide 1)</li>
          <li>Free community: {ext(SKOOL)}</li>
        </ol>
      </section>
      {end_band("Get support for your first month", "Ask arrival and banking questions in New arrivals inside the free Skool community.")}
      {email_box()}
    </div>
  </div>
</div></section>'''

# 1 Home
cards = "".join(guide_card(g) for g in GUIDES)
home = f'''<section class="hero"><div class="wrap">
  <div class="hero-card">
    <span class="eyebrow">For expats moving to and living in Paraguay</span>
    <h1>Clear guides and a free community for your Paraguay move</h1>
    <p class="lead">ParaguayNext is an information hub and free Skool community for expats. We share practical guides and peer support. We are not an immigration agency, and we do not sell legal services.</p>
    <div class="cta-row">{cta()}<span class="microcopy">Free to join. Meet other expats, ask questions, and follow the guides at your own pace.</span></div>
  </div>
  <picture class="hero-media">
    <source type="image/webp" srcset="assets/images/hero/B-red-earth-lapacho-road-1280x360.webp">
    <img src="assets/images/hero/B-red-earth-lapacho-road-1280x360.jpg" alt="Illustrative scene of a red-earth road under pink lapacho trees in Paraguay" width="1280" height="360" decoding="async">
  </picture>
</div></section>
<section class="section band-yerba"><div class="wrap">
  <span class="eyebrow">Inside the free community</span>
  <h2>What you get in the community</h2>
  <p class="lead">Eight sections inside the free Skool group, so you can find the right conversation fast.</p>
  <div class="grid grid--4" style="margin-top:28px">{home_sections()}</div>
  <div class="cta-row">{cta("btn--on-dark")}</div>
</div></section>
<section class="section section--tight"><div class="wrap">
  {email_box()}
</div></section>
<section class="section"><div class="wrap">
  <span class="eyebrow">Free guides</span><h2>Start with the guides</h2>
  <p class="lead">Short, practical guides for planning your move, settling in, and handling money questions. Read free on the site. Dig deeper in the community.</p>
  <div class="grid grid--3" style="margin-top:28px">{cards}
    <article class="card" style="justify-content:center;align-items:flex-start"><h3>All guides</h3><p>Filter by Planning to move, Just arrived, or Money and business.</p><a class="btn btn--ghost" href="guides.html">Browse the guides</a></article>
  </div>
</div></section>
<section class="section--tight section"><div class="wrap">
  <span class="eyebrow">Follow ParaguayNext</span><h2>Find us on social</h2>
  {social()}
</div></section>'''
page("index.html",
     "ParaguayNext | Free guides and community for expats in Paraguay",
     home,
     desc="Free guides and a friendly Skool community for people moving to or living in Paraguay. General information only. Not an immigration agency.",
     exact_title=True,
     cta_h="Ready when you are",
     cta_p="Ask questions, follow the guides, and connect with other expats in Paraguay.")

# 2 Guides hub
hub = intro("Guides", "Guides for moving to and living in Paraguay", ph("Intro line for the guides hub."))
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
page("guides.html", "Guides", hub, "guides.html")

# 3 Guide pages from the signed-off copy, using the guide template layout
page("guides/moving-to-paraguay.html",
     "Moving to Paraguay: the step-by-step plan",
     guide_moving(),
     current="guides.html", depth=1, exact_title=True, bottom_cta=False,
     desc="People who are seriously planning a move to Paraguay and want a plain overview before they dig into paperwork with professionals.")
page("guides/first-30-days.html",
     "Your first 30 days in Paraguay",
     guide_first_30(),
     current="guides.html", depth=1, exact_title=True, bottom_cta=False,
     desc="People who just arrived in Paraguay, or who are packing for arrival next month.")

# Guide template stays a wireframe for guides that do not have signed-off bodies yet.
toc = ["Section 1", "Section 2", "Section 3", "Section 4", "Sources"]
art_secs = "".join(f'''<section id="s{i}"><h2>{ph(f"Section {i} heading")}</h2>
  <p>{ph("Body copy. Every key fact needs a cited, dated source.")}</p>
  <div class="ph-lines"><span style="width:96%"></span><span style="width:88%"></span><span style="width:92%"></span><span style="width:60%"></span></div>
</section>''' for i in range(1, 5))
guide = f'''<section class="section"><div class="wrap">
  <p class="crumbs"><a href="guides.html">Guides</a> / {ph("Guide title")}</p>
  <div class="tags" style="margin-bottom:12px"><span class="tag">{ph("Filter tag", "TAG")}</span></div>
  <h1>{ph("Guide title")}</h1>
  <div class="meta"><span><b>Last checked:</b> YYYY-MM-DD</span><span>{ph("Author / reviewer", "TBD")}</span></div>
  <p class="lead">{ph("Intro: who this guide is for and what it covers.")}</p>
  <div class="cta-row">{cta()}</div>
  <div class="disclaimer-box" role="note"><strong>Please read</strong>{DISCLAIMER}
    <div class="note" style="margin-bottom:0">Template rule: this box appears on tax, residency and investment guides (e.g. "Tax and residency basics"). Remove it on other guides.</div></div>
  <div class="guide-layout" style="margin-top:36px">
    <aside class="toc"><b>On this page</b><ol>{"".join(f'<li><a href="#{"s"+str(i+1) if t!="Sources" else "sources"}">{t}</a></li>' for i, t in enumerate(toc))}</ol></aside>
    <div class="article">
      {art_secs}
      <section id="sources"><h2>Sources</h2>
        <p class="microcopy">Official sources first, then our guides, then community posts.</p>
        <ol class="sources">
          <li>{ph("Official source name, URL, accessed YYYY-MM-DD", "SOURCE")}</li>
          <li>{ph("Official source name, URL, accessed YYYY-MM-DD", "SOURCE")}</li>
          <li>{ph("Related ParaguayNext guide or community post", "SOURCE")}</li>
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
page("guide-template.html", "Guide template", guide, "guides.html")

# 4 Community
csecs = "".join(f'<article class="card"><img class="icon" src="{SYMBOL}" alt=""><h3>{s}</h3><p>{ph("What members find in this section.")}</p></article>' for s in SECTIONS)
comm = intro("Community", "The free ParaguayNext community on Skool", ph("Intro: what the community is and who it is for."))
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
page("community.html", "Community", comm, "community.html")

# 5 Events
ev = intro("Events and meetups", "Events and meetups", ph("Placeholder until the first real event exists."))
evcard = f'''<article class="card"><span class="tag" style="align-self:flex-start">{ph("Date", "TBD")}</span>
  <h3>{ph("Event name", "TBD")}</h3><p>{ph("City / venue", "TBD")}</p><p>{ph("Short description", "TBD")}</p>
  <a class="more" href="{SKOOL}" rel="noopener">Details in the community →</a></article>'''
ev += f'''<section class="section"><div class="wrap">
  <div class="card" style="text-align:center;padding:40px;margin-bottom:28px"><h2>No events yet</h2>
    <p>{ph("Message: events and meetups are announced in the community first.")}</p><div>{cta()}</div></div>
  <h3>Event card layout (for later)</h3>
  <div class="grid grid--3" style="margin-top:16px">{evcard * 3}</div>
  <p class="note">Card layout only. No real events, dates or venues are listed.</p>
</div></section>'''
page("events.html", "Events and meetups", ev, "events.html")

# 6 About
ab = intro("About", "About ParaguayNext", "ParaguayNext is an information hub and community, not an immigration agency.")
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
page("about.html", "About", ab, "about.html")

# 7 Sponsors
sp = intro("Sponsors", "Partner with ParaguayNext", ph("Placeholder: sponsors come later."))
sp += f'''<section class="section"><div class="wrap">
  <div class="grid grid--3">{"".join(f'<article class="card"><h3>{ph(f"Partnership option {i}", "TBD")}</h3><p>{ph("Description", "TBD")}</p></article>' for i in (1, 2, 3))}</div>
  <div class="card" style="margin-top:28px"><h3>Get in touch</h3>
    <p>{ph("Contact method for sponsors (not chosen yet)", "TBD")}</p>
    <p class="note">PLACEHOLDER. No contact form. No sponsor names, audience figures or prices are shown until Roger supplies them.</p></div>
</div></section>'''
page("sponsors.html", "Sponsors", sp)

# 8 Legal
lg = intro("Legal", "Privacy, terms and disclaimer", ph("Short intro line."), show_cta=False)
lg = lg.replace("</p></div>\n</div></section>", "</p><div class=\"cta-row\">" + cta() + "</div></div>\n</div></section>", 1)
lg += f'''<section class="section legal"><div class="wrap">
  <nav class="subnav" aria-label="Legal sections"><a class="btn btn--ghost btn--sm" href="#privacy">Privacy</a><a class="btn btn--ghost btn--sm" href="#terms">Terms</a><a class="btn btn--ghost btn--sm" href="#disclaimer">Disclaimer</a></nav>
  <section id="privacy"><h2>Privacy policy</h2><p>{ph("Privacy policy text, to be written and reviewed before the email signup goes live (depends on the email provider).", "LEGAL")}</p>
    <p class="microcopy">Last updated: YYYY-MM-DD</p></section>
  <section id="terms"><h2>Terms of use</h2><p>{ph("Terms of use text, to be written and reviewed.", "LEGAL")}</p>
    <p class="microcopy">Last updated: YYYY-MM-DD</p></section>
  <section id="disclaimer"><h2>Disclaimer</h2>
    <div class="disclaimer-box" role="note"><strong>Disclaimer</strong>{DISCLAIMER}</div>
    <p>{ph("Any longer disclaimer text, to be written and reviewed.", "LEGAL")}</p></section>
</div></section>'''
page("legal.html", "Legal", lg)
print("built")
