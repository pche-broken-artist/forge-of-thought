---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 715203508958f803
inputs:
  - projects/forge/10-intent.md#POS.0790
  - projects/forge/10-intent.md#POS.0800
  - projects/forge/10-intent.md#POS.1870
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/10-intent.md#REJ.0440
  - projects/forge/10-intent.md#REJ.0480
  - projects/forge/10-intent.md#REJ.0490
  - projects/forge/40-solution-design.md#SOL.0860
  - projects/forge/40-solution-design.md#SOL.0870
  - projects/forge/40-solution-design.md#SOL.0880
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Another model family

A model of another family is the forge's calibration point outside
its own model: a model with different priors, asked the same
question as Claude and answering on its own. This page explains why
the forge reaches such a model, how it is reached and how its answer
is kept independent. It is written for whoever uses the forge,
extends it or evaluates it.

## What it is

Claude writes with the [principal](../reference/glossary.md) (the
person whose thinking is being forged). The critic and the
challengers read what was written; the page
[The isolated reviewers](isolated-reviewers.md) describes them. The
author, the critic and the challengers share one model family. What
that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation. It means only that what they read is consistent under
one set of priors. The reviewers are isolated, and isolation is not
independence.

The calibration point lies outside the family. It is a review by
humans or by a model of a different family, invited at the
principal's discretion.

The forge's word for a model that answers a question is an engine.
The model Claude itself runs on is the first engine. A model of a
different family is a second engine. It is one row of a table in the
engine script, and the row names the engine's own command-line tool.
The table has one row today: `antigravity`, reached by its tool
`agy`.

Where several engines answer one question, Claude lays the answers
side by side with the engines named, and the principal weighs them.
Agreement is consistency and never validation. Difference is spelled
out.

## How it works

### One link, over the engine's own tool

The forge reaches a model of another family through one link. One
script (`scripts/forge-engine.py`) runs one
[packet](../reference/glossary.md) (a folder that holds the whole
context of one run) on an engine of its table and brings the answer
back as a note. The page [Scripts](../reference/scripts.md) lists
the script and its options. A new engine is one more row of the
table; the page [Add an engine](../extend/add-an-engine.md) shows
how one is added.

The link runs over the engine's own command-line tool:

- The login belongs to the principal. It is made once, outside the
  forge, in the engine's own tool.
- How the tool is installed and signed in is said by the tool's own
  documentation.
- The forge asks only that the tool is on PATH.
- The forge carries no key, no account and no configuration of who
  connects.

The forge names engines and tiers, never models or versions. An
engine is named by its row of the table, such as `antigravity`. A
tier is named by its word where a model is overridden. The version
belongs to the tool and is resolved at the call.

### Where the engine works

The engine works in the packet folder and nowhere else. The folder
holds `packet.md`, the whole context of the run:

- the [card](../reference/glossary.md) (one question of a research
  plan)
- the agent's brief
- the shape of the note that is asked for
- the notes attached to the run

The command that asks for the run composes the packet from the
research skill (`.claude/skills/research/SKILL.md`). The engine is
given that folder as its workspace and runs in it. The folder lies
under `tmp/` (the forge's working folder), where the run stays
traceable. The engine never works at the forge's root. The root
holds the forge's [hooks](../reference/glossary.md) and its instance
file (the file that holds the facts of one installation), and an
engine must neither see nor execute them.

The place alone locks nothing. The script therefore gives the engine
a profile of its own for the run. The profile is a copy of the
principal's own settings for the engine with permission rules added:

- allowed: the web
- denied: the shell
- denied: every write of a file
- denied: the reading of every entry of the forge's root but `tmp/`
- denied: the reading of the run's hold folder, where the first
  engine's notes wait

The paths are computed from where the script lies. The engine is
started under that profile. A deny rule holds while every tool call
is allowed, the shell is refused, the engine's own web tools work
and the login is found. The principal's own settings are not
touched. The profile stays in the run folder as the record of the
run.

Every tool call of the engine is allowed, and the engine's sandbox
contains what the engine does.

### What one run does

Read-only is verified, never trusted. One run of the script goes in
this order:

1. The script finds the engine's tool on PATH and checks its
   version. Where a bug is known below a version, it refuses a tool
   below that floor.
2. It records a fingerprint of every file in the packet folder.
3. It starts the engine once, non-interactively and with a time
   limit, with one sentence: read `packet.md`, do exactly what it
   says, give the whole note as the final message and write no file.
4. It compares the folder with the fingerprint. A run that changed
   or added anything is refused, and nothing is filed.
5. It reads the engine's envelope (the wrapper around the answer
   that carries the status and the usage). The status must say
   success and the answer must not be empty. An empty answer is a
   failure, also where the tool ended without an error.
