---
generated: 2026-10-10
made: derived
inputs-hash: 94d2f7eda59b7ce5
inputs:
  - CLAUDE.md
  - .claude/skills/forge/SKILL.md
  - projects/forge/10-intent.md
---

# About the document chain

This page explains what the document chain of a project is: where
it starts, what its trunk is, how it grows, and where a change goes
once the chain has more than one layer. It is for anyone who uses
the forge, extends it with a new kind of artefact, or evaluates how
it is built. It was put together from `CLAUDE.md`, the `/forge`
skill (`.claude/skills/forge/SKILL.md`) and the forge's own intent
(`projects/forge/10-intent.md`).

## What the chain is

An idea travels through the forge as a chain of versioned documents,
the artefacts, from the idea put together onward, under isolated
adversarial review. The chain starts at a brief, the principal's own
text of what he wants and why, and its trunk is the intent, where
that text is worked into positions the principal holds. Every
project has these two; they are the trunk of every project.

Below the intent a project takes the layers it needs, and no layer
below the intent is a condition of another. Many projects end at the
intent, where what is wanted needs no solution written down. A layer
a project does not have is not missing: the state map (`/forge`) and
the checks say nothing of it, and the ledger declares no end of the
chain. How deep a chain goes is the project's own matter: deep
enough that what is wanted can be built from the artefacts alone,
without a look at a finished product, since the product is what is
built and never a source of its own design.

The chain ends at content. Nothing is implemented in the forge; the
engine specifies. A render, an audience-specific output generated
from the chain, is not part of it: the boundary between chain and
render is authorship. A chain artefact is composed by the principal
with Claude; a render is generated from artefacts.

## The chain is a star, not a line

Every artefact of the chain has a definition, one file in
`.claude/skills/forge/states/`, paired with the artefact's template.
The definition says what the artefact is, how it is found, by
questions, research and sources, and what its inputs are; the
template says what comes out.

Because each definition declares its own inputs, the chain is a
star, not a fixed line. A layer branches from any artefact: a new
kind of artefact is added by adding one definition, without
reworking anything that exists. The solution design, for example, is
derived from the lowest layer the project has above it, whether that
is the intent alone, an assignment or something in between; whatever
stands above it is its input.

Work on the chain is invoked by target state, never by verb:
`/forge intent`, `/forge assignment`, and so on for every artefact
the forge has. Knowing the name of the artefact is knowing the
command, with nothing to memorise as layers are added. The
dispatcher behind `/forge <state>` resolves the definition of the
named state, reads it and follows it; it never changes when a layer
is added, because everything a layer needs is in its definition.
Bare `/forge` reports the state map of a project: which artefacts
exist, at what version, and which target states can be worked on
from here because their inputs exist.

## How the files are numbered

The files of the chain carry a number in tens: `00-brief.md`,
`10-intent.md`, and the layers below in the same pattern. The gaps
of ten leave room for a layer to be added between two existing ones
without renaming anything that exists. The number orders the files
on disk and prescribes no sequence: which artefact is derived from
which is said by the definitions, not by the numbers.

Beside every artefact lies its history, an append-only companion
`<file>.history.md`; beside the chain lie the project's decisions
and its ledger, the single source of truth for state.

## Which artefacts exist

Which artefacts the forge has is the listing of the definitions
directory, one definition each. They are listed nowhere else by
hand; the table of artefacts in the README is rendered from the
definitions, and the reference page linked below mirrors them. A
kind of artefact that has no definition does not exist, however
often it is talked about.

## Where a change goes

A change of substance goes into the intent first and propagates from
there down the whole chain the project has: each lower layer is
brought to the changed intent. Only wording is fixed in a lower
layer directly.

The change may come from below. When solving shows that what is
wanted cannot be had, or must be wanted differently, the intent
still changes first and the layers follow. If the principal dictates
substance straight into a lower layer, the corresponding change of
the intent is proposed in the same step. The reason is that the
intent is the one place that says what is wanted; a lower layer
that drifts from it leaves the project with two accounts of the
same thing.

## One principal, one chain

The layers below the intent grow in the same project, by the same
principal's hand, when he chooses to take his own thought further. A
chain never spans two principals. What a recipient does with an
assignment handed to him is his own run of the forge: the assignment
becomes his brief, in his own instance, and it is self-contained for
exactly that reason. Feedback from recipients has no channel of its
own; the principal processes it and feeds what he concludes back
into the intent.

## See also

- [About the brief](the-brief.md): the first artefact.
- [About the intent](the-intent.md): the trunk.
- [Artefacts](../reference/artefacts.md): the definitions of today, one row each.
