from lib import *

POST = "https://careers.wipro.com/job/Director-Digital-Experience-(DX)/190063-en_US/"

# minute start, minutes, segment, what I show, what I want to learn, page
RUN = [
    (0, 5, "Introductions", "Nothing on screen.", "Who is in the room and what each person needs from this hire.", ""),
    (5, 8, "Track record", "Three stories from sixteen years of selling design-led consulting, and the three gaps I would close first.", "Which of the three matters most for the accounts you have in mind.", "record.html"),
    (13, 7, "Thesis", "Three claims about why Wipro is hiring this role now: Americas growth, the front-end gap, and the 2027 deadlines.", "Where my reading of Wipro is wrong or out of date.", "thesis.html"),
    (20, 12, "First year", "A $25m bookings year worked back to 70 first meetings, then forward through the first 180 days with targets.", "How the book is handed over and what a good first two quarters looks like to you.", "first-year.html"),
    (32, 10, "Sample deal", "DePuy Synthes, taken from a dated separation trigger to a $21m pursuit, with who does what across the matrix.", "Whether Wipro has the relationship and carve-out experience to win it.", "deal.html"),
    (42, 13, "Your questions", "Any appendix page that helps answer them: account map, pursuit scorecard, portfolio calculator, competitor notes.", "What you are testing for.", "research.html"),
    (55, 5, "My questions", "Twelve questions about the book, the matrix, the offer and how success is judged.", "The next step and the decision timeline.", "questions.html"),
]

TAKE = [
    ("spark", "A design-led opening", "Wipro's DX weakness is the first conversation with a CMO or CDO. I have spent sixteen years leading that conversation with Fortune 500 executives."),
    ("calendar", "Deadlines sell", "Platform support dates and accessibility rules converge in 2027 on Wipro's focus industries. Each one is a dated reason to buy."),
    ("ladder", "A number with a method", "A $25m year is about six wins built with SMU client partners. The maths, the targets and the first 180 days are written down for you to test."),
]


def run_svg():
    W, X0, X1 = 1000, 20, 980
    X = lambda m: X0 + m / 60 * (X1 - X0)
    cols = ["c6", "c0", "c1", "c3", "c2", "c6", "c0"]
    o = ['<svg viewBox="0 0 1000 150" role="img" aria-labelledby="rs rsd"><title id="rs">Run of show for a one-hour meeting</title>'
         '<desc id="rsd">Seven segments: introductions 5 minutes, track record 8, thesis 7, first year 12, sample deal 10, your questions 13, my questions 5.</desc>']
    for k, (m, d, lab, *_r) in enumerate(RUN):
        op = ".35" if cols[k] == "c6" else "1"
        o.append(f'<rect class="grow" style="transition-delay:{k*.08:.2f}s" x="{X(m)+2:.0f}" y="40" width="{X(m+d)-X(m)-4:.0f}" height="56" rx="4" fill="var(--{cols[k]})" opacity="{op}"/>')
        o.append(f'<text x="{(X(m)+X(m+d))/2:.0f}" y="74" text-anchor="middle" font-size="{15 if d >= 7 else 12}" font-weight="700" fill="{"#fff" if op == "1" else "currentColor"}" class="{"" if op == "1" else "svg-ink"}">{d}</text>')
        o.append(f'<text x="{(X(m)+X(m+d))/2:.0f}" y="122" text-anchor="middle" font-size="13" class="svg-muted">{E(lab if d >= 7 else lab.split()[0])}</text>')
    for m in (0, 15, 30, 45, 60):
        o.append(f'<text x="{X(m):.0f}" y="24" text-anchor="{"start" if m == 0 else "end" if m == 60 else "middle"}" font-size="13" class="svg-muted">{m} min</text>')
    o.append("</svg>")
    return "".join(o)


def build():
    cta = '<a class="pill fill" href="record.html">Start the meeting</a><a class="pill line" href="research.html">Research appendix</a>'
    body = hero("Wipro · Director, Digital Experience", "One Hour",
                "Five short pages to show, plenty of time for your questions, and the research behind them in an appendix.", f'<div class="art">{run_svg()}</div>', cta)

    rows = ""
    for m, d, lab, show, learn, href in RUN:
        link = f' <a href="{href}">Open</a>' if href else ""
        rows += (f'<div class="r rv"><div><span class="m">{m} to {m+d} min · {d} min</span><br><b>{E(lab)}</b></div>'
                 f'<p><small>What I show</small>{E(show)}{link}</p><p><small>What I want to learn</small>{E(learn)}</p></div>')
    body += sec(head_block("Run of show", "Seven Parts", "About half the hour is conversation. Each meeting page ends with questions for you.") + f'<div class="ros">{rows}</div>', "grey")

    tk = "".join(tile(f'{icon(i)}<h3 style="margin-top:22px">{E(h)}</h3><p>{E(p)}</p>', 4) for i, h, p in TAKE)
    body += sec(head_block("Takeaways", "Three Points", "If the meeting runs short, these are the ones I want you to keep.") + f'<div class="bento">{tk}</div>')

    m_pages = [("record.html", "pen", "Track Record", "Three stories and three gaps."), ("thesis.html", "chart", "Thesis", "Why this role, and why now."),
               ("first-year.html", "bolt", "First Year", "From $25m to meetings and milestones."), ("deal.html", "ladder", "Sample Deal", "One account, from trigger to $21m."),
               ("questions.html", "people", "Questions", "What I need to learn from you."), ("cv.html", "door", "CV", "Two pages, ordered for this role.")]
    cards = "".join(tile(f'{icon(i)}<h3 style="margin-top:22px">{E(t)}</h3><p>{E(d)}</p><span class="go">Open</span>', 4, href=h) for h, i, t, d in m_pages)
    body += sec(head_block("Meeting", "Six Pages", "In the order I would show them.") + f'<div class="bento">{cards}</div>'
                + f'<p class="fine">The <a href="research.html">research appendix</a> holds nine working pages: role anatomy, operating matrix, market, triggers, account map, pursuit model, portfolio maths, the detailed 180-day plan and the full fit assessment. Prepared by Arpan Bakshi, October 2026, from public sources. The <a href="{POST}">posting</a> is Wipro req 190063.</p>', "grey")
    page("overview.html", body, "Agenda for a one-hour interview for the Wipro Director, Digital Experience role, with the pages to show and discuss.")
