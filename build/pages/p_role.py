from lib import *

POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"
SIB = "https://careers.wipro.com/job/DX-Practice-Director-Retail-&-Consumer%2C-Life-Sciences%2C-Medical-Devices/198032-en_US/"
EMR = "https://careers.wipro.com/job/DX-Practice-Director-Energy%2C-Manufacturing%2C-and-Resources/190268-en_US/"
FRA = "https://careers.wipro.com/job/Business-Development-Director-%28MFD%29/212298-en_US/"

# each line of the posting, what it means in practice, and what I would do with it
DECODE = [
    ("As a Sales Practitioner",
     "Wipro uses practitioner for an offering specialist who sells one service line into accounts that a Strategic Market Unit (SMU) client partner owns. The practitioner carries a DX number but does not own the client relationship or the account P&amp;L.",
     "Treat every SMU client partner as my first customer. Arrive with a reason for them to bring me into their account: a dated trigger, a point of view and a sized opportunity that grows their number as well as mine."),
    ("Matrixed and leveraged organization construct as a part of the Enterprise Apps portfolio",
     "DX sits inside the Enterprise Apps portfolio, next to the platform practices (SAP, Oracle, Salesforce and others). Many DX deals are won on a platform decision, and the credit for them is shared between the SMU, the platform practice and DX.",
     "Agree credit splits and roles before the pursuit starts. Build pursuits that pull platform work through DX, so the platform practices gain from inviting me in."),
    ("Accountable for meeting sales KPIs based on Revenue growth and Order bookings (ACV / TCV)",
     "Two measures run in parallel. Total contract value (TCV) counts the whole multi-year commitment at signature. Annual contract value (ACV) and revenue show how fast it turns into billing. A three-year $21m deal is $7m of ACV a year.",
     "Shape deals with a run phase so that TCV is large and ACV is steady. Track bookings and revenue separately in my own forecast, because a design-heavy year can book well and bill late."),
    ("Experience in leading large experience transformation deals. Large deal min. $20m",
     "Experience design and build projects on their own rarely reach $20m. Deals of that size are put together: strategy and design, a platform rebuild, then multi-year managed operations of the platform, content and AI agents. Wipro's quarterly results count large deals from $30m TCV, so a $30m deal is also visible to the group.",
     "Land with a paid diagnostic or design sprint, then ladder to build and run. The Pursuit Model page shows how a $1.2m design engagement becomes a deal of more than $20m TCV."),
    ("Experience in managing portfolio of $20m to $25m",
     "The seller is expected to hold a book of business of that size across several accounts, so the role mixes expanding existing DX work with winning new logos.",
     "Split the book into protect, expand and new logo targets from month one. The Portfolio Maths page sets the pipeline coverage each needs."),
    ("Engage with customer CDOs / CXOs ... to influence their digital experience strategy",
     "The buyer is a business executive (chief digital officer, chief marketing officer, chief customer officer) with the CIO as co-signer. The pitch has to be about revenue, retention and cost to serve, with technology as the means.",
     "Lead with a measured business case: conversion, cost per contact, content cost per asset, time to market. Bring the CIO in early so that the IT side backs the case instead of blocking it."),
    ("Collaborate with various Wipro teams to develop proactive proposals",
     "Proactive means unsolicited. Wipro wants deals shaped before an RFP exists, when there is no competitive bake-off and the client buys the idea before it buys a supplier.",
     "Run a trigger calendar (platform end-of-support dates, regulation deadlines, leadership changes) and turn each trigger into a costed proposal before the client goes to market."),
    ("Provide thought leadership throughout the sales lifecycle",
     "The seller is expected to bring insight that a client cannot get from its incumbent agency, and to keep bringing it after the first meeting.",
     "Publish short points of view tied to a client's own data: an accessibility scan of their site, a tech-stack audit, a benchmark against peers. I did this for net zero with carbon baselines, and the method carries over."),
    ("Drive operational efficiency and minimize friction in sales/solution/delivery process",
     "Wipro wins on blended delivery with large offshore teams. A deal sold without a delivery plan turns into a margin problem for the account.",
     "Bring the delivery lead into the pursuit at qualification, price on a realistic onshore and offshore mix, and hand over with a written plan for the first 90 days."),
    ("Leverage Wipro leadership to forge strategic relationships with clients",
     "Executive sponsorship is a deliberate lever: a Wipro executive meets the client's executive at a decisive moment of the pursuit.",
     "Plan one leadership touchpoint per large pursuit, with a brief, a specific ask and a follow-up owner."),
    ("New age digital experiences like metaverse, AR/VR",
     "This line reads like older boilerplate. The August and September 2026 DX postings replace it with AI and generative AI, and names Adobe, SAP Commerce, Adobe Commerce, Shopify, Pega and Appian.",
     "Lead with agentic and AI-assisted experience work, where client budgets are moving in 2026, and keep AR/VR for the few clients who have a real case for it."),
]

