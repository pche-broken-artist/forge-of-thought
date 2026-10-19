---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 13205a4c904a82cc
inputs:
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#Repository layout
  - scripts/forge-status.py
  - scripts/forge_repos.py
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/40-solution-design.md#SOL.0620
---

# Add a script

A script of the forge is a small Python program in `scripts/` that
does one mechanical job, such as reporting the git state or
converting a document. This page is for the extender who writes a
new one. It says how the script is written so that it runs
unchanged on every platform. It says how the script documents
itself in its own help, and how what several scripts share is kept
in one place.

## Before you start

A new script is a change to the forge like any other. How a change
is proved, recorded and released is on
[Make a change to the forge](../extend/how-a-change-is-made.md).
The addition is recorded and released as any change of the forge.

The scripts that exist already are listed on
[Scripts](../reference/scripts.md). Look there first: the job may
belong to a script that is already there. Why the scripts are the
only way into git is explained on
[Persistence in git](../about/persistence-in-git.md). Terms of the
forge are in one line each on the [Glossary](../reference/glossary.md).

## The files

- `scripts/<name>.py`: the new script.
- A shared module beside it in `scripts/`, where the script needs
  something another script already does. The shared modules are
  these:
  - `forge_repos.py`: what the git scripts share (the engine root,
    the check that git is there, the list of repositories a command
    visits, running git, the state of a repository against its
    origin, coloured output).
  - `forge_tools.py`: what the conversions share (a tool on PATH,
    resolving paths, the headless run of Claude Code).
  - `forge_docs.py`: a module the scripts share; what it holds is
    not said here.
  - `docs_map.py`: the reader of the documentation map, shared by
    the documentation scripts.
- `CLAUDE.md`, section "Repository layout": the comment beside
  `scripts/`, which names every script.

## Steps

1. **Decide what is shared.** Whatever several scripts need lives
   in one module beside them and never twice. Where your script
   needs the engine root, running git or a tool on PATH, import it
   from the module that already has it. Where your script brings
   something a second script will need too, put it in a module, not
   in the script. A module says in its own docstring what it holds
   and that it is not a command.

2. **Write the help first, in the module docstring.** The docstring
   at the top of the file is the script's help. It carries these
   parts:
   - the first line: the file name and what the script does, in one
     line;
   - SYNOPSIS: the line as it is typed, `python scripts/<name>.py`
     with its options;
   - WHAT IT DOES: what the script reads, what it changes or that
     it changes nothing, and what each option adds;
   - WHAT IT NEEDS: Python 3.8 or newer, every external tool it
     calls, and every shared module it imports;
   - EXAMPLES: lines as they are typed, each with a short comment.

   The docstring is where these facts stand. A command that needs
   them points to the script by its path instead of repeating them.

3. **Write the script to the portability rules.** The forge runs
   beyond Windows, and `scripts/` is the only layer bound to a
   platform. So every script is written to run unchanged on Linux
   and macOS:
   - Python 3.8 or newer, run as `python scripts/<name>.py`.
     `python` on PATH is the one prerequisite of the scripts. A
     system that has only `python3` gives it that name.
   - Nothing Windows-only.
   - Paths composed with `pathlib`.
   - Processes run through `subprocess` with a list of arguments,
     never through a shell.
   - External tools (`git`, `markitdown`, `pandoc`, `claude`)
     resolved from PATH. The script checks that a tool it needs is
     there and stops with a plain message when it is not.
   - Colour only when the output goes to a terminal.
   - Examples in the help free of Windows-specific paths and
     invocations.
   - No URL and no identity. Facts of one instance (one
     installation of the forge) stay out of the script: the remote
     and the commit identity belong to git and to the user's own
     git configuration.

4. **Import a shared module by path.** The script adds its own
   directory to Python's import path and then imports the module by
   name. `forge-status.py` does this for `forge_repos.py` and
   `forge_tools.py`. It is the smallest model of a script that
   follows these rules.

5. **Name the script in `CLAUDE.md`.** Add it to the comment beside
   `scripts/` in "Repository layout", with a few words on what it
   does. If it is a new shared module, add it there too, and to the
   list of shared modules under "Persistence (git)", Portability.

## Prove it

Run the engine check:

```
/check engine
```

Among other things, it verifies that every file in `scripts/` is
described in `CLAUDE.md`, in the layout comment and its governing
rule. It also verifies that nothing described there is missing on
disk. A run that finds nothing files nothing.

Then run the script as its examples have it, for instance:

```
python scripts/<name>.py
```

## Record and release

The new script is recorded and released as any change of the forge,
as [Make a change to the forge](../extend/how-a-change-is-made.md)
describes.

## A worked example

The docstring of a made-up script that counts the words of the
Markdown files in a directory. The shape is the one step 2 gives.

```
"""
word-count.py - count the words of the Markdown files in a
directory.

SYNOPSIS
    python scripts/word-count.py <directory> [--total]

WHAT IT DOES
    Read-only, changes nothing. Prints one line per Markdown file
    under <directory>: its path and its number of words. With
    --total it prints only the sum.

WHAT IT NEEDS
    Python 3.8 or newer. `forge_tools.py` beside it.

EXAMPLES
    python scripts/word-count.py projects/<slug>            # one line per file
    python scripts/word-count.py projects/<slug> --total    # the sum only
"""
```

## See also

- [Make a change to the forge](../extend/how-a-change-is-made.md):
  proving, recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
