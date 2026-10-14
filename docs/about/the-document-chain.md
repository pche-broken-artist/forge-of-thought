---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: d7f1f1ef21055ad5
inputs:
  - CLAUDE.md#What this workspace is
  - CLAUDE.md#Document chain
  - .claude/skills/forge/SKILL.md
  - .claude/skills/forge/states/brief.md#Inputs
  - .claude/skills/forge/states/intent.md#Inputs
  - .claude/skills/forge/states/assignment.md#Inputs
  - .claude/skills/forge/states/solution-design.md#Inputs
  - projects/forge/10-intent.md#POS.0100
  - projects/forge/10-intent.md#POS.0140
  - projects/forge/10-intent.md#POS.0580
  - projects/forge/10-intent.md#POS.0700
  - projects/forge/10-intent.md#POS.1400
---

# The document chain

The document chain is the series of versioned documents through
which one idea travels in a project, from the idea put together to
as far as the project needs it taken. This page says what the chain
is, how it is worked and how it grows, and why it is built as a star
of definitions rather than as a fixed line. It is for anyone who
uses the forge, anyone who wants to extend it with a layer, and
anyone who evaluates its design.

## What it is

The chain is made of artefacts. An artefact is a document of the
chain, composed by the principal (the person whose thinking is
being forged) together with Claude, versioned and rewritten freely.
Every other file of a project is a document of another kind: a
record, a state file, a render or a resource. The chain is where the
thinking stands; a render is generated from it and is never a source
of truth.

A chain starts at a brief and its trunk is the intent. The
[brief](the-brief.md) is the principal's text of one whole of
thinking, put together. The [intent](the-intent.md) is what the
principal holds, chiselled out of the briefs. Below the intent a
project takes the layers it needs. Many projects end at the intent.

Every artefact has a definition. A definition is the state file
`.claude/skills/forge/states/<state>.md`, worked through
`/forge <state>` and paired with the artefact's template. The
definition says what the artefact is and how it is found, by
questions, by research and by sources, and it owns the artefact's
rules; the template says what comes out. What a definition is and
how it is walked is said on [Elicitation](elicitation.md).

Which artefacts the forge has is the listing of that directory, one
definition each. They are listed nowhere else. The table of
artefacts in the README is rendered from the definitions, and the
definitions of today stand one row each on
[Artefacts](../reference/artefacts.md).

In a project the artefacts are files named `NN-<artefact>.md`,
numbered in tens:

- `00-brief.md`: the brief, with any later brief as
  `00-brief-<name>.md`
- `10-intent.md`: the intent
- `20-assignment.md`: the assignment, what is handed to the
  recipients
- `40-solution-design.md`: the solution design, how the things
  wanted are realised

Beside every artefact stands its history companion
`<file>.history.md`, append-only. Beside the chain stand
`decisions.md`, the append-only record of the principal's decisions,
and `ledger.md`, the ledger: the single source of truth for the
state of the project. The project's open threads, the matters still
to elicit, live in `threads.md`.

Nothing is implemented in the forge; the engine specifies. From the
artefacts of the chain the thing must be buildable without a look at
the finished product. How deep the chain must go for that is the
project's own matter: the solution design gives the architecture,
and a technical specification gives the detail where the one who
builds needs it.

## How it works

Work on the chain is invoked by target state, never by verb:
`/forge intent`, `/forge assignment`. Bare `/forge` reports the
state map of a project: which artefacts exist, at what version and
status, which target states can be worked from here because their
inputs exist, and which cannot yet. `/forge <state>` resolves the
definition of that state, reads it and follows it. The definition
declares the target artefact, its inputs and its working rules;
everything else, such as one write per round, versioning and the
upkeep of the ledger, follows the shared conventions of the forge.
Where no definition of that name exists, the command lists the
states that do and stops.

The command that dispatches never changes. What changes, when the
forge grows, is the set of definitions it dispatches to.

Each definition declares its own inputs. This is what makes the
chain a star rather than a fixed line: every artefact names the
artefacts it is derived from, and no central list says what follows
what. The inputs of the definitions of today are these.

- The brief takes the principal's thought, however it arrives, and
  around it what was gathered during the elicitation: research
  notes in `research/`, sources in `sources/` and Claude's own
  proposals. The existing intent and the ledger are read only to
  know what already stands, never to shape the text.
- The intent takes the briefs the principal says to mine, approved
  or not, `decisions.md` and the ledger; sources only as the
  principal directs. The intent as it stands is read with the
  project's threads.
- The assignment takes `10-intent.md`, `decisions.md` and the
  ledger. The intent is read with the project's threads.
