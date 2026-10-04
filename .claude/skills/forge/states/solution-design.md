---
description: Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on
---

The definition of the solution design's elicitation, in the seven
blocks of POS.1310 of the forge intent; what it is to achieve and
why is POS.1400 and POS.1420. Shared mechanism is cited and never
repeated here: the form of the conversation and one write per round
(CLAUDE.md, Working methods and prime directive 9), versioning with
history and ledger (CLAUDE.md, Versioning & status), the language
(CLAUDE.md, prime directive 6).

**Target.** `40-solution-design.md`. Shape of the result:
`templates/solution-design.md`.

**Inputs.** The lowest layer the project has above it, the intent
alone, the assignment or the BRD, and whatever stands above that;
`decisions.md`, the ledger. The intent is read with the project's
threads, `threads.md`. Where the thing already exists, what
realises it is read as it stands. Research and sources as the
principal directs.

**Aim.** The solution design says how the things wanted are
realised, as the solution stands today, and is kept current. It is
read by whoever realises the solution, a person or an agent,
without the principal in the room. It holds what cannot be read off
the thing itself: why, against what, at what price, and how the
parts fit. It restates nothing of the layer above, which it cites
by ID, and copies nothing of what realises it, which it names by
path. It is complete for now when every item of the layer above
that is in scope is realised by a part, knowingly left unanswered,
or open as a TBC, and when no TBC that blocks realisation is open;
it is never finished.

**Partner.** How the design is composed is the principal's choice
(CLAUDE.md, Working methods, Handing over). Either way Claude
proposes the parts and the choices and the principal judges them.
Claude names the few real choices and does not dress every part as
one: where there was no real alternative he says so and invents
none, and where a reason is not known he says it is unknown. How
sure he is of a claim he says in words. What the designing shows
cannot be realised, or only at a price not worth paying, he raises
as a thread, and what is wanted is decided in the intent first
(CLAUDE.md, Working methods, Intent-first). Nothing is built here:
the design specifies.

**Map.** What the design finds, whatever the order; where it lands
is the template's. Walked before the design is returned or a write
is offered; an area may stay empty when it was considered and found
not to apply.
- what is to be realised: the items of the layer above the design
  answers, and what of them it knowingly leaves unanswered;
- the ground: what already exists and is kept or replaced, what
  stands around it, and what the principal has fixed in advance;
- the approach as a whole: the few ideas the solution rests on;
- the parts: what is built or done, by whom where it is not
  software, and where each is realised;
- how the parts work together, and what holds across them;
- the choices: for each real one, what it was chosen against, doing
  nothing or the least that would do among it, and what it costs;
- what is open or unproven: what would close it, and whether it
  blocks realisation;
- how it will be known to hold: by what the thing is compared with
  the design;
- the way there, where the solution replaces something that runs;
- what is deliberately not designed and left to the file or to the
  one who realises.

**Instruments.** The coverage map of the Course below. `/research
<topic>`: proposed where a choice needs outside grounding, run on
the principal's word. `/challenge <persona> solution-design`: the
independent test of the choices, offered once the design stands,
never run on Claude's own judgement.

**Course.** Resolve the project and read the inputs and the design
as it stands. The ways in: no design yet, and whether one is worth
writing is the principal's to say (POS.1400); a layer above that
moved, and the pass runs on what changed; the thing changed below,
and the design is brought current; a wording fix, made directly.
With every pass Claude makes the coverage map: the in-scope items
of the layer above with no part, and the parts that realise no
item. The map is a tool of the pass, not part of the design. End by
naming what changed and what stays open; when the Aim's completion
is reached, offer the approval: a recommendation, never a gate.

How the files are made: the first design is created from
`templates/solution-design.md` as v0.1, with its companion
`40-solution-design.history.md` from `templates/history.md` and its
row in the ledger's Documents table. SOL and TBC follow the ID
scheme of CLAUDE.md. A write rewrites for coherence, never appends;
empty sections and all template comments are deleted.

**The shape of an item.**
- A SOL is a part of the solution, or a matter that holds across
  parts. It says what the part is and what it answers for, then in
  this order: `Realises:` the IDs of the layer above, never their
  wording; `Choice:` what was chosen, against what, and what it
  costs, or that there was no real alternative; `Where:` the path.
- Where a part is realised in a file of its own, the item names the
  file and the detail is the file's. Where it is only part of a
  file, or no file exists yet, the item carries the detail.
- A choice Claude made and the principal has not judged says so in
  plain words at the item, until he has judged it.
- A TBC carries its owner, what would close it, and whether it
  blocks realisation.
