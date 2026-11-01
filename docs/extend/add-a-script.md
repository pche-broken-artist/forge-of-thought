---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 717b0fb76fb15902
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

A script of the forge is a Python file in `scripts/` that does one
mechanical job for a command, such as reading git state, building the
ledger or converting a render. This page is for the extender who
writes a new one. It shows how to write the script so that it runs
unchanged beyond Windows, carries its own help in its docstring and
is the one place its facts are stated.

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md): a new
  script is recorded and released as any change of the forge.
- Look at [Scripts](../reference/scripts.md) first. The job may
  already have a script, or a shared module may already hold what
  you need.
- A run on a model of another family is not a new script. It is a
  row of the engine script, as
  [Add an engine](add-an-engine.md) shows.
- The scripts are the only door to a write of git; why is said in
  [Persistence in git](../about/persistence-in-git.md).

Terms of the forge used below are defined in one line each in the
[Glossary](../reference/glossary.md). "The engine" here is the
forge's own repository: its rules, commands, templates and scripts.

## The files

- `scripts/<name>.py`: the new script.
- `scripts/<module>.py`: a shared module, only where what the script
  needs is also needed by another script.
- `CLAUDE.md`: the layout comment of `scripts/` in Repository layout
  names every script and every shared module; a new shared module is
  also named in the list of modules under Persistence, Portability.
- `tmp/`: the engine's working folder, where the script writes any
  working file it needs.

## Steps

1. **Write the script in portable Python.** The rules every script
   keeps:
   - Python 3.8 or newer, run as `python scripts/<name>.py`. `python`
     on PATH is the one prerequisite of the scripts. A system that
     has only `python3` gives it that name.
   - Nothing Windows-only.
   - Paths composed with `pathlib`.
   - Processes started through `subprocess` with argument lists,
     never through a shell.
   - External tools (`git`, `markitdown`, `pandoc`, `claude`)
     resolved from PATH. The script does not install a missing
     tool: it names what is missing and stops, as the git check of
     `forge_repos.py` does with "git is not installed."
   - Colour only on a terminal. The shared output of
     `forge_repos.py` colours only when the output is a terminal and
     `NO_COLOR` is not set.
   - No remote URL and no author identity in the script. These are
     instance facts: git configuration belongs to the user.

   The scripts are written to run unchanged on Linux and macOS. The
   git scripts, the ledger and docs-state have run on Linux. For the
   conversions and the two hooks the rule is still a writing rule,
   until a run says otherwise. A new script is written to the rule.

   You should now see a script that uses no path separator of its
   own, no shell string and no fixed location of a tool.

2. **Put its help in its module docstring.** The docstring is the one
   owner of the script's facts:
   - its synopsis, the line as it is typed;
   - what it does;
   - what it needs (the Python version, the tools on PATH, the
     modules beside it);
   - its options, where it has any;
   - where its output lands, where it writes any;
   - examples.

   A command that needs one of these facts cites the script's header
   and never restates it. The examples in the help are free of
   platform-specific paths and invocations. `scripts/forge-status.py`
   is the smallest model of such a docstring.

   You should now see every fact a reader of the script needs at the
   head of the file, and no copy of it elsewhere.

3. **Share through a module, never twice.** What several scripts
   share lives in one module beside them, imported by path from the
   script's own directory. Five modules exist:
   - `forge_repos.py`: the engine root, the git check, the list of
     repositories to visit and running git, for the git scripts.
   - `forge_tools.py`: a tool on PATH, resolving paths and the
     headless Claude Code run, for the three conversions.
   - `forge_docs.py`: the front-matter, the records, the ledger
     tables, the index entries and the threads as the scripts read
     them, for forge-ledger, forge-migrate and forge-history.
   - `docs_map.py`: the reader of the documentation map, for the
     three documentation scripts.
   - `forge_check.py`: a finding and its report, and the keys and
     comments a template owns, for forge-check.

   Use a module that already holds what you need. Where a second
   script would need the same code, move it into a module. A shared
   module carries a docstring of its own that says what it holds and
   that it is not a command; `scripts/forge_repos.py` is the model.

   You should now see each piece of shared behaviour in exactly one
   file.

4. **Send working files to `tmp/`.** A script's working files go to
   `tmp/` at the engine root, in a subfolder the script makes when it
   needs one. They never go to the system's temporary directory. The
   folder is in git with its own README and `.gitignore`, so that it
   exists on every clone; its contents never are. Nothing in it is a
   source of truth: no check, no ledger and no history reads from
   it. A run is kept for inspection and deleted by hand, never by a
   script.

   You should now see the script's working files under `tmp/` and
   nowhere else.

5. **Name it in `CLAUDE.md`.** Add the script to the layout comment
   of `scripts/` in Repository layout, in a few words of what it is.
   A new shared module is added there and to the list of modules
   under Persistence, Portability.

   You should now see the new file named in the layout comment.

## Prove it

```
/check engine
```

The engine check verifies that every file in `scripts/` is described
in `CLAUDE.md` (the layout comment and its governing rule) and that
nothing described there is missing on disk. A script on disk that the
layout comment does not name is a finding.

## Record and release

The new script is recorded and released as any change of the forge,
as [Make a change to the forge](how-a-change-is-made.md) says.

## A worked example

A generic docstring for a script `scripts/example-tool.py`, taken
from no real script, in the shape step 2 gives:

```
"""
example-tool.py - one line that says what the script is for.

SYNOPSIS
    python scripts/example-tool.py <slug> [--dry]

WHAT IT DOES
    What the script reads, what it writes and what it leaves alone.
    Whether it touches the network, and when.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

OPTIONS
    --dry    say what would be written, write nothing

OUTPUT
    tmp/example-tool/<slug>.md

EXAMPLES
    python scripts/example-tool.py demo-project
    python scripts/example-tool.py demo-project --dry
"""
```

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
