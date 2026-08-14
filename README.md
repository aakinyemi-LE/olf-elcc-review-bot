# OLF Engagement Letter & Commercial Contract Review — Cowork plugin

A Cowork-facing first-pass review of engagement letters and corporate commercial
contracts for an OLF lawyer acting for a client. Issue-first (not precedent-first),
lean, and **draft-only — nothing sends**.

This repository is **both the plugin and its marketplace** (`.claude-plugin/plugin.json`
+ `.claude-plugin/marketplace.json`), so Cowork can add it by URL and install it in
one step.

## What it produces

- **Chat (succinct first glance):** a two-line party narration → **Legal issues** →
  **Commercial deal terms** → **Recommendations** (push back / negotiate / acceptable,
  each with a reason and a fallback).
- **Downloadable:** a native tracked-changes **`.docx`** redline of the actual document.
- **HTML console:** the full packet — key terms (two columns) + a draft client
  escalation email.

## Install in Claude Cowork

Cowork loads plugins through its own **Plugins** area (it does **not** read the local
`claude` CLI's `~/.claude/plugins`). Do this in the Cowork app:

1. Push this repo to GitHub (see below).
2. In Cowork → **Plugins** → add a marketplace, pasting this repo's GitHub URL
   (`https://github.com/<you>/olf-elcc-review-bot`). The marketplace id is **`olf-elcc`**.
3. Install **`olf-elcc-review-bot`** from the `olf-elcc` marketplace.
4. In the same **Plugins** area, **remove/disable the older EL/CC plugins** so this is
   the only one running: `el-review`, `engagement-letter-review`, `olf-legal-workflows-v0`.
5. Start a new Cowork session, attach a letter, and run `/olf-elcc-review-bot:review`
   (or say "review this engagement letter").

## Push to GitHub

From this folder:

```bash
git add -A
git commit -m "OLF EL & CC review plugin (Cowork)"
gh repo create olf-elcc-review-bot --private --source=. --push
```

(Or create the repo in the GitHub UI and `git remote add origin … && git push -u origin main`.)

## Optional: auto-load for a project

Commit a `.claude/settings.json` in whatever repo you open in Cowork:

```json
{ "enabledPlugins": { "olf-elcc-review-bot@olf-elcc": true } }
```

## Layout

```
.claude-plugin/plugin.json        plugin manifest
.claude-plugin/marketplace.json   marketplace catalog (this repo, source "./")
commands/review.md                the /olf-elcc-review-bot:review slash command
skills/                           review (orchestrator) + summarize-matter, spot-issues, redline, client-email
reference/legal-brain.md          issue-first method, clause families, guardrails
reference/output-contract.md      exact packet shape + shared review-state JSON
assets/console-template.html      HTML console (key terms + draft client email)
tools/redline_to_docx.py          review-state → native tracked-changes .docx
```

## Notes

- **Draft-only.** Redlines and emails are drafts the lawyer owns and sends themselves.
- **No invented identifiers** — real party names and roles only; no matter numbers.
- **No investment advice** — business terms are presented for the client to decide.
- `tools/redline_to_docx.py` needs `python-docx` (`pip install python-docx`).
