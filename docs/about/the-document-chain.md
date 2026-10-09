---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - .claude/skills/forge/SKILL.md
  - projects/forge/10-intent.md
---

# About the document chain

This page explains what the document chain of a Forge of Thought
project is, how it grows and where a change goes. It is for anyone who
uses the forge, extends it with a new kind of artefact, or wants to
judge how it is built. It was put together from `CLAUDE.md` (What this
workspace is, Document chain, Working methods), the `/forge` command's
definition `.claude/skills/forge/SKILL.md` and the positions of the
forge's own intent that give the reasons.

## What the chain is

An idea travels through a chain of versioned documents, the
artefacts, from the idea first put together onward. The chain starts
at a brief: the principal's own text of what he wants and why. Its
trunk is the intent, where those thoughts become the positions he
holds.

Below the intent a project takes the layers it needs, and no layer
below the intent is a condition of another. Many projects end at the
intent, where what is wanted needs no further layer written down. A
layer a project does not have is not missing: `/forge` and the checks
say nothing of it, and the ledger declares no end of the chain. The
chain ends where the project needs it to.

The reason is that thoughts are forged as far as the principal needs
them taken. A further layer is worth writing where it earns its
place, and whether it does is his to say, not the forge's.

## A star, not a line

Every artefact of the chain has a definition: a state file in
`.claude/skills/forge/states/<state>.md`, named after the artefact it
produces and paired with the artefact's template. The definition says
what the artefact is, how it is found and what its rules are; the
template says what comes out.

Each definition declares its own inputs. So the chain is a star, not
a fixed line: a new layer can branch from any artefact by adding one
definition. The number in a file name orders the files and
prescribes no sequence.

Work on an artefact is invoked by its name: `/forge <state>`, for
instance `/forge intent`. Knowing the name of the artefact is knowing
the command, so there is nothing to memorise as layers are added.
The dispatcher behind `/forge` never changes: adding a layer means
adding a file. Run bare, `/forge` reads the definitions directory
and reports which artefacts can be worked on from where the project
stands.

## Which artefacts exist

Which artefacts the forge has is the listing of the definitions
directory, one definition each. They are listed nowhere else, and the
table of artefacts in the README is rendered from the definitions.
The chain grows by adding a layer's definition, without reworking
anything that exists.

## Numbering

Files of the chain are named `NN-<artefact>.md` and numbered in tens:
`00-brief.md`, `10-intent.md` and so on. The gaps of ten leave room
for a layer to be added later without renaming or renumbering
anything that exists. Beside each versioned document stands its
history companion, `<file>.history.md`; a project also keeps
`decisions.md` and `ledger.md`.

## Where a change goes

Substance goes into the intent first and propagates from there down
the whole chain the project has; each layer below is brought to it.
Only wording is fixed downstream directly.

A change may also come from below: when solving shows that what is
wanted cannot be had, or must be wanted differently, the intent
changes first and the layers follow. This keeps the intent the one
place where what is wanted is said, so no layer below drifts away
from it.

## One principal per chain

The chain never spans two principals. The layers below the intent
grow in the same project, by the same principal's hand, when he
chooses to take his own thought further. An assignment handed to
someone else is not continued in the sender's chain: what the
recipient does with it is his own run of the forge, where the
assignment becomes his brief. An assignment is self-contained for
exactly that reason.

## See also

- [About the brief](the-brief.md): the first artefact.
- [About the intent](the-intent.md): the trunk.
- [Artefacts](../reference/artefacts.md): the definitions of today, one row each.
