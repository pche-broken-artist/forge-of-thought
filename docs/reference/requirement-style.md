---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 208733d01cefc721
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
---

# Requirement style

This page states the rules for writing the items of an assignment, and the stricter rules for the items of a BRD (business requirements document). It is for the principal (the person whose thinking is forged) and for anyone who extends the forge. Terms of the forge are in the [Glossary](glossary.md).

## The items of an assignment

- Use **shall** and **shall not**.
- Do not use would, could, should, might, may or MoSCoW wording.
- There is no priority column and there are no priority tags.
- Everything in an assignment is essential by default.
- An exception is marked by a note reading *optional* on that item.
- Each item covers one idea.
- Each item is written once.
- Each item is written in full, correct sentences.
- Testability is recommended, not required. Assignments are deliberately high-level, and delegating concretisation through a deliverable item is a legitimate outcome.
- Defined terms are capitalised in item text, to signal that they appear in the Terms section.
- An item must not depend on an external link to be understood, agreed or later tested.

Why the items are written so: [The assignment](../about/the-assignment.md).

## The items of a BRD

The BRD follows the rules of the assignment above, with these made stricter.

- Testability is mandatory. Every business requirement (BR) and every non-functional requirement (NFR) can be shown met or not met.
- One idea per item, within reason. A list of two to nine members inside an item is allowed where the members are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value that no stakeholder gave. A category without a value is an open question (TBC) with an owner, never a figure from the skeleton.
- Every BR and every use case (UC) cites its parent, a REQ item or a POS item.
- In a work product made from a source, the parent is the path of the source and the place in it.
- That place is a turn of the principal's side. What a vendor or any other party said is cited only by a dependency (DEP) or by a note after an item, never by a shall.
- An NFR cites the REQ or POS item it follows from where there is one. Otherwise it cites its category of the template, since the qualities are asked of every ask whether the parent named them or not.
- An item with neither a parent nor a category is a finding of the check.
- `shall` and `shall not` are the wording of a BR and of an NFR.
- The steps of a UC are written in the active voice and the present tense, as a scenario and not as a rule. Example: "the Customer submits the order".
- A type is never told by a number. The prefix says what an item is, and the group says where it belongs.

Why the items are written so: [The BRD](../about/the-brd.md).

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
