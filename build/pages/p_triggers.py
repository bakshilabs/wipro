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


def lanes_svg():
    W, H = 1000, 250
    x0, x1 = 170, 980
    d0, d1 = datetime.date(2025, 1, 1), datetime.date(2028, 12, 31)
    span = (d1 - d0).days
    X = lambda d: x0 + (x1 - x0) * (d - d0).days / span
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="lt ld"><title id="lt">Buying triggers 2025 to 2028 by category</title><desc id="ld">{len(T)} dated triggers. The densest period is the second half of 2026 to the first half of 2027.</desc>']
    for y in range(2025, 2029):
        x = X(datetime.date(y, 1, 1))
        o.append(f'<line x1="{x}" x2="{x}" y1="20" y2="{H-30}" stroke="var(--line)"/><text x="{x+6}" y="{H-12}" font-size="12" class="svg-muted">{y}</text>')
    tx = X(TODAY)
    o.append(f'<line x1="{tx}" x2="{tx}" y1="10" y2="{H-30}" stroke="var(--ink)" stroke-dasharray="3 3"/><text x="{tx+5}" y="16" font-size="11.5" class="svg-ink">Today, 23 Oct 2026</text>')
    for k, (key, (lab, c)) in enumerate(CATS.items()):
        y = 44 + k * 48
        o.append(f'<text x="0" y="{y+5}" font-size="12.5" class="svg-ink">{lab}</text><line x1="{x0}" x2="{x1}" y1="{y}" y2="{y}" stroke="var(--line)" stroke-width="0.6"/>')
        for d, cat, title, *_ in T:
            if cat != key:
                continue
            dd = datetime.date.fromisoformat(d)
            past = dd < TODAY
            o.append(f'<circle cx="{X(dd):.1f}" cy="{y}" r="8" fill="var(--{c})" opacity="{0.4 if past else 1}" stroke="var(--panel)" stroke-width="2"><title>{E(d)}: {E(title)}</title></circle>')
    o.append("</svg>")
    return "".join(o)


