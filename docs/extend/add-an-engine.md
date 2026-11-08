---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 9054996b757f438f
inputs:
  - scripts/forge-engine.py
  - .claude/skills/research/SKILL.md
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/40-solution-design.md#SOL.0870
---

# Add an engine

An engine is one row of the engine table of `scripts/forge-engine.py`
and its pair of functions in `COMMANDS`: one that builds the engine's
command line and one that reads the envelope the engine returns. This
page is for the extender who wants a model of another family to take
part in a deep research, and it says what the row holds, where the
profile of a run comes from, how the row is proved and how the change
is recorded and released. The forge is the workshop in which the
principal's thinking is forged; the principal is the person whose
thinking it is, and Claude is the cognitive extension that works it
with him.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first: an
engine is a change of the forge like any other, and it is proved,
recorded and released as any change is.

What the link to another engine is, and why it is a command-line tool
and not a library or a server, is explained in
[Another model family](../about/another-model-family.md). Every term
of the forge is in the [Glossary](../reference/glossary.md).

Three things hold for every engine and are not yours to change:

- The login is the user's. It is made once, outside the forge, in
  the engine's own tool. The forge carries no key, no account and no
  configuration of who connects. How the tool is installed and signed
  in is said by the tool's own documentation; the forge asks only
  that the tool is on PATH.
- The forge names engines and tiers, never models or versions.
  So that a name always means the newest of its kind: the version is
  the tool's, resolved at the call, and when a new version arrives
  nothing in the forge changes.
- The engine's tool must run in a one-shot, non-interactive shape:
  one prompt, one answer, a JSON envelope asked for, a time limit set
  and stdin closed. A tool that cannot run so has no row.

## The files

- `scripts/forge-engine.py`: the script. Its header lists the engine
  table, one row per engine, and says what the script does with a
  packet, the profile, the envelope and the flags. The table in the
  code is `ENGINES`; the pairs of functions are `COMMANDS`. The row
  `antigravity`, with its tool `agy`, is the one row the table has
  and the pattern a new row follows.
- `.claude/skills/research/SKILL.md`: the research command. Its
  opening paragraph says that `<name>` in `--engine <name>` is a row
  of the engine table and names the rows the table has today.
- `docs/reference/scripts.md`: the engine script with its flags and
  exit codes, in [Scripts](../reference/scripts.md).

## Steps

1. **Install the tool and sign in.** Follow the tool's own
   documentation. When you are done, the tool answers on PATH under
   its own name, and the login is found when the tool runs.
   You should now see the tool start from a shell without asking for
   an account.

2. **Choose the row's name.** The name is the engine, in lower case:
   the kind of tool, never a model and never a version. This name is
   what `/research --deep --engine <name>` takes.

3. **Add the row to `ENGINES`.** The row holds what the script needs
   to find and start the tool:
   - the executable, as it is called on PATH;
   - how the tool prints its version, and a version floor where a bug
     of the tool below some version is known. The script refuses a
     tool below the floor;
   - the flag that approves every tool call, which `--allow-all`
     passes;
   - the sandbox flag, where the tool has one, which `--sandbox`
     passes.

4. **Write the function that builds the command line.** It returns
   the engine's command in its one-shot shape:
   - the prompt, the one sentence the engine is started with (the
     default tells it to read `packet.md` in its workspace and do
     exactly what it says, the final message the whole note);
   - the packet folder added as the workspace;
   - the JSON envelope asked for;
   - the time limit, where the tool has a flag for it (the script
     enforces its own limit a minute later in any case);
   - and where the tool has them, the model word, the effort, the
     schema file, the sandbox and the flag that approves every tool
     call.
   The engine is given the packet folder as its workspace and runs in
   it, under the project's `tmp/`. Never the forge root. Because the
   forge root holds the hooks and the instance file, which an engine
   must not see or execute.

5. **Write the function that reads the envelope.** It takes the
   tool's output and returns whether the run succeeded, the response,
   the model, the usage and a reason where it failed. The script
   reads three things from the envelope:
   - a status that says success;
   - a response that is not empty. Exit 0 with an empty answer is a
     failure, not a note;
   - the usage.
   Say whether the model is in the envelope. Where it is not, the
   `--model` word is recorded, else "engine default".
   Enter the pair under the row's name in `COMMANDS`.

