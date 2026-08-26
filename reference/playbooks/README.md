# Commercial-contract playbooks

Client-approved **preferred / fallback** positions for the OLF review, one file
per sub-type, keyed to the same 8-way classification the plug-in already uses
(`reference/subtype-lenses.md`, `legal-brain.md` §2). These power **playbook
mode** (`legal-brain.md` §9): the review measures the draft against these
positions instead of reasoning purely from first principles.

## Files

| File | Sub-type | Depth |
|---|---|---|
| `_core.yaml` | Shared spine (applies to all) | — |
| `01-financial-advisory.yaml` | Financial advisory & transaction ELs | Complex |
| `02-professional-services.yaml` | Professional services | Complex |
| `03-technology-saas.yaml` | Technology, SaaS & software | Complex |
| `04-data-privacy-security.yaml` | Data, privacy & security | Complex |
| `05-managed-services-outsourcing.yaml` | Managed services & outsourcing | Complex |
| `06-routine-vendor-supplier.yaml` | Routine vendor & supplier | Simple |
| `07-facilities-events-hospitality.yaml` | Facilities, events & hospitality | Simple–Complex |
| `08-other.yaml` | Other / uncategorised | Complex |

## How the review loads a playbook

1. Classify the document into a sub-type (existing step).
2. Load **`_core.yaml`**, then the matching **`NN-*.yaml`** overlay.
3. **Merge:** an overlay entry with the same `id` as a core entry **overrides**
   it; a new `id` **adds**. (Overrides are used where a sub-type needs a tighter
   position than the generic core — e.g. `auto-renewal`, `liability-cap`.)
4. If the document plainly carries a second type (e.g. SaaS **with a DPA**), pull
   in that secondary overlay for the relevant part (each file's `meta` notes this).

## How each entry drives the output

Every entry maps onto the brain's existing axes — nothing new for the reviewer to
learn:

- `preferred` / `fallback` → the landing zone in the combined issue item
  (`legal-brain.md` §11). Draft outside the furthest fallback ⇒ surface it.
- `default_stance` (`push_back` | `negotiate` | `acceptable`) → the **stance**
  shown on the issue (§11).
- `owner` (`legal` | `business` | `hybrid`) → the **business-vs-legal split**
  (§8). `business` items go to the client escalation email and are **never**
  redlined; `hybrid` entries carry an `owner_split` telling you which half is which.
- `red_flag_if` → the condition that promotes the issue to a **RED FLAG** (§4).
- `missing_is` (`red_flag` | `watch` | `ok`) → the **missing-provision check**
  (§4): how to treat the clause's *absence*.
- `model` → approved precedent wording to use in the redline when we have it.
- `normalization_rules` (core only) → mechanical language edits applied to the
  client's obligations; redline these as **silent** (§10), not as issues.

Playbook mode **sharpens, never gates** the review (§9): if no playbook is
accessible, the review proceeds on the brain alone. When a position is applied
from here, cite it as "outside the client's approved fallback" rather than as a
free-standing opinion.

## Schema (per entry)

```yaml
- id: liability-cap            # stable key; the override target across files
  family: Limitation of liability
  issue: Cap on liability
  owner: legal | business | hybrid
  owner_split: {legal: "...", business: "..."}   # only when owner: hybrid
  preferred: "..."
  fallback: "..." | ["...", "..."]               # furthest acceptable landing zone
  default_stance: push_back | negotiate | acceptable   # legal/hybrid items
  red_flag_if: "condition"        # optional — promotes to RED FLAG
  missing_is: red_flag | watch | ok   # optional — how to treat absence
  model: "..."                    # optional — approved precedent wording
  note: "..."                     # optional
```

## Provenance

Distilled from Ontra's negotiation playbooks: the Standard NDA Playbook (shared
confidentiality / non-solicit / boilerplate spine), the Template Vendor Agreement
Playbook (the commercial buckets and the legal-vs-check-with-client split), and
the Vendor Diligence EL Playbook (the engagement-letter positions in `01`).
Deal-specific NDA rows (standstill, anti-clubbing, financing "tree", no-contact,
non-circumvent) were intentionally **not** carried over — they do not apply to
commercial paper.

**Maintenance:** these encode *client-approved* positions. Treat changes as legal
content, not code — a lawyer should sign off before a position changes.
