---
name: summarize-matter
description: Extract the matter summary and key operative terms from an engagement letter or commercial contract. Trigger on "summarize this letter", "what are the key terms", "what's the fee / success fee / tail / cap / term", "who are the parties", "walk me through this agreement", or as the extraction step of the review. Describes and extracts only — it classifies issues (spot-issues) and drafts emails (client-email) elsewhere.
---

# Summarize the matter & extract key terms

The by-hand capture pass. Produce (a) the matter narration and (b) the full
key-terms table. Describe what the document says; do **not** evaluate whether
terms are acceptable — that is `spot-issues`.

**Read first:** `${CLAUDE_PLUGIN_ROOT}/reference/legal-brain.md` (§2 classify, §3
method, §5/§6 clause families) and the `review-state` shape in
`${CLAUDE_PLUGIN_ROOT}/reference/output-contract.md`.

## Steps

1. **Read the document.** `.docx` → extract text with whatever is available —
   `pandoc`, the `docx` skill, or `python-docx` — and **keep the original `.docx`
   path** for the redline export; `.pdf` → the pdf skill; else the pasted text.
   Note every incorporated-by-reference document (schedules, SLAs, DPAs, order
   forms, URL "standard terms").
2. **Classify.** Family (engagement letter / commercial contract), sub-type, and
   Simple vs Complex. Capture the **matter narration**: the two parties by real
   name with their roles as `matter.party_lines` (one string per party, rendered
   on its own line), plus document type/sub-type and a one-line read of how the
   paper leans. No invented matter numbers, and no separate "matter summary"
   block beyond this narration.
3. **Extract key terms by hand.** Walk the clause families and pull every
   operative term into `key_terms[]`. **Check every number and its measurement
   point separately** — a fee % *and* its base, a cap *and* its multiplier, a
   term *and* its renewal/notice mechanics, a tail *and* its trigger. Capture each
   as **two fields**: `term` (the name) and `provision` (what the agreement
   provides), plus `ref` (the section/clause, e.g. "§3(a)") and optional `href`
   (a link to that part of the document when the source is hosted with
   addressable anchors). The console renders this as a two-column table
   (**Term · Provision**) with the clause reference hyperlinked where `href` is
   present.
4. **Missing-term note.** Flag standard provisions that are absent (no
   confidentiality, no liability cap for the client, no termination-for-
   convenience, no IP ownership) — pass these to `spot-issues`.

## Output

Fill `matter{}` (incl. `party_lines[]`) and `key_terms[]` in the review-state.
When run standalone, present: the matter narration (two party lines, type/sub-type,
one-line read) then a scannable two-column key-terms table. Keep it factual and
neutral — description, not judgment. Offer to proceed to issue-spotting.
