from lib import *
import json, os

D = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "accounts.json")))

SHORT = {
    "Roche / Genentech": "Roche and Genentech", "ESPN (The Walt Disney Company)": "ESPN", "Kenvue (to be acquired by Kimberly-Clark)": "Kenvue",
    "Kellanova (Mars)": "Kellanova and Mars", "Kraft Heinz (Global Taste Elevation Co. / North American Grocery Co.)": "Kraft Heinz",
    "DICK'S Sporting Goods (incl. Foot Locker)": "DICK'S Sporting Goods", "DePuy Synthes (J&J Orthopaedics separation)": "DePuy Synthes",
    "MiniMed (Medtronic Diabetes)": "MiniMed", "BD (Becton, Dickinson)": "BD", "Eli Lilly (LillyDirect)": "Eli Lilly", "Pfizer (PfizerForAll)": "Pfizer",
    "Fifth Third Bancorp (incl. Comerica)": "Fifth Third", "Capital One (incl. Discover)": "Capital One",
    "Stellantis North America": "Stellantis", "Levi Strauss & Co.": "Levi Strauss", "Hyundai Motor America": "Hyundai Motor America",
}
# corrections from the trigger research, which is more recent than the account file for these two
OVERRIDE = {
    "Kraft Heinz (Global Taste Elevation Co. / North American Grocery Co.)": {"trigger": "New CEO paused the planned split on 11 February 2026 and moved $600m into marketing, sales and R&D", "trigger_date": "2026-02-11", "sources": ["https://www.supermarketnews.com/mergers-acquisitions/kraft-heinz-pauses-plans-to-split-into-2-companies"]},
}
# my opening move and the Wipro entry offer for each account
MOVES = {
    "Roche / Genentech": ("Ask my former Roche and Genentech property clients for introductions to Genentech's digital marketing office. Open with an assessment of their Adobe Experience Cloud content supply chain.", "Content supply chain and omnichannel diagnostic, then Adobe run"),
    "Hyundai Motor America": ("Use my Hyundai relationship to reach the US marketing team that owns the CRM, consumer site and online buying, and propose a review of the Amazon and dealer buying journey.", "Digital retail journey audit, then platform and CRM build"),
    "Citigroup": ("Work through the Wipro client partner. Bring a wealth client experience point of view to the new marketing organisation, priced so it does not add contractor headcount.", "Wealth experience redesign on outcome pricing"),
    "JPMorgan Chase": ("Target a scoped piece where the bank buys outside help, such as Chase Travel or the international digital bank, through contacts from the JPMorgan headquarters project.", "Scoped experience build with Designit"),
    "ESPN (The Walt Disney Company)": ("Keep warm through my ESPN contacts and pass to the media sector team. The work is real but mostly built in-house.", "Commerce and personalisation support"),
    "Kenvue (to be acquired by Kimberly-Clark)": ("Reach the integration office before close with a plan to consolidate the two brand portfolios' sites, DTC stores and martech onto one estate.", "Digital estate consolidation programme"),
    "Kellanova (Mars)": ("Approach Mars Snacking's digital team with a costed plan to fold Kellanova's brand sites and martech into the Mars estate.", "Brand site and martech integration"),
    "Kraft Heinz (Global Taste Elevation Co. / North American Grocery Co.)": ("Follow the $600m reinvestment into marketing with a proposal for AI content production and DTC commerce that shows a return within the year.", "AI content operations and commerce"),
    "Walgreens": ("Each standalone unit needs its own digital estate on a private-equity timeline. Lead with a managed DX model that cuts run cost.", "Carve-out digital estate on managed run"),
    "DICK'S Sporting Goods (incl. Foot Locker)": ("Offer a multi-banner commerce architecture review as the Foot Locker integration moves into its second year.", "Composable commerce roadmap and build"),
    "Target": ("Watch the Enterprise Acceleration Office for outsourced scope. Large in-house engineering makes this a later target.", "Agentic commerce readiness"),
    "Medline": ("A newly public B2B supplier with a heavy customer portal and ordering load. Lead with a B2B commerce and portal experience benchmark.", "B2B commerce and portal modernisation"),
    "DePuy Synthes (J&J Orthopaedics separation)": ("The separation needs a full new web, HCP portal, commerce and martech estate by about 2027. Reach the separation CIO and CMO with a dated plan.", "Separation digital estate with managed run"),
    "MiniMed (Medtronic Diabetes)": ("The patient app, e-commerce and support estate must leave Medtronic's systems within the transition period. Smaller deal, clear deadline.", "Patient experience and commerce exit from TSA"),
    "BD (Becton, Dickinson)": ("Both sides of the Waters deal re-scope their digital estates. Offer BD a pure-play medtech brand and portal refresh.", "Brand and HCP portal rebuild"),
    "Solventum": ("The ERP cutover is ending. The commercial and customer experience layer is the next investment. Time the approach for the post-cutover budget.", "Commercial experience layer on new ERP"),
    "Eli Lilly (LillyDirect)": ("Direct-to-patient demand is real, but Lilly already partners with Amazon and telehealth firms. Look for a specific gap such as accessibility or pricing pages.", "Accessibility and DTC optimisation"),
    "Pfizer (PfizerForAll)": ("TrumpRx routes patients to manufacturer sites. Bring a checkout and pricing experience benchmark against other DTC pharma sites.", "DTC commerce optimisation"),
    "Fifth Third Bancorp (incl. Comerica)": ("After the Labor Day 2026 conversion, Comerica customers in new markets judge the bank on the digital experience. Offer a post-conversion experience review.", "Post-merger CX optimisation"),
    "Capital One (incl. Discover)": ("Strong in-house engineering. Hold unless a scoped need appears.", "Hold"),
    "Stellantis North America": ("New Ram and Jeep brand chiefs with digital retail backgrounds. Reach them in their first 90 days with a digital retail journey audit.", "Digital retail and dealer experience"),
    "Levi Strauss & Co.": ("Existing Wipro digital commerce client. Expand into experience design and AI personalisation through the account team.", "AI personalisation on the existing estate"),
    "HanesBrands": ("Wipro runs AI-led IT managed services. Use that access to reach DTC and e-commerce leaders.", "DTC experience and commerce"),
    "TruStage": ("A live Designit and Wipro reference. Use it as the case study for financial services pursuits.", "Reference client"),
    "Oracle": ("A Wipro partner, not a buyer. Use for Oracle CX and commerce co-selling.", "Co-sell lever"),
    "Apple": ("A Wipro partner, not a buyer. Useful for medical device and field service mobile experiences.", "Co-sell lever"),
}
SMU = {"Life Sciences": "Americas 1", "MedTech": "Americas 1", "Media & Entertainment": "Americas 1", "Technology": "Americas 1",
       "Banking": "Americas 2", "Financial Services": "Americas 2", "Automotive": "Americas 2"}
