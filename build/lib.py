"""Shared page shell for the Wipro application site: head, navigation, pager, footer and small HTML helpers."""
import html, json, os, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(str(s), quote=True)

# nav order; file, short label, page title
PAGES = [
    ("overview.html", "Overview", "Overview"),
    ("role.html", "Role", "Role Anatomy"),
    ("operating-model.html", "Matrix", "Operating Matrix"),
    ("market.html", "Market", "Market and Competitors"),
    ("triggers.html", "Triggers", "Buying Triggers"),
    ("accounts.html", "Accounts", "Account Map"),
    ("pursuit.html", "Pursuit", "Pursuit Model"),
    ("portfolio.html", "Portfolio", "Portfolio Maths"),
    ("plan.html", "Plan", "First 180 Days"),
    ("fit.html", "Fit", "Fit and Evidence"),
    ("cv.html", "CV", "CV"),
]
TITLES = {f: t for f, _, t in PAGES}
GUARD_PAGES = [f for f, _, _ in PAGES]

# password page: only a salted hash is stored
SALT = "wipro-dx-2026:"


def nav(cur):
    links = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == cur else ""}>{E(l)}</a>' for f, l, _ in PAGES
    )
    return (
        '<header class="sitenav"><div class="in">'
        '<a class="brand" href="overview.html">Arpan Bakshi<span>Wipro Digital Experience</span></a>'
        '<button class="theme" type="button" aria-label="Switch to dark mode">Dark</button>'
        '<button class="menu" type="button" aria-expanded="false" aria-controls="sitelinks">Menu</button>'
        f'<nav class="links" id="sitelinks" aria-label="Site pages">{links}</nav></div></header>'
    )


NAV_JS = """<script>(function(){var r=document.documentElement,t=document.querySelector('.sitenav .theme');function cur(){return r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}function show(){var d=cur()==='dark';t.textContent=d?'Light':'Dark';t.setAttribute('aria-label','Switch to '+(d?'light':'dark')+' mode')}if(t){t.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('theme',n)}catch(e){}show();document.dispatchEvent(new Event('themechange'))});show()}var b=document.querySelector('.sitenav .menu'),l=document.getElementById('sitelinks');if(!b)return;b.addEventListener('click',function(){var o=l.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'Close':'Menu'});l.addEventListener('click',function(e){if(e.target.tagName==='A'){l.classList.remove('open');b.textContent='Menu';b.setAttribute('aria-expanded','false')}})})();</script>"""

HEAD_JS = """<script>try{if(sessionStorage.getItem("pw")!=="ok"){document.documentElement.style.visibility="hidden";location.replace("index.html?next="+encodeURIComponent(location.pathname.split("/").pop()||"overview.html"))}}catch(e){location.replace("index.html")}</script>
<script>try{var s=localStorage.getItem("theme");if(s==="light"||s==="dark")document.documentElement.setAttribute("data-theme",s)}catch(e){}</script>"""

FAVICON = "data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%277%27 fill=%27%234a1fb8%27/%3E%3C/svg%3E"


