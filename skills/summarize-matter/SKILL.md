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
2. **Classify into a sub-type.** Pick one of the **eight sub-types** (brain §2 /
   `subtype-lenses.md`) plus Simple vs Complex; record it in `matter.sub_type`.
   If none clearly fits, use **Other** and note the sub-type was uncertain.
   Capture the **matter block, facts only**: the two parties as `matter.party_lines`
   in the form **`Name (role)`** (e.g. "Acme Advisors LLC (sell-side financial
   advisor)"), one string per party, and the document type (include the sub-type,
   e.g. "Technology / SaaS · Complex"). Use the parenthetical form, never a dash
   separator. **No `overall_read` and no characterisation of the paper** (that
   belongs in the issues). No invented matter numbers, and **no em-dashes** in any
   field.
3. **Extract key terms by hand, guided by the sub-type lens's checklist.** Walk
   the clause families and pull every operative term into `key_terms[]`. **Check
   every number and its measurement point separately** — a fee % *and* its base, a
   cap *and* its multiplier, a term *and* its renewal/notice mechanics, a tail
   *and* its trigger. Capture each
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

Fill `matter{}` (incl. `party_lines[]`, no `overall_read`) and `key_terms[]` in
the review-state. When run standalone, present: the matter block (two party lines
+ document type — no opinion) then a scannable two-column key-terms table (material
terms only, ≤ 12). Keep it factual and neutral — description, not judgment. Offer
to proceed to issue-spotting.
