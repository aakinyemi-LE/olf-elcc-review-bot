# Sub-type lenses

The review is one method (see `legal-brain.md`), but *what to look hardest at*
depends on the contract's sub-type. Classify the document into one of the eight
sub-types below, then apply that lens: it re-weights the clause walk, adds the
red flags that actually bite for this type, and sets the key-terms checklist and
default depth. The lens does not replace the general clause families (brain §5
engagement letters, §6 commercial contracts, §7 cross-cutting) — it prioritises
them and adds type-specific checks.

**Classification.** Pick the single best fit from its signals. If none clearly
fits, or the document straddles types, use **8 (Other)** and proceed — label the
matter "Other / uncategorised", note the sub-type was uncertain, and let the
lawyer redirect. The lawyer can always override the sub-type. When a contract
plainly carries a second type inside it (e.g. a SaaS agreement with a full DPA),
run the primary lens and pull in the secondary lens for that part.

Each lens: **Signals · Review hardest · Type red flags · Key terms · Depth.**

---

## 1. Financial advisory & transaction engagement agreements
*(investment bank / M&A advisor / placement agent / capital-raising — this is the
engagement-letter family; use brain §5.)*
- **Signals:** "engagement letter"; advisor/banker/placement agent as
  counterparty; success or transaction fee; "Aggregate Consideration"; tail and
  exclusivity language.
- **Review hardest:** success/transaction fee (% and its base) and any minimum;
  when the fee is *earned* (signing vs closing); tail (length, trigger,
  covered-party list); exclusivity scope; indemnity of the advisor; advisor's own
  liability cap; expenses; reliance / no-fiduciary; fee survival on termination.
- **Type red flags:** fee earned on an IOI/LOI or payable even if the deal fails;
  long tail with no covered-party list; client indemnity covering the advisor's
  own negligence; advisor cap at retainers while client exposure is uncapped;
  uncapped/unapproved expenses; over-broad "Client Group" sweep.
- **Key terms:** success fee %/base, minimum, retainer, tail length+trigger,
  exclusivity, term, indemnity, advisor cap, expenses, governing law.
- **Depth:** Complex.

## 2. Professional services agreements
*(consulting, accounting/tax, marketing/agency, staffing, advisory — brain §6.)*
- **Signals:** "services agreement"; SOW / statement of work; deliverables;
  hourly/day rates; consultant/contractor.
- **Review hardest:** scope & deliverables & acceptance; fees, rates & expenses;
  IP / work-product ownership; non-solicit; service warranty (skill and care);
  liability cap; independent-contractor status; confidentiality; termination.
- **Type red flags:** vendor keeps IP in bespoke deliverables the client paid for;
  broad client indemnity; no service warranty / "as is"; over-broad or long
  non-solicit; silent auto-renewal; uncapped or one-way liability; open-ended
  expenses.
- **Key terms:** fee structure/rates, SOW mechanics, IP ownership, non-solicit
  scope/term, liability cap, term/termination, warranty.
- **Depth:** Complex (Simple if one-off and low value).

## 3. Technology, SaaS & software agreements
*(subscriptions, hosted software, licences, order forms — brain §6.)*
- **Signals:** "subscription", "SaaS", "software licence", order form, uptime/SLA,
  "hosted", acceptable-use policy, seats/users, URL-linked "standard terms".
- **Review hardest:** term & **auto-renewal + notice window**; uptime/SLA &
  service credits; **data ownership & security** (pull in lens 4 if a DPA is
  attached); licence/IP scope & restrictions; **price increases / uplift**;
  acceptable use & suspension; warranties & IP-infringement indemnity; liability
  cap & carve-outs; unilateral amendment of URL terms; exit & data return.
- **Type red flags:** auto-renew with a long notice tail; unilateral change of
  URL-linked terms; vendor claims rights in client data; uncapped price uplift;
  a one-way/low cap that swallows the data-breach carve-out; "AS IS" for a
  business-critical service; no data return/portability on exit.
- **Key terms:** term, renewal/notice, fees + uplift cap, SLA %/credits, data
  ownership, security standard / DPA presence, liability cap + multiple, IP
  indemnity, exit terms.
- **Depth:** Complex.

## 4. Data, privacy & security agreements
*(DPA, BAA, data-sharing, standard contractual clauses — brain §6.)*
- **Signals:** "data processing agreement", controller/processor, "personal
  data", GDPR/CCPA/HIPAA, sub-processors, SCCs, "processing".
