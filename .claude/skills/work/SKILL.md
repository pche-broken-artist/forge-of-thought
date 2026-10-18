---
description: Work a work product — bare = the roster of the project's work products, with a name = iterate its specification and make its file
argument-hint: "[name] [project-slug]"
---

Role: the one door to a work product (CLAUDE.md, Document kinds;
POS.1520, SOL.0640). A work product is two files in `work/`: the
specification `work/<name>.spec.md`, the way and the why, and the file
`work/<name>.<ext>`, the content, named by the work alone. Shared
mechanism is cited and never repeated here: one write per round
(CLAUDE.md, prime directive 9),
versioning with history and ledger (Versioning & status), the language
(prime directive 6: the specification in the project's language, the
file in whatever language the work needs, said in `## Making`), the
two ways of composing (Working methods, Handing over and Elicitation
interview). The shape of the specification is `templates/work.md`.

**Bare `/work` — the roster.**
1. Infer the current project from context ($0 may be a slug; if
   ambiguous, ask).
2. Read the ledger's Work table and list each work product: its file,
   the specification with its version, the inputs, when it was made
   and its state (`current` | `stale` | `by hand`).
3. Recommend a next step only where the conversation suggests one.

**`/work <name>` — work the specification and make the file.**
1. Resolve `work/<name>.spec.md`. If it does not exist, its birth is
   a step of its own on the principal's word (CLAUDE.md, Working
   methods, Step by step): the specification from `templates/work.md`
   as v0.1, its companion `work/<name>.spec.history.md` from
   `templates/history.md`, its row in the ledger's Work table with
   Made `—` and state `stale`.
2. Read the inputs the specification names, by ID and by path, as they
   stand; the intent with the project's threads where it is among them.
3. Work the specification with the principal, the way he chooses:
   handed over, Claude works it alone from what he was given, from
   research and from the sources, and returns a proposal with his
   assumptions and choices listed, each choice with what it was chosen
   against; found together, by elicitation interview. The specification
   cites and never copies; assumptions are ASM items and open matters
   TBC items with an owner, by the ID scheme of CLAUDE.md; `## Making`
   says how the file is made from it.
4. Reflect the round back and write once, on the principal's word:
   the specification rewritten for coherence, unused placeholders and
   template comments deleted; the records appended to the companion
   and `last_change` derived from them; the ledger row with the new
   version and the state `stale`. Approval of the specification (1.0
   and on) is the principal's word, as the house scheme has it.
5. Make the file on the principal's word, in the same round or a
   later one, as `## Making` says: `work/<name>.<ext>`, carrying of the
   specification only what `## Making` says it carries. Then the
   ledger row: the inputs with their versions, the date made, the
   state `current`. A file the principal has worked by hand and does
   not want remade is `by hand` on his word; Claude never remakes it
   on his own judgement — he names it and offers. A file by hand carries
   the states of the work and its wording; a change of the way or the
   why made in it, its task, its inputs, its method or what it
   assumes, is carried into the specification in the same round and
   written with it, the record in the specification's history naming
   the change of the file (POS.1520).
6. End by naming what was written and where, and what the ledger row
   says.
