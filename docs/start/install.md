---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: cc7d7c7aa12a1b76
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
runs, and the order to install it in. It is for anyone who is about
to use the forge for the first time. What you are installing is
described in [What Forge of Thought is](what-it-is.md).

## When to use it

Use it once per machine, before the first setup. Each step comes in
the order you first need it. The optional tools come last, and you
install only the ones for the commands you mean to use.

The forge is not tied to one operating system. Its scripts are
written to run unchanged on Linux and macOS. The git scripts, the
ledger script (the script that builds the state of a project) and the
documentation state script have run on Linux. The conversions and the
two hooks are written to that rule, but no run has shown it yet.

## What you do

You install three tools, then clone the engine and start Claude Code
from its root:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

1. **Install git.** The forge keeps every project in git, and its own
   scripts are the way it writes to git. The git scripts need nothing
   beyond git. Where the first setup is to write your commit identity
   per host, git must be version 2.36 or newer.

   You should now see a version of 2.36 or newer when you type
   `git --version`.

2. **Install Python 3.8 or newer, on PATH as a real executable named
   `python`.** The scripts are Python. The two hooks are Python as
   well (a hook is a script Claude Code runs on its own at a given
   moment, here at every prompt and before every shell command). Claude
   Code starts both hooks as `python` and without a shell. So a shell
   alias named `python` does not reach them: the name must be a real
   executable. A system that has only `python3` gives it that name:
   - on Debian or Ubuntu, install the package `python-is-python3`;
   - elsewhere on Linux and on macOS, make a symlink:
     `ln -s "$(command -v python3)" /usr/local/bin/python`.

   You should now see a version of 3.8 or newer when you type
   `python --version`.

3. **Install Claude Code.** You need a paid Claude subscription. Use
   one of these lines:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - with npm: `npm install -g @anthropic-ai/claude-code`

   You sign in on the first run. Usage draws from the same pool as
   Claude chat.

   You should now see `claude` start when you type it, and ask you to
   sign in the first time.

4. **Clone the engine from its public home.** Clone it, never copy
   it. The scripts refuse an engine that is not the top of a git
   repository.

   You should now see a folder `forge-of-thought` holding the engine.

5. **Start `claude` from the engine root, always.** Only there do
   `CLAUDE.md` and `CLAUDE.local.md` load, which carry the rules of
   the forge and the facts of your installation.

   You should now see Claude Code open in the engine's folder.

6. **Add the optional tools you need.** Each is found on PATH, and no
   script of the forge installs any of them. You install it yourself:
   - **markitdown**, for the conversions of `/ingest` (a document
     turned into Markdown):
     `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
   - **pandoc**, for the plain Word and PowerPoint files that
     `/render` makes. Install it once from pandoc's own installation
     page or your package manager.
   - **Pillow and ffmpeg**, for the video format of a screenplay:
     `pip install pillow`, and ffmpeg on PATH. The player format of a
     screenplay needs nothing beyond Python.
   - **The document-skills plugin**, for `/publish`, unless Claude
     Code already brings the docx and pptx skills. Install it once
     from an interactive Claude Code session:
     `/plugin marketplace add anthropics/skills`, then
     `/plugin install document-skills@anthropic-agent-skills`.
   - **The command-line tool of a second engine**, for a research on
     two model families (described in [Research a topic](../use/research-a-topic.md)).
     Today that is `agy`, the engine named `antigravity`, at version
     1.1.1 or newer. It must be on PATH and signed in once in its own
     tool. The forge carries no key and no account for it.

   You should now see each tool you installed answer from PATH.
   For markitdown, `python scripts/doc2md.py --list-tools` checks that
   it is reachable.

What each script needs, with its options, is listed in
[Scripts](../reference/scripts.md).

## What you have afterwards

You have git, Python and Claude Code on your machine, a clone of the
engine, and Claude Code started from its root. The next step is the
first run, `/setup`, described in [Set up the forge](setup.md). Every
term of the forge is explained in one line in the
[Glossary](../reference/glossary.md).

## If something goes wrong

- **A script stops with "The engine is not the top of a git
  repository (clone it, do not copy it)."** The engine was copied,
  not cloned. Clone it again from its public home.
- **The hooks do not run, while `python` works in your shell.** The
  name `python` may be a shell alias. The hooks are started without a
  shell, so give `python` a real executable as in step 2.
- **A research on a second engine is refused.** The engine's tool is
  missing from PATH, or its version is below the floor (1.1.1 for
  `antigravity`). Install or update it, and sign in once in its own
  tool.

## A worked example

One install on a machine that already has git, Python and Claude
Code, with `<folder>` standing for wherever you keep your work:

```
git --version
python --version
cd <folder>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

Inside Claude Code, the next line you type is `/setup`.

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Scripts](../reference/scripts.md): every script with what it needs
  and its options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
