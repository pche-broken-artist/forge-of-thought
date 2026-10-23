---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: a3eb2b1725f68847
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/hook-git.py
  - scripts/forge-config.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/forge_tools.py
  - scripts/md2video.py
---

# Install what the forge needs

This page lists what must be on your machine before Forge of Thought
runs, and the order to put it there in. Forge of Thought is a
workshop where an idea travels a chain of versioned documents under
review, with Claude working beside you
([What Forge of Thought is](what-it-is.md)). The page is for you if
you are about to use the forge for the first time. It covers git,
Python, Claude Code, the engine itself and the optional tools that
some commands need. The terms of the forge are each explained in one
line in the [Glossary](../reference/glossary.md).

## When to use it

Use it once per machine, before the first setup. Come back to the
optional tools when you first need the command that uses them.

## What you do

The steps below are in the order you first need each piece. The one
line that brings the forge itself onto your machine is:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

1. **Install git.** The forge keeps every document in git. The
   scripts that save, pull and report state need nothing beyond
   git. If you want the first setup to write a commit identity per
   host for you, git must be version 2.36 or newer. Every tool the
   forge uses is found on PATH, so git must be reachable there.
   You should now see a version of 2.36 or newer when you ask git
   for its version.

2. **Install Python 3.8 or newer, reachable as `python`.** The
   forge's scripts are Python. The two hooks are Python as well. A
   hook is a small script Claude Code runs on its own at set moments:
   one repeats the rules of a walkthrough (a list worked one item
   per message) at every prompt, and one stands before every shell
   command Claude sends and stops any write to git that does not go
   through the forge's scripts. Claude Code starts both hooks without
   a shell, by the name `python`. Because of that, a shell alias does
   not reach them: `python` must be a real executable on PATH. On a
   system that has only `python3`, give it the name `python`:
   - on Debian or Ubuntu, install the package `python-is-python3`;
   - elsewhere on Linux and on macOS, make a symlink named `python`
     that points to `python3`, in a directory on PATH.

   The scripts are written to run unchanged on Linux and macOS.
   You should now see a version of 3.8 or newer when you run
   `python --version`.

3. **Install Claude Code and sign in.** The forge runs inside Claude
   Code and needs a paid Claude subscription. Its usage draws from
   the same pool as Claude chat. One way to install it is:

   ```
   npm install -g @anthropic-ai/claude-code
   ```

   Sign in the first time you run `claude`.
   You should now see Claude Code start and ask you to sign in, and
   after that accept a prompt.

4. **Clone the engine from its public home.** The engine's public
   home is https://github.com/pche-broken-artist/forge-of-thought.
   Clone it with git; do not copy its files. The forge's git scripts
   refuse an engine that is not the top of a git repository.
   You should now see a folder `forge-of-thought` that git reports
   as a repository.

5. **Start `claude` from the engine root, always.** The engine root
   is the folder you just cloned. Claude Code reads the forge's rules
   from `CLAUDE.md` and the facts of your installation from
   `CLAUDE.local.md`, both at that root. Started anywhere else, they
   do not load.
   You should now see Claude Code start inside the engine folder.

6. **Install the optional tools when you need them.** No script
   installs anything. Each tool is found on PATH, and you install it
   yourself, once:
   - **markitdown**, for the conversions of `/ingest` (a Word,
     PowerPoint, PDF or Excel file turned into Markdown):

     ```
     pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
     ```

   - **pandoc**, for the plain Word and PowerPoint files `/render`
     makes. Install it from pandoc's own installation page or with
     your system's package manager.
   - **Pillow and ffmpeg**, for the video format of a screenplay
     render. Pillow is installed with `pip install pillow`; ffmpeg must
     be on PATH. The player format of a screenplay needs nothing
     beyond Python.
   - **the document-skills plugin**, for `/publish`, which makes the
     designed Word or PowerPoint file through a model. You need it
     only where Claude Code does not already bring the docx and pptx
     skills. Install it once from an interactive Claude Code session:

     ```
     /plugin marketplace add anthropics/skills
     /plugin install document-skills@anthropic-agent-skills
     ```

   You should now see, for markitdown, the check
   `python scripts/doc2md.py --list-tools` report that markitdown is
   reachable.

## What you have afterwards

You have git, `python` and Claude Code on your machine, the engine
cloned as a git repository, and Claude Code started from its root.
The next step is the first run, `/setup`, which prepares this
installation: [Set up the forge](setup.md). What each script needs
and its options are listed in [Scripts](../reference/scripts.md).

## If something goes wrong

- **A script stops with "The engine is not the top of a git
  repository (clone it, do not copy it)."** The engine was copied,
  not cloned. Clone it again from its public home and work in the
  clone.
- **A script stops with "git is not installed."** git is not on
  PATH. Install it, or put it on PATH, and start again.
- **The hooks fail although `python3` works in your shell.** The
  hooks are started without a shell, so an alias does not reach
  them. Make `python` a real executable on PATH as step 2 says.
- **Claude does not follow the forge's rules.** Claude Code was
  started outside the engine root, so `CLAUDE.md` and
  `CLAUDE.local.md` did not load. Quit and start `claude` again from
  the engine root.

## A worked example

One install on a machine that already has git, Python and npm, with
placeholders for your own folder:

```
git --version
python --version
npm install -g @anthropic-ai/claude-code
cd <your-folder-for-repositories>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

Inside Claude Code, the next command is `/setup`.

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