def build():
    filt = '<div class="filters" role="group" aria-label="Filter triggers"><button type="button" data-c="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-c="{k}" aria-pressed="false">{E(v[0])}</button>' for k, v in CATS.items()) + '<button type="button" data-c="future" aria-pressed="false">Still ahead</button></div>'
    items = ""
    for d, cat, title, who, forces, buyer, signal, play, url in T:
        dd = datetime.date.fromisoformat(d)
        past = dd < TODAY
        items += (
            f'<div class="tl-item{" past" if past else ""}" data-c="{cat}" data-f="{0 if past else 1}">'
            f'<p class="d">{dd.strftime("%-d %B %Y")} <span class="chip plain" style="margin-left:6px">{E(CATS[cat][0])}</span></p>'
            f'<h3>{E(title)}</h3>'
            f'<p><b>Affects</b> {E(who)}. <b>Forces</b> {E(forces)}. <b>Buyer</b> {E(buyer)}.</p>'
            f'<p><b>Signal to watch</b> {E(signal)}. <b>Wipro play</b> {E(play)}. <a href="{E(url)}">Source</a></p></div>'
        )
    js = """<script>(function(){var bs=document.querySelectorAll('.filters button[data-c]'),it=document.querySelectorAll('.tl-item');
bs.forEach(function(b){b.addEventListener('click',function(){var c=b.dataset.c;bs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
it.forEach(function(i){i.style.display=(c==='all'||i.dataset.c===c||(c==='future'&&i.dataset.f==='1'))?'':'none'})})})})();</script>"""
    leg = "".join(f'<span><i style="background:var(--{c})"></i>{E(l)}</span>' for l, c in CATS.values())

    signals = table(
        ["Signal", "What to look for", "Where", "Lead time"],
        [
            ["Tech-stack scans", "AEM 6.5 against AEM cloud hosts, Sitecore version headers, Drupal version, SAP Commerce storefront paths, legacy Salesforce chat scripts.", "BuiltWith, Wappalyzer", "Twelve months or more before the support date"],
            ["Job postings", "Contract roles for AEM cloud migration, SitecoreAI, composable commerce architects, WCAG remediation, FHIR APIs, Agentforce.", "LinkedIn, Indeed, company career sites", "Three to nine months: a programme is being scoped"],
            ["Annual and quarterly reports", "New risk factors on accessibility litigation, words such as replatform, one platform, direct to consumer, segment changes after spin-offs.", "SEC EDGAR full-text search", "Year-on-year changes signal next year's budget"],
            ["Earnings calls", "Mentions of digital experience, AI search traffic, agentic commerce, cost take-out and reinvestment in marketing.", "Investor relations sites, transcript services", "Budget direction for the next two quarters"],
            ["Leadership changes", "New CMO, CDO, CIO or CEO.", "Press releases, LinkedIn", "First 90 days set the agenda; platform decisions follow within a year"],
            ["Corporate actions", "Form 10 filings for spin-offs, merger close dates, transition services agreement terms.", "SEC EDGAR 8-K and Form 10", "TSA expiry is a fixed date, usually 12 to 24 months after close"],
            ["Partner lists", "Adobe and Salesforce account teams' migration and renewal lists.", "Adobe and Salesforce partner portals", "Vendors often fund migration work, so register early"],
            ["Public procurement", "Website, CMS and WCAG 2.1 AA tenders ahead of the April 2027 ADA Title II date.", "SAM.gov, state portals, CanadaBuys", "RFP published, usually three to six months to award"],
        ],
        caption="Lead signals and where to find them",
    )
    par = table(
        ["Pattern", "In net zero consulting, which I sold", "In digital experience"],
        [[E(a), E(b), E(c)] for a, b, c in PARALLEL],
        caption="Buying patterns compared",
    )

    body = (
        phead("Triggers", "Buying Triggers",
              "Large digital experience programmes start when something with a date on it forces a decision. Between now and the end of 2028 a cluster of platform support deadlines and accessibility rules lands on Wipro's focus industries. This page lists them, shows what each one forces and names the signal that reveals which clients are affected.",
              "Dates checked against vendor support pages, the Federal Register and company releases in October 2026. The US accessibility deadlines moved back a year in April and May 2026.")
        + block("Calendar", "Trigger calendar, 2025 to 2028", f'<figure class="fig">{lanes_svg()}<div class="legend">{leg}<span>Faded dots are past.</span></div><figcaption>Hover a dot for its trigger. The densest window runs from the second half of 2026 to the end of 2027, which is the first eighteen months of this role.</figcaption></figure>')
        + block("Detail", "What each trigger forces", filt + f'<div class="tl">{items}</div>',
                "Each entry names who is affected, what the event forces them to do, who buys, how to spot it and the Wipro offer that answers it.")
        + block("Signals", "How to find the affected clients", signals,
                "A trigger is only useful when it is matched to a named client before that client goes to market. These are the signals I would monitor every week.")
        + block("Pattern", "The same buying pattern I sold in net zero", par,
                "Net zero transformation and digital experience transformation are bought the same way. A deadline creates urgency, a baseline assessment creates the case, and a multi-year programme follows.")
        + '<section class="wrap notes"><h3>Caveats</h3><ul><li>Adobe Campaign Classic v7 is left out because Adobe\'s support matrix gives 31 December 2030 while some consultancies cite 31 March 2027.</li><li>Salesforce has published no retirement date for SFRA, PWA Kit or Marketing Cloud Engagement, so none is claimed.</li><li>The SAP Commerce 2205 date comes from secondary sources.</li><li>The CMO tenure figure covers the S&amp;P 500 and is not comparable with earlier Fortune 500 studies.</li></ul></section>'
    )
    page("triggers.html", body, "Dated platform, regulation, organisational and AI triggers for DX buying, 2025 to 2028, with lead signals.", js)
