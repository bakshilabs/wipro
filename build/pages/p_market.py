from lib import *

MQ = "https://research.oz.spotlightar.com/reports/magic-quadrant-digital-experience-services-2025/leaders"
MQG = "https://www.gartner.com/en/documents/7122730"
EVA = "https://www.tcs.com/content/dam/global-tcs/en/pdfs/who-we-are/news/analyst-reports/tcs-named-leader-adobe-services-everest-group.pdf"
EVS = "https://www.wipro.com/analyst-speak/"
FRC = "https://research.oz.spotlightar.com/reports/forrester-wave-commerce-services-2026/leaders"
CMO26 = "https://gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities"
CMO25 = "https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-2025-cmo-spend-survey-reveals-marketing-budgets-have-flatlined-at-seven-percent-of-overall-company-revenue"
MD = "https://www.marketingdive.com/news/marketings-data-breakdown-h1-by-the-numbers/819958/"
ISGS = "https://ir.isg-one.com/news-market-information/press-releases/news-details/2026/AI-Integration-Accelerates-U-S--Salesforce-Adoption/default.aspx"
AGENT40 = "https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027"
ISGQ = "https://www.marketbeat.com/instant-alerts/information-services-group-sees-ai-cloud-demand-fuel-record-tech-spending-2026-07-10/"

# 4 Leader, 3 Challenger or Visionary, 2 Major Contender, 1 Niche Player, 0 not evaluated or not found
RATINGS = [
    ("Accenture Song", 4, 4, 4, 4),
    ("Deloitte Digital", 4, 4, 4, None),
    ("Publicis Sapient", 4, 4, None, 4),
    ("Capgemini and frog", 4, 4, 4, None),
    ("IBM iX", 3, 4, 4, None),
    ("Infosys and WONGDOODY", 3, 4, 4, None),
    ("HCLTech", 3, 2, 2, None),
    ("EPAM", 3, 2, None, None),
    ("Valtech", 3, None, None, None),
    ("TCS Interactive", None, 4, 2, None),
    ("Cognizant Moment", 1, 2, 4, None),
    ("Wipro", 1, 2, 4, 0),
]
LAB = {4: "Leader", 3: "Challenger or Visionary", 2: "Major Contender", 1: "Niche Player", 0: "Not included"}

COMP = [
    ("Accenture Song", "About $20bn of revenue in FY25 and about 121,000 DX practitioners. Gartner, Forrester and Everest all rate it a Leader.",
     "Premium rates, a junior-heavy bench (Gartner says 68% of its DX staff have under five years' experience) and a 2025 restructure into Reinvention Services.",
     "Offer a fixed-price design phase and a managed run at a lower blended rate, with named senior people in the client's time zone."),
    ("Deloitte Digital", "Highest ability to execute in the 2025 Gartner MQ. Advise, implement and operate model. Deep Salesforce bench.",
     "Gartner notes little interest in point projects and outcome commitments that clients cannot always see.",
     "Win the scoped work Deloitte will not prioritise, then grow it. Put outcome measures in the contract from day one."),
    ("Publicis Sapient and the agency groups", "Integrated media, creative and technology, with data assets such as Publicis ID. Often the incumbent agency.",
     "Gartner notes fewer resources in implementation and run. CMOs are cutting agency budgets: 39% planned to in 2025.",
     "Partner with the incumbent agency on creative and take the platform, content operations and AI run work they staff thinly."),
    ("Infosys, TCS and HCLTech", "The same offshore economics as Wipro, larger Adobe benches (Everest Leaders for Infosys and TCS) and strong North American client bases.",
     "Similar creative gaps (TCS 4% creative staff per Gartner) and the same pricing pressure.",
     "Compete on Salesforce, Pega and ServiceNow strength, Designit's design studios and AI platforms, and on a sharper industry point of view."),
    ("EPAM, Globant and Valtech", "Engineering-led or design-led firms with nearshore delivery and newer commercial models such as Globant's AI Pods subscription.",
     "Smaller scale for $20m-plus run contracts. EPAM has 5% outcome-based revenue against a 12% market average.",
     "Use Wipro's scale for global run, managed services and multi-tower deals they cannot staff."),
]

