---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 9866486f9e862b7b
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

The document chain is the row of versioned documents a thought
travels in a project of Forge of Thought: it starts at a brief, its
trunk is the intent, and below the intent a project takes only the
layers it needs. This page says what the chain is, how a layer is
worked and how the chain grows, and why it is built as a set of
definitions that each name their own inputs rather than as a fixed
line. It is for the user who takes a project through the chain, for
the extender who adds a layer to it, and for the evaluator who wants
to know why the chain has the shape it has.

## What it is

Any idea can travel the chain: a process redesign, a platform
initiative, an organisational topic, anything. It travels from the
idea put together onward, under isolated adversarial review, that
is, reviewers that never see the working conversation. The chain is
not tied to one person or one management relationship. Anyone can be
the principal, the person whose thinking is forged, who supplies the
ideas, the answers and the decisions and is the final authority on
all content. The recipients of an assignment may be teams,
colleagues, or the principal's future self. Nothing is implemented
in the forge: the engine specifies.

The documents of the chain are its artefacts: each is composed by
the principal with Claude, versioned, and rewritten freely. A chain
starts at a brief, the artefact where the idea is put together
([The brief](the-brief.md)). Its trunk is the intent
([The intent](the-intent.md)): every lower layer derives from the
intent, directly or through the layers between. Below the intent a
project takes the layers it needs. No layer below the intent is a
condition of another. Many projects end at the intent. A layer a
project does not have is not missing: the state map of `/forge` and
the checks say nothing of it, and the ledger (the project's single
source of truth for state) declares no end of the chain.

Every artefact of the chain has a definition: its state file
`.claude/skills/forge/states/<state>.md`, paired with the artefact's
template. The definition says what the artefact is and how it is
found, by questions, research and sources, and it owns the
artefact's rules. The template says what comes out. How an artefact
is found by its definition is said in
[Elicitation](elicitation.md). Which artefacts the forge has is the
listing of that directory, one definition each. They are listed
nowhere else, and the table of artefacts in the README is rendered
from the definitions. Why the directory is the one listing is not
recorded. The definitions of today stand one row each in
[Artefacts](../reference/artefacts.md).

The files of a project's chain are laid out so that the chain can
grow without renaming anything:

```
NN-<artefact>.md   an artefact of the chain — versioned
<file>.history.md  history of each versioned document —
                   append-only companion beside it
decisions.md       append-only DEC records
ledger.md          single source of truth for state
```

The artefacts are numbered in tens: `00-brief.md`, `10-intent.md`,
`20-assignment.md`, `40-solution-design.md`. The gap of ten between
two numbers leaves room for a layer to be added between them without
renumbering. The number orders the files and prescribes no sequence
of work.

## How it works

### Working a layer

Work on the chain is invoked by the target state, never by a verb:
`/forge <state>`, as in `/forge intent` or `/forge assignment`.
Claude resolves the definition file of that state and follows it.
The definition declares the target artefact, its inputs and its
working rules. Everything else (one write per round, versioning, the
upkeep of the ledger) follows the common conventions of the forge.
Where no definition of that name exists, Claude lists the states
that do and stops.

Bare `/forge` reports the state map of a project. The map says which
artefacts exist, at what version and status; which target states
can be worked from here, because their inputs exist; and which
cannot yet, with what is missing. A layer the project does not have
is not reported as missing. The map ends with a recommendation of
the natural next step, in words, never a gate. The dispatcher behind
`/forge` never changes when a layer is added: it reads whatever
definitions the directory holds.

### The inputs each definition declares

Each definition names the inputs its artefact is derived from. The
arrows below are those of today's four definitions, drawn from their
Inputs blocks.

```
  the principal's thought, however it arrives
  (around it: research notes, sources, Claude's proposals)
                     |
                     v
          00-brief.md  (and any 00-brief-<name>.md)
                     |
                     v   the briefs the principal says to mine;
                         decisions.md, the ledger; sources as he directs
             10-intent.md  (read with threads.md)
                 |                      |
                 v                      |
        20-assignment.md                |
     (10-intent.md, decisions.md,       |
      the ledger, threads.md)           |
                 |                      |
                 v                      v
             40-solution-design.md
     (the lowest layer the project has above it: the
      assignment, or the intent alone; whatever stands above
      that; decisions.md, the ledger, threads.md)
```

In words:

- The brief is made from the principal's thought, however it
  arrives, and from what is gathered around it during the
  elicitation: research notes in `research/`, sources in `sources/`
  and Claude's own proposals. The existing intent and ledger are read
  only to know what already stands, never to shape the text.
- The intent is made from the briefs the principal says to mine
  (`00-brief.md` and any `00-brief-<name>.md`, approved or not), from
  `decisions.md` and the ledger, and from sources only as the
  principal directs. The intent as it stands is read with the
  project's threads, `threads.md`.
