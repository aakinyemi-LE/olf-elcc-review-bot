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
- **No em-dashes in any output.** Never use `—` in chat, the console, the `.docx`,
  or the client email. Use a comma, colon, or a new sentence instead. (This is a
  house style rule; it applies to everything the lawyer or client sees.)
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

**Cards first.** Emit the two deliverable cards at the very top of the reply, side
by side — the **console (Artifact)** and the **redline `.docx` (SendUserFile)** —
*before* any analysis text. Then render the analysis in this order.

### 0. Count line (the single lead line)
Open the analysis with one short line giving the totals: **`N legal issues ·
M commercial points`** (using the actual counts from `legal_issues[]` and
`business_terms[]`, e.g. "5 legal issues · 4 commercial points"). Nothing else on
the line — it is the high-level glance before the matter block.

### 1. Matter block (top of the output) — facts only, no opinion
Three lines, then move straight to the issues. **No characterisation of how the
paper reads, no "advisor-friendly", no assessment — that is what the issues are
for.**
- **Party line 1** — counterparty by real name, with the role in parentheses
  (e.g. "Acme Advisors LLC (sell-side financial advisor)").
- **Party line 2** — client by real name, role in parentheses (e.g.
  "PortfolioCo (client)"). Use the `Name (role)` form, never a dash separator.
- **Document type** — the sub-type (from the taxonomy, brain §2 /
  `subtype-lenses.md`) + Simple/Complex, in a few words (e.g. "Technology / SaaS ·
  Complex", or "Financial advisory · Complex"). If the sub-type was uncertain, say
  "Other / uncategorised".

That is the entire matter block. Then go directly to §2.

### 2. Legal issues & recommendations
The **3–6 highest-value** points, most-serious first. Skip minor/market points.
**In chat, keep each entry to two parts only — Issue, Recommendation.** Do **not**
prefix a **Push back / Negotiate / Acceptable** position tag — it reads as clutter;
the stance still drives the redline and the console decisions, it just is not
displayed as a per-issue label. The **Risk and Fallback are NOT shown in chat**;
they live in the console (and the lawyer can ask for them). Lawyers reviewing
commercial contracts already know the risks, so chat stays scannable.
- **Issue** — clause ref + what it does (one clause).
- **Recommendation** — one sentence: the fix, in the client's interest (matches
  the change marked in the `.docx`).

Close the section with a single line: *"Ask if you'd like the risk or fallback on
any of these."* Draft-only — never auto-send. (The full record — Risk, Fallback,
and clause hyperlinks — is in the console, which carries all five fields.)

### 3. Commercial deal terms for the client's confirmation
The business calls — **≤ 5**, present don't opine. One line each:
- **Term** — what the document proposes (with the number).
- **Confirm** — the specific decision the client must make.
Fees, success-fee %/base, term length, exclusivity, caps/insurance *amounts*,
publicity.

No closing pointer block is needed — the console and redline are already the two
cards at the top of the reply.

---

## In the HTML console (the full on-screen packet)

A single self-contained HTML artifact (Ontra-branded, theme-aware, sectioned with
a jump nav). Its **header carries the matter block** — title, the two parties one
per line, document type, and a note that the tracked-changes redline is a separate
`.docx` download. **No overall-read / opinion line.** There is **no separate
matter-summary section**. Below the header:

- **1. Legal issues & recommendations** — the combined worklist: clause · what it
  does · risk · recommendation · fallback. (No push-back / negotiate / acceptable
  position tag is displayed — the `stance` is retained in the data and still drives
  the redline and the decisions layer, but it is not shown as a per-issue label.)
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
context, then **Business decisions we need from you as a numbered list** (one item
per deal term, the term in bold followed by its confirmation question), a clear
ask, and a sign-off. **Do not list the legal issues in the email body** — those
are handled in the markup; the email exists to get the client's commercial
decisions, presented as a scannable list. Draft-only, with a copy affordance. It
never sends.

**Console data.** The template reads one JSON block (`<script id="review-data">`)
that is a display projection of the review-state — keys: `matter{title,
party_lines[], doc_type, document_sections?, source_url?}` (the header block;
`party_lines` is one string per party; **no `overall_read`/opinion**;
`document_sections` embeds the document so refs link to it — see refs below;
`source_url` is a hosted document URL fallback), `legal_issues[]`
(`clause, stance, says, risk, recommendation, fallback`, optional `anchor`/`href`
— the **combined** issue+recommendation), `business_terms[]` (`term, confirm`,
optional `ref`/`anchor`/`href`), `key_terms[]` (`term, provision, ref`, optional
`anchor`/`href`), and `client_email{subject, body_markdown}`. **No separate
`recommendations[]`** (folded into `legal_issues[]`) and **no `redline` key** (the
redline is the `.docx` only). Map straight from the review-state fields below; the
console never introduces content the chat/redline don't already carry.

**Section-reference hyperlinks.** In the console, every `§` reference (an issue's
clause, a deal term's `ref`, a key term's `ref`) links to the relevant part of the
document. The **default and best way** is `matter.document_sections` — an array of
`{ref, text}` for the document's own clauses (`ref` like `"§6"`, `"Part A"`; `text`
is that clause's text, verbatim or lightly trimmed). The console embeds them under
a collapsible **Source document** section and links each `§` reference to the
matching clause **in-page** (it highlights on jump). **Use the same `ref` label on
an item and on its `document_sections` entry** so they match (a coarser section,
e.g. `§6`, also catches `§6(a)` and `§6/§7`). Populate `document_sections` on every
review so the references resolve. Fallbacks when you have not embedded the text: a
hosted `matter.source_url` (+ per-item `anchor` such as `"page=6"`, or a full
`href`); otherwise refs render as plain chips. Never invent a `source_url`. (Deep,
precise in-`.docx` linking and the accept/reject workflow remain the Word plugin's
job; embedding the text here is the self-contained way to make the console refs
clickable.)

**Decisions layer.** The console gives each legal issue and each deal term a "Your
call" control (Agree/Adjust on issues, Confirm/Change on terms) with an optional
note, and a **Copy decisions to chat** button that emits a plain-text
`Decisions for <matter>` summary. The lawyer marks their calls, copies the summary,
and pastes it back into chat. When you receive such a summary, **apply the deltas**:
update the review-state, re-emit the tracked-changes `.docx`, and revise the client
email (an accepted term drops out of the email; a changed one becomes a redline
edit). Do not re-run the whole review. Marks persist per-viewer in localStorage,
keyed by matter title; this is authored automatically by the template, so the
review-state needs no extra field for it.

---

## The shared `review-state` object

One JSON object drives all three outputs. Written to the working dir as
`<slug>.review-state.json`. Shape (fill only what the document supports):

```json
{
  "matter": {
    "title": "Acme Advisors ↔ PortfolioCo Engagement Letter (M&A advisor)",
    "doc_family": "engagement_letter",
    "sub_type": "m&a advisor",
    "complexity": "complex",
    "parties": { "client": "PortfolioCo", "counterparty": "Acme Advisors LLC" },
    "party_lines": [
      "Acme Advisors LLC (sell-side financial advisor)",
      "PortfolioCo (client)"
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
    "subject": "PortfolioCo, Acme engagement letter: decisions needed",
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
