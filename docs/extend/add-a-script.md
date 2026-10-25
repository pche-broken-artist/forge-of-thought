---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: e9fa4848caaaf9a6
inputs:
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#Repository layout
  - scripts/forge-status.py
  - scripts/forge_repos.py
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/40-solution-design.md#SOL.0620
  - projects/forge/40-solution-design.md#SOL.0890
---

# Add a script

A script of the forge is a Python file in the engine's `scripts/`
folder that does one mechanical job, such as a write of git, a
conversion or the making of the ledger. The engine is the forge's
own repository: its commands, its rules and its scripts. This page is
for the extender who adds a new script: how it is written so that it
runs unchanged beyond Windows, carries its own help, and is the one
place its facts are stated.

## Before you start

- A new script is a change to the forge. How a change is made, proved,
  recorded and released is on
  [Make a change to the forge](how-a-change-is-made.md).
- The addition is recorded and released as any change of the forge.
- The scripts that exist are listed on [Scripts](../reference/scripts.md).
  Look there first: what you need may already be one.
- The scripts are the door to a write of git; why is on
  [Persistence in git](../about/persistence-in-git.md).
- A model of another family for research needs no script of its own.
  It is a row of the engine script, as
  [Add an engine](add-an-engine.md) shows.
- A term of the forge you do not know is on the
  [Glossary](../reference/glossary.md).

## The files

- `scripts/<name>.py`: the new script.
- A shared module beside it, where your script needs what another
  script already does. The modules that exist:
  - `forge_repos.py`: the engine root, the git check, the list of
    repositories to visit, running git, and coloured output.
  - `forge_tools.py`: a tool on PATH, resolving paths, and the
    headless Claude Code run.
  - `forge_docs.py`: shared by the documentation scripts.
  - `docs_map.py`: the reader of the documentation map (the file the
    documentation pages are made from).
- `CLAUDE.md`: its Repository layout section, where every script is
  named in the comment beside `scripts/`.

## Steps

1. **Write the help first, as the module docstring.** The docstring
   is the string at the top of the file, and it is the script's help.
   It holds, in this order, the sections the script has material for:
   - SYNOPSIS: the line as it is typed, with its options.
   - WHAT IT DOES: what it reads, what it changes or that it changes
     nothing.
   - WHAT IT NEEDS: Python 3.8 or newer, the external tools on PATH,
     the shared modules beside it.
   - OPTIONS, where the script has more than the synopsis shows.
   - Where the output lands, where the script writes a file.
   - EXAMPLES: one line per typical run, with a comment of what it
     does.

   The docstring owns these facts. A command or a page that needs
   them cites the script's header and never copies them, because one
   mechanism lives in one place.

   You should now see `python scripts/<name>.py` described in full by
   its own file, with nothing about it written anywhere else yet.

2. **Write the script to the portability rules.** `scripts/` is the
   only platform-bound layer of the forge. Its scripts are written to
   run unchanged on Linux and macOS:
   - Python 3.8 or newer, run as `python scripts/<name>.py`.
   - Nothing Windows-only.
   - Paths composed with `pathlib`.
   - Processes run through `subprocess` with argument lists, never
     through a shell.
   - External tools (`git`, `markitdown`, `pandoc`, `claude`) resolved
     from PATH.
   - Colour only when the output is a terminal.
   - Usage examples in the help free of platform-specific paths and
     invocations.
   - No URL and no identity. Who commits and where a remote lives
     belong to the user's own git configuration, never to a script.

   `python` on PATH is the one prerequisite of the scripts. A system
   that has only `python3` gives it that name. The reason is that
   Windows has only `python`, while a Unix system gives that name by
   an alias or a package, and one command name can then be written
   everywhere.

   You should now see a script that names no drive, no separator of
   its own and no tool by a fixed location.

3. **Put what is shared in one module.** What several scripts share
   lives in one module beside them, imported by path from the
   `scripts/` folder, never written twice. Use the module that already
   owns the job: for example `forge_repos.py` for running git and for
   coloured output. Where a new piece is needed by more than one
   script, it goes into a module; a module carries its own docstring
   that says what it holds and that it is not a command.

   You should now see your script import the shared module and repeat
   none of its functions.

4. **Send working files to `tmp/`.** A file the script needs only
   while it works (a packet, a report before it is filed, a dry run)
   goes into the engine's working folder `tmp/`, in a subfolder the
   script makes. It never goes into the system's temporary directory.
   - `tmp/` is in git with its own README and `.gitignore`, so that it
     exists on every clone. Its contents never are.
   - Nothing in `tmp/` is a source of truth. No check, no ledger and
     no history reads from it.
   - A script never deletes a run from `tmp/`. A run is kept for
     inspection and deleted by hand.

   One folder in the engine is chosen over the system's temporary
   directory so that a run can be traced on the machine. A second
   reason is that a profile's deny rules then have one path to name.
   The price is a folder to empty by hand.

   You should now see the script's working files under
   `tmp/<subfolder>/` after a run.

5. **Name the script in `CLAUDE.md`.** Add it to the comment beside
   `scripts/` in the Repository layout section, with a few words of
   what it does. A new shared module is also named in the Portability
   paragraph of the Persistence (git) section, beside the four
   modules.

   You should now see the script in the layout comment.

## Prove it

```
/check engine
```

The engine check verifies that every file in `scripts/` is described
in `CLAUDE.md` (its layout comment and the rule that governs it) and
that nothing described there is missing on disk. A script on disk and
absent from the comment is a finding; so is a name in the comment
with no file.

## A worked example

A generic docstring in the shape of the forge's scripts. The names
in angle brackets are placeholders.

```
"""
<name>.py - <what the script does, in one line>.

SYNOPSIS
    python scripts/<name>.py <slug> [--option]

WHAT IT DOES
    <What it reads; what it changes, or that it is read-only and
    changes nothing.> Its working files go to tmp/<name>/, kept
    until deleted by hand.

WHAT IT NEEDS
    Python 3.8 or newer; <tool> on PATH. `forge_repos.py` beside it.

OPTIONS
    --option    <what the option changes>

OUTPUT
    <Where the output lands: a file of the project, or only the
    terminal.>

EXAMPLES
    python scripts/<name>.py <slug>             # <what this run does>
    python scripts/<name>.py <slug> --option    # <what this run does>
"""
```

## Record and release

The new script is recorded and released as any change of the forge:
the steps are on [Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Add an engine](add-an-engine.md): a row of the engine script,
  which needs no script of its own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
