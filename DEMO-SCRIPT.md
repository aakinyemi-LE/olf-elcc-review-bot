# Demo script — OLF EL & CC Review bot (Cowork)

Target length: ~3 minutes. Talking points, not a paragraph to read. Riff naturally.

---

## 0. Open (~20s) — before you upload anything
**On screen:** Cowork, empty composer.
**Say:**
- "This is a Cowork plugin that gives an OLF lawyer a first-pass review of an
  engagement letter or a commercial contract — on the other side's paper."
- "The goal is a fast, lawyer-ready packet: what matters, what to push on, and a
  redline ready to send — not a 20-page memo."
- "It's issue-first and draft-only. Nothing ever gets sent; the lawyer stays in
  control."

## 1. Kick it off (~15s)
**On screen:** Drag in the engagement letter `.docx`. Type `/olf-elcc-review-bot:review` (or "review this engagement letter"). Send.
**Say:**
- "I just drop the letter in and run one command. No pasting, no setup."
- "Behind it, it's reading the document, classifying it, and running a structured
  first pass on our legal brain."

## 2. The chat packet — top to bottom (~60s)
**On screen:** Scroll the chat response slowly as you talk.
**Say — hit these four in order:**
- **Matter narration:** "First line tells me the two parties and their roles —
  who we act for, who's on the other side — and the document type. No made-up
  matter numbers."
- **Legal issues:** "Then the legal red flags, worst first — the indemnity, the
  liability cap, the fee trigger, the tail. Each one: what it says, why it's a
  risk, and the fix."
- **Commercial deal terms:** "Then the business points — fees, retainer,
  exclusivity — presented for the client to confirm. It doesn't opine on price;
  that's the client's call."
- **Recommendations:** "And this is the part I care about — not a checklist.
  For each point it takes a position: push back, negotiate, or accept — with the
  reasoning and a fallback. That's the judgment a junior would give me."

## 3. The redline (~30s)
**On screen:** Open the attached `.docx`. Show tracked changes inline.
**Say:**
- "The redline isn't a list — it's the actual letter marked up, native tracked
  changes. I accept or reject clause by clause in Word."
- "Notice it only redlines the legal points. Business terms aren't marked — those
  go to the client, not the counterparty."

## 4. The console (~30s)
**On screen:** Open the HTML console link. Scroll through it.
**Say:**
- "To keep the chat clean, the full detail lives here. Same review, one page."
- "Key terms in two columns with the clause references."
- "And a **draft client escalation email**, ready to edit and copy — the business
  decisions and the legal points, already written up. Draft only; I send it."

## 5. Close (~20s)
**On screen:** Back to the chat.
**Say:**
- "So: drop a letter, get a redline, a triaged issues list, real recommendations,
  and a client email — in one pass."
- "It's deliberately lean and issue-first — no precedent rabbit-holes — and every
  judgment call is surfaced for the lawyer, never buried."
- "Draft-only, human-in-the-loop, start to finish."

---

## Backup one-liners (if asked)
- **"Does it send anything?"** — "No. Redline and email are drafts; the lawyer
  transmits from their own client."
- **"Where's the legal reasoning from?"** — "Ontra's negotiation and redline
  discipline, encoded as a shared legal brain — used the same way across every
  review."
- **"Playbooks/precedent?"** — "Used to sharpen positions when they're available,
  never required. It won't stall waiting for them."
- **"Engagement letters only?"** — "Engagement letters and corporate commercial
  contracts — SaaS, MSAs, consulting, vendor paper."

## Pre-record checklist
- [ ] Old EL/CC plugins removed in Cowork (this is the only one running)
- [ ] Sample letter handy on the desktop
- [ ] A clean/new Cowork session open
- [ ] Console opens and renders; `.docx` opens in Word with tracked changes on
