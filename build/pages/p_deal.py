from lib import *
from pages.p_pursuit import CRITERIA, PHASES

JNJ = "https://www.jnj.com/media-center/press-releases/johnson-johnson-announces-intent-to-separate-its-orthopaedics-business"
BW = "https://www.businesswire.com/news/home/20251014819650/en/Johnson-Johnson-Announces-Intent-to-Separate-Its-Orthopaedics-Business"

# the ladder at the pursuit model's default inputs: $170 onshore, $35 offshore, 160 hours a month
RON, ROFF, H = 170, 35, 160
MUL = {"weeks": 12 / 52, "months": 1, "years": 12}
SCOPE = {
    "p1": "Twelve weeks. An inventory of every site, HCP portal, ordering flow and martech tool that runs on J&J shared services, a target estate, a platform decision and a cutover plan set against the separation dates.",
    "p2": "Twelve months. Stand up the new estate, migrate content and customer data, rebuild the HCP portal and surgeon ordering journeys, and meet the 2027 accessibility rules at launch.",
    "p3": "Three years. Platform support, content operations across markets, testing and personalisation, and AI service agents for surgeons and hospital buyers, under service levels.",
}


def ladder():
    out = []
    for key, lab, unit, ln, team, on, _ in PHASES:
        v = ln * MUL[unit] * H * team * (on / 100 * RON + (1 - on / 100) * ROFF)
        out.append((key, lab, unit, ln, team, on, v))
    return out


def ladder_svg(L):
    tot = sum(x[6] for x in L)
    W, x0 = 960, 20
    cols = ["c1", "c0", "c3"]
    o = ['<svg viewBox="0 0 1000 190" role="img" aria-labelledby="lt ld"><title id="lt">Deal ladder for DePuy Synthes</title>'
         f'<desc id="ld">{E("; ".join(f"{x[1]} ${x[6]/1e6:.1f}m" for x in L))}; total ${tot/1e6:.1f}m.</desc>']
    x = x0
    for i, (key, lab, unit, ln, team, on, v) in enumerate(L):
        w = max(8, W * v / tot)
        o.append(f'<rect class="grow" style="transition-delay:{i*.25:.2f}s" x="{x:.0f}" y="60" width="{w-3:.0f}" height="60" rx="3" fill="var(--{cols[i]})"/>')
        anchor, tx = ("start", x) if i == 0 else ("middle", x + w / 2)
        o.append(f'<text x="{tx:.0f}" y="{40 if i == 0 else 98}" text-anchor="{anchor}" font-size="{15 if i == 0 else 20}" font-weight="700" {"class=svg-ink" if i == 0 else "fill=#fff"}>${v/1e6:.1f}m</text>')
        o.append(f'<text x="{tx if i else x:.0f}" y="146" text-anchor="{anchor}" font-size="13" class="svg-muted">{E(["Diagnostic", "Build and migration", "Managed run"][i])}</text>')
        x += w
    o.append(f'<text x="{x0+W:.0f}" y="178" text-anchor="end" font-size="17" font-weight="700" class="svg-ink">${tot/1e6:.1f}m TCV over about four years</text>')
    o.append("</svg>")
    return "".join(o), tot


# my reading today and after the first sixty days of work on the account
TODAY = {"event": 3, "buyer": 1, "value": 1, "smu": 1, "platform": 1, "compete": 3, "deliver": 2, "run": 3, "strategic": 3}
DAY60 = {"event": 3, "buyer": 2, "value": 2, "smu": 2, "platform": 2, "compete": 3, "deliver": 2, "run": 3, "strategic": 3}
MOVE = {
    "buyer": "Meet the separation CIO or the CMO through the client partner, with the dated cutover plan as the reason.",
    "value": "Size the cost of running two estates past the transition period, in the company's own numbers.",
    "smu": "Confirm Wipro's J&J relationship with the Americas 1 health client partner and agree to co-lead.",
    "platform": "Register the opportunity with the platform vendor, which wants the new standalone licence as much as we want the build.",
}


def score(S):
    return round(sum(S[k] / 3 * w for k, _, _, w, _, _ in CRITERIA))


ROLES = [
    ("Me", "Originate the pursuit, write the point of view, lead the buyer conversations and the proposal, and carry the DX number."),
    ("Americas 1 client partner", "Sponsor the pursuit, open the J&J and DePuy Synthes relationships, and agree the credit split."),
    ("Designit", "Lead the twelve-week diagnostic, the journey research with surgeons and hospital buyers, and the target experience."),
    ("Platform practice", "Own the platform decision, the build estimate and the architects on the proposal."),
    ("Delivery and run", "Price and staff the managed run, and stand behind the service levels."),
    ("Alliances", "Register the deal with the platform vendor and draw on co-sell funding for the diagnostic."),
    ("Deal desk and sponsor", "Approve price and risk at the deal reviews, and put a Wipro executive in front of the Worldwide President."),
]

RISKS = [
    ("J&J keeps the work with its incumbents", "Separation advisors and existing agencies are already inside. I would go in through the customer-facing estate, which the ERP and finance advisors do not cover, and offer to work alongside them."),
    ("The separation date moves", "The ladder still holds if the dates slip, because the diagnostic is useful on any timeline. I would price it so that it stands alone."),
    ("Wipro has no footprint at J&J", "Then the score stays below 70 and the right call is a smaller entry, or a pass in favour of MiniMed or a Walgreens unit, which share the same separation pattern."),
]

