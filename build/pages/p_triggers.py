from lib import *
import datetime

# curated from the research file; each item: date, category, title, who, what it forces, buyer, signal, wipro play, source
T = [
    ("2025-04-29", "ai", "Mastercard Agent Pay launched, followed by Visa Intelligent Commerce on 30 April", "Merchants and issuers", "Agent-ready checkout, tokenisation and bot management", "Chief digital or commerce officer", "Agentic commerce pilots, bot management changes at the CDN", "Agent-ready commerce assessment bundled with a commerce rebuild", "https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai"),
    ("2025-05-12", "org", "Gartner CMO Spend Survey: marketing budgets flat at 7.7% of revenue", "Enterprise marketing organisations", "Agency consolidation and AI productivity programmes", "CMO and CFO", "Agency reviews, martech rationalisation", "Self-funding managed content and martech operations", "https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-2025-cmo-spend-survey-reveals-marketing-budgets-have-flatlined-at-seven-percent-of-overall-company-revenue"),
    ("2025-06-28", "reg", "European Accessibility Act applies to e-commerce, banking and travel services sold in the EU", "US multinationals with EU consumer sites and apps", "Accessibility remediation and design-system rework", "CDO, compliance, CMO", "EU accessibility statements, 10-K risk factors", "Accessibility remediation programme run from US and nearshore centres", "https://eur-lex.europa.eu/eli/dir/2019/882/oj"),
    ("2025-07-22", "ai", "Pew finds users click a result in 8% of visits with an AI summary against 15% without", "Retailers, publishers, B2B content marketers", "Content and site structure for AI answers", "CMO, head of content", "Organic traffic decline mentioned on earnings calls", "Content model redesign and generative engine optimisation", "https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/"),
    ("2025-09-29", "ai", "OpenAI and Stripe launch the Agentic Commerce Protocol", "Retailers and brands", "Product feed and catalogue readiness for AI assistants", "CDO, e-commerce lead", "ACP and feed management projects", "Product data and feed readiness as a fixed-price entry offer", "https://openai.com/index/buy-it-in-chatgpt/"),
    ("2026-01-01", "reg", "Indiana, Kentucky and Rhode Island privacy laws take effect", "Consumer brands with US customers", "Consent management, preference centres, data mapping", "CMO, chief privacy officer", "Consent platform changes", "Consent and CDP governance as part of a martech rebuild", "https://www.koleyjessen.com/insights/publications/new-state-privacy-laws-effective-january-1-2026-indiana-kentucky-and-rhode-island"),
    ("2026-01-11", "ai", "Google launches the Universal Commerce Protocol at NRF with Shopify, Target and Walmart", "US retailers selling through Google AI Mode and Gemini", "Merchant feed quality and native checkout integration", "Chief commerce officer", "UCP adoption announcements", "Agentic commerce integration on SAP, Adobe or Shopify storefronts", "https://developers.googleblog.com/en/under-the-hood-universal-commerce-protocol-ucp/"),
    ("2026-01-31", "org", "Spencer Stuart: S&P 500 CMO tenure averages 4.1 years, 3.5 in consumer", "S&P 500 marketing organisations", "Frequent new leaders who review platforms and agencies", "New CMO or CDO", "Appointment announcements", "Meet each new CMO in the first 90 days with an audit of their estate", "https://spencerstuart.com/research-and-insight/cmo-tenure-2026-snapshot-of-an-expanding-role-for-marketing-leaders"),
    ("2026-02-05", "reg", "TrumpRx.gov goes live and routes cash-pay patients to manufacturers' own sites", "Pharma manufacturers including Pfizer, Lilly, Novo Nordisk and AstraZeneca", "Direct-to-patient commerce, pricing pages and checkout", "Pharma CDO, head of consumer", "New DTC storefronts and pharma e-commerce hires", "Digital patient services from the DX life sciences offer", "https://healthexec.com/topics/healthcare-management/healthcare-logistics/trumprx-launches-40-brand-name-medications-available-including-popular-weight-loss-drugs"),
    ("2026-02-14", "eol", "Salesforce retires Legacy Chat", "Service Cloud customers still on Legacy Chat", "Move to Enhanced Chat with Agentforce, often a contact-centre redesign", "Chief customer officer, CIO", "Legacy chat scripts on the client's site", "Agentforce service redesign with Wipro's Salesforce practice", "https://help.salesforce.com/s/articleView?id=001790618&language=en_US&type=1"),
    ("2026-05-01", "eol", "Dynamics 365 Customer Insights outbound marketing removed", "Dynamics marketing customers on outbound journeys", "Rebuild of journeys, segments and reporting, or a martech switch", "CMO, marketing operations", "Dynamics marketing job posts", "Martech replatform assessment", "https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/outbound-removal-notes"),
    ("2026-06-01", "eol", "Sitecore makes security fixes in the extended support phase a paid service", "Sitecore 10.0 to 10.3 customers", "Higher run cost, which strengthens the upgrade or replatform case", "CIO, CDO", "Sitecore version detection", "Total cost comparison of upgrade, SitecoreAI and Adobe", "https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB0641167"),
    ("2026-06-29", "org", "Honeywell completes the Aerospace spin-off", "Honeywell Aerospace and Honeywell Technologies", "New brand, domains, DXP, CRM and martech under a transition services agreement", "CDO and CMO of the new company", "Form 10 filings and TSA expiry dates", "Separation programme for the digital estate with a fixed exit date", "https://www.honeywell.com/us/en/news/press-releases/2026/06/honeywell-board-of-directors-approves-spin-off-of-honeywell-aerospace"),
    ("2026-07-31", "eol", "SAP Commerce on-premises 2205 reaches end of mainstream maintenance", "SAP Commerce (Hybris) B2B and B2C customers", "Move to SAP Commerce Cloud or composable commerce", "CIO, chief digital officer", "Storefront fingerprints and Hybris developer job posts", "Commerce replatform with the SAP practice", "https://www.riministreet.com/blog/sap-end-of-mainstream-maintenance-deadlines-are-looming-for-gts-bobj-bpc-bw-hybris/"),
    ("2026-08-31", "eol", "AEM 6.5 core support ends on Adobe Managed Services", "Enterprises running AEM 6.5 on Adobe Managed Services", "Move to AEM as a Cloud Service, with content and component refactoring", "CDO, CMO, CIO", "AEM 6.5 detected by tech-stack scans, migration job posts", "AEM cloud migration with an experience redesign and managed run", "https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html"),
    ("2026-12-09", "eol", "Drupal 10 reaches end of life", "Drupal 10 site owners, many in public sector and higher education", "Upgrade to Drupal 11 or a CMS change", "CIO, director of digital", "Drupal version detection, website RFPs", "Bundle with ADA Title II remediation for public entities", "https://www.drupal.org/about/core/policies/core-release-cycles/schedule"),
    ("2026-12-31", "eol", "Sitecore 10.0 and 10.1 extended support ends", "Sitecore XP and XM 10.0 and 10.1 customers", "Upgrade to 10.4 or 10.5, SitecoreAI, or another DXP", "CMO, CDO, CIO", "Sitecore version detection, SitecoreAI job posts", "DXP decision workshop led by Designit, then migration", "https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB0641167"),
    ("2027-01-01", "reg", "CMS-0057-F payer API deadline for patient access, provider access and prior authorisation", "Medicare Advantage, Medicaid and ACA plan payers", "FHIR APIs and member and provider portal redesign", "Payer CDO, chief member experience officer", "FHIR job posts, payer RFPs", "Member experience redesign alongside Wipro's health platforms", "https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f"),
    ("2027-02-28", "eol", "AEM 6.5 on-premises core support ends, with extended support to 28 February 2028", "Enterprises running AEM 6.5 on premises", "Cloud migration or long-term-support upgrade, often with a redesign", "CDO, CMO, CIO", "AEM version fingerprints, Adobe renewal dates", "Largest single replatform pool for 2027 deals", "https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-42541"),
    ("2027-04-26", "reg", "ADA Title II web rule applies to public entities serving 50,000 people or more", "State and local governments, public universities, transit and utilities", "WCAG 2.1 AA remediation of web, apps and documents", "State CIO, university CIO", "Accessibility and website RFPs", "Accessibility remediation factory with managed testing", "https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web"),
    ("2027-05-11", "reg", "HHS Section 504 web and mobile accessibility applies to recipients with 15 or more staff", "Hospitals, health systems and HHS-funded universities", "WCAG 2.1 AA across web, patient portals and apps", "Health system CDO, CMO", "Accessibility audit RFPs, patient portal redesigns", "Patient portal and app redesign for health clients", "https://www.federalregister.gov/documents/2026/05/11/2026-09266/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web"),
    ("2027-12-05", "reg", "Accessible Canada Act digital rules apply to federal public sector web pages", "Canadian federal departments and Crown corporations", "EN 301 549 conformance for new and updated pages", "Federal CIO or CDO", "CanadaBuys tenders", "Canadian public sector accessibility work", "https://www.canada.ca/en/employment-social-development/programs/accessible-canada-regulations-guidance/digital-technologies-phase-1.html"),
    ("2027-12-31", "eol", "Sitecore 10.4 mainstream support ends", "Sitecore XP and XM 10.4 customers", "Decision on 10.5, SitecoreAI or another DXP", "CMO, CDO, CIO", "Sitecore version, DXP shortlist inquiries", "Second wave of DXP decisions", "https://support.sitecore.com/kb?id=kb_article_view&sysparm_article=KB0641167"),
    ("2028-02-28", "eol", "AEM 6.5 extended support ends", "Remaining AEM 6.5 on-premises sites", "Final forced migration", "CIO, CDO", "Continued 6.5 detection through 2027", "Late-mover migrations at lower margin", "https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-42541"),
    ("2028-12-05", "reg", "Accessible Canada Act digital rules apply to large federally regulated private companies", "Canadian banks, telecoms, airlines and broadcasters", "EN 301 549 conformance and accessibility statements", "CDO, CMO, compliance", "Accessibility roles, design-system projects", "Canadian banking accessibility, with Americas 2", "https://www.canada.ca/en/employment-social-development/programs/accessible-canada-regulations-guidance/digital-technologies-phase-1.html"),
]
CATS = {"eol": ("Platform end of support", "c0"), "reg": ("Regulation", "c2"), "org": ("Organisation and budget", "c3"), "ai": ("AI and commerce", "c1")}
TODAY = datetime.date(2026, 10, 23)

