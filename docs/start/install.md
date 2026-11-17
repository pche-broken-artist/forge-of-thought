---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 2726fe9beb5cadbc
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Portability
  - CLAUDE.md#The system's own project
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/10-intent.md#POS.1930
  - projects/forge/10-intent.md#POS.1980
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/hook-git.py
  - scripts/forge-config.py
  - scripts/forge_repos.py
  - scripts/forge-status.py
  - scripts/doc2md.py
  - scripts/forge_tools.py
  - scripts/md2video.py
  - scripts/forge-engine.py
  - .claude/skills/test/SKILL.md
---

# Install what the forge needs

Forge of Thought is installed as a clone of one git repository, the
[engine](../reference/glossary.md), and is worked in Claude Code (the
command-line program `claude`). This page says what must be on your
machine before the forge runs, in the order a newcomer needs it, and
what you see when each step worked. It is for anyone who is about to
use the forge for the first time. What you are installing is said in
one paragraph on [What Forge of Thought is](what-it-is.md).

## When to use it

Use it once on every machine the forge is to run on, before the first
run. A program that is already there in the version named needs no
new install.

The forge runs beyond Windows. What a run has shown, and what it has
not, is this:

- The scripts are the only layer of the forge bound to a platform.
  They are written to run unchanged on Linux and macOS.
- The engine's tests run in CI, that is automatically at every push,
  on Linux and Windows. Among what they cover are the git scripts,
  the [ledger](../reference/glossary.md) (made from a project's
  documents), the [light check](../reference/glossary.md) and the
  judgement of the git hook over a command.
- The conversions of documents are tested only for their failure
  without the tool.
- The per-prompt hook is a writing rule until a run says otherwise:
  the script is written by the rule, and no run has confirmed it yet.
- Nothing has run on macOS. There the whole set is the writing rule
  alone.

The two hooks are scripts that Claude Code starts by itself. Step 2
says what they are.

## What you do

You install three programs, clone the engine and start Claude Code in
the clone:

1. git;
2. Python 3.8 or newer, answering to the name `python`;
3. Claude Code, with a paid Claude subscription;
4. a clone of the engine;
5. `claude`, started from the root of that clone.

The optional tools come last, each one when you first want what it
serves.

Of the five, the line that brings the forge itself is the clone. As it
is typed:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

### 1. Install git

Install git by your system's own means. It must be on PATH, that is
found by its name from any directory of a terminal. Beyond Python
(step 2), the git scripts of the forge need nothing but git. Version
2.36 or newer is needed where `/setup`, the command of the first
setup, is to write the identity per host. What that is, is said on
[Set up the forge](setup.md).

You should now see git found by its name in a terminal, in version
2.36 or newer where the first setup is to write the identity per
host.

### 2. Install Python and give it the name `python`

Python 3.8 or newer must be on PATH as a real executable named
`python`. The scripts of the forge are Python and are run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite.

The two hooks of the forge are Python too. A hook is a script that
Claude Code starts by itself at a fixed moment:

- the per-prompt hook, at every prompt you send: it repeats to Claude
  the rules that must hold in a long conversation;
- the git hook, before every Bash command Claude sends: it judges
  every part of the command that calls git.

Claude Code starts both hooks as `python`, without a shell. A shell
alias therefore does not reach them.

A system that has only `python3` gives it the name `python`:

- on Debian or Ubuntu, by the package `python-is-python3`;
- elsewhere on Linux and on macOS, by a symlink:

  ```
  ln -s "$(command -v python3)" /usr/local/bin/python
  ```

You should now see `python`, typed by exactly that name in a
terminal, start Python 3.8 or newer.

### 3. Install Claude Code

Claude Code needs a paid Claude subscription. Install it by one of
these lines:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or: `npm install -g @anthropic-ai/claude-code`

You sign in on the first run, which is step 5.

You should now see `claude` found by its name in a terminal.

### 4. Clone the engine

Clone the engine from its public home:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

Clone it, never copy it. The git scripts of the forge refuse an
engine that is not a git repository.

The engine is all you clone. The forge's own project
(`projects/forge`, that is Forge of Thought itself run through its
own process) is a repository of its own and is needed by no user.
Only whoever develops the engine clones it beside the engine. How
that is done is said on
[Make a change to the forge](../extend/how-a-change-is-made.md).

You should now see the directory of the clone, with `CLAUDE.md` and
`scripts/` at its root and a directory `projects/` that holds a line
on what belongs in it and no project.

### 5. Start `claude` from the engine root

Always start `claude` from the root of the clone, the engine root.
That is where `CLAUDE.md` and `CLAUDE.local.md` load from. On its
first run Claude Code has you sign in. Usage draws from the same pool
as Claude chat.

You should now see Claude Code signed in, open in the engine root and
waiting for your prompt.

