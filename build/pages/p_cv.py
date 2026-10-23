from lib import *


def li(items):
    return "<ul>" + "".join(f"<li>{E(x)}</li>" for x in items) + "</ul>"


def meta(k, v):
    return f'<p class="meta"><b>{E(k)}</b>{E(v)}</p>'


def job(name, date, loc, rev, desc, role, body):
    return (f'<article class="job"><div class="job-top"><h3>{E(name)}</h3><span class="date">{E(date)}</span></div>'
            f'<div class="job-sub"><span>{E(loc)}</span><span>{E(rev)}</span></div><p class="desc">{E(desc)}</p><p class="role">{role}</p>{body}</article>')


def tags(xs):
    return '<div class="tags">' + "".join(f"<span>{E(x)}</span>" for x in xs) + "</div>"


def ent(t, y="", d=""):
    return f'<div class="entry"><div class="eh"><span>{E(t)}</span><span>{E(y)}</span></div>' + (f"<p>{E(d)}</p>" if d else "") + "</div>"


def build():
    atlas = job("Atlas Learn", "Oct 2025 to Present", "London", "", "Atlas Learn trains executive teams and senior professionals to use AI tools in their daily work.", "Co-Founder", li([
        "Run the company's sales, marketing and commercial operations, and design its courses.",
        "Sold and delivered training for the board of directors of a FinTech company, and for another client's chief executive and its heads of HR, marketing and IT.",
        "Trained more than 250 senior professionals to use Claude Code, Cowork and other AI tools in workshops held in Central London.",
    ]))
    foster = job("Foster + Partners", "Oct 2015 to Jul 2026", "London", "Revenue £653m (FY2025)",
                 "Foster + Partners is an architecture and engineering practice with about 2,500 staff. Its buildings include Apple Park, Bloomberg's London headquarters, JPMorgan Chase's New York headquarters and Lusail Stadium.",
                 "Associate Partner, 2020 to 2026 <span>&middot; Associate, 2015 to 2020</span>",
                 '<p class="subhead">Business development and advisory</p>' + li([
                     "Co-created and launched a strategic advisory service line that took the firm into corporate environmental strategy, digital transformation and spatial consulting.",
                     "Led pitches, bids and competition entries that won more than £10 million a year in fees as Associate Partner and more than £5 million a year as Associate.",
                     "Pitched, negotiated and won a multi-year contract with a global pharmaceutical company to write the sustainability vision plan for its property portfolio.",
                     "My presentations to Fortune 500 chief executives helped the design studios win contracts worth more than £10 million.",
                     "Acted as the main technical contact for international developers and institutional clients, setting performance targets that fitted their budgets and ESG commitments.",
                 ]) + '<p class="subhead">Design, digital tools and research</p>' + li([
                     "Developed early design tools that estimate whole life carbon before building elements are designed in enough detail for full analysis.",
                     "Served on the whole life carbon and sustainability leadership teams, and correlated every rating system the firm uses into one framework of ten themes.",
                     "Managed environmental strategy, microclimate analysis and computational modelling on large projects in the UAE, Qatar, Saudi Arabia, Europe and Asia, including Lusail Stadium, San Siro and Old Trafford.",
                 ]) + meta("Clients", "Roche, Genentech, Apple, Oracle, Alibaba, Hyundai, JPMorgan Chase")
                 + meta("Tools", "Rhino 3D, Grasshopper, Revit, Python, C#, Unreal Engine, Claude Code, Copilot Studio, Gemini, NotebookLM"))
    som = job("Skidmore, Owings & Merrill (SOM)", "Oct 2013 to Oct 2015", "New York", "Revenue $347m (2021)",
              "SOM is a Chicago architecture and engineering firm whose buildings include One World Trade Center.", "High Performance Design Lead", li([
                  "Led business development for my department in the New York office, presented to executives at major Wall Street banks and won more than $3 million a year in fees.",
                  "Led environmental and building performance strategy for tall buildings and large urban projects in North America and abroad.",
                  "Brought simulation into early design stages to improve energy performance and cut carbon emissions.",
              ]) + meta("Clients", "Citigroup, Shenzhen Rural Commercial Bank, Empire State Development"))
    wsp = job("WSP", "Jul 2010 to Oct 2013", "New York", "Revenue C$18.3bn (2025)",
              "WSP is a Montreal engineering and professional services consultancy listed in Toronto.", "Sustainability Manager, YR&amp;G", li([
                  "Won more than $2 million a year in fees through cold and warm outreach, pitches and bids.",
                  "Managed sustainability projects for public and private sector clients and led teams of engineers, energy modellers and analysts on evaluations of multi-property portfolios.",
              ]) + meta("Clients", "ESPN, Lotte, Essence Securities"))
    rva = job("Rafael Viñoly Architects", "Oct 2008 to Jan 2010", "New York", "",
              "Rafael Viñoly Architects is a New York practice whose buildings include 432 Park Avenue.", "Computational and Environmental Designer", li([
                  "Co-founded the firm's Technology Group, which introduced scripting and simulation to its design process.",
                  "Led environmental analysis, solar modelling and geometry optimisation for complex projects in North America and Asia.",
              ]))
    skills = ('<h3>Commercial</h3>' + tags(["Consultative selling to C-suite", "Building new service lines", "Pursuit leadership and bids", "Multi-year advisory contracts", "Executive presentations"])
              + '<h3>Experience and digital</h3>' + tags(["Experience and spatial design", "Computational design", "Simulation and analytics", "Digital twins", "AI tools and agents"])
              + '<h3>Industries</h3>' + tags(["Life sciences", "Banking", "Technology", "Real estate", "Sports and media"]))
    side = [
        ("Skills", skills),
        ("Education", ent("Building Performance Simulation", "2011", "Harvard University Graduate School of Design") + ent("Certificate in Sustainable Finance", "2022", "University of Cambridge Institute for Sustainability Leadership") + ent("Master of Engineering", "2010", "Stevens Institute of Technology") + ent("Bachelor of Architecture", "2004", "Iowa State University")),
        ("AI credentials", '<h3>Anthropic</h3>' + tags(["AI Fluency", "Claude Code in Action", "Claude Cowork", "Claude Platform"]) + '<h3>Microsoft</h3>' + tags(["Copilot Studio in a Day"])),
        ("Accreditations", tags(["LEED Accredited Professional", "Estidama Pearl Qualified Professional"])),
        ("Teaching", ent("Industry Partner Instructor", "", "Imperial College London") + ent("Associate Adjunct Professor", "", "City University of New York") + ent("Graduate Consultant", "", "Harvard GSD, Penn Design and Columbia")),
        ("Presentations", ent("COP26 Buildings Pavilion", "2021", "Two sessions on net zero and whole life carbon") + ent("UN COP28, Dubai", "2023", "Lecture") + ent("Foster + Partners Earth Day and COP Week", "", "Chaired panels") + ent("One Click LCA Bootcamp", "2023", "Panel") + ent("BPAC and SimBuild", "2018", "Keynote") + ent("CoreNet Global Summit, Dubai", "2023", "Listed speaker")),
    ]
    sideh = "".join(f'<section class="side-block"><h2>{t}</h2>{b}</section>' for t, b in side)
    body = f"""<div class="wrap">
<header class="cv-head">
  <img src="assets/arpan-bakshi.jpg" alt="Portrait of Arpan Bakshi" width="560" height="700">
  <div>
    <h1>Arpan Bakshi</h1>
    <p class="title">Business Development and Transformation Advisory</p>
    <div class="contact">
      <a href="mailto:arpanbakshi@outlook.com"><b>Email</b>arpanbakshi@outlook.com</a>
      <span><b>Phone</b>07535 141944</span>
      <a href="https://linkedin.com/in/arpanbakshi"><b>LinkedIn</b>linkedin.com/in/arpanbakshi</a>
      <span><b>Based in</b>London, UK and US citizen</span>
    </div>
    <div class="cv-actions"><a class="btn primary" href="arpan-bakshi-cv-wipro.pdf">Download PDF</a><button class="btn ghost" type="button" onclick="window.print()">Print</button></div>
  </div>
</header>
<section class="cv-profile">
  <p class="kick">Consultative selling | Experience and design-led transformation | AI adoption</p>
  <p>I have sold design-led consulting and transformation services to executives since 2010, at WSP and SOM in New York and at Foster + Partners in London. At Foster + Partners I co-created a strategic advisory service line covering corporate environmental strategy, digital transformation and spatial consulting, led pitches that won more than £10 million a year in fees, and won a multi-year portfolio contract with a global pharmaceutical company. My clients have included Roche, Genentech, JPMorgan Chase, Citigroup, Apple, Oracle and Hyundai. I trained as an architect and computational designer, so I can discuss experience design, digital tools and delivery with marketing and technology leaders in the same meeting. Since 2025 I have co-run Atlas Learn, which trains boards and executive teams to use AI tools, and I have trained more than 250 senior professionals.</p>
</section>
<div class="cv-grid">
  <section><h2>Experience</h2>{atlas}{foster}{som}{wsp}{rva}</section>
  <aside class="cv-side">{sideh}</aside>
</div>
</div>"""
    page("cv.html", body, "Curriculum vitae of Arpan Bakshi, tailored for the Wipro Director, Digital Experience role.")
