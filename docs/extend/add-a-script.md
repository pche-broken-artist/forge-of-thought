---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 733a44c86cab79f0
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

A script of the forge is a Python program in `scripts/` that does one
mechanical job, such as a write to git, a conversion or the making of
the ledger (the state of a project, built from its documents). This
page is for the extender who adds a new one. It says how the script is
written so that it runs beyond Windows, carries its own help and is
the one place its facts are stated. The scripts that exist are listed
in [Scripts](../reference/scripts.md).

## Before you start

A new script is a change to the engine. How a change is made, proved,
recorded and released is in
[Make a change to the forge](../extend/how-a-change-is-made.md). The
script is recorded and released as any change of the forge is.

Check first that the job needs a script of its own. A run on another
model family, for instance, is a row of the engine script and needs
no new script: see [Add an engine](../extend/add-an-engine.md). Why
the scripts are the only way a write reaches git is explained in
[Persistence in git](../about/persistence-in-git.md). Terms of the
forge are in the [Glossary](../reference/glossary.md).

## The files

- `scripts/<name>.py`: the new script.
- One of the shared modules beside it, where the script needs what
  other scripts already use (below).
- `CLAUDE.md`: the layout comment of `scripts/` under Repository
  layout, where every script is named. A new shared module is also
  named in the Portability paragraph of Persistence (git).

The shared modules are the one home of what several scripts use. A
script imports them by path, from the directory it lies in. There are
five today:

- `forge_repos.py`: the engine root, the git check, the list of
  repositories to visit, running git and coloured output; for the git
  scripts.
- `forge_tools.py`: a tool on PATH, resolving paths and the headless
  Claude Code run; for the three conversions.
- `docs_map.py`: the reader of the documentation map; for the three
  documentation scripts.
- `forge_docs.py`: the front-matter, the records, the ledger tables,
  the index entries and the threads as the scripts read them; for
  forge-ledger, forge-migrate and forge-history.
- `forge_check.py`: a finding and its report, and the keys and
  comments a template owns; for forge-check.

What a module holds is said in its own docstring. A shared module is
not a command.

## Steps

1. **Write it in Python 3.8 or newer.** The script is run as
   `python scripts/<name>.py`. `python` on PATH is the one
   prerequisite of the scripts. A system that has only `python3` gives
   it that name.

2. **Keep it portable.** `scripts/` is the only layer of the forge
   bound to a platform. Its scripts are written to run unchanged on
   Linux and macOS. Portability is verified only in part, so the
   writing rule, not a past run, is what a new script is held to:
   - nothing Windows-only;
   - paths composed with `pathlib`;
   - processes started through `subprocess` with argument lists, never
     through a shell;
   - external tools (`git`, `markitdown`, `pandoc`, `claude`) resolved
     from PATH;
   - colour only when the output is a terminal;
   - usage examples in the help free of Windows-specific paths and
     invocations.

3. **Carry no instance fact.** The script holds no remote URL and no
   author identity. Git configuration belongs to the user, not to a
   script.

4. **Put what is shared in a module.** Code that another script
   already needs, or will need, goes into the shared module that
   serves it. It is never written twice. A new module is made only
   where none of the five fits.

5. **Send working files to `tmp/`.** `tmp/` at the engine root is the
   one working folder of the forge. A script that needs a working file
   makes its subfolder there and never uses the system's temporary
   directory. One folder in the engine keeps a run traceable on the
   machine. It also gives the deny rules of an engine profile one path
   to name. The folder is in git with its own README and `.gitignore`,
   so that it exists on every clone; its contents never are. Nothing in
   it is a source of truth. A run is kept for inspection and deleted by
   hand, never by a script.

6. **Write the help in the module docstring.** The docstring is the
   one owner of the script's facts. Commands and other documents cite
   it and do not repeat it. It carries, in this order:
   - the name and one line of what the script is;
   - SYNOPSIS: the command line as it is typed;
   - WHAT IT DOES: the job, each option, and what it changes or
     leaves alone;
   - where the output lands, for a script that writes a file;
   - WHAT IT NEEDS: Python, the tools on PATH, the modules beside it;
   - EXAMPLES: lines that can be typed as they stand.

   A generic docstring of this shape, for a placeholder script:

   ```
   """
   forge-example.py - report one thing about a project; changes nothing.

   SYNOPSIS
       python scripts/forge-example.py <slug> [--all]

   WHAT IT DOES
       Read-only. Reads projects/<slug> and prints what it found, one
       line per item. With --all it visits every project instead of
       one. Touches no network.

   WHAT IT NEEDS
       Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

   EXAMPLES
       python scripts/forge-example.py my-project     # one project
       python scripts/forge-example.py --all         # every project
   """
   ```

7. **Name it in `CLAUDE.md`.** Add the script to the layout comment of
   `scripts/` in Repository layout, with one clause of what it is for.
   Name a new shared module in the Portability paragraph as well.

## Prove it

Run the engine check:

```
/check engine
```

Among other things it verifies that every file in `scripts/` is
described in `CLAUDE.md`, in the layout comment and its governing
rule, and that nothing described there is missing on disk. A run that
finds nothing files nothing.

## Record and release

The new script is recorded and released as any change of the forge,
as [Make a change to the forge](../extend/how-a-change-is-made.md)
says.

## See also

- [Make a change to the forge](../extend/how-a-change-is-made.md):
  proving, recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Add an engine](../extend/add-an-engine.md): a row of the engine
  script, which needs no script of its own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