COMPARE_ROWS = [
    ("Posted", "16 Jul 2026", "10 Aug 2026", "2 Sep 2026", "20 Oct 2026"),
    ("Territory", "North America, Americas sales outcomes", "Detroit, New Jersey, Dallas or Houston", "Americas, flexible US location", "Germany and Austria"),
    ("Industry focus", "Any, within a defined portfolio", "Energy, manufacturing and resources (Americas 2)", "Retail and consumer, life sciences, medical devices (Americas 1)", "Manufacturing, cross-industry"),
    ("Experience asked", "10 to 15 years, 5 to 7 selling DX to C-suite", "Same template as the retail posting", "12 to 18 years, 5 or more selling DX to C-suite", "10 or more years in IT services sales"),
    ("Deal size named", "Large deals of $20m or more; portfolio of $20m to $25m", "Large-deal outcomes", "Large-deal outcomes, multi-tower deals", "Multi-technology deals of $30m or more"),
    ("Platforms named", "Low code, ECM, MarTech, commerce (generic)", "Adobe marketing stack, SAP Commerce, Adobe Commerce, Shopify, Pega, Appian", "Adobe marketing stack, SAP Commerce, Adobe Commerce, Shopify, Pega, Appian", "AI, apps, engineering, infrastructure"),
    ("New technology named", "Metaverse, AR/VR", "AI and generative AI", "AI and generative AI, AI-led solutioning", "AI solutions"),
    ("Who you work with", "SMUs, Wipro sales, Experience Technologies practices", "Consulting, practice, alliance, delivery and account teams", "Consulting, practice, alliance, delivery and account teams", "Solution architects, finance, delivery, legal, alliances"),
    ("How success is measured", "Order bookings (ACV/TCV) and revenue", "Pipeline, bookings, revenue, large-deal wins", "Qualified pipeline, bookings, revenue, large-deal wins, account expansion", "Sales quota"),
    ("Pay range", "$200,000 to $280,000", "$200,000 to $280,000", "$200,000 to $280,000", "Not stated"),
]

CONSTANTS = [
    ("Origination", "Every posting asks the seller to create opportunities: generate leads, build pipeline, propose proactively. None of them describes a role that waits for RFPs."),
    ("Deal shaping", "Each one asks for large-deal experience and the commercial skill to structure it: financial modelling, contract terms, multi-tower bundling."),
    ("C-suite consultative selling", "The buyer is always a business executive, and the method is consultative: understand the problem, frame it, size the value."),
    ("Matrix fluency", "All four list the internal teams the seller has to orchestrate. Wipro is hiring someone who gets more done through other people's teams than through their own."),
]

# estimated weekly time split for a DX practitioner; my estimate from the posting language, not Wipro data
TIME = [
    ("Client executives and their teams", 30, "c0"),
    ("SMU client partners and account teams", 20, "c1"),
    ("Solutioning, pricing and proposals with practice and delivery", 20, "c2"),
    ("Alliance partners (Adobe, Salesforce, SAP, Pega)", 10, "c3"),
    ("Points of view, events and analyst relations", 10, "c4"),
    ("Forecasting, deal reviews and CRM", 10, "c6"),
]


SHORT_DO = [
    "Treat every client partner as my first customer.",
    "Agree credit splits before the pursuit starts.",
    "Shape deals with a run phase: large TCV, steady ACV.",
    "Land with a small design phase, ladder to build and run.",
    "Split the book into protect, expand and new logo.",
    "Lead with revenue, retention and cost to serve.",
    "Turn each dated trigger into a costed proposal first.",
    "Bring insight from the client's own data.",
    "Put delivery in the room at qualification.",
    "Plan one leadership meeting per large pursuit.",
    "Lead with AI and agentic experience work.",
]
QUOTE = [
    "Sales Practitioner", "Matrixed and leveraged organization", "Order bookings (ACV / TCV)", "Large deal min. $20m",
    "Portfolio of $20m to $25m", "Engage CDOs / CXOs", "Proactive proposals", "Thought leadership throughout",
    "Minimize friction in sales, solution, delivery", "Leverage Wipro leadership", "Metaverse, AR/VR",
]


