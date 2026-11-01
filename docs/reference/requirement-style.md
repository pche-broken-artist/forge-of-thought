---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 51da4dd3db5aef7e
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
---

# Requirement style

This page lists the rules for writing the items of an assignment and the stricter rules for the items of a BRD (business requirements document). It is for the principal (the person whose thinking is forged) who judges those items and for the extender who changes the rules.

## The assignment

- Use **shall** / **shall not**.
- Do not use would, could, should, might, may or MoSCoW wording.
- There is no priority column and there are no priority tags.
- Everything in an assignment is essential by default.
- An exception is marked by a note reading *optional* on that item.
- Each item covers one idea.
- Each item is written once.
- Each item is written in full, correct sentences.
- Testability is recommended, not required.
- Assignments are deliberately high-level.
- Delegating concretisation through a `DEL` item is a legitimate outcome.
- Defined terms are capitalised in the item text, to signal that they appear in the Terms section.
- An item must not depend on an external link to be understood, agreed or later tested.

## The BRD

The BRD keeps the rules of the assignment. These are made stricter:

- Testability is mandatory: every BR and NFR can be shown met or not.
- One idea per item, within reason. A list of two to nine members inside an item is allowed where they are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value that no stakeholder gave. A category without a value is a TBC with an owner, never a figure from the skeleton.
- Every BR and UC cites its parent, a REQ item or a POS item. In a work product made from a source, the parent is the path and the place. The place is a turn of the principal's side.
- What a vendor or any other party said is cited only by a DEP or by a note after an item, never by a shall.
- An NFR cites the REQ or POS item it follows from where there is one. Otherwise it cites its category of the template, since the qualities are asked of every ask whether the parent named them or not.
- An item with neither is a finding of the check.
- `shall` / `shall not` is the wording of a BR and an NFR.
- The steps of a UC are written in the active voice, present tense, as a scenario and not as a rule. Example: "the Customer submits the order".
- A type is never told by a number. The prefix says what an item is, the group says where it belongs.

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
