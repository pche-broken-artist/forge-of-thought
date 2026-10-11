---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: d484dfc34133e3ee
inputs:
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Persistence (git)
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/forge_repos.py
  - scripts/doc2md.py
  - scripts/forge_tools.py
---

# Install what the forge needs

Forge of Thought is a workshop where an idea is shaped into a chain
of versioned documents, with Claude as the one doing the shaping
under the principal's authority (the principal is the person whose
thinking is forged). Before it runs, a few things must be on your
machine, in a particular order. This page says what they are, how
you get each one and what you see when it is in place. It is for
you, the user installing the forge for the first time; what you are
installing is said in one paragraph in [What Forge of Thought
is](what-it-is.md).

## When to use it

Use this page once, on a machine that has never run the forge: a
new computer, or a computer where the engine (the repository that
holds the rules, the commands and the scripts) has not been cloned
yet. Everything that is per person rather than per machine comes
after, on the first run, and is the next page's:
[Set up the forge](setup.md).

## What you do

Four things are required, in this order: git; Python 3.8 or newer,
reachable as a real executable named `python`; Claude Code with a
paid Claude subscription; the engine, cloned from its public home.
Three more are optional and come last, each only for the command
that uses it. The one line that gets the engine onto your machine:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

## What happens

### 1. Install git

The engine is one git repository with a remote, and every project
you make in it is a repository of its own. Git is needed before
anything else: the clone in step 4 is a git operation, and the
forge's own git scripts stop at once when git is missing. Install
git in the way your platform does it. The forge does not care which
version.

You should now see `git --version` answer with a version line.

### 2. Install Python 3.8 or newer, as `python`

The scripts of the forge are Python, run as
`python scripts/<name>.py`. So is the per-prompt hook: a small
script that Claude Code runs at every prompt you type, to repeat the
walkthrough rule (the forge's way of working a list one item per
message) and three lines of conduct into Claude's context. The
scripts have one prerequisite: an executable named `python` on
PATH. A system that has only `python3` gives it that name.

The name matters more than it looks. Claude Code starts the hook
without a shell: `.claude/settings.json` names the command `python`
and hands it the script's path as an argument, in exec form. A
shell alias for `python` is therefore never seen by the hook, and
only a real executable or a symlink does. The remedies the forge
names:

- on Debian or Ubuntu, the package `python-is-python3`;
- elsewhere on Linux and on macOS, a symlink:
  `ln -s "$(command -v python3)" /usr/local/bin/python`.

The scripts are written to run unchanged on Linux and macOS, with
nothing Windows-only in them.

You should now see `python --version` answer with 3.8 or newer,
from any directory, in a fresh shell.

### 3. Install Claude Code and sign in

Claude is the machine side of the forge, and it runs in Claude
Code. Install it with the command the forge gives for your
platform:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS or Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- anywhere with npm: `npm install -g @anthropic-ai/claude-code`

A paid Claude subscription is required. On the first run Claude
Code asks you to sign in; usage draws from the same pool as Claude
chat.

You should now see `claude` start in a terminal and, the first
time, ask you to sign in.

### 4. Clone the engine from its public home

The engine's public home is
https://github.com/pche-broken-artist/forge-of-thought. It is the
address a clone points to and the address a project's README points
back to. Clone it:

```
git clone https://github.com/pche-broken-artist/forge-of-thought
```

The forge is cloned, not copied. Do not download the files as an
archive and unpack them: the save script refuses an engine that is
not a git repository, with the message "The engine is not a git
repository (clone it, do not copy it)." The scripts in `scripts/`
are the only door to git in the forge, and they find the engine
root as the parent of their own directory, so the clone may lie
wherever you keep your repositories.

You should now see a directory `forge-of-thought` with `CLAUDE.md`,
`scripts/` and `.claude/` inside it, and
`python scripts/forge-status.py`, run from that directory, report
the state of the engine instead of an error.

### 5. Start `claude` from the engine root

Always start `claude` in the engine root, the directory that holds
`CLAUDE.md`. That is where Claude Code loads `CLAUDE.md`, the rules
of the forge, and `CLAUDE.local.md`, the instance facts (who the
principal is and what language the conversation runs in), which the
first setup creates. Started elsewhere, Claude knows nothing of the
forge. The per-prompt hook, by contrast, is independent of the
working directory: Claude Code hands it its own path through the
`${CLAUDE_PROJECT_DIR}` placeholder.