6. It writes the answer as a note.

The envelope is saved beside the packet for inspection. The run
folder is kept and never cleaned.

The note is the engine's text with these fields put into its
front-matter:

- `engine`: the row of the table the run used
- `model`: the model word the envelope or the call gave, else
  `engine default`
- `usage`: what the engine reports it used
- `run`: the packet folder of the run
- `status`: `immutable`

The forge never chooses a model by default. A model word given at
the call is passed to the engine and recorded. The script writes the
note and nothing more. The command that asked for the run files it.

### Where it is used today

The research is the first job on this link; the page
[How a research is made](the-research.md) explains how a research
runs. A deep research may take a second engine beside the session
model (the model the conversation with Claude runs on). The second
engine is asked for by name at the call, as the page
[Research a topic](../use/research-a-topic.md) shows. It is not the
default of a deep research, and a research on the session model
alone stays a deep research.

The second engine does two things:

- It reads the draft plan before the
  [walkthrough](../reference/glossary.md) of the plan (the
  conversation in which the principal decides a list one item at a
  time) and says what the plan misses. Its additions are shown
  beside Claude's draft and marked as the engine's additions. Claude
  takes none of them by its own judgement.
- It takes every card whole, on the same packet as the first
  engine. Two full answers to one question can then be laid side by
  side.

The first engine answers a card through a
[subagent](../reference/glossary.md) (a separate agent that Claude
starts for one job) with web access. The subagent is given the
packet's text and the path of its folder.

A deep research is filed as a bundle: one folder with the plan at
its head and one note per card per engine, named
`<card>.<engine>.md`. In the synthesis of the research the answers
stand side by side with the engine named. Agreement is consistency
of two families reading the same web. It is stronger than the
agreement of one family and still never validation.

An engine that is named and cannot be used does not stop the
research. Claude says so in one sentence with the script's reason,
the research goes on as without the engine, and the bundle records
the deviation. The engine is never passed over in silence, and no
question is asked in the middle of the run. The script refuses, each
time with its reason, when:

- the engine's tool is not on PATH
- the tool's version is below the floor
- the packet folder holds no `packet.md`
- the run changed its folder
- the envelope cannot be read or the answer is empty

One engine's quota is a budget of the research day. It is spent one
or two runs at a time, never six at once, and the time of its reset
is said plainly.

The reviewers on this link are intended and not built. The intention
is that a challenger persona or a critic lens may be sent to another
engine over the same link, as a reviewer with genuinely different
priors. What would be composed is the forge's own persona and
contract. The engine would read the project from disk as a subagent
does. The report would be scanned for instance values and checked
for its shape before the command numbers it and files it unchanged.
The engine would be named at the call. The mechanics are built for
the research alone.

### How independence is kept and measured

Independence is measured, never assumed. Two things serve it.

The first is the order of filing. The first engine's note of a card
is written to a hold folder of the run, and the second engine's
profile denies the reading of that folder. The note moves into the
bundle only when the second engine's note of that card has returned,
or when the card is closed with one engine.

The second is a count. Before the notes are filed, the citation
script (`scripts/forge-cite.py`) takes every card that has a note
from more than one engine and counts:

- the URLs the notes share
- the longer sentences the notes have in common (over sixty
  characters; the card's own text, quoted by both notes, then counts
  little)

It prints the counts with a verdict and touches no network. A second
engine's note that shares most of its sources or a third of its
sentences with the first engine's note was written from that note
and not from the web. Such a note goes back to its agent once, when
the other note is out of its reach. Otherwise the synthesis says
that the note is no second voice. Nothing is written into a note;
what the count finds goes into the synthesis.

## Why

**Why a model of another family.** Reviewers of one family share
what that family cannot see. Their agreement shows consistency under
one set of priors and nothing more. Two families reading the same
web agree more strongly than one family does. Their agreement is
still not validation, and the principal remains the one who weighs
the answers.

**Why engines and tiers, never versions.** A name then always means
the newest of its kind. When a new version arrives, nothing in the
forge changes, and everything that ran on that name runs on the new
one.

