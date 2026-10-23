from lib import *

Q2 = "https://www.wipro.com/newsroom/press-releases/2026/wipro-announces-results-for-the-quarter-ended-september-30-2026/"
Q2T = "https://www.wipro.com/content/dam/nexus/en/investor/quarterly-results/2026-2027/q2fy27/q2fy27-earnings-transcript.pdf"
Q1T = "https://www.wipro.com/content/dam/nexus/en/investor/quarterly-results/2026-2027/q1fy27/q1fy27-earnings-transcript.pdf"
Q4 = "https://www.wipro.com/content/dam/nexus/en/investor/quarterly-results/2025-2026/q4fy26/press-release-q4fy26.pdf"
AR = "https://www.wipro.com/content/dam/nexus/staticsites/annual-report-2025/pdf/Integrated-annual-report-2025-26.pdf"
SEBI = "https://www.wipro.com/content/dam/nexus/en/investor/corporate-governance/stock-exchange-filing/intimation-under-regulation-30-of-sebi-listing-obligations-and-disclosure-requirements-regulations-2015-change-in-senior-management-personnel-1-apr-2026.pdf"
GOYAL = "https://hrtoday.in/ashish-kumar-goyal-appointed-as-senior-vice-president-and-global-head-enterprise-applications-at-wipro/"
DESIGNIT = "https://www.designit.com/stories/news/keri-dawson-named-global-leader-at-designit"
TRIB = "https://assets.publishing.service.gov.uk/media/668beac24a94d44125d9ce95/Mr_P_Chandrashekarappa_v_Wipro_Ltd-3300028-2022_and_3311832-2022-FMH_Reserved_Judgment.pdf"
CLOUD = "https://careers.wipro.com/job/Cloud-&-Digital-Director-Automotive/183342-en_US/"

SMUS = [("Americas 1", "34.4%", "-2.7%", "Health, consumer, communications and media, technology"),
        ("Americas 2", "25.6%", "-4.7%", "Banking, capital markets and insurance, energy, manufacturing and resources"),
        ("Europe", "27.4%", "+5.1%", "UK and Ireland, Germany, Switzerland, Western Europe"),
        ("APMEA", "12.6%", "+13.3%", "Australia, Asia, Japan, India, Middle East, Africa")]
GBLS = [("Consulting", "Wipro Consulting and AI advisory"),
        ("Technology Services", "Cloud, apps, AI, cyber, infrastructure"),
        ("Engineering", "Product engineering, HARMAN DTS"),
        ("Business Process Services", "Operations and contact centres")]


