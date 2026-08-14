---
name: redline
description: Author the OLF markup on the actual engagement letter or commercial contract and export it as a native tracked-changes Word .docx. Trigger on "redline this", "mark up the document", "produce the tracked-changes doc", "export the redline", or as the markup step of the review. Marks the client's legal positions in place with minimum necessary intervention; business terms are NOT redlined (they go to the client email). Draft-only — never sends.
---

# Author the redline & export the tracked-changes .docx

Turn the classified legal issues into edits **on the actual document**, then
export a Word file with native tracked changes the attorney can accept or reject.

**Read first:** `${CLAUDE_PLUGIN_ROOT}/reference/legal-brain.md` §10 (redline
discipline) and the `redline` block in
`${CLAUDE_PLUGIN_ROOT}/reference/output-contract.md`.

## Steps

1. **Draft edits from the legal issues only.** For each `red_flag` (and any
   `watch` that warrants a drafting change), write one edit. Do **not** redline
   pure business terms — those are the client's call and go to the escalation
   email; leave them out of the markup.
2. **Minimum necessary intervention.** Prefer surgical edits — carve-outs, caps,
   notice windows, symmetry fixes — over wholesale rewrites. To add a missing
   protection, use `op:"insert"` with an `anchor` marking where it goes.
3. **For each edit set** (see the shape in the output contract): `op`
   (replace/insert/delete), `section`, `anchor` (verbatim text that locates the
   edit in the source — required for a true inline redline), `before`, `after`,
   `rationale` (one line), `gate_class` (`card` = legally-operative, attorney
   decides; `silent` = administrative/conforming), and `cites` (the issue id).
   Never disguise an operative change as administrative.
4. **Export the .docx.** Ensure `source.path` points at the original `.docx` (or
   set `source.text` to the extracted plain text), write the review-state JSON,
   then run:

   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/tools/redline_to_docx.py" <slug>.review-state.json -o <slug>.redline.docx
   ```

   The tool applies each edit **in place** against the source (true inline
   redline) when a source is present, and falls back to a clause-by-clause
   tracked-changes list when it is not. It enables track-changes on open. If
   `python-docx` is missing: `pip install python-docx`.

## Output

The redline is delivered **only** as the `.docx` — do **not** render a redline
box in chat or a redline panel in the console.

- `redline.edits[]` in the review-state (drives the export; also the source of
  the "Fix"/recommendation text shown elsewhere, which points back to the `.docx`).
- The exported `<slug>.redline.docx`. Send it to the lawyer with SendUserFile
  (`attach`) and reference it with a one-line pointer from chat/console. Never
  transmit it to the counterparty — the lawyer sends from their own client.
