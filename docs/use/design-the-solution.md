---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 64969471c1b76682
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - .claude/agents/challenger-architect.md
---

# Design the solution

This page shows how you iterate the solution design, the file
`40-solution-design.md` that says how the things wanted are realised,
with the command `/forge solution-design`. It is for you when a project
has reached the point where someone has to build or do what the layers
above ask for. The principal is whoever's thinking is being forged:
here, you.

For what a solution design holds and why it exists, see
[The solution design](../about/the-solution-design.md). Terms of the
forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when the project has something above the design to realise. The
design is built from the lowest layer the project has above it: the
intent alone, the assignment, the BRD or the user stories.

Whether a design is worth writing at all is yours to say. Claude does
not decide it.

There are four ways in:

- No design yet. You say the project needs one, and the first pass
  writes it.
- A layer above has moved. The pass runs on what changed.
- The thing changed below, where it is built. The design is brought
  current.
- A wording fix. It is made directly, without a pass.

## The command

```
/forge solution-design [slug]
```

The slug names the project. Leave it out and Claude resolves the
project from where you are working.

## What happens

1. Claude reads the lowest layer above the design, whatever stands
   above that, the decisions of the project and its threads. Where the
   thing already exists, it reads what realises it as it stands. It
   also reads the design as it stands.

   You should now see Claude say what it has read and which of the four
   ways in applies.

2. Claude proposes the parts of the solution and the few real choices
   among them. For each real choice it says what was chosen, against
   what, and what it costs. Where there was no real alternative, it
   says so and invents none. Where a reason is not known, it says that
   it is unknown.

   You should now see parts and choices put to you to judge, and a
   choice you have not judged marked as Claude's own in plain words.

3. Claude makes the coverage map. The map lists the items of the layer
   above that are in scope and have no part, and the parts that realise
   no item. It is a tool of the pass and is not part of the design.

   You should now see both lists, each empty or named.

4. What the designing shows cannot be realised, or only at a price not
   worth paying, goes back to the intent as a thread. What is wanted is
   decided in the intent first, and the design follows.

   You should now see a thread raised for each such matter, and no
   change to what is wanted made in the design itself.

5. Claude ends by naming what changed and what stays open. When every
   in-scope item of the layer above is realised by a part, knowingly
   left unanswered or open as a to-be-confirmed matter, and no open
   matter that blocks realisation remains, Claude offers the approval.
   It is a recommendation, never a gate.

   You should now see what changed, what is open, and, where the design
   is complete for now, the offer of approval.

Claude writes once at the end of the round, on your word. You may order
a write of what is agreed so far at any moment.

## What you have afterwards

- `40-solution-design.md`, written in the shape of
  `templates/solution-design.md`: how the parts work together, the
  parts, what holds across the parts, and what is open.
- A history record beside it, `40-solution-design.history.md`, that
  carries what changed and why.
- Threads in the intent for whatever could not be realised.

The design is complete for now, never finished: it is kept current as
the layers above and the thing itself change.

## Challenge the design

Once the design stands, Claude offers
`/challenge <persona> solution-design`. It never runs it on its own
judgement. The persona `architect` exists for it: it reviews a solution
design, from outside the conversation, and returns what it finds. How a
challenge runs and how its findings are settled is described in
[Challenge the thinking](challenge-the-thinking.md). The personas that
exist today are listed in
[Challenger personas](../reference/challenger-personas.md).

```
/challenge architect solution-design
```

## A worked example

A project with the placeholder slug `my-project` has an intent and an
assignment, and no design.

```
/forge solution-design my-project
```

Claude reads the assignment, the intent and the threads. It proposes
three parts: one that collects the requests, one that decides who
handles each, one that reports the result. For the second it names one
real choice, a fixed rule against a person deciding each case, and says
what each costs. For the first and third it says there was no real
alternative.

The coverage map shows one in-scope item of the assignment with no
part. You decide it is knowingly left unanswered for now, and Claude
marks it open as a to-be-confirmed matter that does not block
realisation. The designing also shows that one wanted item cannot be
realised as worded. Claude raises it as a thread for the intent and
does not change the item.

Claude names what changed and what stays open. You say write, and
`40-solution-design.md` and its history record are written. Claude then
offers `/challenge architect solution-design`.

## See also

- [The solution design](../about/the-solution-design.md): what a
  solution design holds.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of
  the design.
- [Challenger personas](../reference/challenger-personas.md): the
  personas of today, the architect among them.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