- The assignment is made from `10-intent.md`, `decisions.md` and the
  ledger. The intent is read with `threads.md`.
- The solution design is made from the lowest layer the project has
  above it, whichever that is: the intent alone, or the assignment,
  and whatever stands above that. With it come `decisions.md`, the
  ledger and the threads. Where the thing already exists, what
  realises it is read as it stands. Research and sources come in as
  the principal directs.

Because each definition declares its own inputs, the chain is a set
of definitions that each point at the artefacts they read, not a
fixed line in which every layer follows the one before. The forge
calls this shape a star. A new layer branches from any artefact by
adding one definition and its template, without reworking anything
that exists.

### How the chain grows

The chain grows by adding a layer's definition. The mechanics of a
layer (its commands, its agents, the calibration of its reviewers)
are designed when that layer is actually taken up, not in advance.
Which layers come, and in what order, is open.

The layers below the assignment grow in the same project, by the
same principal's hand, when he chooses to take his own thought
further. What a recipient does with an assignment is a forge run of
his own, in his own instance: the assignment becomes his brief, by
his hand. The chain never spans two principals. Feedback from the
recipients has no channel of its own: the principal processes it and
feeds his conclusions back through `/forge intent`.

### How a change travels

Substance changes go into the intent first and then propagate down
the whole chain the project has: each lower layer is brought to the
changed intent. Only wording is fixed in a lower layer directly. A
change may come from below. When solving shows that what is wanted
cannot be had, or must be wanted differently, the intent changes
first and the layers follow. If the principal dictates substance
straight into a lower layer, Claude proposes the corresponding
change of the intent in the same step. Why the intent goes first is
not recorded.

## Why

The files are numbered in tens so that later layers can be added
without renaming anything that exists. The solution design stands at
40, and the number 30 is free for a layer that may come.

Work is invoked by target state so that knowing the name of the
target artefact is knowing the command. Nothing has to be memorised
as layers are added.

Each definition declares its own inputs so that a future layer can
branch from any artefact by adding one definition. The dispatcher
stays the same whatever the directory holds.

A project takes only the layers it needs because many thoughts end
at the intent, where what is wanted needs no solution written down.
A solution design is worth writing where the way is not obvious,
where a choice has a price, or where two hands would solve the same
matter differently if it were not written down. Whether it is
written, the principal says.

The chain grows downward because the forge is meant to take a
thought as far as its principal needs it taken. The layers are added
by the principal's own hand because the thought stays his: a layer
below the assignment is his next step, not someone else's
deliverable.

The chain never spans two principals because the recipient's work is
his own forge run. An assignment is self-contained for exactly that
reason, so that it can become his brief without the first principal
in the room.

Why the definitions directory is the one listing of the artefacts,
and why a substance change goes into the intent first, is not
recorded.

## A worked example

A principal starts a project with the slug `<slug>`. He writes down
an idea for reorganising how his team handles incoming requests, and
`/forge brief` puts it together as `00-brief.md`. Nothing else of
the chain exists yet. Bare `/forge` shows one artefact, the brief,
and says that the intent can be worked from here, because its input
exists, while the assignment cannot yet, because there is no intent.

He runs `/forge intent`. Claude reads the brief he says to mine, the
decisions and the ledger, and the intent `10-intent.md` is found by
elicitation. For some time the chain ends here: what he wants is
clear to him, and no one else has to act on it. The state map does
not call the assignment missing.

Later he decides to hand the work to a colleague's team. He runs
`/forge assignment`. Claude reads `10-intent.md`, `decisions.md`,
the ledger and the threads, and `20-assignment.md` is found. The
team takes the assignment into its own instance, where it becomes
the team's brief. The team's chain is its own: the principal's chain
does not continue into it.

In a second project the principal ends at the intent and still wants
the way to the solution written down, because one choice has a
price. He runs `/forge solution-design` with no assignment in the
project. The definition of the solution design reads the lowest
layer above it, here the intent alone, and `40-solution-design.md`
is found. The number 20 stays empty, and nothing is missing.

In the first project the solution design, written later from the
assignment, shows that one requirement cannot be met as wanted. The
change goes into the intent first. The assignment is then brought to
the changed intent, and the solution design follows, each in its own
round. A sentence of the assignment that was merely unclear is fixed
in the assignment directly, because wording is not substance.

## See also

- [The brief](the-brief.md): the first artefact.
- [The intent](the-intent.md): the trunk.
- [Elicitation](elicitation.md): what a definition is and how an
  artefact is found by it.
- [Artefacts](../reference/artefacts.md): the definitions of today,
  one row each.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