You should now see Claude Code open in the engine root; the first
setup, on the next page, is where you see Claude answer as the
forge.

### 6. The optional tools, last

Three commands reach for an external tool. Each tool is resolved
from PATH when the command runs and is installed by no script of
the forge: you install it yourself, one-off, and only when you need
the command. The git scripts need nothing beyond git.

- **markitdown**, for `/ingest`: the conversion of a Word,
  PowerPoint, PDF or Excel document to a Markdown extract is done
  exclusively by markitdown, through `scripts/doc2md.py`. Install
  it with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`, then
  reopen the shell. You should now see
  `python scripts/doc2md.py --list-tools` print `markitdown  OK`
  followed by the path it found.
- **pandoc**, for `/render`: the plain Word and PowerPoint files a
  render makes beside its Markdown, through `scripts/md2docx.py`
  and `scripts/md2pptx.py`, are made by pandoc. Install it from
  pandoc's own install page, by the way your platform does it (on
  Windows `winget install JohnMacFarlane.Pandoc`, on macOS
  `brew install pandoc`, on Linux your package manager). You should
  now see `pandoc --version` answer with a version line.
- **the document-skills plugin**, for `/publish`: the designed file
  is made by Claude Code with the official document skill of the
  format, `pptx` or `docx`. The skill may already be there under the
  name `anthropic-skills:<format>`, where Claude Code brings it. If
  it is not, install the plugin once, from an interactive Claude
  Code session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`. You
  should now see the skill under the name
  `document-skills:<format>`.

## What you have afterwards

A machine with git, `python` and Claude Code on PATH, a clone of
the engine with its `.git` directory, and, where you want them, the
tools of `/ingest`, `/render` and `/publish`. What you do not yet
have is an instance: no `CLAUDE.local.md`, no principal named, no
model chosen. That is the first run, `/setup`, on
[Set up the forge](setup.md). Every script, with what it needs and
its options, is listed in [Scripts](../reference/scripts.md); the
words of the forge are in the [Glossary](../reference/glossary.md).

## If something goes wrong

The messages below are the ones the forge's own scripts print;
anything else comes from the tool itself.

- `ERROR: git is not installed.` A git script of the forge found no
  `git` on PATH. Go back to step 1, then open a fresh shell.
- `ERROR: The engine is not a git repository (clone it, do not copy
  it).` The engine directory has no `.git`: it was copied or
  unpacked. Remove it and clone it as step 4 says.
- The hook does not run, or Claude Code reports that it could not
  start `python`. There is no executable named `python` on PATH, or
  only a shell alias. Step 2 gives the remedy; an alias is not
  enough because the hook is started without a shell.
- `markitdown  --   not found on PATH`, from
  `python scripts/doc2md.py --list-tools`, or
  `ERROR: markitdown not found.` when `/ingest` converts. Install
  markitdown with the pip line of step 6, then reopen the shell, or
  pass `--markitdown-path <exe>` to the script.
- `ERROR: claude CLI not found on PATH - the claude engine runs on
  headless Claude Code.` `/publish` ran without the `claude`
  executable reachable on PATH. Step 3 installs it.

## A worked example

One machine, one afternoon, as typed. `<workspace>` stands for the
directory where you keep your repositories.

```
git --version
python --version
claude                       # first run: sign in, then leave it
cd <workspace>
git clone https://github.com/pche-broken-artist/forge-of-thought
cd forge-of-thought
python scripts/forge-status.py
pip install "markitdown[docx,pptx,pdf,xlsx,xls]"
python scripts/doc2md.py --list-tools
claude
```

Inside Claude Code, in the engine root, the first thing you type is
`/setup`. Everything from here on is the next page's.

## See also

- [What Forge of Thought is](what-it-is.md): what you are
  installing, in one paragraph.
- [Set up the forge](setup.md): the first run, `/setup`, which
  fills the instance facts and sets the model.
- [Scripts](../reference/scripts.md): every script with what it
  needs and its options.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
