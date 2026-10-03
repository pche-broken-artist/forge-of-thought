---
project: forge
title: Next generation, the requirements for a forge that can be rolled out into real operation
date: 2026-10-03
author: PCHe
version: 0.2
status: draft
last_change: 0.2 (2026-10-03): the eighteen researches of 2026-10-03 cited under the sections they serve, each with what it found; THR.0520 linked; what is still open rewritten on them.
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: CLAUDE.md, Document chain 1; the history companion:
templates/history.md. -->

## What this brief is for

To put together the requirements for the next generation of the
forge. Its aim: a forge I am able to roll out into real operation.

Why a brief and not threads: several open threads already carry
these requirements, at least in part, but they are worked task by
task. This brief is to make us think of the whole as a concept.

For now the needs are thrown in; they are sifted later. Not all of
them will survive, and some may prove unrealistic. The brief does
not look for solutions. The order of the work set earlier (the brief
`brd` first, then `engine-split`) is held loosely.

Open in the aim itself:
- What "rolled out" means: how many people, which teams, and by what
  one tells that it works.
- Who the target user is.

## What the forge is

### The shape of the whole

One question that frames the others: one general forge, a core with
frameworks on it, or several forges that hand artefacts to each
other. I see the split on two levels: the forge as it is today, to
which a user adds things of his own, and beneath it a core that is
separate from the artefacts. Whether to divide it or to call it a
generalisation of the forge is open; the measure is to be found. The
ambition itself may need revisiting: whether we are not heading
somewhere that cannot be managed. Open too is how this stands to my
word of 2026-09-26 against one tool that does everything.

Research:
`research/2026-10-03-one-tool-a-core-with-modules-or-several-tools.md`.
Everyone surveyed ended at a small core that owns mechanism and
format, with the content outside it; nobody runs several equal tools
with a designed hand-over, and retreats from too much division are
common. It advises not to divide now and to try first on one real
case. This section rests on THR.0520: where the solution lives
decides what the core is.

### User modifications

The forge is to be highly customisable. It comes as a base
framework: the core is kept and maintained centrally, and every user
can add artefacts, elicitations, challengers, critics and checks of
his own. What is central and what is the user's is never mixed; the
user's ideally lives in his own git. There is one place with the
list of every type that can be created, and skills or commands by
which a user creates new types of his own. Naming conventions are
needed with it, also against a collision of names. A possible
support: the boundary between mechanism and instance.

Research:
`research/2026-10-03-user-extensions-kept-apart-from-the-core.md`.
The user's things live where an upgrade never writes; the field is
split on whether a user's thing may shadow a core one of the same
name or may only be added beside it. When the engine renames a
contract, a user's agent runs without it and nobody is told. Claude
Code has no mechanism for artefact definitions and templates.

### Work without a known artefact

An example: a strategy at work. There is no artefact for it and no
procedure, and its outcome is certainly not one document. What I
want is the core: ingesting a file, research, the logs and the
history, elicitation. The price to name: a general elicitor has no
map of what is to be found.

Research:
`research/2026-10-03-work-without-a-known-artefact-and-its-working-files.md`.
It limits the price named above: the map does not vanish, it becomes
the question, its boundaries and a tree of sub-questions, and it is
the first thing found. Mine to answer: whether the outcome of such
work is positions I hold, with documents rendered from them, or
documents I compose by hand.

### Further outputs and working files

Spreadsheets, data, several output documents. Today there is no
place for them and no rule for how to treat them. This holds in
today's forge too, whatever becomes of the rest.

Research: the same note. Outside practice is firm: raw inputs
immutable, derived files kept apart and able to be made again; a
binary file needs a text twin or a script that makes it.

## How one works with it

### Automation

The forge is built on the owner's word, and in places that is a
needless burden: typically checks and releases. Perhaps an agent
that decides routine matters for the owner, who then decides only
what is important. And on the principal's decision a task can be
handed over whole: propose all of it, solutions included, do as much
research as you like, and show me the result. The documentation is
such a task. To be found: where the owner's word protects something
and where it is only ceremony.

Research:
`research/2026-10-03-where-the-forge-asks-for-the-principals-word.md`
and `research/2026-10-03-when-an-agent-may-decide-and-when-it-waits.md`.
The forge asks for my word in thirty-seven places; every recorded
failure behind them is Claude acting beyond the word given, and the
burden sits in conformance findings. Outside, the irreversible, the
outward and the substance wait for a person; routine is delegated by
a class written down beforehand; a whole task is handed over by a
contract and comes back as a proposal. It limits the thought above:
an agent as the judge of the work is warned against.

### Several people on one project

Today it is very unpleasant for the user. I do not know whether it
can be solved, but it must be decided and said how it is to be. It
runs from simple things, such as colliding IDs, to how one document
is put together efficiently; and it is never one document, since a
change rewrites a whole row of files: the history, the ledger and
more. My estimate is that collisions will be few, because analysts
mostly work each on a topic of his own; but they can happen, and
there may be topics where the collaboration is needed. Open is the
level at which it is solved: git and the same files, or lower down,
where the outputs of different people meet in one project, a BRD in
Jira for example. The case that prompted it: the agentic platform
project, worked by two people.

Research:
`research/2026-10-03-what-a-write-touches-and-where-two-authors-collide.md`,
`research/2026-10-03-concurrent-work-on-structured-text-in-git.md`,
`research/2026-10-03-several-authors-on-one-body-of-requirements.md`,
`research/2026-10-03-where-requirements-meet-outside-git.md`. One
owner per document and the others through review; the text meets in
git and a tracker gets a one-way mirror. The forge has no allocator
of IDs, its worst collisions are silent, and a save after a failed
rebase is a dead end already today. Mine to answer: whether "several
people" means taking turns or writing in the same days.

