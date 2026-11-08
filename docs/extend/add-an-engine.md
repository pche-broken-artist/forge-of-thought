---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 11309acdcb1f9c9e
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that the forge reaches
through that model's own command-line tool, as one row of the engine
table of `scripts/forge-engine.py`. This page is for the extender who
adds such a row: what the row holds, what is written beside it, how
the new row is proved and how the change is recorded and released.
What the link to another engine is and why it runs over a
command-line tool is explained in
[Another model family](../about/another-model-family.md); the
script's flags and exit codes are listed in
[Scripts](../reference/scripts.md). The terms of the forge used here
(packet, note, bundle, card) are each given in one line in the
[Glossary](../reference/glossary.md).

## Before you start

Adding an engine is a change of the forge like any other. It is
proved, recorded and released as
[Make a change to the forge](how-a-change-is-made.md) says; this
page gives only what is particular to an engine.

The forge asks three things of the tool, and nothing else.

- The tool is on PATH. How it is installed is said by its own
  documentation, not by the forge.
- The login is yours, made once in the tool itself. The forge
  carries no key, no account and no configuration of who connects.
- The tool has a one-shot, non-interactive shape. It takes a prompt,
  a folder added as its workspace, a request for a JSON envelope and
  a time limit, runs once and exits.

Choose the row's name before you write it. The forge names engines
and tiers, never models or versions: the name says the kind of tool,
and the version is the tool's, resolved at the call. The reason is
that a name then always means the newest of its kind. When a new
version of the tool arrives, nothing in the forge changes, and
everything that ran on that name runs on the new one. The row's name
is what `/research --deep --engine <name>` takes.

## The files

- `scripts/forge-engine.py`: the one file of the change. It holds
  the engine table `ENGINES`, one row per engine; the pairing
  `COMMANDS`, per engine one function that builds the command line
  and one that reads the envelope; and, in its header, the list of
  the engines with the shape of each row and the fields of its
  envelope.
- `.claude/skills/research/SKILL.md`: the command that takes the
  row's name. Where it explains `--engine <name>`, its text names the
  rows of today in brackets.

## Steps

1. **Learn the tool's one-shot shape.** From the tool's own
   documentation, find how it is started once and non-interactively:
   - the flag that takes the prompt;
   - the flag that adds a folder as the workspace;
   - the flag that asks for a JSON envelope;
   - the flag that sets a time limit;
   - where the tool has them, the flags for the model, the effort, a
     schema of the answer, the sandbox and the approval of every
     tool call.

   Find the fields of its envelope as well: which field says the
   status and which value of it means success, which field holds the
   response, which holds the usage, and whether the model is in the
   envelope at all.

2. **Add the row to `ENGINES`.** The row holds:
   - the tool's executable, as it is found on PATH;
   - how the version is asked, and a version floor where a bug of
     the tool is known (the script refuses a version below the
     floor);
   - the tool's flag that approves every tool call, which the
     script's `--allow-all` passes;
   - the tool's sandbox flag, which the script's `--sandbox` passes,
     where the tool has one.

3. **Write the function that builds the command line.** It returns
   the command the script runs, in the tool's one-shot shape: the
   prompt (`--prompt`, or the script's default sentence, which tells
   the engine to read `packet.md` in its workspace and do exactly
   what it says), the packet folder added as the workspace, the JSON
   envelope asked for and the time limit (`--timeout`), and, where
   the tool has them, the model (`--model`), the effort (`--effort`),
   the schema (`--schema`), the sandbox (`--sandbox`) and the flag
   that approves every tool call (`--allow-all`). The script runs the
   command once, non-interactively, with stdin closed.

4. **Write the function that reads the envelope.** It reads the
   tool's envelope and says whether the run succeeded. The status
   must say success and the response must be non-empty; an exit of 0
   with an empty answer is a failure. It returns the response, the
   usage and the model where the envelope carries one. Where the
   model is not in the envelope, the script records the `--model`
   word, or "engine default" when none was given.

5. **Pair the two in `COMMANDS`** under the row's name. The name of
   the row and the name of the pair are one word.

6. **Settle the profile.** For every run the script writes the engine
   a profile of its own: a copy of your settings for the tool, in the
   tool's own settings shape, with permissions added. The profile
   allows the web. It denies the shell, every write, and the reading
   of every entry of the engine root but `tmp/` and of the run's
   `hold/` folder; the paths are computed from where the script
   lies, and the engine is started with HOME and USERPROFILE pointing
   at the profile. Your own settings are not touched, and the profile
   stays in the run folder as the run's record. The place where the
   tool keeps its settings is written in the script for the first
   engine alone. When a second engine comes, that place moves into
   the row, and the new row carries the place of its own tool's
   settings. The price of this design is one settings shape to know
   per engine.

   The profile exists because the place of the run alone locks
   nothing. With every tool call allowed, the engine reads any path
   on the disk, and it reads its permission rules from its own
   settings file alone, which the forge never writes.

