from lib import *

# theme, icon, questions
QS = [
    ("The book", "target", [
        "Which accounts and industries would this role cover, and which SMU client partners own them?",
        "Is there an inherited pipeline, and how much of the first-year target is already in it?",
        "How are the bookings target and the revenue target set, and over what period are they measured?",
    ]),
    ("The matrix", "people", [
        "When a DX deal is won inside an SMU account, how is the credit shared with the client partner and the platform practice?",
        "Who decides whether a pursuit goes ahead, and who approves price on a large deal?",
        "How do Designit and the DX practice work together on the first conversation with a client?",
    ]),
    ("The offer", "grid", [
        "Which DX offers win most often in the Americas today, and which ones are you trying to grow?",
        "Which platform partnerships bring Wipro into deals, and which ones does Wipro have to bring the vendor into?",
        "Where do clients push back hardest: price, onshore presence, creative depth or references?",
    ]),
    ("Success", "chart", [
        "What would make you say, after six months, that this hire was right?",
        "What has stopped people in this kind of role from succeeding at Wipro before?",
        "What are the next steps in the process, and when do you expect to decide?",
    ]),
]

AFTER = [
    ("pen", "A draft account plan", "Send me the list of accounts this role would cover, and I will return a one-page plan for each of the top ten within a week, with trigger, buyer and first move."),
    ("calendar", "One point of view", "A short written point of view on one 2027 deadline for one of your focus industries, written for a client CMO or CDO."),
    ("people", "References", "Former clients and partners who can speak to how I sell to executives and how I work across a matrix."),
]


def build():
    body = hero("Questions", "Twelve Questions", "What I need to learn from you to make the plan real, in four groups.")
    tiles = ""
    for i, (theme, ic, qs) in enumerate(QS):
        lis = "".join(f'<li style="margin-top:12px">{E(q)}</li>' for q in qs)
        tiles += tile(f'{icon(ic)}<h3 style="margin-top:20px">{E(theme)}</h3><ol style="margin:6px 0 0 18px;color:var(--muted);font-size:16px;line-height:1.45">{lis}</ol>', 6)
    body += sec(head_block("Questions", "Four Groups", "Three questions in each. I would start with the book.") + f'<div class="bento">{tiles}</div>', "grey")
    af = "".join(tile(f'{icon(i)}<h3 style="margin-top:20px">{E(a)}</h3><p>{E(b)}</p>', 4) for i, a, b in AFTER)
    body += sec(head_block("After the meeting", "What I Can Send", "Within a week of this conversation.") + f'<div class="bento">{af}</div>'
                + '<p class="fine">The <a href="cv.html">CV</a> is ordered for this role, and the <a href="research.html">research appendix</a> holds the full working analysis.</p>')
    page("questions.html", body, "Questions for the Wipro DX hiring team, and what Arpan Bakshi can send after the meeting.")
