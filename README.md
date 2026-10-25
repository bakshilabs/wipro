# Wipro application: Director, Digital Experience (DX)

Research site and tailored application materials for Wipro's Director, Digital Experience (DX) role, a sales practitioner role in the Americas (req 190063, posted 16 July 2026). Drafted 23 October 2026.

## Site
Open `index.html` in a browser. It is a password page; the password is shared separately and only its salted hash is stored.

The site has two tracks. The meeting track is what I show in a one-hour interview, in this order:
- `overview.html` (Agenda): run of show for the hour, three takeaways, links to the meeting pages
- `record.html` (Track Record): three stories mapped to the role, and the three partial requirements with plans
- `thesis.html` (Thesis): three claims on Americas growth, the front-end gap and the 2027 deadlines
- `first-year.html` (First Year): a $25m target worked back to 70 meetings, the first 180 days, targets and asks
- `deal.html` (Sample Deal): DePuy Synthes from separation trigger to a $21m pursuit, with score, roles and risks
- `questions.html` (Questions): twelve questions for the hiring team and what I can send afterwards
- `cv.html` and `arpan-bakshi-cv-wipro.pdf`: CV ordered for this role (two A4 pages)

The research appendix holds the working analysis, behind `research.html` and its own sub-navigation: `role.html`, `operating-model.html`, `market.html`, `triggers.html`, `accounts.html`, `pursuit.html`, `portfolio.html`, `plan.html` and `fit.html`.

## Other files
- `job-description.txt`: the posting text and the related postings
- `build/`: generators (`python3 build/build.py`), page modules in `build/pages/`, account data in `build/data/`, research notes with sources in `build/research/`, Playwright checks in `build/pwrun/` (`npm i playwright axe-core`, then `node axe.mjs`, `node shots.mjs`, `node pdf.mjs`)
- `session-notes.md`: decisions, assumptions and open points
- `interview-prep.md`: private talk track and likely questions for the meeting, not linked from the site

This repository holds a phone number and career details, so keep it private unless the phone number is removed.
