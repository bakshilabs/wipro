# Wipro application: Director, Digital Experience (DX)

Research site and tailored application materials for Wipro's Director, Digital Experience (DX) role, a sales practitioner role in the Americas (req 190063, posted 16 July 2026). Drafted 23 October 2026.

## Site
Open `index.html` in a browser. It is a password page; the password is shared separately and only its salted hash is stored. All pages share one navigation bar.

- `overview.html`: four framing numbers, my reading of the role, three ideas behind the plan, links to every page
- `role.html`: the posting decoded line by line, four related Wipro postings compared, time split, the person described
- `operating-model.html`: Wipro's market unit and business line matrix, where DX sits, stakeholders, pursuit roles, results context
- `market.html`: DX market size, CMO budget shifts, analyst ratings, positioning map, competitor and objection tables
- `triggers.html`: 25 dated triggers for 2025 to 2028 (platform support ends, accessibility and privacy rules, corporate events, agentic commerce) with lead signals
- `accounts.html`: 24 target accounts by fit and route in, with trigger, sources and first move
- `pursuit.html`: interactive qualification scorecard and deal ladder calculator
- `portfolio.html`: interactive pipeline maths for a $25m bookings target and the operating rhythm
- `plan.html`: first 180 days with day 90, 180 and 365 targets
- `fit.html`: requirements rated against evidence, gaps and how to close them
- `cv.html` and `arpan-bakshi-cv-wipro.pdf`: CV ordered for this role (two A4 pages)

## Other files
- `job-description.txt`: the posting text and the related postings
- `build/`: generators (`python3 build/build.py`), page modules in `build/pages/`, account data in `build/data/`, research notes with sources in `build/research/`, Playwright checks in `build/pwrun/` (`npm i playwright axe-core`, then `node axe.mjs`, `node shots.mjs`, `node pdf.mjs`)
- `session-notes.md`: decisions, assumptions and open points

This repository holds a phone number and career details, so keep it private unless the phone number is removed.
