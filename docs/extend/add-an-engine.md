---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: e568e5fd2ee44b6e
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that the forge reaches over
that model's own command-line tool, and it is added as one row of the
engine table in `scripts/forge-engine.py`. This page is for the
extender who wants a new engine beside the one the table holds today:
what the row holds, what stands beside it in the script, how the row
is proved and how the change is recorded and released. What the link
to another engine is, and why it runs over a command-line tool, is
explained on [Another model family](../about/another-model-family.md).

## Before you start

- A new engine is a change to the forge like any other. How a change
  is proved, recorded and released is on
  [Make a change to the forge](how-a-change-is-made.md); the addition
  is recorded and released as any change of the forge.
- The engine's tool must be installed and signed in before you begin.
  How the tool is installed and how the login is made is said by the
  tool's own documentation; the forge asks only that the tool is on
  PATH. The login is the user's, made once in the engine's own tool.
  The forge carries no key, no account and no configuration of who
  connects.
- The tool must have a one-shot, non-interactive shape: it takes a
  prompt, runs once with its standard input closed and returns a JSON
  envelope. The command-line tools the forge has looked at share this
  shape.
- You must know the engine's own settings shape: where the tool reads
  its user-level settings file and how a permission rule is written
  in it. The script writes a per-run profile in that shape (Steps,
  below). The price of a new engine is one more settings shape to
  know.
- The forge names engines and tiers, never models or versions. The
  name of the row is the engine's name, such as `antigravity`, never
  a model or a version number. A name then always means the newest
  of its kind: when a new version of the tool arrives, nothing in the
  forge changes, and everything that ran on that name runs on the new
  one. The model is the tool's own default, or the `--model` word
  given at the call.

## The files

| File | What changes |
|---|---|
| `scripts/forge-engine.py` | one row in the table `ENGINES` and its pair in `COMMANDS`; the header's ENGINES section gains the row in the shape the first row has |
| `tmp/research/<run>/` | the scratch packet of the proof: a trial, never a research; nothing under `tmp/` is a source of truth |

The flags and the exit codes of the script are listed on
[Scripts](../reference/scripts.md).

## Steps

1. Learn the tool's one-shot shape from its own documentation. The
   row needs these parts of it:
   - the flag that gives the prompt
   - the flag that adds a folder as the workspace
   - the flag that asks for the JSON envelope
   - the flag that sets a time limit
   - where the tool has them: the model, the effort, a schema the
     final answer is shaped by, the sandbox, and the flag that
     approves every tool call
   - the fields of the envelope: the status that says success, the
     response, the usage, and whether the model is in the envelope
   - a version floor, where a bug of the tool is known

2. Add the row to `ENGINES`. The row names the executable, the
   version floor where one is known and how the version is asked, the
   flag that approves every tool call and the sandbox flag. The name
   of the row is the engine's name. The script finds the executable
   on PATH and checks its version against the floor; below it the
   script refuses the run.

3. Add the row's pair to `COMMANDS`: one function that builds the
   engine's command line and one that reads its envelope. The command
   line is the one-shot shape of step 1 with the packet folder added
   as the workspace, the JSON envelope asked for and the time limit
   set, and the model, the effort, the schema, the sandbox and the
   approve-all flag passed where the script was given them. The
   envelope reader must find a status that says success and a
   non-empty response, and it takes the usage; exit 0 with an empty
   answer is a failure. Where the model is in the envelope the reader
   takes it; where it is not, the `--model` word is recorded, else
   "engine default".

4. Give the profile the engine's settings shape. The script writes a
   per-run profile: a copy of the user's settings for the engine with
   permissions added. The web is allowed. The shell, every write and
   the reading of every entry of the engine root but `tmp/` and of
   the run's `hold/` folder are denied. The paths are computed from
   where the script lies, and the engine is started with HOME and
   USERPROFILE pointing at the profile. The settings path of the
   profile is written for the first engine; when the second engine
   comes, it moves into its row, so that each row says where its
   engine reads its settings. The profile stays in the run folder as
   its record; the user's own settings are never touched.

   The profile is needed because the place of the run alone locks
   nothing. With every tool call approved the engine reads any path
   on the disk, and it reads permission rules from its user-level
   settings file alone, which the forge never writes.

5. Write the row into the script's header, in its ENGINES section, in
   the shape the first row has: the command line with its flags, the
   fields of the envelope and whether the model is in it. The header
   is where the table is read by a person; a row that is not in it
   is not documented.