def matrix_svg():
    W, H = 1000, 600
    x0, y0, cw, rh = 230, 96, 180, 92
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="mxt mxd"><title id="mxt">Wipro operating matrix</title>'
         '<desc id="mxd">Four strategic market units as columns own client relationships. Four global business lines as rows own offerings. '
         'The DX practice sits in Enterprise Applications inside Technology Services and sells across Americas 1 and Americas 2 through client partners.</desc>']
    # column heads
    for i, (n, share, g, _) in enumerate(SMUS):
        x = x0 + i * cw
        hl = i < 2
        o.append(f'<rect x="{x+4}" y="10" width="{cw-8}" height="76" rx="4" fill="{"var(--accent-soft)" if hl else "var(--surface)"}"/>')
        o.append(f'<text x="{x+cw/2}" y="38" text-anchor="middle" font-size="15" font-weight="600" class="svg-ink">{n}</text>')
        o.append(f'<text x="{x+cw/2}" y="58" text-anchor="middle" font-size="12" class="svg-muted">{share} of revenue</text>')
        col = "var(--bad)" if g.startswith("-") else "var(--ok)"
        o.append(f'<text x="{x+cw/2}" y="75" text-anchor="middle" font-size="12" fill="{col}">{g} YoY in Q2 FY27</text>')
    o.append(f'<text x="{x0-14}" y="52" text-anchor="end" font-size="12" class="svg-muted">Market units own</text><text x="{x0-14}" y="68" text-anchor="end" font-size="12" class="svg-muted">the client</text>')
    # rows
    for j, (n, d) in enumerate(GBLS):
        y = y0 + j * rh
        o.append(f'<rect x="0" y="{y+4}" width="{x0-12}" height="{rh-8}" rx="4" fill="var(--surface)"/>')
        o.append(f'<text x="14" y="{y+34}" font-size="14.5" font-weight="600" class="svg-ink">{n}</text>')
        o.append(f'<text x="14" y="{y+54}" font-size="11.5" class="svg-muted">{d}</text>')
        for i in range(4):
            x = x0 + i * cw
            o.append(f'<rect x="{x+4}" y="{y+4}" width="{cw-8}" height="{rh-8}" rx="3" fill="none" stroke="var(--line)"/>')
    # DX band inside Technology Services across A1 and A2
    y = y0 + rh
    o.append(f'<rect x="{x0+10}" y="{y+16}" width="{2*cw-20}" height="{rh-32}" rx="4" fill="var(--accent)"/>')
    o.append(f'<text x="{x0+cw}" y="{y+42}" text-anchor="middle" font-size="14" font-weight="600" fill="var(--on-accent)">Enterprise Applications: DX practice</text>')
    o.append(f'<text x="{x0+cw}" y="{y+60}" text-anchor="middle" font-size="12" fill="var(--on-accent)">This role sells here, through A1 and A2 client partners</text>')
    o.append(f'<text x="{x0+2*cw+cw/2}" y="{y+50}" text-anchor="middle" font-size="12" class="svg-muted">Salesforce, SAP, Oracle,</text><text x="{x0+2*cw+cw/2}" y="{y+66}" text-anchor="middle" font-size="12" class="svg-muted">Pega, ServiceNow practices</text>')
    # soft bands across A1 and A2 for the units DX pulls in
    for j in (0, 2, 3):
        yy0 = y0 + j * rh
        o.append(f'<rect x="{x0+10}" y="{yy0+16}" width="{2*cw-20}" height="{rh-32}" rx="4" fill="var(--accent-soft)"/>')
    yc = y0
    o.append(f'<text x="{x0+cw}" y="{yc+44}" text-anchor="middle" font-size="12" class="svg-muted">Consulting partners originate advisory work</text><text x="{x0+cw}" y="{yc+60}" text-anchor="middle" font-size="12" class="svg-muted">that converts to technology programmes</text>')
    yb = y0 + 3 * rh
    o.append(f'<text x="{x0+cw}" y="{yb+44}" text-anchor="middle" font-size="12" class="svg-muted">Contact centre and content operations</text><text x="{x0+cw}" y="{yb+60}" text-anchor="middle" font-size="12" class="svg-muted">for the run phase of DX deals</text>')
    ye = y0 + 2 * rh
    o.append(f'<text x="{x0+cw}" y="{ye+44}" text-anchor="middle" font-size="12" class="svg-muted">Connected products and device experiences</text><text x="{x0+cw}" y="{ye+60}" text-anchor="middle" font-size="12" class="svg-muted">for medical devices and automotive</text>')
    # side units
    yy = y0 + 4 * rh + 14
    side = [("Designit", "Strategy and design studios"), ("Capco", "Financial services consulting"), ("AI-Native unit", "Wipro Intelligence, from Apr 2026")]
    for k, (n, d) in enumerate(side):
        x = x0 + k * 250 - 230
        o.append(f'<rect x="{x+230}" y="{yy}" width="236" height="74" rx="4" fill="var(--surface)" stroke="var(--line)"/>')
        o.append(f'<text x="{x+246}" y="{yy+30}" font-size="14" font-weight="600" class="svg-ink">{n}</text><text x="{x+246}" y="{yy+50}" font-size="11.5" class="svg-muted">{d}</text>')
    o.append(f'<text x="14" y="{yy+30}" font-size="13" font-weight="600" class="svg-ink">Units the DX seller</text><text x="14" y="{yy+48}" font-size="13" font-weight="600" class="svg-ink">brings into pursuits</text>')
    o.append("</svg>")
    return "".join(o)