### 6. Add the optional tools when you want what they serve

Nothing of this step is needed for the first run. Every tool below is
resolved from PATH and installed by no script of the forge: you
install it yourself, once. What each script needs is listed on
[Scripts](../reference/scripts.md).

- **markitdown**: for the conversion of Word, PowerPoint, PDF and
  Excel documents to Markdown, done by `doc2md.py`. Install it with
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- **pandoc**: for the Word and PowerPoint files that `/render` makes
  through `md2docx.py` and `md2pptx.py`. Install it with
  `winget install JohnMacFarlane.Pandoc` on Windows, with
  `brew install pandoc` on macOS, with your package manager on Linux.
- **Pillow and ffmpeg**: for the video format of a
  [screenplay](../reference/glossary.md), made behind `/render` by
  `md2video.py`. Install Pillow with `pip install pillow`. Put ffmpeg
  on PATH with `winget install Gyan.FFmpeg` on Windows, with
  `brew install ffmpeg` on macOS, with your package manager on Linux.
  The player format, which plays in the browser, needs nothing beyond
  Python.
- **The `document-skills` plugin**: for `/publish`, which makes a
  Word or PowerPoint file through Claude Code and its document
  skills. You do not need the plugin where Claude Code already brings
  the docx and pptx skills. Install it once, by two lines typed into
  Claude Code while it runs interactively:

  ```
  /plugin marketplace add anthropics/skills
  /plugin install document-skills@anthropic-agent-skills
  ```

- **The command-line tool of a second engine**: for a research on two
  model families (see [Research a topic](../use/research-a-topic.md)).
  A second engine is a model of another family, reached through its
  own command-line tool. Today the forge has one such row in its
  table of engines: `antigravity`, whose tool is `agy`, at version
  1.1.1 or newer. The forge asks only that the tool is on PATH and
  that you have signed in once, in the tool itself. How the tool is
  installed and signed in is said by the tool's own documentation.
  The forge carries no key and no account.
- **`gh`**, the command-line tool of GitHub, on PATH and logged in:
  for the line that says what waits on GitHub outside git, that is
  the open pull requests and the discussions nobody of the repository
  has answered. Without `gh` that line says that it could not read,
  and why.
- **pytest**: for a contributor only. `python -m pip install pytest`
  is the one thing a contributor installs beyond `python` to run the
  engine's tests (see [Run the tests](../use/run-the-tests.md)). A
  user of the engine never runs the tests and installs nothing for
  them.

You should now see each tool you installed found by its name in a
terminal. For markitdown, `python scripts/doc2md.py --list-tools`
checks that it is reachable.

## What you have afterwards

- git, Python under the name `python` and Claude Code on your
  machine;
- a clone of the engine, with no project in `projects/`;
- Claude Code signed in and started in the engine root.

What comes next is the first setup: [Set up the forge](setup.md).

## If something goes wrong

- **The system has only `python3`, or `python` is a shell alias.**
  The scripts and the hooks need a real executable named `python`.
  Give Python that name by the package or the symlink of step 2.
- **A git script refuses the engine.** The engine was copied, not
  cloned, and is not a git repository. Clone it from its public home
  (step 4).
- **`claude` was started from another directory.** `CLAUDE.md` and
  `CLAUDE.local.md` do not load. Leave Claude Code and start it again
  from the engine root (step 5).
- **A conversion fails for want of its tool.** The failure names the
  tool and how it is installed. No script installs it: install it
  yourself (step 6).
- **The run on a second engine is refused.** The script refuses, with
  the reason, a tool that is not on PATH or that is older than the
  version its row asks for (1.1.1 for `antigravity`).
- **The line on GitHub says it could not read.** `gh` is missing or
  not logged in, the origin is not GitHub, or there is no network.
  The line says which, and the rest of the report goes on.
- **`No module named pytest`.** The tests did not run. Install the
  runner with `python -m pip install pytest`.

## A worked example

The sequence as it is typed where Claude Code is installed by the
line for macOS and Linux. A line in angle brackets is a placeholder:
what stands there depends on your system. The symlink line is typed
only where the system has `python3` alone. On Windows the Claude Code
line is the Windows line of step 3.

```
<install git, by your system's own means>
<install Python 3.8 or newer, by your system's own means>
ln -s "$(command -v python3)" /usr/local/bin/python
curl -fsSL https://claude.ai/install.sh | bash
cd <the directory you keep your work in>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

After the last line Claude Code has you sign in, and the first setup
follows.

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Run the tests](../use/run-the-tests.md): the tests a contributor
  runs with `/test`.
- [Make a change to the forge](../extend/how-a-change-is-made.md):
  how whoever develops the engine clones the forge's own project
  beside it and sends a change.
- [Scripts](../reference/scripts.md): every script with what it needs
  and its options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
