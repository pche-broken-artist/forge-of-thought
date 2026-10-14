---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 9c882fc925998394
inputs:
  - projects/forge/10-intent.md#POS.0700
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1110
  - projects/forge/10-intent.md#POS.1430
  - projects/forge/10-intent.md#POS.1440
---

# Where the forge is going

The direction of the forge is a direction without a destination: the
chain of documents is to grow downward as far as the principal (the
person whose thinking is forged) needs a thought taken, and nothing
beyond that is promised. This page says, for the user, the extender
and the evaluator, which way the forge is developed, what is planned,
what is deliberately left open and what is not promised at all.

## What it is

The forge is a general tool for forging thoughts. A forge run ends
where its owner is satisfied. The outcome is an artefact the
principal stands behind, and nothing further. An intent may be
immaterial and carry no delivery at all. The mechanics of the
[chain](the-document-chain.md) know no domain: the same machinery
that forges an assignment for a platform would forge the campaign of
a tabletop game, as an intent of the story and then materials
rendered for the game master.

Sponsorship, funding, adoption and delivery outcomes are outside the
forge's scope and outside its sight. A direction may be named.
Destinations and deadlines are not.

## How it works

### The chain grows downward

The engine is extended downward: a thought is forged as far as the
principal needs it taken. Three layers are in view:

- a BRD layer, which is certain to come;
- integration, which is intended;
- a strategy layer, which is possible if it proves to make sense.

Which of these layers are added, and in what order, is open: possibly
all of them, possibly none yet. Nothing is approved for construction.
The mechanics of a layer (its commands, its agents, the calibration
of its reviewers) are designed when that layer is actually taken up,
not in advance. How a layer is added to the chain is said on
[The document chain](the-document-chain.md).

The layers below the assignment grow in the same project, by the
same principal's hand, when he chooses to take his own thought
further: a BRD as his next layer, not as someone else's deliverable.
What a recipient does with an assignment in his own instance is his
own forge run. The assignment becomes his brief, by his hand today.
An assignment is self-contained for exactly that. A command of its
own for that step comes only when that day comes. The chain never
spans two principals.

### A new kind of artefact by one command

A new kind of artefact is added to the forge by one command,
`/new-artefact <name>`. The command leads to everything a kind needs
and forgets none of it:

- what the artefact is, for whom, from what it is derived and why,
  held as a position of the forge intent before anything is built;
- its definition and its template, as a pair;
- the prefixes of its items, where it needs its own;
- whether it needs a challenger of its own, and what the critic must
  know of it;
- where it is realised, in the solution design.

The command decides nothing. How the kind is composed is the
principal's choice, as for any artefact, and each of these parts is
born on his word. The first artefact of the new kind is not the
command's: it is made through `/forge <name>` on real work, and that
is the trial of the definition.

For now the command adds to the engine, for every user of it. A user
is to be able to add an artefact of his own as easily, kept at his
own place. Where that place is remains open. Types other than an
artefact (a whole chain, a reviewer, a genre) are not this command's.

### Independent challengers

Independent challengers are planned: challenger personas running on
a different model family than the author's, composed by the
principal outside the forge and invoked from it over a command-line
link. A challenger is a reviewer that runs as an isolated subagent (a
separate run that never sees the working conversation). The
direction is decided. The mechanics are designed when the work is
taken up.

### One principal per instance

The forge stays a single-user tool per instance (one installation).
More people means more instances, and coordination between them is
git's. Branches are voluntary and belong to git. Whoever wants one
gets it through one forge command and never types git; merging and
conflicts stay git's, by hand or by merge request. Nothing forces a
branch: whoever does not use them works on `main`, saves, now and
then releases, and sees none of this. One hole is known and left
until it happens: two parallel branches taking the same next free ID,
which the checks of a release find after the merge.

### The door stays open

The forge may one day feed a delivery chain. Experience from use
flows back through the ordinary door, the principal via
`/forge intent`, as input like any other. Whether a delivery side
would be grown layers of the forge or a separate framework is
deliberately undecided.

### Developed at its owner's discretion and pace

The forge is developed at the principal's discretion and pace, by his
needs and by the feedback its use returns. It is open to those who
use it. What it wants of them most is feedback and ideas. A finished
change is welcome too, on the forge's own rule:

- a change of how the forge behaves goes through the chain before it
  is built;
- a document that is a render changes through its recipe;
- nobody sends a change he has not tried himself.

How a change reaches the forge is said on
[Make a change to the forge](../extend/how-a-change-is-made.md).
What enters the forge stays the principal's decision.

## Why

The reasons the inputs give, and the places where none is recorded:

- A new kind of artefact is added by one command because a kind added
  by hand took a search for everything it touches, and two of the
  things it needs, a prefix and a challenger, are easily forgotten.
- Independent challengers are to run on another model family so that
  `/challenge` can send in a lens with genuinely different priors.
- The mechanics of a layer are designed when the layer is taken up.
  The inputs record the precedent, the solution design's mechanics
  were designed in the same way, and no further reason.
- An assignment is self-contained so that a recipient can make it his
  brief by his own hand.
- Why destinations and deadlines are not named, and why the forge is
  developed at its owner's discretion and pace: the reason is not
  recorded.
- Why the forge stays a single-user tool per instance: the reason is
  not recorded.
- Why the chain never spans two principals: the reason is not
  recorded.
- Why feedback and ideas are wanted most: the reason is not recorded.
- Why sponsorship, funding, adoption and delivery outcomes are
  outside the forge's sight: the reason is not recorded.

## See also

- [The document chain](the-document-chain.md): how a layer is added.
- [Make a change to the forge](../extend/how-a-change-is-made.md):
  how a change reaches the forge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
