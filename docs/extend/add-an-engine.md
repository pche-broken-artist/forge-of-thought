---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 1c797e7ab122445a
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that the forge reaches through
that family's own command-line tool. This page is for the extender who
adds one. An engine is one row of the engine table of
`scripts/forge-engine.py` and a pair of functions beside it, and the
row is proved by three runs. What the link to another engine is and
why it is a command-line tool is explained in
[Another model family](../about/another-model-family.md).

## Before you start

- Adding an engine is a change of the forge. It is proved, recorded
  and released as any change of the forge, the way
  [Make a change to the forge](how-a-change-is-made.md) describes.
- The engine's tool is installed and signed in. You make the login
  yourself, once, outside the forge, in the engine's own tool. How
  the tool is installed and signed in is said by the tool's own
  documentation. The forge asks only that the tool is on PATH.
- The forge carries no key, no account and no configuration of who
  connects. A row holds none of them.
- The tool has a one-shot, non-interactive shape: one call that takes
  a prompt, works in a folder it is given, returns its answer as a
  JSON envelope (one JSON object for the whole run) and ends.
- Every term of the forge has one line in the
  [Glossary](../reference/glossary.md).

## The files

The row is added in one file: `scripts/forge-engine.py`. An engine
stands in it in three places:

- the header, which lists the engines, one row each: the name, the
  tool's command line and the fields of its envelope;
- `ENGINES` (the engine table), with one row per engine;
- `COMMANDS`, which holds the pair of the row: one function that
  builds the engine's command line and one that reads its envelope.

The header shows the one row the table has:

```
antigravity   `agy -p <prompt> --add-dir <packet> --output-format json
               --print-timeout <s>s --disable-slash-commands
               [--model] [--effort] [--json-schema] [--sandbox]
               [--dangerously-skip-permissions]`
              envelope: status (SUCCESS | ERROR | ...), response,
              usage, duration_seconds, num_turns; the model is not
              in the envelope, the --model word is recorded.
```

What a row and its pair hold, with the row `antigravity` beside it:

| What the row and its pair hold | In the row `antigravity` |
|---|---|
| the tool, found on PATH | `agy` |
| the prompt | `-p <prompt>` |
| the packet folder, added as the workspace | `--add-dir <packet>` |
| the JSON envelope, asked for | `--output-format json` |
| a time limit | `--print-timeout <s>s` |
| the model, where the tool takes one | `[--model]` |
| the effort, where the tool has one | `[--effort]` |
| a schema for the final answer, where the tool takes one | `[--json-schema]` |
| the sandbox, where the tool has one | `[--sandbox]` |
| the flag that approves every tool call, where the tool has one | `[--dangerously-skip-permissions]` |
| the fields of the envelope the script reads | `status`, `response`, `usage` |
| whether the model is in the envelope | it is not; the `--model` word is recorded |
| a version floor, where a bug is known | 1.1.1, below which a bug of `agy -p` is known |

The same file writes the per-run profile: the settings the engine is
started with for one run, in the engine's own settings shape. The
settings path of the profile is written for the first row
(`antigravity`). It moves into the row when a second engine comes.

The rest of the script is the same for every engine, and you do not
build it:

- it finds the tool on PATH and refuses a version below the floor;
- it checks that the packet folder holds `packet.md`;
- it runs the engine once, non-interactively, with stdin closed;
- it refuses a run that changed or added anything in the packet
  folder;
- it saves the envelope beside the packet as `envelope.json`;
- it writes the answer as a note.

## Steps

1. Choose the name. The forge names engines and tiers, never models
   or versions: a tier word in a model override, an engine name in
   the engine table. A name then always means the newest of its kind.
   The version belongs to the tool and is resolved at the call. When
   a new version arrives, nothing in the forge changes, and
   everything that ran on that name runs on the new one. The name of
   the row is the word `/research --deep --engine <name>` takes.

2. Add the row to `ENGINES` under that name. It holds what belongs
   to the tool itself:

   - the tool as it is found on PATH;
   - the tool's flag for its sandbox, where it has one;
   - the tool's flag that approves every tool call;
   - a version floor, where a bug is known.

   The row names no model and no version of a model.

3. Write the function that builds the command line and put it into
   `COMMANDS`. It gives the tool its one-shot, non-interactive shape
   from the flags of the script:

   | Flag of the script | What the command line carries |
   |---|---|
   | `--prompt` | the one sentence the engine is started with |
   | `--packet` | the packet folder, added as the workspace |
   | `--timeout` | the time limit in seconds (1800 by default), passed where the tool has a flag; the script enforces it a minute later |
   | `--model` | a model word the tool understands, where the tool takes one |
   | `--effort` | `low`, `medium`, `high`, `xhigh` or `max`, where the tool has it |
   | `--schema` | a JSON schema file the final answer is shaped by, where the tool takes one |
   | `--sandbox` | the tool's sandbox flag, where it has one |
   | `--allow-all` | the tool's flag that approves every tool call |

   The JSON envelope is always asked for. The forge defaults no
   model: without `--model` the tool's own default runs.

4. Write the function that reads the envelope and put it beside the
   first in `COMMANDS`. It reads the status, the response and the
   usage. A run is answered when the status says success and the
   response is not empty. Exit 0 with an empty answer is a failure.
   Where the envelope names the model, the note records it. Where it
   does not, the note records the `--model` word. Without that word
   the note says `engine default`.

