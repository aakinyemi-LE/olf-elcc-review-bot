#!/usr/bin/env python3
"""
check_review_state.py — validate a review-state (or console projection) JSON
against the output contract's structural invariants.

This is the regression guard: it catches the classes of drift we have actually
hit — a stray separate `recommendations[]`, an opinion line in the matter block,
issues missing their position/fallback, and cap/brevity violations. Run it on a
produced review-state before shipping, or over the test fixtures in CI.

Usage:
    python tools/check_review_state.py <file.review-state.json> [more.json ...]
    python tools/check_review_state.py tests/fixtures/*.review-state.json

Exit code 0 = all files pass (no ERRORs); 1 = at least one ERROR. WARNINGs never
fail the run — they flag brevity/caps to eyeball.
"""
import json
import sys

STANCES = {"push_back", "negotiate", "acceptable", "walk_away"}
ISSUE_FIELDS = ("clause", "stance", "says", "risk", "recommendation", "fallback")
LONG = 240  # a field longer than this is a paragraph, not a clause


def check(path):
    errors, warns = [], []
    try:
        d = json.load(open(path))
    except Exception as e:
        return [f"cannot parse JSON: {e}"], []

    # --- structural invariants (ERRORs) ---
    if "recommendations" in d:
        errors.append("top-level `recommendations[]` present — it must be folded into legal_issues[]")

    m = d.get("matter") or {}
    if m.get("overall_read"):
        errors.append("matter.overall_read present — the matter block carries no opinion")
    pls = m.get("party_lines")
    if not isinstance(pls, list) or not pls:
        errors.append("matter.party_lines missing or empty — need one line per party")
    elif len(pls) != 2:
        warns.append(f"matter.party_lines has {len(pls)} lines (expected 2: counterparty, client)")
    if not m.get("doc_type") and not m.get("sub_type"):
        warns.append("matter has no doc_type/sub_type")

    li = d.get("legal_issues")
    if li is None:
        errors.append("legal_issues[] missing (note: the key is legal_issues, not issues)")
        li = []
    for i, x in enumerate(li):
        for f in ISSUE_FIELDS:
            if not x.get(f) and not (f == "fallback" and x.get(f) == "—"):
                if f not in x or x.get(f) in (None, ""):
                    errors.append(f"legal_issues[{i}] missing `{f}`")
        st = str(x.get("stance", "")).lower()
        if st and st not in STANCES:
            errors.append(f"legal_issues[{i}].stance '{st}' not in {sorted(STANCES)}")
        for f in ("says", "risk", "recommendation"):
            if isinstance(x.get(f), str) and len(x[f]) > LONG:
                warns.append(f"legal_issues[{i}].{f} is {len(x[f])} chars — keep it to one clause")

    # --- caps (WARNs) ---
    n = len(li)
    if n and not (3 <= n <= 6):
        warns.append(f"legal_issues has {n} entries (cap is 3–6 highest-value)")
    bt = d.get("business_terms") or []
    if len(bt) > 5:
        warns.append(f"business_terms has {len(bt)} (cap ≤ 5)")
    kt = d.get("key_terms") or []
    if len(kt) > 12:
        warns.append(f"key_terms has {len(kt)} (cap ≤ 12)")
    for i, t in enumerate(kt):
        missing = [f for f in ("term", "provision") if not t.get(f)]
        if missing:
            warns.append(f"key_terms[{i}] missing {missing}")

    ce = d.get("client_email") or {}
    if not ce.get("subject") or not ce.get("body_markdown"):
        warns.append("client_email missing subject or body_markdown")

    # house style: no em-dashes in displayed text
    emd = []
    def scan(v, where):
        if isinstance(v, str):
            if "—" in v:
                emd.append(where)
        elif isinstance(v, list):
            for i, x in enumerate(v):
                scan(x, where + "[" + str(i) + "]")
        elif isinstance(v, dict):
            for k, val in v.items():
                scan(val, where + "." + k)
    for key in ("matter", "legal_issues", "business_terms", "key_terms", "client_email"):
        scan(d.get(key), key)
    if emd:
        warns.append("em-dash found in: " + ", ".join(emd[:8]) + (" …" if len(emd) > 8 else "") + " (house style: no em-dashes)")

    return errors, warns


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    any_err = False
    for path in sys.argv[1:]:
        errors, warns = check(path)
        status = "FAIL" if errors else ("WARN" if warns else "PASS")
        print(f"[{status}] {path}")
        for e in errors:
            print(f"   ✗ ERROR: {e}")
        for w in warns:
            print(f"   • warn:  {w}")
        any_err = any_err or bool(errors)
    sys.exit(1 if any_err else 0)


if __name__ == "__main__":
    main()