## Prove it

No check verifies a row of the table. The proof is three runs, in
this order, each on a packet (the folder that is the whole context of
one run, holding a `packet.md`; the word is in the
[Glossary](../reference/glossary.md)).

1. A trial of the engine alone. Make a scratch packet under
   `tmp/research/`: a folder with a `packet.md` that says what the
   engine is to do and in what shape it is to answer. Then run

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --no-profile
   ```

   `--no-profile` runs the engine under the user's own settings, with
   no per-run profile. This is a trial, never a research: nothing of
   it is filed in a project. You should now see exit 0, the note at
   `--out` with `engine`, `model`, `usage`, `run` and
   `status: immutable` in its front-matter, and `envelope.json` saved
   beside the packet.

2. A run with the profile. On the same packet, run

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
   ```

   `--allow-all` passes the engine's flag that approves every tool
   call; `--sandbox` passes its sandbox flag where it has one. Check
   that the profile's deny rules hold: the profile the script left in
   the run folder carries the permissions in the engine's own
   settings shape, a tool call against the forge's tree or the shell
   is denied, the engine's own web tools work and the login is found.
   A rule written in a shape the engine does not read is no rule, and
   the trial of step 1 cannot have shown it. You should now see the
   same note and envelope as in step 1, and the profile kept in the
   run folder.

3. A real research. Run

   ```
   /research --deep --engine <name> <topic>
   ```

   on a real question of a project. The engine reviews the draft plan
   and takes every card beside Claude's own agents; `<name>` is the
   row's name, and the option takes nothing else. You should now see
   the engine's additions beside the draft plan, marked as the
   engine's, and after the dispatch one note `<card>.<name>.md` per
   card in the bundle.

A refusal of the script is exit 1 with the reason on standard error:
the tool missing, the version below the floor, a packet without
`packet.md`, the folder changed by the run, the envelope unreadable or
the answer empty. The engine's own non-zero exit is reported with its
standard error. A run that changed or added anything in the packet
folder is refused and nothing is filed: read-only is verified, never
trusted. In a research, an engine named but unusable is said in one
sentence with the script's reason, the research goes on as without
`--engine`, and the Deviations of the bundle record it.

## Record and release

The row, its pair in `COMMANDS` and the header's line are one change
to the forge. Once the three runs have passed, the change is recorded
and released as any change of the forge, the way
[Make a change to the forge](how-a-change-is-made.md) gives. From
then on `<name>` is what `/research --deep --engine <name>` takes.

## A worked example

An engine `<name>` whose tool is `<tool>`, added as the second row of
the table.

1. You read the documentation of `<tool>` and find its one-shot
   shape: a flag for the prompt, a flag that adds a folder as the
   workspace, a flag for a JSON envelope, a flag for a time limit, a
   sandbox flag and a flag that approves every tool call. Its
   envelope carries a status, a response, the usage and the model. No
   bug of the tool is known, so the row carries no floor.
2. You add the row `<name>` to `ENGINES`: `<tool>` as its executable,
   how its version is asked, its approve-all flag and its sandbox
   flag.
3. You add the pair to `COMMANDS`: the function that builds the
   command line of `<tool>` from the row and the script's flags, and
   the function that reads its envelope, which takes the model from
   the envelope since it is there.
4. The table now has two rows, so the settings path of the profile
   moves from where it was written for the first engine into each
   row: the row `antigravity` keeps its own, the row `<name>` gets
   the path where `<tool>` reads its user-level settings.
5. You write the row into the header's ENGINES section, in the shape
   of the row `antigravity`.
6. You make `tmp/research/<run>/<card>/packet.md`, a short task with
   the shape of the answer, and run the trial with `--no-profile`.
   The run exits 0; the note stands at `--out` with its front-matter
   filled; `envelope.json` lies beside the packet.
7. You run the same packet with `--allow-all --sandbox`. The profile
   lies in the run folder in the settings shape of `<tool>` with the
   web allowed and the shell, the writes and the forge's tree denied;
   the note and the envelope are as before.
8. You run `/research --deep --engine <name> <topic>` on a real
   question. The engine's review of the draft plan is shown beside
   the draft, marked as the engine's; after the dispatch each card has
   its `<card>.<name>.md` in the bundle.
9. You record and release the change as any change of the forge.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags
  and exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
