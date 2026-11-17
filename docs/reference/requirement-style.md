---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 4f772c8988322ea9
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
  - .claude/skills/forge/states/user-stories.md#Story style
---

# Requirement style and Story style

This page lists the writing rules of the items of an assignment, the stricter rules of the items of a BRD and the rules of a user story. It is for the reader who writes or checks such items. Terms of the forge are in the [Glossary](glossary.md).

## Requirement style of the assignment

- An item is an obligation in the indicative.
- In English the verbs are **shall** and **shall not**, used strictly. The words would, could, should, might, may and MoSCoW wording are not used.
- In another language the item uses that language's own verb of obligation. It is never a conditional, a permission or a wish. The forge names no word of another language.
- There is no priority column and there are no priority tags. Everything in an assignment is essential by default. An exception is marked by a note reading *optional* on that item.
- Each item covers one idea, is written once and is written in full, correct sentences.
- Testability is recommended, not required. Assignments are deliberately high-level, and delegating concretisation through a `DEL` item is a legitimate outcome.
- Defined terms are capitalised in the item text, to signal that they appear in the Terms section.
- An item does not depend on an external link to be understood, agreed or later tested.

## Requirement style of the BRD

The BRD keeps the Requirement style of the assignment, with these rules made stricter.

- Testability is mandatory. Every BR and NFR can be shown met or not met.
- One idea per item, within reason. A list of two to nine members inside an item is allowed where they are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value appears that no stakeholder gave. A category without a value is a TBC with an owner, never a figure from the skeleton.
- A TBC is defined once, in Open questions, with its owner and whether it blocks estimation. A BR or an NFR whose rule is not known cites the TBC in brackets, as it cites its parent.
- Every BR and UC cites its parent, which is a requirement of the assignment or a position of the intent. In a work product made from a source, the parent is the path and the place in the source. The place is a turn of the principal's side. What a vendor or any other party said is cited only by a DEP or by a note after an item, never by a shall.
- An NFR cites the requirement or position it follows from where there is one. Otherwise it cites its category of the template, since the qualities are asked of every ask whether the parent named them or not.
- An item with no parent and no category is a finding of the check.
- The wording of a BR and an NFR is the obligation of the assignment's style, `shall` and `shall not` in English.
- The steps of a UC are written in the active voice, present tense, as a scenario and not as a rule. Generic step: "the Customer submits the order".
- A type is never told by a number. The prefix says what an item is, and the group says where it belongs.

## Story style of the user stories

- A story is one function as the one who uses it meets it: one actor doing or seeing one thing.
- The rules of that function are its variants by condition (a visitor not logged in, a datum missing or deleted, the state after the release), its qualities and its transitions. They are its acceptance criteria and edge cases, never stories of their own.
- A new story begins where another actor does something else, or where the same actor reaches a different function.
- What happens in the usual course is an acceptance criterion.
- An edge case is a situation at the border of the behaviour: a failure, a missing datum, a change during use.
- The sentence of a story is free. It carries who or what wants it, what happens and why ("..., so that..."). The form "As a... I want... so that..." is neither required nor forbidden.
- An acceptance criterion is in the indicative, present tense, one behaviour per bullet. Generic criterion: "The carousel shows at most 5 slides."
- No vague word is used. A vague word names a quality without a value ("fast", "suitable", "intuitive", "unacceptable"), in whatever language the project writes. Where nobody gave a value, the story holds a question with an owner.
- An edge case is written "situation → what happens".
- A risk is written "risk → mitigation" or "risk → consequences", never alone.
- A note is a link to an attachment or a technical analysis with what lies behind it, nothing else.
- The labels `Edge cases`, `Risks`, `Note`, `Questions` and `Reference` are fixed and in English. The content is in the project's language.
- `Reference` is the one part every story has. It names the BR, NFR, UC or DEP the story serves, or, in a small change without a BRD, the position of the intent.
- The other parts are left out where a story has nothing for them, never left empty.
- A story carries no technical solution, no priority and no estimate.

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [The user stories](../about/the-user-stories.md): why a story is shaped so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
