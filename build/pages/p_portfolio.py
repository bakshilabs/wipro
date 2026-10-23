from lib import *

FIELDS = [
    # id, label, min, max, step, default, format, hint
    ("tgt", "Annual order bookings target (TCV)", 5, 60, 1, 25, "m", "The posting names a $20m to $25m portfolio. I use the top of that range."),
    ("exp", "Share of bookings from accounts where Wipro already sells", 0, 100, 5, 60, "%", "Expansion inside SMU accounts, with a client partner already in place."),
    ("dsx", "Average expansion deal (TCV)", 0.5, 15, 0.5, 3, "m", "Add-on DX scope in an existing account."),
    ("dsn", "Average new-logo deal (TCV)", 1, 40, 1, 10, "m", "First DX deal with a new client, usually a design phase plus build."),
    ("wrx", "Win rate on qualified expansion opportunities", 10, 80, 5, 40, "%", ""),
    ("wrn", "Win rate on qualified new-logo opportunities", 5, 60, 5, 20, "%", ""),
    ("q2m", "First meetings needed per qualified opportunity", 1, 10, 1, 4, "", "Conversations with a buyer before one becomes a qualified opportunity."),
    ("cyc", "Average sales cycle in months", 2, 18, 1, 7, "", "From qualification to signature."),
    ("yrs", "Average contract length in years", 1, 5, 0.5, 3, "", "Used to convert TCV into ACV and first-year revenue."),
]


