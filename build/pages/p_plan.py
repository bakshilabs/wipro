from lib import *

PHASES = [
    ("Days 1 to 30", "Map the matrix", [
        "Meet the Americas 1 consumer and health leaders and the Americas 2 banking and manufacturing leaders, then the fifteen client partners whose accounts fall in my portfolio. Agree three to five joint accounts with each.",
        "Learn the DX offers, rate cards, deal desk rules and the reference cases: TruStage, JFK Terminal 4, Odido, Levi Strauss and the Salesforce work shown at Dreamforce 2026.",
        "Meet the Adobe, Salesforce, SAP and Pega partner managers and obtain their end-of-support and migration lists for my accounts.",
        "Run tech-stack scans on fifty target accounts and match each one to the trigger calendar.",
        "Clean the inherited pipeline: every opportunity over $1m gets a next step, a date and an owner, or is closed.",
    ], "A written account plan for 25 named accounts, a dated trigger list and agreed credit rules with each client partner."),
    ("Days 31 to 90", "Open conversations", [
        "Publish three short points of view tied to dated triggers: AEM 6.5 migration for medical device makers, accessibility for health and life sciences ahead of May 2027, and agent-ready commerce for retail and consumer brands.",
        "Hold twenty first meetings with buyers, half through client partners and half through my own relationships at Roche, Genentech, Hyundai and JPMorgan Chase.",
        "Propose two paid diagnostics led by Designit, each scoped under $1m so the client can buy without a full procurement cycle.",
        "Close a first expansion deal inside an existing Wipro account to show the model working.",
    ], "Qualified pipeline of about $40m, two diagnostics in proposal and one booking."),
    ("Days 91 to 180", "Shape large deals", [
        "Shape two pursuits of more than $20m TCV through the deal ladder, each with a Wipro leadership sponsor and a written plan for credit and delivery.",
        "Put one proactive proposal in front of a separating company with a fixed exit date, such as DePuy Synthes, MiniMed or a Walgreens unit.",
        "Reach pipeline coverage of three times the next two quarters' target.",
        "Speak at one platform event or industry conference on experience design and AI, with a client on the panel.",
    ], "Two large pursuits in solution stage, coverage at three times, and bookings tracking to the annual target."),
]

METRICS = [
    ("Qualified pipeline (TCV)", "$40m", "$75m", "$90m or more"),
    ("Bookings (TCV)", "$2m to $3m", "$8m to $12m", "$25m"),
    ("First buyer meetings", "20", "40", "70"),
    ("Client partners actively co-selling", "6", "10", "15"),
    ("Large pursuits ($20m or more) in play", "0", "2", "3 to 4"),
    ("Points of view published", "3", "5", "8"),
]

ASKS = [
    ("Named client partners", "An agreed list of Americas 1 and Americas 2 accounts with a named client partner and an agreed credit rule for each."),
    ("Designit time", "Access to Designit strategists for two diagnostics in the first quarter, priced as a sales investment if necessary."),
    ("Solution architects", "A named pre-sales architect for Adobe and one for commerce, so that first pursuits are technically sound from the first meeting."),
    ("Alliance registration", "Early registration of opportunities with Adobe, Salesforce and SAP, so vendor co-sell support and funding are available."),
]


MILES = [(14, "Client partner list agreed"), (30, "Account plan for 25 accounts"), (45, "First point of view published"), (60, "Two Designit diagnostics proposed"),
         (75, "First expansion booking"), (90, "$40m qualified pipeline"), (120, "First $20m pursuit shaped"), (150, "Proactive separation proposal"), (180, "Three times coverage")]
TRACK = {"pipe": [(0, 0), (30, 5), (90, 40), (180, 75)], "meet": [(0, 0), (30, 4), (90, 20), (180, 40)], "cp": [(0, 0), (30, 3), (90, 6), (180, 10)], "book": [(0, 0), (74, 0), (75, 2), (90, 2.5), (180, 10)]}


def gantt():
    X = lambda d: 40 + d / 180 * 920
    o = ['<svg viewBox="0 0 1000 300" role="img" aria-labelledby="gt gd"><title id="gt">The first 180 days</title><desc id="gd">Three phases: map the matrix to day 30, open conversations to day 90, shape large deals to day 180, with nine milestones.</desc>']
    ph = [(0, 30, "Map the matrix", "c1"), (30, 90, "Open conversations", "c0"), (90, 180, "Shape large deals", "c3")]
    for a, b, l, c in ph:
        o.append(f'<rect class="grow" x="{X(a)+2:.0f}" y="40" width="{X(b)-X(a)-4:.0f}" height="54" rx="4" fill="var(--{c})"/><text x="{(X(a)+X(b))/2:.0f}" y="73" text-anchor="middle" font-size="17" font-weight="700" fill="#fff">{l}</text>')
    for d in (0, 30, 60, 90, 120, 150, 180):
        o.append(f'<text x="{X(d):.0f}" y="26" text-anchor="middle" font-size="13" class="svg-muted">Day {d}</text>')
    o.append(f'<line x1="{X(0)}" x2="{X(180)}" y1="140" y2="140" stroke="var(--line)" stroke-width="2"/>')
    for k, (d, l) in enumerate(MILES):
        x = X(d)
        y = 172 + (k % 4) * 34
        o.append(f'<g class="ms" data-d="{d}"><line x1="{x:.0f}" x2="{x:.0f}" y1="140" y2="{y-14}" stroke="var(--line)"/><rect class="pop" style="transition-delay:{k*.08:.2f}s" x="{x-8:.0f}" y="132" width="16" height="16" rx="2" transform="rotate(45 {x:.0f} 140)" fill="var(--line)"/>'
                 f'<text x="{x:.0f}" y="{y}" text-anchor="{"start" if k==0 else "end" if d==180 else "middle"}" font-size="13.5" class="svg-ink">{E(l)}</text></g>')
    o.append(f'<line id="cursor" x1="{X(0)}" x2="{X(0)}" y1="34" y2="290" stroke="var(--ink)" stroke-width="2.5"/>')
    o.append("</svg>")
    return "".join(o)


