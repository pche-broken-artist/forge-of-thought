---
generated: 2026-10-09
made: derived
inputs-hash: 5a7a5021d3a04864
inputs:
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - CLAUDE.md
  - projects/forge/recipes/readme.md
---

# Get a first result

This page is for you if the forge is installed and set up and you
want to see, in one sitting, how an idea becomes a saved intent. It
walks the three commands of the Quickstart in order and says what
each does for you and what you see. It was put together from the
command definitions of `/new-project`, `/save` and `/import-project`,
the definitions of the brief and the intent, the Persistence section
of `CLAUDE.md` and the Quickstart of the README's recipe.

## Before you start

Start `claude` from the engine root, always: that is where the
forge's instructions load. `/setup` has run once on this machine.
The three commands below are the "Starting a new project" path of
the README's Quickstart; the sitting takes you from nothing to a
saved intent.

```
/new-project my-idea
/forge intent
/save
```

## Step 1: scaffold the project and give it your brief

Type `/new-project my-idea`. The slug is lowercase with hyphens
and no spaces; if `projects/my-idea/` already exists the command
stops and says so, it never overwrites.

What it does for you:

- It creates `projects/my-idea/` with its files: the ledger (the
  one place that holds the project's state), `decisions.md`, the
  empty `sources/`, `research/`, `reviews/` and `challenges/`
  folders with their index files, and the two recipes every
  thought project carries, for its README and its release notes.
  Files only: the command never touches git.
- It needs to know two things about the project and asks when your
  words leave them open: its kind (a thought project, the default,
  or a library) and the language its artefacts are written in
  (English unless you name another).
- It then asks you to paste or dictate the brief: your idea put
  together, what you want and why, in any shape you like. Pasted
  whole, the text is stored word for word and you are asked whether
  it is finished. Say yes and it is approved at once; say no and it
  stays a draft you go on working, by writing with Claude from where
  the text stops.
- It ends by proposing the next step, `/forge intent`, and by
  reminding you once that the project is not under git until you
  initialise its repository (Step 4 below).

What you see at the end: `projects/my-idea/00-brief.md` with its
history companion beside it, and the ledger's Briefs table with one
row, not yet mined. No intent exists yet: each layer of the chain is
born from its own first `/forge` call.

## Step 2: forge the first intent

Type `/forge intent`. Because there is no intent yet, Claude takes
the brief and consolidates it into the first one: the brief
chiselled into what you hold.

What you see:

- An interview, one question per message. Claude mines the brief
  with you, probes what contradicts, what is missing and what is
  assumed, and asks whether an idea is good and whether it is
  feasible as two separate questions. He composes the wording; the
  substance is yours.
- Nothing is written while the conversation runs. What you agree is
  carried in the conversation and reflected back to you so the write
  confirms rather than surprises. At the round's natural end Claude
  asks whether to write; the word is `write`, and you may say it at
  any moment to write what is agreed so far.
- On that word the first intent is created as version 0.1:
  `projects/my-idea/10-intent.md`, its history companion
  `10-intent.history.md`, and `threads.md`, where everything still
  open is kept. The ledger's Briefs table is updated with how far
  the brief is mined.
- Claude ends by naming what changed and what stays open. When no
  open thread blocks the next layer he names the layers that can
  follow, or offers the approval: a recommendation, never a gate.
  You decide whether to go on now or stop here.

## Step 3: save

Type `/save`. What it does for you, in order:

1. It reads the state of the engine and of every project through
   the forge's own scripts, the only door to git, and reports each
   separately with the branch it is on.
2. It runs the `light` check on every repository with changes and
   settles its report with you. A save never waits on a finding you
   have not asked to fix.
3. It drafts a one-line English commit message from the history
   records the round appended and proposes it to you; you confirm or
   adjust the wording. If you gave `-m "message"` it uses yours.
4. Only then it commits and pushes on whatever branch is checked
   out, and reports the outcome. No render is made: that is
   `/release`'s job.

If the project is not under git, the save names it in its report as
such, with its changes, and otherwise leaves it alone.

## Step 4: put the project under git, once

Each project is a git repository of its own inside `projects/`,
which the engine does not track; initialising it and adding a remote
are your one-off act, and until you do, "not under git" is a fact
about the project, not an error. The way in is one command from the
engine root, then a remote if you want one:

```
git -C projects/my-idea init -b main
```

The forge sets no commit identity: git resolves it from your own
configuration, which `/setup` offered to prepare. After that,
`/save` commits and pushes the project like any other repository.

## The other door: an existing project

If the project already lives in a git repository somewhere, the
Quickstart's second path brings it in instead of Step 1:

```
/import-project <project url>
/forge <project-slug>
```

`/import-project` requires the URL and, on your word, clones the
repository into `projects/<repository name>`; the slug is the
repository's name, and nothing is written into the project. It
reports the last commit, the origin, the commit identity git
resolves, and whether the project carries a ledger. Then select the
project by naming it, `/forge <project-slug>`, before any work: the
engine does not track projects and cannot guess which one you mean.
`/forge <slug>` shows the project's state map and the next step
from there.

## See also

- [Start a project](../use/start-a-project.md): the full job of
  starting a project, thought or library.
- [Forge the intent](../use/forge-the-intent.md): the full job of
  iterating the intent.
- [Save your work](../use/save-your-work.md): what a save does and
  asks.
