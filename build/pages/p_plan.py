from lib import *

PHASES = [
    ("Days 1 to 30", "Map the matrix", [
        "Meet the Americas 1 consumer and health leaders and the Americas 2 banking and manufacturing leaders, then the fifteen client partners whose accounts fall in my portfolio. Agree three to five joint accounts with each.",
        "Learn the DX offers, rate cards, deal desk rules and the reference cases: TruStage, JFK Terminal 4, Odido, Levi Strauss and the Salesforce work shown at Dreamforce 2026.",
        "Meet the Adobe, Salesforce, SAP and Pega partner managers and obtain their end-of-support and migration lists for my accounts.",
        "Run tech-stack scans on fifty target accounts and match each one to the trigger calendar.",
        "Clean the inherited pipeline: every opportunity over $1m gets a next step, a date and an owner, or is closed.",
    ], "A written account plan for 25 named accounts, a dated trigger list and agreed credit rules with each client partner."),
    ("Days 31 to 90", "Open conversations", [
        "Publish three short points of view tied to dated triggers: AEM 6.5 migration for medical device makers, accessibility for health and life sciences ahead of May 2027, and agent-ready commerce for retail and consumer brands.",
        "Hold twenty first meetings with buyers, half through client partners and half through my own relationships at Roche, Genentech, Hyundai and JPMorgan Chase.",
        "Propose two paid diagnostics led by Designit, each scoped under $1m so the client can buy without a full procurement cycle.",
        "Close a first expansion deal inside an existing Wipro account to show the model working.",
    ], "Qualified pipeline of about $40m, two diagnostics in proposal and one booking."),
    ("Days 91 to 180", "Shape large deals", [
        "Shape two pursuits of more than $20m TCV through the deal ladder, each with a Wipro leadership sponsor and a written plan for credit and delivery.",
        "Put one proactive proposal in front of a separating company with a fixed exit date, such as DePuy Synthes, MiniMed or a Walgreens unit.",
        "Reach pipeline coverage of three times the next two quarters' target.",
        "Speak at one platform event or industry conference on experience design and AI, with a client on the panel.",
    ], "Two large pursuits in solution stage, coverage at three times, and bookings tracking to the annual target."),
]

METRICS = [
    ("Qualified pipeline (TCV)", "$40m", "$75m", "$90m or more"),
    ("Bookings (TCV)", "$2m to $3m", "$8m to $12m", "$25m"),
    ("First buyer meetings", "20", "40", "70"),
    ("Client partners actively co-selling", "6", "10", "15"),
    ("Large pursuits ($20m or more) in play", "0", "2", "3 to 4"),
    ("Points of view published", "3", "5", "8"),
]

ASKS = [
    ("Named client partners", "An agreed list of Americas 1 and Americas 2 accounts with a named client partner and an agreed credit rule for each."),
    ("Designit time", "Access to Designit strategists for two diagnostics in the first quarter, priced as a sales investment if necessary."),
    ("Solution architects", "A named pre-sales architect for Adobe and one for commerce, so that first pursuits are technically sound from the first meeting."),
    ("Alliance registration", "Early registration of opportunities with Adobe, Salesforce and SAP, so vendor co-sell support and funding are available."),
]


def build():
    cols = ""
    for i, (when, name, items, out) in enumerate(PHASES):
        li = "".join(f"<li>{E(x)}</li>" for x in items)
        cols += f'<div class="panel"><p class="k">{E(when)}</p><h3>{E(name)}</h3><ul>{li}</ul><p style="margin-top:14px"><b>Output.</b> {E(out)}</p></div>'
    met = table(["Measure", "Day 90", "Day 180", "Day 365"], [[E(a), (E(b), "n"), (E(c), "n"), (E(d), "n")] for a, b, c, d in METRICS], caption="Targets by day 90, 180 and 365")
    asks = '<div class="grid2">' + "".join(f'<div class="panel"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in ASKS) + "</div>"

    weekly = """<div class="grid3">
<div class="panel"><p class="k">Monday</p><p>Pipeline review of every opportunity over $1m. Trigger list refreshed from tech-stack scans, job posts and filings.</p></div>
<div class="panel"><p class="k">Tuesday to Thursday</p><p>Client meetings and client partner sessions, grouped by city to keep travel efficient. Solution and pricing reviews for live pursuits.</p></div>
<div class="panel"><p class="k">Friday</p><p>Points of view and proposals. Alliance calls. Forecast update within the variance Wipro expects.</p></div>
</div>"""

    body = (
        phead("Plan", "First 180 Days",
              "The first six months decide whether a matrix seller gets invited into accounts. This plan sets out what I would do in each period, what each period produces, and the measures I would ask to be held to.")
        + block("Phases", "Three phases", f'<div class="grid3">{cols}</div>')
        + block("Measures", "What I would be held to", met,
                "These targets assume the defaults on the Portfolio Maths page: a $25m annual bookings target, 60% from existing Wipro accounts, and a seven-month sales cycle. Day 365 bookings depend on inheriting some live pipeline.")
        + block("Rhythm", "A normal week", weekly)
        + block("Support", "What I would ask Wipro for", asks,
                "An overlay seller depends on resources owned by other teams. I would agree these four in the first two weeks.")
    )
    page("plan.html", body, "A 180-day plan for the Wipro DX Director role, with targets for days 90, 180 and 365.")
