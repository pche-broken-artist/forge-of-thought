---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: ca23e370dab88db0
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

This page lists what must be on your machine before Forge of Thought
runs, in the order you need it. It is for anyone installing the
forge for the first time. The forge is a workspace where Claude helps
the principal (the person whose thinking is being forged) shape an
idea through a chain of versioned documents; what it is in full is
on [What Forge of Thought is](what-it-is.md).

## When to use it

Use this page once per machine, before the first setup. Come back to
the optional tools of the last step when you first need one of them.

## What you do

You install git, Python and Claude Code, clone the engine (the
forge's own repository, which holds its rules, commands and scripts)
and start Claude Code from its root. The one line that brings the
engine onto your machine is:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

1. **Install git.** The forge keeps its documents in git, and the git
   scripts need nothing beyond git. You should now see a version
   number when you type `git --version`.

2. **Install Python 3.8 or newer, as `python`.** The scripts are
   Python, and so is the per-prompt hook (a small script Claude Code
   runs at every message you send). The hook is started without a
   shell, by the name `python`. A shell alias therefore does not
   reach it: `python` must be a real executable on PATH.
   - On Debian or Ubuntu, install the package `python-is-python3`.
   - Elsewhere on Linux and on macOS, make a symlink:
     `ln -s "$(command -v python3)" /usr/local/bin/python`

   You should now see a Python version of 3.8 or newer when you type
   `python --version`.

3. **Install Claude Code.** You need a paid Claude subscription.
   Install Claude Code by one of these lines:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS and Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - Anywhere with npm: `npm install -g @anthropic-ai/claude-code`

   Sign in when Claude Code first runs. Its usage draws from the same
   pool as Claude chat. You should now see Claude Code start when you
   type `claude`.

4. **Clone the engine from its public home.** Clone it with git; do
   not copy its files. The scripts refuse an engine that is not a git
   repository. The public home of the engine is
   https://github.com/pche-broken-artist/forge-of-thought. You should
   now see a directory `forge-of-thought` with `CLAUDE.md` and
   `scripts/` inside it.

5. **Start `claude` from the engine root.** Always start Claude Code
   from the engine's top directory, so that `CLAUDE.md` and
   `CLAUDE.local.md` load. You should now see Claude Code open in the
   engine directory.

6. **Install the optional tools you need.** Each tool below serves one
   command. Each is found on PATH, and no script of the forge installs
   it: you install it yourself, once. Every script with what it needs
   and its options is on [Scripts](../reference/scripts.md).
   - **markitdown**, for `/ingest` when it converts a Word,
     PowerPoint, PDF or Excel file to Markdown:
     `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`
   - **pandoc**, for the plain Word and PowerPoint files that
     `/render` makes from a render (a generated output of a project):
     on Windows `winget install JohnMacFarlane.Pandoc`, on macOS
     `brew install pandoc`, on Linux your package manager.
   - **Pillow and ffmpeg**, for the video format of a screenplay (a
     render shown as a simulated terminal): Pillow by
     `pip install pillow`, and ffmpeg on PATH, on Windows by
     `winget install Gyan.FFmpeg`, on macOS by `brew install ffmpeg`,
     on Linux by your package manager. The player format of a
     screenplay needs nothing beyond Python.
   - **The `document-skills` plugin**, for `/publish`, which makes a
     designed Word or PowerPoint file through a model. You need it
     only where Claude Code does not already bring the docx and pptx
     skills. Install it once from an interactive Claude Code session
     (one running conversation in Claude Code) by these two lines, in
     order:

     ```
     /plugin marketplace add anthropics/skills
     /plugin install document-skills@anthropic-agent-skills
     ```

   You should now see markitdown reported as reachable when you type
   `python scripts/doc2md.py --list-tools`, if you installed it.

The terms used here are each explained in one line in the
[Glossary](../reference/glossary.md).

## What you have afterwards

You have git, Python as `python`, a signed-in Claude Code and a clone
of the engine, with Claude Code started from its root. The next step
is the first setup of the instance (your one installation of the
forge): [Set up the forge](setup.md).

## If something goes wrong

- **The hook does not run although `python3` works in your shell.**
  The hook needs a real executable named `python` on PATH, and an
  alias does not count. Install `python-is-python3` or make the
  symlink of step 2.
- **A script refuses to run on the engine.** The engine was copied
  instead of cloned. Clone it with git, as in step 4.
- **`/ingest` cannot convert a document.** markitdown is missing or
  not on PATH. Install it with the pip line of step 6. The command
  `python scripts/doc2md.py --list-tools` checks whether markitdown
  can be reached.

## A worked example

One install, typed in order on a machine that already has git,
Python as `python` and a signed-in Claude Code. `<parent-dir>` stands
for whatever directory you keep the engine in.

```
git --version
python --version
cd <parent-dir>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

Inside Claude Code, the next thing you type is `/setup`.

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Scripts](../reference/scripts.md): every script with what it needs
  and its options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