PARALLEL = [
    ("A dated regulation with penalties", "New York City Local Law 97 set carbon limits for large buildings from 2024, with fines per tonne over the limit. Owners bought audits, then retrofits.", "ADA Title II from April 2027 and HHS Section 504 from May 2027 set WCAG 2.1 AA as the legal standard. Owners will buy audits, then remediation and redesign."),
    ("An asset that becomes unusable", "The UK minimum energy efficiency standard stopped landlords letting buildings rated F or G. The building still stood but could not earn rent.", "A platform past end of support still runs but cannot be patched. AEM 6.5 on premises reaches that point in February 2027."),
    ("Disclosure that exposes the gap", "The EU Corporate Sustainability Reporting Directive made companies publish emissions data, and the gap between pledge and performance became visible to investors.", "AI answers reduce clicks on organic results, and the drop shows up in traffic and revenue reports that executives read."),
    ("A portfolio assessment as the way in", "I won a multi-year contract to write a sustainability vision plan for a global pharmaceutical company's property portfolio, starting from a baseline of every site.", "A scan of a client's whole digital estate (platforms, versions, accessibility, page speed) gives the same baseline, and the same route to a multi-year programme."),
]


SHORT = {
    "2026-12-31": "Sitecore 10.0 and 10.1 support ends", "2027-02-28": "AEM 6.5 on-premises core support ends",
    "2027-04-26": "ADA Title II web rule applies", "2027-05-11": "HHS Section 504 web rule applies",
}
COUNT = ["2026-12-31", "2027-02-28", "2027-04-26", "2027-05-11"]