WEEK = {
    "Client executives and their teams": "Discovery, workshops, proposal defence and executive meetings. The only time that books revenue directly.",
    "SMU client partners and account teams": "Fortnightly account sessions, joint plans and credit agreements. Access to the client runs through here.",
    "Solutioning, pricing and proposals with practice and delivery": "Scope, staffing mix, price and risk with the DX practice and deal desk.",
    "Alliance partners (Adobe, Salesforce, SAP, Pega)": "Migration lists, registered opportunities and co-sell funding.",
    "Points of view, events and analyst relations": "Short, data-led points of view tied to dated triggers, and one event a quarter.",
    "Forecasting, deal reviews and CRM": "Weekly pipeline review and a forecast within the variance Wipro expects.",
}
POSTD = [
    ("16 July 2026", "Director, Digital Experience (DX)", "Americas, any industry, inside the Enterprise Apps portfolio. Large deals of $20m or more, a $20m to $25m portfolio, $200,000 to $280,000. This role."),
    ("10 August 2026", "DX Practice Director, Energy, Manufacturing and Resources", "Detroit, New Jersey, Dallas or Houston. An Americas 2 sector. Names the Adobe marketing stack, SAP Commerce, Adobe Commerce, Shopify, Pega and Appian."),
    ("2 September 2026", "DX Practice Director, Retail, Life Sciences, Medical Devices", "Chicago or Seattle. Americas 1 sectors. Originate, shape and close; multi-tower deals; AI-led solutioning."),
    ("October 2026", "DX Practice Director, Enterprise Experience Lead", "Detroit. A multi-year portfolio in a matrixed Enterprise Apps environment. Seen on an aggregator."),
]

VENN = {
    "v0": '<p class="t-k">My evidence</p><h3>Hunter</h3><p>Won more than $2m a year at WSP through cold and warm outreach. Found work for Foster + Partners studios in accounts that partners owned.</p>',
    "v1": '<p class="t-k">My evidence</p><h3>Shaper</h3><p>Led pitches that won more than £10m a year in fees. Won a multi-year portfolio contract with a global pharmaceutical company. Co-created a new advisory service line.</p>',
    "v2": '<p class="t-k">My evidence</p><h3>Translator</h3><p>Architect and computational designer who sells. Talks experience design with marketing and tools, data and delivery with technology. Trains executives on AI tools at Atlas Learn.</p>',
}


def overlay_svg():
    W, H = 1100, 420
    o = ['<svg viewBox="0 0 1100 420" role="img" aria-labelledby="ot od"><title id="ot">The practitioner overlay</title>'
         '<desc id="od">Five client accounts, each owned by a client partner. The DX practitioner sells across all of them through a band that crosses every account.</desc>']
    accts = ["Life sciences", "Medical devices", "Retail", "Consumer goods", "Banking"]
    for i, a in enumerate(accts):
        x = 40 + i * 210
        o.append(f'<rect class="rv d{i%4+1}" x="{x}" y="20" width="180" height="330" rx="6" fill="var(--grey)"/>')
        o.append(f'<circle cx="{x+90}" cy="70" r="22" fill="var(--c6)" opacity=".5"/><path d="M{x+76} 106c4-10 24-10 28 0" stroke="var(--c6)" stroke-width="6" fill="none" opacity=".5"/>')
        o.append(f'<text x="{x+90}" y="140" text-anchor="middle" font-size="14" font-weight="600" class="svg-ink">Client partner</text>')
        o.append(f'<text x="{x+90}" y="160" text-anchor="middle" font-size="13" class="svg-muted">{a}</text>')
        for k in range(3):
            o.append(f'<rect x="{x+30}" y="{280+k*16}" width="{120-k*30}" height="8" rx="4" fill="var(--line)"/>')
    o.append('<rect class="grow" x="20" y="196" width="1060" height="58" rx="6" fill="var(--accent)"/>')
    o.append('<text x="550" y="232" text-anchor="middle" font-size="19" font-weight="700" fill="var(--on-accent)">DX practitioner: one number, sold through every account</text>')
    o.append('<text x="550" y="400" text-anchor="middle" font-size="14" class="svg-muted">Client partners own the relationship and the account P&amp;L. The practitioner owns the DX bookings.</text>')
    o.append("</svg>")
    return "".join(o)


