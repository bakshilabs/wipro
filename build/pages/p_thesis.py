from lib import *

MQ = "https://research.oz.spotlightar.com/reports/magic-quadrant-digital-experience-services-2025/leaders"
Q2 = "https://www.wipro.com/investors/"
POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"

def postings_vis():
    pts = [("Jul", "This role", 0), ("Aug", "Energy", 1), ("Sep", "Retail, life sciences", 2), ("Oct", "Enterprise", 3)]
    o = ['<svg viewBox="0 0 520 110" aria-hidden="true">', '<line x1="30" x2="490" y1="40" y2="40" stroke="var(--line)" stroke-width="2"/>',
         '<line class="draw" style="--len:460" x1="30" x2="490" y1="40" y2="40" stroke="var(--accent)" stroke-width="3"/>']
    for m, lab, i in pts:
        x = 30 + i * 153
        o.append(f'<circle class="pop" style="transition-delay:{.3+i*.25}s" cx="{x}" cy="40" r="11" fill="var(--accent)"/>')
        o.append(f'<text x="{x}" y="16" text-anchor="middle" font-size="14" font-weight="600" class="svg-ink">{m}</text>')
        o.append(f'<text x="{x}" y="74" text-anchor="{"start" if i==0 else "end" if i==3 else "middle"}" font-size="12.5" class="svg-muted">{lab}</text>')
    o.append("</svg>")
    return "".join(o)


def smu_vis():
    d = [("Americas 1", 34.4, "-2.7%", "c0"), ("Americas 2", 25.6, "-4.7%", "c1"), ("Europe", 27.4, "+5.1%", "c6"), ("APMEA", 12.6, "+13.3%", "c6")]
    o = ['<svg viewBox="0 0 520 96" aria-hidden="true">']
    x = 0
    for lab, v, g, c in d:
        w = 520 * v / 100
        op = 1 if c != "c6" else .35
        o.append(f'<rect class="grow" x="{x:.1f}" y="10" width="{w-3:.1f}" height="34" rx="3" fill="var(--{c})" opacity="{op}"/>')
        o.append(f'<text x="{516 if lab == "APMEA" else x+4:.1f}" y="66" font-size="13" font-weight="600" class="svg-ink" text-anchor="{"end" if lab == "APMEA" else "start"}">{lab}</text>')
        col = "var(--bad)" if g.startswith("-") else "var(--ok)"
        last = lab == "APMEA"
        o.append(f'<text x="{516 if last else x+4:.1f}" y="86" font-size="12.5" fill="{col}" text-anchor="{"end" if last else "start"}">{g} YoY</text>')
        x += w
    o.append("</svg>")
    return "".join(o)


def waffle():
    o = ['<svg viewBox="0 0 300 140" aria-hidden="true">']
    for k in range(100):
        r, c = divmod(k, 20)
        on = k < 6
        avg = 6 <= k < 9
        fill = "var(--accent)" if on else "none"
        stroke = "var(--accent)" if avg else "var(--line)"
        o.append(f'<rect class="{"pop" if on else ""}" style="transition-delay:{k*.08:.2f}s" x="{c*15}" y="{r*15}" width="12" height="12" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="{1.6 if avg else 1}"/>')
    o.append('<text x="0" y="98" font-size="12.5" class="svg-muted"><tspan fill="var(--accent)" font-weight="600">6 Wipro</tspan> against a market average of 9 in every 100 DX staff</text>')
    o.append("</svg>")
    return "".join(o)


def deadline_vis():
    ev = [("Feb", "AEM 6.5 on-premises support ends", 1), ("Apr", "ADA Title II web rule", 3), ("May", "HHS Section 504 web rule", 4), ("Dec", "Sitecore 10.4 support ends", 11)]
    o = ['<svg viewBox="0 0 620 130" aria-hidden="true"><line x1="10" x2="610" y1="34" y2="34" stroke="var(--line)" stroke-width="2"/>']
    for m in range(12):
        x = 10 + m * 600 / 11
        o.append(f'<line x1="{x:.0f}" x2="{x:.0f}" y1="29" y2="39" stroke="var(--line)"/>')
    for i, (m, lab, mo) in enumerate(ev):
        x = 10 + mo * 600 / 11
        o.append(f'<circle class="pop" style="transition-delay:{.2+i*.2}s" cx="{x:.0f}" cy="34" r="10" fill="var(--c2)"/>')
        o.append(f'<text x="{x:.0f}" y="14" text-anchor="middle" font-size="13" font-weight="600" class="svg-ink">{m}</text>')
        y = 64 + [0, 1, 2, 0][i] * 22
        anc = "start" if i in (0, 1, 2) else "end"
        x = x - 8 if anc == "start" else x
        o.append(f'<text x="{x:.0f}" y="{y}" text-anchor="{anc}" font-size="12.5" class="svg-muted">{lab}</text>')
    o.append("</svg>")
    return "".join(o)


