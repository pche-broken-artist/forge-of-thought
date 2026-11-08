---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 30279eae89b837ea
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
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

Forge of Thought (the engine, in short) is a set of files that Claude
Code reads: slash commands, skills, agents, hooks and scripts. What
it is and what it does for you is said on
[What Forge of Thought is](what-it-is.md). This page is for you, the
user who is about to put the forge on a machine for the first time:
it lists what must be installed before the forge runs, in the order
you need it, with the sign that each step worked. The optional tools,
needed only by some commands, come last.

## When to use it

Use this page once per machine, before the first run of `/setup`.
Nothing here is done by the forge itself: no script of the forge
installs anything, every external tool is resolved from your PATH,
and what you install is yours to install. Come back to the last
section when a command tells you that a tool it needs is missing.

## What you do

The one line that brings the forge onto the machine is the clone of
the engine from its public home:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

Everything before it prepares the machine for the clone; everything
after it is optional until a command asks for it.

## What happens

### 1. Install git

The forge keeps the engine and every project in git, and its git
scripts need nothing beyond git. Install git with your system's own
means. Version 2.36 or newer is needed if `/setup` is to write the
commit identity per host for you. The reason is a git feature of that
version, `hasconfig` in `includeIf`, which the identity stanzas use.
How the identity per host works is the setup page's
([Set up the forge](setup.md)).

You should now see `git --version` answer with a version of 2.36 or
higher.

### 2. Install Python 3.8 or newer, as `python`

The scripts of the forge and its two hooks are Python. Python 3.8 or
newer must be on PATH as a real executable named `python`. A shell
alias is not enough. The reason is the way the hooks are started:
`.claude/settings.json` starts both of them as `python` with the
script's path as argument, without a shell, so that an alias defined
in your shell never reaches them. The two hooks are:

- the per-prompt hook (`scripts/hook-walkthrough.py`), which repeats
  the rule of the walkthrough, the method by which a list is settled
  one item per message, at every prompt;
- the git hook (`scripts/hook-git.py`), which judges every git
  command Claude sends and holds the wall between reading git and
  writing it.

Each of them needs Python 3.8 or newer on PATH as `python`, and
nothing else.

Where your system has only `python3`, give it the name `python`:

- on Debian or Ubuntu, the package `python-is-python3`;
- elsewhere on Linux and on macOS, a symlink:
  `ln -s "$(command -v python3)" /usr/local/bin/python`.

You should now see `python --version` answer with `Python 3.8` or a
newer version, from any directory.

### 3. Install Claude Code and sign in

The forge runs in Claude Code, Anthropic's agent for the command
line, and needs a paid Claude subscription. Install Claude Code by
one of the three lines:

- on Windows: `irm https://claude.ai/install.ps1 | iex`
- on macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or, with npm: `npm install -g @anthropic-ai/claude-code`

Sign in on the first run. Usage draws from the same pool as Claude
chat.

You should now see `claude` start and, after the sign-in, show its
prompt.

### 4. Clone the engine, never copy it

Clone the engine from its public home into the place where you keep
your repositories:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

The forge is cloned, not copied. The reason is in the scripts: every
git script asks git whether the engine's directory is the top of a
repository and refuses an engine that is not, with the message
`The engine is not the top of a git repository (clone it, do not copy
it).` A copy of the files without the `.git` directory would therefore
never save, pull or branch.

The engine is all a user clones. The forge's own project,
`projects/forge`, is a repository of its own beside the engine, needed
by no user and cloned beside the engine only by whoever develops it;
how is said on [Make a change to the forge](../extend/how-a-change-is-made.md).
A fresh clone has the `projects/` directory with one `README.md` in
it, a line on what belongs there, and nothing else.

You should now see a directory `forge-of-thought` with `CLAUDE.md`,
`scripts/`, `templates/`, `.claude/` and `projects/README.md` in it.

### 5. Start `claude` from the engine root, always

Always start `claude` from the engine root, the directory that holds
`CLAUDE.md`. The reason is that Claude Code loads `CLAUDE.md` and
`CLAUDE.local.md` from the directory it is started in; started
elsewhere, the forge's rules do not load and its commands are not
there.

You should now see the forge's slash commands, `/setup` among them,
offered when you type `/` at the prompt.

### Platforms