DISCUSS = [
    "Does Wipro have a relationship at J&J that would carry into DePuy Synthes?",
    "Who in Wipro runs carve-out and transition services exit work today, and could DX join it?",
    "Would you fund a diagnostic like this as a sales investment if the client will not pay for it?",
]


def build():
    L = ladder()
    lsvg, tot = ladder_svg(L)
    body = hero("Sample Deal", "DePuy Synthes", "How I would take one account from a dated trigger to a $20m pursuit. Built from public sources. The numbers are my assumptions.",
                f'<div class="art">{lsvg}</div>')

    trig = (tile(f'<p class="t-k">Trigger</p>{num(18, suf=" to 24")}<h3>months to separate, from 14 October 2025</h3><p>Johnson &amp; Johnson announced its intent to separate its orthopaedics business as a standalone company named DePuy Synthes, with about $9bn of revenue. That puts completion between April and October 2027.</p>', 6)
            + tile(f'<p class="t-k">What it needs</p><h3>A digital estate of its own</h3><p>A new brand site in every market, HCP and surgeon portals, ordering and commerce, martech and customer data, all moved off J&amp;J shared services before the transition agreements end.</p>'
                   f'<p>The earliest completion date is <b><span data-days="2027-04-14">170</span> days</b> away.</p>', 6)
            + tile('<p class="t-k">Buyers</p><h3>Three people</h3><p>The Worldwide President, named when the separation was announced. The separation CIO or CDO, who owns the cutover. The CMO, who owns the brand and the surgeon experience.</p>', 6)
            + tile('<p class="t-k">Why Wipro</p><h3>Run economics at scale</h3><p>A standalone company has to carry its own run costs from day one. A managed run with offshore content operations is where Wipro is cheaper than the design-led rivals, and Designit gives it the front end they would otherwise win on.</p>', 6))
    body += sec(head_block("Account", "The Trigger", "A fixed exit date that the company cannot move on its own.") + f'<div class="bento">{trig}</div>' + src([("J&J press release, 14 Oct 2025", JNJ), ("Business Wire", BW)]), "grey")

    lad = "".join(tile(f'<p class="t-k">Phase {i+1} · ${v/1e6:.1f}m</p><h3>{E(lab)}</h3><p>{E(SCOPE[key])}</p><p class="small muted">{ln} {unit}, {team} people on average, {on}% onshore.</p>', 4)
                  for i, (key, lab, unit, ln, team, on, v) in enumerate(L))
    body += sec(head_block("Ladder", "Three Phases", f"A diagnostic small enough to buy quickly, then build and run. The run is {round(100*L[2][6]/tot)}% of the value.") + f'<div class="bento">{lad}</div>'
                + f'<p class="fine">Rates of ${RON} an hour onshore and ${ROFF} offshore at {H} hours a month are my assumptions. Change them on <a href="pursuit.html">Pursuit Model</a> in the appendix.</p>')

    rows = []
    for k, lab, _, w, _, lv in CRITERIA:
        a, b = TODAY[k], DAY60[k]
        rows.append([E(lab), (f"{w}", "n"), E(lv[a]), (f"<b>{E(lv[b])}</b>" if b != a else E(lv[b])), E(MOVE.get(k, ""))])
    t0, t1 = score(TODAY), score(DAY60)
    tbl = table(["Criterion", "Weight", "Today", "After 60 days", "What moves it"], rows, caption="Pursuit score for DePuy Synthes")
    sc = (tile(f'<p class="t-k">Today</p>{num(t0)}<h3>Shape before committing</h3><p>A strong event and a large run, with no engaged buyer yet and Wipro\'s position at J&amp;J unconfirmed.</p>', 6)
          + tile(f'<p class="t-k">After 60 days</p>{num(t1)}<h3>Pursue</h3><p>Four criteria move one level each. That is the work of the first two months on the account.</p>', 6))
    body += sec(head_block("Score", f"From {t0} to {t1}", "The pursuit scorecard from the appendix, filled in for this account.") + f'<div class="bento">{sc}</div><div class="rv" style="margin-top:28px">{tbl}</div>', "dark")

    rl = "".join(tile(f'<h3>{E(a)}</h3><p>{E(b)}</p>', 4 if i < 6 else 12, "short") for i, (a, b) in enumerate(ROLES))
    body += sec(head_block("Matrix", "Who Does What", "Agreed with the client partner before the first buyer meeting.") + f'<div class="bento">{rl}</div>', "grey")

    rk = "".join(tile(f'{icon("shield")}<h3 style="margin-top:20px">{E(a)}</h3><p>{E(b)}</p>', 4) for a, b in RISKS)
    body += sec(head_block("Risks", "What Could Stop It", "And what I would do about each.") + f'<div class="bento">{rk}</div>')

    q = "".join(f"<li>{E(x)}</li>" for x in DISCUSS)
    body += sec(head_block("Discussion", "Questions for You", "") + f'<ol class="disc rv">{q}</ol>'
                + '<p class="fine">DePuy Synthes is one of twenty-four accounts on the <a href="accounts.html">Account Map</a> in the appendix.</p>', "grey")
    page("deal.html", body, "A worked DX pursuit for DePuy Synthes: separation trigger, buyers, a three-phase deal ladder to $21m, pursuit score and matrix roles.")
