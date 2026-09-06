---
description: Compose or finish a brief — the principal's own text of one whole of thinking, locked when done
---

Target: `00-brief.md` (bare) or `00-brief-<name>.md` (with a name — a
later whole of thinking born during the project's life).
Inputs: none but the principal. The existing intent and ledger are
read only to know what already stands, never to shape the text.

Role: clarifier and reality check under the principal's moderation,
never author. He says what is being explored and steers; Claude stays
on the theme he set and does not take the helm. What a brief is —
its freedom of form, its language, its lifecycle from draft to the
lock — is CLAUDE.md's (Document chain, item 1) and is not restated
here. The aim is a thought clear enough to be checked against what
already exists.

Two things Claude does throughout, whichever way the text arrives:
- **Clarify.** Where he is terse or unclear, ask — not to add Claude's
  own content, but to get his thought out in a form that can be
  understood and tested.
- **Correlate with reality.** Keep offering the confrontation with
  what exists: best practice, projects and tools that solve the same
  thing, standards — "are we reinventing the wheel?", "X does this;
  inspiration, or is the difference here?". The instruments are
  `/research <topic>` (durable findings into `research/`, indexed) and
  `/ingest` (outside material into `sources/`); Claude proposes them,
  the principal says when. What a check or an inspiration contributes
  enters the brief only by his word: the brief stays his text, not a
  literature review.

1. Resolve the project (the slug argument, or infer from context; if ambiguous, ask)
   and the file. If the named brief does not exist, create it from
   `templates/brief.md` (the minimal YAML header, nothing else), its
   companion `<file>.history.md`
   from `templates/history.md`, and add its row to the ledger's Briefs
   table (Mined: pending). If it exists and is `approved`, stop: a locked
   brief is not edited — a new whole is a new brief.
2. However the text arrives:
   - **Pasted whole:** store it verbatim and ask whether it is
     finished — if so, lock it at once (step 4).
   - **Begun outside, to be finished here:** store what came, then
     clarify and correlate as above and let him write or dictate the
     additions. Claude may draft a sentence to sharpen his reaction,
     but the words that stay are his.
   - **Born here:** he opens with what is being explored; Claude
     clarifies and correlates from the first word and accumulates his
     answers as his text, not as a summary of them.
   Never translate, restructure or tidy the text. Never introduce
   IDs or conventions. When he asks to record a summary or a
   structured proposal Claude has just shown him, store it as shown —
   headings, tables and lists included — never re-narrated as prose.
3. Write once per round on his confirmation, per CLAUDE.md,
   Versioning & status (a 0.x bump); the ledger row is its state.
4. **Lock** only on his explicit word: version 1.0, status approved,
   the lock's row per the same rule; ledger row updated. A brief that arrived finished has that one
   row. From then on the file is
   immutable and its whole is mined by `/forge intent`, which keeps
   the Mined column current.
5. End by naming the state — draft or locked — and, if locked,
   proposing `/forge intent` to mine it.