def argument():
    steps = [("The gap", "Gartner rates Wipro a Niche Player in DX. The reason is a thin creative, onshore front end.", "c2"),
             ("The fit", "Architect and computational designer. Sixteen years selling design-led consulting to Fortune 500 executives.", "c0"),
             ("The result", "Design-led entry deals that grow into multi-year runs at Wipro's scale.", "c3")]
    o = ['<svg viewBox="0 0 1100 300" role="img" aria-label="The gap, the fit, the result"><defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--muted)"/></marker></defs>']
    for i, (h, p, c) in enumerate(steps):
        cx = 170 + i * 380
        o.append(f'<circle class="pop" style="transition-delay:{i*.3}s" cx="{cx}" cy="110" r="92" fill="none" stroke="var(--{c})" stroke-width="3"/>')
        o.append(f'<circle class="pop" style="transition-delay:{i*.3+.1}s" cx="{cx}" cy="110" r="78" fill="var(--{c})" opacity=".14"/>')
        o.append(f'<text x="{cx}" y="118" text-anchor="middle" font-size="27" font-weight="700" class="svg-ink">{h}</text>')
        if i < 2:
            o.append(f'<line class="draw" style="--len:160;transition-delay:{.4+i*.3}s" x1="{cx+104}" x2="{cx+276}" y1="110" y2="110" stroke="var(--muted)" stroke-width="2" marker-end="url(#ah)"/>')
    o.append("</svg>")
    caps = "".join(f'<div class="rv d{i+1}"><p class="lead" style="margin:0 auto;max-width:18em;font-size:17px">{E(p)}</p></div>' for i, (h, p, c) in enumerate(steps))
    return "".join(o) + f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:8px">{caps}</div>'


CLAIMS = [
    ("Growth", "Wipro needs new Americas pipeline", "The Americas carry 60% of Wipro's revenue, and both Americas units shrank year on year in the latest quarter while Europe and APMEA grew. Wipro posted four US DX seller roles between July and October 2026, one per industry cluster. I read that as a bet that DX can open new conversations in accounts where Wipro already runs IT.",
     "smu", "operating-model.html", "Operating Matrix"),
    ("Gap", "The weakness is the front end", "Gartner places Wipro as a Niche Player in DX Services. The stated reasons are a thin creative bench (6% of DX staff against a market average of about 9%) and a delivery base that is about 80% in APAC. Everest rates Wipro a Leader in Salesforce services. Wipro loses ground at the first conversation with a CMO or CDO, which needs design-led people in the client's time zone.",
     "waffle", "market.html", "Market and Competitors"),
    ("Timing", "2027 gives buyers a date", "Adobe Experience Manager 6.5 on-premises support ends in February 2027. The ADA Title II and HHS Section 504 web accessibility rules take effect in April and May 2027, and Sitecore 10.4 support ends in December 2027. These dates fall on Wipro's focus industries and turn a capability pitch into a decision with a deadline.",
     "deadline", "triggers.html", "Buying Triggers"),
]

DISCUSS = [
    "Do clients raise the Gartner placement with you, and how does the team answer it today?",
    "Of the four DX seller roles posted since July, which are filled, and how are accounts divided between them?",
    "Where has DX won in the Americas this year, and what did the first deal look like?",
]


def build():
    vis = {"smu": smu_vis, "waffle": waffle, "deadline": deadline_vis}
    body = hero("Thesis", "Three Claims", "What I think the role is for. I would like to hear where you see it differently.")
    for i, (k, h, p, v, href, lab) in enumerate(CLAIMS):
        num_html = {"smu": num(60, suf="%", small=" of revenue"), "waffle": num(6, suf="%", small=" creative staff"), "deadline": num(2027)}[v]
        left = f'<p class="t-k">Claim {i+1} · {E(k)}</p>{num_html}<h3>{E(h)}</h3><p>{E(p)}</p><span class="go">{E(lab)}</span>'
        right = f'<div class="vis" style="margin-top:0;padding-top:0">{vis[v]()}</div>'
        if v == "smu":
            right += f'<div class="vis">{postings_vis()}</div><p>Four US DX seller postings, July to October 2026.</p>'
        inner = f'<div class="bento">{tile(left, 6, href=href)}{tile(right, 6)}</div>' 
        body += sec(head_block(f"Claim {i+1}", k, "") + inner, "grey" if i == 1 else "")
    body += sec(head_block("Argument", "Gap, Fit, Result", "Why a design-led seller, and why now.") + f'<div class="art rv">{argument()}</div>', "dark", center=True)
    q = "".join(f"<li>{E(x)}</li>" for x in DISCUSS)
    body += sec(head_block("Discussion", "Questions for You", "Where I would like your correction.") + f'<ol class="disc rv">{q}</ol>'
                + f'<p class="fine">The Gartner placement comes from a secondary reproduction of the 2025 Magic Quadrant (<a href="{MQ}">Spotlight AR</a>) and should be checked against the Gartner document. Revenue shares are from Wipro quarterly results. The full analysis is in the <a href="research.html">research appendix</a>.</p>', "grey")
    page("thesis.html", body, "Three claims about why Wipro is hiring a design-led DX seller in the Americas, with questions for discussion.")
