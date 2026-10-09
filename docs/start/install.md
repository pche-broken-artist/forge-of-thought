---
generated: 2026-10-09
made: derived
inputs-hash: c26e3d8742bfc97a
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/forge-save.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/md2pptx.py
  - scripts/md2docx.py
  - projects/forge/recipes/readme.md
  - projects/forge/40-solution-design.md
---

# Install what the forge needs

This page is for a newcomer about to run the forge on a machine for
the first time. It says what must be installed before the forge
runs, how each piece is installed, in the order you will need it,
and how the engine itself gets onto the machine. It was put together
from `CLAUDE.md`, `.claude/settings.json`, the help headers of the
scripts in `scripts/`, the pinned facts of the readme recipe and the
solution design of the forge.

Three things are required: git, Python and Claude Code. Everything
else is optional and needed only by one command each. None of the
forge's scripts installs anything for you: every tool is installed
by you, once, and found on PATH.

## 1. git

Install git so that the command `git` is on PATH.

The engine is a git repository, and the forge's git scripts
(`scripts/forge-save.py` and its siblings) are the forge's only door
to git. They need nothing beyond git itself; they stop with
`git is not installed.` when it is missing.

## 2. Python

Install Python 3.8 or newer so that it is on PATH under the name
`python`.

Python is needed before anything else of the forge works: every
script in `scripts/` is Python, and so is the hook that Claude Code
runs at every prompt (`scripts/hook-walkthrough.py`, started as
`python` by `.claude/settings.json`). The hook needs Python on PATH
as `python` and nothing else.

On Linux or macOS, where only `python3` exists, give it the name
`python` by an alias or by the `python-is-python3` package. The
scripts are written to run unchanged on Linux and macOS: they are
run as `python scripts/<name>.py`, and `python` on PATH is their one
prerequisite.

## 3. Claude Code with a paid subscription

The forge runs inside Claude Code, and Claude Code needs a paid
Claude subscription. Install it with one of these:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- any platform with npm: `npm install -g @anthropic-ai/claude-code`

Sign in on the first run. Usage draws from the same pool as Claude
chat.

## 4. Optional tools, by what they are for

Each of these is needed by one function only. Install what you will
use; skip the rest. Each is resolved from PATH, and no script of the
forge installs it for you.

### markitdown, for converting documents at `/ingest`

When an external document (Word, PowerPoint, PDF, Excel) is brought
into a project with `/ingest`, the conversion to Markdown is done by
`scripts/doc2md.py`, and the script does the conversion exclusively
through markitdown. Install it with pip:

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
```

### pandoc, for the plain Word and PowerPoint files of `/render`

Where a recipe names a format, `/render` makes a plain `.docx` or
`.pptx` beside the Markdown through pandoc (the `pandoc` engine of
`scripts/md2docx.py` and `scripts/md2pptx.py`). Install pandoc once
from https://pandoc.org/installing.html; on Windows
`winget install JohnMacFarlane.Pandoc`, on macOS `brew install
pandoc`, on Linux your package manager.

### The document-skills plugin, for `/publish`

`/publish` makes the designed Word or PowerPoint file through a
model (the `claude` engine of the same two scripts). The model needs
the docx and pptx skills, under either of their names:
`anthropic-skills:docx` and `anthropic-skills:pptx` where Claude
Code already brings them, `document-skills:docx` and
`document-skills:pptx` where the plugin does. Where neither is
there, install the plugin once, from an interactive Claude Code
session:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

If Claude Code already brings the docx and pptx skills, nothing is
to install.

## 5. Clone the engine

The engine's public home is

```
https://github.com/pche-broken-artist/forge-of-thought
```

Clone it with git into a directory of your choice. That directory
is the engine root.

Clone, do not copy: the engine must be a git repository. The save
script refuses an engine that is not one, with the message
`The engine is not a git repository (clone it, do not copy it).`.
The scripts recognise the engine root as the parent of their own
`scripts/` directory, so the clone works wherever you put it.

## 6. Start `claude` from the engine root

Always start `claude` in the engine root, the directory that holds
`CLAUDE.md`. Started there, Claude Code loads `CLAUDE.md`, the
rules of the forge, and `CLAUDE.local.md`, the facts of your
instance.

## What comes next

With the machine prepared, the first run of the forge is `/setup`,
which fills in the instance facts and sets the model. It is the next
page.

## See also

- [Set up the forge](setup.md): the first run, `/setup`, which fills the instance facts and sets the model.
- [Scripts](../reference/scripts.md): every script with what it needs and its options.