5. Give the engine its profile. The profile is a copy of your
   settings for the engine with the permission rules added, written
   in the engine's own settings shape. What the rules say does not
   change with the engine:

   - the web is allowed;
   - the shell is denied;
   - every write is denied;
   - reading any entry of the forge's root folder but `tmp/` is
     denied;
   - reading the `hold/` folder of the run is denied, where the notes
     of the session model (the model Claude runs on in the
     conversation) wait.

   The paths are computed from where the script lies. The engine is
   started with `HOME` and `USERPROFILE` pointing at the profile. Your
   own settings are not touched. Move the settings path of the
   profile into the rows: each row then holds its own. The price of
   the profile is one settings shape to know per engine.

6. List the row in the header, in the shape of the row it shows: the
   name, the command line, the fields of the envelope and whether
   the model is among them.

## Prove it

The row is proved by three runs, in this order. Each run of the
script takes a packet: a folder that holds `packet.md`, the whole
context of the run. The engine is given that folder as its workspace
and runs in it. An engine never works in the forge's root, whose
hooks and instance file (the file that holds the facts of one
installation) it must not see or execute. For the first two runs,
make a scratch packet under `tmp/research/`: a folder with a
`packet.md` that states one small task.

### 1. The trial of the engine alone

```
python scripts/forge-engine.py <name> --packet tmp/research/<run>/trial --out tmp/research/<run>/trial/<name>.md --no-profile
```

`--no-profile` runs the engine under your own settings, without the
per-run profile. It is a trial, never a research. A headless run (a
run with nobody to answer a permission question) denies a tool call
it cannot ask about and returns nothing. Where the trial comes back
empty for that reason, it needs `--allow-all`, and `--sandbox` where
the tool has a sandbox. Without the profile and with every tool call
approved, the engine reads any path on the disk. A research never
runs this way.

You should now see two lines and exit code 0. The first line names
the engine, its version and the packet and ends with `no profile`.
The second is `note written:` with the path of the note. The
front-matter of the note carries the engine, the model, the usage,
the run and `status: immutable`. The envelope lies beside the packet
as `envelope.json`, for inspection.

The trial shows four things:

- the tool is found on PATH;
- its version is read and is not below the floor;
- the command line the row builds runs;
- the envelope is read.

Exit code 1 is a refusal, with the reason on stderr:

- the tool is missing;
- the version is below the floor;
- the packet has no `packet.md`;
- the run changed the folder;
- the envelope is unreadable or the answer is empty.

The engine's own non-zero exit is reported with its stderr. The
script refuses an `--out` file that exists and asks for another name:
a note is immutable. The flags and the exit codes are listed in
[Scripts](../reference/scripts.md).

### 2. The run with the profile

Make a second scratch packet and run:

```
python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
```

`--allow-all` passes the engine's flag that approves every tool call.
`--sandbox` passes its sandbox flag. Every call is allowed, the
engine's sandbox contains it, and the profile denies what the engine
must not read or do.

You should now see the same two lines, the first naming the profile
where the trial said `no profile`. The profile stays in the run
folder as the record of the run.

Then check that the deny rules of the profile hold. Four things hold
for the row `antigravity`, and the same four are to hold for yours:

- a deny rule holds while every tool call is approved;
- the shell is refused;
- the engine's own web tools work;
- the login is found.

The script verifies one thing itself. It records a fingerprint of
every file in the packet folder before the run and compares the
folder afterwards. A run that changed or added anything is refused
and nothing is filed.

### 3. A research on a real question

Type to Claude:

```
/research --deep --engine <name> <topic>
```

`--deep --engine <name>` adds your engine beside the session model.
The engine reads the draft plan of the research and takes every card
(one question of the plan).

You should now see the engine's additions shown beside the draft
plan, marked as the engine's. At the end you should see one note per
card from your engine (`<card>.<name>.md`) in the bundle of the
research (the folder `research/YYYY-MM-DD-<topic>/`).

An engine that is named but unusable does not stop the research.
Claude says so in one sentence, with the script's reason. The
research goes on as without `--engine`. The Deviations of the bundle
record it. A research whose Deviations name your engine has not
proved the row.

## Record and release

The row, its pair and the profile are one change of the forge. The
change is recorded and released as any change, the way
[Make a change to the forge](how-a-change-is-made.md) describes. The
scratch runs stay under `tmp/research/` for inspection. The run
folder is kept, never cleaned. Nothing in `tmp/` is a source of
truth.

## A worked example

An engine is added under the name `<name>`. The run folder of the
proof is `tmp/research/engine-trial/`, with two scratch packets
(`trial/` and `card-1/`), each holding a `packet.md` with one small
task.

The script now holds the engine in its three places:

- the row `<name>` in `ENGINES`;
- its two functions in `COMMANDS`;
- the row `<name>` in the header, below `antigravity` and in the same
  shape.

The settings path of the profile has moved into the two rows.

The trial:

```
python scripts/forge-engine.py <name> --packet tmp/research/engine-trial/trial --out tmp/research/engine-trial/trial/<name>.md --no-profile
```

The script answers:

```
<name> <version>: running on trial (timeout 1800s; no profile)
note written: tmp/research/engine-trial/trial/<name>.md (<n> chars; <n> turns, <n> s)
```

The front-matter of the note carries:

```
engine: <name>
model: engine default
usage: <the usage as the envelope gives it>
run: tmp/research/engine-trial/trial
status: immutable
```

The run with the profile:

```
python scripts/forge-engine.py <name> --packet tmp/research/engine-trial/card-1 --out tmp/research/engine-trial/card-1/<name>.md --allow-all --sandbox
```

The first line of the answer now ends with `profile` and the folder
of the profile. The profile lies in the run folder. The four things
of the check hold: a deny rule held, the shell was refused, the web
tools worked and the login was found.

The research:

```
/research --deep --engine <name> <topic>
```

The bundle `research/YYYY-MM-DD-<topic>/` holds one note
`<card>.<name>.md` per card, and its Deviations do not name `<name>`.
The row is proved, and the change is recorded and released.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags and
  exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
