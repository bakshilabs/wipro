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
    pts = [("Accenture Song", 9.2, 8.6, "l"), ("Deloitte Digital", 8.3, 7.9, "l"), ("Publicis Sapient", 5.4, 8.8, "r"), ("Capgemini and frog", 6.6, 7.2, "l"),
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
        o.append(f'<circle cx="{X(x):.0f}" cy="{Y(y):.0f}" r="6" fill="var(--c6)"/><text x="{tx:.0f}" y="{Y(y)+4:.0f}" text-anchor="{anc}" font-size="12" class="svg-ink">{n}</text>')
    wx, wy, tx, ty = X(8.2), Y(2.6), X(8.2), Y(6.6)
    o.append(f'<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>')
    o.append(f'<line x1="{wx:.0f}" y1="{wy-10:.0f}" x2="{tx:.0f}" y2="{ty+12:.0f}" stroke="var(--accent)" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#ar)"/>')
    o.append(f'<circle cx="{wx:.0f}" cy="{wy:.0f}" r="9" fill="var(--accent)"/><text x="{wx+14:.0f}" y="{wy+5:.0f}" font-size="13" font-weight="600" class="svg-accent">Wipro today</text>')
    o.append(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="none" stroke="var(--accent)" stroke-width="2.5"/><text x="{tx+14:.0f}" y="{ty-4:.0f}" font-size="13" font-weight="600" class="svg-accent">With Designit</text><text x="{tx+14:.0f}" y="{ty+12:.0f}" font-size="13" font-weight="600" class="svg-accent">in front</text>')
    o.append("</svg>")
    return f'<figure class="fig">{"".join(o)}<figcaption>My qualitative placement, informed by the Gartner 2025 descriptions of creative share and delivery mix. It is a judgement for discussion, not a measured score.</figcaption></figure>'


def build():
    stats = f"""<div class="stats">
<div class="stat"><b>$90bn</b><span>DX services revenue of the 17 providers in Gartner's 2025 DX Services MQ, for 2024, growing 6%</span><small><a href="{MQ}">Gartner MQ via Spotlight AR</a></small></div>
<div class="stat"><b>$21bn to $23bn</b><span>Adobe services market in 2024, forecast to grow 17% to 19% a year to 2027</span><small><a href="{EVA}">Everest Group, Oct 2025</a></small></div>
<div class="stat"><b>12%</b><span>Average share of DX services revenue that is outcome-based across MQ providers</span><small><a href="{MQ}">Gartner MQ via Spotlight AR</a></small></div>
<div class="stat"><b>40%</b><span>Share of agentic AI projects Gartner expects to be cancelled by the end of 2027</span><small><a href="{AGENT40}">Gartner, 25 Jun 2025</a></small></div>
</div>"""

    shifts = """<div class="grid3">
<div class="panel"><p class="k">From agencies to operations</p><p>CMOs are moving money from agencies and martech licences to their own labour and to AI. Services firms that run content operations, platforms and AI agents gain from that shift. Agency-of-record creative work does not.</p></div>
<div class="panel"><p class="k">From projects to run contracts</p><p>Over a third of DX staff across the MQ providers work on ongoing services. Buyers want reusable accelerators, run commitments and KPIs written into the contract. That is how $20m deals get built.</p></div>
<div class="panel"><p class="k">From hours to outcomes</p><p>AI is pushing build prices down. Analysts estimate 2% to 5% a year of deflation, and ISG reports Americas managed services contract value down 12% in Q2 2026. The seller who prices on outcomes keeps margin when hours fall.</p></div>
</div>""" + src([("ISG Index Q2 2026 via MarketBeat, 10 Jul 2026", ISGQ)])

    comp = table(["Competitor", "Strength", "Weakness", "How Wipro wins against it"], [[E(a), E(b), E(c), E(d)] for a, b, c, d in COMP], caption="Competitor comparison")
    battle = "".join(
        f'<div class="panel"><p class="k">Objection</p><h3>{E(a)}</h3><p>{E(b)}</p><p><b>Response.</b> {E(c)}</p></div>' for a, b, c in BATTLE)

    body = (
        phead("Market", "Market and Competitors",
              "Digital experience services is a market of about $90bn among the largest providers, growing at about 6% a year. Budgets are moving from agencies and licences towards operations and AI. This page sets out the size and direction of the market, where analysts place Wipro and how I would sell against each type of competitor.")
        + block("Size", "Market size and direction", stats)
        + block("Budgets", "Where marketing budgets are moving", budget_fig() + shifts)
        + block("Analysts", "Analyst ratings in digital experience", heat_tbl() + src([("Gartner MQ text via Spotlight AR", MQ), ("ISG Salesforce Ecosystem US, 27 Apr 2026", ISGS)]),
                "Wipro is rated a Leader for Salesforce services by Everest, and ISG rated it a Leader in all three US Salesforce quadrants in April 2026. In Adobe services and the Gartner DX MQ it trails. Most of the Gartner placements come from one secondary reproduction of the report, so they need checking against the Gartner document.")
        + block("Positioning", "Where Wipro can win", position_fig(),
                "Wipro has the scale for multi-year run work and a design company in Designit. The commercial question for this role is how often Designit leads the front of a deal so that Wipro is bought as an experience partner.")
        + block("Competitors", "Selling against each competitor type", comp)
        + block("Objections", "Wipro's weak points and how I would answer them", f'<div class="grid2">{battle}</div>',
                "A buyer's procurement team will read the same analyst reports. A seller who raises the weak points first, and answers them with a staffing plan, keeps control of the conversation.")
    )
    page("market.html", body, "DX services market size, budget shifts, analyst ratings and competitive positioning for Wipro.")
