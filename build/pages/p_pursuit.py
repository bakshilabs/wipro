from lib import *

CRITERIA = [
    # key, label, hint, weight, axis (u = client urgency, r = Wipro right to win, b = both), level descriptions 0..3
    ("event", "Compelling event with a date", "A deadline the client cannot move: end of platform support, a regulation date, a launch, a separation.", 15, "u",
     ["None found", "Vague ambition", "Internal date (budget cycle, launch)", "External deadline (support end, regulation)"]),
    ("buyer", "Economic buyer engaged", "A CDO, CMO or chief customer officer who owns the budget has met us.", 15, "u",
     ["Not identified", "Identified, not met", "Met, interested", "Sponsoring the case"]),
    ("value", "Quantified value case", "The benefit is in the client's own numbers: conversion, cost to serve, content cost, time to market.", 10, "u",
     ["None", "Generic benchmarks", "Client data, our estimate", "Client agrees the numbers"]),
    ("smu", "Wipro account position", "The SMU client partner sponsors the pursuit, and Wipro already has a footprint to build on.", 15, "r",
     ["No Wipro presence", "Presence, no sponsor", "Client partner supportive", "Client partner co-leads"]),
    ("platform", "Platform partner alignment", "Adobe, Salesforce, SAP, Pega or another vendor co-sells with us on this client.", 10, "r",
     ["Vendor backs a rival", "Neutral", "Registered co-sell", "Vendor introduced us"]),
    ("compete", "Competitive position", "Are we shaping the deal before an RFP, or answering one written for an incumbent?", 10, "r",
     ["RFP wired for incumbent", "Open RFP", "Shortlist with insight", "Sole-source or proactive"]),
    ("deliver", "Deliverability and margin", "Skills are available, the onshore and offshore mix is realistic, and margin clears the account threshold.", 10, "r",
     ["Gaps we cannot fill", "Gaps with a plan", "Staffable at target margin", "Staffed, margin above target"]),
    ("run", "Run and scale potential", "There is a multi-year managed phase (platform, content, AI agents) that makes the TCV large.", 10, "b",
     ["Project only", "Small support tail", "Run phase likely", "Run phase in scope"]),
    ("strategic", "Strategic value", "A reference client, a new logo in a focus industry, or a first deal on a new platform.", 5, "b",
     ["None", "Some", "Strong", "Flagship"]),
]

PRESETS = {
    "aem": ("Proactive AEM 6.5 migration at a medical device maker", {"event": 3, "buyer": 2, "value": 2, "smu": 2, "platform": 3, "compete": 3, "deliver": 2, "run": 3, "strategic": 2}),
    "rfp": ("Open commerce replatform RFP with an entrenched agency", {"event": 2, "buyer": 1, "value": 1, "smu": 1, "platform": 1, "compete": 1, "deliver": 2, "run": 1, "strategic": 1}),
    "cmo": ("New CMO at a retailer, no Wipro footprint", {"event": 1, "buyer": 2, "value": 1, "smu": 0, "platform": 2, "compete": 3, "deliver": 2, "run": 2, "strategic": 3}),
}

PHASES = [
    # key, label, unit, default length, default team, default onshore %, description
    ("p1", "Diagnostic, experience strategy and design", "weeks", 12, 15, 50,
     "Journey research, a target experience, a platform decision and a costed roadmap. This is the paid way in, often led by design."),
    ("p2", "Platform build and migration", "months", 12, 60, 25,
     "Replatforming, integration, content migration, accessibility remediation and launch, delivered in releases."),
    ("p3", "Managed run, content operations and AI agents", "years", 3, 40, 15,
     "Platform support, content production at scale, testing and personalisation, and operation of customer-facing AI agents under service levels."),
]


