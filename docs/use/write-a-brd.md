---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: cb58a6720449cf82
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

`/forge brd` is the command that iterates the business requirements,
the file `30-brd.md`. This page is for the analyst, who is also the
principal (the person whose thinking is being forged), and who wants
to break an assignment, an intent or a document someone gave them into
business requirements. What a BRD is and why it names what it cannot
know is in [The BRD](../about/the-brd.md).

## When to use it

Use it when a parent exists that the stakeholders and the delivery
teams need broken into rules, behaviour and qualities they can review
and estimate. The parent is one of three:

- The assignment. Claude reads it together with the intent and the
  threads, for the reasons the assignment does not carry.
- The intent, where the project has no assignment. No assignment is
  invented for it.
- A file someone else gave you, such as a transcript, an offer or a
  document. This is a third way in and not a parent of the chain.

## The command

```
/forge brd <slug>
```

When you ask, you name the parent in your words, for example "from the
assignment" or "from the intent". Claude says whether the parent is
stable enough to derive from, approved or on your word. It is never a
gate.

## What happens

Claude resolves the project, the parent you named and the BRD as it
stands. Around the parent it reads these:

- The decisions of the project and its ledger (the state report made
  from the documents at read time).
- The resource indexes of the project and of every library it depends
  on, so that a standard, a regulation or a report already held is
  cited and never declared unknown.
- The roster of areas of the instance. This is a library document of
  the instance, cited by path, that names the areas of the enterprise a
  BRD must consider and which of them are mandatory. A project with no
  enterprise around it has no roster. It writes `Roster: none` and
  walks the areas against nothing. How a library is kept and cited is
  in [Share material through a library](share-material-through-a-library.md).

Then the pass runs in one of five ways. Pick the one that fits.

### Found together

1. Claude asks questions up front, one per message, on the
   stakeholders, the scope of the document and the phasing. The parent
   does not answer these.

   You should now see the questions closed one by one, with your
   answers reflected back.

2. Claude writes the whole draft with its provenance map. The map lists
   every item of the parent and shows where each is carried, so that
   nothing is lost in silence.

   You should now see one draft and, beside it, the map.

3. Claude runs a walkthrough by group. A walkthrough is the method that
   takes one item per message and closes each with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The touched
   areas of the enterprise are walked one per item.

   You should now see each group settled by your verdicts, which are
   written once at the end of the round.

### Automatically, on your word

Claude asks nothing. It builds the provenance map, walks the areas
alone and writes the items from the map. What the parent does not
answer it leaves as an open question or an assumption. It returns:

- the draft with the provenance map
- the list of what it assumed
- the list of what must be supplied from outside, in two parts: what
  the forge already holds, by path, and what must be fetched

A step of a use case or a guarantee that no place of the parent gives
is marked as Claude's reading, and so is the phasing. An open question
whose owner the parent does not name carries `owner: unassigned`. That
is a valid open state until you name a role. Nothing is derived from
the draft before you have judged it.

You should now see the three lists after the draft.

### From a file someone gave you

1. Register the file first. How is in
   [Register a source](register-a-source.md).
2. Ask for the BRD from it. The automatic way runs on the file. Each
   item cites its place in the file, and that place is a turn of the
   principal's side. What another party said is cited only by a
   dependency or by a note after an item.

   You should now see a draft in `work/`. It is never `30-brd.md`,
   because what someone said is not silently promoted to your position.
   How a work product is worked is in
   [Work a work product](work-a-work-product.md).

3. To have the BRD in the chain, hand over an intent from the same file
   first. The BRD is then re-parented on that intent.

### A parent that moved

The pass runs again on what changed in the parent.

### A wording fix

It is made directly, with no pass.

### Where a draft lands

For the found-together and the automatic ways, you say when you ask
where the draft lands. It lands in the chain as `30-brd.md`, or as a
quick look in `work/`.

## What you have afterwards

The first BRD is created from the template as a draft, version 0.1,
with its history companion `30-brd.history.md` beside it. Each write
rewrites the file for coherence and never appends. Empty sections and
all template comments are removed.

Each round ends with Claude naming what changed, what stays open and
what must come from outside. When the BRD is complete, it offers the
approval, which is yours. A BRD is complete when nothing of the parent
is left out in silence and when every matter that must come from
outside is named with its owner. It is also complete when no open
question that blocks estimation remains. A requirement delegated,
phased later or open with an owner counts as carried.

The stakeholders' sign-off is your organisation's act. It is recorded
outside the forge, or as a decision where you want it kept.

## What Claude does not write

Much of a BRD is not in the intent or the assignment. It is in the
supplier's and the systems' documentation, in the standards and the
regulation that apply, and in what operations know. Claude writes none
of it from imagination:

- no value of a quality that the stakeholders have not given
- no behaviour of a system it has not read
- no rule of a standard it has not been shown

In their place stands a dependency or an open question with an owner.
The owner is a role of the roster or of the stakeholders wherever one
fits, and `unassigned` only where none does. An assumption never
settles an open question. The wording of the items follows
[Requirement style](../reference/requirement-style.md).

## If something goes wrong

- If the parent does not answer something, Claude raises it as a
  question or leaves it as an open question with an owner. It never
  invents a requirement the parent does not carry.
- If a change of substance is needed, it goes to the intent first and
  the BRD follows.
- If a standard, a regulation or a report seems unknown, check the
  resource indexes first. The forge may already hold it.

## Reviewers you can run

- `/critique essence`, for drift from the parent.
- `/critique clarity`, for the wording against the Requirement style.
- `/challenge business-analyst`, for what was written from the parent
  though it belongs to the world outside it. How is in
  [Challenge the thinking](challenge-the-thinking.md).
- `/check brd`, for the mechanics. How is in
  [Check conformance](check-conformance.md).

## A worked example

You have a project `<slug>` with an approved assignment and no BRD.

1. You type `/forge brd <slug>` and say the parent is the assignment.
2. Claude reads the assignment, the intent, the threads, the decisions
   and the resource indexes. The project has no enterprise around it, so
   it writes `Roster: none`.
3. Claude asks who approves and who reviews, what the document leaves
   out and what the phases are. You answer one question at a time.
4. Claude returns the whole draft with its provenance map. You should
   now see every item of the assignment carried or marked open.
5. You walk the groups and give your verdicts. At the end you say
   `write`, and `30-brd.md` appears as version 0.1.
6. Claude names what changed, what stays open and what must come from
   outside, then offers the approval. You run `/check brd <slug>`.

## See also

- [The BRD](../about/the-brd.md): what a BRD is, what it holds and why the forge names what it cannot know.
- [Work a work product](work-a-work-product.md): the work product a BRD from someone else's file becomes.
- [Register a source](register-a-source.md): registering the file put in.
- [Share material through a library](share-material-through-a-library.md): the library a roster of areas is kept in and cited from.
- [Challenge the thinking](challenge-the-thinking.md): running the business-analyst persona.
- [Check conformance](check-conformance.md): running the `brd` check.
- [Requirement style](../reference/requirement-style.md): the rule set of a BRD's items.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
