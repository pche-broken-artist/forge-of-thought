---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 1ee7cdbc88e9e8d7
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that the forge reaches through
its own command-line tool, and adding one means adding one row to the
engine table of `scripts/forge-engine.py`. This page is for an
extender who wants a second voice beside the session model (the model
Claude runs on in this conversation). It covers the files you touch,
the steps, and the commands that prove the new row works. What the
link to another engine is, and why it is a command-line tool, is
explained in [Another model family](../about/another-model-family.md).

## Before you start

- The way every change to the forge is proved, recorded and released
  is described in [Make a change to the forge](how-a-change-is-made.md).
  A new engine is recorded and released as any change of the forge.
- Install the engine's command-line tool so that it is on PATH.
- Log in once, in the engine's own tool, outside the forge. The login
  belongs to the person who runs the forge. The forge carries no key,
  no account and no configuration of who connects.
- Know the engine's one-shot shape. That is the way its tool is
  started once, non-interactively, with a prompt, and returns one
  answer and exits.
- Know the engine's settings shape. The script writes a settings file
  of its own for every run, in the engine's own format, so each engine
  costs one settings shape to know.

The forge names engines, never models. The row's name is the word you
give `/research --deep --engine <name>`. A model is chosen per run
with `--model`, and the note records it.

## The files

- `scripts/forge-engine.py`: the one script that runs one packet on an
  engine and brings its answer back as a note. Two names in it matter:
  - `ENGINES`: the table of engines, one row each.
  - `COMMANDS`: for each row, the pair of functions that serve it.
- The script's own help header, in the same file: its `ENGINES`
  section lists every row with its command line and its envelope, and
  gains a line for the new one.

The script's flags and exit codes are listed in
[Scripts](../reference/scripts.md). Terms of the forge such as packet,
note and principal are in [Glossary](../reference/glossary.md).

## Steps

1. **Add the row to `ENGINES`.** The row names the engine's tool, the
   arguments that make it print its version, and the engine's own
   words for two switches where it has them:
   - the flag that approves every tool call;
   - the sandbox flag.

   Where a bug of the tool is known, the row also carries a version
   floor. Below the floor the script refuses to run. The one row the
   forge has today is `antigravity`, whose tool is `agy`, with a floor
   set because of a known pipe bug of `agy -p` on Windows.

2. **Write the function that builds the command line.** It starts the
   engine's tool in its one-shot, non-interactive shape:
   - the prompt;
   - the packet folder added as the workspace;
   - the JSON envelope asked for (the structured answer the tool
     prints when the run ends);
   - a time limit.

   Where the engine has them, the function also passes:
   - the model (`--model`);
   - the effort (`--effort`);
   - a JSON schema for the answer (`--schema`);
   - the sandbox flag (`--sandbox`);
   - the flag that approves every tool call (`--allow-all`).

   You should now see the same shape as the row `antigravity` in the
   header: `agy -p <prompt> --add-dir <packet> --output-format json
   --print-timeout <s>s --disable-slash-commands`, with the optional
   flags after it.

3. **Write the function that reads the envelope.** It returns whether
   the run succeeded, the answer, the model where the envelope names
   it, and the usage. The script reads these fields:
   - a status that says success;
   - a non-empty response;
   - the usage.

   Exit 0 with an empty answer is a failure. Say in the header whether
   the model is in the envelope. Where it is not, as for `antigravity`,
   the `--model` word is recorded, else "engine default".

4. **Add the pair to `COMMANDS`** under the row's name.

5. **Give the profile a settings path for the new engine.** For every
   run the script writes a per-run profile. That is a copy of the
   user's settings for the engine, in the engine's own settings shape,
   with these rules added:
   - the web allowed;
   - the shell denied;
   - every write denied;
   - the reading of the forge's tree denied, except `tmp/`;
   - the reading of the run's `hold/` folder denied, where the first
     engine's notes wait.

   The engine is then started with its home pointing at that profile.
   The user's own settings are never touched, and the profile stays in
   the run folder as its record. The settings path of the profile is
   written in the script for the first engine. When a second engine
   comes, that path moves into each engine's row. You should now see
   one settings path per row and none left in the profile function.

6. **Add the row's line to the header's `ENGINES` section**: the
   command line, the envelope's fields, whether the model is in the
   envelope, and the version floor where there is one.

## Prove it

Make the proof in the order below. Each step rests on the one before.

1. **A trial of the engine alone.** Make a scratch packet folder under
   `tmp/research/` holding a `packet.md` that asks for a short answer
   and needs no tool. Run it without the profile:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/trial --out tmp/research/<run>/trial/<name>.md --no-profile
   ```

   `--no-profile` runs the engine under the user's own settings. It is
   a trial, never a research. You should now see the line
   `note written:` and a note whose front-matter carries `engine`,
   `model`, `usage`, `run` and `status: immutable`. The envelope is
   kept beside the packet as `envelope.json`.

2. **A run with the profile.** Run a packet as the research runs it:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
   ```

   Then check that the profile's deny rules hold. Give the packet a
   request to read a file of the forge's tree outside `tmp/` and to run
   a shell command. You should now see both refused by the engine
   while its web tools still work, and the login still found.

3. **A real research.** Run the command on a real question:

   ```
   /research --deep --engine <name> <topic>
   ```

   You should now see a note `<card>.<name>.md` beside the session
   model's note for each card of the bundle.

4. **The checks.** Run `/check engine`.

## A worked example

You add the engine `<name>`, whose tool `<tool>` prints a JSON
envelope with a status, a response and the usage, and no model.

- `ENGINES` gains the row `<name>`: the tool `<tool>`, its version
  arguments, its flag for every tool call and its sandbox flag.
- `COMMANDS` gains `<name>` with its pair of functions. One builds
  `<tool>` with the prompt, the packet folder as workspace, the JSON
  envelope and the time limit. The other reads the status, the
  response and the usage.
- The profile's settings path moves from the script into the rows
  `antigravity` and `<name>`.
- The header's `ENGINES` section gains the line for `<name>`, saying
  that the model is not in the envelope.
- The trial with `--no-profile` writes `tmp/research/<run>/trial/<name>.md`.
  The run with the profile writes its note, and the deny rules hold.
- `/research --deep --engine <name> <topic>` files one note per card
  from `<name>`.

## If something goes wrong

The script exits 1 and gives its reason on standard error when:

- the tool is not on PATH (install the engine's tool and log in once,
  outside the forge);
- the tool did not report a version;
- the version is below the floor ("update it");
- the packet folder holds no `packet.md`;
- the note named by `--out` exists (a note is immutable, so choose
  another name);
- the engine did not finish within the time limit and one minute more;
- the run changed or added anything in its packet folder (nothing is
  filed, and the output is kept in `envelope.rejected.json`);
- the envelope cannot be read, or the status is not success, or the
  answer is empty.

An empty answer with a success status may come from a headless run,
that is, one with nobody to answer a question. Such a run denies every
tool call it cannot ask about. The script then names the denied tool
calls and suggests `--allow-all` with `--sandbox`. The engine's own
non-zero exit is reported with its standard error.

## Record and release

Record and release the new engine as described in
[Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags and
  exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
