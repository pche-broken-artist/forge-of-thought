---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: fa4966a7fda86cfb
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
docstring and uses nothing bound to one operating system. This page
is for the extender who writes a new script: what the file must look
like, what it may share with the scripts beside it, where it is
named and how the addition is proved. The forge is the engine that
runs the chain of a project; a script is one of its doors to the
machine, git among the things behind them.

## Before you start

A script is a change to the forge like any other. How a change is
proposed, proved, recorded and released is on
[Make a change to the forge](how-a-change-is-made.md); this page
adds only what is particular to a script. The addition is recorded
and released as any change of the forge.

Before you write, look at what exists. The scripts the forge has
today are listed on [Scripts](../reference/scripts.md). Why the
scripts in `scripts/` are the only door to git, reading state
included, is explained on
[Persistence in git](../about/persistence-in-git.md). The terms of
the forge are gathered in one line each in the
[Glossary](../reference/glossary.md).

Two facts frame every script:

- `scripts/` is the only platform-bound layer of the forge. It is
  written to run unchanged on Linux and macOS. This is a writing
  rule, not a verified claim: portability is verified by running the
  set on Linux, and until then the rules below are what holds.
- Instance facts stay out of the scripts. A script carries no remote
  URL, no author identity and no first-run initialisation. The git
  configuration belongs to the user of the installation.

## The files

- `scripts/<name>.py`: the script itself. Its module docstring is its
  help and the one owner of the facts about it.
- `scripts/forge_repos.py`, `scripts/forge_tools.py`,
  `scripts/docs_map.py`: the shared modules. What several scripts
  share lives in one of them, never twice.
- `CLAUDE.md`, the comment on `scripts/` in the section
  "Repository layout": every script is named there in a few words.
- `CLAUDE.md`, the section "Persistence (git)": a script that serves
  git is also named there, with one clause on what it does.
- The skill or the agent that uses the script: it cites the script
  by path and reads its docstring for the facts. It does not restate
  them.

## Steps

### 1. Decide what the script owns

A script owns one job and the facts about that job. Anything the job
shares with another script (the engine root, the check that `git` is
installed, the list of repositories a bare or a slug form visits,
running git, a tool on PATH, the reader of the documentation map)
is already in a shared module. Read the three modules before you
write: what they have, you import; what two scripts would need and
no module has, you add to the module that fits, not to both scripts.

The three modules and whom they serve:

- `forge_repos.py`: the engine root, the git check, the list of
  repositories to visit, running git, the state of a repository
  against its origin and coloured output. Shared by the git scripts.
- `forge_tools.py`: a tool on PATH, resolving paths, the headless
  Claude Code run. Shared by the conversions.
- `docs_map.py`: the reader of the documentation map. Shared by the
  documentation scripts.

You should now know what the script does itself and what it imports.

### 2. Write the docstring first

The module docstring is the help of the script. It is what a person
reads with the file open and what a command cites instead of
describing the script a second time. It holds, in this order:

- one line that names the script and says what it does;
- SYNOPSIS: the command as it is typed, with its options and
  arguments;
- WHAT IT DOES: what the script changes and what it leaves alone,
  what each option does, and where the output lands when the script
  writes a file;
- WHAT IT NEEDS: the Python version, the tools that must be on PATH,
  the shared module it imports;
- EXAMPLES: runs that can be typed as they stand, each with a short
  comment on what that run does.

The examples name no path of one operating system and no path of
one installation. A run is written as `python scripts/<name>.py`,
nothing else. Where the script acts on a project, the examples use a
placeholder slug.

The smallest model on disk is the docstring of
`scripts/forge-status.py`: four headings, the one option explained
under WHAT IT DOES, two examples. A shared module has a docstring
too; `scripts/forge_repos.py` opens with what it shares, whom it
serves and the sentence "Not a command", so that nobody runs it.

You should now have a docstring from which the script can be
written and which a command can cite.

### 3. Write the body by the rules

The body follows the docstring. The rules it keeps:

- Python 3.8 or newer. Use nothing newer than that.
- Nothing Windows-only.
- Paths are composed with `pathlib`, never with a string and a
  separator.
- Processes run through `subprocess` with an argument list, never
  through a shell.
- External tools (`git`, `markitdown`, `pandoc`, `claude`) are
  resolved from PATH. A script that needs one checks that it is
  there and fails aloud when it is not; it never installs it.
  `forge_repos.py` does this for `git` with one call.
- Colour is printed only on a terminal. The shared `say` of
  `forge_repos.py` prints plain text when the output is not a
  terminal or when `NO_COLOR` is set in the environment.
- No URL and no identity. The script does not know where a remote
  is or who commits.
- The help in the body is the docstring: an argument parser takes
  its description from the docstring's first line rather than from
  a second sentence of its own. `forge-status.py` does this.

A shared module is imported by path: the script puts its own
directory first on the import path and imports the module by name.
`forge-status.py` shows the two lines; copy that way of importing,
not another. The model script also calls `utf8_console()` of
`forge_tools.py` before it prints anything.

You should now have a script that runs with `python
scripts/<name>.py` and prints its help with `--help`.

### 4. Name it in `CLAUDE.md`

Add the script to the comment on `scripts/` in the section
"Repository layout", in the few words the other scripts get there.
A script that serves git is also named in the section "Persistence
(git)", in the sentence that lists the git scripts, with one clause
on what it does. Nothing more goes into `CLAUDE.md`: the facts about
the script stay in its docstring.

Where a command or an agent uses the script, that definition cites
the script by path and says that what it needs and where its output
lands are the docstring's. The facts are stated once, in the
docstring.

You should now see the script in the layout comment and, where it
serves git, in the Persistence section.

### 5. Share, do not copy

If while writing you found that a second script needs the same
function, move it to the module that fits and import it from both.
A function that stands in two scripts is a defect the check does not
catch for you; keep it out yourself.

You should now have nothing in the script that another script also
has.

## Prove it

Run the script as its synopsis says and read its help:

```
python scripts/<name>.py --help
```

Then run the engine check:

```
/check engine
```

The check reads `scripts/` against `CLAUDE.md`: every file in
`scripts/` must be described in the layout comment and its governing
rule, and nothing described there may be missing on disk. A script
you wrote and did not name, or a name you changed in one place only,
is a finding of that check. The check verifies conformance with the
conventions only; whether the script works is yours to prove by
running it.

Whether the set runs on Linux and macOS is not something the check
says. The rules of step 3 are what the forge holds the script to.

## Record and release

The addition is a change of the forge and is recorded and released
as one: how that is done, step by step, is on
[Make a change to the forge](how-a-change-is-made.md). The write
happens on the word of the principal, the person whose thinking the
forge serves and who alone decides what is written.

## A worked example

The docstring of a new script, with placeholders where the script's
own facts go. Its shape is the shape of `scripts/forge-status.py`.

```
"""
<name>.py - <one line: what the script does>.

SYNOPSIS
    python scripts/<name>.py [--option] <slug>

WHAT IT DOES
    <What the script reads, what it changes and what it leaves
    alone. Which project <slug> names. What --option adds and
    what the run does without it. Where the output lands, when
    the script writes a file.>

WHAT IT NEEDS
    Python 3.8 or newer; <tool> on PATH. `<module>.py` beside it.

EXAMPLES
    python scripts/<name>.py my-project             # <what this run does>
    python scripts/<name>.py --option my-project    # <what this run does>
"""
```

`my-project` is a placeholder slug. Nothing in the docstring names a
host, a drive, a user or a remote.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