### Connection to the systems around

Inputs come from the company's systems and outputs are to go into
them. Today the forge is an island with ingest by hand.

Research:
`research/2026-10-03-where-requirements-meet-outside-git.md`. A
finished artefact is published one way; the connectors can read and
write nearly everything. Mine to answer: which systems are in play
and whether they are in the cloud.

## How it is operated

### Upgrade and compatibility

A stable line beside the one under development, a statement of what
does not change between versions, and a way to bring a project to a
new structure. The case that prompted it: I keep changing the forge
while a second person works on the same project, so he has another
version of the engine and his documents come out in another
structure (the history, the ledger). The tension between user
modifications and a central upgrade belongs here too.

Research:
`research/2026-10-03-versions-channels-and-migration-of-user-content.md`.
Tools whose content has a strict shape record a format version in
the content; a stable line is cheap as a pointer moved at releases.
It goes against today's rule that a project records no engine
version.

### Testing how the engine behaves

A change of the instructions changes the behaviour, and nothing
verifies it. The engine also depends on what is outside our control:
a new version of Claude Code, a new model.

Research:
`research/2026-10-03-testing-the-behaviour-of-a-prompt-framework.md`.
A small suite built from real failures, checks by code, several
runs; scripted sessions fit the forge today. It will not catch the
quality of the elicitation.

### Operation in a company

Data and security: what may enter a project and a conversation with
a model, and who approves it. Costs. Support, and the way a good
user-made type returns to the core.

Research:
`research/2026-10-03-operating-claude-code-for-many-users-in-a-company.md`.
Data, security and cost are decided by the plan and the centrally
managed settings, not by a framework; three central locks silently
switch the forge off, and only a plugin passes into a locked-down
company. The rule of one model runs against the first lever on cost.

### A technical clean-up

To standardise the architecture, how the single things are done; to
take as much as possible out of CLAUDE.md, which may also keep the
generality; to name the technical and architectural debt. The forge
has grown step by step, some things were rewritten many times, and
who knows whether they are right.

Research:
`research/2026-10-03-operating-layer-architecture-and-debt.md`,
`research/2026-10-03-anthropic-guidance-for-claude-code-and-where-the-forge-departs.md`,
`research/2026-10-03-agent-instruction-architecture-beyond-anthropic.md`.
Of the 650 lines of CLAUDE.md 285 serve named commands; the write of
a round has no definition of its own; the same kind of thing is done
in five or six ways. Every vendor describes three layers: a short
always-on file, procedures loaded on demand, hooks and scripts for
what must always hold. A rule moved into a skill is weaker late in a
long session. This section rests on THR.0520.

## How people get to it

### Documentation and news

The README is today the documentation, and that is not good: it is
very long and poor as documentation. The README is to be short: what
the forge is and what it is for, perhaps the current news. The
documentation is a normal series of documents on single topics,
separate linked pages on which a topic can be described well. It is
for people inside the company and outside it, so that they
understand the forge and use its potential in full. We also show
badly what is new in a version: the README does not say, and the
release notes are technical. There should be something like the
biggest news, which strikes the reader: the new elicitation and what
it is, to take the last releases.

Research:
`research/2026-10-03-how-project-documentation-is-built.md` and
`research/2026-10-03-showing-the-main-news-of-a-version-to-a-reader.md`.
The README orients and points; one page, one topic; plain pages in
`docs/`, the reference derived from the definitions; no need to wait
for the split. The news is a second document beside the changelog,
written per period and not per release; an item is a capability, and
a person makes the cut.

### The threshold of entry

Installation, the first run, and what a person must be able to do
before he starts.

Research:
`research/2026-10-03-the-threshold-of-entry-for-a-non-developer.md`.
The threshold is what the forge adds: git, PowerShell 7, Python,
pandoc, about eleven steps to the first question. The desktop app
removes the terminal without a change of the architecture; untried.

## What already stands in the intent

Threads this brief carries whole: THR.0340, THR.0300, THR.0480,
THR.0230, THR.0420, THR.0500, THR.0090, THR.0240, THR.0150,
THR.0460.

In part: THR.0200, THR.0410, THR.0190, THR.0360, THR.0170, THR.0490,
THR.0470; and the parked challenge CHL.0150.

To be sifted, as connected: THR.0400 (a gate in front of the tools
pulls against less asking), THR.0210 (the public boundary once more
people work over a public engine), THR.0430 with THR.0490 (the start
and the end of a session), THR.0140 (the delivery side), THR.0320 (a
lens over the operating layer as a tool for finding debt), THR.0510
(live reference material).

Opened from the talk over this brief: THR.0520, the intent carries
the solution and a layer for the solution is missing; priority. The
sections "The shape of the whole" and "A technical clean-up" rest on
it.

## Still open

- Whether user modifications are the engine split or a level of
  their own; the field treats them as a level of their own on the
  same mechanism.
- Where the researches disagree. A plugin cannot carry CLAUDE.md,
  yet it is the only form a locked-down company allows and the
  lowest entry there is. Moving rules out of CLAUDE.md is advised by
  everyone, yet a rule in a skill weakens and nothing verifies it.
  One model for everything against the cost.
- What the researches rest on. Most pages were read through a tool
  that summarises, so quotations are to be checked at the source;
  several recommendations rest on reasoning and not on a trial: how
  git merges the forge's files, the forge in the desktop app, a
  contract loaded from a user's own pack.
