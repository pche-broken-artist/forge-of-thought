---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 61fd4ba63d95ed54
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/forge_tools.py
  - scripts/md2video.py
---

# Install what the forge needs

Installing the forge means putting three tools on your machine, in
order, and then cloning the engine, the repository that holds the
forge itself (what it is: [What Forge of Thought is](what-it-is.md)).
This page is for a newcomer who has nothing yet. It says what to
install, in which order, and what you see when each step worked.
Everything else is optional and comes last: one tool per command
that converts a file, none of them installed by any script.

## When to use it

Use this page once, on a machine where the forge has never run.
When the three tools are in place and the engine is cloned, go on
to the first run: [Set up the forge](setup.md).

## What you do

The order is the order in which each piece is first needed: the
scripts need Python and git, Claude Code needs its sign-in, the
clone needs git, and the first session needs all of them.

1. Install git.
2. Install Python 3.8 or newer and make sure it answers to the name
   `python`.
3. Install Claude Code and sign in with a paid Claude subscription.
4. Clone the engine from its public home. Never copy it.
5. Start `claude` from the engine root, always.
6. Install the optional tools you want, each by hand.

The one line that brings the engine in, typed where you want it to
live:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

### Step 1: git

Install git the way your platform does. The forge keeps git behind
its own scripts, so you will rarely type a git command yourself;
the scripts need nothing beyond git. The scripts stop with
`git is not installed.` where git is not found.

You should now see a version when you type `git --version`.

### Step 2: Python 3.8 or newer, named `python`

Install Python 3.8 or newer. It must be on PATH as a real executable
named `python`, not as a shell alias. The scripts of the forge are
Python and are run as `python scripts/<name>.py`. The per-prompt
hook is Python too: a small script that Claude Code runs on every
prompt you submit, started as `python` directly, without a shell.
Because no shell is involved, a shell alias does not reach it.

A system that has only `python3` must give it the name `python`:

- on Debian or Ubuntu, the package `python-is-python3`;
- elsewhere on Linux and on macOS, a symlink:
  `ln -s "$(command -v python3)" /usr/local/bin/python`.

The inputs give no remedy for Windows beyond the requirement
itself: the executable is named `python` there.

You should now see a version of 3.8 or newer when you type
`python --version`.

### Step 3: Claude Code

Claude Code is the program in which Claude runs. Install it by one
of these lines:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- any platform with npm: `npm install -g @anthropic-ai/claude-code`

Sign in on first run with a paid Claude subscription. Usage draws
from the same pool as Claude chat.

You should now see `claude` start and ask you to sign in the first
time, and start without asking afterwards.

### Step 4: clone the engine

Clone the engine from its public home,
https://github.com/pche-broken-artist/forge-of-thought. This is the
address a clone and a project's README point to.

The forge is cloned, not copied. The engine is one git repository
with a remote, and the save script refuses an engine that is not a
git repository: it stops with
`The engine is not a git repository (clone it, do not copy it).`
A copied folder has no `.git` and will never save.

You should now see a folder `forge-of-thought` with a `.git` folder
inside it, and `python scripts/forge-status.py` run from that folder
reporting the state of the repository without changing anything.

### Step 5: start from the engine root

Always start `claude` from the engine root, the folder you just
cloned. The files `CLAUDE.md` and `CLAUDE.local.md` load from there
and nowhere else. `CLAUDE.md` is the forge's own instruction to
Claude; `CLAUDE.local.md` holds the facts of your installation, and
the first run creates it ([Set up the forge](setup.md)).

You should now see Claude Code open in the engine root and, from
the first prompt on, the lines the per-prompt hook prints into the
turn: the hook is working, so `python` is found.

### Step 6: the optional tools

Each of these serves one command and is resolved from PATH. No
script installs any of them, and the model behind `/publish` is
told to install and download nothing as well. Install only what you
will use, and at any later time.