- **Review hardest:** roles (controller vs processor vs joint); processing purpose
  & scope; sub-processor authorisation & flow-down; **cross-border transfer
  mechanism** (SCCs/adequacy); security measures (TOMs); **breach-notification
  timeline**; audit/inspection rights; data return/deletion on exit; liability &
  indemnity for a breach; regulator cooperation; retention.
- **Type red flags:** no or slow breach-notification window; unrestricted
  sub-processors; no transfer mechanism for cross-border data; weak/undefined
  security standard; vendor re-use of personal data ("to improve services");
  liability cap that swallows the data-breach carve-out; no deletion on exit;
  missing audit rights.
- **Key terms:** role, transfer mechanism, breach-notice window, sub-processor
  terms, security standard, retention/deletion, audit, liability position.
- **Depth:** Complex.

## 5. Managed services & outsourcing agreements
*(BPO, IT outsourcing, payroll/HR, facilities management — brain §6.)*
- **Signals:** "managed services", "outsourcing", governance / steering
  committee, SLAs, transition, service credits, "in-scope services".
- **Review hardest:** SLAs & service credits & earn-back; governance & reporting;
  change control; **transition-in / exit assistance & disentanglement**;
  benchmarking; data & security (pull in lens 4); business continuity / DR;
  liability & whether service credits are the *sole* remedy; termination &
  step-in; personnel/TUPE; subcontracting.
- **Type red flags:** service credits as the sole/exclusive remedy; no exit or
  transition assistance (lock-in); no benchmarking; weak DR/BCP; uncapped or
  asymmetric liability; unilateral change control; no data return on exit.
- **Key terms:** SLA targets & credits, term, exit assistance, governance cadence,
  liability cap, security standard, price/change mechanics.
- **Depth:** Complex.

## 6. Routine vendor & supplier agreements
*(goods, supplies, low-risk one-off services — brain §6, light touch.)*
- **Signals:** purchase of goods/supplies; short form; low value; no personal-data
  access or IP creation; one-off or simple recurring.
- **Review hardest (light touch):** price & payment terms; term & auto-renewal;
  termination for convenience; basic liability & indemnity; warranty/returns;
  delivery. **Flag only the outliers** — do not over-review a routine deal.
- **Type red flags:** surprise auto-renewal with a long notice period; unusually
  long term or no convenience out; one-sided indemnity; **personal-data access
  hiding in a "routine" deal** (escalate to lens 4); liability disproportionate to
  the deal's value.
- **Key terms:** price, payment terms, term/renewal, termination, liability.
- **Depth:** Simple by default (escalate to Complex if data, IP or a critical
  dependency appears).

## 7. Facilities, events & hospitality agreements
*(venues, catering, conferences, hotel room blocks, travel — brain §6.)*
- **Signals:** venue/hotel; event date; room block; banquet/catering; "attrition";
  cancellation schedule; minimum spend / F&B minimum; deposits.
- **Review hardest:** cancellation & attrition schedule; **force majeure** (does
  it cover epidemic / government order?); deposit & payment schedule; minimum
  spend; insurance & indemnity (injury/property); liability for guests/attendees;
  permits/compliance; IP / publicity / photography; damage or security deposit.
- **Type red flags:** punitive, escalating cancellation/attrition penalties;
  narrow force majeure with no epidemic/government-order cover; large
  non-refundable deposits; one-way injury indemnity; uncapped attrition liability;
  auto-charged minimums.
- **Key terms:** event dates, cancellation/attrition scale, deposit schedule,
  minimum spend, force-majeure scope, insurance/indemnity, total value.
- **Depth:** Simple to Complex by value and headcount.

## 8. Other commercial contracts
*(fallback — nothing above clearly fits, or the type is ambiguous.)*
- **Signals:** none of 1–7 match, or the document straddles several.
- **Behaviour:** run the **general** commercial-contract brain (§6) and the full
  cross-cutting sweep (§7). **Label the matter "Other / uncategorised" and note
  the sub-type was uncertain**, so the lawyer can redirect to a specific lens. Do
  not force a wrong lens onto the document.
- **Key terms:** the general operative-terms checklist (brain §6).
- **Depth:** Complex (the safer default when unsure).
