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


def build():
    rows = "".join(
        f'<tr><th scope="row">{E(q)}</th><td>{m}</td><td>{E(a)}</td></tr>'
        for q, m, a in DECODE
    )
    decode = (
        '<div class="tbl-wrap" tabindex="0" role="region" aria-label="Posting decoded line by line"><table class="t">'
        '<thead><tr><th scope="col" style="width:24%">What the posting says</th><th scope="col">What it means at Wipro</th><th scope="col">How I would work it</th></tr></thead>'
        f"<tbody>{rows}</tbody></table></div>"
        + src([("Wipro careers, Director - Digital Experience (DX), posted 16 Jul 2026", POST)])
    )

    comp = table(
        ['<span class="sr">Attribute</span>', '<a href="' + POST + '">Director, DX</a>', '<a href="' + SIB + '">DX Practice Director, Retail and Life Sciences</a>', '<a href="' + EMR + '">DX Practice Director, EMR</a>', '<a href="' + FRA + '">Business Development Director (Frankfurt)</a>'],
        [[E(r[0])] + [E(x) for x in r[1:]] for r in COMPARE_ROWS],
        caption="Four related Wipro postings compared",
    )
    const = '<div class="grid2">' + "".join(
        f'<div class="panel"><p class="k">Constant {i+1}</p><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, (h, p) in enumerate(CONSTANTS)
    ) + "</div>"

    # stacked bar of time allocation on a 1000 wide canvas
    leg = "".join(f'<span><i style="background:var(--{c})"></i>{E(l)} ({p}%)</span>' for l, p, c in TIME)
    segs = ""
    x = 0
    for lab, pct, c in TIME:
        segs += f'<rect x="{x*10}" y="0" width="{pct*10}" height="44" fill="var(--{c})"><title>{E(lab)}: {pct}%</title></rect>'
        x += pct
    timefig = (
        f'<figure class="fig"><svg viewBox="0 0 1000 44" preserveAspectRatio="none" style="height:44px" role="img" aria-label="Estimated share of a working week: clients 30%, SMU partners 20%, solutioning 20%, alliances 10%, thought leadership 10%, forecasting 10%">{segs}</svg>'
        f'<div class="legend">{leg}</div>'
        '<figcaption>My estimate of where a DX practitioner\'s week goes, read from the posting\'s language about SMUs, practices, alliances and thought leadership. About half the week is spent inside Wipro.</figcaption></figure>'
    )

    persona = """<div class="grid3">
<div class="panel"><p class="k">Hunter inside farmed accounts</p><p>The practitioner finds new DX work inside accounts that other people already manage, and wins new logos where the SMU has none. The skill is spotting a DX opportunity in an account where Wipro sells infrastructure or applications today.</p></div>
<div class="panel"><p class="k">Shaper of large deals</p><p>The practitioner turns a client's problem into a priced, phased programme with a run phase that makes it a $20m deal, and can defend the price, the staffing and the outcomes in front of procurement.</p></div>
<div class="panel"><p class="k">Credible with the CMO and the CIO</p><p>The practitioner can talk about brand, journeys and content operations with marketing, and about platforms, integration and cost with IT, in the same meeting.</p></div>
</div>"""

    body = (
        phead("Role", "Role Anatomy",
              "The Director, Digital Experience (DX) posting describes an overlay seller who originates and shapes large experience transformation deals inside Wipro's account matrix. This page reads the posting line by line, compares it with three related Wipro postings and sets out how I would do the job.",
              f'Primary source: <a href="{POST}">Wipro careers listing</a>, posted 16 July 2026, $200,000 to $280,000.')
        + block("Decoded", "The posting line by line", decode,
                "Each line of the posting has an operating consequence. The middle column is my reading of how Wipro runs this role. The right column is what I would do about it.")
        + block("Related postings", "Four Wipro sales postings side by side", comp + const,
                "Between July and October 2026 Wipro posted four US DX practitioner roles on the same template and pay band, which suggests it is building a sector-aligned DX sales bench across both Americas market units. Comparing three of them with a European business development posting shows what changes by territory and what stays constant. The constants are what Wipro screens for.")
        + block("The week", "Where the time goes", timefig)
        + block("The person", "The person the posting describes", persona,
                "Taken together, the posting asks for three capabilities that rarely sit in one person. Most candidates bring one or two of them.")
    )
    page("role.html", body, "The Wipro DX Director posting decoded line by line, compared with related postings, with an operating plan.")
