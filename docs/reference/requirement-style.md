---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: f989afcec99230c6
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
---

# Requirement style

This page states the rules for writing the items of an assignment
(see [The assignment](../about/the-assignment.md)) and the stricter
rules for the items of a BRD, a business requirements document (see
[The BRD](../about/the-brd.md)). It is for the user who reads or
writes such items and for the extender who changes the rules.

## The rules of an assignment

- Use **shall** / **shall not**. Do not use would, could, should,
  might, may, or MoSCoW wording.
- There is no priority column and there are no priority tags.
  Everything in an assignment is essential by default. An exception
  is marked by a note reading *optional* on that item.
- Each item covers one idea, is written once, and is written in
  full, correct sentences.
- Testability is recommended, not required. Assignments are
  deliberately high-level, and delegating concretisation through a
  deliverable item is a legitimate outcome.
- Defined terms are capitalised in item text to signal that they
  appear in the Terms section.
- An item must not depend on an external link to be understood,
  agreed or later tested.

## The rules a BRD makes stricter

A BRD follows the rules of an assignment above, with these made
stricter for its items.

- Testability is mandatory: every business requirement (BR) and
  every non-functional requirement (NFR) can be shown met or not.
- Each item covers one idea, within reason. A list of two to nine
  members inside an item is allowed where they are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value is given that no stakeholder gave. A category without a
  value is an open question (TBC) with an owner, never a figure from
  the skeleton.
- Every BR and every use case (UC) cites its parent, a requirement
  (REQ) or a position (POS) item. In a work product made from a
  source, the parent is the path and the place in the source. The
  place is a turn of the principal's side. What a vendor or any other
  party said is cited only by a dependency (DEP) or by a note after
  an item, never by a shall.
- An NFR cites the REQ or POS item it follows from where there is
  one. Otherwise it cites its category of the template, since the
  qualities are asked of every ask whether the parent named them or
  not.
- An item with neither parent nor category is a finding of the
  check.
- `shall` / `shall not` is the wording of a BR and an NFR. The steps
  of a UC are written in the active voice, present tense
  ("the Player submits the bet"), as a scenario and not as a rule.
- A type is never told by a number. The prefix says what an item is,
  and the group says where it belongs.

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