PEOPLE = [
    ("SMU client partner or global account executive", "Owns the account relationship and the account number. Decides who gets access to the client's executives.",
     "Growth in their account without risk to the relationship, and a DX story that helps their renewal.", "Bring a trigger and a sized idea for their account before asking for an introduction. Share credit on the booking."),
    ("DX practice leadership", "Owns DX capability, delivery and the global practice P&amp;L. Rajesh Damodaran is Global Head of the DX Practice.",
     "Bookings that delivery can staff at margin, and reference clients in focus industries.", "Bring delivery in at qualification, and pick pursuits that build references in retail, life sciences and medical devices."),
    ("Enterprise Applications leadership", "Ashish Kumar Goyal has led Enterprise Applications since May 2026, after about 15 years at Accenture.",
     "Pull-through for the platform practices (Salesforce, SAP, Oracle, Pega) and a consulting-led story.", "Design deals that combine experience design with platform work, so the portfolio grows as a whole."),
    ("Designit", "Wipro's strategic design company, led globally by Keri Dawson and aligned with the Experience Advisory practice.",
     "Strategy and design engagements with clients who value design, and a place in large deals as the studio model.", "Open with a Designit-led diagnostic where the buyer is a CMO, as in the TruStage and JFK Terminal 4 work."),
    ("Platform alliances", "Partner managers at Adobe, Salesforce, SAP and Pega. Wipro is an Adobe Platinum partner, Salesforce Summit partner and Pega Global Elite partner.",
     "Migrations to their cloud products and consumption growth.", "Work their end-of-support lists (AEM 6.5, legacy chat, SAP Commerce on premises) and register opportunities early to get co-sell support and funding."),
    ("Consulting and AI advisory", "Wipro Consulting under Amit Kumar originates advisory work that converts into technology and operations programmes.",
     "Advisory work that leads to larger programmes, and AI use cases with measurable value.", "Pair DX pursuits with an AI advisory lead so the client sees a self-funding case for AI in service and marketing."),
    ("Deal desk, pricing and delivery", "Finance, solution architects and delivery leads who price, staff and sign off large deals.",
     "Realistic staffing, margin above threshold and few surprises after signature.", "Bring them a clean scope, an onshore and offshore mix and a risk register at the first review."),
]


ORBIT = [("SMU client partner", "Access to the client"), ("DX practice leadership", "Delivery and margin"), ("Enterprise Applications", "Platform pull-through"),
         ("Designit", "The design front end"), ("Platform alliances", "Co-sell and funding"), ("Consulting and AI advisory", "Larger programmes"), ("Deal desk and delivery", "Price and staffing")]