BATTLE = [
    ("Wipro is a Niche Player in the Gartner DX MQ", "Gartner rates Wipro's execution on scale, investment and repeat business, and places it outside the leaders because of a small creative share and APAC-weighted delivery. That describes a capability gap at the front of the work, and Designit's studios exist to fill it.", "Lead with a Designit-led diagnostic and an onshore experience lead. Show the run economics only after the client trusts the design thinking."),
    ("About 80% of Wipro's DX staff are in APAC", "That ratio is the reason Wipro can offer a lower total cost of ownership for multi-year run work. Clients worry about it when the onshore team is thin in the early, ambiguous phases.", "Staff the first phase onshore and nearshore. Move to the offshore model in build and run, with the client's agreement on the transition plan."),
    ("Only 6% of Wipro's DX staff are creative", "Wipro should not compete for agency-of-record creative work. CMOs are moving budget from agencies and martech towards labour and AI, which suits a platform, content operations and AI partner.", "Position Wipro beside the creative agency, running the platforms, content supply chain and AI agents."),
    ("Large-deal bookings fell to $674m in Q2 FY27", "Clients may read this as weak momentum, and inside Wipro it raises the value of every large pursuit in the Americas.", "Bring large-deal shaping skill and a pipeline of trigger-based proactive proposals in the first two quarters."),
]


def heat_tbl():
    rows = []
    for n, g, ea, es, fc in RATINGS:
        cells = [f"<b>{E(n)}</b>" if n == "Wipro" else E(n)]
        for v in (g, ea, es, fc):
            cells.append(heat(0, "Not found") if v is None else heat(v, LAB[v]))
        rows.append(cells)
    return table(
        ["Provider", f'<a href="{MQG}">Gartner MQ, DX Services, Oct 2025</a>', f'<a href="{EVA}">Everest, Adobe Services, 2025</a>', f'<a href="{EVS}">Everest, Salesforce Services, 2024</a>', f'<a href="{FRC}">Forrester Wave, Commerce Services, Q1 2026</a>'],
        rows, caption="Analyst ratings in digital experience categories")


def budget_fig():
    data = [("Paid media", 30.6, 31.4), ("Labour", 21.9, 24.5), ("Agencies", 20.7, 19.2), ("Martech", 22.4, 19.4)]
    o = ['<svg viewBox="0 0 640 250" role="img" aria-labelledby="bt bd"><title id="bt">Share of marketing budget, 2025 against 2026</title><desc id="bd">Paid media 30.6 to 31.4 percent, labour 21.9 to 24.5, agencies 20.7 to 19.2, martech 22.4 to 19.4.</desc>']
    mx = 35
    for i, (lab, a, b) in enumerate(data):
        y = 20 + i * 56
        o.append(f'<text x="0" y="{y+22}" font-size="13" class="svg-ink">{lab}</text>')
        wa, wb = 440 * a / mx, 440 * b / mx
        o.append(f'<rect x="120" y="{y}" width="{wa:.0f}" height="16" fill="var(--c6)" rx="2"/><text x="{124+wa:.0f}" y="{y+13}" font-size="12" class="svg-muted">{a}% in 2025</text>')
        o.append(f'<rect x="120" y="{y+20}" width="{wb:.0f}" height="16" fill="var(--accent)" rx="2"/><text x="{124+wb:.0f}" y="{y+33}" font-size="12" class="svg-ink">{b}% in 2026</text>')
    o.append("</svg>")
    return f'<figure class="fig">{"".join(o)}<figcaption>Gartner CMO Spend Survey, 2025 and 2026 editions. Marketing budgets held at 7.7% and 7.8% of company revenue. AI took 15.3% of the 2026 budget.</figcaption></figure>' + src([("Gartner, 12 May 2025", CMO25), ("Gartner, 11 May 2026", CMO26), ("Marketing Dive, 7 Jul 2026", MD)])