def postings_svg():
    P = [("16 Jul", "DX Director", "Americas, any industry", "This role"), ("10 Aug", "DX Practice Director", "Energy, manufacturing, resources", "Americas 2"),
         ("2 Sep", "DX Practice Director", "Retail, life sciences, medical devices", "Americas 1"), ("Oct", "DX Practice Director", "Enterprise experience lead", "Detroit")]
    o = ['<svg viewBox="0 0 1100 250" role="img" aria-label="Four US DX postings from July to October 2026">',
         '<line x1="150" x2="948" y1="60" y2="60" stroke="var(--line)" stroke-width="2"/><line class="draw" style="--len:800" x1="150" x2="948" y1="60" y2="60" stroke="var(--accent)" stroke-width="3"/>']
    for i, (d, t, f, u) in enumerate(P):
        x = 150 + i * 266
        o.append(f'<g data-pick="p{i}" aria-label="{E(t)}, {E(f)}"><circle class="pop" style="transition-delay:{.3+i*.3}s" cx="{x}" cy="60" r="{16 if i==0 else 12}" fill="var(--accent)" stroke="transparent" stroke-width="10"/></g>')
        o.append(f'<text x="{x}" y="24" text-anchor="middle" font-size="16" font-weight="700" class="svg-ink">{d} 2026</text>')
        o.append(f'<text x="{x}" y="112" text-anchor="middle" font-size="17" font-weight="700" class="svg-ink">{E(t)}</text>')
        o.append(f'<text x="{x}" y="136" text-anchor="middle" font-size="14" class="svg-muted">{E(f)}</text>')
        o.append(f'<text x="{x}" y="162" text-anchor="middle" font-size="13" font-weight="600" fill="var(--accent)">{E(u)}</text>')
    o.append('<text x="550" y="228" text-anchor="middle" font-size="14" class="svg-muted">Same template. Same $200,000 to $280,000 band. One seller per industry cluster.</text></svg>')
    return "".join(o)


def donut_svg():
    import math
    R, r, cx, cy = 150, 96, 180, 180
    o = ['<svg viewBox="0 0 360 360" role="img" aria-label="Estimated share of a working week">']
    a0 = -math.pi / 2
    for lab, pct, c in TIME:
        a1 = a0 + 2 * math.pi * pct / 100
        large = 1 if pct > 50 else 0
        p = (f"M{cx+R*math.cos(a0):.1f} {cy+R*math.sin(a0):.1f} A{R} {R} 0 {large} 1 {cx+R*math.cos(a1):.1f} {cy+R*math.sin(a1):.1f} "
             f"L{cx+r*math.cos(a1):.1f} {cy+r*math.sin(a1):.1f} A{r} {r} 0 {large} 0 {cx+r*math.cos(a0):.1f} {cy+r*math.sin(a0):.1f}Z")
        o.append(f'<g data-pick="w{TIME.index((lab, pct, c))}" aria-label="{E(lab)}"><path class="pop" d="{p}" fill="var(--{c})" stroke="var(--bg)" stroke-width="3"/></g>')
        a0 = a1
    o.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="44" font-weight="700" class="svg-ink">50%</text><text x="{cx}" y="{cy+24}" text-anchor="middle" font-size="14" class="svg-muted">inside Wipro</text>')
    o.append("</svg>")
    return "".join(o)


def venn_svg():
    C = [(380, 170, "Hunter in farmed accounts", "c0"), (560, 170, "Shaper of large deals", "c1"), (470, 320, "Credible with CMO and CIO", "c3")]
    o = ['<svg viewBox="0 0 940 500" role="img" aria-label="Three capabilities that overlap in one hire">']
    for i, (x, y, t, c) in enumerate(C):
        o.append(f'<g data-pick="v{i}" aria-label="{E(t)}"><circle class="pop" style="transition-delay:{i*.25}s" cx="{x}" cy="{y}" r="150" fill="var(--{c})" fill-opacity=".22" stroke="var(--{c})" stroke-width="2.5"/></g>')
    o.append('<text x="250" y="130" text-anchor="middle" font-size="19" font-weight="700" class="svg-ink">Hunter</text><text x="250" y="154" text-anchor="middle" font-size="14" class="svg-muted">finds DX inside other</text><text x="250" y="172" text-anchor="middle" font-size="14" class="svg-muted">people\'s accounts</text>')
    o.append('<text x="690" y="130" text-anchor="middle" font-size="19" font-weight="700" class="svg-ink">Shaper</text><text x="690" y="154" text-anchor="middle" font-size="14" class="svg-muted">builds $20m deals</text><text x="690" y="172" text-anchor="middle" font-size="14" class="svg-muted">and defends the price</text>')
    o.append('<text x="470" y="410" text-anchor="middle" font-size="19" font-weight="700" class="svg-ink">Translator</text><text x="470" y="434" text-anchor="middle" font-size="14" class="svg-muted">speaks brand and platforms</text><text x="470" y="452" text-anchor="middle" font-size="14" class="svg-muted">in the same meeting</text>')
    o.append('<circle cx="470" cy="222" r="44" fill="var(--accent)"/><text x="470" y="228" text-anchor="middle" font-size="16" font-weight="700" fill="var(--on-accent)">The hire</text>')
    o.append("</svg>")
    return "".join(o)


