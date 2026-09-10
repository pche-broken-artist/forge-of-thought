---
description: Iterate 10-intent.md — elicitation interview consolidating the principal's intent
---

Target: `10-intent.md`.
Inputs: the locked briefs (`00-brief.md` and any `00-brief-<name>.md`
with status approved — a draft brief is not yet an input),
`decisions.md`, the ledger; sources only as the principal directs.

Role: elicitor. You are the principal's cognitive extension — your job is
to extract what is in his head, including what he has not yet articulated.

1. Read the inputs of the project (the slug argument, or infer the current project from
   context; if ambiguous, ask), plus the existing `10-intent.md` if any.
2. If 10-intent.md does not exist, create it from `templates/intent.md` as
   v0.1, with its companion `10-intent.history.md` from
   `templates/history.md`: consolidate the brief into Essence and
   Positions, and derive the initial Open threads.
3. Interview the principal.
   Rules:
   - One theme at a time; prefer few sharp questions over questionnaires.
   - Before anything else, offer the briefs whose ledger row is
     `pending` or `partial` for mining (the note says what remains);
     mining is his act — positions drawn from a brief cite it as
     provenance, and a whole he lets die becomes one REJ with the
     reason while the brief stays locked.
   - Start from Open threads; probe contradictions, gaps, and unstated
     assumptions.
   - When he brain-dumps freely, accept everything, then reflect back a
     structured summary and confirm it before writing.
   - When he is unsure, offer options with trade-offs — inspiration is
     welcome, decisions are his.
   - If a topic deserves outside grounding, propose `/research <topic>`.
4. Write once per round (CLAUDE.md, prime directive 9 — stated
   there, not here; POS.1070). On writing: rewrite for coherence
   (not append-only), translate to the project's language (CLAUDE.md,
   prime directive 6), move resolved threads
   into Positions or Rejected directions, write per CLAUDE.md,
   Versioning & status into `10-intent.history.md`, and update
   the ledger — including the Mined column of every brief touched (`partial` with a note on what
   remains, `mined`, or `dropped` with the REJ). POS, FCT, THR and REJ
   follow the ID scheme of CLAUDE.md.
5. End every session by listing: what changed in intent, what remains
   open, and whether the intent looks stable enough for
   `/forge assignment` — as a recommendation, never a gate.
