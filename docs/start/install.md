---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 6d6f2b0a936c8f5e
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

This page lists the programs that must be on your machine before Forge
of Thought runs, in the order you need them. It is for anyone setting
up the forge for the first time. What you are installing is described
in [What Forge of Thought is](what-it-is.md). The forge has one
required set of tools, which comes first. A few optional tools follow,
each needed only by one command. The forge's own repository is called
the engine: it holds the rules, the commands and the scripts. Every
other term is in the [Glossary](../reference/glossary.md).

## When to use it

Use this page once per machine, before the first setup. Come back to
its last part when you first want a command that needs an optional
tool.

## What you do

The required steps, typed in order, are these lines:

```
git --version
python --version
claude
git clone https://github.com/pche-broken-artist/forge-of-thought <folder>
```

Then start `claude` from inside `<folder>`, as step 5 says.

## What happens

1. **Install git.** Any git runs the forge's git scripts, which need
   nothing beyond git. `/setup` can write a commit identity for each
   host you push to. That needs git 2.36 or newer. Run
   `git --version` to check.

   You should now see a git version printed, 2.36 or newer if you want
   `/setup` to write the identity per host.

2. **Install Python 3.8 or newer, on PATH as `python`.** The scripts
   are Python. So are the two hooks (small programs Claude Code runs on
   its own at every prompt and before every shell command Claude
   sends). Claude Code starts both hooks directly as `python`, without
   a shell. A shell alias therefore does not reach them: `python` must
   be a real executable. On a system that has only `python3`, give it
   that name:
   - on Debian or Ubuntu, install the package `python-is-python3`;
   - elsewhere on Linux and on macOS, make a symlink:
     `ln -s "$(command -v python3)" /usr/local/bin/python`.

   You should now see `python --version` print Python 3.8 or newer,
   started from a new terminal.

3. **Install Claude Code.** You need a paid Claude subscription. Use
   one of these lines:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS and Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - anywhere with npm: `npm install -g @anthropic-ai/claude-code`

   Run `claude` and sign in on the first run. Usage draws from the same
   pool as Claude chat.

   You should now see Claude Code signed in and ready for a prompt.

4. **Clone the engine.** Clone it from its public home,
   `https://github.com/pche-broken-artist/forge-of-thought`. Never copy
   the files instead. The scripts refuse an engine that is not a git
   repository.

   You should now see a folder holding `CLAUDE.md`, `scripts/` and
   `.claude/`.

5. **Always start `claude` from the engine root.** The engine root is
   the folder you cloned. Started there, Claude Code loads `CLAUDE.md`
   and `CLAUDE.local.md`, the files that carry the forge's rules and
   the facts of your installation.

   You should now see Claude Code open with the engine as its working
   folder.

### On platforms

The scripts are written to run unchanged on Linux and macOS. The git
scripts, the ledger script and the documentation state script have run
on Linux. The conversions and the two hooks are a writing rule until a
run says otherwise.

### The optional tools

Each tool below is needed by one command only. Each is resolved from
PATH, and no script installs it: you install it yourself, once.

- **markitdown**, for the conversions of `/ingest` (a Word, PowerPoint,
  PDF or Excel file made into Markdown):
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  You should now see `python scripts/doc2md.py --list-tools` report
  markitdown as reachable.
- **pandoc**, for the plain Word and PowerPoint files that `/render`
  makes where a recipe names a format. Install it from the pandoc
  project, or on macOS with `brew install pandoc` and on Linux with
  your package manager.
- **Pillow and ffmpeg**, for the video format of a screenplay render:
  `pip install pillow`, and ffmpeg on PATH (on macOS
  `brew install ffmpeg`, on Linux your package manager). The player
  format needs nothing beyond Python.
- **The document-skills plugin**, for `/publish`, unless Claude Code
  already brings the docx and pptx skills. Install it once from an
  interactive Claude Code session (a conversation in Claude Code, as
  opposed to a run without one):

  ```
  /plugin marketplace add anthropics/skills
  /plugin install document-skills@anthropic-agent-skills
  ```

- **The command-line tool of a second engine**, for a research on two
  model families (see [Research a topic](../use/research-a-topic.md)).
  Today this is `agy`, the row `antigravity`, at version 1.1.1 or
  newer. It must be on PATH and signed in once in its own tool. The
  forge carries no key and no account for it.

What each script needs, with its options, is listed in
[Scripts](../reference/scripts.md).

## What you have afterwards

You have git, Python as `python`, a signed-in Claude Code and a clone of
the engine, with Claude Code started from its root. You may also have
some optional tools. The next step is the first run,
[Set up the forge](setup.md).

## If something goes wrong

- A script stops with "The engine is not the top of a git repository
  (clone it, do not copy it)." The engine was copied, not cloned.
  Clone it again from its public home.
- A hook fails although `python3` works in your terminal. `python` is
  only a shell alias, which the hooks do not see. Install the package
  or make the symlink of step 2.
- The forge's rules do not seem to apply. Claude Code was started from
  another folder. Quit it and start `claude` from the engine root.
- A research on a second engine refuses to run. The script refuses
  `agy` below version 1.1.1; update the tool. It also needs `agy` on
  PATH and signed in.

## A worked example

One newcomer's sequence on Linux, with `<folder>` as a placeholder for
the folder the engine goes into:

```
git --version
python --version
curl -fsSL https://claude.ai/install.sh | bash
claude
git clone https://github.com/pche-broken-artist/forge-of-thought <folder>
cd <folder>
claude
```

The first `claude` signs you in; the second starts Claude Code from the
engine root. From there the first setup follows.

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

Generated on 2026-11-01 for version 6.4 from the files the front-matter
names; never edited by hand.
