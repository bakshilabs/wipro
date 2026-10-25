from lib import *
from pages.p_fit import REQ

# title, firm and years, situation, what I did, result, what it means at Wipro
STORIES = [
    ("A new service line inside a matrix", "Foster + Partners, 2020 to 2026",
     "The firm sold buildings through design studios that owned each client. Clients were asking for advice that came before a building: environmental strategy, digital transformation and how to use their space.",
     "Co-created a strategic advisory service line and sold it into clients that the studios owned. I had no accounts of my own, so every opportunity started by giving a studio partner a reason to bring me in.",
     "The service line took the firm into corporate environmental strategy, digital transformation and spatial consulting. As Associate Partner I led pitches and bids that won more than £10m a year in fees.",
     "This is the practitioner overlay. An SMU client partner owns the account, DX carries the number, and the seller earns access by growing the client partner's business."),
    ("Land and expand in life sciences", "Foster + Partners",
     "A global pharmaceutical company wanted a single sustainability vision for its whole property portfolio, tied to its corporate commitments.",
     "Pitched, negotiated and won a multi-year contract to write the sustainability vision plan for the whole portfolio, starting from an assessment of the client's own data.",
     "A multi-year contract covering the whole portfolio, for a client in one of Wipro's DX focus industries.",
     "The deal ladder: an assessment in the client's own numbers that opens a multi-year programme."),
    ("Helping the account owner win", "Foster + Partners and SOM",
     "Large competitions are won or lost in a few executive presentations. The studio partner owns the relationship but needs a specialist who can make the technical case to a chief executive.",
     "Presented to Fortune 500 chief executives for the design studios, and at SOM New York led business development for my department, presenting to executives at Wall Street banks.",
     "My presentations helped the studios win contracts worth more than £10m. At SOM I won more than $3m a year in fees.",
     "Selling into Americas 2 banking and Americas 1 health accounts alongside a client partner, with the specialist case made to a CDO or CMO."),
]

NUMS = [("16", "", "", "years selling consulting to executives"), ("10", "£", "m", "a year in fees won as Associate Partner"),
        ("250", "", "", "senior professionals trained on AI tools"), ("4", "", "", "regions of project work, and a US citizen")]

# the partial requirements from the fit assessment, in plain terms
GAPS = [
    ("DX platform selling", "My selling has been design, advisory and transformation services. I have not sold Adobe, Salesforce or commerce platform services.", REQ[1][3]),
    ("A single $20m deal", "My largest wins were multi-year advisory contracts and studio fees of more than £10m a year in total. I have not closed one $20m services contract.", REQ[3][3]),
    ("A $25m book", "I have held fee targets of more than £10m a year at Foster + Partners and more than $3m a year at SOM, across several clients and studios.", REQ[4][3]),
]

DISCUSS = [
    "Which of these three stories is closest to the accounts you would give this role?",
    "How would you weigh platform selling experience against a design-led front end in this hire?",
    "Who on the DX team would I pair with on the first pursuits?",
]


def build():
    nums = "".join(tile(f'{num(n, pre=p, suf=x)}<p>{E(l)}</p>', 3, "short") for n, p, x, l in NUMS)
    body = hero("Track Record", "Three Stories", "Sixteen years selling design-led consulting to executives. Three stories that match the work, and the three gaps I would close first.")
    body += sec(head_block("In numbers", "Sixteen Years", "Architect and computational designer by training. Seller by practice since 2010.") + f'<div class="bento">{nums}</div>', "grey")

    for i, (t, firm, sit, did, res, wip) in enumerate(STORIES):
        parts = [("Situation", sit), ("What I did", did), ("Result", res)]
        cols = "".join(f'<div class="tile short" style="min-height:0"><p><small>{E(k)}</small>{E(v)}</p></div>' for k, v in parts)
        inner = f'<div class="story rv">{cols}</div><div class="bento" style="margin-top:20px">{tile(f"<p class=\"t-k\">What it means at Wipro</p><h3>{E(wip)}</h3>", 12, "short feature")}</div>'
        body += sec(head_block(f"Story {i+1} · {firm}", t, "") + inner, "grey" if i == 1 else "")

    gt = "".join(tile(f'<p class="t-k"><span class="tag warn">Partial</span></p><h3>{E(h)}</h3><p><b>Today</b> {E(now)}</p><p><b>Plan</b> {E(close)}</p>', 4) for h, now, close in GAPS)
    body += sec(head_block("Gaps", "Where to Probe", "Seven of eleven requirements in the posting are strong. These three partial ones carry the most weight.") + f'<div class="bento">{gt}</div>'
                + '<p class="fine">Every requirement is rated with its evidence on <a href="fit.html">Fit and Evidence</a> in the appendix. The full history is in the <a href="cv.html">CV</a>.</p>', "dark")

    q = "".join(f"<li>{E(x)}</li>" for x in DISCUSS)
    body += sec(head_block("Discussion", "Questions for You", "") + f'<ol class="disc rv">{q}</ol>', "grey")
    page("record.html", body, "Three stories from Arpan Bakshi's consulting sales career mapped to the Wipro DX role, with the gaps to probe.")