REL = {"existing candidate relationship": ("My relationship", "c0"), "Wipro client": ("Wipro client", "c3"), "new logo": ("New logo", "c2")}


def smu(ind):
    if ind.startswith("Retail"):
        return "Americas 1"
    return SMU.get(ind, "")


def industry(ind):
    return "Retail and consumer" if ind.startswith("Retail") else ind.replace("&", "and")


def build():
    rows = []
    for a in D:
        a = dict(a, **OVERRIDE.get(a["company"], {}))
        if a["company"] in ("Oracle", "Apple"):
            continue
        rows.append(a)
    rows.sort(key=lambda a: (-a["fit_score_1to5"], {"existing candidate relationship": 0, "Wipro client": 1, "new logo": 2}[a["relationship"]]))

    # scatter: x = access, y = fit
    acc = {"existing candidate relationship": 2, "Wipro client": 1, "new logo": 0}
    W, H, L, B = 1000, 470, 70, 410
    cols = 3
    cw = (W - L - 20) / cols
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="at ad"><title id="at">Target accounts by fit and route in</title><desc id="ad">{len(rows)} accounts placed by fit score from one to five and by route in: new logo, Wipro client, or my existing relationship.</desc>']
    for k, lab in enumerate(["New logo", "Wipro client (expand)", "My existing relationship"]):
        x = L + k * cw
        o.append(f'<rect x="{x+4}" y="10" width="{cw-8}" height="{B-10}" rx="4" fill="var(--surface)"/>')
        o.append(f'<text x="{x+cw/2}" y="{B+30}" text-anchor="middle" font-size="13" class="svg-ink" font-weight="600">{lab}</text>')
    for s in range(1, 6):
        y = B - (s - 0.5) * (B - 10) / 5
        o.append(f'<text x="{L-14}" y="{y+4}" text-anchor="end" font-size="12" class="svg-muted">Fit {s}</text>')
    o.append(f'<text x="{W/2}" y="{H-6}" text-anchor="middle" font-size="12" class="svg-muted">Route in</text>')
    slots = {}
    for a in rows:
        k = acc[a["relationship"]]
        s = a["fit_score_1to5"]
        n = slots.get((k, s), 0)
        slots[(k, s)] = n + 1
        x = L + k * cw + 18 + (n % 2) * (cw / 2 - 6)
        y = B - (s - 0.5) * (B - 10) / 5 - 10 + (n // 2) * 18
        c = REL[a["relationship"]][1]
        nm = SHORT.get(a["company"], a["company"])
        o.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="var(--{c})"/><text x="{x+10}" y="{y+4}" font-size="12" class="svg-ink">{E(nm)}</text>')
    o.append("</svg>")
    fig = f'<figure class="fig">{"".join(o)}<figcaption>Fit scores combine trigger strength, deal size, focus industry and how much the client builds in-house. Accounts in the top right have both a strong trigger and a route in, and come first.</figcaption></figure>'

    filt = ('<div class="filters" role="group" aria-label="Filter accounts"><button type="button" data-f="all" aria-pressed="true">All</button>'
            + "".join(f'<button type="button" data-f="{k}" aria-pressed="false">{E(v[0])}</button>' for k, v in REL.items())
            + '<button type="button" data-f="ind:Life" aria-pressed="false">Life sciences and medtech</button><button type="button" data-f="ind:Retail" aria-pressed="false">Retail and consumer</button><button type="button" data-f="ind:Bank" aria-pressed="false">Banking</button></div>')
    trs = ""
    for a in rows:
        nm = SHORT.get(a["company"], a["company"])
        mv, offer = MOVES.get(a["company"], ("", ""))
        rl, c = REL[a["relationship"]]
        srcs = " ".join(f'<a href="{E(u)}">[{i+1}]</a>' for i, u in enumerate(a.get("sources", [])[:3]))
        ind = industry(a["industry"])
        tag = "Life" if ("Life" in ind or "MedTech" in ind) else ("Retail" if "Retail" in ind else ("Bank" if ind in ("Banking", "Financial Services") else "other"))
        trs += (f'<tr data-r="{E(a["relationship"])}" data-i="{tag}"><th scope="row">{E(nm)}<span class="sub">{E(ind)}. {E(smu(a["industry"]))}</span></th>'
                f'<td><span class="chip" style="background:color-mix(in srgb,var(--{c}) 16%,var(--surface));color:var(--ink)">{E(rl)}</span></td>'
                f'<td>{heat(a["fit_score_1to5"]-1, a["fit_score_1to5"])}</td>'
                f'<td>{E(a["trigger"])}<span class="sub">{E(a["trigger_date"])} {srcs}</span></td>'
                f'<td>{E(mv)}<span class="sub">Entry offer: {E(offer)}</span></td></tr>')
    tbl = ('<div class="tbl-wrap" tabindex="0" role="region" aria-label="Target account list"><table class="t" id="acc"><thead><tr>'
           '<th scope="col">Account</th><th scope="col">Route in</th><th scope="col">Fit</th><th scope="col">Trigger</th><th scope="col">My first move</th></tr></thead>'
           f"<tbody>{trs}</tbody></table></div>")
    js = """<script>(function(){var bs=document.querySelectorAll('.filters button'),rs=document.querySelectorAll('#acc tbody tr');
bs.forEach(function(b){b.addEventListener('click',function(){var f=b.dataset.f;bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
rs.forEach(function(r){var ok=f==='all'||r.dataset.r===f||(f.indexOf('ind:')===0&&r.dataset.i===f.slice(4));r.style.display=ok?'':'none'})})})})();</script>"""

    levers = """<div class="grid3">
<div class="panel"><p class="k">Relationships I bring</p><p>At Foster + Partners, SOM and WSP I sold to executives at Roche, Genentech, JPMorgan Chase, Citigroup, Hyundai, ESPN, Apple, Oracle and Alibaba. Those relationships sat with real-estate and workplace leaders. In most cases they can introduce me to the digital and marketing leaders, but they do not replace the Wipro client partner.</p></div>
<div class="panel"><p class="k">Wipro clients to expand</p><p>Wipro already works for Citi, Levi Strauss, HanesBrands, TruStage, Entrust and Integra LifeSciences in the Americas. Expansion inside these accounts closes faster and at a higher win rate, so it carries the larger share of the first-year number.</p></div>
<div class="panel"><p class="k">New logos with a deadline</p><p>Separations and mergers give fixed dates: transition services agreements expire, brands must launch, sites must move. DePuy Synthes, Kenvue, MiniMed and the Walgreens units each have a digital estate that has to exist by a known date.</p></div>
</div>"""

    body = (
        phead("Accounts", "Account Map",
              "This is the list I would start with on day one. It combines accounts where I have senior relationships, Wipro clients where DX can expand, and new logos with a dated trigger in Wipro's focus industries. Each one has a trigger, a fit score and the first move I would make.",
              "Triggers verified against company releases and filings between 2025 and October 2026. Fit scores are my judgement. Oracle and Apple are left off the list because they are Wipro partners, not DX buyers.")
        + block("Map", "Fit against route in", fig)
        + block("Routes", "Three ways into an account", levers)
        + block("List", "Target accounts and first moves", filt + tbl,
                "Sorted by fit, then by route in. The SMU column shows which Wipro market unit owns the client, which tells me whose client partner I need on side.")
        + '<section class="wrap notes"><h3>Caveats</h3><ul><li>Revenue figures are left out where they could not be checked.</li><li>Wipro supplier status is from public announcements only. A missing contract does not mean Wipro has no work there.</li><li>Kraft Heinz uses the February 2026 decision to pause its split, which is later than the account research.</li><li>My relationships at Roche, Genentech, JPMorgan Chase, Citigroup and Hyundai were with property and workplace teams. Turning them into digital introductions is a first-quarter task, not a given.</li></ul></section>'
    )
    page("accounts.html", body, "Target accounts for Wipro DX in the Americas, with triggers, fit scores and first moves.", js)
