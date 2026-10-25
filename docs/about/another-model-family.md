---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 90890351e3017f50
inputs:
  - projects/forge/10-intent.md#POS.0790
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1870
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/10-intent.md#REJ.0440
  - projects/forge/10-intent.md#REJ.0480
  - projects/forge/10-intent.md#REJ.0490
  - projects/forge/40-solution-design.md#SOL.0870
  - projects/forge/40-solution-design.md#SOL.0880
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Another model family

A model of another family is a second voice from outside the model
family Claude runs on, reached by the forge through one script. This
page explains why the forge reaches such a model, how it is reached,
and how its answer is kept independent of Claude's. It is written for
the user who runs a research with a second engine, for the extender
who adds an engine, and for the evaluator who wants to know what the
agreement of two models is worth.

## What it is

The author of a document, the critic and the challengers all share
one model family. The critic and the challengers are the forge's
reviewers: see [The isolated reviewers](isolated-reviewers.md). Each
reviewer runs as a subagent, that is a separate run of Claude that
never sees the working conversation. That isolation is not
independence. What one model family systematically cannot see, none
of them will find.

So the agreement of the reviewers is never treated as validation. It
only means the document is consistent under one set of priors.

The calibration point lies outside: review by humans, or by a model
of another family. The principal (the person whose thinking is being
forged) invites either at his discretion. A model of another family
is reached over one link, and every job sent to such a model runs
over it.

Where several engines answer one question, Claude lays the answers
side by side with each engine named. The principal is the chairman.
Agreement is consistency, never validation. A difference is spelled
out.

## How it works

### One script, one table of engines

The forge reaches a model of another family through one script,
`scripts/forge-engine.py`. The script holds a table of engines, one
row each. Adding an engine means adding a row, never a branch in the
code. The first row is `antigravity`, whose command-line tool is
`agy`.

Each engine is reached over its own command-line tool:

- The login is the user's, made once outside the forge, in the
  engine's own tool.
- The forge carries no key, no account and no configuration of who
  connects.
- The forge names engines, never models. A model word may be passed
  through and is recorded, but the forge never chooses a default.

The script refuses to run when the engine's tool is missing from the
path, or when its version is below a floor the row records.

### The packet and its folder

One run takes one packet. A packet is a folder holding `packet.md`,
the whole context of the run:

- the card: the one question the run answers;
- the brief of the agent that answers it;
- the shape of the note it must return;
- any notes attached to it.

The command composes the packet from the forge's own definition of
the job. The definition travels in the packet word for word.

The engine is given the packet folder as its workspace and runs in
it. The folder lies under `tmp/`, the engine's working folder, so
that the run stays traceable. It never runs at the forge's root,
because the root holds hooks and the instance file that an engine
must not see or execute.

### The profile of the run

The place of the run alone locks nothing. With its tools allowed, an
engine can read any path on the disk that is not denied to it. The
engine reads its permission rules from the user's own settings file
only, and the forge never writes that file.

So the script gives the engine a profile of its own for the run. The
profile is a copy of the user's settings with permissions added:

- allowed: reading the web;
- denied: the shell;
- denied: every write;
- denied: reading every entry of the forge's root except `tmp/`;
- denied: reading the run's holding folder, where the first engine's
  notes wait.

The paths are computed from where the script lies. The engine is
started with its home pointing at the profile, so it finds its login
there. The user's own settings are left untouched. The profile stays
in the run folder as the record of the run.

### Every call allowed, the sandbox on

A run without a person to answer cannot ask for a permission. Such a
run denies every tool call it cannot ask about and returns nothing.
So every tool call is allowed, and the engine's sandbox contains it.

### Read-only, verified

Read-only is verified, never trusted. The script records a
fingerprint of every file in the packet folder before the run and
compares the folder afterwards. A run that changed or added anything
is refused, and nothing is filed.

The script also refuses an answer that is empty or whose status does
not say success, even when the engine exits without an error.

### The answer as a note

The answer comes back as a note. The script puts these fields into
the note's front-matter:

- `engine`: the row of the table that ran;
- `model`: the model word, or "engine default";
- `usage`: what the engine reports it used;
- `run`: the packet folder of the run;
- `status: immutable`.

