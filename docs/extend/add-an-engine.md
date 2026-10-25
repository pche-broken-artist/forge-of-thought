---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 4ba9cea4af77f3d3
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is a model of another family that Claude can hand a
research packet to, reached through that model's own command-line
tool. This page is for the extender who wants the forge to reach one
more engine. It shows what the one row of the engine table holds,
which files it touches, and how the new row is proved before it is
used on a real question.

## Before you start

Adding an engine is a change to the forge. It is proved, recorded
and released as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) describes.
What the link to another engine is, and why it runs over a
command-line tool, is explained in
[Another model family](../about/another-model-family.md).

Three things hold before any row is written:

- The forge names engines, never models.
  A row has an engine's name; a model is at most a word passed to
  the engine for one run.
- The forge carries no key, no account and no configuration of who
  connects.
  The login is yours, made once in the engine's own tool, outside the
  forge.
- An engine is one row of the table, "add a row, never a branch".
  Nothing else in the forge learns the engine's name.

The engine's tool must have a one-shot, non-interactive shape: it
takes one prompt, runs once and prints its answer. This shape is
shared by the command-line tools the forge has looked at, which is
why a new engine fits as a row.

## The files

- `scripts/forge-engine.py`: the engine script.
  Its help header lists the engines under ENGINES, one row each, and
  its table of engines in the code holds the same row.
  Its flags and exit codes are listed in
  [Scripts](../reference/scripts.md).
- `.claude/skills/research/SKILL.md`: the definition of `/research`.
  It names no engine of its own; `<name>` in
  `/research --deep --engine <name>` is a row of the table.

The only row the table has today is `antigravity`, whose tool is
`agy`. Its header row reads:

```
antigravity   `agy -p <prompt> --add-dir <packet> --output-format json
               --print-timeout <s>s --disable-slash-commands
               [--model] [--effort] [--json-schema] [--sandbox]
               [--dangerously-skip-permissions]`
              envelope: status (SUCCESS | ERROR | ...), response,
              usage, duration_seconds, num_turns; the model is not
              in the envelope, the --model word is recorded.
```

## Steps

1. **Choose the name.**
   The row's name is the word the script takes as its first argument
   and the word `/research --deep --engine <name>` takes.
   It is the engine's name, never a model's.

2. **Write the command line of the engine's tool in its one-shot
   shape.**
   The row gives, in the engine's own flags:
   - the prompt the engine is started with;
   - the packet folder, added as the engine's workspace;
   - the request for the JSON envelope (the structured answer the
     tool prints at the end of a run);
   - a time limit, where the tool has a flag for one.

   Where the tool has them, the row also gives:
   - the model word (`--model` of the script);
   - the effort (`--effort`);
   - a schema the final answer must follow (`--schema`);
   - the sandbox flag (`--sandbox`);
   - the flag that approves every tool call (`--allow-all`).

   A headless run cannot ask for a permission. It denies a tool call
   it cannot ask about and returns nothing, so the flag that approves
   every call is what lets the engine read at all, and the sandbox
   contains it.

3. **Say what the script reads from the envelope.**
   The script needs three things from it:
   - a status that says success;
   - a response that is not empty;
   - the usage.

   Say whether the model is in the envelope. Where it is not, the
   `--model` word is recorded in the note; with neither, the note
   says "engine default". An exit of 0 with an empty answer counts as
   a failure.

4. **Set a version floor where a bug is known.**
   The script checks the tool's version before every run and refuses
   below the floor. The `antigravity` row has one, 1.1.1, for a known
   bug of its print mode on Windows. Where no bug is known, the
   inputs give no floor to set.

5. **Know the shape of the engine's own settings file.**
   The script does not run the engine under your own settings. It
   writes a profile for the run (a copy of your settings for that
   engine with permission rules added) in the shape of the engine's
   settings file:
   - the web allowed;
   - the shell denied;
   - every write denied;
   - the reading of every entry of the forge's tree but `tmp/`
     denied, and the reading of the run's `hold/` folder, where the
     first engine's notes wait.

   The engine is started with its home folder pointing at that
   profile. Your own settings are never touched, and the profile
   stays in the run folder as its record. The price of the profile is
   one settings shape to know per engine, kept in the engine's row.

6. **Install the tool and log in once**, in the engine's own tool,
   outside the forge. The script finds the tool on PATH; it never
   logs in for you.

## Prove it

The proof runs in three steps, from the engine alone to a real
question, and ends with the engine check.

1. **A trial of the engine alone**, without the profile, on a scratch
   packet under `tmp/research/`. The packet is a folder holding one
   file, `packet.md`, which carries the whole context of the run.
   This is a trial and never a research.

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<trial>/<card> --out tmp/research/<trial>/<card>/<name>.md --no-profile
   ```

   You should now see the line `note written:` with the note's path,
   and the note under `--out` with `engine`, `model`, `usage`, `run`
   and `status: immutable` in its front-matter.

2. **A run with the profile**, as `/research` makes it:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
   ```

   You should now see the run start with "profile" and the profile's
   path instead of "no profile", and the profile under `.home` in the
   run folder. Then check that the profile's deny rules hold:
   - a deny rule holds while every tool call is approved;
   - the shell is refused;
   - the engine's own web tools work;
   - the login is found.

   How each of these is checked is not recorded beyond this list.

3. **A real research** on a real question:

   ```
   /research --deep --engine <name> <topic>
   ```

   You should now see the engine review the draft plan and then take
   every card beside the session model (the model Claude runs on in
   this conversation). An engine that cannot be used is said in one
   sentence with the script's reason, and the research goes on
   without it.

4. **The engine check**:

   ```
   /check engine
   ```

The script refuses with exit code 1 and the reason on its error
output in these cases:

- the tool is not on PATH;
- the tool's version is below the floor, or it reports none;
- the packet has no `packet.md`;
- the note under `--out` already exists, since a note is immutable;
- the run changed or added anything in the packet folder (its output
  is kept in `envelope.rejected.json` and nothing is filed);
- the envelope cannot be read, or the answer is empty;
- the run did not finish in time.

The engine's own non-zero exit is reported with its error output.
The envelope of every run is kept beside the packet as
`envelope.json`, and the run folder is never cleaned.

## Record and release

The new row is recorded and released as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

You add an engine named `<name>` whose tool is `<tool>`.

1. You write the row of `<name>` in the header's ENGINES section and
   in the table of engines: the one-shot command of `<tool>` with its
   prompt, workspace, JSON envelope and time limit flags, and its
   model, effort, schema, sandbox and approve-all flags where it has
   them. You note which envelope fields say success, carry the
   response and carry the usage, and whether the model is among them.
   You set a version floor only if a bug of `<tool>` is known. You
   note the shape of `<tool>`'s settings file for the profile.
2. You log in once in `<tool>` itself.
3. You make `tmp/research/<trial>/<card>/packet.md` with a small
   question and run the trial with `--no-profile`. The note appears
   under `--out`.
4. You run the same packet shape with `--allow-all --sandbox` under
   a new run folder, read the profile under `.home`, and confirm the
   shell and the forge's tree are refused while the web works.
5. You run `/research --deep --engine <name> <topic>` on a real
   question, then `/check engine`.
6. You record and release the change.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags
  and exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
