---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 7e31c82d99f02cf2
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.1880
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

Forge of Thought runs inside Claude Code on a clone of its own
repository, with git and Python beneath it. This page is for you,
the newcomer who wants the forge on a machine: what must be there,
in the order you need it, and what you see when each piece works.
What you are installing is said in one paragraph on
[What Forge of Thought is](what-it-is.md); every term of the forge
used here is in the [Glossary](../reference/glossary.md).

## When to use it

Once per machine, before the forge is started for the first time.
Again on a new machine, and again whenever you want one of the
optional tools at the end of this page, because each of them is
installed by you and never by a script of the forge.

One line on platforms. The scripts in `scripts/` are the only layer
of the forge bound to a platform, and they are written to run
unchanged on Linux and macOS. On Linux the git scripts, the ledger
script (the ledger is the project's state, made at read time) and
the documentation state script have run; the conversions and the
two hooks are a writing rule until a run says otherwise. Nothing has
run on macOS: there the whole set is the writing rule alone.

## What you do

Five things, in this order, then the optional tools:

1. git.
2. Python 3.8 or newer, on PATH as a real executable named `python`.
3. Claude Code, with a paid Claude subscription.
4. A clone of the engine (the forge's own repository, the files that
   make it run) from its public home.
5. `claude`, started from the engine root.

## What happens

**Step 1: git.** Install git. The git scripts of the forge need
nothing beyond git itself. One part of the first setup, `/setup`,
writes your commit identity per host; that part needs git 2.36 or
newer. You should now see `git --version` answer with a version, and
2.36 or newer where `/setup` is to write the identity per host.

**Step 2: Python.** Install Python 3.8 or newer and make sure it is
on PATH as a real executable named `python`. The scripts and the two
hooks of the forge are Python. The hooks are started by Claude Code
without a shell, as the command `python` with the script's path as
its argument (`.claude/settings.json`), so a shell alias does not
reach them. A system that has only `python3` gives it the name
`python`:

- on Debian or Ubuntu, the package `python-is-python3`;
- elsewhere on Linux and on macOS, a symlink:
  `ln -s "$(command -v python3)" /usr/local/bin/python`.

You should now see `python --version` answer with 3.8 or newer from
any directory.

**Step 3: Claude Code.** You need a paid Claude subscription; usage
draws from the same pool as Claude chat. Install Claude Code by one
of its own lines:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or, with npm: `npm install -g @anthropic-ai/claude-code`

You should now see `claude` as a command your shell finds. The
sign-in comes at the first start, in step 5.

**Step 4: the clone.** Clone the engine from its public home. Never
copy it: the scripts refuse an engine that is not a git repository,
and the clone is also the upgrade channel, which `/pull`
fast-forwards from the remote.

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

You should now see a folder `forge-of-thought`: the engine root.

**Step 5: the first start.** Always start `claude` from the engine
root, so that the engine's instructions load. The two hooks are
configured in `.claude/settings.json` of the engine and are handed
their own path from the folder Claude Code was started in. Sign in
when asked on the first run.

```
cd forge-of-thought
claude
```

You should now see Claude Code open in the engine root and, this
first time, ask you to sign in.

**Step 6: the optional tools.** Each is needed by one command only,
is resolved from PATH when that command runs, and is installed by
you, never by a script of the forge. Install the ones you want, now
or later. What every script needs is listed in
[Scripts](../reference/scripts.md).

- markitdown, for the conversion of a Word, PowerPoint, PDF or Excel
  document to Markdown that `/ingest` runs through
  `scripts/doc2md.py`:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  The sign: `python scripts/doc2md.py --list-tools` reports that
  markitdown is reachable.
- pandoc, for the plain Word and PowerPoint files `/render` makes
  through `scripts/md2pptx.py` and `scripts/md2docx.py`: on Windows
  `winget install JohnMacFarlane.Pandoc`, on macOS
  `brew install pandoc`, on Linux your package manager.
- Pillow and ffmpeg, for the video format of a screenplay that
  `/render` makes through `scripts/md2video.py`: `pip install pillow`,
  and ffmpeg on PATH (on Windows `winget install Gyan.FFmpeg`, on
  macOS `brew install ffmpeg`, on Linux your package manager). Fonts
  are taken from the system where they exist and from Pillow's
  built-in font otherwise. The player format of a screenplay needs
  nothing beyond Python.
- The document-skills plugin, for `/publish`, unless Claude Code
  already brings the docx and pptx skills. `/publish` needs the
  official document skill of its format under either of its names,
  `anthropic-skills:<format>` where Claude Code brings it or
  `document-skills:<format>` where the plugin does. Where neither is
  there, type at Claude Code's prompt, once:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`.
- The command-line tool of a second engine, for a research run on
  two model families ([Research a topic](../use/research-a-topic.md)).
  Today that is `agy`, the row `antigravity` of the forge's engine
  table, at version 1.1.1 or newer. The forge asks only that the tool
  is on PATH and signed in once, in the tool's own way. How it is
  installed and how you sign in is the tool's own documentation's to
  say; the forge carries no key and no account.

You should now see each tool you installed found from any directory,
which is what being on PATH means.

## What you have afterwards

A clone of the engine on your machine, git and `python` reachable
from any directory, Claude Code signed in and started from the
engine root, and whichever optional tools you chose. The engine is
not yet prepared for you: that is the first run, `/setup`, on
[Set up the forge](setup.md).

## If something goes wrong

- A script refuses to run because the engine is not a git
  repository: you copied the engine instead of cloning it. Clone it
  (step 4) and move nothing in by hand.
- `python` is not found although `python3` is: a shell alias does
  not reach the hooks, since they are started without a shell. Give
  Python the name `python` by the package or the symlink of step 2.
  Each hook needs Python 3.8 or newer on PATH as `python` and
  nothing else.
- `/setup` cannot write the identity per host: that part needs
  git 2.36 or newer. Upgrade git.
- A command stops because a tool is missing: the forge installs
  nothing. Install the tool yourself (step 6); it is found on PATH
  when the command runs again.
- `/publish` finds no document skill: neither `anthropic-skills:docx`
  or `:pptx` nor `document-skills:docx` or `:pptx` is there. Install
  the plugin by the two lines of step 6.
- A research run on the second engine is refused with its reason
  on the error output: the tool is missing from PATH, or its version
  is below the floor of its row (1.1.1 for `antigravity`). Install
  or upgrade the tool by its own documentation and sign in once.

## A worked example

One machine, macOS or Linux, set up from nothing. `<code>` stands
for the folder where you keep your repositories.

```
git --version
python --version
curl -fsSL https://claude.ai/install.sh | bash
cd <code>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

On the first start Claude Code asks you to sign in. The optional
tools, only where you want the commands that use them:

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
brew install pandoc
pip install pillow
brew install ffmpeg
```

Then, at Claude Code's prompt in the engine root:

```
/setup
```

On Windows the one line that differs is the install of Claude Code,
`irm https://claude.ai/install.ps1 | iex`, and pandoc and ffmpeg come
by `winget install JohnMacFarlane.Pandoc` and
`winget install Gyan.FFmpeg`.

## See also

- [What Forge of Thought is](what-it-is.md): what you are
  installing, in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
