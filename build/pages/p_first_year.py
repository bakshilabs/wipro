from lib import *
import math
from pages.p_plan import PHASES, METRICS, ASKS, gantt
from pages.p_portfolio import FIELDS

F = {f[0]: f[5] for f in FIELDS}


def maths():
    """The same arithmetic as the portfolio calculator, at its default inputs."""
    T, x = F["tgt"], F["exp"] / 100
    X, N = T * x, T * (1 - x)
    wins_x, wins_n = X / F["dsx"], N / F["dsn"]
    opp_x, opp_n = wins_x / (F["wrx"] / 100), wins_n / (F["wrn"] / 100)
    pipe = opp_x * F["dsx"] + opp_n * F["dsn"]
    meet = (opp_x + opp_n) * F["q2m"]
    return dict(T=T, X=X, N=N, wx=math.ceil(wins_x), wn=math.ceil(wins_n), opp=round(opp_x + opp_n), pipe=pipe, meet=round(meet))


def chain_svg(m):
    steps = [(f"${m['T']}m", "bookings target"), (f"{m['wx'] + m['wn']}", "wins"), (f"{m['opp']}", "qualified opportunities"),
             (f"${round(m['pipe'] / 5) * 5}m", "qualified pipeline"), (f"{m['meet']}", "first buyer meetings"), (f"{round(m['meet'] / 12)}", "meetings a month")]
    o = ['<svg viewBox="0 0 1000 170" role="img" aria-labelledby="ch chd"><title id="ch">From target to activity</title>'
         f'<desc id="chd">{E(", ".join(a + " " + b for a, b in steps))}.</desc>'
         '<defs><marker id="ca" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--muted)"/></marker></defs>']
    cols = ["c0", "c3", "c1", "c1", "c2", "c2"]
    for i, (v, l) in enumerate(steps):
        cx = 85 + i * 166
        o.append(f'<circle class="pop" style="transition-delay:{i*.15:.2f}s" cx="{cx}" cy="66" r="58" fill="var(--{cols[i]})" opacity=".14"/>'
                 f'<circle class="pop" style="transition-delay:{i*.15:.2f}s" cx="{cx}" cy="66" r="58" fill="none" stroke="var(--{cols[i]})" stroke-width="2.5"/>'
                 f'<text x="{cx}" y="76" text-anchor="middle" font-size="{30 if len(v) < 4 else 25}" font-weight="700" class="svg-ink">{E(v)}</text>'
                 f'<text x="{cx}" y="150" text-anchor="middle" font-size="13.5" class="svg-muted">{E(l)}</text>')
        if i < len(steps) - 1:
            o.append(f'<line class="draw" style="--len:40;transition-delay:{.2+i*.15:.2f}s" x1="{cx+62}" x2="{cx+102}" y1="66" y2="66" stroke="var(--muted)" stroke-width="2" marker-end="url(#ca)"/>')
    o.append("</svg>")
    return "".join(o)


DISCUSS = [
    "How is the book handed over: named accounts, an inherited pipeline, or open territory in a set of industries?",
    "What would a good first two quarters look like to you, in bookings and in pipeline?",
    "How is credit shared today between the SMU, the platform practice and DX on a joint win?",
]


def build():
    m = maths()
    body = hero("First Year", "Six Wins", f"A ${m['T']}m bookings year, worked back to the meetings it needs and forward through the first 180 days.",
                f'<div class="art">{chain_svg(m)}</div>')

    parts = [("door", "Expand", f"${m['X']:.0f}m from accounts where Wipro already sells", f"About {m['wx']} wins at ${F['dsx']}m each, at a {F['wrx']}% win rate. Wipro knows the CIO in these accounts. DX reaches the CDO and CMO through the client partner."),
             ("target", "New logo", f"${m['N']:.0f}m from clients with a dated trigger", f"About {m['wn']} win at ${F['dsn']}m, at a {F['wrn']}% win rate. Separations, mergers and platform deadlines give a reason to change supplier."),
             ("ladder", "Large deal", "One pursuit of $20m or more by day 180", "Shaped through the deal ladder with a Wipro leadership sponsor. A large win in year one lifts the target; the plan does not depend on it.")]
    pt = "".join(tile(f'{icon(i)}<p class="t-k" style="margin-top:20px">{E(k)}</p><h3>{E(h)}</h3><p>{E(p)}</p>', 4) for i, k, h, p in parts)
    body += sec(head_block("The book", "Two Sources", f"{F['exp']}% of the target from existing Wipro accounts, the rest from new logos.") + f'<div class="bento">{pt}</div>'
                + f'<p class="fine">Win rates, deal sizes and the {F["q2m"]} meetings per qualified opportunity are my working assumptions, not Wipro data. Change any of them on <a href="portfolio.html">Portfolio Maths</a> in the appendix.</p>', "grey")

    ph = "".join(tile(f'<p class="t-k">{E(d)}</p><h3>{E(t)}</h3><p>{E(items[0])}</p><p><b>Output</b> {E(out)}</p>', 4) for d, t, items, out in PHASES)
    body += sec(head_block("180 days", "Map, Open, Shape", "Three phases, each with a written output.") + f'<div class="art rv">{gantt()}</div><div class="bento">{ph}</div>'
                + '<p class="fine">Every action and milestone is on <a href="plan.html">First 180 Days</a> in the appendix.</p>')

    met = table(["Measure", "Day 90", "Day 180", "Day 365"], [[E(a), (E(b), "n"), (E(c), "n"), (E(d), "n")] for a, b, c, d in METRICS], caption="Targets by day 90, 180 and 365")
    body += sec(head_block("Targets", "Hold Me to These", "Pipeline leads bookings by two to three quarters, so the early targets are about coverage.") + f'<div class="rv" style="margin-top:40px">{met}</div>', "dark")

    asks = "".join(tile(f'{icon(i)}<h3 style="margin-top:20px">{E(a)}</h3><p>{E(b)}</p>', 6, "short") for i, (a, b) in zip(["people", "pen", "grid", "bolt"], ASKS))
    body += sec(head_block("Support", "Four Asks", "What the plan needs from Wipro in the first two weeks.") + f'<div class="bento">{asks}</div>')

    q = "".join(f"<li>{E(x)}</li>" for x in DISCUSS)
    body += sec(head_block("Discussion", "Questions for You", "") + f'<ol class="disc rv">{q}</ol>', "grey")
    page("first-year.html", body, "A first-year plan for the Wipro DX Director role: a $25m bookings target worked back to activity, 180 days, targets and asks.")