def orbit_svg():
    import math
    cx, cy, R = 550, 300, 210
    o = ['<svg viewBox="0 -30 1100 630" role="img" aria-labelledby="obt obd"><title id="obt">Who the DX practitioner depends on</title><desc id="obd">Seven groups around the practitioner, none of which report to the role.</desc>']
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="var(--line)" stroke-dasharray="4 6"/>')
    for k, (n, w) in enumerate(ORBIT):
        a = -math.pi / 2 + k * 2 * math.pi / len(ORBIT)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        o.append(f'<line class="draw" style="--len:240;transition-delay:{k*.1:.1f}s" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="var(--accent)" stroke-width="1.5" opacity=".6"/>')
        o.append(f'<g data-pick="o{k}" aria-label="{E(n)}"><circle class="pop" style="transition-delay:{.3+k*.1:.1f}s" cx="{x:.0f}" cy="{y:.0f}" r="18" fill="var(--c{k%6})" stroke="transparent" stroke-width="10"/></g>')
        anc = "middle" if abs(math.cos(a)) < .3 else ("start" if math.cos(a) > 0 else "end")
        dx = 0 if anc == "middle" else (26 if anc == "start" else -26)
        dy = -52 if (anc == "middle" and math.sin(a) < 0) else (40 if anc == "middle" else 0)
        o.append(f'<text x="{x+dx:.0f}" y="{y+dy-2:.0f}" text-anchor="{anc}" font-size="22" font-weight="700" class="svg-ink">{E(n)}</text>')
        o.append(f'<text x="{x+dx:.0f}" y="{y+dy+26:.0f}" text-anchor="{anc}" font-size="20" class="svg-muted">{E(w)}</text>')
    o.append(f'<circle class="pop" cx="{cx}" cy="{cy}" r="86" fill="var(--accent)"/><text x="{cx}" y="{cy-6}" text-anchor="middle" font-size="30" font-weight="700" fill="var(--on-accent)">DX</text><text x="{cx}" y="{cy+24}" text-anchor="middle" font-size="21" font-weight="600" fill="var(--on-accent)">practitioner</text>')
    o.append("</svg>")
    return "".join(o)


def deals_vis():
    q = [("Q4 FY26", 1440), ("Q1 FY27", 1626), ("Q2 FY27", 674)]
    o = ['<svg viewBox="0 0 420 200" aria-hidden="true">']
    for i, (l, v) in enumerate(q):
        h = 150 * v / 1700
        x = 30 + i * 130
        c = "var(--bad)" if i == 2 else "var(--accent)"
        o.append(f'<rect class="growy" style="transition-delay:{i*.2}s" x="{x}" y="{165-h:.0f}" width="80" height="{h:.0f}" rx="3" fill="{c}"/>')
        o.append(f'<text x="{x+40}" y="{158-h:.0f}" text-anchor="middle" font-size="14" font-weight="700" class="svg-ink">${v:,}m</text><text x="{x+40}" y="188" text-anchor="middle" font-size="13" class="svg-muted">{l}</text>')
    o.append("</svg>")
    return "".join(o)


def growth_vis():
    d = [("Americas 1", -2.7), ("Americas 2", -4.7), ("Europe", 5.1), ("APMEA", 13.3)]
    o = ['<svg viewBox="0 0 420 200" aria-hidden="true"><line x1="200" x2="200" y1="10" y2="190" stroke="var(--line)"/>']
    for i, (l, v) in enumerate(d):
        y = 20 + i * 44
        w = abs(v) * 12
        x = 200 if v > 0 else 200 - w
        c = "var(--ok)" if v > 0 else "var(--bad)"
        o.append(f'<text x="0" y="{y+20}" font-size="14" font-weight="600" class="svg-ink">{l}</text>')
        o.append(f'<rect class="grow" x="{x:.0f}" y="{y+4}" width="{w:.0f}" height="24" rx="3" fill="{c}"/>')
        tx = 200 + w + 8 if v > 0 else 200 + 8
        o.append(f'<text x="{tx:.0f}" y="{y+21}" font-size="13" font-weight="600" fill="{c}">{v:+.1f}%</text>')
    o.append("</svg>")
    return "".join(o)