def build():
    rows = ""
    for key, lab, hint, w, ax, levels in CRITERIA:
        btns = "".join(
            f'<button type="button" data-k="{key}" data-v="{v}" aria-pressed="false" title="{E(levels[v])}">{v}</button>' for v in range(4)
        )
        rows += (
            f'<div class="score-row"><div class="q">{E(lab)} <span class="chip plain">weight {w}</span>'
            f'<small>{E(hint)}</small><small class="lvl" id="lvl-{key}"></small></div>'
            f'<div class="seg-ctl" role="group" aria-label="{E(lab)} score">{btns}</div></div>'
        )
    presets = "".join(f'<button type="button" data-preset="{k}" aria-pressed="false">{E(v[0])}</button>' for k, v in PRESETS.items())

    quad_svg = """<svg viewBox="0 0 420 420" role="img" aria-labelledby="qt" id="quad">
<title id="qt">Pursuit position on client urgency and Wipro right to win</title>
<rect x="40" y="10" width="180" height="180" class="svg-panel"/><rect x="230" y="10" width="180" height="180" class="svg-panel"/>
<rect x="40" y="200" width="180" height="180" class="svg-panel"/><rect x="230" y="200" width="180" height="180" class="svg-panel"/>
<text x="130" y="34" text-anchor="middle" class="svg-ink" font-size="13" font-weight="600">Create the position</text>
<text x="130" y="52" text-anchor="middle" class="svg-muted" font-size="11.5">Paid diagnostic or design sprint</text>
<text x="320" y="34" text-anchor="middle" class="svg-ink" font-size="13" font-weight="600">Pursue now</text>
<text x="320" y="52" text-anchor="middle" class="svg-muted" font-size="11.5">Full team, leadership sponsor</text>
<text x="130" y="224" text-anchor="middle" class="svg-ink" font-size="13" font-weight="600">Nurture</text>
<text x="130" y="242" text-anchor="middle" class="svg-muted" font-size="11.5">Content and events only</text>
<text x="320" y="224" text-anchor="middle" class="svg-ink" font-size="13" font-weight="600">Create the urgency</text>
<text x="320" y="242" text-anchor="middle" class="svg-muted" font-size="11.5">Point of view on their data</text>
<text x="225" y="408" text-anchor="middle" class="svg-muted" font-size="12">Wipro right to win</text>
<text x="16" y="195" text-anchor="middle" class="svg-muted" font-size="12" transform="rotate(-90 16 195)">Client urgency</text>
<circle id="qdot" cx="225" cy="195" r="11" fill="var(--accent)" stroke="var(--bg)" stroke-width="3"/>
</svg>"""

    score = f"""<div class="filters" role="group" aria-label="Example pursuits">{presets}</div>
<div class="calc">
<div class="inputs" id="crit">{rows}</div>
<div class="out">
<div class="kpis"><div class="kpi"><b id="sc">0</b><span>Weighted score out of 100</span></div><div class="kpi"><b id="uq">0</b><span>Urgency and right to win, each out of 100</span></div></div>
<div class="verdict" id="vd" aria-live="polite"></div>
<figure style="margin-top:14px">{quad_svg}</figure>
<p class="small muted" style="margin-top:8px">Urgency combines the event, buyer and value scores. Right to win combines account position, platform alignment, competition and deliverability. Run potential and strategic value add to the overall score only.</p>
</div></div>"""

    ph_inputs = ""
    for key, lab, unit, ln, team, on, desc in PHASES:
        mx = {"weeks": 26, "months": 24, "years": 5}[unit]
        ph_inputs += f"""<div class="panel" style="margin-top:12px;background:var(--surface)"><h3>{E(lab)}</h3><p class="small muted" style="margin-top:4px">{E(desc)}</p>
<div class="field"><label for="{key}l">Length <output id="{key}lo"></output></label><input type="range" id="{key}l" min="0" max="{mx}" value="{ln}" data-unit="{unit}"></div>
<div class="field"><label for="{key}t">Average team size <output id="{key}to"></output></label><input type="range" id="{key}t" min="0" max="150" value="{team}"></div>
<div class="field"><label for="{key}o">Onshore share <output id="{key}oo"></output></label><input type="range" id="{key}o" min="0" max="100" step="5" value="{on}"></div></div>"""

    ladder = f"""<div class="calc">
<div class="inputs">
<div class="field"><label for="ron">Onshore blended rate, $ per hour <output id="rono"></output></label><input type="range" id="ron" min="90" max="260" step="5" value="170"><p class="hint">Assumption for a US onshore team mix of strategists, designers, architects and engineers.</p></div>
<div class="field"><label for="roff">Offshore blended rate, $ per hour <output id="roffo"></output></label><input type="range" id="roff" min="20" max="70" step="1" value="35"><p class="hint">Assumption for India and nearshore delivery centres.</p></div>
{ph_inputs}
</div>
<div class="out">
<div class="kpis"><div class="kpi"><b id="tcv">$0</b><span>Total contract value</span></div><div class="kpi"><b id="acv">$0</b><span>Average annual contract value</span></div>
<div class="kpi"><b id="yrs">0</b><span>Contract length in years</span></div><div class="kpi"><b id="br">$0</b><span>Blended rate per hour</span></div></div>
<div class="verdict" id="lv" aria-live="polite"></div>
<figure style="margin-top:16px"><svg id="lad" viewBox="0 0 520 260" role="img" aria-label="Contract value by phase"></svg>
<div class="legend"><span><i style="background:var(--c1)"></i>Diagnostic and design</span><span><i style="background:var(--c0)"></i>Build and migration</span><span><i style="background:var(--c3)"></i>Managed run</span></div></figure>
<p class="small muted" style="margin-top:10px">Services fees only. Platform licences are excluded because the client usually buys them from the vendor. 160 billable hours a month per person.</p>
</div></div>"""

    js = jsdata("CRIT", [{"k": k, "w": w, "a": a, "lv": lv} for k, _, _, w, a, lv in CRITERIA]) + jsdata("PRESETS", {k: v[1] for k, v in PRESETS.items()}) + """
<script>
(function(){
var S={};CRIT.forEach(function(c){S[c.k]=0});
function setBtns(){document.querySelectorAll('#crit button').forEach(function(b){b.setAttribute('aria-pressed',String(S[b.dataset.k]==+b.dataset.v))});
CRIT.forEach(function(c){document.getElementById('lvl-'+c.k).textContent='Selected: '+c.lv[S[c.k]]})}
function calc(){var tot=0,u=0,uw=0,r=0,rw=0;CRIT.forEach(function(c){var v=S[c.k]/3;tot+=v*c.w;if(c.a=='u'){u+=v*c.w;uw+=c.w}if(c.a=='r'){r+=v*c.w;rw+=c.w}});
var U=Math.round(100*u/uw),R=Math.round(100*r/rw),T=Math.round(tot);
document.getElementById('sc').textContent=T;document.getElementById('uq').textContent=U+' / '+R;
var vd=document.getElementById('vd'),msg,cls;
if(S.event===0&&S.buyer<2){msg='Nurture. There is no dated event and no engaged buyer, so the score does not matter yet. Keep the account warm with content and revisit at the next trigger.';cls='bad'}
else if(T>=70){msg='Pursue. Assemble the full pursuit team, agree credit with the SMU and platform practice, and plan a Wipro leadership meeting with the buyer.';cls='ok'}
else if(T>=50){msg='Shape before committing. Invest in a workshop or paid diagnostic to close the weakest criteria before building a full proposal.';cls='warn'}
else{msg='Qualify out or nurture. The pursuit cost would exceed the expected return. Record the reasons so the account team knows what would change the decision.';cls='bad'}
vd.className='verdict '+cls;vd.textContent=msg;
var d=document.getElementById('qdot');d.setAttribute('cx',40+R/100*370);d.setAttribute('cy',380-U/100*370)}
document.getElementById('crit').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;S[b.dataset.k]=+b.dataset.v;
document.querySelectorAll('[data-preset]').forEach(function(p){p.setAttribute('aria-pressed','false')});setBtns();calc()});
document.querySelectorAll('[data-preset]').forEach(function(p){p.addEventListener('click',function(){var v=PRESETS[p.dataset.preset];for(var k in v)S[k]=v[k];
document.querySelectorAll('[data-preset]').forEach(function(q){q.setAttribute('aria-pressed',String(q===p))});setBtns();calc()})});
var first=document.querySelector('[data-preset]');first.click();

var fmt=function(n){return n>=1e6?'$'+(n/1e6).toFixed(1)+'m':'$'+Math.round(n/1e3)+'k'};
var H=160;
function v(id){return +document.getElementById(id).value}
function lad(){var ron=v('ron'),roff=v('roff');document.getElementById('rono').textContent='$'+ron;document.getElementById('roffo').textContent='$'+roff;
var ph=['p1','p2','p3'],mul={weeks:12/52,months:1,years:12},vals=[],hrs=0,yrs=0;
ph.forEach(function(p){var el=document.getElementById(p+'l'),u=el.dataset.unit,L=+el.value,T=v(p+'t'),O=v(p+'o')/100;
document.getElementById(p+'lo').textContent=L+' '+u;document.getElementById(p+'to').textContent=T;document.getElementById(p+'oo').textContent=Math.round(O*100)+'%';
var months=L*mul[u],h=months*H*T,val=h*(O*ron+(1-O)*roff);vals.push(val);hrs+=h;yrs+=months/12});
var tcv=vals.reduce(function(a,b){return a+b},0);
document.getElementById('tcv').textContent=fmt(tcv);document.getElementById('acv').textContent=yrs>0?fmt(tcv/Math.max(1,yrs)):'$0';
document.getElementById('yrs').textContent=yrs.toFixed(1);document.getElementById('br').textContent=hrs>0?'$'+Math.round(tcv/hrs):'$0';
var lv=document.getElementById('lv'),share=tcv>0?Math.round(100*vals[2]/tcv):0;
if(tcv>=20e6){lv.className='verdict ok';lv.textContent='Above the $20m line in the posting. The run phase supplies '+share+'% of the value, and the design phase is '+fmt(vals[0])+', small enough to buy without a full procurement cycle.'+(tcv>=30e6?' It also counts as a large deal in Wipro’s quarterly results, which use $30m.':' Wipro’s quarterly results count large deals from $30m, so a second business unit or a longer run phase would make it visible at group level.')}
else{lv.className='verdict warn';lv.textContent='Below the $20m large-deal line by '+fmt(20e6-tcv)+'. Lengthen or widen the run phase, or add a second business unit, before calling this a large deal.'}
var svg=document.getElementById('lad'),max=Math.max(34e6,tcv*1.1),W=520,base=220,sc=200/max,cols=['var(--c1)','var(--c0)','var(--c3)'],labs=['Design','Build','Run'],out='',cum=0;
var y20=base-20e6*sc,y30=base-30e6*sc;out+='<line x1="40" x2="'+(W-10)+'" y1="'+y20+'" y2="'+y20+'" stroke="var(--bad)" stroke-dasharray="4 4"/><text x="40" y="'+(y20-6)+'" font-size="11" fill="var(--bad)">$20m: large deal in the posting</text>';
out+='<line x1="40" x2="'+(W-10)+'" y1="'+y30+'" y2="'+y30+'" stroke="var(--muted)" stroke-dasharray="2 4"/><text x="40" y="'+(y30-6)+'" font-size="11" class="svg-muted">$30m: large deal in Wipro results</text>';
vals.forEach(function(val,i){var h=val*sc,x=60+i*120;out+='<rect x="'+x+'" y="'+(base-cum*sc-h)+'" width="90" height="'+Math.max(0,h)+'" fill="'+cols[i]+'" rx="2"/><text x="'+(x+45)+'" y="'+(base+18)+'" text-anchor="middle" font-size="12" class="svg-muted">'+labs[i]+'</text><text x="'+(x+45)+'" y="'+(base-cum*sc-h-6)+'" text-anchor="middle" font-size="12" class="svg-ink">'+fmt(val)+'</text>';cum+=val});
var x=60+3*120,h=tcv*sc;out+='<rect x="'+x+'" y="'+(base-h)+'" width="70" height="'+h+'" fill="var(--ink)" opacity=".85" rx="2"/><text x="'+(x+35)+'" y="'+(base+18)+'" text-anchor="middle" font-size="12" class="svg-muted">TCV</text><text x="'+(x+35)+'" y="'+(base-h-6)+'" text-anchor="middle" font-size="12" class="svg-ink">'+fmt(tcv)+'</text>';
out+='<line x1="40" x2="'+(W-10)+'" y1="'+base+'" y2="'+base+'" class="svg-line" stroke="var(--line)"/>';svg.innerHTML=out}
document.querySelectorAll('.calc input[type=range]').forEach(function(i){i.addEventListener('input',lad)});lad();
})();
</script>"""

    steps = [("calendar", "Find the date", "A support end, a rule, a separation."), ("target", "Score it", "Nine criteria, before spending a dollar."), ("ladder", "Shape the ladder", "Small first phase. Run phase makes it large.")]
    st = "".join(tile(f'{icon(i)}<p class="t-k" style="margin-top:20px">Step {k+1}</p><h3>{E(h)}</h3><p>{E(p)}</p>', 4, "short") for k, (i, h, p) in enumerate(steps))
    hero_art = """<svg viewBox="0 0 1000 300" role="img" aria-label="A deal ladder: design under $1m, build $8m, run $13m, total $21m">
<rect class="growy" x="120" y="250" width="160" height="10" rx="3" fill="var(--c1)"/><text x="200" y="236" text-anchor="middle" font-size="22" font-weight="700" class="svg-ink">$0.7m</text><text x="200" y="290" text-anchor="middle" font-size="16" class="svg-muted">Design</text>
<rect class="growy" style="transition-delay:.25s" x="340" y="150" width="160" height="110" rx="3" fill="var(--c0)"/><text x="420" y="136" text-anchor="middle" font-size="22" font-weight="700" class="svg-ink">$7.9m</text><text x="420" y="290" text-anchor="middle" font-size="16" class="svg-muted">Build</text>
<rect class="growy" style="transition-delay:.5s" x="560" y="80" width="160" height="180" rx="3" fill="var(--c3)"/><text x="640" y="66" text-anchor="middle" font-size="22" font-weight="700" class="svg-ink">$12.7m</text><text x="640" y="290" text-anchor="middle" font-size="16" class="svg-muted">Run</text>
<rect class="growy" style="transition-delay:.75s" x="780" y="20" width="120" height="240" rx="3" fill="var(--ink)"/><text x="840" y="290" text-anchor="middle" font-size="16" font-weight="700" class="svg-ink">$21.3m TCV</text>
<line x1="80" x2="940" y1="260" y2="260" stroke="var(--line)"/></svg>"""
    body = (
        hero("Pursuit Model", "Score and Shape", "Nine criteria decide whether to pursue. Three phases decide how large it gets.", f'<div class="art m">{hero_art}</div>')
        + sec(head_block("Method", "Three Steps", "The same routine on every opportunity.") + f'<div class="bento">{st}</div>', "grey")
        + sec(head_block("Scorecard", "Pursue, Shape or Walk Away", "Pick an example or score your own. Watch the dot move.") + f'<div class="rv">{score}</div>')
        + sec(head_block("Ladder", "From $0.7m to $21m", "Drag the sliders. The run phase is what makes it a large deal.") + f'<div class="rv">{ladder}</div>'
              + more("Assumptions", '<p class="lead" style="margin-top:0">The weights, rates and team sizes are my working assumptions for illustration, not Wipro figures. A real pursuit would use Wipro rate cards, deal desk margin rules and the client\'s own value data.</p>'), "dark")
    )
    page("pursuit.html", body, "A weighted pursuit scorecard and a deal ladder showing how DX deals reach $20m TCV.", js)