def build():
    body = hero("Role Anatomy", "Sales Practitioner",
                "An overlay seller who originates large experience deals inside accounts that other people own.", f'<div class="stage">{overlay_svg()}</div>')

    cards = "".join(
        f'<div class="tile"><p class="t-k">Line {i+1}</p><h3 style="font-size:28px">“{E(QUOTE[i])}”</h3><p style="margin-top:auto;padding-top:24px;font-size:18px;color:var(--ink)"><b style="color:var(--accent)">I would</b> {E(SHORT_DO[i].rstrip("."))}.</p></div>'
        for i in range(len(DECODE)))
    rows = "".join(f'<tr><th scope="row">{E(q)}</th><td>{m}</td><td>{E(a)}</td></tr>' for q, m, a in DECODE)
    decode = ('<div class="tbl-wrap" tabindex="0" role="region" aria-label="Posting decoded line by line"><table class="t">'
              '<thead><tr><th scope="col" style="width:24%">What the posting says</th><th scope="col">What it means at Wipro</th><th scope="col">How I would work it</th></tr></thead>'
              f"<tbody>{rows}</tbody></table></div>" + src([("Wipro careers, Director - Digital Experience (DX), posted 16 Jul 2026", POST)]))
    body += sec(head_block("Decoded", "Eleven Lines", "Each line of the posting, and what I would do about it.") + f'<div class="rail rv">{cards}</div>' + more("Show what each line means at Wipro", decode), "dark")

    comp = table(
        ['<span class="sr">Attribute</span>', '<a href="' + POST + '">Director, DX</a>', '<a href="' + EMR + '">DX Practice Director, EMR</a>', '<a href="' + SIB + '">DX Practice Director, Retail and Life Sciences</a>', '<a href="' + FRA + '">Business Development Director (Frankfurt)</a>'],
        [[E(r[0])] + [E(x) for x in r[1:]] for r in COMPARE_ROWS], caption="Related Wipro postings compared")
    consts = "".join(tile(f'{icon(ic)}<h3 style="margin-top:20px;font-size:22px">{E(h)}</h3>', 3, "short") for ic, (h, p) in zip(["spark", "ladder", "people", "grid"], CONSTANTS))
    body += sec(head_block("Pattern", "Four Postings", "Wipro is hiring one DX seller per industry cluster.") + explorer(postings_svg(), {f"p{i}": f'<p class="t-k">{E(d)}</p><h3>{E(t)}</h3><p>{E(x)}</p>' for i, (d, t, x) in enumerate(POSTD)}, "Select a posting.", first="p0", stack=True)
                + '<h3 class="h-l rv" style="margin-top:72px">What never changes</h3>' + f'<div class="bento" style="margin-top:28px">{consts}</div>' + more("Compare the postings", comp), "grey")

    body += sec(head_block("The week", "Half Inside Wipro", "My estimate of where a practitioner's time goes.") + explorer(f'<div class="art s" style="margin-top:0">{donut_svg()}</div>', {f"w{i}": f'<p class="t-k">{pct}% of the week</p><h3>{E(lab)}</h3><p>{E(WEEK[lab])}</p>' for i, (lab, pct, c) in enumerate(TIME)}, "Select a segment.", first="w0"))
    body += sec(head_block("The person", "Three in One", "The posting asks for three capabilities that rarely sit in one person.") + explorer(venn_svg(), VENN, "Select a circle to see my evidence for it.", first="v0"), "grey", center=True)
    page("role.html", body, "The Wipro DX Director posting decoded, compared with related postings, and the person it describes.")
