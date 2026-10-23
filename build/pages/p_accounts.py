from lib import *
import json, os

D = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "accounts.json")))

SHORT = {
    "Roche / Genentech": "Roche and Genentech", "ESPN (The Walt Disney Company)": "ESPN", "Kenvue (to be acquired by Kimberly-Clark)": "Kenvue",
    "Kellanova (Mars)": "Kellanova", "Kraft Heinz (Global Taste Elevation Co. / North American Grocery Co.)": "Kraft Heinz",
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


def rows_sorted():
    rows = []
    for a in D:
        a = dict(a, **OVERRIDE.get(a["company"], {}))
        if a["company"] in ("Oracle", "Apple"):
            continue
        rows.append(a)
    rows.sort(key=lambda a: (-a["fit_score_1to5"], {"existing candidate relationship": 0, "Wipro client": 1, "new logo": 2}[a["relationship"]]))
    return rows


def panel(a):
    nm = SHORT.get(a["company"], a["company"])
    mv, offer = MOVES.get(a["company"], ("", ""))
    rl, c = REL[a["relationship"]]
    srcs = " ".join(f'<a href="{E(u)}">Source {i+1}</a>' for i, u in enumerate(a.get("sources", [])[:3]))
    dots_ = "".join(f'<i style="display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:4px;background:{"var(--accent)" if k < a["fit_score_1to5"] else "var(--line)"}"></i>' for k in range(5))
    return (f'<p class="t-k">{E(industry(a["industry"]))} · {E(smu(a["industry"]))} · {E(rl)}</p><h3>{E(nm)}</h3><p>{dots_} <b>Fit {a["fit_score_1to5"]} of 5</b></p>'
            f'<p><b>Trigger</b> {E(a["trigger"])} ({E(a["trigger_date"])})</p><p><b>First move</b> {E(mv)}</p><p><b>Entry offer</b> {E(offer)}</p><p class="src">{srcs}</p>')


def map_svg(rows):
    acc = {"existing candidate relationship": 2, "Wipro client": 1, "new logo": 0}
    W, H, L, B = 840, 560, 56, 500
    cw = (W - L - 6) / 3
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="at ad"><title id="at">Target accounts by fit and route in</title><desc id="ad">{len(rows)} accounts. Select one to see its trigger and my first move.</desc>']
    for k, lab in enumerate(["New logo", "Wipro client", "My relationship"]):
        x = L + k * cw
        o.append(f'<rect x="{x+4}" y="10" width="{cw-8}" height="{B-10}" rx="6" fill="var(--tile)"/>')
        o.append(f'<text x="{x+cw/2}" y="{B+34}" text-anchor="middle" font-size="17" class="svg-ink" font-weight="700">{lab}</text>')
    for s_ in range(1, 6):
        y = B - (s_ - 0.5) * (B - 10) / 5
        o.append(f'<text x="{L-14}" y="{y+5}" text-anchor="end" font-size="14" font-weight="600" class="svg-muted">Fit {s_}</text>')
    slots = {}
    for idx, a in enumerate(rows):
        k = acc[a["relationship"]]
        s_ = a["fit_score_1to5"]
        n = slots.get((k, s_), 0)
        slots[(k, s_)] = n + 1
        x = L + k * cw + 18 + (n % 2) * (cw / 2 - 4)
        y = B - (s_ - 0.5) * (B - 10) / 5 - 14 + (n // 2) * 24
        c = REL[a["relationship"]][1]
        nm = SHORT.get(a["company"], a["company"])
        o.append(f'<g data-pick="a{idx}" aria-label="{E(nm)}"><circle class="pop" style="transition-delay:{idx*.04:.2f}s" cx="{x:.0f}" cy="{y:.0f}" r="8" fill="var(--{c})" stroke="transparent" stroke-width="10"/><text x="{x+13:.0f}" y="{y+5:.0f}" font-size="14.5" class="svg-ink">{E(nm)}</text></g>')
    o.append("</svg>")
    return "".join(o)


def build():
    rows = rows_sorted()
    data = {f"a{i}": panel(a) for i, a in enumerate(rows)}
    art = explorer(map_svg(rows), data, "Select an account to see its trigger and my first move.", first="a0")
    body = hero("Account Map", "Twenty-Four Doors", "Each one with a dated trigger, a route in and the first move I would make.", art, dark=True)

    cnt = {k: sum(1 for a in rows if a["relationship"] == k) for k in REL}
    rt = (tile(f'{icon("people")}{num(cnt["existing candidate relationship"])}<h3>My relationships</h3><p>Roche, Genentech, Hyundai, JPMorgan Chase, ESPN. Senior contacts in property and workplace teams who can introduce me to digital leaders.</p>', 4)
          + tile(f'{icon("door")}{num(cnt["Wipro client"])}<h3>Wipro clients</h3><p>Citi, Levi Strauss, HanesBrands, TruStage. Expansion closes faster and carries most of the first-year number.</p>', 4)
          + tile(f'{icon("calendar")}{num(cnt["new logo"])}<h3>New logos with a deadline</h3><p>Separations and mergers with fixed exit dates: DePuy Synthes, Kenvue, MiniMed, Walgreens units.</p>', 4))
    body += sec(head_block("Routes", "Three Ways In", "Expansion first, relationships second, new logos with a date third.") + f'<div class="bento">{rt}</div>', "grey")

    filt = ('<div class="filters" role="group" aria-label="Filter accounts"><button type="button" data-f="all" aria-pressed="true">All</button>'
            + "".join(f'<button type="button" data-f="{k}" aria-pressed="false">{E(v[0])}</button>' for k, v in REL.items())
            + '<button type="button" data-f="ind:Life" aria-pressed="false">Life sciences and medtech</button><button type="button" data-f="ind:Retail" aria-pressed="false">Retail and consumer</button><button type="button" data-f="ind:Bank" aria-pressed="false">Banking</button></div>')
    cards = ""
    for idx, a in enumerate(rows):
        nm = SHORT.get(a["company"], a["company"])
        mv, offer = MOVES.get(a["company"], ("", ""))
        rl, c = REL[a["relationship"]]
        ind = industry(a["industry"])
        tag = "Life" if ("Life" in ind or "MedTech" in ind) else ("Retail" if "Retail" in ind else ("Bank" if ind in ("Banking", "Financial Services") else "other"))
        dots_ = "".join(f'<i style="display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:3px;background:{"var(--accent)" if k < a["fit_score_1to5"] else "var(--line)"}"></i>' for k in range(5))
        cards += (f'<div class="tile s4 acard link" tabindex="0" role="button" data-go="a{idx}" data-r="{E(a["relationship"])}" data-i="{tag}" style="min-height:0"><p class="t-k" style="color:var(--{c})">{E(rl)} · {E(ind)}</p>'
                  f'<h3 style="font-size:24px">{E(nm)}</h3><p>{dots_}</p><p style="color:var(--ink);font-size:16px">{E(offer)}</p></div>')
    js = """<script>(function(){var bs=document.querySelectorAll('.filters button'),rs=document.querySelectorAll('.acard');
bs.forEach(function(b){b.addEventListener('click',function(){var f=b.dataset.f;bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
rs.forEach(function(r){var ok=f==='all'||r.dataset.r===f||(f.indexOf('ind:')===0&&r.dataset.i===f.slice(4));r.style.display=ok?'':'none'})})});
rs.forEach(function(r){function go(){var m=document.querySelector('[data-pick="'+r.dataset.go+'"]');if(!m)return;m.dispatchEvent(new Event('click'));m.closest('section').scrollIntoView({behavior:'smooth'})}r.addEventListener('click',go);r.addEventListener('keydown',function(e){if(e.key==='Enter'){go()}})})})();</script>"""
    caveats = ('<ul style="padding-left:18px;color:var(--muted)"><li>Fit scores are my judgement.</li><li>Wipro supplier status is from public announcements only.</li>'
               '<li>Kraft Heinz uses the February 2026 decision to pause its split.</li><li>My relationships were with property and workplace teams, so digital introductions are a first-quarter task.</li></ul>')
    body += sec(head_block("Shortlist", "Entry Offers", "Filter by route in or industry. Select a card to open it on the map.") + filt + f'<div class="bento" style="margin-top:28px">{cards}</div>' + more("Caveats", caveats))
    page("accounts.html", body, "Target accounts for Wipro DX in the Americas, with triggers, fit scores and first moves.", js)
