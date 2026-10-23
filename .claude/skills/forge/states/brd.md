---
description: 'Iterate 30-brd.md — the business requirements: the assignment, the intent or a source put in, broken into rules, behaviour and qualities the stakeholders can review and the delivery can estimate'
---

The definition of the BRD's elicitation, in the seven blocks of
POS.1310 of the forge intent; what it is to achieve and why is the
brief `00-brief-brd.md` 0.3 of the forge project until its position
in the intent is written after the first trials (POS.1780). Shared
mechanism is cited and never repeated here: the form of the
conversation and one write per round (CLAUDE.md, Working methods
and prime directive 9), versioning with history (CLAUDE.md,
Versioning & status), the language (CLAUDE.md, prime directive 6).

**Target.** `30-brd.md`. Shape of the result: `templates/brd.md`.

**Inputs.** One parent, named by the principal when he asks for
the BRD, and the trail of each item leads to it:
- `20-assignment.md`, read with `10-intent.md` and `threads/` for
  the reasons the assignment does not carry; the parent of an item
  is a REQ;
- `10-intent.md` with `threads/`, where the project has no
  assignment; the parent is a POS; no assignment is invented for
  it.
A file the principal puts in — a transcript, an offer, a document
of someone else — is a third way in, not a parent of the chain:
registered through `/ingest` and cited by path, it yields a draft
BRD that is always a work product in `work/`
(`.claude/skills/work/SKILL.md`), never `30-brd.md`, since what
someone said is never silently promoted to the principal's position
(CLAUDE.md, Document chain, External inputs); each item cites its
place in the source. Where the principal wants that BRD in the
chain, an intent is handed over from the same source first
(THR.0670) and the BRD is re-parented on it.
Around the parent: `decisions.md`, the ledger, the DEL items of an
assignment as the list of what the BRD is asked to bring back;
the roster of the instance — the areas of the enterprise a BRD must
consider and which of them are mandatory — a library document
cited by path (POS.1020), for now the fork's template in
`projects/lib-allwyn/sources/fork-brd/template-brd.md`; a project
with no enterprise around it has no roster, says `Roster: none`
and walks the area against nothing; the group's standard in the
same bundle; sources and research as the principal directs.

**Aim.** The BRD breaks the parent into rules, behaviour and
qualities that the stakeholders can review on their own, the
delivery teams can estimate and the solution design can start
from: every in-scope requirement of the parent carried by business
requirements and, where behaviour must be agreed as a sequence, by
use cases; every item one sentence, testable and traced to its
parent; the touched areas of the enterprise each found or
knowingly found not to apply; the boundaries — out of scope,
dependencies, assumptions — and the scope of the document
explicit; the qualities named by category with a value from the
stakeholders or open as a TBC; the phasing stated, even as "all in
the first version" (POS.1360); every term defined. It admits the
solution at the level the stakeholders need to agree the ask and
leaves the how to the solution design; where to stop is a
judgement, made when the teams can estimate, when more detail would
not interest the stakeholders or would be superseded by design. It
is complete when nothing of the parent is left out in silence —
delegated, phased later or open with an owner is complete, silent
is not — when every matter that must come from outside the forge
is named with its owner, and when no TBC that blocks estimation is
open.

**Partner.** The analyst's recast is Claude's: the whole from the
parent with the provenance map, the groupings proposed so that
every stakeholder finds theirs and nothing is twice, the use cases
drawn from the parent's process view, the touched areas raised one
by one, the wording in the Requirement style below. The principal —
the analyst working as principal — decides the scope of the
document, the groupings, which areas apply, the owner of every TBC
and every value.

What Claude does not do, because the forge cannot: much of a BRD
is not in the intent or the assignment at all. It is in the
documentation of the supplier and of the systems touched, in the
standards and the regulation that apply, in what the operations
know — and the analyst brings it from outside. Claude writes
nothing of that from imagination: no value of a quality the
stakeholders have not given, no behaviour of a system he has not
read, no rule of a standard he has not been shown. In their place
stands a DEP or a TBC with an owner, and the pass ends with the
list of what must be supplied from outside, said plainly as the
analyst's work. He copies nothing of the parent, invents no
requirement the parent does not carry, and what he finds missing
in the parent he raises as a question; a change of substance goes
to the intent first (CLAUDE.md, Working methods).

**Map.** What the BRD finds; where it lands is the template's.
Walked before the recast, to see what the parent does not answer,
and at the end; an area may stay empty when it was considered and
found not to apply, said with the reason where the roster of the
instance makes the area mandatory.
- the stakeholders: who approves, who reviews, who is consulted or
  informed, as roles;
- the scope of work and the scope of the document: what is done
  and not done, and what this BRD does not cover that a reader
  would expect, with where it is covered;
- the cut of the parent: what is carried now, what is phased later
  and in which version, what is delegated onward;
