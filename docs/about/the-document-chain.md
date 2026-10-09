---
generated: 2026-10-09
made: derived
inputs-hash: 881b0517aab6280b
inputs:
  - CLAUDE.md
  - .claude/skills/forge/SKILL.md
  - projects/forge/10-intent.md
---

# About the document chain

This page explains what the document chain is: the row of versioned
documents an idea travels through in a project, where it starts,
what its trunk is, how it grows and where a change goes. It is for
anyone who uses the forge, anyone who wants to extend it with a new
layer, and anyone judging whether its shape holds together. It was
put together from `CLAUDE.md`, the definition of the `/forge`
command and the positions of the forge's own intent.

## What the chain is

An idea of any kind, a process redesign, a platform initiative, an
organisational topic, travels a chain of versioned documents, from
the idea as it was put together onward, under isolated adversarial
review. The documents of the chain are called artefacts: the ones
the principal composes, the reviewers read and the renders are
generated from. Every other file of a project (a history, a
decision record, a review, a source) is a document but not an
artefact.

Nothing is implemented in the forge: the engine specifies, and the
chain ends where the project needs it to.

## Where it starts and what its trunk is

A chain starts at a brief and its trunk is the intent.

- The brief is the principal's own text of one whole of thinking:
  what he wants and why, with what he chose to take from the finding
  around it. It is free-form, holds thoughts to be processed rather
  than decisions, and only the intent turns them into positions.
- The intent is where those thoughts become positions the principal
  holds, with stable IDs. It is the trunk: every layer below it is
  derived from it, directly or through the layer above.

Below the intent a project takes the layers it needs. No layer
below the intent is a condition of another, and many projects end
at the intent, where what is wanted needs no further document
written down. A layer a project does not have is not missing: the
state map and the checks say nothing of it, and the ledger declares
no end of the chain.

## A star, not a line

Every artefact of the chain has a definition: a state file in
`.claude/skills/forge/states/<state>.md`, named after the artefact
it produces and paired with the artefact's template. The definition
says what the artefact is, how it is found (by questions, research
and sources) and owns its rules; the template says what comes out.

Each definition declares its own inputs. That is why the chain is a
star and not a fixed line: a layer branches from any artefact above
it, and the number in a file name orders the files without
prescribing a sequence. Adding a layer means adding one definition;
nothing that exists is reworked.

Work on the chain is invoked by target state, never by verb:
`/forge intent`, `/forge assignment`, and so on. Knowing the name of
the target artefact is knowing the command, with nothing to memorise
as layers are added. `/forge <state>` is a dispatcher: it resolves
the state file for the name it is given and follows it, and the
dispatcher itself never changes when a layer is added. Bare `/forge`
reports the map of a project: which artefacts exist, at what version
and status, and which target states can be worked on from here.

## Numbering

Files in the chain are numbered in tens: `00-brief.md`,
`10-intent.md`, `20-assignment.md`, and so on. The gaps of ten leave
room for a layer to be added between existing ones without renaming
anything that exists.

```
NN-<artefact>.md   an artefact of the chain, versioned
<file>.history.md  history of each versioned document,
                   an append-only companion beside it
decisions.md       append-only decision records
ledger.md          single source of truth for state
```

## Which artefacts exist

Which artefacts the forge has is the listing of the definitions
directory, `.claude/skills/forge/states/`, one definition each. They
are listed nowhere else; the table of artefacts in the README is
rendered from the definitions. A new kind of artefact enters the
forge by its definition and template being added as a pair, on the
principal's decision, never on Claude's own.

## Where a change goes

Changes are intent-first. A change of substance goes into the
intent and propagates from there down the whole chain the project
has: each lower layer is brought to the intent. Only wording is
fixed downstream directly.

A change may also come from below. When solving shows that what is
wanted cannot be had, or must be wanted differently, the intent
changes first and the layers follow.

Behind this stands one principle: from the artefacts of the chain
the thing must be buildable without a look at the finished product.
The product is what is built, never a source of its own design. How
deep the chain must go for that is the project's to decide.

## One principal per chain

The chain never spans two principals. The layers below the intent
grow in the same project, by the same principal's hand, when he
chooses to take his own thought further. An assignment is written
to be self-contained for exactly this reason: what a recipient does
with it in his own instance is his own run of the forge, and the
assignment becomes his brief. Feedback from recipients has no
channel of its own; the principal processes it and feeds his
conclusions back through `/forge intent`.

## See also

- [About the brief](the-brief.md): the first artefact.
- [About the intent](the-intent.md): the trunk.
- [Artefacts](../reference/artefacts.md): the definitions of today, one row each.
