---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 23c46be16979a5c0
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

A script of the forge is a Python program in `scripts/`, run as
`python scripts/<name>.py`, that does one mechanical job for the
engine or for a project: it commits and pushes, builds the ledger
(the state of a project, made at read time), converts a document,
checks a convention. This page is for you as an extender who adds
one. It says how a new script is written so that it runs unchanged on
every platform the forge names, carries its help in its own
docstring, and is the one owner of the facts it states. The terms of
the forge used here are gathered in the [Glossary](../reference/glossary.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first: it
says how a change is proved, recorded and released. A new script is
recorded and released as any change of the forge.

Make sure a script is what you need. An engine of another model
family is not a script of its own: it is a row of the engine script,
as [Add an engine](add-an-engine.md) says.

Know why the scripts matter. The scripts in `scripts/` are the door
to a write of git; reading git directly is open. The line between
the two is held for Claude by the hook `scripts/hook-git.py` of
`.claude/settings.json`, which denies every write and names the
script to use. How many scripts there are is not a rule. Why the
scripts are the only door is said on [Persistence in git](../about/persistence-in-git.md).

Know what the portability rule promises and what it does not.
`scripts/` is the only platform-bound layer of the forge, and its
scripts are written to run unchanged on Linux and macOS. The git
scripts, the ledger and docs-state have run on Linux. The
conversions and the two hooks are a writing rule until a run says
otherwise. Nothing has run on macOS: for it the whole set is the
writing rule alone. A new script is therefore written to the rule,
not to a run.

## The files

- `scripts/<name>.py`: the script, with its help in its module
  docstring.
- `scripts/forge_repos.py`, `scripts/forge_tools.py`,
  `scripts/forge_docs.py`, `scripts/docs_map.py`,
  `scripts/forge_check.py`: the five modules the scripts share,
  one for what several scripts need alike.
- `CLAUDE.md`, Repository layout: the layout comment on `scripts/`,
  which names every script in one clause, and the comment on `tmp/`,
  which names what lies in the working folder.
- `tmp/`: the engine's working folder, in git with its own
  `README.md` and `.gitignore`, its contents never; where a script's
  working files go.

## Steps

1. **Name and place it.** The script is `scripts/<name>.py` and is
   run as `python scripts/<name>.py`. It is Python 3.8 or newer.
   `python` on PATH is the one prerequisite of the scripts; a system
   that has only `python3` gives it that name. A script installs
   nothing.

2. **Write the docstring before the code.** Each script carries its
   help in its module docstring: a synopsis, what it does, what it
   needs, its options, where its output lands, and examples. The
   docstring is the one place those facts are stated: a skill, a
   command or a page that needs them cites the script by its path and
   never restates them. The examples are free of Windows-specific
   paths and invocations. The smallest model of such a docstring is
   `scripts/forge-status.py`: its header says that it is read-only,
   what it reports and in which order, what the `--remote` flag adds
   and that without it the script touches no network, what it needs,
   and two example invocations. A module that is not a command says
   so in its docstring, as `scripts/forge_repos.py` does.

3. **Write it portable.** Nothing in a script is Windows-only. Paths
   are composed with `pathlib`. Processes run through `subprocess`
   with argument lists and never a shell. External tools (`git`,
   `markitdown`, `pandoc`, `claude`) are resolved from PATH and never
   installed by the script. Colour is written only on a terminal.
   Options are spelled as the language spells them (`--tag`,
   `--engine`, `-o`) and parsed by its own convention. A script
   carries no URL and no identity and makes no first-run
   initialisation. Git configuration is the user's, and the forge
   sets none of it.

4. **Share through a module, never twice.** What several scripts
   share lives in one module beside them, imported by path. There
   are five today:
   - `forge_repos.py`: the engine root, the git check, the list of
     repositories a bare or a slug form visits, running git, the
     state of a repository against its origin, the files of the
     global git configuration, the registration of the merge driver
     and coloured output; for the git scripts, and shared by the
     scripts of collaboration too.
   - `forge_tools.py`: a tool on PATH, resolving paths, the headless
     Claude Code run; for the three conversions.
   - `docs_map.py`: the reader of the documentation map; for the
     three documentation scripts.
   - `forge_docs.py`: the front-matter, the records, the ledger
     tables, the index entries and the threads as the scripts read
     them; for forge-ledger, forge-migrate and forge-history.
   - `forge_check.py`: a finding and its report, the keys and
     comments a template owns; for forge-check.

   A new script that needs one of these imports the module and does
   not copy it. A thing your script and another would both need goes
   into a module, never into both. `scripts/forge_repos.py` is the
   model of a shared module: its docstring names each thing it
   offers and the rule it holds, such as recognising a project's
   repository by asking git and never by a `.git` looked for.

5. **Send working files to `tmp/`.** `tmp/` at the engine root is the
   one working folder of the forge. A script that needs a working
   file makes its subfolder there, as the research runs, the
   documentation's tasks, a dry ledger, a check's report before it is
   filed and a migration's manifest do. Nothing in it is a source of
   truth: no check, no ledger and no history reads from it. A run is
   kept for inspection and deleted by hand, never by a script. The
   system's temporary directory is not used. The reason is recorded:
   one folder in the engine keeps a run traceable on the machine and
   gives a profile's deny rules one path to name; the price is a
   folder to empty by hand.

6. **Name it in the layout comment of `CLAUDE.md`.** The comment on
   `scripts/` in Repository layout names every script in one clause
   saying what it does, and ends with the modules the scripts share.
   Add your script there in one clause. A new shared module is named
   among the modules. A script that serves the engine and every
   project repository through git is also named in the passage
   Persistence (git) of `CLAUDE.md`, which lists those scripts, each
   described in full by its own help header.

## Prove it

Run the script on your own machine with each example of its
docstring, as the examples stand:

```
python scripts/<name>.py
```

Then run the engine check:

```
/check engine
```

Among what it verifies: every file in `scripts/` is described in
`CLAUDE.md`, in the layout comment and its governing rule, and
nothing described there is missing on disk. The same check runs at
every release.

The forge does not ask for a run on Linux or macOS before the change
is released. The script is written to the rule, and what has run
where is said above and nowhere claimed beyond it.

## Record and release

The change is recorded and released as any change of the forge, the
way [Make a change to the forge](how-a-change-is-made.md) says. The
script's docstring is its documentation, and the layout comment of
`CLAUDE.md` is its registration. The scripts that exist are listed on
[Scripts](../reference/scripts.md).

## A worked example

A generic docstring, the shape the rule asks for. `forge-example.py`
is a model and no script of the forge; `my-project` is a placeholder
slug.

```
"""
forge-example.py - count the documents of a project, by kind.

SYNOPSIS
    python scripts/forge-example.py <slug> [--kind <kind>] [-o <file>]

WHAT IT DOES
    Read-only, changes nothing. Walks projects/<slug> and prints one
    line per kind of document with the number found. With --kind it
    reports one kind only.

WHAT IT NEEDS
    Python 3.8 or newer. `forge_docs.py` beside it.

OPTIONS
    --kind <kind>   one kind of document instead of all
    -o <file>       write the report to a file under tmp/ instead of
                    printing it

WHERE THE OUTPUT LANDS
    The terminal. With -o, tmp/<file>; the folder is in git, its
    contents never.

EXAMPLES
    python scripts/forge-example.py my-project
    python scripts/forge-example.py my-project --kind recipe
    python scripts/forge-example.py my-project -o tally.md
"""
```

The layout comment of `CLAUDE.md` would then carry one clause for
it, in the shape of its neighbours: `forge-example (the documents of
a project counted by kind)`.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the scripts are the only door.
- [Add an engine](add-an-engine.md): a row of the engine script, which needs no script of its own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