def position_fig():
    # qualitative judgement: x = scale for multi-year run, y = design and creative depth, both 0..10
    # name, x, y, label side
    pts = [("Accenture Song", 9.2, 8.6, "l"), ("Deloitte Digital", 8.3, 7.9, "l"), ("Publicis Sapient", 5.4, 8.8, "l"), ("Capgemini and frog", 6.4, 7.3, "r"),
           ("IBM iX", 6.4, 5.0, "l"), ("Infosys", 7.4, 5.6, "l"), ("TCS", 9.0, 3.9, "r"), ("HCLTech", 7.0, 3.3, "l"), ("Cognizant", 7.6, 4.5, "l"),
           ("EPAM", 4.2, 3.0, "r"), ("Valtech", 3.0, 7.2, "r"), ("Globant", 3.6, 6.0, "r")]
    W, H, L, B = 640, 440, 60, 390
    X = lambda v: L + v / 10 * (W - L - 40)
    Y = lambda v: B - v / 10 * (B - 20)
    o = ['<svg viewBox="0 0 640 440" role="img" aria-labelledby="pt pd"><title id="pt">Competitive positions by design depth and run scale</title><desc id="pd">A qualitative map. Wipro today sits with high run scale and low design depth. With Designit leading the front of the deal it moves up towards the leaders.</desc>']
    o.append(f'<line x1="{L}" x2="{W-20}" y1="{B}" y2="{B}" stroke="var(--line)"/><line x1="{L}" x2="{L}" y1="20" y2="{B}" stroke="var(--line)"/>')
    o.append(f'<text x="{(L+W)/2}" y="{B+34}" text-anchor="middle" font-size="12.5" class="svg-muted">Scale for multi-year build and run</text>')
    o.append(f'<text x="18" y="{(B+20)/2}" text-anchor="middle" font-size="12.5" class="svg-muted" transform="rotate(-90 18 {(B+20)/2})">Design and creative depth</text>')
    for n, x, y, side in pts:
        tx, anc = (X(x) + 10, "start") if side == "r" else (X(x) - 10, "end")
        o.append(f'<g data-pick="{E(n)}" aria-label="{E(n)}"><circle cx="{X(x):.0f}" cy="{Y(y):.0f}" r="7" fill="var(--c6)" stroke="transparent" stroke-width="10"/><text x="{tx:.0f}" y="{Y(y)+4:.0f}" text-anchor="{anc}" font-size="15.5" class="svg-ink">{n}</text></g>')
    wx, wy, tx, ty = X(8.2), Y(2.6), X(8.2), Y(6.6)
    o.append(f'<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>')
    o.append(f'<line x1="{wx:.0f}" y1="{wy-10:.0f}" x2="{tx:.0f}" y2="{ty+12:.0f}" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#ar)"/>')
    o.append(f'<circle cx="{wx:.0f}" cy="{wy:.0f}" r="9" fill="var(--accent)"/><text x="{wx+14:.0f}" y="{wy+5:.0f}" font-size="16" font-weight="700" class="svg-accent">Wipro today</text>')
    o.append(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="none" stroke="var(--accent)" stroke-width="2.5"/><text x="{tx+14:.0f}" y="{ty-4:.0f}" font-size="16" font-weight="700" class="svg-accent">With Designit</text><text x="{tx+14:.0f}" y="{ty+12:.0f}" font-size="16" font-weight="700" class="svg-accent">in front</text>')
    o.append("</svg>")
    return f'<figure class="fig">{"".join(o)}<figcaption>My qualitative placement, informed by the Gartner 2025 descriptions of creative share and delivery mix. It is a judgement for discussion, not a measured score.</figcaption></figure>'


def analyst_svg():
    cols = ["Gartner DX Services 2025", "Everest Adobe 2025", "Everest Salesforce 2024", "Forrester Commerce Q1 2026"]
    W, top, rh = 1100, 90, 40
    H = top + rh * len(RATINGS) + 20
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="ant and"><title id="ant">Analyst ratings by provider</title><desc id="and">Larger, brighter dots are higher ratings. Wipro is a Leader for Salesforce services and trails in the Gartner DX MQ and Adobe services.</desc>']
    for j, c in enumerate(cols):
        x = 380 + j * 190
        o.append(f'<text x="{x}" y="40" text-anchor="middle" font-size="14" font-weight="600" class="svg-ink">{E(c.rsplit(" ",1)[0])}</text><text x="{x}" y="60" text-anchor="middle" font-size="13" class="svg-muted">{c.rsplit(" ",1)[1]}</text>')
    for i, (n, *v) in enumerate(RATINGS):
        y = top + i * rh
        me = n == "Wipro"
        if me:
            o.append(f'<rect x="0" y="{y-22}" width="{W}" height="{rh}" rx="4" fill="var(--accent)" opacity=".16"/>')
        o.append(f'<text x="16" y="{y+5}" font-size="16" font-weight="{700 if me else 500}" class="svg-ink">{E(n)}</text>')
        for j, r in enumerate(v):
            x = 380 + j * 190
            if r is None:
                o.append(f'<circle cx="{x}" cy="{y}" r="4" fill="var(--line)"/>')
                continue
            rad = [5, 7, 10, 12, 15][r]
            col = ["var(--line)", "var(--c2)", "var(--c6)", "var(--c1)", "var(--accent)"][r]
            o.append(f'<circle class="pop" style="transition-delay:{(i+j)*.03:.2f}s" cx="{x}" cy="{y}" r="{rad}" fill="{col}"><title>{E(n)}: {LAB[r]}</title></circle>')
    o.append("</svg>")
    leg = "".join(f'<span><i style="background:{c};border-radius:50%"></i>{l}</span>' for l, c in [("Leader", "var(--accent)"), ("Challenger or Visionary", "var(--c1)"), ("Major Contender", "var(--c6)"), ("Niche Player", "var(--c2)"), ("Not rated or not found", "var(--line)")])
    return "".join(o) + f'<div class="legend" style="justify-content:center">{leg}</div>'


def slope_svg():
    # name, 2025, 2026, colour, left label nudge, right label nudge
    data = [("Labour", 21.9, 24.5, "c3", 8, 0), ("Paid media", 30.6, 31.4, "c6", 0, 0), ("Agencies", 20.7, 19.2, "c2", 4, 14), ("Martech", 22.4, 19.4, "c4", -8, -12)]
    Y = lambda v: 320 - (v - 17) * 20
    o = ['<svg viewBox="0 0 900 360" role="img" aria-label="Share of marketing budget, 2025 to 2026: labour up, agencies and martech down">']
    o.append('<line x1="260" x2="260" y1="20" y2="330" stroke="var(--line)"/><line x1="640" x2="640" y1="20" y2="330" stroke="var(--line)"/>')
    o.append('<text x="260" y="352" text-anchor="middle" font-size="16" font-weight="700" class="svg-ink">2025</text><text x="640" y="352" text-anchor="middle" font-size="16" font-weight="700" class="svg-ink">2026</text>')
    for n, a, b, c, la, ra in data:
        o.append(f'<line class="draw" style="--len:400" x1="260" y1="{Y(a):.0f}" x2="640" y2="{Y(b):.0f}" stroke="var(--{c})" stroke-width="5" stroke-linecap="round"/>')
        o.append(f'<circle cx="260" cy="{Y(a):.0f}" r="8" fill="var(--{c})"/><circle cx="640" cy="{Y(b):.0f}" r="8" fill="var(--{c})"/>')
        o.append(f'<text x="240" y="{Y(a)+6+la:.0f}" text-anchor="end" font-size="16" class="svg-muted">{a}%</text>')
        o.append(f'<text x="662" y="{Y(b)+6+ra:.0f}" font-size="18" font-weight="700" fill="var(--{c})">{n} {b}%</text>')
    o.append("</svg>")
    return "".join(o)



def _pos(n, edge, win):
    return f'<p class="t-k">Competitor</p><h3>{E(n)}</h3><p><b>Their edge</b> {E(edge)}</p><p><b>How Wipro wins</b> {E(win)}</p>'


_C = {c[0]: c for c in COMP}
POSDATA = {
    "Accenture Song": _pos("Accenture Song", _C["Accenture Song"][1], _C["Accenture Song"][3]),
    "Deloitte Digital": _pos("Deloitte Digital", _C["Deloitte Digital"][1], _C["Deloitte Digital"][3]),
    "Publicis Sapient": _pos("Publicis Sapient", _C["Publicis Sapient and the agency groups"][1], _C["Publicis Sapient and the agency groups"][3]),
    "Capgemini and frog": _pos("Capgemini and frog", "A Gartner DX Leader with frog's design studios. Gartner notes only 8% of its DX resources are in North America.", "Compete on North American delivery depth and run economics."),
    "IBM iX": _pos("IBM iX", "Implementation, orchestration and a 20-year Adobe partnership. An Everest Adobe Leader.", "Bring design-led framing through Designit, where IBM's marketing bench is thin."),
    "Infosys": _pos("Infosys", _C["Infosys, TCS and HCLTech"][1], _C["Infosys, TCS and HCLTech"][3]),
    "TCS": _pos("TCS", _C["Infosys, TCS and HCLTech"][1], _C["Infosys, TCS and HCLTech"][3]),
    "HCLTech": _pos("HCLTech", "DX is 15% of revenue and growing 11%, with an experience-level-agreement run model.", "Lead with Salesforce, Pega and ServiceNow strength and Designit's front end."),
    "Cognizant": _pos("Cognizant", "Outcome-based fees tied to KPIs and a strong North American presence. Also a Gartner Niche Player.", "Match outcome pricing and win on Designit and AI platforms."),
    "EPAM": _pos("EPAM", _C["EPAM, Globant and Valtech"][1], _C["EPAM, Globant and Valtech"][3]),
    "Valtech": _pos("Valtech", "A pure-play experience firm with outcome pricing. A Gartner Visionary.", "Use Wipro's scale for global run and multi-tower deals Valtech cannot staff."),
    "Globant": _pos("Globant", "Design-led engineering with Latin American nearshore delivery and an AI Pods subscription.", "Win the $20m-plus run contracts that need global scale."),
}

def build():
    body = hero("Market and Competitors", "A $90bn Market",
                "Budgets are moving from agencies to operations and AI. Wipro has the scale. Designit is how it leads with design.",
                explorer(position_fig().replace('<figure class="fig">', "<figure>"), POSDATA, "Select a competitor to see how Wipro wins against it.", first="Accenture Song"))

    b = (tile(f'<p class="t-k">DX services, 17 largest providers</p>{num(90, pre="$", small="bn")}<p>2024 revenue, growing 6% a year.</p>', 3)
         + tile(f'<p class="t-k">Adobe services growth</p>{num(18, suf="%")}<p>A year to 2027, on a $21bn to $23bn base.</p>', 3)
         + tile(f'<p class="t-k">Outcome-based</p>{num(12, suf="%")}<p>Of DX revenue on average. Rising.</p>', 3)
         + tile(f'<p class="t-k">Agentic AI projects</p>{num(40, suf="%")}<p>Expected to be cancelled by 2027.</p>', 3))
    body += sec(head_block("Size", "Where the Money Is", "Four numbers that shape every pitch.") + f'<div class="bento">{b}</div>'
                + src([("Gartner MQ via Spotlight AR", MQ), ("Everest Group, Oct 2025", EVA), ("Gartner, 25 Jun 2025", AGENT40)]), "grey")

    body += sec(head_block("Budgets", "From Agencies to Operations", "Share of the marketing budget, Gartner CMO Spend Survey.") + f'<div class="art m rv">{slope_svg()}</div>'
                + src([("Gartner, 12 May 2025", CMO25), ("Gartner, 11 May 2026", CMO26), ("Marketing Dive, 7 Jul 2026", MD)]))

    body += sec(head_block("Analysts", "Where Wipro Stands", "A Leader in Salesforce services. Behind in Adobe and the Gartner DX MQ.") + f'<div class="art rv">{analyst_svg()}</div>'
                + more("Show the ratings table", heat_tbl() + src([("Gartner MQ text via Spotlight AR", MQ), ("ISG Salesforce Ecosystem US, 27 Apr 2026", ISGS)])), "dark", center=True)

    cards = "".join(
        f'<div class="tile"><h3 style="font-size:26px">{E(a)}</h3><p><b style="color:var(--ink)">Their edge</b> {E(b2)}</p><p style="margin-top:auto;padding-top:20px;font-size:17px;color:var(--ink)"><b style="color:var(--accent)">How Wipro wins</b> {E(d)}</p></div>'
        for a, b2, c, d in COMP)
    body += sec(head_block("Competitors", "Five Rivals, Five Answers", "Swipe for how I would sell against each.") + f'<div class="rail rv">{cards}</div>', "grey")

    obj = "".join(tile(f'<p class="t-k">They say</p><h3>“{E(a)}”</h3><p style="margin-top:auto;padding-top:20px;font-size:17px;color:var(--ink)"><b style="color:var(--accent)">I answer</b> {E(c)}</p>', 6) for a, b2, c in BATTLE)
    body += sec(head_block("Objections", "Weak Points, Answered", "Procurement reads the same analyst reports. Raise them first.") + f'<div class="bento">{obj}</div>')
    page("market.html", body, "DX services market size, budget shifts, analyst ratings and competitive positioning for Wipro.")
