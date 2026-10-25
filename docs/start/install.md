---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 8f210ae04489b336
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
  - scripts/forge-engine.py
---

# Install what the forge needs

This page lists what must be on your machine before Forge of Thought
runs, in the order you need each piece. Forge of Thought is a
workspace where an idea travels a chain of versioned documents under
review. It is described in one paragraph on
[What Forge of Thought is](what-it-is.md). The required pieces come
first. The optional tools come last, each needed only by the command
that uses it. The page ends where the first setup begins.

## When to use it

Use this page once per machine, before you start the forge for the
first time.
Use the optional part again when you first need a command that
converts documents, makes Word or PowerPoint files, makes a video, or
runs a research on two model families.

## What you do

The required steps, in order:

1. Install git.
2. Install Python 3.8 or newer, reachable as `python`.
3. Install Claude Code and sign in.
4. Clone the engine from its public home.
5. Start `claude` from the engine root.

The optional tools follow, in any order.

## What happens

### 1. git

Install git.
The git scripts of the forge need nothing beyond git.
Where `/setup` is to write your identity per host, git must be
version 2.36 or newer. The configuration it writes relies on a
feature of git that older versions lack.

You should now see a version of 2.36 or newer when you type
`git --version`.

### 2. Python 3.8 or newer, named `python`

Install Python 3.8 or newer.
It must be on PATH as a real executable named `python`.
This is because the scripts of the forge are Python, and so are its
two hooks. A hook is a small script Claude Code starts by itself: one
runs at every prompt, one before every shell command Claude sends.
Claude Code starts both hooks as `python` without a shell.
So a shell alias that maps `python` to `python3` does not reach them.

Where your system has only `python3`, give it the name `python`:

- on Debian or Ubuntu, install the package `python-is-python3`;
- elsewhere on Linux and on macOS, make a symlink:
  `ln -s "$(command -v python3)" /usr/local/bin/python`.

The scripts are written to run unchanged on Linux and macOS as well
as Windows.

You should now see a version of 3.8 or newer when you type
`python --version`.

### 3. Claude Code, with a paid subscription

Claude Code needs a paid Claude subscription.
Install it with one of these lines:

- on Windows: `irm https://claude.ai/install.ps1 | iex`
- on macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- anywhere npm is installed: `npm install -g @anthropic-ai/claude-code`

Sign in when you start `claude` for the first time.
Its usage draws from the same pool as Claude chat.

You should now see Claude Code start and ask you to sign in, and
then accept your prompts.

### 4. Clone the engine

Clone the engine from its public home,
https://github.com/pche-broken-artist/forge-of-thought.
Clone it; never copy it.
The git scripts refuse an engine that is not a git repository.

You should now see a folder holding `CLAUDE.md`, `scripts/`,
`templates/` and `.claude/`.

### 5. Start `claude` from the engine root

Always start `claude` from the engine root, that is the folder the
clone made.
Only there do `CLAUDE.md` and the instance file `CLAUDE.local.md`
load. The instance file holds the facts of your installation, and
`/setup` creates it on the first run.

You should now see Claude Code open in the engine root, ready for
`/setup`.

### Optional tools

Each tool below is resolved from PATH.
No script of the forge installs any of them: you install each
yourself, once.

- **markitdown**, for the conversions of `/ingest` (a Word,
  PowerPoint, PDF or Excel file turned into Markdown):
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  You should now see `python scripts/doc2md.py --list-tools` report
  that markitdown is reachable.
- **pandoc**, for the plain Word and PowerPoint files that `/render`
  makes: install it from pandoc's own installation page, or through
  your system's package manager.
- **Pillow and ffmpeg**, for the video format of a screenplay:
  `pip install pillow`, and ffmpeg on PATH.
  The player format of a screenplay needs nothing beyond Python.
- **The `document-skills` plugin**, for `/publish`, unless Claude
  Code already brings the docx and pptx skills.
  Install it once from an interactive Claude Code session (one run
  of `claude` in which you type), with these two lines:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`.
- **The command-line tool of a second engine**, for a research on
  two model families, described on [Research a topic](../use/research-a-topic.md).
  Today one engine is supported: the row `antigravity`, whose tool is
  `agy`.
  It must be on PATH at version 1.1.1 or newer.
  Sign in to it once, in its own tool.
  The forge carries no key and no account for it.

What every script needs, with its options, is listed on
[Scripts](../reference/scripts.md).

## What you have afterwards

You have git, Python reachable as `python`, a signed-in Claude Code
and a clone of the engine.
You have whichever optional tools the commands you plan to use need.
The next step is the first run, `/setup`, on
[Set up the forge](setup.md).
Terms of the forge you meet there are explained in one line each in
the [Glossary](../reference/glossary.md).

## If something goes wrong

- **A hook fails because `python` is not found.** `python` is an
  alias, or only `python3` exists. Give Python the real name
  `python`, as in step 2.
- **A git script refuses the engine.** The engine was copied, not
  cloned. Clone it from its public home.
- **`CLAUDE.md` does not seem to apply.** `claude` was started
  outside the engine root. Start it again from the engine root.
- **The identity per host does not take effect.** git is older than
  2.36. Update git.
- **A conversion says markitdown is not reachable.** Install it with
  the pip line above, or check that it is on PATH.
- **A research refuses the second engine.** The research script
  refuses when the tool is missing from PATH, or when its version is
  below 1.1.1. Install or update `agy`, and sign in to it once.

## A worked example

One run on macOS or Linux, the folder name a placeholder:

```
git --version
python --version
curl -fsSL https://claude.ai/install.sh | bash
git clone https://github.com/pche-broken-artist/forge-of-thought <folder>
cd <folder>
claude
```

At the first start, sign in; then type `/setup`.

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Scripts](../reference/scripts.md): every script with what it needs
  and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
