from lib import *
import os

POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"


def devices():
    lap = "assets/shots/laptop.webp"
    ph = "assets/shots/phone.webp"
    have = os.path.exists(os.path.join(ROOT, lap)) and os.path.exists(os.path.join(ROOT, ph))
    if not have:
        return ""
    return (f'<div class="devices"><div class="laptop"><div class="screen"><img src="{lap}" alt="The account map from this site shown on a laptop" width="1440" height="900"></div><div class="base"></div></div>'
            f'<div class="phone"><img src="{ph}" alt="The requirement ring from this site shown on a phone" width="390" height="845"></div></div>')


def postings_vis():
    pts = [("Jul", "This role", 0), ("Aug", "Energy", 1), ("Sep", "Retail, life sciences", 2), ("Oct", "Enterprise", 3)]
    o = ['<svg viewBox="0 0 520 110" aria-hidden="true">', '<line x1="30" x2="490" y1="40" y2="40" stroke="var(--line)" stroke-width="2"/>',
         '<line class="draw" style="--len:460" x1="30" x2="490" y1="40" y2="40" stroke="var(--accent)" stroke-width="3"/>']
    for m, lab, i in pts:
        x = 30 + i * 153
        o.append(f'<circle class="pop" style="transition-delay:{.3+i*.25}s" cx="{x}" cy="40" r="11" fill="var(--accent)"/>')
        o.append(f'<text x="{x}" y="16" text-anchor="middle" font-size="14" font-weight="600" class="svg-ink">{m}</text>')
        o.append(f'<text x="{x}" y="74" text-anchor="{"start" if i==0 else "end" if i==3 else "middle"}" font-size="12.5" class="svg-muted">{lab}</text>')
    o.append("</svg>")
    return "".join(o)


def smu_vis():
    d = [("Americas 1", 34.4, "-2.7%", "c0"), ("Americas 2", 25.6, "-4.7%", "c1"), ("Europe", 27.4, "+5.1%", "c6"), ("APMEA", 12.6, "+13.3%", "c6")]
    o = ['<svg viewBox="0 0 520 96" aria-hidden="true">']
    x = 0
    for lab, v, g, c in d:
        w = 520 * v / 100
        op = 1 if c != "c6" else .35
        o.append(f'<rect class="grow" x="{x:.1f}" y="10" width="{w-3:.1f}" height="34" rx="3" fill="var(--{c})" opacity="{op}"/>')
        o.append(f'<text x="{x+4:.1f}" y="66" font-size="13" font-weight="600" class="svg-ink">{lab}</text>')
        col = "var(--bad)" if g.startswith("-") else "var(--ok)"
        o.append(f'<text x="{x+4:.1f}" y="86" font-size="12.5" fill="{col}">{g} YoY</text>')
        x += w
    o.append("</svg>")
    return "".join(o)


def waffle():
    o = ['<svg viewBox="0 0 300 140" aria-hidden="true">']
    for k in range(100):
        r, c = divmod(k, 20)
        on = k < 6
        avg = 6 <= k < 9
        fill = "var(--accent)" if on else "none"
        stroke = "var(--accent)" if avg else "var(--line)"
        o.append(f'<rect class="{"pop" if on else ""}" style="transition-delay:{k*.08:.2f}s" x="{c*15}" y="{r*15}" width="12" height="12" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="{1.6 if avg else 1}"/>')
    o.append('<text x="0" y="98" font-size="12.5" class="svg-muted"><tspan fill="var(--accent)" font-weight="600">6 Wipro</tspan> against a market average of 9 in every 100 DX staff</text>')
    o.append("</svg>")
    return "".join(o)


