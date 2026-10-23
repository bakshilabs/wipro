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
<link rel="stylesheet" href="assets/site.css">
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
        + scripts
        + "\n</body>\n</html>\n"
    )
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
