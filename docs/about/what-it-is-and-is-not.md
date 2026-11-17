---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 7ce66f8d6af26332
inputs:
  - CLAUDE.md#What this workspace is
  - projects/forge/10-intent.md#Essence
  - projects/forge/10-intent.md#POS.0005
  - projects/forge/10-intent.md#POS.0010
  - projects/forge/10-intent.md#POS.0070
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0330
  - projects/forge/10-intent.md#POS.0600
  - projects/forge/10-intent.md#POS.0620
  - projects/forge/10-intent.md#REJ.0125
  - projects/forge/10-intent.md#REJ.0130
---

# What the forge is and is not

Forge of Thought is a workshop for thinking: an idea of any kind is
worked through a chain of versioned documents, under review, until
the person whose idea it is stands behind what is written. This page
says what the forge is, what it is not and why it is so. It is for
anyone who meets the forge for the first time.

## What it is

Forge of Thought is a place for forging thoughts: a workshop where
thought is tempered and shaped. In plain words, an idea travels a
[chain](how-a-thought-travels.md) of versioned documents, from the
idea put together onward, under isolated adversarial review.

The chain ends where the project needs it to. Below the
[intent](../reference/glossary.md) a project takes the layers it
needs, and many projects end at the intent.

The forge is a general-purpose engine. It is not bound to one person
or to one management relationship. Anyone can be the
[principal](the-principal-and-claude.md), that is the person whose
thinking is being forged.

The subject matter is deliberately unconstrained. It may be:

- a process redesign
- a platform initiative
- an organisational topic
- anything else

An [assignment](../reference/glossary.md) is one of the documents a
chain may hold. Its recipients are whoever receives it. They may be:

- teams
- colleagues
- the principal's future self

Some facts belong to an [instance](../reference/glossary.md) (one
installation of the forge) and are not properties of the system:

- who the principal is
- what language the conversation runs in
- the handle the principal signs records with

These facts are kept in `CLAUDE.local.md` at the root of the engine
(a file kept out of git).

Claude is the principal's cognitive extension, not a supplier. Claude
owns:

- structure
- order
- process discipline
- document hygiene

The principal owns the content and every decision.

"Cognitive extension" means an amplifier of the principal's thinking,
never its substitute. Claude's contribution to the content is:

- to criticise
- to challenge
- to inspire
- to lay out options

The composition belongs to the principal, who assembles what the
forge offers into the principal's own positions and decisions. What
Claude proposes does not enter the content by being proposed. It
enters only when the principal takes it up. Claude proposes and
never decides.

## What it is not

### Not a program

The forge runs in Claude Code (an agent for the command line). The
mechanisms belong to Claude Code:

- the slash commands
- the skills
- the agents
- the hooks

The forge is what these mechanisms are told.

### Not a delivery tool

Nothing is implemented in the forge: the engine specifies. A run of
the forge ends where its owner is satisfied. The outcome is an
[artefact](../reference/glossary.md) (a forged document) the
principal stands behind, and nothing further. An intent may be
immaterial and carry no delivery at all.

Outside the scope of the forge, and outside its sight, are:

- sponsorship
- funding
- adoption
- delivery outcomes

This is left open, not closed. The forge may one day feed a delivery
chain. Whether a delivery side would be grown as layers of the forge
or as a separate framework is deliberately undecided. The direction
the forge is developed in is the subject of
[Where the forge is going](where-it-is-going.md).

### Not a chat

State lives in files, never only in the conversation. What is in a
file is still there when the conversation is over. What lives only
in the conversation is not.

### Not tied to one domain

The mechanics of the chain are the same in every domain. The same
machinery that forges a platform assignment would forge a D&D
campaign: an intent of the story, then materials rendered for the
one who runs the game.

## How it works

An idea is put together, and from there it travels the chain as far
as its project needs.

```
an idea, put together
          |
          v
     the intent  ......  many projects end here
          |
          v
  the layers a project needs, as far as it needs them
```

The chain grows by adding the
[definition](../reference/glossary.md) of a new layer. Nothing that
exists is reworked for it.

The primary ambition is the full chain: from a raw idea all the way
to a deck ready for realisation, growing layer by layer. The layers
named on that way are, in this order:

1. an assignment
2. a BRD
3. user stories
4. a solution design
5. an implementation-ready specification, including integration

While the work runs, Claude keeps the structure, the order and the
discipline of the process. Every decision about content remains with
the principal.

Isolated AI reviewers provide adversarial pressure from different
angles. They are deliberately blind to the working conversation.

## Why

### Why a general engine

The forge began as one person's tool. That origin is an instance
fact, not the system. The framing of the forge as one person's tool
is rejected as the identity of the system. The reason is that it
describes the first instance, not the engine.

### Why the name

The system is named Forge of Thought. Thoughts are the raw material:
they may be of whatever kind, and nothing is presumed about them.
Forged artefacts are the product, and an assignment is one among
them. The name is chosen with the full chain in mind. The full name
stands in documents. The short form "Forge" is expected in daily
speech.

Two other names are rejected:

- "Cascade": it literally names the waterfall.
- "Foundry": it collides with the names of existing products.

### Why "thought" and not "assignment"

An assignment is one place a chain may end, not the goal. For that
reason the subtitle of the README is "*A workshop where thought is
tempered and shaped.*" Any subtitle or one-line description must
present the forge as a place and space where thoughts are forged. It
must not name the assignment as the goal.

Every design decision is made with the growth of the chain in mind.
That is why the name says thought, not assignment. It is also why
files and IDs are numbered with gaps.

### Why the chain ends where the project needs it to

The forge is a general tool for forging thoughts. The outcome of a
run is an artefact the principal stands behind, and nothing further.
A run therefore ends where its owner is satisfied. An intent may be
immaterial and carry no delivery at all.

## A worked example

The thought below is invented, and so is the slug of its project,
`reading-year`.

A principal wants to settle what a year of reading is for. There is
no team to brief and nothing to deliver. The idea is put together,
and the work on the intent begins.

In the conversation Claude keeps the structure and the order. It
lays out options, for instance reading few books slowly against
reading widely, and it challenges the choice the principal leans to.
The principal takes up the first option and leaves the second. Only
what the principal took up enters the intent.

Isolated reviewers read the written intent. They saw nothing of the
conversation, and they press on the intent from different angles.
What becomes of what they return is the principal's decision.

What was agreed is written in the files of the project. It is still
there when the conversation is over.

The principal reads the intent and stands behind it. The run ends at
the intent. The project takes no layer below it: it needs none.
Whether the year of reading turns out as intended is outside the
scope of the forge and outside its sight.

A different thought ends elsewhere. A thought that others are to act
on goes on below the intent, for instance to an assignment for
colleagues, and ends where its project needs it to.

## See also

- [How a thought travels through the forge](how-a-thought-travels.md):
  the course of one thought through the forge.
- [The principal and Claude](the-principal-and-claude.md): the two
  roles and the rule between them.
- [Where the forge is going](where-it-is-going.md): the direction the
  forge is developed in.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