def deadline_vis():
    ev = [("Feb", "AEM 6.5 on-premises support ends", 1), ("Apr", "ADA Title II web rule", 3), ("May", "HHS Section 504 web rule", 4), ("Dec", "Sitecore 10.4 support ends", 11)]
    o = ['<svg viewBox="0 0 620 130" aria-hidden="true"><line x1="10" x2="610" y1="34" y2="34" stroke="var(--line)" stroke-width="2"/>']
    for m in range(12):
        x = 10 + m * 600 / 11
        o.append(f'<line x1="{x:.0f}" x2="{x:.0f}" y1="29" y2="39" stroke="var(--line)"/>')
    for i, (m, lab, mo) in enumerate(ev):
        x = 10 + mo * 600 / 11
        o.append(f'<circle class="pop" style="transition-delay:{.2+i*.2}s" cx="{x:.0f}" cy="34" r="10" fill="var(--c2)"/>')
        o.append(f'<text x="{x:.0f}" y="14" text-anchor="middle" font-size="13" font-weight="600" class="svg-ink">{m}</text>')
        y = 64 + [0, 1, 2, 0][i] * 22
        anc = "start" if i in (0, 1, 2) else "end"
        x = x - 8 if anc == "start" else x
        o.append(f'<text x="{x:.0f}" y="{y}" text-anchor="{anc}" font-size="12.5" class="svg-muted">{lab}</text>')
    o.append("</svg>")
    return "".join(o)


def argument():
    steps = [("The gap", "Gartner rates Wipro a Niche Player in DX. The reason is a thin creative, onshore front end.", "c2"),
             ("The fit", "Architect and computational designer. Sixteen years selling design-led consulting to Fortune 500 executives.", "c0"),
             ("The result", "Design-led entry deals that grow into multi-year runs at Wipro's scale.", "c3")]
    o = ['<svg viewBox="0 0 1100 300" role="img" aria-label="The gap, the fit, the result"><defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--muted)"/></marker></defs>']
    for i, (h, p, c) in enumerate(steps):
        cx = 170 + i * 380
        o.append(f'<circle class="pop" style="transition-delay:{i*.3}s" cx="{cx}" cy="110" r="92" fill="none" stroke="var(--{c})" stroke-width="3"/>')
        o.append(f'<circle class="pop" style="transition-delay:{i*.3+.1}s" cx="{cx}" cy="110" r="78" fill="var(--{c})" opacity=".14"/>')
        o.append(f'<text x="{cx}" y="118" text-anchor="middle" font-size="27" font-weight="700" class="svg-ink">{h}</text>')
        if i < 2:
            o.append(f'<line class="draw" style="--len:160;transition-delay:{.4+i*.3}s" x1="{cx+104}" x2="{cx+276}" y1="110" y2="110" stroke="var(--muted)" stroke-width="2" marker-end="url(#ah)"/>')
    o.append("</svg>")
    caps = "".join(f'<div class="rv d{i+1}"><p class="lead" style="margin:0 auto;max-width:18em;font-size:17px">{E(p)}</p></div>' for i, (h, p, c) in enumerate(steps))
    return "".join(o) + f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:8px">{caps}</div>'


PAGES = [
    ("role.html", "grid", "Role Anatomy", "The posting decoded, and the person it describes."),
    ("operating-model.html", "people", "Operating Matrix", "Where DX sits, and who it depends on."),
    ("market.html", "chart", "Market and Competitors", "Analyst ratings, budget shifts and battlecards."),
    ("triggers.html", "calendar", "Buying Triggers", "Twenty-five dated reasons to buy, 2025 to 2028."),
    ("accounts.html", "target", "Account Map", "Twenty-four accounts with a trigger and a first move."),
    ("pursuit.html", "ladder", "Pursuit Model", "Score a deal. Build a ladder to $20m."),
    ("portfolio.html", "bolt", "Portfolio Maths", "From a $25m target to meetings per month."),
    ("plan.html", "door", "First 180 Days", "Map, open, shape. With targets."),
    ("fit.html", "shield", "Fit and Evidence", "Every requirement, rated candidly."),
]


QA = [
    ("Why this role", "4", "DX seller roles posted in four months", "Wipro is building a sector bench of DX sellers across both Americas units while Americas revenue shrinks. The role is a growth bet, judged on pipeline within two quarters.", "role.html", "Role Anatomy"),
    ("Why me", "16", "years selling design-led consulting to executives", "Architect and computational designer. Built a new service line inside a matrix of studios. Won multi-year portfolio work in life sciences. Partial on DX platform selling, with a plan to close it.", "fit.html", "Fit and Evidence"),
    ("Why now", "DAYS", "days until AEM 6.5 on-premises support ends", "Platform support deadlines and US accessibility rules converge in 2027 on Wipro's focus industries. Each one is a dated reason to buy.", "triggers.html", "Buying Triggers"),
    ("What first", "25", "named accounts in a written plan by day 30", "Map the client partners, agree joint accounts, scan fifty estates against the trigger calendar, then open conversations with three points of view.", "plan.html", "First 180 Days"),
]