6. **Give the row its settings shape.** The script writes a per-run
   profile for the engine: a copy of the user's settings file for the
   engine, in the engine's own settings shape, with permissions added.
   The web is allowed. The shell, every write and the reading of every
   entry of the forge's tree but `tmp/` and the run's `hold/` folder
   are denied, the paths computed from where the script lies. The
   engine is started with HOME and USERPROFILE pointing at the
   profile, and the profile stays in the run folder as the record of
   the run. The user's own settings are never touched.
   The settings path of the profile is written for the first engine
   and moves into its row when a second engine comes: your step is to
   move it into the table and give your row its own. The price of
   this design is one settings shape to know per engine. Because
   the place of the run alone locks nothing: with every tool call
   allowed the engine reads any path on the disk, and the engine reads
   permission rules from its user-level settings file alone, which the
   forge never writes.

7. **Say the row in the research command.** The opening paragraph of
   `.claude/skills/research/SKILL.md` names the rows the table has
   today. Check that its sentence still holds with your row.

## Prove it

No check of the forge verifies a row of the table; the proof is three
runs, in this order, each typed as it stands. `<run>` is a run folder
under `tmp/research/`, and nothing under `tmp/` is a source of truth.

1. **The engine alone.** Make a scratch packet, a folder with a
   `packet.md` that asks one small question, and run the engine
   without the profile:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/trial --out tmp/research/<run>/trial/<name>.md --no-profile --allow-all --sandbox
   ```

   `--no-profile` runs the engine under the user's own settings. This
   is a trial and never a research: nothing of it is filed. You should
   now see the note written to `--out`, with `engine`, `model`,
   `usage`, `run` and `status: immutable` in its front-matter, and
   `envelope.json` saved beside the packet.

2. **The engine under the profile.** Run the same packet with the
   profile, in the form the research command uses:

   ```
   python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox
   ```

   Then check that the profile's deny rules hold: the shell is
   refused, no file of the forge's tree outside `tmp/` is read, the
   engine's web tools work and the login is found under the profile.
   The envelope beside the packet shows what the engine was denied.
   You should now see the note written, the run not refused, and the
   packet folder unchanged by the run. The script compares the folder
   before and after; a run that changed or added anything in it is
   refused and nothing is filed.

3. **A real research.** Run the command on a real question of a
   project:

   ```
   /research --deep --engine <name> <topic>
   ```

   The engine reviews the draft plan and then takes every card beside
   the session model, that is the model Claude itself runs on in the
   conversation. An engine that is named but unusable (not on PATH,
   no login, quota spent, an envelope that cannot be read) is said in
   one sentence with the script's reason; the research goes on
   without it and the Deviations of the bundle record it. You should
   now see one note per card from your engine in the bundle,
   `<card>.<name>.md`, and the synthesis stating the independence of
   the engines per card.

## Record and release

The change is recorded and released as any change of the forge; the
steps are on [Make a change to the forge](how-a-change-is-made.md).
What the record says for an engine: the row and its pair, the settings
shape the profile takes for it, and the three runs of the proof.

## A worked example

You have signed in to the tool of `<name>` and see it on PATH. You
add a row `<name>` to `ENGINES` with the executable, how the version
is printed, the flag that approves every tool call and the sandbox
flag; you set no floor, because no bug of the tool is known. You
write the two functions and enter them in `COMMANDS` under `<name>`:
the first builds the one-shot command with the prompt, the packet
folder as the workspace, the JSON envelope and the time limit; the
second reads the status, the response and the usage, and notes that
the model is not in the envelope, so that the `--model` word is
recorded. `<name>` is the second engine, so you move the settings
path of the profile out of the script's one place into the row of
`antigravity` and write the path of `<name>` into its own row.

You make `tmp/research/<run>/trial/packet.md` with one small question
and run the engine with `--no-profile`: the note comes back with
`engine: <name>` in its front-matter. You run the same packet with
the profile and read `envelope.json`: the shell was refused, no file
of the forge's tree was read, the web tools worked, and the packet
folder is unchanged. You run `/research --deep --engine <name>` on a
real question of a project and find one note per card from `<name>`
in the bundle. Then you record and release the change.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Another model family](../about/another-model-family.md): what the
  link to another engine is and why it is a command-line tool.
- [Scripts](../reference/scripts.md): the engine script, its flags
  and exit codes.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
