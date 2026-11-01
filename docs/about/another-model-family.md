---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 0490e5886e1a5ac5
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

A model of another family is a second mind the forge can ask the same
question it asks its own, so that the answer of one family can be set
beside the answer of another. This page explains why the forge reaches
such a model, how the link to it is built, how the run is kept from
seeing or changing anything of the forge, and how the independence of
the second answer is measured rather than assumed. It is written for
the user who runs a research on two engines, for the extender who
wants to know what the link is before adding an engine to it, and for
the evaluator who asks what the forge's second opinion is worth.

## What it is

Claude is the author of the forge's documents. The critics and the
challengers are isolated reviewers (see [The isolated
reviewers](isolated-reviewers.md)), each a subagent, that is, a run of
Claude that sees nothing of the working conversation. The author and
all its reviewers share one model family. What that family cannot see
as a matter of course, none of them finds. When the reviewers agree
with the author, the agreement therefore means only that the document
is consistent under one set of priors. It is never treated as
validation.

The calibration point lies outside the family. It is a review by
humans, or a review by a model of a different family. Both are invited
at the discretion of the principal, the person whose thinking is being
forged. The link to another model family is the forge's way of
reaching the second of these.

The forge calls what it reaches an engine. An engine is one row of a
table in one script, and the row names the engine's own command-line
tool. The forge names engines and tiers, never models or versions. A
name therefore always means the newest of its kind, and the version is
the tool's own, resolved at the call. The first row of the table is
`antigravity`, reached through its tool `agy`.

## How it works

### The link

One script, `scripts/forge-engine.py`, runs one packet on one engine
of its table and brings the answer back as a note (see
[Scripts](../reference/scripts.md) for its options). The packet is a
folder with one file, `packet.md`, which holds the whole context of
the run: the question, the agent's brief, the shape of the note that
is wanted and any attached notes. Claude composes the packet from the
forge's own definitions. Nothing of the conversation goes into it.

The login is the user's. It is made once, outside the forge, in the
engine's own tool. How that tool is installed and signed in is said by
the tool's own documentation, not by the forge. The forge asks only
that the tool is on PATH. It carries no key, no account and no
configuration of who connects.

The script finds the tool on PATH and checks its version against the
floor the row sets. Below the floor a known bug lies, and the script
refuses to run.

### The place of the run

The engine is given the packet folder as its workspace. That folder
lies under `tmp/`, the working folder of the forge's own repository,
never at the repository's root. The root holds the forge's hooks and
its instance file, and an engine must neither see nor execute them.

The place alone locks nothing. An engine that is allowed every tool
call reads any path on the disk that its own permission rules do not
deny, and it reads those rules from the user's own settings, which the
forge never writes. So the script gives the engine a profile of its
own for the run. The profile is a copy of the user's settings with
permissions added:

- the web is allowed;
- the shell is denied;
- every write is denied;
- the reading of every entry of the forge's repository is denied,
  except `tmp/`;
- the reading of the run's `hold/` folder is denied, where the first
  engine's notes wait.

The paths of the denied entries are computed from where the script
lies. The engine is started with its home pointed at the profile. The
user's own settings are not touched. The profile stays in the run
folder as the record of what the engine was allowed.

### What the engine may do, and what is verified

Every tool call is allowed, and the engine's sandbox is switched on.
Because a headless run has nobody to ask, an engine that meets a tool
call it cannot ask about denies it and returns nothing. So every call
is allowed and the sandbox contains it.

Read-only is verified, never trusted. Before the run the script
records a fingerprint of every file in the packet folder, leaving out
the envelopes and logs of earlier runs. It runs the engine once,
non-interactively, with its input closed, its answer asked for in the
tool's own envelope and a time limit set. Afterwards it compares the
folder. A run that changed or added anything is refused, and nothing
is filed.

### The answer

The envelope must say success, and the answer must not be empty. An
exit without error but with an empty answer is a failure. The envelope
is kept beside the packet for inspection, and the run folder is never
cleaned.

