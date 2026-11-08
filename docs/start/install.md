---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: d3fc2f8adcb4716a
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.1880
  - projects/forge/10-intent.md#POS.1930
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

Installing the forge is four things on your machine (git, Python,
Claude Code and a clone of the engine) and one habit (starting
Claude Code from the engine root). This page is for you if you are
new to Forge of Thought and want it running on your own machine: it
gives the steps in the order you need them, each with the sign that
it worked, and then the optional tools that single commands need.
What you are installing is said in one paragraph on
[What Forge of Thought is](what-it-is.md). The engine is the forge's
own repository, the one you clone; your projects live inside it as
repositories of their own.

## When to use it

Once per machine, before the first run of the forge. The forge runs
beyond Windows. The scripts are written to run unchanged on Linux
and macOS. The engine's tests run in CI on Linux and Windows at every
push; the git scripts, the ledger (the state report of a project,
made at read time), the light check and the git hook's judgement are
among them. The conversions are tested only for their failure without
the tool. The per-prompt hook is a writing rule until a run says
otherwise. Nothing has run on macOS; there the whole set is the
writing rule alone.

## The command

The one line of this page that the forge itself asks for is the
clone of the engine from its public home:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

Everything before it is installing a tool; everything after it is
starting Claude Code in the right place.

## What happens

1. **Install git.** Any git serves the scripts, which need nothing
   beyond git. Version 2.36 or newer is needed where `/setup` writes
   the identity per host, because that stanza uses a form of
   `includeIf` older versions do not know. You should now see
   `git --version` answer with 2.36 or a newer number.

2. **Install Python 3.8 or newer, on PATH as a real executable named
   `python`.** The scripts and the two hooks are Python. A hook is a
   script Claude Code runs on its own at a fixed moment: one at every
   prompt, one before every shell command. Both hooks are started as
   `python` directly, without a shell, so a shell alias does not
   reach them. A system that has only `python3` gives it that name:
   on Debian or Ubuntu the package `python-is-python3`; elsewhere on
   Linux and on macOS a symlink,
   `ln -s "$(command -v python3)" /usr/local/bin/python`. You should
   now see `python --version` answer with 3.8 or a newer number.

3. **Install Claude Code, with a paid Claude subscription.** The
   install lines:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS and Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - or, on any platform: `npm install -g @anthropic-ai/claude-code`

   Sign in on first run; usage draws from the same pool as Claude
   chat. You should now see Claude Code open its prompt after the
   sign-in.

4. **Clone the engine.** Run the clone line above in the folder where
   you keep your repositories. Never copy the engine: the git scripts
   refuse an engine that is not a git repository. You should now see
   a folder `forge-of-thought` with `CLAUDE.md` in its root.

5. **Start `claude` from the engine root, always.** Change into
   `forge-of-thought` and run `claude` there, so that `CLAUDE.md`
   loads, and later `CLAUDE.local.md`, the instance file `/setup`
   makes. You should now see Claude Code running with the engine
   root as its working directory.

6. **Add the optional tools, each when a command needs it.** Every
   tool is resolved from PATH; no script of the forge installs
   anything. The list, with the command each serves:
   - markitdown, for the conversions of `/ingest` (Word, PowerPoint,
     PDF, Excel to Markdown):
     `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
   - pandoc, for the plain Word and PowerPoint files of `/render`:
     install it yourself, one-off, from pandoc's own site or your
     package manager.
   - Pillow and ffmpeg, for the video format of a screenplay render
     (a render is an output generated from a recipe, never edited by
     hand; the [Glossary](../reference/glossary.md) has every term of
     the forge in one line): `pip install pillow`, and ffmpeg on PATH.
     The player format needs nothing beyond Python.
   - the document-skills plugin, for `/publish`, unless Claude Code
     already brings the docx and pptx skills: from an interactive
     Claude Code session, `/plugin marketplace add anthropics/skills`,
     then `/plugin install document-skills@anthropic-agent-skills`.
   - the command-line tool of a second engine, for a research on two
     model families ([Research a topic](../use/research-a-topic.md)):
     today `agy`, the row `antigravity`, at version 1.1.1 or newer.
     The forge asks only that it is on PATH and signed in once. How
     it is installed and signed in is the tool's own documentation's
     business; the forge carries no key and no account.
   - GitHub's command-line tool `gh`, on PATH and logged in, for the
     line that reports what waits on GitHub outside git (open pull
     requests and unanswered discussions), read by
     `scripts/forge-status.py --remote`. Without it that line says
     it could not read, and why.
   - pytest, for the engine's tests, which a contributor runs with
     `/test` ([Run the tests](../use/run-the-tests.md)) and a user
     never runs: `python -m pip install pytest`, the one thing a
     contributor installs beyond `python`.

   You should now see each command run without its script stopping
   to name the tool as missing; for markitdown,
   `python scripts/doc2md.py --list-tools` checks that it is
   reachable and exits.

What each script needs and its options is listed on
[Scripts](../reference/scripts.md).

## What you have afterwards

A machine on which the forge runs: git, `python` and `claude` on
PATH, the engine cloned, and the habit of starting Claude Code from
its root. The forge itself is not yet prepared: the instance file,
the git configuration the scripts rely on and the rest of the first
run are the next page, [Set up the forge](setup.md), by `/setup`.

## If something goes wrong

- The hooks do not start, or Claude Code reports that it could not
  run `python`: `python` is an alias, not an executable, or it is
  not on PATH. Give the real executable that name, as step 2 says.
- A git script stops and says that the engine is not the top of a
  git repository: the engine was copied, not cloned. Clone it as
  step 4 says.
- A conversion stops and names markitdown, pandoc or ffmpeg as
  missing, with how it is installed: install that tool as step 6
  says, then run the command again.
- `scripts/forge-engine.py` refuses with the reason on its error
  output: the engine's tool is missing from PATH, or its version is
  below the floor. Install or update the tool as its own
  documentation says.
- The line on what waits on GitHub says it could not read: `gh` is
  missing, not logged in, the origin is not GitHub, or there is no
  network. The line says which; the rest of the report stands.
- `/test` says the tests did not run (`No module named pytest`):
  install pytest with `python -m pip install pytest`.

## A worked example

One machine, prepared from nothing, as typed in a terminal on macOS
or Linux; on Windows the install line of Claude Code is the Windows
one of step 3.

```
git --version
python --version
curl -fsSL https://claude.ai/install.sh | bash
cd <the folder where you keep your repositories>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

The first two lines show 2.36 or newer and 3.8 or newer. The third
installs Claude Code; its first run asks you to sign in. The clone
makes the folder `forge-of-thought`; `claude` started inside it is
the forge. Inside Claude Code the next thing you type is `/setup`.
The optional tools come later, each when a command first needs it:

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
pip install pillow
python -m pip install pytest
```

## See also

- [What Forge of Thought is](what-it-is.md): what you are
  installing, in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Run the tests](../use/run-the-tests.md): the tests a contributor
  runs with `/test`.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
