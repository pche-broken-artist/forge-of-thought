---
generated: 2026-10-10
made: derived
inputs-hash: aeb88836dff8679e
inputs:
  - CLAUDE.md
  - scripts/forge-status.py
  - scripts/forge_repos.py
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# Add a script

This page is for someone extending the forge who wants to add a
script to `scripts/`. It says what a script is, the rules every
script keeps, how it carries its own help, how it shares code with
its neighbours, and how the engine is told that it exists. It was
put together from `CLAUDE.md` (Persistence, Portability, and
Document chain), the forge intent and solution design, the agent
`check-engine`, and two existing scripts taken as models:
`scripts/forge-status.py` for a command and `scripts/forge_repos.py`
for a shared module.

## What a script is

The forge is a set of instructions that Claude Code reads; the
deterministic work at its edge is kept in scripts. `scripts/` is the
only platform-bound layer of the forge, and it is written so that it
runs unchanged beyond Windows. A script is Python 3.8 or newer, run
as `python scripts/<name>.py`. `python` on PATH is the one
prerequisite of the whole set; a system that has only `python3`
gives it that name. The scripts are Python because the forge's users
asked for it, and because the document conversion already needed
Python.

Portability is a writing rule, not a claim: the set is written to
run on Linux and macOS, and what you add is held to the same rule.

## Before you start

Decide what the script is for and check that nothing already does
it. Three families exist, each with a shared module beside it:

- the git scripts, `forge-save`, `forge-pull`, `forge-status`,
  `forge-clone` and `forge-branch`, sharing `forge_repos.py`;
- the conversions, `doc2md`, `md2pptx` and `md2docx`, sharing
  `forge_tools.py`;
- the documentation scripts, `docs-state`, `docs-index` and
  `docs-check`, sharing `docs_map.py`.

Beside them stands `hook-walkthrough`, the per-prompt hook that
`.claude/settings.json` starts with `python`.

How many scripts there are is not a rule. What is a rule is that a
mechanism lives in one place: a procedure stated in two places is a
defect. If your script would restate what a command, a skill or
another script already does, the right move is to use that one
through its own definition.

## Step 1: write the script by the rules of the set

Every script keeps these rules, taken from the Portability rule of
`CLAUDE.md` and the solution design:

- Nothing Windows-only. Paths are composed with `pathlib`, never
  with string concatenation or a platform separator.
- Processes run through `subprocess` with an argument list, never
  through a shell. The model: `forge_repos.py` runs git as
  `["git", *args]` with `cwd` set, output captured as UTF-8 text.
- External tools (`git`, `markitdown`, `pandoc`, `claude`) are
  resolved from PATH. A script that needs one looks for it first
  and stops with a plain message when it is absent, as
  `forge_repos.py` does for git; it does not go and fetch it.
- Colour only on a terminal. `forge_repos.py` prints colour when
  standard output is a terminal and `NO_COLOR` is not set, plain
  text otherwise.
- Options in the Python spelling of `argparse` (`--tag`,
  `--engine`, `--recipe`, `--reference`, `--template`,
  `--page-size`, `-o`), because that is the convention of the
  language.
- No URL and no identity in the script. The commit identity is
  git's, resolved by the user's own configuration; the remote is the
  user's one-off act. A script that carried either would duplicate
  what the user already keeps.
- Usage examples free of Windows-specific paths and invocations.

A command script ends by returning an exit code from `main()` and
runs only when invoked directly; `forge-status.py` is the smallest
model of this shape.

## Step 2: write the help into the module docstring

Each script carries its help in its module docstring, and that
docstring is the owner of the facts about the script. Commands and
`CLAUDE.md` cite the header and never restate it: the layout
comment names the script in a few words, and a command that uses it
says "how it runs and what it needs installed is the script's
header's". So whatever a reader must know to run your script has to
be in the docstring, because nowhere else will say it.

`forge-status.py` is the model. Its docstring opens with a one-line
statement of what the script is, then four sections:

- **SYNOPSIS**: the invocation, `python scripts/<name>.py` with its
  arguments.
- **WHAT IT DOES**: what happens, in plain sentences, and why the
  script exists (for `forge-status`, so that even reading git state
  goes through the scripts).
- **WHAT IT NEEDS**: the Python version, the tools it expects on
  PATH, and the shared module beside it.
- **EXAMPLES**: invocations as they are typed, with no
  platform-specific path in them.

Where the script takes options or writes a file, the docstring says
the options and where the output lands: for the conversions,
`CLAUDE.md` leaves exactly those facts (what each needs installed,
how a template or a reference document is named, where the output
lands, what becomes of a diagram) to the header.

## Step 3: share through a module, never by copying

What several scripts share lives in one module beside them, imported
by path, never twice. A shared module is not a command: it has no
`main()`, and its docstring opens with what it holds and says "Not a
command". `forge_repos.py` is the model: it holds the engine root
(the parent of `scripts/`), the git check, the list of repositories
a bare or a slug form visits, running git, and coloured output.

A command script reaches its module by putting its own directory on
the import path before importing, as `forge-status.py` does, so that
the script runs from any working directory.

If your script belongs to one of the three families, use its
module. If it needs something two or more scripts of the set would
also need, put that in the module rather than in each script. Add a
new module only when a new family exists; a module for one script
is a script with its code split in two.

## Step 4: name it in `CLAUDE.md`

The layout comment of `CLAUDE.md` names every script in `scripts/`
in a few words, grouped by family, and the Persistence section names
the shared modules. Add yours to the layout comment, and if it is a
git script, to the sentence under Persistence that lists what each
git script does.

Where a command uses the script, the command names it by path in
its skill file; the command does not describe how the script runs.
The one description of the script is its docstring.

## Step 5: run the engine check

`/check engine` verifies scripts on disk against `CLAUDE.md`: every
file in `scripts/` must be described there, in the layout comment
and its governing rule, and nothing described there may be missing
on disk. It also verifies that the commands table matches the skills
and that the agents named exist. A script added without its line in
`CLAUDE.md`, or a line without its script, is a finding at the next
release, where this check runs. Run it when you are done, and
settle what it finds.

## What a script may do with git

The scripts are the only door to git, reading state included. The
deny rules of `.claude/settings.json` keep Claude from raw `git`, so
whatever the forge must do in a repository has to be a script. If
your script touches git, it does so through `forge_repos.py`, it
carries no URL and no identity, and it reports or refuses aloud when
a repository is not what it expects: `forge-status.py` says "not
under git" and "no origin" rather than guessing, and
`forge_repos.py` refuses to run when the engine itself is not a
repository.

## See also

- [Scripts](../reference/scripts.md): the scripts that exist.
- [About persistence in git](../about/persistence-in-git.md): why
  the scripts are the only door.
