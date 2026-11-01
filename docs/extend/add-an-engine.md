---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: a8dc9a33b2a11f28
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that Claude can send one
packet of work to and get one note back from. This page is for the
extender who wants to add a new engine to the forge. It shows the one
row and the pair of functions you add to the engine script, and the
runs that prove the new engine works. Why the link to another engine
is a command-line tool, and what it is for, is explained in
[Another model family](../about/another-model-family.md).

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md).
  Adding an engine is recorded and released like any other change of
  the forge.
- Install the engine's own command-line tool, so that it is on PATH.
  If the tool is missing, the script stops and tells you to install
  it and log in once, outside the forge.
- Log in once, in the engine's own tool. The login is yours. The
  forge carries no key, no account and no configuration of who
  connects.
- Check that the tool has a one-shot, non-interactive shape: one call
  with a prompt that runs to the end and prints its answer.

The forge names engines, never models. The name you give the row is
the name everything else uses. The reason for naming engines rather
than models is not recorded.

## The files

- `scripts/forge-engine.py`: the engine script. It holds the table of
  engines, `ENGINES`, with one row per engine, and beside it
  `COMMANDS`, which pairs each row with its two functions. Its module
  header says in words what each row holds.

Nothing else is changed to add an engine. The research command picks
the engine up by the row's name: `<name>` in
`/research --deep --engine <name>` is a row of this table.

## Steps

1. **Add the row to `ENGINES`.** One row, under the name of the
   engine. The row holds:
   - the engine's command-line tool, as it is found on PATH;
   - how the tool reports its version;
   - a version floor, where a bug is known below it (the first row,
     `antigravity` with the tool `agy`, refuses versions below 1.1.1
     because of a known bug of its print mode on Windows);
   - the tool's flag that approves every tool call, where it has one;
   - the tool's sandbox flag, where it has one.

   You should now see the new name accepted as the first argument of
   `python scripts/forge-engine.py`.

2. **Write the function that builds the command line.** It gives the
   tool's one-shot call. It always carries:
   - the prompt;
   - the packet folder, added as the engine's workspace;
   - the request for the JSON envelope, that is, the structured
     answer the tool prints at the end of a run;
   - the time limit.

   Where the tool has them, it adds the model word, the effort, a
   schema for the final answer, the sandbox flag and the flag that
   approves every tool call. Each of these is passed only when the
   matching flag of the script is given.

3. **Write the function that reads the envelope.** It finds in the
   envelope:
   - a status that says success;
   - a non-empty response, since an exit with an empty answer is a
     failure;
   - the usage;
   - the model, where the envelope carries it. Where it does not, the
     script records the `--model` word, or "engine default".

   Write in the module header, under ENGINES, the row's call and the
   fields of its envelope, in the shape the first row has there.

4. **Pair the two functions in `COMMANDS`** under the row's name.

5. **Give the profile the engine's settings shape.** For every run
   the script writes a profile of the engine's own: a copy of your
   settings file for that engine, with permissions added. The
   permissions allow the web. They deny the shell, every write, and
   the reading of the forge's tree (every entry of the engine root
   but `tmp/`, and the folder where the first engine's notes wait).
   The engine is started with its home pointing at the profile, and
   your own settings are not touched. The settings path of the
   profile is written for the first engine. When you add a second
   engine, that path moves into the row of each engine. The price of
   this design is one settings shape to know per engine.

   You should now see a profile folder in the run folder after a run
   with the profile. It stays there as the record of the run.

## Prove it

Every run takes a packet folder: a folder holding `packet.md`, the
whole context of the run. The engine is given that folder as its
workspace. A run that changes or adds anything in that folder is
refused, and nothing is written.

1. **A trial of the engine alone.** Make a scratch packet under
   `tmp/research/` and run the engine without the profile:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --no-profile --allow-all --sandbox
   ```

   `--no-profile` runs the engine under your own settings. It is a
   trial and never a research: its note stays in `tmp/` and is filed
   nowhere. `--allow-all` is passed because a headless run denies a
   tool call it cannot ask about and then returns nothing.

   You should now see "note written" with the size of the answer, and
   a note at the `--out` path whose front-matter carries `engine`,
   `model`, `usage`, `run` and `status: immutable`.

2. **A run with the profile.** Run the same kind of packet under the
   per-run profile:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
   ```

   Then check that the profile's deny rules hold. With every tool
   call approved:
   - a read of a path the profile denies is refused as matching a
     deny rule;
   - the shell is refused;
   - the engine's own web tools work;
   - the login is found.

   You should now see the script name the profile in its first line,
   the note written, and the profile kept in the run folder.

3. **A real research.** Run the research command with the new engine
   on a real question:

   ```
   /research --deep --engine <name> <topic>
   ```

   You should now see the engine review the draft plan and take every
   card beside Claude. If the engine is named but cannot be used (not
   on PATH, no login, quota spent, an envelope that cannot be read),
   the research says so in one sentence with the script's reason,
   goes on without it, and records the deviation in the bundle.

4. **The engine check.**

   ```
   /check engine
   ```

   You should now see the check run on the engine and file nothing
   when it finds nothing.

**When the script refuses.** It exits 0 when the note is written. It
exits 1 with the reason on stderr when:
- the tool is missing;
- the version is below the floor;
- the packet has no `packet.md`;
- the run changed its folder;
- the envelope cannot be read, or the answer is empty.

The engine's own non-zero exit is reported with its stderr. The
envelope is saved beside the packet as `envelope.json` for
inspection, and the run folder is kept. The other flags of the script
and its exit codes are listed in [Scripts](../reference/scripts.md).

## A worked example

A row for a new engine `<name>`, written in the module header in the
shape the first row has, with the tool's own flags in place of the
placeholders:

```
<name>        `<tool> <one-shot flag> <prompt> <workspace flag> <packet>
               <json-output flag> <time-limit flag> <s>
               [<model flag>] [<effort flag>] [<schema flag>]
               [<sandbox flag>] [<approve-every-call flag>]`
              envelope: <status> (<success word> | ...), <response>,
              <usage>; the model is (or is not) in the envelope.
```

The row itself goes into `ENGINES` under `<name>`, and the pair of
its command builder and its envelope reader goes into `COMMANDS`
under the same name. The proof runs the trial with `--no-profile`,
then the run with the profile, then
`/research --deep --engine <name> <topic>`, then `/check engine`.

## Record and release

The new row is recorded and released as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) describes. The
words of the forge used here are each given in one line in the
[Glossary](../reference/glossary.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags and
  exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