def lanes_svg():
    W, H = 1100, 330
    x0, x1 = 200, 1080
    d0, d1 = datetime.date(2025, 1, 1), datetime.date(2028, 12, 31)
    span = (d1 - d0).days
    X = lambda d: x0 + (x1 - x0) * (d - d0).days / span
    o = [f'<svg data-scroll-end viewBox="0 0 {W} {H}" role="img" aria-labelledby="lt ld"><title id="lt">Buying triggers 2025 to 2028 by category</title><desc id="ld">{len(T)} dated triggers. The densest period runs from late 2026 to the end of 2027.</desc>']
    tx = X(TODAY)
    o.append(f'<rect x="{tx}" y="20" width="{X(datetime.date(2028,4,23))-tx:.0f}" height="{H-70}" fill="var(--accent)" opacity=".08"/>')
    o.append(f'<text x="{tx+10}" y="40" font-size="13" font-weight="600" fill="var(--accent)">The first eighteen months of this role</text>')
    for y in range(2025, 2029):
        x = X(datetime.date(y, 1, 1))
        o.append(f'<line x1="{x}" x2="{x}" y1="20" y2="{H-50}" stroke="var(--line)"/><text x="{x+6}" y="{H-24}" font-size="15" font-weight="600" class="svg-muted">{y}</text>')
    o.append(f'<line x1="{tx}" x2="{tx}" y1="14" y2="{H-50}" stroke="var(--ink)" stroke-width="2"/><text x="{tx-8}" y="14" text-anchor="end" font-size="13" class="svg-ink">Today</text>')
    for k, (key, (lab, c)) in enumerate(CATS.items()):
        y = 80 + k * 58
        o.append(f'<text x="0" y="{y+6}" font-size="16" font-weight="600" class="svg-ink">{lab}</text><line x1="{x0}" x2="{x1}" y1="{y}" y2="{y}" stroke="var(--line)" stroke-width=".7"/>')
        n = 0
        for d, cat, title, *_ in T:
            if cat != key:
                continue
            dd = datetime.date.fromisoformat(d)
            past = dd < TODAY
            o.append(f'<g data-pick="t{T.index(next(t for t in T if t[0]==d and t[2]==title))}" aria-label="{E(title)}"><circle class="pop" style="transition-delay:{.15+n*.12:.2f}s" cx="{X(dd):.1f}" cy="{y}" r="{9 if past else 12}" fill="var(--{c})" opacity="{0.35 if past else 1}" stroke="transparent" stroke-width="8"/></g>')
            n += 1
    o.append("</svg>")
    return "".join(o)


