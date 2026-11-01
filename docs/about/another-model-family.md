---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 963b14f7220a2c0f
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

A model of another family is a second, outside voice that Claude can
send one piece of work to and get one answer back from. This page
explains why the forge reaches such a model, how the link works and
how the forge checks that the answer is really independent. It is
for anyone who uses the forge, extends it or weighs whether to trust
it.

## What it is

The author, the critic and the challengers of the forge all run on
one model family. The critic and the challengers are isolated
reviewers, explained in
[The isolated reviewers](isolated-reviewers.md). Isolation is not
independence. What that one family systematically cannot see, none
of them will find. So agreement between the reviewers is never
treated as validation. It only means the work is consistent under
one set of priors.

The calibration point lies outside the family. It is a review by
humans, or by a model of a different family, invited when the
principal wants it. The principal is the person whose thinking is
being forged and who decides everything in it.

The forge reaches such a model over one link. Today one job uses the
link: the deep research, explained in
[How a research is made](the-research.md). Reviewers on the link are
intended and not built. A challenger persona or a critic lens is
meant to be sent to another engine over the same link, so that a
review can come in with genuinely different priors.

## How it works

### One script, one table of engines

One script, `scripts/forge-engine.py`, runs one packet on an engine
and brings its answer back as a note. A packet is a folder holding
`packet.md`, the whole context of the run: the card, the agent's
brief, the shape of the note and any attached notes. The command
composes it from the forge's own definition.

The script has a table of engines, one row per engine. Each engine
is reached over its own command-line tool. The first row is
`antigravity`, whose tool is `agy`. Adding an engine is adding a row,
as [Add an engine](../extend/add-an-engine.md) shows.

- **The login.** The login is the user's own, made once outside the
  forge in the engine's own tool. The forge carries no key, no
  account and no configuration of who connects.
- **Engines, not models.** The forge names engines, never models.
  The reason is not recorded.

The script refuses to run, with its reason, when:

- the engine's tool is not found;
- the tool's version is below the floor the table sets;
- the packet folder holds no `packet.md`;
- the run changed anything in its folder;
- the engine's answer cannot be read or is empty.

### Where the engine works, and the profile

The engine works in the packet folder, under the engine's working
folder `tmp/`. It never works at the forge's root. The root holds the
hooks and the instance file, and an engine must not see or execute
them. A hook is a script Claude's tooling runs on its own at fixed
moments; the instance file holds the facts of one installation.

The place alone locks nothing. With every tool allowed, an engine
reads any path on the disk that its settings do not deny. So the
script gives the engine a profile of its own for each run:

- **Allowed:** the web.
- **Denied:** the shell, every write, and the reading of every part
  of the forge's tree but `tmp/`.

The profile is a copy of the user's settings for that engine with
these rules added. The user's own settings are not touched. The
profile stays in the run folder as the record of the run. The price
of the profile is one settings shape to know per engine.

### Every tool call allowed, the sandbox on

A run that cannot ask a question denies every tool call it would
have asked about, and then returns nothing. So every tool call is
allowed and the engine's sandbox contains the run.

Read-only is verified, never trusted. The script records every file
of the folder before the run and compares the folder afterwards. A
run that changed or added anything is refused and nothing is filed.

### The answer as a note

The answer comes back as a note. Its front-matter carries:

- `engine`: the engine's name in the table;
- `model`: the model word, as the engine reports it or as it was
  given, else "engine default";
- `usage`: what the engine reports it spent;
- `run`: the folder the run worked in.

The command then files the note, indexes it and remakes the ledger
(the file that holds the state of a project, made from its documents
whenever it is read). The options of the script are listed in
[Scripts](../reference/scripts.md).

### The second engine in a deep research

A deep research may take a second engine beside the session model
(the model Claude runs on in the current conversation). The engine is
asked for by name, as
[Research a topic](../use/research-a-topic.md) shows; it is never
the default of a deep research. A research on the session model
alone is still a deep research.

The second engine does two things:

1. It reads the draft plan before the walkthrough (the conversation
   in which the principal decides item by item) and says what the
   plan misses. Its additions are shown beside Claude's draft,
   marked as the engine's. Claude takes none of them on its own
   judgement.
