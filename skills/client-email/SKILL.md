---
name: client-email
description: Draft the escalation email from the OLF lawyer to the client / deal team, presenting the business decisions they must make and the legal points the lawyer is handling. Trigger on "draft the client email", "write the escalation email", "email the client about this", "prepare the client communication", or as the escalation step of the review. Goes to the CLIENT (who engaged OLF), never to the counterparty. Draft-only — never sends.
---

# Draft the client escalation email

Package the review's business decisions and legal posture into one clear email
the client can act on. It goes to the **client / deal team** who engaged OLF —
not to the counterparty.

**Read first:** the `client_email`, "Commercial deal terms", and "Legal issues &
recommendations" sections of `${CLAUDE_PLUGIN_ROOT}/reference/output-contract.md`.
Single-source from the same `business_terms[]` and `legal_issues[]` the review
already produced — do not re-analyse or introduce anything new.

## Structure

Keep it short. **Do not list the legal issues in the body** — those are handled
in the markup; this email is about the client's commercial decisions.

- **Subject** — `<Client>, <counterparty> <doc type>: decisions needed`.
- **Greeting + one-line context** — what the document is and where it stands
  (first-pass done, markup drafted).
- **Business decisions we need from you** — the `business_terms[]` as a
  **numbered list**, one item per term: the term (with its number, in **bold**)
  followed by the specific question. Present, don't opine. This list is the body
  of the email, and it must be a list, not a run-on sentence.
- **Clear ask + next step** — what you need back (leave the date for the lawyer),
  and that the tracked-changes redline is ready to go on their confirmation.
- **Sign-off** — leave sender name/title as an easily-edited placeholder.

## Voice — write like a lawyer, not like an AI

The email must read as if a busy senior lawyer typed it in a hurry, not as
"Claude-speak." Apply this:
- **Plain and direct.** Short sentences. Say the thing. A colleague, not a chatbot.
- **Cut AI throat-clearing and filler** — no "I've gone ahead and…", "I hope this
  finds you well", "Please find below", "As requested", "I'd be happy to", "Great
  question", "Certainly". No summarising what the email is about to do; just do it.
- **No over-explaining or hedging.** Don't justify or pad; state the decision needed.
- **No praise, no meta-commentary, no signposting** ("Below you will find…").
- **Concrete and specific** — the term, the number, the question. Nothing generic.
- **Brief.** A one-line context, the numbered decisions, a one-line ask, sign-off.
  If a sentence isn't load-bearing, delete it.
- **House style:** no em-dashes (`—`); use commas, colons, or new sentences.

Test it: if a line sounds like an assistant wrote it, rewrite it the way a lawyer
emailing their deal team would.

## Output

Fill `client_email{subject, body_markdown}` in the review-state. The email is a
**draft** — it renders in the HTML console (the "Draft client escalation email"
section) with a copy affordance and is never sent. The lawyer edits and sends it
from their own client.