- **markitdown**, for the conversions of `/ingest`. The script
  `scripts/doc2md.py` turns Word, PowerPoint, PDF and Excel files
  into Markdown through markitdown and nothing else. Install it
  with
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  You should now see `python scripts/doc2md.py --list-tools` report
  that markitdown is reachable.
- **pandoc**, for the plain Word and PowerPoint files of `/render`
  (the scripts `scripts/md2pptx.py` and `scripts/md2docx.py` with
  their pandoc engine). Install it once from
  https://pandoc.org/installing.html: on Windows
  `winget install JohnMacFarlane.Pandoc`, on macOS
  `brew install pandoc`, on Linux your package manager.
  You should now see pandoc found on PATH, and `/render` of a recipe
  that names a format leaving a `.docx` or `.pptx` beside the
  render.
- **Pillow and ffmpeg**, for the video format of a screenplay
  (`scripts/md2video.py`, behind `/render` of a screenplay). Install
  Pillow with `pip install pillow` and ffmpeg on PATH from
  https://ffmpeg.org: on Windows `winget install Gyan.FFmpeg`, on
  macOS `brew install ffmpeg`, on Linux your package manager. The
  player format needs nothing beyond Python. Fonts are taken from
  the system where they exist and from Pillow's built-in font
  otherwise.
  You should now see `--frame` of the script paint one frame of a
  video to a PNG: a check of the look without the whole render.
- **The document-skills plugin**, for `/publish`. The `claude`
  engine behind `/publish` needs the `claude` CLI on PATH and the
  official document skill of the format, pptx or docx, under either
  of its names: `anthropic-skills:<format>` where Claude Code brings
  it, `document-skills:<format>` where the plugin does. Where
  neither is there, install the plugin once from an interactive
  Claude Code session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`.
  You should now see the docx and pptx skills listed under one of
  the two names.

What each script needs and its options are in
[Scripts](../reference/scripts.md).

## What you have afterwards

- git, Python 3.8 or newer as `python`, and Claude Code signed in.
- The engine as a git repository with a remote, in a folder of
  your choice. `main` is the released line.
- A machine ready for the first run, `/setup`, which prepares your
  installation: [Set up the forge](setup.md). Git identity is set
  there, not here.
- Whichever optional tools you chose, each found on PATH by the
  command it serves.

## If something goes wrong

- `git is not installed.`: a git script stopped because git is not
  on PATH. Install git and try again.
- `The engine is not a git repository (clone it, do not copy it).`:
  the save script found no `.git` in the engine root. The engine
  was copied. Delete the copy and clone it.
- The per-prompt hook prints nothing, or Claude Code reports that
  it failed: `python` is not a real executable on PATH. A shell
  alias does not reach the hook. Give Python the name `python` as
  step 2 says.
- `python scripts/doc2md.py --list-tools` does not find markitdown:
  markitdown is not on PATH. Install it by the pip line, or name
  its executable with `--markitdown-path`.
- A conversion script stops naming a tool it did not find: the tool
  is not on PATH. Each script resolves its tool from PATH and never
  installs it. Install the tool and run the command again.
- `/publish` finds no document skill: neither name is present.
  Install the plugin from an interactive Claude Code session as step
  6 says.

## A worked example

One run of the sequence, on a machine with git, Python and Claude
Code already installed by their own installers, as typed. The
folder name is yours to choose; the path is a placeholder.

```
git --version
python --version
claude
```

You see a git version, a Python version of 3.8 or newer, and Claude
Code asking you to sign in. Sign in and leave Claude Code.

```
cd <where-you-keep-repositories>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
python scripts/forge-status.py
```

You see the clone being made and the status script reporting a
clean repository on `main`.

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
python scripts/doc2md.py --list-tools
```

You see markitdown reported as reachable. This step is optional.

```
claude
```

Started from the engine root, Claude Code loads `CLAUDE.md`. Your
first prompt is `/setup`: [Set up the forge](setup.md).

## See also

- [What Forge of Thought is](what-it-is.md): what you are
  installing, in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
