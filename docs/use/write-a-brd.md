---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: eb5c6f0e1ac07077
inputs:
  - .claude/skills/forge/states/brd.md
  - templates/brd.md
---

# Write a BRD

This page shows how you break an assignment, an intent or a document someone gave you into business requirements with `/forge brd`. It is for the principal (the person whose thinking is being forged) who wants a BRD that the stakeholders can review, the delivery teams can estimate and the solution design can start from. What a BRD is and why it names what it cannot know is on [The BRD](../about/the-brd.md).

## When to use it

Use it when the project has an assignment, or an intent without one, and the ask must be stated as rules, behaviour and qualities that others can review. Use it also when someone has given you a file (a transcript, an offer, a document) and you want a quick BRD from it.

Claude, the machine that works with you, asks you to name one parent when you ask for the BRD. Every item of the BRD leads back to it.

## The command

```
/forge brd <slug>
```

You name the parent in the same breath:

- The assignment. Claude reads it together with the intent and the threads, because they hold the reasons the assignment does not carry.
- The intent, where the project has no assignment. Claude invents no assignment for it.

The result is `30-brd.md`, the business requirements of the project. Claude says first whether the parent is stable enough to be derived from, approved or by your word. This is information and never a gate.

## What happens

There are five ways in. You pick one by what you have.

### Found together

You have no BRD yet and want to find it with Claude.

1. Claude asks its questions up front, one per message. They cover the stakeholders, the scope of the document and the phasing, which the parent does not answer. You should now see the questions one at a time, each waiting for your answer.
2. Claude returns the whole draft with its provenance map, which shows where each item came from in the parent. You should now see one draft and a map from the parent to the items.
3. Claude walks the draft with you by group, as a walkthrough (one item per message, each closed with the verdict line). The touched areas of the enterprise are walked one per item. You should now see one item at a time with its verdict line.
4. The round ends. Claude names what changed, what stays open and what must come from outside. When the BRD is complete it offers the approval. You should now see those three lists and the offer.

### On your word, drafted automatically

You say the word and Claude works alone. It builds the provenance map first, listing every item of the parent as an ask, a question or an agreement. It then walks the areas of the BRD by itself and writes the items from the map, so that nothing of the parent is lost in silence. Claude asks you nothing.

You should now see, with the draft:

- The provenance map.
- What Claude assumed.
- The list of what must be supplied from outside, in two parts: what the forge already holds, by path, and what must be fetched.

Some details of the draft:

- A step of a use case, or a guarantee, that no place of the parent gives is marked as Claude's reading. The phasing is marked the same way.
- An open question whose owner the parent does not name carries `owner: unassigned`. That is a valid open state. It stays until you name a role.
- Nothing is derived from the draft before you have judged it.

### From a file someone gave you

A transcript, an offer or a document of someone else is not a parent of the chain. Register it first with `/ingest`, as [Register a source](register-a-source.md) describes. Then ask for the BRD and let the automatic way run on it.

The draft is always a work product in `work/` and never `30-brd.md`. Each item cites its place in the file. The reason is that what someone said is never silently promoted to your own position. You should now see the draft as a work product, which you handle as [Work a work product](work-a-work-product.md) describes.

If you want that BRD in the chain, hand an intent over from the same file first. The BRD is then re-parented on that intent.

### A parent that moved

When the assignment or the intent changes after the BRD was written, Claude runs the pass on what changed only. You should now see the changed items and what they touch.

### A wording fix

A small fix of wording is made directly, without a pass.

### Where a draft lands

For the found-together way and the automatic way, you say when you ask where the draft lands. It lands either in the chain as `30-brd.md` or, as a quick look, in `work/`.

## What you have afterwards

- `30-brd.md` with its companion history file, or a draft in `work/`.
- The provenance map of the pass.
- The list of what must be supplied from outside. This is the analyst's work: the supplier's and the systems' documentation, the standards and the regulation that apply, what the operations know. Claude writes none of it from imagination. In its place stand a dependency or an open question with an owner.

The stakeholders' sign-off is your organisation's act. It is recorded outside the forge, or as a decision in `decisions.md` where you want it kept.

## Reviewers offered for it

- `/critique essence`, for drift from the parent.
- `/critique clarity`, for the wording. The rules of the items are on [Requirement style](../reference/requirement-style.md).
- `/challenge business-analyst`, for what was written from the parent though it belongs to the world outside it. See [Challenge the thinking](challenge-the-thinking.md).
- `/check brd`, for the mechanics. See [Check conformance](check-conformance.md).

## If something goes wrong

- Claude finds something missing in the parent. It raises a question and does not fill the gap. A change of substance goes to the intent first.
- A value, a behaviour of a system or a rule of a standard is not in anything Claude has read. It stays an open question or a dependency with an owner, and does not become a figure in the BRD.
- A project with no enterprise around it has no roster of areas. The BRD then says `Roster: none` and walks the areas against nothing.

## A worked example

You have a project `<slug>` with an assignment and want a BRD found together.

```
/forge brd <slug>
```

You say the parent is the assignment. Claude reports that the assignment is approved. It asks who is responsible, who approves and who reviews, then what the document does not cover, then whether the delivery comes in phases. You answer each in turn. Claude returns the draft with its provenance map. You walk it by group and then through the touched areas, one per item. Two open questions have no owner, and you name a role for each. Claude ends by listing what changed, what stays open, and what you must fetch from outside. It offers the approval, and you accept.

## See also

- [The BRD](../about/the-brd.md): what a BRD is, what it holds and why the forge names what it cannot know.
- [Work a work product](work-a-work-product.md): the work product a BRD from someone else's file becomes.
- [Register a source](register-a-source.md): registering the file put in.
- [Challenge the thinking](challenge-the-thinking.md): running the business-analyst persona.
- [Check conformance](check-conformance.md): running the `brd` check.
- [Requirement style](../reference/requirement-style.md): the rule set of a BRD's items.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
