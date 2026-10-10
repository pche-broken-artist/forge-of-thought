---
generated: 2026-10-10
made: derived
inputs-hash: 612b3f940dbf6ca2
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/forge-save.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/md2pptx.py
  - scripts/md2docx.py
  - scripts/forge_tools.py
  - projects/forge/recipes/readme.md
---

# Install what the forge needs

This page is for someone putting the forge on a machine for the
first time. It says what must be installed before the forge runs,
how each piece is installed and in which order a newcomer needs it,
then how the engine itself is brought in and started. It was put
together from `CLAUDE.md`, the engine's `.claude/settings.json`, the
help headers of the scripts in `scripts/` and the pinned facts of the
readme recipe, which are the one home of the prerequisites and of
the engine's public address.

## What you need, in order

Three things must be there before anything else works: git, Python,
and Claude Code with a paid subscription. A few more tools are
optional and serve one command each; install them when you reach
that command. Every external tool is found on PATH and never
installed by a script of the forge: you install each one yourself,
once.

The order below is the order in which each piece is first needed.

## 1. git

The engine is a git repository and every project you make in it is
a repository of its own. The forge's git scripts, `forge-save.py`
among them, need `git` on PATH and stop with "git is not installed"
when it is missing. Install git from your platform's usual source
and check that `git` answers in a terminal.

## 2. Python 3.8 or newer, on PATH as `python`

Everything the forge runs is Python: every script in `scripts/` and
the hook that Claude Code runs at every prompt. That hook is started
through the command `python` by the engine's settings, and the hook
itself needs nothing but Python 3.8 or newer on PATH under that
name. This is why Python comes before Claude Code: without it, the
very first prompt of a session already fails.

What you do:

- Install Python 3.8 or newer.
- Make sure the command `python` works in a terminal. The scripts
  are run as `python scripts/<name>.py`; `python` on PATH is their
  one prerequisite.
- On Linux or macOS, where often only `python3` exists, give it the
  name `python`: by an alias, or by the `python-is-python3` package
  where your distribution offers it.

The scripts are written to run unchanged on Linux and macOS: paths
are composed portably and external tools are resolved from PATH, so
nothing in them is bound to one platform.

## 3. Claude Code, with a paid subscription

The forge is run inside Claude Code. You need a paid Claude
subscription; usage draws from the same pool as Claude chat.

Install Claude Code by one of these commands:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- Any platform with npm: `npm install -g @anthropic-ai/claude-code`

Sign in on the first run. After that the `claude` command is on
PATH, which the forge's conversion scripts also rely on (step 4).

## 4. Optional tools, by what they serve

Each of these serves one command. None is needed to start; install
the one you need when you reach that command. The scripts find each
tool on PATH and install nothing themselves.

### markitdown, for `/ingest`

`/ingest` converts a Word, PowerPoint, PDF or Excel document into a
Markdown extract through `scripts/doc2md.py`, and that script does
the conversion exclusively with markitdown. Install it with:

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
```

Without it, text sources can still be registered; only the
conversion of a binary document needs it.

### pandoc, for the plain files of `/render`

Where a recipe names a Word or PowerPoint format, `/render` makes a
plain `.docx` or `.pptx` beside the Markdown render through pandoc:
deterministic, cheap, the same result every time. Install pandoc
once from https://pandoc.org/installing.html; on Windows `winget
install JohnMacFarlane.Pandoc`, on macOS `brew install pandoc`, on
Linux through your package manager.

### The document skills, for `/publish`

`/publish` makes the designed file through a model, running Claude
Code non-interactively with the official document skill of the
format, docx or pptx. The skill is present under either of two
names: Claude Code may bring it itself, or the `document-skills`
plugin provides it. Where neither is there, install the plugin once
from an interactive Claude Code session:

```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Skip this if Claude Code already brings the docx and pptx skills.

## 5. Clone the engine

The engine's public home is
https://github.com/pche-broken-artist/forge-of-thought. This is the
address a clone and a project's README point to; it is a fact of the
product, not of any one installation.

Clone it with git. Do not copy the directory: the forge is cloned,
not copied, and `forge-save.py` refuses an engine that is not a git
repository ("The engine is not a git repository (clone it, do not
copy it)"). A clone is also how the engine is upgraded later, since
its released line is pulled from the remote.

## 6. Always start `claude` from the engine root

Open a terminal in the directory you cloned, the engine root, and
start `claude` there. Claude Code loads `CLAUDE.md` and
`CLAUDE.local.md` from the directory it starts in; started anywhere
else, the forge's rules and your instance facts are not loaded and
the commands do not behave as the forge intends.

## What comes next

With the tools in place and the engine cloned, the first thing to do
inside Claude Code is the first setup, `/setup`: it creates and
fills the instance facts and sets the model. The page on setting up
the forge takes it from here.

## See also

- [Set up the forge](setup.md): the first run, `/setup`, which fills
  the instance facts and sets the model.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
