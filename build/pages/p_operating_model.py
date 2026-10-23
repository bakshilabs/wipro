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


def build():
    stats = f"""<div class="stats">
<div class="stat"><b>$10.48bn</b><span>IT services revenue, FY26, down 1.6% in constant currency</span><small><a href="{Q4}">Q4 FY26 results</a></small></div>
<div class="stat"><b>60%</b><span>Share of revenue from Americas 1 and Americas 2 in Q2 FY27</span><small><a href="{Q2}">Q2 FY27 results</a></small></div>
<div class="stat"><b>$7.8bn</b><span>Large-deal bookings in FY26, up 45%. Large deals are $30m TCV or more</span><small><a href="{Q4}">Q4 FY26 results</a></small></div>
<div class="stat"><b>-58.6%</b><span>Fall in large-deal bookings from Q1 to Q2 FY27, to $674m</span><small><a href="{Q2}">Q2 FY27 results</a></small></div>
</div>"""

    reading = f"""<div class="grid2">
<div class="panel"><p class="k">What the numbers say</p><p>Both Americas units shrank year on year in Q2 FY27 while Europe and APMEA grew. Large-deal bookings fell sharply in the quarter, and guidance for Q3 is between -1.5% and +0.5%. Wipro needs new Americas pipeline, and it needs it to be large.</p></div>
<div class="panel"><p class="k">What the CEO says buyers want</p><p>On the Q1 FY27 call Srini Pallia said discretionary spend has been slower, decisions take longer, and clients are reinvesting cost savings in AI. A DX pitch therefore has to pay for itself and lead with AI, with experience design as the way to get the value.</p></div>
<div class="panel"><p class="k">What the hiring pattern says</p><p>Between July and October 2026 Wipro posted four US DX practitioner roles: this one, energy and manufacturing, retail and life sciences, and an enterprise experience lead. Wipro is building a bench of sector DX sellers across both Americas units at the same time.</p></div>
<div class="panel"><p class="k">What the leadership changes say</p><p>Technology Services and Enterprise Applications both have new leaders since April and May 2026, both from Accenture. New leaders tend to back a consulting-led, large-deal model and to measure sellers against it early.</p></div>
</div>
{src([("Q2 FY27 press release, 15 Oct 2026", Q2), ("Q1 FY27 earnings call transcript, 16 Jul 2026", Q1T), ("SEBI filing on senior management, 1 Apr 2026", SEBI), ("HR Today on Enterprise Applications appointment, 21 May 2026", GOYAL)])}"""

    ppl = table(
        ["Who", "Their role", "What they want", "How I would work with them"],
        [[E(a), b, E(c), E(d)] for a, b, c, d in PEOPLE],
        caption="Stakeholders a DX practitioner works through",
    ) + src([("Designit, Keri Dawson appointment, 4 Nov 2024", DESIGNIT), ("Wipro partner pages for Adobe, Salesforce and Pega", "https://www.wipro.com/partners/adobe/")])

    raci = table(
        ["Pursuit step", "DX practitioner", "SMU client partner", "DX practice and delivery", "Designit or consulting", "Alliance partner"],
        [
            ["Spot the trigger and size the idea", heat(4, "Leads"), heat(2, "Informs"), heat(1, "Consulted"), heat(1, "Consulted"), heat(2, "Informs")],
            ["Get access to the buyer", heat(2, "Shares"), heat(4, "Leads"), heat(0, ""), heat(1, "Supports"), heat(2, "Introduces")],
            ["Diagnostic or point of view", heat(3, "Owns"), heat(1, "Supports"), heat(2, "Supports"), heat(4, "Delivers"), heat(1, "Supports")],
            ["Solution, staffing and price", heat(3, "Owns"), heat(1, "Approves"), heat(4, "Builds"), heat(2, "Supports"), heat(1, "Funds")],
            ["Negotiate and sign", heat(4, "Leads"), heat(3, "Co-leads"), heat(1, "Supports"), heat(0, ""), heat(0, "")],
            ["Hand over and expand", heat(2, "Supports"), heat(3, "Owns"), heat(4, "Delivers"), heat(1, "Supports"), heat(1, "Supports")],
        ],
        caption="Roles across a DX pursuit",
    )

    comp = f"""<div class="grid3">
<div class="panel"><p class="k">Overlay</p><p>Practitioner sellers are specialists who support the account lead. A Wipro cloud and digital practitioner posting asks them to "work collaboratively with Client Partners and Global Account Executives in a matrix model to sell into their accounts" and to act as "the technical deal owner".</p></div>
<div class="panel"><p class="k">Hunting and farming</p><p>A UK employment tribunal judgment describes Wipro's sales incentive plan as dividing work into hunting (new logos) and farming (expansion), with hunting paid at higher risk and reward. The two need different plans and different pipeline coverage.</p></div>
<div class="panel"><p class="k">Forecast discipline</p><p>The same cloud and digital posting sets bookings (TCV and ACV), profitable revenue and a monthly forecast within 5% variance as the measures. I would expect DX to be held to the same standard.</p></div>
</div>
{src([("Wipro Cloud and Digital Director posting, 2026", CLOUD), ("Chandrashekarappa v Wipro, UK Employment Tribunal, c. 2024", TRIB)])}"""

    body = (
        phead("Matrix", "Operating Matrix",
              "Wipro sells through four strategic market units that own clients and four global business lines that own offerings. The DX practice sits inside Enterprise Applications in Technology Services. This page maps where the role sits, who it depends on and what Wipro's current results ask of it.",
              f'Structure from the <a href="{AR}">FY2025-26 annual report</a> and the <a href="{Q2}">Q2 FY27 results</a> of 15 October 2026.')
        + block("Structure", "Where the role sits", f'<figure class="fig">{matrix_svg()}<figcaption>Revenue shares and growth rates are constant-currency figures for Q2 FY27 (July to September 2026). The reporting line from the DX practice to Enterprise Applications to Technology Services is my reading of public titles and is not documented by Wipro.</figcaption></figure>',
                "Revenue is booked to the market unit that owns the client. The DX practitioner carries a number for the practice and gets there through the market units, mostly Americas 1 for consumer and health and Americas 2 for banking and manufacturing.")
        + block("Context", "The numbers the role inherits", stats + reading)
        + block("Stakeholders", "Who the role depends on", ppl,
                "None of these people report to the DX practitioner. Each one controls something a large deal needs.")
        + block("Roles", "Who does what in a pursuit", raci,
                "Agreeing these roles before a pursuit starts is the cheapest way to avoid the credit and access disputes that slow matrix selling.")
        + block("Compensation logic", "How practitioner selling is measured", comp)
    )
    page("operating-model.html", body, "Where the Wipro DX practitioner sits in the SMU and business-line matrix, with stakeholders and pursuit roles.")
