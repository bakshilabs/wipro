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


SHORTREQ = ["10 to 15 years in services", "5 to 7 years selling DX to C-suite", "Consultative selling", "Large deals, $20m minimum", "$20m to $25m portfolio",
            "Experience technology trends", "Communication", "Self-starter", "Analytical", "Matrix working", "Travel"]


def ring():
    import math
    cx, cy, R, r = 300, 300, 260, 170
    n = len(REQ)
    o = ['<svg viewBox="0 0 600 600" role="img" aria-labelledby="rt rd"><title id="rt">Requirements rated against evidence</title><desc id="rd">Eleven segments, seven strong and four partial. Select a segment for its evidence.</desc>']
    gap = .025
    for k, (req, rt, ev, close) in enumerate(REQ):
        a0 = -math.pi / 2 + k * 2 * math.pi / n + gap
        a1 = -math.pi / 2 + (k + 1) * 2 * math.pi / n - gap
        pth = (f"M{cx+R*math.cos(a0):.1f} {cy+R*math.sin(a0):.1f} A{R} {R} 0 0 1 {cx+R*math.cos(a1):.1f} {cy+R*math.sin(a1):.1f} "
               f"L{cx+r*math.cos(a1):.1f} {cy+r*math.sin(a1):.1f} A{r} {r} 0 0 0 {cx+r*math.cos(a0):.1f} {cy+r*math.sin(a0):.1f}Z")
        col = "var(--ok)" if rt == 2 else "var(--warn)"
        am = (a0 + a1) / 2
        o.append(f'<g data-pick="r{k}" aria-label="{E(SHORTREQ[k])}"><path class="pop" style="transition-delay:{k*.06:.2f}s" d="{pth}" fill="{col}" stroke="transparent"/>'
                 f'<text x="{cx+(R+r)/2*math.cos(am):.0f}" y="{cy+(R+r)/2*math.sin(am)+6:.0f}" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">{k+1}</text></g>')
    st = sum(1 for x in REQ if x[1] == 2)
    o.append(f'<text x="{cx}" y="{cy-10}" text-anchor="middle" font-size="88" font-weight="700" class="svg-ink">{st}/{n}</text><text x="{cx}" y="{cy+34}" text-anchor="middle" font-size="20" class="svg-muted">strong</text>')
    o.append("</svg>")
    return "".join(o)


def build():
    data = {}
    for k, (req, rt, ev, close) in enumerate(REQ):
        lab = "Strong" if rt == 2 else "Partial"
        cls = "ok" if rt == 2 else "warn"
        data[f"r{k}"] = (f'<p class="t-k">Requirement {k+1} · <span class="tag {cls}">{lab}</span></p><h3>{E(req)}</h3><p><b>Evidence</b> {E(ev)}</p>'
                         + (f'<p><b>How I close the gap</b> {E(close)}</p>' if close else ""))
    st = sum(1 for x in REQ if x[1] == 2)
    art = explorer(f'<div class="art s" style="margin-top:0">{ring()}</div>', data, "Select a segment to see the evidence.", first="r1")
    body = hero("Fit and Evidence", f"{st} Strong, {len(REQ)-st} Partial", "Every requirement in the posting, rated as a hiring manager would. The partial ones are where the interview should probe.", art)

    why = (tile(f'<p class="t-k">The gap Gartner names</p>{num(80, suf="%")}<h3>of Wipro DX staff are in APAC</h3><p>And 6% are creative. Wipro has delivery scale and is short of onshore people who lead the design conversation.</p>', 4)
           + tile(f'<p class="t-k">What I bring</p>{num(18)}<h3>years in design-led consulting</h3><p>Architect and computational designer. Sixteen years selling to executives in New York and London.</p>', 4)
           + tile(f'<p class="t-k">What I still need</p>{num(2)}<h3>quarters to close it</h3><p>Platform depth on Adobe, Salesforce, SAP Commerce and Pega through enablement and paired pursuits.</p>', 4))
    body += sec(head_block("Argument", "Why Now", "A design-led seller fixes the weakness analysts name.") + f'<div class="bento">{why}</div>', "grey")

    rows = ""
    for k, (a, b) in enumerate(MAP):
        rows += (f'<div class="rv d{k%4+1}" style="display:grid;grid-template-columns:1fr 60px 1fr;gap:16px;align-items:center;margin-top:18px">'
                 f'<div class="tile" style="min-height:0"><p class="t-k">What I did</p><p style="color:var(--ink);font-size:17px">{E(a)}</p></div>'
                 f'<svg viewBox="0 0 60 24" aria-hidden="true"><path d="M4 12h44" stroke="var(--accent)" stroke-width="2.5"/><path d="M44 5l10 7-10 7" fill="none" stroke="var(--accent)" stroke-width="2.5"/></svg>'
                 f'<div class="tile" style="min-height:0"><p class="t-k" style="color:var(--accent)">What it equals here</p><p style="color:var(--ink);font-size:17px">{E(b)}</p></div></div>')
    rws = []
    for req, r, ev, close in REQ:
        lab, c = RL[r]
        rws.append([E(req), f'<span class="chip {c}">{lab}</span>', E(ev), E(close) if close else '<span class="muted">No gap to close</span>'])
    tbl = table(["Requirement", "Rating", "Evidence", "How I close the gap"], rws, caption="Requirements against evidence")
    body += sec(head_block("Translation", "What It Equals", "Seven things I have done, mapped to the part of the role they prepare me for.") + f'<div style="margin-top:40px">{rows}</div>' + more("Show the full requirements table", tbl), "dark")
    page("fit.html", body, "Requirements in the Wipro DX posting rated against evidence, with gaps and how to close them.")