def build():
    body = hero("Operating Matrix", "Many Owners, One Number",
                "Market units own the client. Business lines own the offer. DX sells through both Americas units.",
                f'<div class="stage">{matrix_svg()}</div><p class="fine">Q2 FY27 constant-currency figures. The DX reporting line is my reading of public titles.</p>')

    b = (tile(f'<p class="t-k">FY26 IT services revenue</p>{num(10.48, pre="$", small="bn")}<p>Down 1.6% in constant currency.</p>', 4)
         + tile(f'<p class="t-k">Americas share</p>{num(60, suf="%")}<p>Of revenue in Q2 FY27.</p>', 4)
         + tile(f'<p class="t-k">Q3 FY27 guidance</p><div class="num" style="font-size:clamp(40px,4.4vw,60px)">-1.5% to +0.5%</div><p>Flat at best.</p>', 4)
         + tile(f'<p class="t-k">Large-deal bookings</p><h3>Down 58.6% in one quarter</h3><div class="vis">{deals_vis()}</div>', 6)
         + tile(f'<p class="t-k">Growth by market unit</p><h3>Both Americas units are shrinking</h3><div class="vis">{growth_vis()}</div>', 6))
    body += sec(head_block("Results", "The Numbers It Inherits", "Wipro needs new Americas pipeline, and it needs it large.") + f'<div class="bento">{b}</div>'
                + src([("Q2 FY27 results, 15 Oct 2026", Q2), ("Q4 FY26 results, 16 Apr 2026", Q4), ("Q1 FY27 call, 16 Jul 2026", Q1T)]), "grey")

    ppl = table(["Who", "Their role", "What they want", "How I would work with them"], [[E(a), b2, E(c), E(d)] for a, b2, c, d in PEOPLE], caption="Stakeholders")
    body += sec(head_block("Stakeholders", "Seven Groups, No Direct Reports", "Each one controls something a large deal needs.") + explorer(orbit_svg(), {f"o{k}": f'<p class="t-k">{E(ORBIT[k][1])}</p><h3>{E(a)}</h3><p>{b2}</p><p><b>They want</b> {E(c)}</p><p><b>How I work with them</b> {E(d)}</p>' for k, (a, b2, c, d) in enumerate(PEOPLE)}, "Select a group.", first="o0") + more("Show the table", ppl), "dark", center=True)

    raci = table(
        ["Pursuit step", "DX practitioner", "SMU client partner", "DX practice and delivery", "Designit or consulting", "Alliance partner"],
        [["Spot the trigger and size the idea", heat(4, "Leads"), heat(2, "Informs"), heat(1, "Consulted"), heat(1, "Consulted"), heat(2, "Informs")],
         ["Get access to the buyer", heat(2, "Shares"), heat(4, "Leads"), heat(0, ""), heat(1, "Supports"), heat(2, "Introduces")],
         ["Diagnostic or point of view", heat(3, "Owns"), heat(1, "Supports"), heat(2, "Supports"), heat(4, "Delivers"), heat(1, "Supports")],
         ["Solution, staffing and price", heat(3, "Owns"), heat(1, "Approves"), heat(4, "Builds"), heat(2, "Supports"), heat(1, "Funds")],
         ["Negotiate and sign", heat(4, "Leads"), heat(3, "Co-leads"), heat(1, "Supports"), heat(0, ""), heat(0, "")],
         ["Hand over and expand", heat(2, "Supports"), heat(3, "Owns"), heat(4, "Delivers"), heat(1, "Supports"), heat(1, "Supports")]],
        caption="Roles across a pursuit")
    body += sec(head_block("Roles", "Who Does What", "Agreed before the pursuit starts.") + f'<div class="rv">{raci}</div>')

    comp = (tile(f'{icon("grid")}<h3 style="margin-top:20px">Overlay</h3><p>Sell into accounts that client partners own, as the technical deal owner.</p>', 4, "short")
            + tile(f'{icon("target")}<h3 style="margin-top:20px">Hunt and farm</h3><p>New logos pay more and carry more risk than expansion.</p>', 4, "short")
            + tile(f'{icon("chart")}<h3 style="margin-top:20px">Forecast within 5%</h3><p>Bookings, revenue and a monthly forecast close to plan.</p>', 4, "short"))
    body += sec(head_block("Measures", "How It Is Measured", "From Wipro practitioner postings and a UK tribunal judgment.") + f'<div class="bento">{comp}</div>'
                + src([("Wipro Cloud and Digital Director posting", CLOUD), ("Chandrashekarappa v Wipro, UK Employment Tribunal", TRIB)]), "grey")
    page("operating-model.html", body, "Where the Wipro DX practitioner sits in the matrix, with results, stakeholders and pursuit roles.")