7. **Add the row to the header.** The header lists the engines, one
   row each, with the command-line shape of each and the fields of
   its envelope. The new row stands beside the first in the same
   shape.

## Prove it

Three runs, in this order; each rests on the one before. No check of
the forge verifies a row of the table: these runs are the proof.

**A trial of the engine alone.** Make a scratch packet under
`tmp/research/`: a folder with a `packet.md` that holds one small
question and the sentence that the engine writes no file and returns
the whole answer as its final message. Run the script on it without
the profile:

```
python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --no-profile
```

`--no-profile` runs the engine under your own settings for the tool.
It is a trial of the tool and of the pair, never a research: nothing
of it is filed. Where the tool's web tools would wait for a
permission nobody can give in a headless run, add `--allow-all`. You
should now see the script exit with 0 and the answer written to the
`--out` file as a note, with `engine`, `model`, `usage`, `run` and
`status: immutable` in its front-matter; the envelope lies beside the
packet as `envelope.json` for inspection.

**A run with the profile.** Run the same packet, or a fresh one, as
the research command runs it:

```
python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
```

Then check that the profile's deny rules hold for this tool. What
must hold:

- the shell is refused;
- a write is refused, and the script's comparison of the folder
  before and after the run finds nothing changed;
- a read of the forge's tree outside `tmp/` is refused;
- the tool's own web tools work;
- the login is found.

How you make the engine attempt a denied call is yours; the question
of the scratch packet may ask for it. Where to look is the envelope
saved beside the packet as `envelope.json` and the profile kept in
the run folder as the run's record. You should now see the note
written as in the trial, and no denied call carried out.

**A research on a real question.** Run
`/research --deep --engine <name> <topic>` on a question a project
has. The engine named does two things in that run: it reviews the
draft plan before the principal (the person whose thinking is
forged) confirms it, and it takes every card beside Claude's own
agents, one note per card as `<card>.<name>.md` in the research
bundle. An engine the command finds unusable (not on PATH, no login,
quota spent, an envelope it cannot read) is said in one sentence
with the script's reason, and the research goes on without it; the
bundle's Deviations record it. You should now see the engine's
review shown beside the draft plan, a note of the new engine for
every card, and the measure of the engines' independence stated per
card in the synthesis.

**If the script refuses.** The script exits with 1 and gives the
reason on stderr:

- the tool is missing from PATH;
- the version is below the floor;
- the packet has no `packet.md`;
- the folder was changed by the run;
- the envelope cannot be read, or the answer is empty.

The tool's own non-zero exit is reported with the tool's stderr.

## Record and release

The addition is recorded and released as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) says. The run
folders of the proof under `tmp/` stay where they are, for
inspection; nothing in `tmp/` is a source of truth, and none of them
is recorded.

## A worked example

One addition, with `<name>` for the row and `<tool>` for the
executable of its command-line tool.

1. `<tool>` is installed and signed in once, by its own
   documentation; `<tool>` is on PATH.
2. In `scripts/forge-engine.py` a row `<name>` enters `ENGINES`: the
   executable `<tool>`, how its version is asked, a floor where a bug
   of `<tool>` is known, and the approve-all flag and the sandbox
   flag of `<tool>`.
3. Two functions are written: one returns the command line of
   `<tool>` in its one-shot shape; the other reads the JSON envelope
   of `<tool>` for its status, its response, its usage and, where it
   is there, its model.
4. `COMMANDS` gains the pair under `<name>`.
5. Since `<name>` is a second row, the place of a tool's settings
   moves into each row, and the row `<name>` carries the place of the
   settings of `<tool>`.
6. The header gains the row `<name>` beside the first, with its
   command-line shape and the fields of its envelope.
7. A scratch packet `tmp/research/<run>/<card>/packet.md` holds one
   small question. The trial runs with `--no-profile`: exit 0, the
   note written to `tmp/research/<run>/<card>/<name>.md`.
8. The run with the profile follows, `--allow-all --sandbox`, and
   the deny rules are checked: the shell refused, nothing written, no
   read outside `tmp/`, the web tools working, the login found.
9. `/research --deep --engine <name> <topic>` runs on a real
   question: the review of the draft plan is shown beside the draft,
   and the bundle holds `<card>.<name>.md` for every card.
10. The change is recorded and released.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags
  and exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