def build():
    leg = "".join(f'<span><i style="background:var(--{c})"></i>{E(l)}</span>' for l, c in CATS.values())
    data = {}
    for k, (d, cat, title, who, forces, buyer, signal, play, url) in enumerate(T):
        dd = datetime.date.fromisoformat(d)
        data[f"t{k}"] = (f'<p class="t-k">{E(dd.strftime("%-d %B %Y"))} · {E(CATS[cat][0])}</p><h3>{E(title)}</h3>'
                         f'<p><b>Forces</b> {E(forces)}</p><p><b>Buyer</b> {E(buyer)}</p><p><b>Wipro play</b> {E(play)} <a href="{E(url)}">Source</a></p>')
    first = next(k for k, t in enumerate(T) if datetime.date.fromisoformat(t[0]) >= TODAY)
    art = explorer(lanes_svg(), data, "Select a dot to see the trigger.", first=f"t{first}", stack=True) + f'<div class="legend" style="justify-content:center">{leg}<span>Faded dots are past.</span></div>'
    body = hero("Buying Triggers", "Dates That Force Decisions",
                "Twenty-five dated reasons to buy digital experience work. Most of them land in the next eighteen months.", art, dark=True)

    cnt = ""
    for i, d in enumerate(COUNT):
        dd = datetime.date.fromisoformat(d)
        cnt += (f'<div class="tile rv d{i+1}"><p class="t-k">{E(dd.strftime("%-d %B %Y"))}</p>'
                f'<div class="days gradtext"><b data-days="{d}">{(dd-TODAY).days}</b><span>days</span></div><h3 style="font-size:20px">{E(SHORT[d])}</h3></div>')
    body += sec(head_block("Countdown", "Time Left", "Counted from today. Each one is a decision someone has to make.") + f'<div class="count">{cnt}</div>')

    # cards for the triggers still ahead
    cards = ""
    for d, cat, title, who, forces, buyer, signal, play, url in T:
        dd = datetime.date.fromisoformat(d)
        if dd < TODAY:
            continue
        lab, c = CATS[cat]
        cards += (f'<div class="tile"><p class="t-k" style="color:var(--{c})">{E(lab)}</p><div style="font:700 34px/1.05 var(--display);letter-spacing:-.03em;margin-top:8px">{E(dd.strftime("%b %Y"))}</div>'
                  f'<h3 style="font-size:20px">{E(title)}</h3><p><b style="color:var(--ink)">Buyer</b> {E(buyer)}</p><p style="margin-top:auto;padding-top:16px"><b style="color:var(--accent)">Wipro play</b> {E(play)}</p></div>')
    body += sec(head_block("Ahead", "What Comes Next", "Swipe through every trigger still ahead, with its buyer and the Wipro answer.") + f'<div class="rail rv">{cards}</div>', "grey")

    # full list in a drawer
    filt = '<div class="filters" role="group" aria-label="Filter triggers"><button type="button" data-c="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-c="{k}" aria-pressed="false">{E(v[0])}</button>' for k, v in CATS.items()) + '<button type="button" data-c="future" aria-pressed="false">Still ahead</button></div>'
    items = ""
    for d, cat, title, who, forces, buyer, signal, play, url in T:
        dd = datetime.date.fromisoformat(d)
        past = dd < TODAY
        items += (f'<div class="tl-item{" past" if past else ""}" data-c="{cat}" data-f="{0 if past else 1}"><p class="d">{dd.strftime("%-d %B %Y")}</p><h3>{E(title)}</h3>'
                  f'<p><b>Affects</b> {E(who)}. <b>Forces</b> {E(forces)}. <b>Signal</b> {E(signal)}. <a href="{E(url)}">Source</a></p></div>')
    body += sec(more("Show all 25 triggers with sources", filt + f'<div class="tl">{items}</div>'), "grey").replace('class="sec grey"', 'class="sec grey" style="padding-top:0"', 1)

    # same pattern: net zero against DX
    rows = ""
    for i, (a, nz, dx) in enumerate(PARALLEL):
        rows += (f'<div class="rv d{i%4+1}" style="display:grid;grid-template-columns:1fr 60px 1fr;gap:16px;align-items:center;margin-top:20px">'
                 f'<div class="tile" style="min-height:0"><p class="t-k">Net zero</p><p style="color:var(--ink)">{E(nz)}</p></div>'
                 f'<svg viewBox="0 0 60 24" aria-hidden="true"><path d="M4 12h44" stroke="var(--accent)" stroke-width="2.5"/><path d="M44 5l10 7-10 7" fill="none" stroke="var(--accent)" stroke-width="2.5"/></svg>'
                 f'<div class="tile" style="min-height:0"><p class="t-k" style="color:var(--accent)">Digital experience</p><p style="color:var(--ink)">{E(dx)}</p></div></div>')
    body += sec(head_block("Pattern", "Same Playbook", "I sold net zero transformation against deadlines. Digital experience is bought the same way.") + f'<div style="margin-top:40px">{rows}</div>', "dark")

    sig = [("grid", "Tech-stack scans", "Platform versions mapped to support dates"), ("people", "Job postings", "Migration and remediation hires"),
           ("chart", "Filings and calls", "New risk factors, replatform language"), ("spark", "Leadership changes", "A new CMO or CDO sets an agenda in 90 days"),
           ("door", "Corporate actions", "Spin-off and merger exit dates"), ("bolt", "Partner lists", "Adobe and Salesforce migration lists")]
    st = "".join(tile(f'{icon(i)}<h3 style="margin-top:20px;font-size:22px">{E(h)}</h3><p>{E(p)}</p>', 4, "short") for i, h, p in sig)
    body += sec(head_block("Signals", "How I Find Them", "Six signals, checked every week.") + f'<div class="bento">{st}</div>')

    js = """<script>(function(){var t=new Date();t.setHours(0,0,0,0);document.querySelectorAll('[data-days]').forEach(function(e){var d=new Date(e.dataset.days+'T00:00:00');e.textContent=Math.max(0,Math.round((d-t)/864e5))});
var bs=document.querySelectorAll('.filters button[data-c]'),it=document.querySelectorAll('.tl-item');
bs.forEach(function(b){b.addEventListener('click',function(){var c=b.dataset.c;bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
it.forEach(function(i){i.style.display=(c==='all'||i.dataset.c===c||(c==='future'&&i.dataset.f==='1'))?'':'none'})})})})();</script>"""
    page("triggers.html", body, "Dated platform, regulation, organisational and AI triggers for DX buying, 2025 to 2028.", js)