- The solution design takes the lowest layer the project has above
  it, that is the intent alone or the assignment, and whatever
  stands above that; `decisions.md` and the ledger. The intent is
  read with the project's threads. Where the thing already exists,
  what realises it is read as it stands. Research and sources are
  read as the principal directs.

The diagram shows the artefacts of today's chain with their inputs
as the definitions declare them. An arrow runs from an input to the
artefact derived from it.

```
 the principal's thought
 research/   sources/   Claude's proposals
            |
            v
      00-brief.md  (00-brief-<name>.md)
            |
            |  the briefs the principal says to mine;
            |  decisions.md, ledger.md; sources as directed
            v
      10-intent.md  (read with threads.md) -------------+
            |                                           |
            |  10-intent.md; decisions.md, ledger.md    |  the intent alone,
            v                                           |  where the project
      20-assignment.md                                  |  has no assignment
            |                                           |
            |  the lowest layer above; decisions.md,    |
            |  ledger.md; what realises the thing       |
            v                                           |
      40-solution-design.md <---------------------------+
```

No layer below the intent is a condition of another. A project
takes the layers it needs. A layer a project does not have is not
missing: `/forge` and the checks say nothing of it, and the ledger
declares no end of the chain. The number in a file name orders the
files and prescribes no sequence.

The chain grows by adding one definition. Because each definition
declares its own inputs, a future layer branches from any artefact,
and nothing that exists is reworked: no definition changes, the
dispatcher does not change, and no file is renamed. The gaps of ten
in the numbering leave room for the new layer's file. Which layers
are added, and in what order, is open; the mechanics of a layer are
designed when that layer is taken up, not in advance.

Substance changes go into the intent first and propagate from there
down the whole chain the project has: each lower layer is brought
to the intent. Only wording is fixed in a lower layer directly. A
change may come from below. When solving shows that what is wanted
cannot be had, or must be wanted differently, the intent changes
first and the layers follow. If the principal dictates substance
straight into a lower layer, the matching update of the intent is
proposed in the same step.

The chain never spans two principals. The recipients of an
assignment may be teams, colleagues or the principal's future self.
What a recipient does with an assignment in his own instance is his
own run of the forge: the assignment becomes his brief, by his own
hand. The layers below the assignment grow in the same project, by
the same principal's hand, when he chooses to take his own thought
further.

## Why

The files are numbered in tens so that later layers can be added
without renaming anything that exists.

Work is invoked by target state so that knowing the name of the
target artefact is knowing the command. Nothing is to be memorised as
layers are added.

Each definition declares its own inputs so that a future layer
branches from any artefact by adding one definition. The dispatcher
stays as it is.

No layer below the intent is a condition of another because many
projects end at the intent, where what is wanted needs no solution
written down. A solution design is worth writing where the way is
not obvious, where a choice has a price, or where two hands would
solve the same matter differently if it were not written down;
whether it is written, the principal says.

The reason why substance changes go into the intent first is not
recorded in the inputs of this page beyond what the definitions
give: the assignment carries the in-scope substance of the intent,
and the solution design is derived from the lowest layer above it.

The reason why the artefacts are listed in the definitions directory
alone and nowhere else is not recorded in the inputs of this page.

The reason why the chain never spans two principals is not recorded
in the inputs of this page beyond this: an assignment is
self-contained so that a recipient can make it the brief of his own
run.

## A worked example

A project `projects/<slug>/` begins with `00-brief.md`, the
principal's thought put together after a round of research. Through
`/forge intent` the brief is mined into `10-intent.md`, with the
open matters in `threads.md`. The principal decides that a team is
to carry the matter out and works `/forge assignment`, which reads
`10-intent.md`, `decisions.md` and the ledger and produces
`20-assignment.md`. Later he finds that the way is not obvious and
works `/forge solution-design`, which takes the assignment as the
lowest layer above it, with the intent above that, and produces
`40-solution-design.md`.

A second project `projects/<other-slug>/` ends at the intent: what
is wanted needs no solution written down, and bare `/forge` reports
no assignment and no solution design as missing. A third project
has an intent and no assignment, because nothing is handed to
anyone; its `/forge solution-design` takes the intent alone as its
input, and the chain is intent, then solution design.

When a change of substance arises in the first project while the
solution design is being worked, the intent is changed first, and
the assignment and the solution design are then brought to it; a
mere wording fix stays in the layer where it is found.

## See also

- [The brief](the-brief.md): the first artefact.
- [The intent](the-intent.md): the trunk.
- [Elicitation](elicitation.md): what a definition is.
- [Artefacts](../reference/artefacts.md): the definitions of today, one row each.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