def head(title, desc, guard=True, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="noindex">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{FAVICON}">
{HEAD_JS if guard else '<script>try{var s=localStorage.getItem("theme");if(s==="light"||s==="dark")document.documentElement.setAttribute("data-theme",s)}catch(e){}</script>'}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="stylesheet" href="assets/apple.css">
{extra}
</head>"""


def pager(cur):
    files = [f for f, _, _ in PAGES]
    i = files.index(cur)
    out = ""
    if i > 0:
        f = files[i - 1]
        out += f'<a class="prev" href="{f}"><small>Previous</small><b>{E(TITLES[f])}</b></a>'
    if i < len(files) - 1:
        f = files[i + 1]
        out += f'<a class="next" href="{f}"><small>Next</small><b>{E(TITLES[f])}</b></a>'
    return f'<nav class="pager" aria-label="Previous and next page">{out}</nav>'


FOOT = (
    '<footer class="site-foot"><span>Prepared by Arpan Bakshi for the Wipro Director, Digital Experience (DX) role. '
    'Drafted October 2026 from public sources cited on each page.</span>'
    '<span>Wipro is a trademark of Wipro Limited. This site is independent and not produced or endorsed by Wipro.</span></footer>'
)


def page(fname, body, desc, scripts=""):
    title = TITLES[fname]
    doc = (
        head(f"{title} | Arpan Bakshi", desc)
        + '\n<body>\n<a class="skip" href="#main">Skip to content</a>\n'
        + nav(fname)
        + NAV_JS
        + f'\n<main id="main" tabindex="-1">\n{body}\n</main>\n'
        + pager(fname)
        + FOOT
        + STEPPER
        + REVEAL_JS
        + scripts
        + "\n</body>\n</html>\n"
    )
    doc = doc.replace('<div class="rail rv">', '<div class="rail rv" tabindex="0" role="region" aria-label="Cards, scroll sideways">')
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote", fname, len(doc))


# small helpers
def phead(eyebrow, h1, lede, meta=""):
    m = f'<p class="meta">{meta}</p>' if meta else ""
    return f'<header class="phead wrap"><p class="eyebrow">{E(eyebrow)}</p><h1 style="margin-top:14px">{E(h1)}</h1><p class="lede">{lede}</p>{m}</header>'


def block(eyebrow, h2, inner, intro="", id=""):
    i = f'<p class="intro">{intro}</p>' if intro else ""
    idattr = f' id="{id}"' if id else ""
    return f'<section class="block wrap"{idattr}><p class="eyebrow">{E(eyebrow)}</p><h2>{E(h2)}</h2>{i}{inner}</section>'


def src(items):
    """items: list of (label, url)"""
    return '<p class="src">Sources: ' + "; ".join(f'<a href="{E(u)}">{E(l)}</a>' for l, u in items) + "</p>"


def dots(n, of=5, label=""):
    lab = label or f"{n} of {of}"
    return f'<span class="dots" role="img" aria-label="{E(lab)}">' + "".join(
        f'<i class="{"on" if k < n else ""}"></i>' for k in range(of)
    ) + "</span>"


def heat(n, text=None):
    return f'<span class="cell h{max(0,min(4,int(n)))}">{E(text if text is not None else n)}</span>'


def table(headers, rows, cls="t", caption=""):
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    body = ""
    for r in rows:
        attrs = ""
        if isinstance(r, dict):
            attrs = r.get("attrs", "")
            r = r["cells"]
        cells = ""
        for k, c in enumerate(r):
            if k == 0:
                cells += f'<th scope="row">{c}</th>'
            else:
                cells += f"<td>{c}</td>" if not (isinstance(c, tuple)) else f'<td class="{c[1]}">{c[0]}</td>'
        body += f"<tr{attrs}>{cells}</tr>"
    cap = f'<caption class="sr">{E(caption)}</caption>' if caption else ""
    return f'<div class="tbl-wrap" tabindex="0" role="region" aria-label="{E(caption or "Table")}"><table class="{cls}">{cap}<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def jsdata(name, obj):
    return f"<script>window.{name}={json.dumps(obj, ensure_ascii=False)};</script>"


STEPPER = """<nav class="stepper" aria-label="Move between sections">
<button type="button" class="st-up" aria-label="Previous section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 15l6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
<span class="st-n" aria-live="polite"></span>
<button type="button" class="st-down" aria-label="Next section"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button></nav>
<script>(function(){var S=[].slice.call(document.querySelectorAll('main>section,.pager')),up=document.querySelector('.st-up'),dn=document.querySelector('.st-down'),n=document.querySelector('.st-n');
function off(){var h=document.querySelector('.sitenav');return h?h.getBoundingClientRect().height:0}
function tops(){return S.map(function(e){return Math.round(e.getBoundingClientRect().top+scrollY-off())})}
function cur(){var t=tops(),y=scrollY+2,i=0;for(var k=0;k<t.length;k++){if(t[k]<=y)i=k}return i}
function go(d){var t=tops(),y=scrollY,i,page=innerHeight-off(),to;if(d>0){for(i=0;i<t.length;i++){if(t[i]>y+4)break}
to=i<t.length?t[i]:document.documentElement.scrollHeight;if(to-y>page+4)to=y+page}else{for(i=t.length-1;i>=0;i--){if(t[i]<y-4)break}
to=i>=0?t[i]:0;if(y-to>page+4)to=y-page}
var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;scrollTo({top:Math.max(0,Math.round(to)),behavior:rm?'auto':'smooth'})}
up.addEventListener('click',function(){go(-1)});dn.addEventListener('click',function(){go(1)});
function upd(){var i=cur(),t=tops(),atEnd=scrollY+innerHeight>=document.documentElement.scrollHeight-4;up.disabled=scrollY<4;dn.disabled=atEnd||i>=S.length-1&&scrollY>=t[t.length-1]-4;n.textContent=(i+1)+' / '+S.length}
addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
addEventListener('keydown',function(e){if(e.target.closest&&e.target.closest('input,textarea,select,[contenteditable]'))return;if(e.key==='PageDown'||(e.key===' '&&!e.shiftKey&&e.target===document.body)){e.preventDefault();go(1)}else if(e.key==='PageUp'||(e.key===' '&&e.shiftKey&&e.target===document.body)){e.preventDefault();go(-1)}})})();</script>"""

REVEAL_JS = """<script>(function(){var t=new Date();t.setHours(0,0,0,0);document.querySelectorAll('[data-days]').forEach(function(e){var d=new Date(e.dataset.days+'T00:00:00');e.textContent=Math.max(0,Math.round((d-t)/864e5))})})();document.querySelectorAll('[data-scroll-end]').forEach(function(s){var p=s.parentElement;while(p&&!(p.scrollWidth>p.clientWidth))p=p.parentElement;if(p)p.scrollLeft=p.scrollWidth});(function(){var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
function count(el){var to=parseFloat(el.dataset.to),dec=(el.dataset.to.split('.')[1]||'').length,pre=el.dataset.pre||'',suf=el.dataset.suf||'';
if(rm){el.textContent=pre+to.toFixed(dec)+suf;return}var t0=null;function f(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/1400),e=1-Math.pow(1-k,3);el.textContent=pre+(to*e).toFixed(dec)+suf;if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
var els=document.querySelectorAll('.rv,[data-to]');
if(!('IntersectionObserver' in window)||rm){els.forEach(function(e){e.classList.add('in');if(e.dataset.to)count(e)});return}
var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');if(x.target.dataset.to)count(x.target);io.unobserve(x.target)}})},{threshold:.18});
els.forEach(function(e){io.observe(e)})})();
(function(){document.querySelectorAll('[data-xp]').forEach(function(x){var dEl=x.querySelector('script.xp-data');if(!dEl)return;var D=JSON.parse(dEl.textContent),P=x.querySelector('.xp-panel'),ms=x.querySelectorAll('[data-pick]');
function show(m){ms.forEach(function(n){n.classList.toggle('on',n===m);n.setAttribute('aria-pressed',String(n===m))});x.classList.add('xp-dim');P.innerHTML=D[m.dataset.pick]||''}
ms.forEach(function(m){m.setAttribute('tabindex','0');m.setAttribute('role','button');m.addEventListener('click',function(){show(m)});m.addEventListener('mouseenter',function(){show(m)});m.addEventListener('focus',function(){show(m)});
m.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();show(m)}})});
var first=x.dataset.first&&x.querySelector('[data-pick="'+x.dataset.first+'"]');if(first)show(first)})})();</script>"""


def sec(inner, theme="", narrow=False, center=False, id=""):
    cls = "sec" + (f" {theme}" if theme else "")
    idattr = f' id="{id}"' if id else ""
    return f'<section class="{cls}"{idattr}><div class="sec-in{" narrow" if narrow else ""}{" center" if center else ""}">{inner}</div></section>'


def head_block(kicker, title, sub="", size="h-xl", grad=True):
    k = f'<p class="kicker{" grad" if grad else ""}">{E(kicker)}</p>' if kicker else ""
    s = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div class="rv">{k}<h2 class="{size}">{E(title)}</h2>{s}</div>'


HERO_IMG = {
    "Wipro · Director, Digital Experience": ("overview", "An executive reviewing glowing customer journey diagrams on a wall display at dusk"),
    "Role Anatomy": ("role", "Two people sketching a customer journey on a wall of wireframes"),
    "Operating Matrix": ("matrix", "A city grid at night joined by streams of light"),
    "Market and Competitors": ("market", "A hand holding a phone with a shopping interface in a store"),
    "Buying Triggers": ("triggers", "A watch movement lit in violet and blue"),
    "Account Map": ("accounts", "A corridor of doors with one open and lit"),
    "Pursuit Model": ("pursuit", "A stone staircase rising toward a skylight"),
    "Portfolio Maths": ("portfolio", "People moving through a bright office atrium"),
    "First 180 Days": ("plan", "A straight desert road toward the horizon at sunrise"),
    "Fit and Evidence": ("fit", "Two machined aluminium pieces fitting together"),
}


def hero(kicker, title, sub, art="", cta="", dark=False):
    c = f'<div class="cta">{cta}</div>' if cta else ""
    img = HERO_IMG.get(kicker)
    have = img and os.path.exists(os.path.join(ROOT, "assets", "hero", img[0] + ".webp"))
    if have:
        top = (f'<section class="hero-photo"><img class="hp-img" src="assets/hero/{img[0]}.webp" alt="{E(img[1])}" width="2048" height="1152" fetchpriority="high">'
               f'<div class="hp-shade" aria-hidden="true"></div><div class="sec-in hp-copy"><p class="kicker grad">{E(kicker)}</p>'
               f'<h1 class="xl">{E(title)}</h1><p class="sub">{sub}</p>{c}</div></section>')
        if not art:
            return top
        return top + f'<section class="sec hero-art{" dark" if dark else ""}"><div class="sec-in"><div class="art rv" style="margin-top:0">{art}</div></div></section>'
    a = f'<div class="art rv">{art}</div>' if art else ""
    return (f'<section class="hero-x{" dark sec" if dark else ""}"><div class="sec-in"><p class="kicker grad">{E(kicker)}</p>'
            f'<h1 class="xl">{E(title)}</h1><p class="sub">{sub}</p>{c}</div>{a}</section>')


def tile(inner, span=4, cls="", href=""):
    if href:
        return f'<a class="tile s{span} rv link {cls}" href="{href}">{inner}</a>'
    return f'<div class="tile s{span} rv {cls}">{inner}</div>'


def more(label, inner):
    return f'<details class="more"><summary>{E(label)}</summary><div class="body">{inner}</div></details>'


def num(to, pre="", suf="", small=""):
    sm = f"<small>{small}</small>" if small else ""
    return f'<div class="num"><span data-to="{to}" data-pre="{E(pre)}" data-suf="{E(suf)}">{E(pre)}{to}{E(suf)}</span>{sm}</div>'


ICONS = {
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>',
    "ladder": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20V14h5v6M9.5 20V9h5v11M15 20V4h5v16"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.2"/><path d="M3 19c.8-3.2 3.2-5 6-5s5.2 1.8 6 5"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c2.4.1 4.4 1.7 5 4.3"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"/><path d="M19 16l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4v16h16"/><path d="M7 15l4-4 3 3 5-6"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 3v6c0 4.4-3 7.6-7 9-4-1.4-7-4.6-7-9V6z"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/></svg>',
    "door": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M6 21V4h10v17M3 21h18"/><circle cx="13" cy="12.5" r="1" fill="currentColor"/></svg>',
    "pen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S9.4 5.6 12 3z"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 3L5 13h6l-1 8 8-10h-6z"/></svg>',
}


def icon(name):
    return f'<div class="ic" aria-hidden="true">{ICONS[name]}</div>'


def explorer(art, data, hint="Select any mark to see its detail.", first="", stack=False):
    """art: svg with [data-pick] groups; data: {key: html}"""
    import json as _j
    art = art.replace('role="img"', 'role="group"', 1)
    data = {k: v.replace("<h3>", '<h2 class="xh">').replace("</h3>", "</h2>") for k, v in data.items()}
    blob = _j.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    f = f' data-first="{first}"' if first else ""
    return (f'<div class="xp{" stack" if stack else ""} rv" data-xp{f}><div class="xp-art">{art}</div>'
            f'<div class="xp-panel" aria-live="polite"><p class="hint">{E(hint)}</p></div>'
            f'<script type="application/json" class="xp-data">{blob}</script></div>')


def card_html(kicker, title, *paras):
    return f'<p class="t-k">{E(kicker)}</p><h3>{E(title)}</h3>' + "".join(f"<p>{p}</p>" for p in paras)
