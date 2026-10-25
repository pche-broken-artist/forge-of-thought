---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: ae6af48436f2b823
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
that Claude and every reviewer of the forge run on. This page explains
why the forge reaches such a model, how it reaches it and how it keeps
the second answer independent of the first. It is written for the
user who runs a research with a second engine, for the extender who
adds an engine and for the evaluator who wants to know what the
agreement of two engines is worth.

## What it is

The author, the critic and the challengers share one model family.
Claude is the author here, and the critic and the challengers are the
isolated reviewers (subagents: separate runs of Claude that never see
the working conversation). What that family systematically cannot
see, none of them will find. Agreement between them is therefore
never treated as validation. It only means that the artefact is
consistent under one set of priors. More on this is in
[The isolated reviewers](isolated-reviewers.md).

The calibration point lies outside: a review by humans, or by a
model of a different family. The principal (the person whose thinking
is being forged) invites either at his discretion. The forge reaches a
model of another family over one link, described below. An engine is
one such outside model as the forge reaches it, through that engine's
own command-line tool.

## How it works

### One script, one table of engines

The link is one script, `scripts/forge-engine.py`. It runs one packet
on an engine of its table and brings the answer back as a note. A
packet is a folder holding `packet.md`: the whole context of the run,
composed by the command from the forge's own definition. The table has
one row per engine. The first row is `antigravity`, whose command-line
tool is `agy`. Adding an engine is one row of the table and a pair of
functions, one that builds the engine's command and one that reads its
answer; [Add an engine](../extend/add-an-engine.md) shows how.

The login is the user's own. It is made once, outside the forge, in
the engine's own tool. The forge carries no key, no account and no
configuration of who connects. The forge names engines, never models.
The reason it names no models is not recorded.

### Where the engine runs

The engine is given the packet folder as its workspace. The packet
folder lies under `tmp/`, the engine's working folder, so that the run
stays traceable. The engine never runs at the forge's root. The root
holds the forge's hooks and its instance file (the file of facts about
one installation), and an engine must not see or execute them.

The place alone locks nothing. With every tool call allowed, an engine
reads any path on the disk. So the script gives the engine a profile of
its own for the run:

- a copy of the user's settings for the engine, with permission rules
  added;
- the web allowed;
- the shell and every write denied;
- the reading of the forge's tree denied, all but `tmp/`;
- the reading of the folder where the first engine's notes wait
  denied as well.

The engine is started under that profile. The user's own settings are
not touched. The profile is kept in the run folder as the record of the
run. The price of the profile is one settings shape to know per engine.

### Every call allowed, read-only verified

A run without a person cannot answer a question about permission. Such
a headless run denies every tool call it cannot ask about, and returns
nothing. So every tool call is allowed, and the engine's sandbox is
on to contain it.

Read-only is verified, never trusted. The script records a fingerprint
of every file in the packet folder before the run and compares it
afterwards. A run that changed or added anything is refused, and
nothing is filed. A run whose answer is empty is refused as well.

### The answer comes back as a note

The answer comes back as a note. Its front-matter carries:

- `engine`: the row of the table the run used;
- `model`: the model word the engine reported or was given, else
  "engine default";
- `usage`: what the engine reports it used;
- `run`: the packet folder the run took place in.

The note is immutable. The command files it, indexes it and remakes
the ledger (the forge's state file, made from the documents when it is
read), as it does for every reviewer.

### Where it is used today

The research is the first job on this link; how a research is made
is [How a research is made](the-research.md). A deep research may take
a second engine, asked for by name beside the session model (the model
Claude runs on in the conversation). The second engine is never the
default. A deep research on the session model alone stays a deep
research.

The second engine does two things:

1. It reads the draft plan of the research before the principal works
   through it, and says what the plan misses. Its additions are shown
   beside Claude's draft and marked as the engine's. Claude takes
   none of them by its own judgement.
2. It answers every card (one question of the research) in full, on
   the same packet as the session model's agent. Two whole answers to
   one question then lie side by side.

In the synthesis the answers stand side by side, each with its engine
named. The principal is the chairman between them. Agreement is the
consistency of two families reading the same web. It is stronger than
one family's agreement, and it is still never validation. Difference
is spelled out.

An engine that is named but cannot be used is said in one sentence,
with the reason the script gives. The research then goes on as without
it, and the research's record of deviations says so. This is never
silent, and never a question in the middle of the run.

