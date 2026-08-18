# Output contract — the review packet

The deliverable is deliberately split so the lawyer is not overwhelmed at first
glance. Both surfaces open with a **short matter narration that names the two
parties on two separate lines** — there is no separate "matter summary" section:

- **The redline lives only in the downloadable tracked-changes `.docx`.** It is
  never rendered on-screen — not in chat, not in the console.
- **Chat** is the succinct first glance: the matter block, then **one combined
  "Legal issues & recommendations" section**, then commercial deal terms. There
  is **no separate recommendations section** — the position and fallback live on
  each issue.
- **The HTML console** carries the matter block in its header, then the same
  combined "Legal issues & recommendations" section, deal terms, key terms, and
  the draft client escalation email.

Everything is single-sourced from one `review-state` object so the chat, the
`.docx`, and the console never disagree.

**Brevity is the contract, not a preference.** The lawyer is scanning, not
reading. Match the Acme reference run: high-level, terse, high-value only.

- **Hard caps** — the combined Legal issues & recommendations: **the 3–6
  highest-value only**, most-serious first. Deal terms: **≤ 5**. Key terms
  (console): the material terms only, **≤ 12**. If something is minor, drop it —
  do not pad to look thorough.
- **One line per field.** Each entry's Issue / Risk / Recommendation / Fallback is
  a single clause, not a paragraph. No multi-sentence explanations, no
  sub-bullets, no restating the clause verbatim.
- **No process narration and no preamble** — never "I read the document…",
  "Here is the review…", status lines, methodology, confidence, or precedent
  talk. Open on the parties; close on the pointers.
- **No opinions in the matter block** — parties and document type only (see §1).
- **No filler, no invented matter numbers.** Cut every word that is not load-
  bearing.

Tone: senior-associate to a partner — the kind who says the least that fully
does the job.

---

## The redline (downloadable `.docx` only)

A native tracked-changes `.docx` of the **actual letter**, marked up inline
(minimum necessary intervention). This is the *only* place the marked-up text
appears — do **not** render a redline box in chat or a redline panel in the
console. Send the file to the lawyer (SendUserFile, `attach`) and reference it
with a one-line pointer from chat and the console. Nothing is sent to the
counterparty.

## In chat (the succinct first glance)

Open with the matter narration. Render in this order.