The command then files the note, indexes it and remakes the ledger
(the table of the project's state, built from its documents). It does
this as for every report a reviewer returns.

### Where it is used today: the research

The research is the first job on this link. How a research is made in
full is said in [How a research is made](the-research.md); how you run
one is said in [Research a topic](../use/research-a-topic.md).

A deep research may take a second engine, asked for by name. The
second engine is not the default of a deep research. How much time
and money a research is given is the person's choice, made at the
call. A research on Claude's own model alone is still a deep
research.

The second engine works in two places:

1. It reads the draft plan before the walkthrough (the principal's
   decision on the plan, one item at a time) and says what the plan
   misses. Its additions are shown beside Claude's draft and marked as
   the engine's. Claude takes none of them on its own judgement.
2. It answers every card whole, on the same packet as Claude's own
   agent. So two full answers to one question lie side by side.

In the synthesis, the answers stand side by side with the engine
named. Agreement is the consistency of two families reading the same
web. It is stronger than one family's agreement, and still never
validation.

### Independence, measured

Independence is measured, never assumed. An engine with its tools
allowed reads any path the profile does not deny. So the first
engine's notes are held out of its reach, in the holding folder,
until the second engine's note of the same card has returned.

Before filing, the citation script `scripts/forge-cite.py` counts,
for every card with notes from more than one engine:

- the URLs the notes share;
- the sentences they have in common, counting only the longer ones
  (over sixty characters), so that the card's own text quoted by both
  counts little.

It gives a verdict for each pair. A second note that shares most of
its sources, or a third of its sentences, with the first was written
from it, not from the web. The measure touches no network and writes
nothing into a note. What it finds goes into the synthesis.

A note written from the other engine's note goes back to its agent
once, with the other note out of its reach. Otherwise the synthesis
says it is no second voice.

### An unusable engine and the quota

An engine named but unusable is said in one sentence, with the
script's reason. The research goes on as without it, and the
bundle's Deviations record it. It is never silent, and never a
question in the middle of the run.

An engine's quota is a budget of the research day. It cannot be known
before a run, because an engine reports its usage after a run and
never before. So the quota is spent one or two runs at a time, never
many at once, and the time it resets is said plainly.

### The reviewers on this link

A challenger persona and a critic lens are intended to be sent to
another engine over the same link. They would bring a lens with
genuinely different priors. These reviewers are not yet built. The
link itself is built, for the research.

## Why

**Why reach another family at all.** Isolation is not independence.
Reviewers of one family share that family's blind spots, so their
agreement only shows consistency under one set of priors. A
calibration point must lie outside that family.

**Why both engines do the whole work.** A split of roles, one engine
searching and the other reasoning, was rejected. Two halves cannot be
compared. Both engines do the full work on every card, so that the
answers can be laid side by side.

**Why no skill on the other engine's side.** Installing the forge's
rules as a skill in the other engine was rejected. The forge's
definition is the one owner of the agent's rules and travels in the
packet word for word. A skill installed in the engine would be a
second place for the same rules.

**Why a command-line tool, not a library or a server.** A library is
a model without tools, and it needs a key the forge must not carry. A
server between the forge and the engine is the same call to the
command-line tool under another layer, its answer returning through
the model. The command-line tools of several engines share one
shape for a run without a person present.

**Why a profile of its own for every run.** The place of the run
alone does not stop an engine from reading beyond it. Trusting the
place was rejected for a profile per run. The price is one settings
shape to know per engine, kept in the engine's row.

**Why the independence is counted.** Shared URLs and shared sentences
measure whether a second note was written from the web or from the
first note. Counting them was chosen against trusting the place of
the run.

**Why the second engine is asked for by name.** How much time and
money a research is given is the person's choice, made at the call.

**Why the quota is spent a run or two at a time.** An engine reports
its usage only after a run, so the remaining budget cannot be known
in advance.

## A worked example

A research holds one generic card: "What are the common ways to keep
a shared glossary current?". Two engines answer it: Claude's own
agent, and the engine of the row `antigravity`.

1. Claude's agent answers the card first. Its note waits in the
   run's holding folder, which the profile denies to the other
   engine.
2. The script runs the same packet on `antigravity`, in a packet
   folder under `tmp/`, under a profile of its own. The folder is
   the same before and after the run, so the note is written. Its
   front-matter names `engine: antigravity`, the model word, the
   usage and the run.
3. Both notes now lie in the bundle as the card's two notes, one per
   engine, for example `card-1.<first-engine>.md` and
   `card-1.antigravity.md`.
4. The citation script measures the pair. It prints one line for the
   card, of this shape:

   ```
   card-1: antigravity / <first-engine>: shared URLs 2/9, identical sentences 0/31, text ratio 0.11  independent
   ```

   Two shared URLs out of nine is not most of the sources, and no
   longer sentence is shared, so the second note counts as a second
   voice.
5. Had the line read `shared URLs 7/9` or `identical sentences
   14/31`, with the verdict `dependent`, the second note would go back
   to its agent once, the first note out of its reach. Failing that,
   the synthesis would say it is no second voice.
6. In the synthesis, the two answers stand side by side, each with its
   engine named. Where they agree, that is consistency. Where they
   differ, the difference is spelled out for the principal.

## See also

- [How a research is made](the-research.md): the research, the first
  job on this link.
- [The isolated reviewers](isolated-reviewers.md): the reviewers of
  one family and why their agreement is not validation.
- [Research a topic](../use/research-a-topic.md): a research with
  `--engine`.
- [Add an engine](../extend/add-an-engine.md): adding an engine as one
  row of the table.
- [Scripts](../reference/scripts.md): the engine script and the
  citation script, their options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