The scripts are the only platform-bound layer of the forge and are
written to run unchanged on Linux and macOS. The engine's tests run
in CI on Linux and Windows at every push, the git scripts, the ledger
(the project's state report, made at read time), the light check and
the git hook's judgement among them. The conversions are tested only
for their failure without the tool. The per-prompt hook is a writing
rule until a run says otherwise. Nothing has run on macOS; there the
whole set is the writing rule alone.

### 6. The optional tools

Each of these is needed by one command only, is resolved from PATH,
and is installed by no script of the forge. Install what you will
use. Every script with what it needs is listed on
[Scripts](../reference/scripts.md).

- **markitdown**, for the conversions of `/ingest` (a Word,
  PowerPoint, PDF or Excel document to Markdown, through
  `scripts/doc2md.py`):
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  You should now see `python scripts/doc2md.py --list-tools` report
  that markitdown is reachable.
- **pandoc**, for the plain Word and PowerPoint files that `/render`
  makes where a recipe names a format: install it once from its own
  site, by the means of your system. You should now see `pandoc` found
  on PATH.
- **Pillow and ffmpeg**, for the video format of a screenplay render:
  `pip install pillow`, and ffmpeg on PATH from its own site. The
  player format needs nothing beyond Python. Fonts are taken from the
  system where they exist and from Pillow's built-in font otherwise.
- **The document-skills plugin**, for `/publish`, which makes the
  designed Word or PowerPoint file through a model: needed unless
  your Claude Code already brings the docx and pptx skills. Where it
  does not, install the plugin once, from an interactive Claude Code
  session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`.
- **The command-line tool of a second engine**, for a research on two
  model families ([Research a topic](../use/research-a-topic.md)):
  today the tool `agy`, the row `antigravity` of
  `scripts/forge-engine.py`, at version 1.1.1 or newer. The forge asks
  only that the tool is on PATH and signed in once. How it is
  installed and signed in is the tool's own documentation's; the
  forge carries no key and no account. You should now see `agy` found
  on PATH; the script refuses a version below the floor and says so.
- **GitHub's command-line tool `gh`**, on PATH and logged in, for the
  line of the state map of a project (`/forge`) that says what waits
  on GitHub outside git: the open pull requests and the unanswered
  discussions. Without it that line says it could not read, and why.
  Nothing else stops.
- **pytest**, for the engine's tests ([Run the tests](../use/run-the-tests.md)):
  `python -m pip install pytest`. This is the one thing a contributor
  installs beyond `python`. A user never runs the tests and installs
  nothing for them.

## What you have afterwards

A clone of the engine on your machine, git and `python` on PATH,
Claude Code signed in, and `claude` started from the engine root. The
forge is not yet set up: the instance file `CLAUDE.local.md`, the
git configuration and the rest of the first run are made by `/setup`,
on [Set up the forge](setup.md). Every term used here is explained in
one line in the [Glossary](../reference/glossary.md).

## If something goes wrong

- `ERROR: git is not installed.` A git script of the forge did not
  find git on PATH. Install git (step 1).
- `ERROR: The engine is not the top of a git repository (clone it, do
  not copy it).` The engine was copied, or its `.git` directory is
  gone. Clone it anew (step 4).
- The forge's rules seem not to hold, or the verdict line of the
  walkthrough never appears. Either `claude` was started outside the
  engine root (step 5), or the hooks do not run because `python` is
  not a real executable of that name on PATH (step 2).
- `No module named pytest` from `/test`. The tests did not run.
  Install pytest with `python -m pip install pytest`; a user does not
  need to.
- `scripts/doc2md.py` reports that markitdown is not reachable.
  Install it with the pip line above, or name the executable with
  `--markitdown-path`.
- `scripts/forge-engine.py` exits with a refusal on stderr: the tool
  is missing from PATH, or its version is below the floor of its row.
  Install or update the tool by its own documentation and sign in
  once.
- The `github:` line under `remote:` says it could not read. One of
  four reasons stands in the line: no `gh`, an origin that is not
  GitHub, no login, no network. The rest of the report is unaffected.

## A worked example

The sequence as typed on a machine running macOS or Linux, with
placeholders where your own choice stands:

```
git --version
python --version
curl -fsSL https://claude.ai/install.sh | bash
cd <where-you-keep-your-repositories>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
claude
```

On Windows the third line is `irm https://claude.ai/install.ps1 |
iex` and the rest is the same. In Claude Code you then type `/setup`,
the first run, as [Set up the forge](setup.md) describes. Later, when
you need them:

```
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
pip install pillow
python -m pip install pytest
```

## See also

- [What Forge of Thought is](what-it-is.md): what you are installing,
  in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`.
- [Research a topic](../use/research-a-topic.md): the research that
  uses a second engine.
- [Run the tests](../use/run-the-tests.md): the tests a contributor
  runs with `/test`.
- [Make a change to the forge](../extend/how-a-change-is-made.md): how
  whoever develops the engine clones the forge's own project beside
  it and sends a change.
- [Scripts](../reference/scripts.md): every script with what it needs
  and its options.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
