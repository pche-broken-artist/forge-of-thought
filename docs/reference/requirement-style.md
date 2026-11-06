---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 7f98ff37b5804d0c
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
---

# Requirement style

The requirement style is the rule set for writing the items of an assignment, and the stricter rule set for the items of a BRD. This page lists both exactly, for the reader who writes or checks such items. The terms used here are in the [Glossary](glossary.md).

## The assignment's style

- Use **shall** / **shall not**. Do not use would, could, should, might, may, or MoSCoW wording.
- No priority column and no priority tags. Everything in an assignment is essential by default. An exception is marked by a note reading *optional* on that item.
- Each item covers one idea, is written once, and is written in full, correct sentences.
- Testability is recommended, not required. Assignments are deliberately high-level, and delegating concretisation through a `DEL` item is a legitimate outcome.
- Defined terms are capitalised in item text to signal that they appear in the Terms section.
- An item must not depend on an external link to be understood, agreed or later tested.

Why the items of an assignment are written so: [The assignment](../about/the-assignment.md).

## The BRD's style

The BRD takes the assignment's style, with these rules made stricter.

- Testability is mandatory: every BR and NFR can be shown met or not.
- One idea per item, within reason. A list of two to nine members inside an item is allowed where they are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value that no stakeholder gave. A category without a value is a TBC with an owner, never a figure from the skeleton.
- Every BR and UC cites its parent, which is the ID of a requirement or of a position. In a work product made from a source, the parent is the path and the place, and the place is a turn of the principal's side. What a vendor or any other party said is cited only by a DEP or by a note after an item, never by a shall.
- An NFR cites the requirement or position it follows from where there is one. Otherwise it cites its category of the template, since the qualities are asked of every ask whether the parent named them or not.
- An item with neither a parent nor a category is a finding of the check.
- `shall` / `shall not` is the wording of a BR and an NFR.
- The steps of a UC are written in the active voice, present tense ("the Customer submits the order"), as a scenario and not as a rule.
- A type is never told by a number. The prefix says what an item is, and the group says where it belongs.

Why the items of a BRD are written so: [The BRD](../about/the-brd.md).

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
