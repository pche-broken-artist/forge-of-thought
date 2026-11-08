---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 5eddaee630c23e2b
inputs:
  - projects/forge/10-intent.md#POS.0700
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1430
  - projects/forge/10-intent.md#POS.1440
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/10-intent.md#POS.1990
---

# Where the forge is going

The forge is developed in a direction, not toward a destination: the
direction is named, destinations and deadlines are not. This page is
for a user who wants to know what to expect, for an extender who
wants to know what is open, and for an evaluator who wants to know
what is deliberately not promised. It says in which direction the
forge is developed, what is intended and not yet built, and where
the forge stops on purpose.

## What it is

The forge is a general tool for forging thoughts. A run of the forge
ends where its owner is satisfied. The outcome is an artefact the
principal (the one whose thinking is forged) stands behind, and
nothing further. An intent may be immaterial and carry no delivery
at all. The mechanics of the [document chain](the-document-chain.md)
are domain-agnostic: the same machinery that forges a platform
assignment would forge a role-playing campaign, an intent of the
story and then materials rendered for the game master.

Sponsorship, funding, adoption and delivery outcomes are outside the
forge's scope and outside its sight. The door is open, not closed:
the forge may one day feed a delivery chain. Whether such a delivery
side would be grown layers of the forge or a separate framework is
deliberately undecided. Experience from use flows back through the
ordinary door, the principal, by `/forge intent`, as input like any
other.

The forge is developed at the principal's discretion and pace, by his
needs and by the feedback it returns. A direction may be named. A
destination or a deadline is not.

## How it works

### The chain is extended downward

The chain is extended downward as far as the principal needs a
thought taken. Below the intent and the assignment the layers that
exist today are these:

- the BRD, the business requirements document;
- the user stories, below the BRD and above the solution design;
- the solution design.

Integration is intended. A strategy layer is possible if it proves to
make sense. Which layers are added, and in what order, is open:
possibly all of these, possibly none yet. Nothing is approved for
construction. The mechanics of a layer, its commands, its agents and
the calibration of its reviewers, are designed when that layer is
actually taken up, not in advance, as the solution design's were.

The layers below the assignment grow in the same project, by the same
principal's hand, when he chooses to take his own thought further: a
BRD as his next layer, not as someone else's deliverable. What a
recipient does with an assignment in his own instance (one
installation of the forge) is his own forge run. The assignment
becomes his brief, by his hand today, by a command of its own only
when that day comes. The chain never spans two principals.

### A new kind of artefact is added by one command

A new kind of artefact is added to the forge by one command,
`/new-artefact <name>`, so that the chain grows without anyone having
to know by heart what a kind of artefact is made of. The command
leads to everything a kind needs and forgets none of it:

- what the artefact is, for whom, from what it is derived and why,
  held as a position of the forge's intent before anything is built;
- its definition (its state file) and its template (its skeleton) as
  a pair;
- the prefixes of its items, where it needs its own;
- whether it needs a challenger of its own, and what the critic must
  know of it;
- where it is realised, in the solution design.

The command decides nothing. How the kind is composed is the
principal's choice, as for any artefact, and each of these is born on
his word. The first artefact of the new kind is not the command's: it
is made through `/forge <name>` on real work, and that is the trial of
the definition. Where the kind needs a trial on real work before its
position can hold, the order is the brief first, then the pair built
with its reviewers and tried, then the position and the item of the
design.

For now the command adds to the engine, for every user of it. A user
is to be able to add an artefact of his own as easily, kept at his
own place. Where that place is remains open. Types other than an
artefact, such as a whole chain, a reviewer or a genre, are not this
command's.

### Reviewers on another model family

A model of another family is reached today for research; what that
link is and how it stands is said on
[Another model family](another-model-family.md). A challenger
persona, and a critic lens, may be sent to another engine over the
same link, so that `/challenge` can send in a lens with genuinely
different priors. What is composed is the forge's own persona and
contract. The engine on the other side reads the project from disk,
as a subagent (an isolated agent that never sees the working
conversation) does. The report is scanned for instance values and
checked for its shape before the command numbers and files it
unchanged. The engine is named at the call. The direction holds. The
mechanics are built for the research; the reviewers on the link are
intended and not yet built.

### The forge's own project becomes a repository of its own

The forge's own project is to become one project among the others,
under git like them, in a repository of its own beside the engine;
what the engine and the projects are today is said on
[Projects and the engine](projects-and-the-engine.md). Today the
engine still tracks it.

Once cut, a user clones the engine alone, and nothing he runs reads
the project: the tests, the status, the ledger (the project's single
source of state, made at read time), the light check of a project and
both hooks run unchanged without it. A contributor, and the principal
on another machine, clone the project beside the engine, since the
author's commands read it:

- `/check engine`;
- `/document`;
- `/release forge`;
- `/new-artefact`;
- the renders of the README, the release notes and CONTRIBUTING.

The paths `projects/forge/...` that the documentation cites are the
paths of that clone, and the README says where the project lives.

What stays special is in the recipes, not in the scripts. The
project's root renders land in the engine root by their `output:`
path, so a release of the engine lands in two commits, and the ledger
reads where a root render lies from the recipe. In the commands of
git (`/save`, `/pull`, `forge-branch` and `/release`) `forge` names
the whole: the engine's repository and the project beside it where it
is cloned, each its own commit with the prefix `forge:`. In the
commands over documents `forge` is the project.

The repository starts clean, with one commit naming the engine commit
it was cut from; the history before it is the engine's. The order of
the cut is decided: the engine is prepared with the project still
inside and the cut tried on a copy; the project's repository is born
before the engine lets the directory go; then comes the first release.

### Open to those who use it

The forge is open to those who use it. What it wants of them most is
feedback and ideas. A finished change is welcome too, on the forge's
own rule:

- a change of how the forge behaves goes through the chain before it
  is built;
- a document that is a render changes through its recipe;
- nobody sends a change he has not tried himself.

How a change reaches the forge is said on
[Make a change to the forge](../extend/how-a-change-is-made.md).
What enters the forge stays the principal's decision.

## Why

A kind of artefact is added by one command because a kind added by
hand took a search for everything it touches. Two of the things a
kind needs, a prefix and a challenger, are easily forgotten.

Reviewers are to be sent over the link to another model family so
that `/challenge` can send in a lens with genuinely different priors.

The forge's own project is cloned beside the engine by a contributor
because the author's commands read it. A user who clones the engine
alone needs none of it, since nothing he runs reads the project.

Why the mechanics of a layer are designed only when the layer is
taken up, and not in advance, is not recorded beyond the precedent of
the solution design. Why the chain never spans two principals is not
recorded. Why the forge is developed at the principal's discretion
and pace, with no destination promised, is not recorded.

## See also

- [The document chain](the-document-chain.md): how a layer is added.
- [Another model family](another-model-family.md): the link to
  another model family as it stands.
- [Projects and the engine](projects-and-the-engine.md): the engine
  and the projects as they are today.
- [Make a change to the forge](../extend/how-a-change-is-made.md):
  how a change reaches the forge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
