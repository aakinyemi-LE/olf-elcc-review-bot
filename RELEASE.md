# Releasing & source of truth

## Single source of truth
The **GitHub repo** (`github.com/aakinyemi-LE/olf-elcc-review-bot`) is canonical.
Cowork installs from it; the CLI installs from a local marketplace that is a
**derived copy**. Edit here, release here — never hand-edit the derived copies.

## Cut a release
1. Make your changes and run the guard:
   ```bash
   python tools/check_review_state.py tests/fixtures/*.review-state.json
   ```
2. Bump the version in both manifests atomically and re-run the guard:
   ```bash
   tools/release.sh 0.1.3
   ```
3. Commit and push:
   ```bash
   git add -A && git commit -m "Release 0.1.3" && git push origin main
   ```

**Always bump the version.** Cowork keys on it — a content change at the same
version is not reliably pulled.

## Make Cowork actually pick it up
Cowork's **Sync refreshes the catalog, not the plugin files**, so a plain Sync
can leave you on the cached version. To force the new version:
> Cowork → Plugins → **remove the plugin and the marketplace** → **re-add the
> marketplace URL** → **reinstall** → **start a new session**.

## Layout
```
.claude-plugin/     plugin.json + marketplace.json (this repo is both plugin and marketplace)
commands/           the /olf-elcc-review-bot:review slash command
skills/             review (orchestrator) + summarize-matter, spot-issues, redline, client-email
reference/          legal-brain.md, output-contract.md
assets/             console-template.html
tools/              redline_to_docx.py, check_review_state.py (guard), release.sh
tests/fixtures/     golden + negative review-state fixtures for the guard
```
