---
generated: 2026-10-09
made: derived
inputs-hash: d564b9dd02d3f193
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
script to `scripts/`: what a script is made of, the rules every
script keeps, where shared code goes and how the engine knows the
script exists. It was put together from `CLAUDE.md` (Persistence and
its Portability paragraph, Document chain, the layout comment and
prime directive 10), from `scripts/forge-status.py` and
`scripts/forge_repos.py` as the models, from the `check-engine` agent
and from the forge intent and solution design, which give the
reasons.

## What a script is

A script is a Python file in `scripts/`, Python 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is the one prerequisite
of the whole set; a system that has only `python3` gives it that
name. `scripts/` is the only platform-bound layer of the forge, and
it is written to run unchanged on Linux and macOS. That is a writing
rule, not a claim: the intent says portability is verified by
running the set on Linux, and until then it is a rule the writer
keeps. The set was rewritten into Python on 2026-10-09 and tested
that day against a fixture; it has not been run on Linux.

Options are spelled the Python way, through argparse: long names
such as `--tag`, `--engine`, `--recipe`, `--reference`,
`--template`, `--page-size`, and `-o` for the output.

## The docstring owns the help

Each script carries its help in its module docstring, the string at
the top of the file. The docstring is the owner of the facts about
the script; a command that uses the script, and `CLAUDE.md`, cite
it and never restate it. `CLAUDE.md` says so of the conversions
outright: what each needs installed, how a template or a reference
document is named, where the output lands and what becomes of a
diagram "is its header's".

`scripts/forge-status.py` is the smallest model. Its docstring opens
with the script's name and, after a spaced hyphen, one sentence of
what it does; then four parts follow, each under a capitalised
heading:

1. `SYNOPSIS`: the invocation, `python scripts/<name>.py` with its
   options.
2. `WHAT IT DOES`: what the script does and what it changes (or that
   it is read-only and changes nothing), and why it exists, citing
   the section of `CLAUDE.md` that wants it.
3. `WHAT IT NEEDS`: the Python version, the external tools on PATH,
   and the shared module beside it that it imports.
4. `EXAMPLES`: usage examples, free of platform-specific paths and
   invocations.

Where the script writes something, the docstring also says where
the output lands.

## Rules every script keeps

These are the rules of `CLAUDE.md`, Portability, and of the solution
design; `forge_repos.py` shows each of them in use.

- Nothing Windows-only: the script runs the same everywhere.
- Paths through `pathlib`. The engine root, for example, is the
  parent of the directory the script lies in, found from
  `Path(__file__)`, never from a hard-coded path.
- Processes through `subprocess` with argument lists, never a shell.
  Git is run as `["git", *args]` in a working directory the script
  passes, with its output captured as text.
- External tools (`git`, `markitdown`, `pandoc`, `claude`) resolved
  from PATH. A script that needs one checks for it first
  (`shutil.which`) and stops with a plain error when it is missing.
- Colour only on a terminal. Coloured output is written only when
  standard output is a terminal and `NO_COLOR` is not set; otherwise
  the plain text.
- Usage examples in the help free of Windows-specific paths and
  invocations.
- No URL and no identity in the script. Instance facts are out of
  the scripts: no remote URL, no author identity, no first-run
  initialisation. Git configuration is the user's, and the forge
  sets none.

## What is shared lives in one module

What several scripts share lives in one module beside them, imported
by path, never written twice. A shared module is not a command: it
has no synopsis and is never run on its own, and its docstring says
so ("Not a command"), as `scripts/forge_repos.py` does. A script
reaches it by putting its own directory first on `sys.path` and
importing the module by name.

There are three:

| Module | Serves | Holds |
|---|---|---|
| `forge_repos.py` | the git scripts (`forge-save`, `forge-pull`, `forge-status`, `forge-clone`, `forge-branch`) | the engine root, the git check, the list of repositories a bare or a slug form visits, running git, coloured output |
| `forge_tools.py` | the conversions (`doc2md`, `md2pptx`, `md2docx`) | a tool on PATH, resolving paths, the headless Claude Code run |
| `docs_map.py` | the documentation scripts (`docs-state`, `docs-index`, `docs-check`) | the reader of the documentation map |

A new script that needs what one of these holds imports it; a new
script that needs something two scripts will share puts it into the
module its family uses, not into both scripts.

## Git is the scripts' alone

The scripts in `scripts/` are the only door to git, reading state
included, no exceptions. For Claude this is enforced by the deny
rules of `.claude/settings.json`. A script that touches git is
therefore the one place where git is touched: `forge-status.py`
exists so that even reading git state goes through the scripts, and
its docstring says so. How many git scripts there are is not a rule.

## Steps

1. Write the script in `scripts/`, Python 3.8 or newer, with the
   docstring as the section above shapes it and the rules above
   kept. Put what it shares with its family into the family's shared
   module and import it by path.
2. Name the script in the layout comment of `CLAUDE.md`, the
   `scripts/` line of Repository layout, where every script of the
   set is listed with a few words of what it is for. A git script is
   also named in Persistence, which says what each one does.
3. Where a command uses the script, the command names it by path in
   its skill, and cites the docstring for what the script needs and
   where its output lands, without restating it. One mechanism lives
   in one place: a procedure stated twice is a defect.
4. Run `/check engine`. The check verifies scripts on disk against
   `CLAUDE.md`: every file in `scripts/` is described in the layout
   comment and its governing rule, and nothing described there is
   missing on disk. A script added without its line in `CLAUDE.md`,
   or a line without its script, is a finding.

The per-prompt hook that repeats the walkthrough rule at every
prompt, `scripts/hook-walkthrough.py`, is a Python script too,
started by `python` from `.claude/settings.json`.

## See also

- [Scripts](../reference/scripts.md): the scripts that exist.
- [About persistence in git](../about/persistence-in-git.md): why the scripts are the only door.