def build():
    import json as _j
    scrub = f"""<div class="stage rv">{gantt()}
<div class="field" style="margin-top:10px"><label for="day">Drag through the first 180 days <output id="dayo">Day 0</output></label><input type="range" id="day" min="0" max="180" value="0"></div>
<div class="kpis" style="grid-template-columns:repeat(4,1fr);margin-top:18px">
<div class="kpi"><b id="k_pipe">$0m</b><span>Qualified pipeline</span></div><div class="kpi"><b id="k_meet">0</b><span>First buyer meetings</span></div>
<div class="kpi"><b id="k_cp">0</b><span>Client partners co-selling</span></div><div class="kpi"><b id="k_book">$0m</b><span>Bookings</span></div></div>
<p class="lead" id="k_now" style="margin-top:18px;max-width:none" aria-live="polite"></p></div>"""
    phases = [(30, "Map the matrix", PHASES[0][2]), (90, "Open conversations", PHASES[1][2]), (180, "Shape large deals", PHASES[2][2])]
    js = f"""<script>(function(){{var T={_j.dumps(TRACK)},M={_j.dumps(MILES)},P={_j.dumps(phases)};
function at(a,d){{for(var i=1;i<a.length;i++){{if(d<=a[i][0]){{var p=a[i-1],q=a[i];return p[1]+(q[1]-p[1])*(d-p[0])/Math.max(1,q[0]-p[0])}}}}return a[a.length-1][1]}}
var r=document.getElementById('day'),cur=document.getElementById('cursor');
function run(){{var d=+r.value;document.getElementById('dayo').textContent='Day '+d;var x=40+d/180*920;cur.setAttribute('x1',x);cur.setAttribute('x2',x);
document.getElementById('k_pipe').textContent='$'+Math.round(at(T.pipe,d))+'m';document.getElementById('k_meet').textContent=Math.round(at(T.meet,d));
document.getElementById('k_cp').textContent=Math.round(at(T.cp,d));document.getElementById('k_book').textContent='$'+at(T.book,d).toFixed(1)+'m';
document.querySelectorAll('.ms').forEach(function(g){{var on=+g.dataset.d<=d;g.querySelector('rect').setAttribute('fill',on?'var(--accent)':'var(--line)');g.querySelector('text').style.fontWeight=on?'700':'400'}});
var ph=P[0];for(var i=0;i<P.length;i++){{if(d<=P[i][0]){{ph=P[i];break}}}}var done=M.filter(function(m){{return m[0]<=d}}),last=done.length?done[done.length-1][1]:'Start';
document.getElementById('k_now').innerHTML='<b style="color:var(--ink)">'+ph[1]+'.</b> Latest milestone: '+last+'. Now: '+ph[2][Math.min(ph[2].length-1,Math.floor((d%30)/30*ph[2].length))]}}
r.addEventListener('input',run);run();
var io=new IntersectionObserver(function(es){{if(es[0].isIntersecting&&+r.value===0&&!matchMedia('(prefers-reduced-motion: reduce)').matches){{var d=0,t=setInterval(function(){{d+=3;r.value=Math.min(180,d);run();if(d>=180)clearInterval(t)}},30);io.disconnect()}}}},{{threshold:.5}});io.observe(r)}})();</script>"""

    end = [("pipe", "$90m", "Qualified pipeline"), ("book", "$25m", "Bookings"), ("meet", "70", "First buyer meetings"), ("cp", "15", "Client partners co-selling")]
    et = "".join(tile(f'<p class="t-k">Day 365</p><div class="num">{v}</div><p>{E(l)}</p>', 3, "short") for k, v, l in end)
    met = table(["Measure", "Day 90", "Day 180", "Day 365"], [[E(a), (E(b), "n"), (E(c), "n"), (E(d), "n")] for a, b, c, d in METRICS], caption="Targets by day 90, 180 and 365")
    asks = "".join(tile(f'{icon(i)}<h3 style="margin-top:20px">{E(a)}</h3><p>{E(b)}</p>', 6, "short") for i, (a, b) in zip(["people", "pen", "grid", "bolt"], ASKS))
    body = (
        hero("First 180 Days", "Map, Open, Shape", "What I would do, what it produces, and the numbers I would be held to.", scrub)
        + sec(head_block("Year one", "The Numbers", "Hold me to these.") + f'<div class="bento">{et}</div>' + more("Show targets by day 90, 180 and 365", met), "grey")
        + sec(head_block("Support", "Four Asks", "Agreed in the first two weeks.") + f'<div class="bento">{asks}</div>')
    )
    page("plan.html", body, "A 180-day plan for the Wipro DX Director role, with an interactive timeline and targets.", js)
