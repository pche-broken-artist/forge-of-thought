---
generated: 2026-10-09
made: mirrored
inputs-hash: 9e9e1e835070dfc2
inputs:
  - .claude/skills/forge/states/solution-design.md
  - templates/solution-design.md
  - CLAUDE.md
---

# Design the solution

This page is for a user whose project has a layer above the solution
design and who wants to write the design, bring it current or fix it.
It says what `/forge solution-design` does and what you do in it.

## What the command does

`/forge solution-design [slug]` iterates `40-solution-design.md`, the
document that says how the things wanted are realised. Claude derives
it from the lowest layer the project has above it, reading that layer
and whatever stands above it, the decisions, the ledger and the
project's open threads. Where the thing already exists, Claude reads
what realises it as it stands. Research and sources are read as you
direct.

Whether a project needs a design at all is yours to say. A project
without one is not missing anything.

## The ways in

Which pass you start depends on the state of the project:

- **No design yet.** The first design is created from the template as
  a draft, with its history companion and its row in the ledger.
- **A layer above has moved.** The pass runs on what changed.
- **The thing changed below.** The design is brought current with it.
- **A wording fix.** It is made directly.

## What you do

You choose how the design is composed: found together with Claude by
questions, or handed over with a few sentences of what you want, in
which case Claude returns a proposal. Either way Claude proposes the
parts and the choices, and you judge them. Claude names the few real
choices and does not dress every part as one. Where there was no real
alternative he says so, and where a reason is not known he says it is
unknown. A choice you have not yet judged is marked as such in the
design until you do.

As in every working conversation, what is agreed is carried in the
conversation and written once at the end of the round, on your word.
Nothing is built here: the design specifies.

## The coverage map

At every pass Claude makes a coverage map with two lists: the in-scope
items of the layer above that no part realises, and the parts that
realise no item. The map is a tool of the pass and is not part of the
design. The design counts as complete for now when every in-scope item
above is realised by a part, knowingly left unanswered, or open as a
question, and no question that blocks realisation is open. It is kept
current and never finished.

## When something cannot be realised

If the designing shows that something wanted cannot be realised, or
only at a price not worth paying, Claude raises it as a thread. What is
wanted is then decided in the intent first, and the design follows.

## At the end of the pass

Claude names what changed and what stays open. When the design is
complete for now, he offers approval as a recommendation, never as a
gate.

Once the design stands, `/challenge <persona> solution-design` is
offered, and the persona `architect` exists for it. It is never run on
Claude's own judgement. See [Challenge the thinking](challenge-the-thinking.md)
for how a challenge runs.

For what a solution design holds and why it restates nothing above it,
see [About the solution design](../about/the-solution-design.md).

## See also

- [About the solution design](../about/the-solution-design.md): what a solution design holds and why it restates nothing above it.
- [Challenge the thinking](challenge-the-thinking.md): the challenge of the design.
