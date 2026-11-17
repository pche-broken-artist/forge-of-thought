---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 23c99c3b28d521e0
inputs:
  - projects/forge/10-intent.md#POS.0700
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1430
  - projects/forge/10-intent.md#POS.1440
  - projects/forge/10-intent.md#POS.1990
---

# Where the forge is going

The forge is developed in a direction that is named, toward no
destination and against no deadline. This page says what that
direction is, what stands today, what is intended and what is
deliberately not promised. It is for the reader who uses the forge,
the reader who extends it and the reader who weighs it.

## What it is

The forge is a general tool for forging thoughts. A thought is worked
through a [chain](the-document-chain.md) of documents until the
principal (the person whose thinking is being forged) is satisfied.
The outcome is an [artefact](../reference/glossary.md) (a document of
the chain) that the principal stands behind, and nothing further.

The forge has an owner, who decides what enters it. He names the
direction in which the forge is developed. Destinations and deadlines
are not named.

The direction is named along these lines:

- The chain is extended downward, as far as the principal needs a
  thought taken.
- A new kind of artefact is added by one command, and a user of the
  forge is to be able to add a kind of his own.
- A model of another family is reached for research today, and
  reviewers on the same link are intended.

One limit holds along all of them: the chain never spans two
principals.

## How it works

### The chain grows downward

The owner intends to keep extending the
[engine](projects-and-the-engine.md) downward. The engine is the part
of the forge that every user of it shares. Thoughts are forged as far
as the owner needs them taken. Each step downward is a layer (one
kind of artefact of the chain).

The layers stand as follows:

- The [BRD](../reference/glossary.md) exists.
- The user stories exist. They stand below the BRD and above the
  [solution design](../reference/glossary.md). They break their
  parent into behaviour seen from the outside: what the user or the
  business sees happen, and under which conditions it is accepted.
- A layer for integration is intended.
- A strategy layer is possible, if it proves to make sense.

Which further layers are added, and in what order, is open. Nothing
further is approved for construction. The mechanics of a layer (its
commands, its agents and the calibration of its
[reviewers](../reference/glossary.md)) are designed when that layer
is taken up, not in advance. The mechanics of the solution design
were designed in this way.

### The chain stays with one principal

The layers below the [assignment](../reference/glossary.md) grow in
the same project, by the same principal's hand. They grow when he
chooses to take his own thought further. A BRD is then his next
layer, not a deliverable of someone else.

What a recipient does with an assignment is a forge run of his own,
in an instance of his own (an instance is one installation of the
forge). There the assignment becomes his
[brief](../reference/glossary.md). Today he does this by hand. An
assignment is self-contained for exactly that. A command of its own
for the step is left for a later day.

The chain never spans two principals.

### A new kind of artefact by one command

A new kind of artefact is added to the forge by one command:

```
/new-artefact <name>
```

The command leads to everything a kind needs and forgets none of it.
It decides nothing: how the kind is composed is the principal's
choice, as for any artefact. How a layer is added is told on
[The document chain](the-document-chain.md).

For now the command adds to the engine, for every user of it. A user
of the forge is to be able to add an artefact of his own as easily,
kept at his own place. Where that place is has not been decided.

The command adds a kind of artefact and no other type. A whole chain,
a reviewer and a [genre](../reference/glossary.md) are not added by
it.

### Reviewers on another model family

Today a model of another family is reached for research. The
mechanics of that link are built for the research. The link as it
stands is told on [Another model family](another-model-family.md).
Reviewers on the link are intended and not yet built.

The intent is that a [challenger](../reference/glossary.md) persona
and a [critic](../reference/glossary.md) lens may be sent to a model
of another family over the same link. The intended shape:

- What is sent is composed of the forge's own persona and
  [contract](../reference/glossary.md).
- The other model reads the project from disk, as a subagent does (a
  subagent is an isolated run of Claude that reads its inputs from
  disk).
- The report is scanned for instance values (facts of one
  installation) and checked for its shape.
- The command that sent the reviewer then numbers the report and
  files it unchanged.
- The other model is named at the call.

### What is not promised

- No destination and no deadline is named.
- Sponsorship, funding, adoption and delivery outcomes are outside
  the scope of the forge and outside its sight.
- The forge may one day feed a delivery chain. Whether a delivery
  side would be grown layers of the forge or a separate framework is
  deliberately undecided.

Experience from use returns to the forge as input like any other,
through its owner.

### How it is developed

The forge is developed at its owner's discretion and pace, by his
needs and by the feedback its use returns.

The forge is open to those who use it. What it wants of them most is
feedback and ideas. A finished change is welcome too, on the forge's
own rule:

- A change of how the forge behaves goes through the chain before it
  is built.
- A document that is a [render](../reference/glossary.md) is changed
  through its [recipe](../reference/glossary.md).
- Nobody sends a change he has not tried himself.

What enters the forge stays its owner's decision. How a change
reaches the forge is told on
[Make a change to the forge](../extend/how-a-change-is-made.md).

## Why

**No destination and no deadline.** The forge is developed at its
owner's discretion and pace, by his needs and by the feedback its use
returns. On those terms a direction may be named, and a destination
or a deadline is not.

**Only as far as a thought needs to be taken.** A forge run ends
where the principal is satisfied. The outcome is an artefact he
stands behind, and nothing further.

**One command for a new kind.** The purpose is that the chain grows
without anyone having to know by heart what a kind of artefact is
made of. The reason is that a kind added by hand takes a search for
everything it touches. Two of the things a kind needs (a prefix for
its items and a challenger of its own) are easily forgotten.

**Reviewers on another model family.** The purpose is that a
challenge can send in a lens with genuinely different priors.

**A self-contained assignment.** An assignment is self-contained. The
purpose is that a recipient can make it his brief by his own hand.

The reason is not recorded for these:

- why the mechanics of a layer are designed only when the layer is
  taken up
- why the chain never spans two principals
- why the question of a delivery side is deliberately left undecided

## A worked example

A principal has taken a thought as far as an assignment. The thought
can go further in two ways, and the two never join into one chain.

```
the principal's instance          the recipient's instance

assignment  ---- by hand ---->    brief
BRD                               (a forge run of his own)
user stories
solution design
```

- The principal takes his own thought further. The BRD is his next
  layer, in the same project and by his own hand. The user stories
  stand below the BRD, and the solution design below them.
- A recipient takes the assignment up in his own instance. The
  assignment becomes his brief, by his own hand. What follows is his
  own forge run.

Each chain stays with its principal.

## See also

- [The document chain](the-document-chain.md): how a layer is added.
- [Another model family](another-model-family.md): the link to
  another model family as it stands.
- [Projects and the engine](projects-and-the-engine.md): the engine
  and the projects as they are today.
- [Make a change to the forge](../extend/how-a-change-is-made.md): how
  a change reaches the forge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
