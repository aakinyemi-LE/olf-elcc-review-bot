#!/usr/bin/env bash
# release.sh — bump the version atomically across both manifests and run the
# regression guard, so a release is one deterministic step (no hand-edited,
# out-of-sync version fields).
#
#   tools/release.sh 0.1.3
#
# It does NOT git-commit or push — it prints the exact next steps so you stay in
# control. The GitHub repo is the single source of truth (see RELEASE.md).
set -euo pipefail
VER="${1:?usage: tools/release.sh <version>   e.g. 0.1.3}"
cd "$(dirname "$0")/.."   # repo root

python3 - "$VER" <<'PY'
import json, sys
ver = sys.argv[1]
def bump(path, kind):
    d = json.load(open(path))
    if kind == "plugin":
        d["version"] = ver
    else:  # marketplace
        if d.get("metadata", {}).get("version"): d["metadata"]["version"] = ver
        for pl in d.get("plugins", []):
            if pl.get("name") == "olf-elcc-review-bot": pl["version"] = ver
    json.dump(d, open(path, "w"), indent=2); open(path, "a").write("\n")
    print("  set", path, "->", ver)
bump(".claude-plugin/plugin.json", "plugin")
bump(".claude-plugin/marketplace.json", "marketplace")
PY

echo "Running regression guard…"
python3 tools/check_review_state.py tests/fixtures/*.review-state.json

cat <<EOF

Version set to ${VER} and fixtures pass. Next:
  git add -A && git commit -m "Release ${VER}" && git push origin main

Then in Cowork (Sync alone does NOT re-pull files):
  Plugins → remove the plugin AND the marketplace → re-add the marketplace URL → reinstall → new session.
EOF
