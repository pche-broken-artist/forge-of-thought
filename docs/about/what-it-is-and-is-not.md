---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 61f1d92dca5dabe7
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

Forge of Thought is a general engine for forging thoughts: a workshop
where a thought is tempered and shaped into documents its owner
stands behind. This page explains what the forge is, what it is
not, and why it is built and named as it is. It is written for
anyone who uses the forge, extends it or weighs whether to adopt
it.

## What it is

The forge is a place for forging thoughts. Any idea can enter it,
such as a process redesign, a platform initiative or an
organisational topic. The idea travels a chain of versioned
documents, from the idea put together onward. Isolated reviewers
put it under adversarial pressure along the way. A reviewer runs as
a subagent (a separate instance of Claude that is given only the
documents and never sees the working conversation).

The forge is bound to no person and to no management relationship.
The principal is whoever's thinking is being forged. Anyone can be
the principal. The recipients are whoever receives an assignment
made in the forge: a team, colleagues or the principal's own future
self. The forge began as one person's tool. That origin is now a
fact of one instance (one installation of the forge), not a
property of the system.

Claude is the principal's cognitive extension, not a supplier. It
owns structure, order, process discipline and the hygiene of the
documents. The principal owns the content and every decision. The
two roles and the rule between them are described in
[The principal and Claude](the-principal-and-claude.md).

## How it works

Claude contributes to the content in four ways:

- it criticises;
- it challenges;
- it inspires;
- it lays out options.

The principal composes. He assembles what the forge offers into his
own positions and decisions. Nothing enters the content because
Claude proposed it. Something enters only because the principal took
it up. "Cognitive extension" therefore means an amplifier of the
principal's thinking, never its substitute.

The trunk of every chain is the intent (the document of what the
principal holds; this term and the others of the forge are in the
[Glossary](../reference/glossary.md)). Below the intent a project
takes the layers it needs, and many projects end at the intent. The
chain grows by adding the definition of a new layer, without
reworking anything that exists. The course of one thought through
these documents is described in
[How a thought travels through the forge](how-a-thought-travels.md).

## What it is not

- **Not a program.** Nothing is implemented in the forge. The
  engine specifies.
- **Not a delivery tool.** A run ends where its owner is satisfied.
  The outcome is an artefact the principal stands behind, and
  nothing further. Sponsorship, funding, adoption and delivery
  outcomes are outside the forge's scope and outside its sight.
- **Not a chat.** State lives in files, never only in the
  conversation. What is in a file survives the session (one working
  conversation with Claude). What lives only in the conversation
  does not.
- **Not tied to one domain.** The mechanics of the chain are the
  same for any subject. The machinery that forges a platform
  assignment would equally forge a tabletop role-playing campaign:
  an intent of the story, then materials made from it for the game
  master. An intent may be immaterial and carry no delivery at all.

The door to delivery is left open, not closed. The forge may one day
feed a delivery chain. Whether that delivery side would be further
layers of the forge or a separate framework is deliberately left
undecided. The direction the forge is developed in is described in
[Where the forge is going](where-it-is-going.md).

## Why

**Why a general engine.** The forge was once framed as one person's
tool for briefing the people who report to him. That framing was
dropped as the identity of the system. The reason is that it
describes the first instance, not the engine.

**Why the name.** Thoughts are the raw material, of whatever kind,
and nothing is presumed about them. Forged artefacts are the
product, and an assignment is one of them. The name was chosen with
the full chain in mind: from an assignment through a business
requirements document and an architecture to a deck ready for
realisation. The full name stands in documents. The short form
"Forge" is expected in daily speech.

Other names were considered and turned down:

- "Cascade": it literally names the waterfall.
- "Foundry": it collides with existing products of that name.
- "Continuum", "Strata", "Idea Forge" and a name in another
  language: considered; why each was not chosen is not recorded.

**Why "thought" and not "assignment".** An assignment is one place
a chain may end, not the goal. So every subtitle or one-line
description presents the forge as a place where thoughts are
forged, never with the assignment as its goal. The subtitle reads:
"*A workshop where thought is tempered and shaped.*"

**Why the chain ends where the project needs it to.** The primary
ambition is the full chain, from a raw idea to a specification
ready for implementation, grown layer by layer. A run still ends
where its owner is satisfied. The reason is that the outcome is an
artefact the principal stands behind, and nothing further. Every
design decision is made with the growth of the chain in mind. That
is why files and IDs are numbered with gaps. The gaps let a layer
be added without renumbering anything.

## A worked example

A principal wants to settle how a small team runs its weekly
planning. She brings the idea, and it is put together as a brief.
With Claude she works it into an intent: what she holds about the
meeting, what she has rejected and why. Claude asks, challenges and
lays out options. She decides what enters. An isolated reviewer
reads the intent cold and points out where it is unclear.

At that point she is satisfied. The intent says what she wants, and
she means to run the planning herself. The chain ends there, at the
intent, with no assignment and no layer below it. Nothing is
missing: the run ended where its owner was satisfied. Had she wanted
to hand the work to another team, she would have taken an
assignment as the next layer, and the chain would have ended there
instead.

## See also

- [How a thought travels through the forge](how-a-thought-travels.md): the course of one thought through the forge.
- [The principal and Claude](the-principal-and-claude.md): the two roles and the rule between them.
- [Where the forge is going](where-it-is-going.md): the direction the forge is developed in.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
