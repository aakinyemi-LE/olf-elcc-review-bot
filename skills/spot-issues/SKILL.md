---
name: spot-issues
description: Spot and classify the issues in an engagement letter or commercial contract, and split them into legal red flags (lawyer's call) and commercial deal terms (client's call). Trigger on "what are the issues", "where are the problems", "flag the red flags", "what needs to go to the client", "triage these terms", "what's off-market", or as the analysis step of the review. Requires the document (and key terms if already extracted); uses a playbook only if one is accessible.
---

# Spot & classify issues; split business vs legal

Walk the document against the brain, classify every issue, and route each to its
audience. This is the analytical core of the review.

**Read first:** `${CLAUDE_PLUGIN_ROOT}/reference/legal-brain.md` — §4
classification, §5/§6 clause families, §7 cross-cutting sweep, §8 business/legal
split, §9 playbook/precedent. Use the `review-state` shape from
`${CLAUDE_PLUGIN_ROOT}/reference/output-contract.md`.

## Steps

1. **Walk the clause families** (§5 engagement letter / §6 commercial contract).
   For each: present? what does it say? market/acceptable for a client in our
   position?
2. **Classify each issue** into exactly one class (§4): `red_flag` (legal risk /
   material off-market), `business` (client's commercial call), `watch`
   (ambiguous / unseen incorporated doc / novel / fact-dependent), `acceptable`.
   When torn, escalate up (red_flag > watch > acceptable). Under-flagging is the
   costly error.
3. **Cross-cutting sweep** (§7): incorporated-but-unseen terms, defined-term
   drift, asymmetry, survival, number/measurement-point mismatch, silent gaps
   (missing-provision check).
4. **Ground if accessible** (§9): if a relevant client/counterparty playbook or
   precedent is reachable, measure the draft against it and note departures and
   "we've accepted/rejected this before". If none, say so and proceed — never
   stall.
5. **Split business vs legal** (§8): set each issue's `audience`. Route legal
   issues to the lawyer's worklist (and they drive the redline); route business
   terms to `business_terms[]` (they seed the client email). Split hybrids (e.g.
   success fee: % is business, fee-base definition is legal).
6. **Form recommendations** (§11): for each material point take a **stance** —
   `push_back` / `negotiate` / `acceptable` / `walk_away` — with a reason and a
   `fallback` landing zone. This is judgment ("concede this, fight that"), not an
   administrative checklist. Fill `recommendations[]`.

## Output

Fill `issues[]` (with `class`, `audience`, `clause`, `says`, `risk`,
`recommendation`), `business_terms[]`, and `recommendations[]` (`point`, `stance`,
`recommendation`, `fallback`). When standalone, present: legal issues
(most-serious first), commercial terms for confirmation, then the recommendations
with their stances. **Present business terms, never opine** on price or deal
merits; where a stance turns on commercial appetite, say it is subject to the
deal team's call. Offer to proceed to the redline and client email.