- the process view: the behaviour that must be agreed as a
  sequence, with its actors, conditions and exceptions;
- the rules: the business requirements, grouped so that every
  stakeholder finds theirs and nothing is twice;
- the touched areas of the enterprise: the roster of the instance,
  each found or found not to apply, the mandatory ones never
  silent;
- the systems and dependencies: what is impacted, what the BRD
  relies on outside itself;
- the qualities: the non-functional categories of the template,
  each with a value from the stakeholders or open;
- the things the business talks about: the entities, the states
  each may be in and what moves it between them, and the system
  each is taken from, as the business names them; how it is taken
  is the solution design's, and no attribute is listed here;
- what comes from outside: what the BRD needs that neither the
  parent nor the forge holds — the supplier's and the systems'
  documentation, the standards and the regulation that apply, the
  operations' knowledge — each named as a DEP or a TBC with its
  owner, never written from imagination;
- the transition: data to migrate, people to train, the cut-over,
  where the change replaces something;
- the phasing: what each version delivers, in what order, with
  what dependencies;
- the assumptions: what the requirements rest on and would change
  if it stopped holding;
- success: how the stakeholders will know the ask was met;
- the terms: every capitalised term defined, nothing generic;
- what stays open: every TBC with an owner, which of them block
  estimation, and the list of what must be supplied from outside.

**Instruments.** The provenance map of the recast, as the
assignment's definition has it
(`.claude/skills/forge/states/assignment.md`, the joint pass);
`/critique essence` for drift from the parent; `/critique clarity`
with the Requirement style below; `/challenge business-analyst`
for what was written from the parent though it belongs to the
world outside it; `/check brd` for the mechanics; `/ingest` for a
file put in and for the roster and the standard of the instance
into the library; `/work` for the draft a file put in yields; `/recipe` for the page the instance
publishes, a render and never the artefact.

**Course.** Resolve the project, the parent the principal names
and the BRD as it stands; say whether the parent is stable enough
to be derived from — approved, or the principal's word — never as
a gate. The ways in:
- no BRD yet, found together: the joint pass of the assignment's
  definition, adapted — questions up front on the stakeholders,
  the scope of the document and the phasing, which the parent does
  not answer; the recast with the provenance map; the walkthrough
  by group, the touched areas walked one per item;
- no BRD yet, on the principal's word automatically (draft early,
  CLAUDE.md, Working methods, Handing over): Claude walks the Map
  alone, writes what the parent answers, leaves what it does not as
  a TBC or as an ASM, asks nothing, and returns the draft with the
  provenance map, the list of what he assumed and the list of what
  must be supplied from outside; a TBC whose owner the parent does
  not name carries `owner: unassigned`, a valid open state and not
  a residue of the skeleton, until the principal names the role;
  nothing is derived from the draft before the principal has judged
  it;
- a file put in, and the automatic way runs on it into `work/`
  (Inputs);
- a parent that moved, and the pass runs on what changed;
- a wording fix, made directly.
Where the result of the first two ways lands is the principal's
word when he asks: in the chain as `30-brd.md`, or as a work
product in `work/` where it is a quick look. End by
naming what changed, what stays open and what must come from
outside; when the Aim's completion is reached, offer the approval
— the principal's, as the house scheme has it — and say that the
stakeholders' sign-off is the instance's act, recorded where the
instance records it, in `decisions.md` where the principal wants
it kept.

How the files are made: the first BRD is created from
`templates/brd.md` as v0.1, with its companion `30-brd.history.md`
from `templates/history.md`; the ledger reads the header
(CLAUDE.md, Ledger). BR, UC, DEP, NFR, OOS, ASM, TBC and SCR items
follow the ID scheme of CLAUDE.md; BR, UC, DEP and NFR are the
BRD's own. A write rewrites for coherence, never appends; empty
sections and all template comments are deleted.

**Requirement style.** The assignment's
(`.claude/skills/forge/states/assignment.md`, Requirement style),
with these made stricter for the BRD:
- testability is mandatory: every BR and NFR can be shown met or
  not;
- one idea per item, within reason: a list of two to nine members
  inside an item is allowed where they are one rule;
- a note after an item is allowed and carries no requirement;
- an item may name the role that owns it;
- no value that no stakeholder gave: a category without a value is
  a TBC with an owner, never a figure from the skeleton;
- every BR and UC cites its parent (`REQ.NNNN` or `POS.NNNN`; in a
  work product from a source, the path and the place); an NFR
  cites the REQ or POS it follows from where there is one, and
  otherwise its category of the template, since the qualities are
  asked of every ask whether the parent named them or not; an item
  with neither is a finding of the check;
- `shall` / `shall not` is the wording of a BR and an NFR; the
  steps of a UC are written in the active voice, present tense
  ("the Player submits the bet"), as a scenario and not as a rule;
- a type is never told by a number: the prefix says what an item
  is, the group says where it belongs.
