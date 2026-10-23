from lib import *

POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"

# requirement, rating 0..2 (2 strong, 1 partial, 0 gap), evidence, how I close the gap
REQ = [
    ("10 to 15 years in professional services or technology", 2,
     "Eighteen years in professional services since 2008, at Rafael Viñoly Architects, WSP, SOM and Foster + Partners, plus Atlas Learn since 2025.", ""),
    ("5 to 7 years selling digital experience technology to North American C-suite", 1,
     "Sixteen years selling consulting to executives, including Fortune 500 chief executives, Wall Street banks and technology companies in North America. At Foster + Partners I co-created a service line that took the firm into digital transformation and spatial consulting. My selling has been design, advisory and transformation services, without DX platform services.",
     "Pair with a DX solution architect on every pursuit in the first two quarters, earn Adobe and Salesforce sales accreditations in the first 90 days, and lead with the design and advisory front end where my experience is direct."),
    ("Consultative selling", 2,
     "Every engagement I won started with the client's own data: carbon baselines, portfolio assessments, performance targets set against budgets and ESG commitments.", ""),
    ("Leading large transformation deals, $20m minimum", 1,
     "Led pitches, bids and competitions that won more than £10m a year in fees as Associate Partner. Won a multi-year contract with a global pharmaceutical company for a portfolio-wide plan. Presentations to Fortune 500 chief executives helped win contracts worth more than £10m. I have not closed a single $20m services contract.",
     "Use the deal ladder: build large deals from a small first phase plus run, with Wipro's deal desk and a leadership sponsor. I have structured multi-year programmes, and the run economics are Wipro's strength."),
    ("Managing a $20m to $25m portfolio", 1,
     "Held a fee target of more than £10m a year at Foster + Partners and more than $3m a year at SOM, across several clients and studios.",
     "Split the book into protect, expand and new logo targets in month one, and run the weekly pipeline and forecast rhythm on the Portfolio page."),
    ("Understanding of experience technology trends", 1,
     "Computational designer by training: scripting, simulation, Unreal Engine and digital twins. Co-founder of an AI training company that teaches executives to use Claude Code, Copilot Studio and other tools. This site is my working map of DX platforms, triggers and competitors.",
     "Deepen platform knowledge on Adobe, Salesforce, SAP Commerce and Pega through partner enablement in the first 90 days."),
    ("Communication and presentation", 2,
     "Presented at the COP26 Buildings Pavilion and UN COP28, chaired panels at Foster + Partners Earth Day and COP Week, taught at Imperial College London and City University of New York, and trained more than 250 senior professionals.", ""),
    ("Self-starter who learns quickly", 2,
     "Co-founded the Technology Group at Rafael Viñoly Architects, co-created a service line at Foster + Partners and co-founded Atlas Learn.", ""),
    ("Analytical skills", 2,
     "Building performance simulation, Python and C#, whole life carbon tools, and the models on the Pursuit and Portfolio pages of this site.", ""),
    ("Working in a matrix", 2,
     "Foster + Partners runs design studios, specialist groups and partners across many offices. As a specialist I won work for studios that owned the client, which is the practitioner model Wipro uses.", ""),
    ("Willingness to travel extensively", 2,
     "Projects in North America, Europe, the Middle East and Asia. US citizen, so I can work in the US without sponsorship.", ""),
]
RL = {2: ("Strong", "ok"), 1: ("Partial", "warn"), 0: ("Gap", "bad")}

MAP = [
    ("Co-created a strategic advisory service line at Foster + Partners covering environmental strategy, digital transformation and spatial consulting", "Originating a new offer inside a firm organised around design studios and delivery groups, the way DX works with Designit and the platform practices"),
    ("Won a multi-year plan for a global pharmaceutical company's property portfolio", "The land-and-expand ladder in life sciences, starting from a portfolio-wide assessment"),
    ("Presentations to Fortune 500 chief executives that helped studios win contracts worth more than £10m", "Being the specialist who helps the account owner win, which is the practitioner overlay"),
    ("Led department business development at SOM New York, presenting to Wall Street banks", "Overlay selling into banking, the largest Americas 2 sector"),
    ("Won more than $2m a year at WSP through cold and warm outreach", "Hunting for new logos"),
    ("Trained boards and executive teams on AI tools at Atlas Learn", "Credibility in AI-led experience conversations, where Wipro says client budgets are moving"),
    ("Set performance targets that fitted clients' budgets and ESG commitments", "Building value cases in the client's own numbers"),
]


def build():
    strong = sum(1 for r in REQ if r[1] == 2)
    part = sum(1 for r in REQ if r[1] == 1)
    rows = []
    for req, r, ev, close in REQ:
        lab, c = RL[r]
        rows.append([E(req), f'<span class="chip {c}">{lab}</span>', E(ev), E(close) if close else '<span class="muted">No gap to close</span>'])
    tbl = table(["Requirement in the posting", "Rating", "Evidence", "How I close the gap"], rows, caption="Requirements against evidence")

    bars = "".join(
        f'<div class="bar"><span class="lab">{E(l)}</span><span class="track"><span class="fill" style="width:{v/len(REQ)*100:.0f}%;background:var(--{c})"></span></span><span class="v">{v} of {len(REQ)}</span></div>'
        for l, v, c in [("Strong", strong, "ok"), ("Partial", part, "warn"), ("Gap", len(REQ) - strong - part, "bad")])

    mp = table(["What I did", "What it equals in this role"], [[E(a), E(b)] for a, b in MAP], caption="Experience mapped to the role")

    why = """<div class="grid3">
<div class="panel accent"><p class="k">The gap Gartner names</p><p>Gartner's 2025 DX Services report places Wipro as a Niche Player and cautions that 6% of its DX staff are creative and about 80% are in APAC. Wipro has the delivery scale. It is short of onshore people who lead the design and advisory conversation.</p></div>
<div class="panel accent"><p class="k">What I bring to it</p><p>I trained as an architect and computational designer and have spent eighteen years in design-led consulting in New York and London, sixteen of them selling to executives. I can open the conversation the way Designit would, then hand to Wipro's delivery model with a credible plan.</p></div>
<div class="panel accent"><p class="k">What I still need</p><p>Depth on DX platform services: Adobe, Salesforce, SAP Commerce and Pega. Wipro has that depth in its practices, and partner enablement and paired pursuits close it in my first two quarters.</p></div>
</div>"""

    body = (
        phead("Fit", "Fit and Evidence",
              f"This page rates my experience against each requirement in the <a href=\"{POST}\">posting</a>, with the evidence and, where the fit is partial, how I would close it. I have rated it as a hiring manager would. The partial ratings are real and are where an interview should probe.")
        + block("Summary", "Requirements at a glance", f'<div class="bars">{bars}</div>')
        + block("Argument", "Why a design-led seller fits Wipro now", why)
        + block("Detail", "Requirement by requirement", tbl)
        + block("Translation", "What my experience equals in this role", mp,
                "Net zero transformation and digital experience transformation are sold to similar buyers in similar ways. The table maps what I have done to the part of the role it prepares me for.")
    )
    page("fit.html", body, "Requirements in the Wipro DX posting rated against evidence, with gaps and how to close them.")
