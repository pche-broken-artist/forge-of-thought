---
generated: 2026-10-10
made: derived
inputs-hash: a7cc78db700d41da
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

This page walks you, as a user of the forge, through one sitting:
from nothing to a saved intent, in three commands and one short
conversation. It was put together from the definitions of
`/new-project`, `/forge brief`, `/forge intent`, `/save` and
`/import-project`, from the Persistence section of `CLAUDE.md` and
from the Quickstart of the README's recipe. It assumes the engine is
cloned and set up and that you start `claude` from the engine root;
how that is done is not this page's matter.

## The sitting in one glance

```
/new-project my-idea     scaffolds the files, asks for the brief
/forge intent            mines the brief into the first intent
/save                    light check, then commit and push
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: `git -C projects/my-idea
init -b main` (then a remote if you want one) is your one-off act,
and a project "not under git" until then is a fact, not an error.

## 1. Scaffold the project

Run `/new-project my-idea`. The slug is lowercase with hyphens, no
spaces; if `projects/my-idea/` already exists the command stops and
says so, never overwriting.

The command creates files only and never touches git. You see a
new folder `projects/my-idea/` with the ledger, the decisions file,
empty `sources/`, `research/`, `reviews/` and `challenges/`
directories with their two indexes, and the two render recipes
(README and release notes) with their history companions. Claude
may ask two things on the way: the kind of the project, a thought
project by default or a library when the slug begins with `lib-`
or your words say so, and the language of the project's artefacts,
English unless you name another. A library gets its ledger, indexes
and README recipe only, and the command ends by proposing
`/ingest`; the rest of this page is about a thought project.

The intent is not created here: it is born from its own first
`/forge intent`.

## 2. Give the brief

At the end of the scaffold Claude asks you to paste or dictate the
brief, your own text of what you want and why, rough on purpose.
What happens next depends on how the text arrives:

- Pasted whole: it is stored verbatim and Claude asks whether it is
  finished. Say yes and the brief is approved at once.
- Begun outside and not finished: what came is stored and the
  conversation goes on from where it stops.
- Born here: you open with a rough idea and Claude works from the
  first word, verifies, proposes, draws out, and writes down what
  the two of you arrived at, reflected back before it is written.

The brief is written once per round on your confirmation and
approved only on your explicit word. The command ends by naming the
state of the brief, proposing `/forge intent` and reminding you
that the project is not under git until you initialise its
repository.

## 3. Forge the intent

Run `/forge intent`. Since there is no intent yet, Claude
consolidates the brief into the first one, through an interview:
one question per message, drawing out what you have not yet
articulated. Within a round one theme at a time; the reality check
comes last. Claude composes the wording, you the substance.

Nothing is written during the conversation. What is agreed is
carried in the conversation and written once at the round's end,
on your word `write`; before the write Claude reflects back what he
understood. The write creates `10-intent.md` as version 0.1, its
history companion `10-intent.history.md` and the project's
`threads.md`, and keeps the brief's Mined column in the ledger.
Claude ends by naming what changed and what stays open.

## 4. Save

Run `/save`. It reports the engine and each project separately,
with the branch each is on, runs the light check on every
repository in scope and settles its report with you; a save never
waits on a finding you have not asked to fix. Claude then drafts a
one-line English commit message from the records of the round and
proposes it; you confirm or adjust the wording. Only then the
script commits and pushes, and the report shows the commit's file
summary.

A project not under git with changes is named in the report and
otherwise left alone. If you want this first intent saved, do the
one-off act before `/save`: `git -C projects/my-idea init -b main`,
then a remote if you want one. The commit identity is git's,
resolved from your own configuration; the forge sets none.

## The other door: an existing project

If the project already exists as a repository, bring it in instead
of scaffolding:

```
/import-project <project url>    clones into projects/
/forge <project-slug>            selects the project and shows its state
```

The target directory is `projects/<repository name>`; the name
falls out of the URL, and if the directory already exists the
command stops. The clone runs on your word, through the forge's
script, and nothing is written into the imported project. Claude
relays what the script reports: the last commit, the origin, the
identity git resolves and whether the project carries a ledger
with a `kind:` header. Then name the project with
`/forge <project-slug>` before any work: the engine does not track
the project and cannot guess it.

## See also

- [Start a project](../use/start-a-project.md): the full job of starting a project, thought or library.
- [Forge the intent](../use/forge-the-intent.md): the full job of iterating the intent.
- [Save your work](../use/save-your-work.md): what a save does and asks.