The answer is written as a note. Its front-matter carries the engine,
the model word (as the envelope or the call says, else "engine
default"), the usage and the run. The command that asked for the run
files the note, indexes it and remakes the ledger, the project's state
file that is made at read time. This is the same path every
reviewer's report takes.

A refusal comes back with its reason: the tool missing, the version
below the floor, a packet without `packet.md`, a folder changed by the
run, an envelope that cannot be read or an answer that is empty. An
engine named but unusable is said in one sentence with the script's
reason. The work goes on as if the engine had not been named, and the
bundle's Deviations record it. It is never silent, and never a
question in the middle of the run.

### Where it is used today

The research is the first job on this link (see [How a research is
made](the-research.md)). A deep research may take a second engine by
name, `/research --deep --engine <name>` (see [Research a
topic](../use/research-a-topic.md)). The second engine is asked for by
name and is not the default of a deep research, since how much time
and money a research is given is the person's choice, made at the
call.

The second engine first reads the draft plan, before the principal
confirms it, and says what it misses. Its additions are shown beside
Claude's draft and marked as the engine's. Claude takes nothing of
them by its own judgement. Then the second engine takes every card
whole, on the same packet as Claude's own agent, so that two full
answers to one question can be laid side by side. There is no split
of roles between the engines.

In the synthesis the answers stand side by side with the engine
named. Agreement is the consistency of two families reading the same
web. It is stronger than one family's consistency, and it is still
never validation. Difference is spelled out.

One engine's quota is a budget of the research day. It cannot be
known before a run, since an engine reports its usage after a run and
never before. So the quota is spent one or two runs at a time, never
all cards at once, and the time at which it resets is said plainly.

A challenger persona and a critic lens may one day be sent to another
engine over the same link, so that a challenge can come in with
genuinely different priors. What would be composed is the forge's own
persona and contract, the engine reading the project from disk as a
subagent does, and the report would be scanned and checked before the
command files it unchanged. The reviewers on this link are intended
and not built. The engine would be named at the call.

### Independence, measured

Independence is measured, never assumed. An engine with its tools
allowed reads any path its profile does not deny. Two guards stand
against a second note written from the first instead of from the web:

- the first engine's notes are held outside the bundle, in the run's
  `hold/` folder, until the second engine's note of the card has
  returned;
- before filing, a second script, `scripts/forge-cite.py`, counts for
  every card with notes from more than one engine the URLs the notes
  share and the longer sentences they have in common, and gives a
  verdict.

The sentences counted are the longer ones, so that the card's own text
quoted by both notes counts little. A second note that shares most of
its sources or a third of its sentences with the first was written
from it, not from the web. Such a note goes back to its agent once,
after the other note is out of its reach, or it is said in the
synthesis to be no second voice. The measure touches no network and
writes nothing into a note. What it finds goes into the synthesis.

The same script opens every URL a note cites before the note is
filed. That check is the research's and is explained on its page.

## Why

**Why reach another family at all.** One family's blind spots are
shared by everything that runs on it. Only a reader outside the family
can show what the family systematically misses. Agreement within one
family is consistency, and the forge does not call it more than that.

**Why both engines do the whole work.** A split of roles, one engine
searching and the other reasoning, was rejected. Two halves cannot be
compared. Both engines answer every card in full, so that the answers
can be laid side by side.

**Why no skill on the other engine's side.** The forge's definition is
the one owner of the agent's rules, and it travels in the packet
verbatim. A skill installed in the other engine would be a second
place for the same rules.

**Why a command-line tool and not a library or a server.** A library
is a model without tools, and it needs a key that the forge must not
carry. A server that wraps the model is the same command-line call
under a hat, returning through the model. The command-line tools of
several engines share one headless shape, so that one script with one
table can hold them all.

**Why a packet folder under `tmp/`.** The root of the forge's
repository holds hooks and the instance file, which an engine must
neither see nor execute. A run under `tmp/` also stays traceable.

**Why a profile of its own.** The place alone locks nothing, because
an engine with every tool allowed reads any path its rules do not
deny, and those rules live in the user's own settings. A profile per
run denies the forge's tree and the shell without touching the user's
settings, and it stays as the record of the run. The price is one
settings shape to know per engine.

**Why every tool call is allowed.** A headless run cannot ask, and an
engine that is refused a call it needs returns nothing. The sandbox
contains what the allowance opens.

**Why read-only is verified.** The forge does not take the engine's
word that it only read. The comparison of the folder before and after
is the proof, and a run that fails it is refused.

**Why engines and tiers, never versions.** A name that means the
newest of its kind needs no change in the forge when a new version
arrives, and everything that ran on that name runs on the new one.

**Why independence is measured.** Isolation of the run is not
independence of the answer. An engine with its tools allowed can
reach the other engine's note wherever its profile does not deny it,
and a note written from another note is no second voice. Counting
shared sources and shared sentences is the measure chosen against
trusting the place of the run.

**Why the quota goes one or two runs at a time.** An engine reports
its usage after a run and never before, so a budget spent all at once
cannot be known until it is gone.

**Why the login is the user's and the forge carries no key.** The
forge states this as a rule. The reason beyond the rule is not
recorded.

## A worked example

A deep research is run on Claude's own model and on the engine
`antigravity`. One of its cards reads:

> Does pre-registering a study reduce selective reporting, and what
> kind of evidence says so?

Claude composes one packet for the card: the card, the agent's brief,
the shape of the note and nothing of the conversation. The same packet
goes to Claude's own research agent and to the second engine. The
second engine runs in `tmp/research/<run>/<card>/`, under a profile
that denies the forge's tree and the shell and allows the web, with
every tool call allowed and the sandbox on. Claude's agent's note of
the card waits in `hold/`, which the profile denies.

The second engine's answer comes back as a note whose front-matter
carries `engine: antigravity`, the model word, the usage and the run.
The folder is compared before and after and is unchanged, so the note
is accepted.

Before filing, the independence of the two notes is counted for the
card:

- URLs shared: one, of seven in the first note and nine in the
  second;
- longer sentences shared: none;
- verdict: independent.

The one shared URL is a primary source both engines found. No longer
sentence is shared, so neither note was written from the other. Both
notes are filed, and in the synthesis their answers stand side by
side with the engine named. Where they agree, the synthesis says the
two families read the same web consistently. Where they differ, the
synthesis spells the difference out and leaves the judgement to the
principal.

Had the count shown most sources and a third of the sentences shared,
the second note would have gone back to its agent once, or been said
in the synthesis to be no second voice.

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
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter
names; never edited by hand.
