---
description: Iterate 35-user-stories.md — the requirements broken into stories of behaviour that the stakeholders approve as a whole, the delivery builds from and the testers test from
---

The definition of the user stories' elicitation, in the seven blocks
of POS.1310 of the forge intent; what it is to achieve and why is
POS.1910 to POS.1940. Shared mechanism is cited
and never repeated here: the form of the conversation and one write
per round (CLAUDE.md, Working methods and prime directive 9),
versioning with history (CLAUDE.md, Versioning & status), the
language (CLAUDE.md, prime directive 6).

**Target.** `35-user-stories.md`. Shape of the result:
`templates/user-stories.md`.

**Inputs.** One parent, named by the principal when he asks for the
stories, and the trail of each story leads to it:
- `30-brd.md`, read with the layers above it for the reasons it does
  not carry; a story cites the BR, NFR, UC or DEP it serves;
- `10-intent.md` with `threads/`, where the change is small, the ask
  precise and without further impact, and the principal says so; a
  story cites the POS it serves. Whether the ask suffices is the
  principal's word, never Claude's; Claude may say why he thinks it
  does not.
A requirements document of someone else, put in through `/ingest`
and cited by path, yields stories that are a work product in `work/`
(`.claude/skills/work/SKILL.md`), never `35-user-stories.md`, each
story citing its place in the source.
Around the parent: `decisions.md`, the ledger, the indexes of the
project's resources, sources and research as the principal directs.

**Aim.** The stories break the parent into behaviour seen from the
outside — what the user or the business sees happen and under which
conditions it is accepted — so that the stakeholders can approve
them as a whole, the delivery can make its technical analysis and
build from them without an empty place, and the testers can write
their test cases from them. Every in-scope item of the parent is
served by at least one story or said not to be, with the reason;
one item may be served by several stories and one story may serve
several items. Every acceptance criterion can be tested; no two
stories contradict each other or describe one function twice; every
open question has an owner. The stories are complete when that
holds and no question that blocks the delivery is open; the
stakeholders' approval of the whole is the instance's act.

**Partner.** The recast is Claude's: the whole list of stories drawn
from the parent with the reference of each, the groupings proposed,
the edge cases each behaviour invites, the wording in the Story
style below. The principal decides which stories stand, their cut,
the groupings, every value and the owner of every question.
What Claude does not do: he writes no behaviour the parent does not
carry, no value nobody gave, no technical solution — no component,
API, data model or detail of the design —, no priority and no
estimate. What is missing in the parent stands as a question with
an owner, never as an assumption; a change of substance goes to the
parent first (CLAUDE.md, Working methods, Intent-first).

**Map.** What the stories find; where it lands is the template's.
Walked before the recast, to see what the parent does not answer,
and at the end; an area may stay empty when it was considered and
found not to apply.
- the coverage: every in-scope item of the parent and the stories
  that serve it, or the reason none does;
- the behaviour: for each story who or what wants it, what happens
  and why, and the conditions under which it is accepted;
- the edge cases: the situations at the border of each behaviour
  and what happens in them;
- the qualities: the non-functional items that cut across the whole
  as stories of their own, those that concern one function as
  acceptance criteria of its story;
- the dependencies: what a story needs from outside itself, cited
  as a DEP of the parent, or in a small change asked as a question;
- the risks: where a story carries one, its mitigation or its
  consequences;
- the references outward: an attachment or a technical analysis a
  story points to, with what lies behind the link;
- the contradictions: two stories, or a story and its parent, that
  do not agree;
- what stays open: every question with its owner, and which of them
  block the delivery.

**Instruments.** `/check user-stories` for the mechanics;
`/critique clarity` with the Story style below; `/critique essence`
for drift from the parent; `/ingest` for a requirements document put
in; `/work` for the stories it yields; `/render` with the project's
recipe for the export the instance hands over, a render and never
the artefact, which leaves out every reference to a POS, since the
stakeholders never see the intent, and the Reference line of a story
that has no other.

**Course.** Resolve the project, the parent the principal names and
the stories as they stand; say whether the parent is stable enough
to be derived from — approved, or the principal's word — never as a
gate. The ways in:
- no stories yet (the default way, handing over): Claude walks the
  Map alone and returns first the cut — the name of every story with
  a short description of what it covers, in words, and the items of
  the parent no story serves, named by what they say — for the
  principal's word; only on the cut agreed he drafts the whole
  stories, asks nothing, and returns the draft; it is then walked
  story by story (`.claude/skills/walkthrough/SKILL.md`); nothing is
  derived from the draft before the principal has judged it;
- a story whose parent does not suffice: the walk switches to an
  interview on that story, one question at a time;
- a requirements document put in, and the default way runs on it
  into `work/` (Inputs);
- a parent that moved, and the pass runs on what changed;
- a wording fix, made directly.
End by naming what changed and what stays open; when the Aim's
completion is reached, offer the approval — the principal's, as the
house scheme has it — and say that the stakeholders' approval of the
whole is the instance's act, recorded in `decisions.md` where the
principal wants it kept.

How the files are made: the first stories are created from
`templates/user-stories.md` as v0.1, with their companion
`35-user-stories.history.md` from `templates/history.md`; the
ledger reads the header (CLAUDE.md, Ledger). US items follow the ID
scheme of CLAUDE.md and are the layer's own. A write rewrites for
coherence, never appends; empty sections and all template comments
are deleted. A story's past lives in the history, never in the
story.

**Story style.**
- A story is one function as the one who uses it meets it: one
  actor doing or seeing one thing. The rules of that function — its
  variants by condition (a visitor not logged in, a datum missing or
  deleted, the state after the release), its qualities and its
  transitions — are its acceptance criteria and edge cases, never
  stories of their own. A new story begins where another actor does
  something else, or the same actor reaches a different function.
- What happens in the usual course is an acceptance criterion; an
  edge case is a situation at the border of the behaviour — a
  failure, a missing datum, a change during use.
- The sentence of a story is free and carries who or what wants it,
  what happens and why ("…, so that…"); the form "As a… I want… so
  that…" is neither required nor forbidden.
- An acceptance criterion is in the indicative, present tense, one
  behaviour per bullet ("The carousel shows at most 5 slides.").
- No vague word — a word that names a quality without a value, in
  whatever language the project writes ("fast", "suitable",
  "intuitive", "unacceptable"): a value, or a question with an owner
  where nobody gave one.
- An edge case is "situation → what happens".
- A risk is "risk → mitigation" or "risk → consequences", never
  alone.
- A note is a link to an attachment or a technical analysis with
  what lies behind it, nothing else.
- The labels `Edge cases`, `Risks`, `Note`, `Questions` and
  `Reference` are fixed and in English; the content is in the
  project's language.
- `Reference` is the one part every story has: the BR, NFR, UC or DEP
  it serves, or in a small change without a BRD the POS; the other
  parts are left out where a story has nothing for them, never left
  empty.
- No technical solution, no priority, no estimate.
