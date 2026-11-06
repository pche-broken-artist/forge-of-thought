---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 759e9eb9492a1024
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

Forge of Thought is a place for forging thoughts: a workshop where a
thought is tempered and shaped into documents someone can stand
behind. This page says what the forge is, what it is not, and why it
was made this way. It is for anyone who meets the forge for the first
time, whether to use it, to extend it or to judge it, and it assumes
nothing read before it.

## What it is

The forge is a general engine for forging any thought. An idea of any
kind travels a [chain](../reference/glossary.md) of versioned
documents, from the idea put together onward, under review by
isolated reviewers. The subject matter is deliberately
unconstrained: a process redesign, a platform initiative, an
organisational topic, a story, anything. Nothing is presumed about a
thought before it arrives.

The forge is bound to no person and to no management relationship.
The principal, that is, whoever's thinking is being forged, can be
anyone. The recipients, whoever receives what the forge produces,
may be teams, colleagues or the principal's future self. Who the
principal of one installation is, what language his conversation
runs in and the handle he signs records with are facts of that
installation, an instance. They live in a file of the instance,
`CLAUDE.local.md`, and not in the system. The forge began as one
person's tool. That origin is an instance fact, not the system.

Claude is the principal's cognitive extension. The phrase means an
amplifier of the principal's thinking, never its substitute. Claude
owns structure, order, process discipline and document hygiene. The
principal owns the content and every decision. Claude's contribution
to content is to criticise, to challenge, to inspire and to lay out
options. The composition is the principal's. Nothing enters the
content because Claude proposed it, only because the principal took
it up. Claude proposes and never decides. The two roles and the rule
between them are on
[The principal and Claude](the-principal-and-claude.md).

## How it works

A thought enters as a brief, a few sentences of what the principal
wants. From it the
[intent](../reference/glossary.md) is found, the trunk of every
project: the positions the principal holds, with stable identifiers,
so that a position can be cited and revisited without being
restated. Below the intent a project takes the layers it needs. An
[assignment](../reference/glossary.md) is one such layer, a document
that hands the full substance of the intent to the recipients. A
business requirements document and a solution design are further
layers, where a project needs them. The chain grows by adding the
definition of a layer, without reworking anything that exists. The
course of one thought along this chain is on
[How a thought travels through the forge](how-a-thought-travels.md).

Pressure on the thinking comes from isolated reviewers. Each is a
subagent, that is, a separate run of Claude that reads the project's
documents from disk and never sees the working conversation. Because
the reviewers are blind to the conversation, they press on the
documents from angles the conversation did not take.

State lives in files, never only in the conversation. What is in a
file survives the session, that is, one sitting of the conversation
with Claude. What lives only in the conversation does not survive
it. One project per session is the hygienic default.

A forge run ends where its owner is satisfied. The outcome is an
[artefact](../reference/glossary.md) the principal stands behind,
nothing further. An intent may be immaterial and carry no delivery at
all. Many projects end at the intent. Audience-specific outputs, such
as a summary for a team or a deck for a sponsor, are made from the
artefacts as renders. A render is generated and is never a source of
truth.

## What it is not

The forge is not a program. Nothing is implemented in it; the engine
specifies. It runs in Claude Code, the command-line agent of Claude,
and the mechanisms of Claude Code, its commands, skills, agents and
hooks, are what carry it. The forge is what those mechanisms are
told.

The forge is not a delivery tool. A run ends where its owner is
satisfied, with an artefact and nothing further. Sponsorship,
funding, adoption and delivery outcomes are outside the forge's scope
and outside its sight. The door is left open, not closed: the forge
may one day feed a delivery chain, and experience from use flows
back through the principal as input like any other. Whether such a
delivery side would be grown layers of the forge or a separate
framework is deliberately undecided.

The forge is not a chat. A conversation with Claude is where the
thinking happens, but what the conversation alone holds is nowhere
yet. The documents are the forge; the conversation is the way to
them.

The forge is not tied to one domain. The mechanics of the chain are
domain-agnostic. The same machinery that forges an assignment for a
platform would forge a tabletop role-playing campaign: an intent of
the story, then materials rendered for the game master.

The forge is not one person's briefing tool. The founding framing of
the system, a tool for one manager to brief his direct reports, was
dropped. Because it describes the first instance and not the engine,
it was superseded by the general-engine framing above.

## Why

**Why the name.** The system is named Forge of Thought. Thoughts are
the raw material, of whatever kind, with nothing presumed about them.
Forged artefacts are the product, an assignment among them. The name
was chosen with the full chain in mind, from assignment through
business requirements and solution design to a realisation deck.
Other names were weighed and rejected:

- "Cascade": it literally names the waterfall.
- "Foundry": it collides with existing product names.
- "Continuum", "Strata", "Idea Forge" and a name in the principal's
  own language were considered, and Forge of Thought was chosen.

In documents the full name is used; the short form "Forge" is
expected in daily speech. Any subtitle or one-line description must
present the forge as a place and space where thoughts are forged. The
subtitle of the engine's own README is "A workshop where thought is
tempered and shaped."

**Why "thought" and not "assignment".** An assignment is one place a
chain may end, not the goal. Because a description that named the
assignment as the goal would misstate what the forge is for, no
subtitle may name it so. The primary ambition is the full chain, from
a raw idea to a deck ready for realisation, growing layer by layer.
Every design decision was made with that growth in mind. That is why
files and identifiers are numbered with gaps, and why the name says
thought and not assignment.

**Why the chain ends where the project needs it to.** The outcome of
a run is an artefact the principal stands behind, and nothing beyond
it is the forge's business. An intent may carry no delivery at all,
so a layer below it that a project does not have is not missing.
Because the chain grows by adding the definition of a layer without
reworking what exists, a project can stop at any layer and continue
later. Where the forge is being taken from here is on
[Where the forge is going](where-it-is-going.md).

**Why Claude proposes and never decides.** The principal's thinking
is what is being forged. Were Claude to decide, the artefact would
carry Claude's positions and not the principal's, and the amplifier
would have become a substitute. The reason the principal owns every
decision is this one; a further reason is not recorded.

## A worked example

A principal, the head of a small support team, has a thought: the
hand-over between the morning and the evening shift keeps losing
cases. The thought is plainly invented here; it belongs to no project.

He writes a brief of a few sentences. With Claude he finds the
intent: what he wants the hand-over to achieve, what he holds to be
true about the shifts, what he will not change, and three open
matters he has not settled yet. The intent is a file in the project,
versioned, with stable identifiers on its positions. Two isolated
reviewers read it from disk and return findings: one presses on a
position that assumes the evening shift reads the morning's notes,
the other asks what happens on a day with no overlap. He settles
each, and the intent gets a new version. He is satisfied: the three
open matters are closed, and the positions say what he thinks.

The run ends there, at the intent. He needs no assignment, because
no one else is asked to do the work: he will run the new hand-over
himself. A render, a one-page summary for the team, is made from the
intent and put in front of them. Whether the hand-over then loses
fewer cases is outside the forge's sight. Had he wanted to hand the
work to a colleague, the project would have taken one more layer, an
assignment, and ended there instead.

## See also

- [How a thought travels through the forge](how-a-thought-travels.md): the course of one thought through the forge.
- [The principal and Claude](the-principal-and-claude.md): the two roles and the rule between them.
- [Where the forge is going](where-it-is-going.md): the direction the forge is developed in.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