def build():
    inputs = "".join(
        f'<div class="field"><label for="{i}">{E(l)} <output id="{i}o"></output></label>'
        f'<input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{d}" data-f="{f}">'
        + (f'<p class="hint">{E(h)}</p>' if h else "") + "</div>"
        for i, l, mn, mx, st, d, f, h in FIELDS
    )
    calc = f"""<div class="calc">
<div class="inputs">{inputs}</div>
<div class="out">
<div class="kpis">
<div class="kpi"><b id="o_pipe">0</b><span>Qualified pipeline needed in the year (TCV)</span></div>
<div class="kpi"><b id="o_cov">0</b><span>Pipeline coverage over target</span></div>
<div class="kpi"><b id="o_wins">0</b><span>Deals to win (expansion and new logo)</span></div>
<div class="kpi"><b id="o_opps">0</b><span>Qualified opportunities to create</span></div>
<div class="kpi"><b id="o_mtg">0</b><span>First buyer meetings per month</span></div>
<div class="kpi"><b id="o_rev">0</b><span>Revenue billed in year one from those bookings</span></div>
</div>
<div class="verdict" id="o_v" aria-live="polite"></div>
<figure style="margin-top:16px"><svg id="fun" viewBox="0 0 520 230" role="img" aria-label="Funnel from meetings to wins"></svg>
<div class="legend"><span><i style="background:var(--c0)"></i>Expansion in existing accounts</span><span><i style="background:var(--c2)"></i>New logos</span></div></figure>
</div></div>"""

    js = """<script>
(function(){
var ids=['tgt','exp','dsx','dsn','wrx','wrn','q2m','cyc','yrs'];
function g(i){return +document.getElementById(i).value}
function f(n){return n>=1e6?'$'+(n/1e6).toFixed(1)+'m':'$'+Math.round(n/1e3)+'k'}
function run(){ids.forEach(function(i){var el=document.getElementById(i),fm=el.dataset.f,v=+el.value;document.getElementById(i+'o').textContent=fm=='m'?'$'+v+'m':fm=='%'?v+'%':v});
var T=g('tgt')*1e6,X=T*g('exp')/100,N=T-X,wx=g('wrx')/100,wn=g('wrn')/100,dx=g('dsx')*1e6,dn=g('dsn')*1e6;
var px=X/wx,pn=N/wn,P=px+pn,winsx=X/dx,winsn=N/dn,ox=winsx/wx,on=winsn/wn,O=ox+on,M=O*g('q2m'),yrs=g('yrs');
var rev=(T/yrs)*0.5;
document.getElementById('o_pipe').textContent=f(P);document.getElementById('o_cov').textContent=(P/T).toFixed(1)+'x';
document.getElementById('o_wins').textContent=Math.ceil(winsx)+' + '+Math.ceil(winsn);
document.getElementById('o_opps').textContent=Math.ceil(O);document.getElementById('o_mtg').textContent=(M/12).toFixed(1);
document.getElementById('o_rev').textContent=f(rev);
var cyc=g('cyc'),v=document.getElementById('o_v');
var lead=Math.max(0,12-cyc);
if(cyc>=10){v.className='verdict bad';v.textContent='With a '+cyc+' month cycle, almost everything that closes this year must already be qualified in the first two months. The plan depends on inheriting live pipeline.'}
else if(P/T>4){v.className='verdict warn';v.textContent='Coverage of '+(P/T).toFixed(1)+'x is heavy. Raise win rates through earlier shaping and proactive proposals, or move more of the target into existing accounts.'}
else{v.className='verdict ok';v.textContent='Workable. Opportunities qualified in the first '+lead+' months can still close this year. Year-one revenue is about '+f(rev)+' because bookings bill over '+yrs+' years and arrive through the year.'}
var svg=document.getElementById('fun'),rows=[['First meetings',M*ox/O,M*on/O],['Qualified opportunities',ox,on],['Wins',winsx,winsn]],mx=M,out='';
rows.forEach(function(r,i){var y=20+i*68,wx=400*r[1]/mx,wn=400*r[2]/mx,x0=60+(400-wx-wn)/2;
out+='<text x="0" y="'+(y-6)+'" font-size="12" class="svg-muted">'+r[0]+'</text>';
out+='<rect x="'+x0+'" y="'+y+'" width="'+Math.max(1,wx)+'" height="34" fill="var(--c0)" rx="2"/><rect x="'+(x0+wx)+'" y="'+y+'" width="'+Math.max(1,wn)+'" height="34" fill="var(--c2)" rx="2"/>';
out+='<text x="'+(x0+wx+wn+8)+'" y="'+(y+22)+'" font-size="12.5" class="svg-ink">'+Math.ceil(r[1]+r[2])+'</text>'});
svg.innerHTML=out}
ids.forEach(function(i){document.getElementById(i).addEventListener('input',run)});run();
})();
</script>"""

    book = """<div class="grid3">
<div class="panel"><p class="k">Protect</p><h3>Live DX work in the book</h3><p>Renewals and phase extensions on work Wipro already delivers. The aim is zero leakage: every live engagement has a named next phase and a date for proposing it.</p></div>
<div class="panel"><p class="k">Expand</p><h3>SMU accounts with no DX yet</h3><p>Accounts where Wipro runs infrastructure, applications or operations but the marketing and digital teams buy from an agency. Wipro's existing access to the CIO shortens the route to the CDO.</p></div>
<div class="panel"><p class="k">New logo</p><h3>Clients with a dated trigger</h3><p>A short list of companies with a forced event, such as a platform end-of-support date, a spin-off or a new CMO. These take longer and need a sharper point of view.</p></div>
</div>"""

    rhythm = table(
        ["Cadence", "What happens", "Who"],
        [
            ["Weekly", "Pipeline review of every opportunity above $1m: next step, date, owner, risk.", "Me, practice lead"],
            ["Fortnightly", "Account sessions with each priority SMU client partner on triggers and joint plays.", "Me, client partners"],
            ["Monthly", "Alliance pipeline review with Adobe, Salesforce, SAP and Pega partner managers, matched against their registered opportunities.", "Me, alliance managers"],
            ["Quarterly", "Book review: bookings against target, coverage for the next two quarters, and qualify-out decisions.", "Me, DX leadership"],
            ["Each large pursuit", "Deal reviews at qualification, solution and price, with the leadership sponsor briefed before client meetings.", "Pursuit team, deal desk"],
        ],
        caption="Operating rhythm",
    )

    body = (
        phead("Portfolio", "Portfolio Maths",
              "A $25m bookings target breaks down into a number of meetings, opportunities and wins. The calculator below works it out from assumptions you can change, so the conversation can be about the inputs.")
        + block("Calculator", "From target to weekly activity", calc,
                "The defaults assume 60% of bookings come from accounts where Wipro already sells, at twice the win rate of new logos. Move any input to test a different book.")
        + block("Book", "Three parts of the book", book,
                "I would sort every account in the portfolio into one of three groups in the first month, because each group needs a different kind of selling and a different pipeline coverage.")
        + block("Rhythm", "Operating rhythm", rhythm,
                "Matrix selling depends on regular meetings with people who do not report to me. This is the cadence I would set up in the first 30 days.")
        + '<section class="wrap notes"><h3>Assumptions</h3><p>Win rates, deal sizes and meeting ratios are working assumptions drawn from my own pipeline experience in consulting. They are not Wipro data. First-year revenue assumes bookings arrive evenly through the year and bill evenly over the contract.</p></section>'
    )
    page("portfolio.html", body, "Pipeline, coverage and activity maths for a $20m to $25m DX bookings target.", js)
