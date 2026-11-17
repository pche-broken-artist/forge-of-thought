---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: b28b78188e932135
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

This page shows how you break an assignment, an intent or a document
someone gave you into business requirements with `/forge brd`. It is
for the user who wants a BRD (business requirements document) that
stakeholders can review and delivery teams can estimate. What a BRD is
and why it names what the forge cannot know is explained in
[The BRD](../about/the-brd.md). Terms of the forge are in the
[Glossary](../reference/glossary.md).

## When to use it

- You have an assignment, or an intent in a project without an
  assignment, and want it recast as business requirements.
- You were given a file by someone else (a transcript, an offer, a
  document) and want a draft BRD from it.
- A BRD exists and its parent has moved, or a wording needs a fix.

## The command

```
/forge brd <slug>
```

`/forge brd [slug]` iterates `30-brd.md`, the business requirements of
the project `<slug>`. When you ask for it, you name its parent:

- the assignment, which Claude reads together with the intent and the
  threads for the reasons the assignment does not carry;
- the intent, where the project has no assignment. No assignment is
  invented for it.

Around the parent Claude reads the decisions, the ledger (the state
of the project, made at read time from its documents) and the resource
indexes of the project and of every library it depends on. It reads the
indexes so that a standard or a report the forge already holds is
cited and never declared unknown.

It also reads the instance's roster of areas. That is a library
document of the instance, cited by path. It names the areas of the
enterprise a BRD must consider and says which of them are mandatory. A
project with no enterprise around it has no roster. Its BRD then says
`Roster: none` and walks the areas against nothing. How a library is
shared is in [Share material through a
library](share-material-through-a-library.md).

## What happens

Claude first says whether the parent is stable enough to be derived
from, that is approved or the principal's word. The principal is the
person whose thinking is being forged, and that is you. The statement
is information and never a gate. Then the way in you choose decides
what you see.

1. **Found together.** Claude asks its questions up front, one per
   message, on the stakeholders, the scope of the document and the
   phasing, because the parent does not answer them.
   You should now see the questions one at a time, each waiting for
   your answer.
2. Claude writes the whole draft with its provenance map, which lists
   what each item of the parent became.
   You should now see the draft and the map together.
3. Claude walks the draft as a walkthrough (one item per message, each
   closed with the verdict line) by group, and raises the touched
   areas of the enterprise one per item.
   You should now see each area either found in items or put forward
   as not applicable.

The other ways in:

- **Automatically, on your word.** Claude asks nothing. It builds the
  provenance map, walks the areas alone and writes the items from the
  map. What the parent does not answer stays a TBC (an open question)
  or an ASM (an assumption). A step or a guarantee that no place of
  the parent gives is marked as Claude's reading.
  You should now see the draft with the provenance map, what Claude
  assumed, and the list of what must be supplied from outside.
- **A file someone else gave you.** Register it first with `/ingest`,
  as described in [Register a source](register-a-source.md). The
  automatic way then runs on it, and each item cites its place in the
  file. The draft is always a work product in `work/` and never
  `30-brd.md`, because what someone said is never silently promoted to
  your position. How such a product is worked is in [Work a work
  product](work-a-work-product.md). To have the BRD in the chain, an
  intent is first handed over from the same file, and the BRD is then
  re-parented on it.
  You should now see a draft in `work/` that cites the file.
- **A parent that moved.** The pass runs on what changed.
- **A wording fix.** It is made directly.

Where a draft of the first two ways lands is your word when you ask:
in the chain as `30-brd.md`, or in `work/` as a quick look.

The list of what must be supplied from outside has two parts: what the
forge already holds, by path, and what must be fetched. Much of a BRD
is not in the parent at all. It lies in the documentation of the
supplier and of the systems touched, in the standards and the
regulation that apply, and in what operations know. Claude writes none
of it from imagination. A dependency or an open question with an owner
stands in its place. An open question with no known owner is marked
`owner: unassigned` until you name a role.

The round ends when Claude names what changed, what stays open and what
must come from outside.
You should now see an offer of the approval. The approval is yours. The
stakeholders' sign-off is your organisation's act. It is recorded
outside the forge, or as a decision where you want it kept.

## What you have afterwards

- `30-brd.md` with its history companion, or a draft in `work/`.
- The provenance map, the list of what Claude assumed and the list of
  what must be supplied from outside.
- Open questions that each carry an owner and say whether they block
  estimation.

The rules for the wording of every item are in [Requirement style and
Story style](../reference/requirement-style.md). The reviewers offered
for a BRD are:

- `/critique essence` for drift from the parent
- `/critique clarity` for the wording
- `/challenge business-analyst`, described in [Challenge the
  thinking](challenge-the-thinking.md)
- `/check brd`, described in [Check conformance](check-conformance.md)

## If something goes wrong

- The parent is not approved. Claude says so and goes on, because the
  statement is never a gate.
- The parent lacks an answer the BRD needs. Claude raises it as a
  question, or leaves a TBC or an ASM in the automatic way. It does
  not invent a requirement.
- A change of substance is found missing in the parent. It goes to the
  intent first, and the BRD follows.
- A matter must come from outside the forge. It stands as a dependency
  or an open question with an owner and appears in the list to be
  supplied from outside.

## A worked example

You have a project `<slug>` with an approved assignment and no BRD.

```
/forge brd <slug>
```

You name the assignment as the parent. Claude says the parent is
approved, then asks one message at a time who approves and reviews,
what the document does not cover, and what each phase delivers. You
answer. Claude returns the draft with its provenance map. You walk the
groups and the touched areas, one item per message. The round ends with
a list: two open questions with owners, one of them blocking
estimation, and one matter to fetch from outside. Claude offers the
approval. Next, you can break the BRD into stories, as described in
[Write user stories](write-user-stories.md).

## See also

- [The BRD](../about/the-brd.md): what a BRD is, what it holds and why the forge names what it cannot know.
- [Work a work product](work-a-work-product.md): the work product a BRD from someone else's file becomes.
- [Register a source](register-a-source.md): registering the file put in.
- [Share material through a library](share-material-through-a-library.md): the library a roster of areas is kept in and cited from.
- [Write user stories](write-user-stories.md): the stories that may be broken out of a BRD next.
- [Challenge the thinking](challenge-the-thinking.md): running the business-analyst persona.
- [Check conformance](check-conformance.md): running the `brd` check.
- [Requirement style and Story style](../reference/requirement-style.md): the rule set of a BRD's items.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