def qa_block():
    btn = "".join(f'<button type="button" data-q="{i}" aria-pressed="{str(i==0).lower()}">{E(q)}</button>' for i, (q, *_ ) in enumerate(QA))
    panes = "".join(
        f'<div class="qa" data-q="{i}"{"" if i==0 else " hidden"}><div class="num" style="font-size:clamp(80px,12vw,160px);margin-top:36px">{('<span data-days="2027-02-28">128</span>' if n == "DAYS" else E(n))}</div>'
        f'<h3 class="h-l" style="margin-top:6px">{E(l)}</h3><p class="lead" style="margin:16px auto 0">{E(t)}</p><p style="margin-top:22px"><a class="link-arrow" href="{h}">{E(hl)}</a></p></div>'
        for i, (q, n, l, t, h, hl) in enumerate(QA))
    js = """<script>(function(){var bs=document.querySelectorAll('.seg-tabs [data-q]'),ps=document.querySelectorAll('.qa');bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});ps.forEach(function(p){p.hidden=p.dataset.q!==b.dataset.q})})})})();</script>"""
    return f'<div class="rv"><div class="seg-tabs" role="group" aria-label="Questions">{btn}</div>{panes}</div>{js}'


def build():
    cta = '<a class="pill fill" href="plan.html">See the plan</a><a class="pill line" href="fit.html">See the fit</a>'
    body = hero("Wipro · Director, Digital Experience", "Digital Experience Director",
                "How the role works, where the deals are, and how I would build a $25m book.", devices(), cta)

    body += sec(head_block("Questions", "Four Questions", "Pick one.") + qa_block(), "", center=True)

    nums = (
        tile(f'<p class="t-k">Hiring</p>{num(4)}<h3>US DX seller roles in four months</h3><div class="vis">{postings_vis()}</div><span class="go">Role Anatomy</span>', 6, href="role.html")
        + tile(f'<p class="t-k">Revenue</p>{num(60, suf="%")}<h3>of Wipro revenue is in the Americas, and both units are shrinking</h3><div class="vis">{smu_vis()}</div><span class="go">Operating Matrix</span>', 6, href="operating-model.html")
        + tile(f'<p class="t-k">Analysts</p>{num(6, suf="%")}<h3>of Wipro DX staff are creative</h3><div class="vis">{waffle()}</div><span class="go">Market and Competitors</span>', 5, href="market.html")
        + tile(f'<p class="t-k">Deadlines</p>{num(2027)}<h3>Platform and accessibility deadlines converge</h3><div class="vis">{deadline_vis()}</div><span class="go">Buying Triggers</span>', 7, href="triggers.html")
    )
    body += sec(head_block("Context", "Four Numbers", "What frames the role in October 2026.") + f'<div class="bento">{nums}</div>', "grey")

    body += sec(head_block("Argument", "Gap, Fit, Result", "Why a design-led seller, and why now.") + f'<div class="art rv">{argument()}</div>', "dark", center=True)

    ideas = [
        ("door", "Client partners first", "Every deal starts by giving the account owner a reason to open the door."),
        ("calendar", "Sell the deadline", "A dated event turns a capability pitch into a decision."),
        ("ladder", "Land with design, expand to run", "A diagnostic under $1m opens it. The run phase makes it $20m."),
    ]
    it = "".join(tile(f'{icon(i)}<h3 style="margin-top:22px">{E(h)}</h3><p>{E(p)}</p>', 4) for i, h, p in ideas)
    body += sec(head_block("Approach", "Three Ideas", "The plan rests on these.") + f'<div class="bento">{it}</div>')

    cards = "".join(tile(f'{icon(i)}<h3 style="margin-top:22px">{E(t)}</h3><p>{E(d)}</p><span class="go">Open</span>', 4, href=h) for h, i, t, d in PAGES)
    body += sec(head_block("Study", "Nine Pages", "Plus a CV ordered for this role.")
                + f'<div class="bento">{cards}</div><p class="fine">Prepared by Arpan Bakshi, 23 October 2026, from public sources cited on each page. The <a href="{POST}">posting</a> is Wipro req 190063.</p>', "grey")
    page("overview.html", body, "A study of the Wipro Director, Digital Experience role by Arpan Bakshi.")
