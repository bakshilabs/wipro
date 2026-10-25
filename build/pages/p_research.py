from lib import *

# file, icon, what it holds, meeting pages it supports
GROUPS = [
    ("Role and organisation", [
        ("role.html", "grid", "The posting decoded line by line, four related Wipro postings compared, where the week goes, and the person it describes.", "Thesis, Track Record"),
        ("operating-model.html", "people", "Wipro's market units and business lines, where DX sits, seven stakeholder groups, pursuit roles and how the role is measured.", "Thesis, Sample Deal"),
    ]),
    ("Market and demand", [
        ("market.html", "chart", "DX market size, CMO budget shifts, analyst ratings, five competitors and how to sell against each, and objections answered.", "Thesis"),
        ("triggers.html", "calendar", "Twenty-five dated triggers from 2025 to 2028: platform support ends, accessibility and privacy rules, corporate events and agentic commerce.", "Thesis, Sample Deal"),
        ("accounts.html", "target", "Twenty-four target accounts by fit and route in, each with a trigger, sources and the first move.", "First Year, Sample Deal"),
    ]),
    ("Models", [
        ("pursuit.html", "ladder", "An interactive nine-criterion pursuit scorecard and a deal ladder calculator that shows how DX deals reach $20m.", "Sample Deal"),
        ("portfolio.html", "bolt", "An interactive calculator from a bookings target to pipeline, wins and meetings, with the operating rhythm.", "First Year"),
    ]),
    ("Detail", [
        ("plan.html", "door", "Every action in the first 180 days, nine milestones, targets for day 90, 180 and 365, and four asks.", "First Year"),
        ("fit.html", "shield", "Each requirement in the posting rated against evidence, with the gaps and how I would close them.", "Track Record"),
    ]),
]

CHECKS = [
    "The Gartner Magic Quadrant placements come mainly from a secondary reproduction and should be checked against the Gartner document.",
    "The reporting line from the DX practice to Enterprise Applications and Technology Services is inferred from public job titles.",
    "Deal ladder rates ($170 onshore, $35 offshore), win rates and meeting ratios are my assumptions, not Wipro data.",
    "Account fit scores are my judgement. Names of Wipro leaders come from LinkedIn and company filings.",
]


def build():
    body = hero("Research Appendix", "Nine Pages", "The working analysis behind the meeting pages. I would open these only when a question needs the detail.")
    for gi, (g, items) in enumerate(GROUPS):
        cards = "".join(tile(f'{icon(i)}<h3 style="margin-top:22px">{E(TITLES[f])}</h3><p>{E(d)}</p><p class="small muted"><b>Supports</b> {E(u)}</p><span class="go">Open</span>', 12 // len(items) if len(items) > 1 else 6, href=f)
                        for f, i, d, u in items)
        body += sec(head_block(f"Group {gi+1}", g, "") + f'<div class="bento">{cards}</div>', "grey" if gi % 2 == 0 else "")
    ch = "".join(f"<li>{E(x)}</li>" for x in CHECKS)
    body += sec(head_block("Caveats", "Checks Before Quoting", "Where the research rests on secondary sources or my own assumptions.") + f'<ol class="disc rv">{ch}</ol>', "dark")
    page("research.html", body, "Index of the research appendix behind the Wipro DX interview pages: role, matrix, market, triggers, accounts, models, plan and fit.")
