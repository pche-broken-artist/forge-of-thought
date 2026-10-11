---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 47d8db7229ff082d
inputs:
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#Repository layout
  - scripts/forge-status.py
  - scripts/forge_repos.py
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/40-solution-design.md#Across the parts
---

# Add a script

A script of the forge is a Python file in `scripts/`, run as
`python scripts/<name>.py`, that carries its own help in its module
docstring and shares what it has in common with its neighbours
through one module beside it. This page is for the extender who
wants to add one: it says what files are touched, how the script is
written so that it runs unchanged on Linux and macOS, how it is
proved and how the change is recorded. The scripts are the only
layer of the forge that is bound to a platform; why they are the one
door to git is said on [Persistence in git](../about/persistence-in-git.md),
and the scripts that exist today are listed on
[Scripts](../reference/scripts.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md): a new
script is a change of the engine (the forge itself, as opposed to a
project run through it: see the [Glossary](../reference/glossary.md))
and is recorded and released as any change of the forge.

Two things hold before a line is written.

- The rules below are writing rules. Portability is proved by
  running the whole set of scripts on Linux. Until that has been
  done it is not claimed.
- Nothing of the instance (one installation of the forge) enters a
  script: no remote URL, no author identity, no first-run
  initialisation. Git configuration belongs to the user.

## The files

- `scripts/<name>.py`: the script itself, a new file.
- One shared module beside it, only where the script shares
  something with its family:
  - `scripts/forge_repos.py` for a git script, that is, one that
    joins `forge-save`, `forge-pull`, `forge-status`, `forge-clone`
    and `forge-branch`
  - `scripts/forge_tools.py` for a conversion, that is, one that
    joins `doc2md`, `md2pptx` and `md2docx`
  - `scripts/docs_map.py` for a documentation script, that is, one
    that joins `docs-state`, `docs-index` and `docs-check`
- `CLAUDE.md`, Repository layout: the comment on the `scripts/`
  line, where every script is named with a phrase of what it does.
- `CLAUDE.md`, Persistence (git): the sentence that names each git
  script with one clause, touched only when the new script is a git
  script.
- `.claude/settings.json`, touched only when the new script is a
  hook: a hook is started by `python` from there.

## Steps

1. Create `scripts/<name>.py` for Python 3.8 or newer, started as
   `python scripts/<name>.py`. `python` on PATH is the one
   prerequisite of the scripts. A system that has only `python3`
   gives it that name; the script does not.

2. Open the file with its module docstring. The docstring is the
   one place the facts of the script stand; CLAUDE.md names the
   script in a phrase and leaves the full description to this
   header. It holds, in this order:
   - the first line: `<name>.py - ` and what the script does, in
     one sentence
   - `SYNOPSIS`: the line as it is typed, with its options in
     brackets
   - `WHAT IT DOES`: what happens, what it changes or that it
     changes nothing, and what each option adds
   - `WHAT IT NEEDS`: the Python version, every tool it expects on
     PATH, and the shared module it imports
   - `EXAMPLES`: one line per example, each followed by a comment
     saying what that example shows
   The examples carry no path of any platform and no invocation
   of any particular shell.

3. Write the body to run unchanged on Linux and macOS. The rules
   are:
   - paths are composed with `pathlib`, never as strings
   - a process is started with `subprocess` and an argument list,
     never through a shell
   - an external tool (`git`, `markitdown`, `pandoc`, `claude`) is
     resolved from PATH; when it is missing, the script stops with
     an error that names it, and installs nothing
   - colour is printed only when the output is a terminal; the
     shared `say` of `forge_repos.py` prints plain text when it is
     not, or when `NO_COLOR` is set
   - nothing Windows-only
   - no URL and no identity anywhere in the file

4. Put what the script shares with its family into the shared
   module and import it from there. A script imports the module by
   path: it adds its own directory to the import path and then
   imports the module by name. What each module holds today:
   - `forge_repos.py`: the engine root (the parent of `scripts/`),
     the check that git is installed and that the engine is a
     repository, the list of repositories a bare or a slug form
     visits (a project is a repository when `projects/<slug>/.git`
     exists), running git with and without captured output, the
     state of a branch against its origin after a fetch, and the
     coloured output
   - `forge_tools.py`: a tool on PATH, resolving paths, and the
     headless Claude Code run
   - `docs_map.py`: the reader of the documentation map
   Something two scripts need is written once, in the module, never
   in both scripts. A module is not a command: it has no synopsis
   and is not run on its own.

5. Name the script in the layout comment of `CLAUDE.md`, on the
   `scripts/` line of Repository layout, with a phrase of what it
   does. Where the script is a git script, add its clause to the
   sentence of Persistence (git) that names the git scripts. Where
   the script is a hook, name it in `.claude/settings.json`.

## Prove it

Run the examples of the docstring as they stand, from the engine
root. For the smallest script of the set that is:

```
python scripts/forge-status.py
```

You should now see the output the docstring describes, and nothing
changed on disk.

Then run the engine check:

```
/check engine
```

It verifies the scripts on disk against `CLAUDE.md`: every file in
`scripts/` is described in the layout comment and its governing
rule, and nothing described there is missing on disk. A script that
is on disk and not in the comment is a finding; so is a name in the
comment with no file behind it.

## Record and release

The change is recorded and released as any change of the forge:
[Make a change to the forge](how-a-change-is-made.md) says how. The
script's own facts stay in its docstring; the record says that the
script was added and why.

## A worked example

The docstring of a generic script, `forge-example.py`, that reports
something about every project and changes nothing. It shows the
shape; the script itself is made up.

```
forge-example.py - report, for the engine and every project, the
thing this script exists to report.

SYNOPSIS
    python scripts/forge-example.py [slug] [--verbose]

WHAT IT DOES
    Read-only, changes nothing. Bare, it visits the engine and every
    project under projects/ that is a repository and prints one line
    for each; the others are reported and skipped. With a slug it
    visits that one project, which must exist and be a repository.

    With --verbose it prints the detail behind each line. Without
    the flag the script touches no network.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-example.py              # every repository, one line each
    python scripts/forge-example.py my-project   # one project
    python scripts/forge-example.py --verbose    # every repository, with the detail
```

The slug in the examples is a placeholder. No path of a platform
appears, no shell is assumed, and the tool the script needs is
named, not installed.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the scripts are the only door.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