2. It answers every card whole, on the same packet as the session
   agent (an isolated subagent: a helper run of Claude that sees only
   its packet). Two full answers to one question then lie side by
   side.

In the synthesis the two answers stand side by side with the engine
named. Agreement is consistency of two families reading the same
web. It is stronger than one family's agreement, and still never
validation. Where the answers differ, the difference is spelled out.

An engine that is named but unusable is said in one sentence, with
the script's reason. The research goes on as without it, and the
research bundle records the deviation. It is never silent and never
a question in the middle of the run.

### Independence is measured

Independence is measured, never assumed. Two steps hold it:

- **Held out of reach.** The first engine's notes wait in a folder
  the second engine's profile denies, until the second engine's note
  of the same card has returned.
- **Counted before filing.** A second script, `scripts/forge-cite.py`,
  counts for every card with notes from two engines the URLs the
  notes share and the longer sentences they have in common, and gives
  a verdict. It touches no network.

The verdict is "dependent" when the notes share more than half of
the smaller note's URLs, or more than a third of its longer
sentences. Such a note was written from the other note, not from the
web. It goes back to its agent once, with the other note out of its
reach. Otherwise the synthesis says it is no second voice.

The same script also opens every URL a note cites before the note is
filed.

### The quota

An engine reports what a run cost only after the run, never before.
So an engine's quota is spent one or two runs at a time, never many
at once, and the time it resets is said plainly.

## Why

- **Why another family at all.** Reviewers of one family share one
  set of priors. Their agreement cannot show what the family cannot
  see. A different family is a calibration point outside it.
- **Why both engines do the whole work.** A split of roles, one
  engine searching and the other reasoning, was rejected. Two halves
  cannot be compared. Both engines answer every card in full so that
  the answers can be laid side by side.
- **Why no skill on the other engine's side.** The forge's
  definition is the one owner of the agent's rules, and it travels
  in the packet word for word. A skill installed in the other engine
  would be a second place for the same rules.
- **Why a command-line tool, and not a library or a server.** A
  library gives a model without tools. It also needs a key, and the
  forge must not carry one. A server between the forge and the engine
  would be the same command-line call under another layer, with the
  answer returning through the model. The command-line tools of
  several engines share one shape for a single run without a person
  present.
- **Why a packet folder under `tmp/`.** The run stays traceable
  there. The forge's root holds the hooks and the instance file, which
  an engine must not see or execute.
- **Why a profile, and not the place alone.** With every tool
  allowed, an engine reads any path on the disk its settings do not
  deny. The folder it works in does not stop that; the profile's deny
  rules do.
- **Why every tool call is allowed.** A run that cannot ask denies
  what it would ask about and returns nothing. The sandbox contains
  the run, and the comparison of the folder proves it read only.
- **Why the second engine is asked for by name.** How much time and
  money a research is given is the person's choice, made when the
  command is called.
- **Why independence is measured.** An engine with its tools allowed
  reads any path its profile does not deny. Without the hold and the
  count, a second note could be a rewrite of the first and look like
  a second voice.
- **Why the forge names engines and never models.** The reason is
  not recorded.

## A worked example

One generic card of a deep research, `card-1`, asks one question. The
session agent and `antigravity` each answer it on the same packet.

```
            packet of card-1
           /                \
   session agent         antigravity
   (note filed,          (runs while the first
    then held out         note is out of reach)
    of reach)                   |
           \                    /
            two notes of card-1
                    |
       forge-cite.py --independence
       shared URLs, shared sentences
                    |
          verdict per pair of notes
```

Say the session agent's note cites 8 URLs and holds 30 longer
sentences. The `antigravity` note cites 10 URLs and holds 26 longer
sentences.

- **Independent.** The notes share 3 URLs and 2 sentences. Half of
  the smaller URL count is 4 and a third of the smaller sentence
  count is 8. Neither is exceeded, so the verdict is "independent".
  The synthesis lays both answers side by side, names each engine,
  calls what they agree on consistency and spells out where they
  differ.
- **Dependent.** The notes share 6 URLs. That is more than half of
  8, so the verdict is "dependent". The `antigravity` note goes back
  to its agent once, with the other note out of its reach. If it is
  not run again, the synthesis says it is no second voice.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
