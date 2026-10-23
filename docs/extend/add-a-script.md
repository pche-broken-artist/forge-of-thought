---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 4156b5ef52e8ad7b
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

A script of the forge is a Python file in `scripts/` that does one
mechanical job, such as saving to git, building the ledger (the
state report made from the documents) or converting a document.
This page is for the extender who adds one. It shows how the new
script is written so that it runs unchanged on any platform, carries
its own help and is the one place where its facts are stated.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first: it
says how a change is proven, recorded and released. A new script is
recorded and released as any change of the forge.

See [Scripts](../reference/scripts.md) for the scripts that already
exist. A job one of them does already is not a new script.

The rules below exist because the forge runs beyond Windows.
`scripts/` is the only platform-bound layer of the forge, so it is
the one layer that has to be written to run unchanged on Linux and
macOS. Instance facts stay out of the scripts. That is, no remote
URL, no author identity and no first-run set-up: git configuration
belongs to the user. Why the scripts are the one way Claude writes
to git is explained in [Persistence in git](../about/persistence-in-git.md).
Terms of the forge are explained in one line each in the
[Glossary](../reference/glossary.md).

## The files

- `scripts/<name>.py`: the new script, one file.
- A shared module beside it, where the script needs what other
  scripts already share. The modules are:
  - `forge_repos.py`: the engine root, the git check, the list of
    repositories a bare or a slug form visits, running git and
    coloured output; used by the git scripts.
  - `forge_tools.py`: a tool on PATH, resolving paths and the
    headless Claude Code run; used by the conversions.
  - `docs_map.py`: the reader of the documentation map; used by the
    documentation scripts.
  - `forge_docs.py`: also a shared module; what it holds is not
    stated in the inputs of this page.
- `CLAUDE.md`, section Repository layout: the comment beside
  `scripts/`, which names every script and every shared module.

## Steps

1. **Write the script in Python 3.8 or newer.** It is run as
   `python scripts/<name>.py`. `python` on PATH is the one
   prerequisite of the scripts. A system that has only `python3`
   gives it that name.

2. **Put the help in the module docstring.** The docstring opens the
   file and is the script's whole help. It holds these parts:
   - the name and one line of what the script is for;
   - SYNOPSIS: the command line with its options;
   - WHAT IT DOES: the behaviour, every option included;
   - WHAT IT NEEDS: the Python version, the external tools on PATH
     and the shared modules beside it;
   - EXAMPLES: command lines as they are typed, each with a short
     comment.

   The docstring is where the script is described in full. Other
   files cite the script by its path and do not repeat what its
   docstring says. A generic example of the shape:

   ```
   """
   forge-example.py - report something about the engine and every
   project, without changing anything.

   SYNOPSIS
       python scripts/forge-example.py [--remote]

   WHAT IT DOES
       Read-only. For the engine and each projects/<slug>, prints one
       line of state. With --remote it also asks each origin; without
       the flag the script touches no network.

   WHAT IT NEEDS
       Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

   EXAMPLES
       python scripts/forge-example.py             # local state only
       python scripts/forge-example.py --remote    # against each origin as well
   """
   ```

3. **Use nothing Windows-only.**
   - Compose paths with `pathlib`.
   - Start processes through `subprocess` with argument lists, never
     through a shell.
   - Resolve external tools (`git`, `markitdown`, `pandoc`,
     `claude`) from PATH. Where a tool is missing, the script stops
     with an error that names it.
   - Print colour only when the output is a terminal.
   - Keep the examples in the help free of Windows-specific paths
     and invocations.

4. **Leave instance facts out.** The script carries no URL and no
   identity. The commit identity is git's, resolved from the user's
   own configuration.

5. **Share code through a module, never twice.** What several
   scripts need lives in one module beside them, imported by its
   path. Add to an existing module where its subject fits. A new
   module carries a docstring that says what it holds and that it is
   not a command.

6. **Name the script in `CLAUDE.md`.** Add it to the comment beside
   `scripts/` in the section Repository layout, with a few words of
   what it is for. A new shared module joins the list of modules
   there too.

## Prove it

Run the engine check:

```
/check engine
```

Among other things, it verifies that every file in `scripts/` is
described in `CLAUDE.md` (the layout comment and the rule that
governs it) and that nothing described there is missing on disk. A
run that finds nothing files nothing.

Then run the script itself with each example of its help, as it
stands, for instance:

```
python scripts/<name>.py
```

## Record and release

The script is recorded and released as any change of the forge, as
[Make a change to the forge](how-a-change-is-made.md) describes.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
