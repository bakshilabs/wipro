from lib import *

POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"

CARDS = [
    ("role.html", "Role", "Role Anatomy", "The posting decoded line by line, compared with three related Wipro postings, and the person it describes.", True),
    ("operating-model.html", "Matrix", "Operating Matrix", "Where DX sits among Wipro's market units and business lines, who the role depends on and what Wipro's results ask of it.", False),
    ("market.html", "Market", "Market and Competitors", "Market size, budget shifts, analyst ratings, positioning and how to answer Wipro's weak points.", False),
    ("triggers.html", "Triggers", "Buying Triggers", "Twenty-five dated platform, regulation and AI triggers from 2025 to 2028, with the signals that reveal affected clients.", False),
    ("accounts.html", "Accounts", "Account Map", "Twenty-four target accounts by fit and route in, each with its trigger and my first move.", False),
    ("pursuit.html", "Pursuit", "Pursuit Model", "A weighted qualification scorecard and a deal ladder that shows how a design phase grows into a $20m deal.", False),
    ("portfolio.html", "Portfolio", "Portfolio Maths", "A calculator that turns a $25m bookings target into pipeline, opportunities and meetings per month.", False),
    ("plan.html", "Plan", "First 180 Days", "What I would do in each period, what it produces and the measures I would be held to.", False),
    ("fit.html", "Fit", "Fit and Evidence", "Each requirement in the posting rated against my evidence, with the gaps and how I would close them.", False),
]

IDEAS = [
    ("Client partners are the first customer", "The practitioner does not own accounts. Every opportunity starts by giving a client partner a reason to open the door: a dated trigger, a point of view and a sized idea that grows their number."),
    ("Sell the deadline", "AEM 6.5 on-premises support ends in February 2027. The ADA Title II web rule applies from April 2027, and HHS Section 504 from May 2027. A dated event turns a capability pitch into a decision the client has to make."),
    ("Land with design, expand to run", "A Designit-led diagnostic under $1m opens the door. The build and the multi-year managed run that follow make it a $20m deal, and they play to Wipro's delivery scale."),
]


def build():
    cards = "".join(
        f'<a class="pcard{" feature" if f else ""}" href="{h}"><span class="eyebrow">{E(e)}</span><h3>{E(t)}</h3><p>{E(d)}</p><span class="go">Open page</span></a>'
        for h, e, t, d, f in CARDS)
    stats = """<div class="stats">
<div class="stat"><b>4</b><span>US DX practitioner roles Wipro posted between July and October 2026, on one template and one pay band</span><small><a href="role.html">Role Anatomy</a></small></div>
<div class="stat"><b>60%</b><span>Share of Wipro revenue from the Americas, where both market units shrank year on year in Q2 FY27</span><small><a href="operating-model.html">Operating Matrix</a></small></div>
<div class="stat"><b>6%</b><span>Share of Wipro's DX staff that is creative, which Gartner cites in rating Wipro a Niche Player</span><small><a href="market.html">Market and Competitors</a></small></div>
<div class="stat"><b>2027</b><span>The year platform support deadlines and US accessibility rules converge on Wipro's focus industries</span><small><a href="triggers.html">Buying Triggers</a></small></div>
</div>"""
    ideas = '<div class="grid3">' + "".join(f'<div class="panel"><p class="k">Idea {i+1}</p><h3>{E(a)}</h3><p>{E(b)}</p></div>' for i, (a, b) in enumerate(IDEAS)) + "</div>"

    reading = """<div class="prose">
<p>The posting asks for a seller who can originate large experience transformation deals inside accounts that other people own. Wipro has posted four roles like it in four months, one for each cluster of industries, at a time when its Americas revenue is shrinking and its large-deal bookings fell by more than half in a quarter. The role is a growth bet, and the people hiring will judge it on pipeline within two quarters.</p>
<p>Wipro brings delivery scale, a design company in Designit, strong Salesforce, Pega and ServiceNow practices, and AI platforms under Wipro Intelligence. Analysts mark it down for its thin creative and onshore presence at the front of a deal. A seller who can lead the design and advisory conversation with a CMO, then hand over to Wipro's delivery model with a credible plan, addresses that weakness directly.</p>
<p>That is the case I make on these pages. I have sold design-led consulting to Fortune 500 executives for sixteen years, built a new service line inside a matrix of studios, and won multi-year portfolio work in life sciences. I have not sold DX platform services, and the Fit page says so and sets out how I would close that gap.</p>
</div>"""

    body = (
        f'<section class="hero wrap"><p class="eyebrow">Wipro, Director, Digital Experience (DX)</p><h1 style="margin-top:16px">Digital Experience Director</h1>'
        f'<p class="lede">A working study of the <a href="{POST}">Director, Digital Experience</a> role: how it works inside Wipro\'s matrix, the market and buying triggers for 2026 to 2028, where I would start and how I would build a $25m book.</p>'
        '<p class="meta">Prepared by Arpan Bakshi, 23 October 2026. All figures are from public sources cited on each page.</p></section>'
        + block("Findings", "Four numbers that frame the role", stats)
        + block("Reading", "How I read the role", reading)
        + block("Approach", "Three ideas behind the plan", ideas)
        + block("Pages", "The study", f'<div class="cards">{cards}<a class="pcard" href="cv.html"><span class="eyebrow">CV</span><h3>CV</h3><p>My CV, ordered for this role, with business development first. Printable to A4.</p><span class="go">Open page</span></a></div>')
        + '<section class="wrap notes"><h3>Sources and limits</h3><p>Wipro facts come from its careers site, quarterly results, earnings call transcripts, annual report and stock exchange filings. Analyst placements come partly from secondary reproductions of Gartner and Everest reports and should be checked against the originals. Fit scores, deal ladder rates and pipeline ratios are my own working assumptions and are labelled as such. The research notes behind each page are kept in the repository.</p></section>'
    )
    page("overview.html", body, "A study of the Wipro Director, Digital Experience role by Arpan Bakshi.")