An engine's quota is spent one or two runs at a time.

### Independence is measured, never assumed

An engine with its tools allowed reads any path its profile does not
deny. So the first engine's notes are held out of its reach until the
second engine's note of the same card has returned.

Before filing, the citation script `scripts/forge-cite.py` counts, for
every card that has notes of two engines:

- the URLs the two notes share;
- the longer sentences they have in common.

It gives a verdict per pair, and touches no network to do so. A second
note that shares most of its sources, or a third of its sentences,
with the first was written from it, not from the web. Such a note goes
back to its agent once, with the other note out of reach. Otherwise
the synthesis says that it is no second voice. What the count finds
goes into the synthesis; nothing is written into a note.

The options of both scripts are listed in [Scripts](../reference/scripts.md).

### The reviewers on this link

A challenger persona and a critic lens are intended to be sent to
another engine over the same link, so that a review can bring in
genuinely different priors. They are not built. The mechanics exist
for the research alone.

### The run at a glance

```
  packet folder under tmp/          per-run profile
  (packet.md: the card, the     +   (web allowed; shell, writes and
   brief, the note's shape)          the forge's tree denied)
              |                               |
              +---------------+---------------+
                              v
             forge-engine.py <engine>: fingerprint before
                              |
                     the engine's own tool, one headless run
                              |
             fingerprint after: changed? -> refused, nothing filed
                              |
                 the answer as a note (engine, model, usage, run)
                              |
         the command files it; forge-cite counts what two notes share
```

## Why

- **Why another family at all.** What one family systematically cannot
  see, no reviewer of that family will find. A calibration point has
  to lie outside.
- **Why a profile and not the place of the run alone.** The place locks
  nothing: an engine with its tools allowed reads any path on the
  disk. Only a deny rule of the engine's own settings holds under
  every tool allowed.
- **Why every tool call is allowed.** A headless run denies what it
  cannot ask about and returns nothing. The sandbox and the profile
  contain what the allowance opens.
- **Why read-only is checked afterwards.** It is verified, never
  trusted.
- **Why the second engine is asked for by name.** How much time and
  money a research is given is the person's choice, made at the call.
- **Why the quota is spent one or two runs at a time.** An engine
  reports its usage after a run and never before. The quota of a
  research day cannot be known before a run.
- **Why both engines do the whole work.** A split of roles, one engine
  searching and the other reasoning, was rejected. Two halves cannot
  be compared. Both engines answer every card in full, so that the
  answers can be laid side by side.
- **Why independence is measured.** An engine can read the other
  engine's note wherever its profile does not deny it, and a note
  written from another note is no second voice. Shared URLs and shared
  sentences show it; the place of the run does not.
- **Why no skill on the other engine's side.** The forge's definition
  is the one owner of the agent's rules. It travels in the packet word
  for word. A skill installed in the engine would be a second place
  for the same rules.
- **Why a command-line tool and not a library or a server.** A library
  is a model without tools, and it needs a key the forge must not
  carry. A server of the Model Context Protocol is the same call of
  the command-line tool under another hat, and its answer returns
  through the model. The one-shot command-line call has one headless
  shape shared by the tools of several engines.
- **Why the forge's root is out of the engine's reach.** The root holds
  the hooks and the instance file. The reason an engine must not see
  them is not recorded beyond that rule.

## A worked example

One card of a research, `card-1`, asks a generic question: which
practices keep a web source's date honest. Two engines answer it on
the same packet.

1. The session model's agent answers the card. Its note is held in a
   folder the second engine's profile denies.
2. `forge-engine.py antigravity` runs the same packet. The fingerprint
   of the folder is the same after the run, so the answer is accepted.
   It comes back as `card-1.antigravity.md`, with `engine`, `model`,
   `usage` and `run` in its front-matter.
3. Only now is the first note filed beside it in the research.
4. The citation script counts the pair. Its line has this shape:

   ```
   card-1: <session> / antigravity: shared URLs 3/10, identical sentences 1/28, text ratio 0.14  independent
   ```

   Three shared URLs of ten is less than half. One shared sentence of
   twenty-eight is less than a third. The verdict is independent, and
   the synthesis lays the two answers side by side, agreement named as
   consistency and difference spelled out.
5. Had the line read `shared URLs 8/10` the verdict would be
   dependent. The second note would go back to its agent once, with the
   first note out of reach, or the synthesis would say that it is no
   second voice.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
