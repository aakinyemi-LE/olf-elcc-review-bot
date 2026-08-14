# Output contract — the review packet

The deliverable is deliberately split so the lawyer is not overwhelmed at first
glance. Both surfaces open with a **short matter narration that names the two
parties on two separate lines** — there is no separate "matter summary" section:

- **The redline lives only in the downloadable tracked-changes `.docx`.** It is
  never rendered on-screen — not in chat, not in the console.
- **Chat** is the succinct first glance: the matter narration, then legal issues,
  commercial deal terms, and recommendations.
- **The HTML console** carries the narration in its header, then legal issues,
  deal terms, recommendations, key terms, and the draft client escalation email.

Everything is single-sourced from one `review-state` object so the chat, the
`.docx`, and the console never disagree.

Tone: senior-associate to a partner. Concise, skimmable, specific. No filler, no
restating the whole document, no invented matter numbers.

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

### 1. Matter narration (top of the output)
A short narration — **not** a labelled "matter summary" block:
- **The two parties on two separate lines**, each by real name with its role
  (line 1 e.g. "Acme Advisors LLC — sell-side financial advisor
  (provider/counterparty)"; line 2 e.g. "PortfolioCo — client (OLF acts for)").
- **Document type / sub-type** — family + sub-type from the brain (§2), and the
  Simple/Complex call in a few words.
- One line on how the paper reads overall (e.g. "advisor-friendly with a broad
  indemnity and a 24-month tail").

### 2. Legal issues
The RED FLAG and material WATCH items (the *legal* side of the split). For each,
one tight entry:
- **Issue** — clause + what it says.
- **Risk** — why it matters to the client.
- **Recommendation** — the proposed fix (matches the change marked in the `.docx`).
Ordered most-serious first. This is the lawyer's worklist.

### 3. Commercial deal terms for the client's confirmation
The BUSINESS items — the client's calls. Present, don't opine. For each:
- **Term** — what the document proposes (with the number).
- **Confirm** — the specific decision the client must make.
Fees, success-fee %/base, term length, exclusivity, caps/insurance *amounts*,
publicity. These also seed the escalation email.

### 4. Recommendations
Not an administrative checklist — the lawyer's **judgment** on how to play each
material point. For each recommendation:
- **Point** — the issue/term at stake (with its clause ref).
- **Stance** — one of **Push back** (hold firm; off-market or unacceptable),
  **Negotiate** (seek improvement, with a landing zone), **Acceptable** (fine as
  drafted / market — can concede), or **Walk-away** (deal-breaker if not fixed).
- **Recommendation** — what to do and *why*, in the client's interest (e.g. "Hold
  firm on carving advisor fault out of the indemnity — this is market and the
  exposure is otherwise open-ended").
- **Fallback** — what we could live with if the counterparty resists (e.g. "If
  resisted, at minimum carve out fraud and willful misconduct").
Order by leverage/importance. Ground each in the brain (§4 classification, §10
redline discipline, §8 business/legal split); state trade-offs, don't just list
tasks. Draft-only — never auto-send.

Close the chat message with a one-line pointer to the downloadable `.docx`
redline and to the console (which holds the full packet including **key terms**
and the **draft client escalation email**).

---

## In the HTML console (the full on-screen packet)

A single self-contained HTML artifact (Ontra-branded, theme-aware, sectioned with
a jump nav). Its **header carries the matter narration** — title, the two parties
one per line, document type, a note that the tracked-changes redline is a separate
`.docx` download, and the one-line read. There is **no separate matter-summary
section**. Below the header:

- **1. Legal issues** — the red-flag/watch worklist (clause · says · risk · fix).
- **2. Commercial deal terms** — the client's business calls (term · confirm).
- **3. Recommendations** — judgment calls: point · stance (push back / negotiate /
  acceptable / walk-away) · recommendation · fallback.

…plus the two items the chat does **not** show:

### 4. Key terms
The operative terms from the by-hand extraction, in exactly **two columns**:
- **Term** — the term's name (e.g. "Success fee", "Tail period").
- **Provision** — what the agreement provides for that term, **including its
  section/clause reference** (e.g. "1.75% of enterprise value — §3(a)"). Where a
  linkable location for the source exists, the section reference is a
  **hyperlink** to the relevant part of the document (`ref` + `href`); otherwise
  it renders as a plain clause reference. (A downloadable `.docx` has no
  addressable anchor, so hyperlinks resolve only when the source is hosted with
  anchors — e.g. a PDF page link or an HTML/Docs URL.)

### 5. Draft client escalation email
The ready-to-edit email to the client / deal team: subject, greeting, one-line
context, **Business decisions we need from you** (the deal terms), **Legal points
we're handling** (brief, from the legal issues), a clear ask, and a sign-off.
Draft-only, with a copy affordance. It never sends.

**Console data.** The template reads one JSON block (`<script id="review-data">`)
that is a display projection of the review-state — keys: `matter{title,
party_lines[], doc_type, overall_read}` (the header narration; `party_lines` is
one string per party, rendered on its own line — falls back to splitting `roles`
on ";"), `legal_issues[]` (`clause, severity, says, risk,
recommendation`), `business_terms[]` (`term, confirm`), `recommendations[]`
(`point, stance, recommendation, fallback`), `key_terms[]` (`term, provision,
ref, href`), and `client_email{subject, body_markdown}`. No `redline` key — the
redline is the `.docx` only. Map straight from the review-state fields below; the
console never introduces content the chat/redline don't already carry.

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
      "Acme Advisors LLC — sell-side financial advisor (provider/counterparty)",
      "PortfolioCo — client (OLF acts for)"
    ],
    "overall_read": "advisor-friendly; broad indemnity and a 24-month tail"
  },
  "source": { "path": "uploads/letter.docx", "href": null },
  "key_terms": [
    { "term": "Success fee", "provision": "1.75% of enterprise value",
      "ref": "§3(a)", "href": null }
  ],
  "issues": [
    { "id": "L1", "class": "red_flag", "audience": "legal", "clause": "Indemnification",
      "says": "Client indemnifies advisor incl. advisor's own negligence",
      "risk": "Open-ended; no carve-out for advisor GN/WM/fraud",
      "recommendation": "Carve out advisor's gross negligence, willful misconduct, bad faith, fraud" }
  ],
  "business_terms": [
    { "term": "Success fee — 1.75% of EV", "confirm": "Is 1.75% and the EV base approved?" }
  ],
  "recommendations": [
    { "point": "Client indemnity (§9)", "stance": "push_back",
      "recommendation": "Hold firm on carving advisor fault out of the indemnity — market standard; exposure is otherwise open-ended.",
      "fallback": "If resisted, at minimum carve out fraud and willful misconduct." }
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

- `issues[].class` ∈ `red_flag | watch | business | acceptable`;
  `audience` ∈ `legal | business`.
- `recommendations[].stance` ∈ `push_back | negotiate | acceptable | walk_away`.
  Each recommendation is a judgment call with a `fallback` landing zone — not an
  administrative step.
- `key_terms[]` renders as two columns (**Term** · **Provision**); `ref` is the
  clause reference and, when `href` is present, the console hyperlinks it to the
  source. A downloadable `.docx` has no addressable anchor, so `href` is set only
  when the source is hosted with anchors (PDF page link, HTML/Docs URL).
- `redline.edits[].gate_class` ∈ `card | silent`; `anchor` is the verbatim text
  that locates the edit in the source (the `.docx` exporter needs it for a true
  inline redline). The redline is delivered **only** as the `.docx`.
- Business terms are **not** redline edits — they are the client's call.
