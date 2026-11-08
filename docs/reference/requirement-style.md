---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 45505ee7ff04e54e
inputs:
  - .claude/skills/forge/states/assignment.md#Requirement style
  - .claude/skills/forge/states/brd.md#Requirement style
  - .claude/skills/forge/states/user-stories.md#Story style
---

# Requirement style and Story style

This page lists the rules for how the items of an assignment, of a
BRD and of the user stories are worded. It is for the reader who
writes or checks such items, whether as the principal (the person
whose thinking is forged) or as someone who extends the forge.

## Requirement style of the assignment

- An item is an obligation in the indicative.
- In English the verb is **shall** or **shall not**, strictly.
- Would, could, should, might, may and MoSCoW wording are not used.
- In another language the item uses the language's own verb of
  obligation.
- That verb is never a conditional, a permission or a wish.
- The forge names no word of another language.
- There is no priority column and there are no priority tags.
- Everything in an assignment is essential by default.
- An exception is marked by a note reading *optional* on that item.
- Each item covers one idea, is written once, and is written in
  full, correct sentences.
- Testability is recommended, not required.
- Assignments are deliberately high-level, and delegating the
  concretisation through a `DEL` item is a legitimate outcome.
- Defined terms are capitalised in item text to signal that they
  appear in the Terms section.
- An item must not depend on an external link to be understood,
  agreed or later tested.

## Requirement style of the BRD

The BRD takes the style of the assignment above, with these rules
made stricter:

- Testability is mandatory: every `BR` and `NFR` can be shown met or
  not met.
- One idea per item, within reason: a list of two to nine members
  inside an item is allowed where the members are one rule.
- A note after an item is allowed and carries no requirement.
- An item may name the role that owns it.
- No value that no stakeholder gave: a category without a value is a
  `TBC` with an owner, never a figure from the skeleton.
- A `TBC` is defined once, in Open questions, with its owner and
  whether it blocks estimation.
- A `BR` or an `NFR` whose rule is not known cites the `TBC` in
  brackets, as it cites its parent.
- Every `BR` and `UC` cites its parent, a requirement or a position
  of the intent.
- In a work product made from a source, the parent is the path and
  the place in the source.
- The place is a turn of the principal's side.
- What a vendor or any other party said is cited only by a `DEP` or
  by a note after an item, never by a shall.
- An `NFR` cites the requirement or position it follows from where
  there is one.
- Otherwise an `NFR` cites its category of the template, since the
  qualities are asked of every ask whether the parent named them or
  not.
- An item with neither parent nor category is a finding of the check.
- The obligation of the assignment's style is the wording of a `BR`
  and an `NFR`: `shall` / `shall not` in English.
- The steps of a `UC` are written in the active voice, present tense,
  as a scenario and not as a rule. Example of a step: "the Customer
  submits the order".
- A type is never told by a number: the prefix says what an item is,
  the group says where it belongs.

## Story style of the user stories

- A story is one function as the one who uses it meets it: one actor
  doing or seeing one thing.
- The rules of that function are its acceptance criteria and edge
  cases, never stories of their own.
- Those rules are its variants by condition (a visitor not logged in,
  a datum missing or deleted, the state after the release), its
  qualities and its transitions.
- A new story begins where another actor does something else, or the
  same actor reaches a different function.
- What happens in the usual course is an acceptance criterion.
- An edge case is a situation at the border of the behaviour: a
  failure, a missing datum, a change during use.
- The sentence of a story is free.
- It carries who or what wants the function, what happens and why
  ("..., so that...").
- The form "As a... I want... so that..." is neither required nor
  forbidden.
- An acceptance criterion is in the indicative, present tense, one
  behaviour per bullet. Example of a criterion: "The carousel shows
  at most 5 slides."
- No vague word: a word that names a quality without a value, in
  whatever language the project writes ("fast", "suitable",
  "intuitive", "unacceptable").
- Instead of a vague word the story gives a value, or a question
  with an owner where nobody gave one.
- An edge case is written "situation → what happens".
- A risk is written "risk → mitigation" or "risk → consequences",
  never alone.
- A note is a link to an attachment or a technical analysis with what
  lies behind it, nothing else.
- The labels `Edge cases`, `Risks`, `Note`, `Questions` and
  `Reference` are fixed and in English.
- The content under the labels is in the project's language.
- `Reference` is the one part every story has: the `BR`, `NFR`, `UC`
  or `DEP` it serves, or in a small change without a BRD the
  position of the intent.
- The other parts are left out where a story has nothing for them,
  never left empty.
- No technical solution, no priority, no estimate.

## See also

- [The assignment](../about/the-assignment.md): why the items of an assignment are written so.
- [The BRD](../about/the-brd.md): why the items of a BRD are written so.
- [The user stories](../about/the-user-stories.md): why a story is shaped so.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
