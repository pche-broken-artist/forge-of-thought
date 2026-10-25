---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: ac12402d8abb2913
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

This page shows how you break an assignment, an intent or a document
someone gave you into business requirements with `/forge brd`. It is
for the principal (the person whose thinking is being forged) who
wants requirements that stakeholders can review, delivery teams can
estimate and the solution design can start from.

## When to use it

Use it when a parent document is stable enough to be broken down. Claude
says whether it is, by being approved or by your word, and never
treats that as a gate.

Use it when you hold one of these:

- An assignment. Claude reads it together with the intent and the
  threads, because the assignment does not carry all the reasons.
- An intent, in a project that has no assignment. Claude invents no
  assignment for it.
- A file someone else gave you, such as a transcript, an offer or a
  document. This is a third way in and not a parent of the chain.

What a BRD is and why it names what it cannot know is on
[The BRD](../about/the-brd.md).

## The command

```
/forge brd <slug>
```

The command iterates `30-brd.md`, the business requirements of the
project. When you ask for it, you name its parent: the assignment, or
the intent where the project has no assignment. Every item of the BRD
leads back to that parent.

## What happens

There are five ways in. Claude first resolves the project, the parent
you name and the BRD as it stands. Then you take the way that fits.

1. **No BRD yet, found together.** Claude asks questions up front,
   one per message. They are about the stakeholders, the scope of the
   document and the phasing, because the parent does not answer
   them. Then it shows the whole draft with its provenance map,
   which is the list that traces every item to its place in the
   parent. Last comes a walkthrough by group, in which you decide one
   item per message. The touched areas of the enterprise are walked
   one per item.

   You should now see the draft, the provenance map and a first item
   waiting for your verdict.

2. **No BRD yet, drafted automatically on your word.** Claude asks
   you nothing. It builds the provenance map from the parent first,
   walks the areas the BRD must consider, and writes the items from
   the map, so that nothing of the parent is lost in silence. What
   the parent does not answer stays an open question or an
   assumption. A step or a guarantee that no place of the parent
   gives is marked as Claude's reading. An open question whose owner
   the parent does not name carries `owner: unassigned` until you
   name a role.

   You should now see the draft, the provenance map, the list of what
   Claude assumed and the list of what must be supplied from outside.
   That last list has two parts: what the forge already holds, named
   by path, and what must be fetched.

3. **A file someone else gave you.** Register it first with `/ingest`
   (see [Register a source](register-a-source.md)). The automatic way
   then runs on it. The draft is always a work product in `work/`
   and never `30-brd.md`, because what someone said is never
   promoted to your position unasked. Each item cites its place in
   the source. A work product is a file made with work of its own
   (see [Work a work product](work-a-work-product.md)). To have the
   BRD in the chain, hand over an intent from the same file first.
   The BRD is then re-parented on that intent.

   You should now see a draft in `work/` whose items cite the file.

4. **A parent that moved.** The pass runs on what changed.

   You should now see the changed items and their parents.

5. **A wording fix.** Claude makes it directly.

   You should now see the corrected wording.

For the first two ways, you say when you ask where the draft lands:
in the chain as `30-brd.md`, or as a quick look in `work/`.

The round ends with Claude naming what changed, what stays open and
what must come from outside. When the BRD is complete, it offers the
approval. Complete means that nothing of the parent is left out in
silence and that every matter from outside has an owner. It also
means that no open question that blocks estimation remains. A matter
that is delegated, phased later or open with an owner counts as
complete. A silent one does not.

## What you have afterwards

- `30-brd.md`, or a draft in `work/`, written once at the end of the
  round, with its history companion.
- The provenance map, which shows where each item came from.
- The list of what must be supplied from outside, as your work as the
  analyst. Claude writes nothing of that from imagination: no value of
  a quality the stakeholders have not given, no behaviour of a system
  it has not read, no rule of a standard it has not been shown. A
  dependency or an open question with an owner stands in its place.
- The wording of the items follows [Requirement style](../reference/requirement-style.md).

The stakeholders' sign-off is your organisation's act. It is recorded
outside the forge, or as a decision where you want it kept.

## Reviewers offered for it

Each runs as an isolated subagent (a helper that does not see your
conversation), only on your command.

- `/critique essence` finds drift from the parent.
- `/critique clarity` checks the wording against the requirement style.
- `/challenge business-analyst` finds what was written from the
  parent though it belongs to the world outside it (see
  [Challenge the thinking](challenge-the-thinking.md)).
- `/check brd <slug>` checks the mechanics (see
  [Check conformance](check-conformance.md)).

## If something goes wrong

- The parent is not yet stable. Claude says so and goes on; you
  decide whether to wait.
- The parent leaves a matter unanswered. Claude raises it as a
  question, or in the automatic way leaves it open with an owner. It
  does not fill the gap. A change of substance goes to the intent
  first.
- An automatic draft is not yet judged. Nothing is derived from it
  until you have judged it.
- An open question blocks estimation. The BRD is not complete until
  it is answered or delegated.
- A term is unfamiliar. See the [Glossary](../reference/glossary.md).

## A worked example

You have an approved assignment in a project `<slug>` and want a draft
quickly.

```
/forge brd <slug>
```

You name the assignment as the parent and say: draft it automatically
into the chain. Claude builds the provenance map from every item of the
assignment, walks the areas alone, and returns the draft with the map,
its assumptions and the two-part list of what must be supplied from
outside. One open question names no owner, so it carries
`owner: unassigned`. You reply with the role, judge the draft, and ask
for `/critique essence`. The round closes with what changed, what stays
open and the offer of approval.

## See also

- [The BRD](../about/the-brd.md): what a BRD is, what it holds and why the forge names what it cannot know.
- [Work a work product](work-a-work-product.md): the work product a BRD from someone else's file becomes.
- [Register a source](register-a-source.md): registering the file put in.
- [Challenge the thinking](challenge-the-thinking.md): running the business-analyst persona.
- [Check conformance](check-conformance.md): running the `brd` check.
- [Requirement style](../reference/requirement-style.md): the rule set of a BRD's items.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
