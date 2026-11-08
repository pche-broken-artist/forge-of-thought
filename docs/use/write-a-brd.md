---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 6330c11594ec1a97
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

This page shows how to break an assignment, an intent or a document
someone gave you into business requirements with `/forge brd`. It is
for the principal (the person whose thinking is being forged) who has
a parent to derive from and wants the BRD, the file `30-brd.md`, that
stakeholders can review and delivery teams can estimate. What a BRD
is and why it names what the forge cannot know is on
[The BRD](../about/the-brd.md).

## When to use it

Use it when the parent is stable enough to derive from. Claude says
whether it is: approved, or on your word. It is never a gate.

Use it too when:

- a file someone else gave you (a transcript, an offer, a document)
  has to become business requirements;
- the parent has moved and the BRD must follow;
- one wording in the BRD needs a fix.

## The command

```
/forge brd <slug>
```

When you ask, you name the parent of the BRD:

- the assignment, which Claude reads together with the intent and the
  threads for the reasons the assignment does not carry;
- the intent with its threads, where the project has no assignment.
  No assignment is invented for it.

## What happens

1. Claude resolves the project, the parent you named and the BRD as
   it stands.

   You should now see Claude say whether the parent is stable enough
   to derive from.

2. Claude reads around the parent:
   - the decisions and the ledger (the state of the project, made
     from its documents when it is read);
   - the resource indexes of the project and of every library it
     depends on, so that a standard, a regulation or a report the
     forge already holds is cited and never declared unknown;
   - the roster of areas of the instance.

   The roster is a library document of the instance, cited by path.
   It names the areas of the enterprise a BRD must consider and says
   which of them are mandatory. A project with no enterprise around
   it has no roster: the BRD says `Roster: none` and walks the area
   against nothing. A library is where such a document is kept; see
   [Share material through a library](share-material-through-a-library.md).

   You should now see the BRD, once written, name its roster by path
   or say `Roster: none`.

3. The pass runs by one of the ways in below.

## The ways in

### Found together

Claude asks questions up front, one per message, on the
stakeholders, the scope of the document and the phasing, because the
parent does not answer them. Then it shows the whole draft with its
provenance map, which says where each item came from. Then a
walkthrough runs by group (a walkthrough is the one-item-per-message
decision loop of the forge), and the touched areas of the enterprise
come one per item.

You should now see each group of the draft put to you item by item,
with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject /
(p)ark`.

### Drafted automatically

On your word, Claude asks nothing. It builds the provenance map from
the parent, walks the areas alone and writes the items from the map,
so that nothing of the parent is lost in silence. It returns:

- the draft with the provenance map;
- what it assumed;
- the list of what must be supplied from outside, in two parts: what
  the forge already holds, by path, and what must be fetched.

Open questions the parent gives no owner for are marked
`owner: unassigned` until you name a role. That is a valid open
state. Claude derives nothing from the draft until you have judged
it.

You should now see the three lists after the draft, and the
unassigned questions among them.

### From a file someone else gave you

Register the file first with `/ingest`; see
[Register a source](register-a-source.md). The automatic way then
runs on it. The draft is always a work product in `work/` and never
`30-brd.md`, because what someone said is not silently promoted to
your position. Each item cites its place in the source. How such a
product is worked is on
[Work a work product](work-a-work-product.md).

To have that BRD in the chain, an intent is first handed over from
the same file, and the BRD is then re-parented on it.

You should now see a draft in `work/` and no new `30-brd.md`.

### The parent moved

The pass runs on what changed.

### A wording fix

Claude makes it directly.

## Where the draft lands

For the first two ways, where the draft lands is your word when you
ask:

- in the chain as `30-brd.md`;
- as a quick look in `work/`.

## What you have afterwards

The round ends with Claude naming:

- what changed;
- what stays open;
- what must come from outside.

Claude writes nothing from imagination that the forge cannot know: no
value of a quality the stakeholders have not given, no behaviour of a
system it has not read, no rule of a standard it has not been shown.
In their place stands a dependency or an open question with an owner.
The owner is a role of the roster or of the stakeholders wherever one
fits.

When nothing of the parent is left out in silence, every matter from
outside is named with its owner and no open question that blocks
estimation remains, Claude offers the approval. It is yours. The
stakeholders' sign-off is your organisation's act. It is recorded
outside the forge, or as a decision where you want it kept.

The wording rules of the items are on
[Requirement style and Story style](../reference/requirement-style.md).

## Review it

Claude offers these reviewers. They run only when you ask.

- `/critique essence`, for drift from the parent.
- `/critique clarity`, for the wording.
- `/challenge business-analyst`, for what was written from the
  parent though it belongs to the world outside it; see
  [Challenge the thinking](challenge-the-thinking.md).
- `/check brd`, for the mechanics; see
  [Check conformance](check-conformance.md).

## A worked example

You have a project `<slug>` with an approved assignment and want the
BRD in the chain.

```
/forge brd <slug>
```

You name the assignment as the parent. Claude reads it with the
intent, the decisions and the resource indexes, and says the
assignment is approved. It asks, one per message, who approves, who
reviews and who is informed, what this BRD does not cover, and what
each phase delivers. It then shows the whole draft with the
provenance map. You walk it group by group, and the touched areas
come one per item. Claude closes with what changed, the two open
questions that remain and the list of what must be fetched from the
supplier. You ask for the approval and record the stakeholders'
sign-off in your own system.

Where the BRD stands, the next step may be the stories broken out of
it; see [Write user stories](write-user-stories.md).

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

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
