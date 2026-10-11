---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: e1264a539b072480
inputs:
  - projects/forge/10-intent.md#POS.0700
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1110
  - projects/forge/10-intent.md#POS.1430
  - projects/forge/10-intent.md#POS.1440
---

# Where the forge is going

The direction of the forge is the way its owner intends to develop
it: the chain extended downward as far as a thought needs taking, a
new kind of artefact added by one command, challengers on another
model family, one principal per instance, and nothing promised
beyond that. This page is for anyone who uses the forge, extends it
or evaluates it and wants to know what is intended, what is
deliberately left open and what is not promised. It names a
direction, not destinations.

## What it is

The forge is a general tool for forging thoughts. A forge run ends
where its owner is satisfied. The outcome is an artefact (a document
of the chain) that the principal stands behind, and nothing further.
The principal is the person whose thinking is forged; Claude is his
cognitive extension, and it proposes and never decides.

The direction of the forge is named. Its destinations and deadlines
are not. The forge is developed at the principal's discretion and
pace, by his needs and by the feedback that its use returns. Nothing
on this page is approved for construction: it says where the work
points, not when or whether a given piece arrives.

## How it works

### The chain grows downward

The chain is the series of versioned documents a thought travels,
from the brief through the intent to whatever layers the project
takes below it. The principal intends to keep extending the chain
downward: thoughts are forged as far as he needs them taken. The
layers in view are these:

- a BRD layer: certain to come
- integration: intended
- a strategy layer: possible, if it proves to make sense

Which layers are added, and in what order, is open: possibly all of
these, possibly none yet. Nothing is approved for construction. The
mechanics of a layer (its commands, its agents, the calibration of
its reviewers) are designed when that layer is actually taken up,
not in advance. The solution design's mechanics were designed the
same way. The reason why the mechanics wait for the layer is not
recorded.

The layers below the assignment grow in the same project, by the
same principal's hand, when he chooses to take his own thought
further: a BRD as his next layer, not as someone else's
deliverable. What a recipient does with an assignment in his own
instance is his own forge run. The assignment becomes his brief, by
his hand today. An assignment is self-contained for exactly that. A
command for this hand-over is foreseen only when that day comes.
The chain never spans two principals.

How a layer is added to the chain is said on
[The document chain](the-document-chain.md).

### A new kind of artefact by one command

A new kind of artefact is added to the forge by one command,
`/new-artefact <name>`. The command leads to everything a kind needs
and forgets none of it:

- what the artefact is, for whom, from what it is derived and why,
  held as a position of the forge's own intent before anything is
  built
- its definition (the state file that says how the artefact is
  found) and its template as a pair
- the prefixes of its items, where it needs its own
- whether it needs a challenger of its own, and what the critic
  must know of it
- where it is realised, in the solution design

The command decides nothing. How the kind is composed is the
principal's choice, as for any artefact, and each of these pieces
is born on his word. The first artefact of the new kind is not the
command's: it is made through `/forge <name>` on real work, and that
is the trial of the definition.

For now the command adds to the engine, for every user of it. A
user is to be able to add an artefact of his own as easily, kept at
his own place. Where that place is remains open. Other types that
the forge can be extended by (a whole chain, a reviewer, a genre)
are not this command's.

### Independent challengers

A challenger is an isolated reviewer that goes after the substance
of the thinking, never the quality of the document. Independent
challengers are planned: challenger personas running on a different
model family than the author's, composed by the principal outside
the forge and invoked from the forge over a command-line link, so
that `/challenge` can send in a lens with genuinely different
priors. The direction is decided. The mechanics are designed when
the work is taken up.

### One principal per instance

An instance is one installation of the forge. The forge stays a
single-user tool per instance. More people means more instances,
with coordination between them left to git. Branches are voluntary
and belong to git: whoever wants one gets it through one forge
command, and whoever does not use them works on `main`. The reason
why one instance serves one principal is not recorded.

### Where a forge run ends

An intent may be immaterial and carry no delivery at all. The
mechanics of the chain are domain-agnostic: the same machinery that
forges a platform assignment would forge a role-playing campaign,
as an intent of the story and then materials rendered for the game
master. Sponsorship, funding, adoption and delivery outcomes are
outside the forge's scope and outside its sight.

That door stays open, not closed. The forge may one day feed a
delivery chain. Experience from use flows back through the ordinary
door, the principal, via `/forge intent`, as input like any other.
Whether a delivery side would be grown as layers of the forge or as
a separate framework is deliberately undecided.

### What is asked of those who use it

The forge is open to those who use it. What it wants of them most
is feedback and ideas. A finished change is welcome too, on the
forge's own rule:

- a change of how the forge behaves goes through the chain before
  it is built
- a document that is a render is changed through its recipe
- nobody sends a change he has not tried himself

What enters the forge stays the principal's decision. How a change
reaches the forge is said on
[Make a change to the forge](../extend/how-a-change-is-made.md).

## Why

The direction is named and the destinations are not, because the
forge is developed at the principal's discretion and pace, by his
needs and by the feedback that its use returns.

A kind of artefact is added by one command because a kind added by
hand took a search for everything it touches, and two of the things
it needs, a prefix and a challenger, are easily forgotten. The
command exists so that the chain grows without anyone having to
know by heart what a kind of artefact is made of.

Challengers on another model family are planned so that
`/challenge` can send in a lens with genuinely different priors.

The reason why the mechanics of a layer are designed only when the
layer is taken up is not recorded. The reason why one instance
serves one principal is not recorded.

## See also

- [The document chain](the-document-chain.md): how a layer is added.
- [Make a change to the forge](../extend/how-a-change-is-made.md):
  how a change reaches the forge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