### 1. Matter block (top of the output) — facts only, no opinion
Three lines, then move straight to the issues. **No characterisation of how the
paper reads, no "advisor-friendly", no assessment — that is what the issues are
for.**
- **Party line 1** — counterparty by real name + role (e.g. "Acme Advisors LLC —
  sell-side financial advisor").
- **Party line 2** — client by real name + role (e.g. "PortfolioCo — client").
- **Document type** — family + sub-type + Simple/Complex, in a few words (e.g.
  "Engagement letter · M&A advisor · Complex").

That is the entire matter block. Then go directly to §2.

### 2. Legal issues & recommendations
The legal worklist and the call on each, **combined into one section** (they
covered the same ground twice — now once). One entry per point, the **3–6
highest-value only**, most-serious / highest-leverage first. Skip minor/market
points. Each field a single clause, not a paragraph:
- **Issue** — clause ref + what it does (terse).
- **Risk** — why it bites the client (one clause).
- **Position** — **Push back** / **Negotiate** / **Acceptable** (/ **Walk-away**).
- **Recommendation** — one sentence: the fix and why, in the client's interest
  (matches the change marked in the `.docx`).
- **Fallback** — one clause: what we could live with if resisted (or "—").
Draft-only — never auto-send.

### 3. Commercial deal terms for the client's confirmation
The business calls — **≤ 5**, present don't opine. One line each:
- **Term** — what the document proposes (with the number).
- **Confirm** — the specific decision the client must make.
Fees, success-fee %/base, term length, exclusivity, caps/insurance *amounts*,
publicity.

Close the chat message with a one-line pointer to the downloadable `.docx`
redline and to the console (which holds the full packet including **key terms**
and the **draft client escalation email**).

---

## In the HTML console (the full on-screen packet)

A single self-contained HTML artifact (Ontra-branded, theme-aware, sectioned with
a jump nav). Its **header carries the matter block** — title, the two parties one
per line, document type, and a note that the tracked-changes redline is a separate
`.docx` download. **No overall-read / opinion line.** There is **no separate
matter-summary section**. Below the header:

- **1. Legal issues & recommendations** — the combined worklist: clause · what it
  does · risk · position (push back / negotiate / acceptable) · recommendation ·
  fallback.
- **2. Commercial deal terms** — the client's business calls (term · confirm).

…plus the two items the chat does **not** show:

### 3. Key terms
The operative terms from the by-hand extraction, in exactly **two columns**:
- **Term** — the term's name (e.g. "Success fee", "Tail period").
- **Provision** — what the agreement provides for that term, **including its
  section/clause reference** (e.g. "1.75% of enterprise value — §3(a)"). Where a
  linkable location for the source exists, the section reference is a
  **hyperlink** to the relevant part of the document (`ref` + `href`); otherwise
  it renders as a plain clause reference. (A downloadable `.docx` has no
  addressable anchor, so hyperlinks resolve only when the source is hosted with
  anchors — e.g. a PDF page link or an HTML/Docs URL.)

### 4. Draft client escalation email
The ready-to-edit email to the client / deal team: subject, greeting, one-line
context, **Business decisions we need from you** (the deal terms), **Legal points
we're handling** (brief, from the legal issues), a clear ask, and a sign-off.
Draft-only, with a copy affordance. It never sends.

**Console data.** The template reads one JSON block (`<script id="review-data">`)
that is a display projection of the review-state — keys: `matter{title,
party_lines[], doc_type}` (the header block; `party_lines` is one string per
party, rendered on its own line; **no `overall_read`/opinion**), `legal_issues[]`
(`clause, stance, says, risk, recommendation, fallback` — the **combined**
issue+recommendation), `business_terms[]` (`term, confirm`), `key_terms[]`
(`term, provision, ref, href`), and `client_email{subject, body_markdown}`. **No
separate `recommendations[]`** (folded into `legal_issues[]`) and **no `redline`
key** (the redline is the `.docx` only). Map straight from the review-state
fields below; the console never introduces content the chat/redline don't
already carry.

---

## The shared `review-state` object

One JSON object drives all three outputs. Written to the working dir as
`<slug>.review-state.json`. Shape (fill only what the document supports):

```json
{
  "matter": {
    "title": "Engagement Letter (M&A advisor) — Acme Advisors ↔ PortfolioCo",
    "doc_family": "engagement_letter",
    "sub_type": "m&a advisor",
    "complexity": "complex",
    "parties": { "client": "PortfolioCo", "counterparty": "Acme Advisors LLC" },
    "party_lines": [
      "Acme Advisors LLC — sell-side financial advisor",
      "PortfolioCo — client"
    ]
  },
  "source": { "path": "uploads/letter.docx", "href": null },
  "key_terms": [
    { "term": "Success fee", "provision": "1.75% of enterprise value",
      "ref": "§3(a)", "href": null }
  ],
  "legal_issues": [
    { "id": "L1", "audience": "legal", "clause": "Indemnification (§9)",
      "stance": "push_back",
      "says": "Client indemnifies advisor incl. advisor's own negligence",
      "risk": "Open-ended; no carve-out for advisor GN/WM/fraud",
      "recommendation": "Carve out advisor's gross negligence, willful misconduct, bad faith, fraud — market standard.",
      "fallback": "If resisted, at minimum carve out fraud and willful misconduct." }
  ],
  "business_terms": [
    { "term": "Success fee — 1.75% of EV", "confirm": "Is 1.75% and the EV base approved?" }
  ],
  "redline": {
    "edits": [
      { "op": "replace", "section": "Indemnification", "gate_class": "card",
        "anchor": "the Client shall indemnify the Advisor",
        "before": "for any and all losses",
        "after": "for any and all losses, except to the extent arising from the Advisor's gross negligence, willful misconduct, bad faith or fraud",
        "rationale": "Carve out advisor fault from the client indemnity", "cites": "L1" }
    ]
  },
  "client_email": {
    "subject": "PortfolioCo — Acme engagement letter: decisions needed",
    "body_markdown": "..."
  }
}
```

- Each `legal_issues[]` entry is the **combined** issue + recommendation:
  `clause`, `says` (what it does), `risk`, `stance` ∈ `push_back | negotiate |
  acceptable | walk_away`, `recommendation` (one-sentence fix + why), and
  `fallback` (landing zone, or "—"). `audience` ∈ `legal | business`. There is
  **no separate `recommendations[]` array** — the position and fallback live on
  the issue.
- `key_terms[]` renders as two columns (**Term** · **Provision**); `ref` is the
  clause reference and, when `href` is present, the console hyperlinks it to the
  source. A downloadable `.docx` has no addressable anchor, so `href` is set only
  when the source is hosted with anchors (PDF page link, HTML/Docs URL).
- `redline.edits[].gate_class` ∈ `card | silent`; `anchor` is the verbatim text
  that locates the edit in the source (the `.docx` exporter needs it for a true
  inline redline). The redline is delivered **only** as the `.docx`.
- Business terms are **not** redline edits — they are the client's call.