**Why the login belongs to the principal and the forge carries no
key.** The reason is not recorded.

**Why a command-line tool and not a library or a server.** A library
is a model without tools, and it needs a key, which the forge must
not carry. A server would be the same call of the command-line tool
with one more layer over it, and its answer would return through the
model. The command-line tools of four engines share the shape of one
non-interactive run, and each further engine is a row to add when it
is wanted.

**Why no skill on the other engine's side.** The research skill is
the one owner of the agent's rules, and the rules travel in the
packet word for word. A skill installed in the engine would be a
second place for them.

**Why the engine never works at the forge's root.** The root holds
the hooks and the instance file, which an engine must neither see
nor execute. Under `tmp/` the run stays traceable.

**Why a profile for the run.** The place of a run alone locks
nothing. With every tool call allowed, the engine reads any path on
the disk. The sandbox restrains the terminal, not the reading. The
engine takes its permission rules from the principal's settings
alone, and the forge never writes those. A profile of its own gives
the run its rules and leaves the principal's settings untouched. The
price is one shape of settings to know for each engine.

**Why every tool call is allowed.** A run with nobody to ask (a
headless run) denies a tool call it cannot ask about and returns
nothing. Allowing every call is the only way such a run reads at all
in a folder the engine does not trust. The engine's sandbox contains
the calls, and the profile denies what the run must not reach.

**Why the second engine is asked for by name.** How much time and
money a research is given is the principal's choice, made at the
call.

**Why both engines do the whole work.** The engines do not split
roles (one searching and the other reasoning). Two halves cannot be
compared. Both engines do the full work on every card, from one
packet, and the answers can then be laid side by side.

**Why independence is measured.** An engine with its tools allowed
reads any path on the disk that its profile does not deny. The place
of a run therefore says nothing about what the engine read. The hold
folder and the order of filing keep the first answer out of reach,
and the count shows what the two notes share.

**Why the quota is spent one or two runs at a time.** An engine
reports its usage after a run and never before. Its quota is
therefore unknowable before a run.

## A worked example

The principal asks for a deep research and names `antigravity` as
the second engine. Before the walkthrough of the plan, `antigravity`
reads the draft and says what it misses. The plan the principal
confirms has a card of this kind:

> Card 1. Which open standards describe the exchange of calendar
> data, and which of them is the most widely implemented?

One packet is composed for the card, and both engines answer it
whole:

```
        tmp/research/<run>/card-1/packet.md
        one packet, the same for both engines
               |                         |
      first engine                 second engine
      a subagent of the            antigravity, over agy,
      session model                under its own profile
               |                         |
      note waits in                note returns
      tmp/research/<run>/hold/     to the command
               |                         |
               +------------+------------+
                            |
        shared URLs and sentences counted
                            |
        both notes filed in the bundle:
        card-1.<first-engine>.md  card-1.antigravity.md
```

Before the notes are filed, the count prints one line for the card:

```
card-1: antigravity / <first-engine>: shared URLs 2/11, identical sentences 0/38, text ratio 0.06  independent
```

The line reads as follows:

- `shared URLs 2/11`: two URLs stand in both notes, and the note
  that cites fewer cites eleven. More than half would make the
  verdict `dependent`.
- `identical sentences 0/38`: no longer sentence stands in both
  notes, and the note that has fewer has thirty-eight. More than a
  third would make the verdict `dependent`.
- `text ratio 0.06`: how alike the two texts are as a whole. It is
  printed and does not enter the verdict.
- `independent`: the verdict.

Both notes are filed. The synthesis lays the two answers to the card
side by side with the engines named. Where they agree, the agreement
is consistency. Where they differ, the difference is spelled out.

The other outcome looks like this:

```
card-1: antigravity / <first-engine>: shared URLs 9/11, identical sentences 17/38, text ratio 0.61  dependent
```

Here the second engine's note was written from the first engine's
note and not from the web. It goes back to its agent once, with the
first engine's note out of its reach. Otherwise the synthesis says
that the card has no second voice.

## See also

- [How a research is made](the-research.md): the research, the first
  job on this link.
- [The isolated reviewers](isolated-reviewers.md): the reviewers of
  one family and why their agreement is not validation.
- [Research a topic](../use/research-a-topic.md): a research with
  `--engine`.
- [Add an engine](../extend/add-an-engine.md): adding an engine as
  one row of the table.
- [Scripts](../reference/scripts.md): the engine script and the
  citation script, their options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
