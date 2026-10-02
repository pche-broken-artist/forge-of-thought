---
description: Iterate 20-assignment.md — the intent's in-scope substance carried to the recipients in a joint pass
---

The definition of the assignment's elicitation, in the seven blocks
of POS.1310 of the forge intent; what it is to achieve and why is
POS.1350. Shared mechanism is cited and never repeated here: the form
of the conversation and one write per round (CLAUDE.md, Working
methods and prime directive 9), versioning with history and ledger
(CLAUDE.md, Versioning & status), the language (CLAUDE.md, prime
directive 6).

**Target.** `20-assignment.md`. Shape of the result:
`templates/assignment.md`.

**Inputs.** `10-intent.md`, `decisions.md`, the ledger. The intent is
read with its threads, `10-intent.threads.md`.

**Aim.** The assignment carries the in-scope substance of the
intent to the recipients, complete and precise, so that they can
act on it without the principal in the room: who they are, what
must be true at the end, what is theirs to decide and bring back,
what they shall not do, and what the principal has left open on
purpose. It is complete when nothing the recipients would need is
left to assumption — delegated or open on purpose is complete,
silent is not — and when they know what must be true at the end,
and why, well enough to act rightly where the plan no longer fits.
Nothing is omitted for brevity's sake, and length is whatever
fidelity requires; leaving a matter out is legitimate only as an
explicit delegation (a DEL or TBC item). The boundary is the kind
of content, assigning and not solving, never its amount: machinery
of executing delivery belongs to the recipients, but any apparatus
(a stakeholder matrix, an impact analysis) may appear where the
principal judges it part of setting direction.

**Partner.** Claude reads the intent against what the assignment
needs — recipients, objective, delegation, success criteria,
horizon — and takes the principal through the joint pass below.
What the intent is silent on he raises as a TBC rather than filling
it, and a substance change he proposes to the intent first. The
wording is Claude's, in the Requirement style; the substance the
principal's.

**Map.** What the assignment finds, most of it in the intent and
the rest by asking; where it lands is the template's. Walked
twice: before the recast, to see what the intent leaves
unanswered, and at the end of the joint pass; an area may stay
empty when it was considered and found not to apply.
- the recipients: who they are, what they already know and what
  they will do with the assignment;
- the objective: what must be true at the end;
- the cut: what of the intent is theirs now, what is expressly
  later and what is out of scope;
- the line between assigning and solving: what is specified, what
  is theirs to decide and bring back, what is left open on purpose
  and whose it is;
- the boundaries: what they shall not do, what is not to be
  challenged, and what the whole rests on;
- success: criteria present, delegated or deliberately absent;
- self-containment: what must be defined so that the assignment is
  read without the principal in the room.

**Instruments.** The provenance map and the walkthrough by group,
both of the joint pass below. `/critique essence`: the independent
test of drift, offered at the end of the pass, never run on Claude's
own judgement.

**Course.** Resolve the project and read the intent and the
assignment as it stands; say whether the intent is ready to be
derived from (its Aim, `.claude/skills/forge/states/intent.md`),
never as a gate. The
ways in: no assignment yet, and the joint pass runs whole, in its
three phases below; an assignment that stands and an intent that
moved, and the pass runs on what changed, the provenance map
showing what the change touched; a wording fix, made in the
assignment directly. A substance change asked for in the
assignment goes to the intent first (CLAUDE.md, Working methods).
End by naming what changed; when the Aim's completion is reached,
offer the approval: a recommendation, never a gate.

The joint pass, in three phases and no new kind of interview:

1. Questions up front — one per message, only what is the
   principal's and the intent does not answer: who the recipients
   are, what is delegated and what specified, whether success
   criteria are present, delegated or deliberately absent, what is
   later. None where the intent answers everything. A question on the detail of the
   handover is asked here; a question on substance the intent has
   not settled means the intent is not ready, and the work returns
   to it. Many questions are evidence of that, never its measure.
2. The recast — Claude writes the whole draft from the intent, and
   with it the provenance map: group → items → the positions they
   came from, plus the in-scope positions that landed nowhere (to
   be none) and the items with no position (drift, to be none).
   The map is a tool of the pass, not part of the assignment.
3. The walkthrough by group — one item of the walkthrough is one
   group (`### <Group>`): what it covers, from which positions,
   what in it is DEL or TBC, what is optional or later. A verdict
   per group; a question on a single item opens a sub-item and
   closes it before moving on. Dozens of items pass in a handful
   of messages and nothing is skipped, the provenance visible at
   each. After the pass, `/critique essence` offered as the
   independent test of drift; its findings, an ordinary
   walkthrough.

Why not item by item: most items are craft derived from the intent
and a verdict on each is ceremony. Why not "read the whole":
without the map one sees what is there, not what is missing.

How the files are made: the first draft is created from
`templates/assignment.md`, with its companion
`20-assignment.history.md` from `templates/history.md`. The draft
follows the ID scheme and prime directive 7 of CLAUDE.md as written
there, and the Requirement style below; the Terms section lists only
the prefixes and terms actually used; empty sections and all
template comments are deleted.

**Requirement style.**
- Use **shall** / **shall not**. Do not use would, could, should,
  might, may, or MoSCoW wording.
- **No priority column and no priority tags.** Everything in an
  assignment is essential by default; an exception is marked by a
  note reading *optional* on that item.
- Each item covers one idea, is written once, and is written in
  full, correct sentences.
- Testability is **recommended, not required**: assignments are
  deliberately high-level, and delegating concretisation via a `DEL`
  item is a legitimate outcome.
- Defined terms are capitalised in item text to signal they appear
  in the Terms section.
- An item must not depend on an external link to be understood,
  agreed or later tested.
