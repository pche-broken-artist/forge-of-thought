---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 76fceb43249b20d2
inputs:
  - projects/forge/recipes/readme.md#Instructions
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/forge/states/brief.md#Course
  - .claude/skills/forge/states/intent.md#Course
  - .claude/skills/save/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - CLAUDE.md#Persistence (git)
---

# Get a first result

A first result is a project with an approved brief and a saved
first intent, reached in one sitting. This page is for you, the
person whose thinking is to be forged (the principal, in the forge's
word), on your first sitting after [Set up the forge](setup.md) has
run. It walks the shortest path from nothing to a saved intent, and
it names the one act along that path that happens outside Claude,
in your own terminal. The same sitting, on real work, is shown in
the teaching videos at
https://pche-broken-artist.github.io/forge-of-thought/videos/.

## When to use it

Use this page once, when the forge is set up and no project of
yours exists yet. You have an idea, a few sentences or a page of
notes, and you want to see the forge turn it into a first intent
and keep it in git before the sitting ends. Every later job has a
page of its own under `use/`; this page only strings the first ones
together.

The page covers two doors into a project:

- a new project, made from nothing by `/new-project`;
- a project you already have in a git repository, brought in by
  `/import-project`.

The first door is the main matter of the page. The second is one
short section at the end.

## What you do

Start `claude` from the engine root, the directory that holds
`CLAUDE.md`, as setup told you. Then, in Claude, with `my-idea` as
your own slug:

```
/new-project my-idea
```

When Claude asks for the brief, paste it and say it is finished.
Then:

```
/forge intent
```

After the intent is written, in your own terminal, not in Claude,
at the engine root:

```
git -C projects/my-idea init -b main
```

Then, back in Claude:

```
/save my-idea
```

Four acts, each a step of its own. The sections below say what each
one does and what you see when it has worked.

## What happens

### 1. Scaffold the project

`/new-project my-idea` creates `projects/my-idea/` and the files a
project starts with. The slug must be lowercase, with hyphens and
no spaces. Claude asks two things where your words leave them open:

- the kind of the project, a thought project (the default, the
  chain of documents) or a library (material shared across projects,
  with no chain; a slug with the prefix `lib-` is taken as one);
- the language of the project's documents, English unless you name
  another.

The command writes files only. It never touches git: a project is a
repository of its own, which the engine does not track, and
initialising it is your one-off act (step 4). The project's folders
for sources, research, reviews, challenges and threads are made
empty, with a catalogue file in sources and research; the project
file, the decisions file and the two recipes of the project's README
and release notes are made from templates. The intent and every
layer below it are not created here: each is born from its own first
`/forge`.

You should now see `projects/my-idea/` with `project.md`,
`decisions.md`, `recipes/`, `sources/00-INDEX.md` and
`research/00-INDEX.md` in it, and Claude asking you to paste or
dictate the brief.

### 2. Paste the brief and approve it

The brief is your idea put together, in your own words. Pasted
whole, it is stored verbatim as `00-brief.md`, with a history
companion `00-brief.history.md` beside it, and Claude asks whether
the text is finished. Say that it is, and the brief is approved at
once; approval happens only on your explicit word. A brief that is
not finished stays a draft and is worked on from where it stops.

A brief of five lines is enough for a first sitting. A generic one,
taken from no project:

```
We spend two days each month assembling the same status report by
hand from four systems. I want one place where the numbers land and
the report is generated from it. The teams that own the systems
must keep their tools; only the reporting changes. A first version
should exist within a quarter, for one department, before anything
is promised to the others.
```

After the brief, Claude makes the ledger once (the ledger is the
project's state report, built from its documents by a script and
never kept in git), proposes `/forge intent` as the next step and
reminds you that the project is not under git until you initialise
its repository. That reminder states a property of the project, not
an error: a project "not under git" is a fact the forge lives with,
and nothing is lost by it until you want the work saved.

You should now see `00-brief.md` and `00-brief.history.md` in
`projects/my-idea/`, Claude naming the brief's state as approved and
proposing `/forge intent`.

### 3. Forge the first intent

`/forge intent` reads the approved brief and mines it into the
first intent, the document that holds what you actually hold true
and what you have rejected. There is no intent yet, so the brief is
consolidated into the first one. Claude works it as an interview,
one question per message, one theme at a time; the questions bring
out what the brief says and what it leaves open. The answers are
carried in the conversation and reflected back to you. The intent is
written once, at the end of the round, when you say the word
`write`. Claude ends by naming what changed and what stays open.
The full job, with its later rounds, is [Forge the
intent](../use/forge-the-intent.md).

You should now see `10-intent.md` and `10-intent.history.md` in
`projects/my-idea/`, and Claude's closing message naming what the
intent now holds and which matters stay open.

### 4. Put the project under git, in your own terminal

The project's repository is yours to create. Claude writes nothing
into git itself: the forge's scripts are its one door to a write of
git, and the first initialisation of a repository is not among what
they do. So you open your own terminal at the engine root and run:

```
git -C projects/my-idea init -b main
```

A remote is optional: add one with git's own commands if you want
the project pushed somewhere. The commit identity is git's, resolved
per host from your own configuration, which setup offered to write;
the forge sets none.

You should now see git's own message that an empty repository was
initialised in `projects/my-idea/.git/`.

### 5. Save

`/save my-idea` saves the project's repository. Claude first reads
the state of the engine and every project through
`scripts/forge-status.py`. It then runs the light check, a
mechanical check of the project's conventions, on the repository in
scope and settles its report with you; a save never waits on a
finding you have not asked to fix. It drafts a one-line English
commit message from the records the round wrote into the touched
histories and proposes it; you confirm or adjust the wording. Only
then does it run `scripts/forge-save.py`, which commits and pushes
on whatever branch is checked out and prints the commit's file
summary. No render is made at a save; the README and release notes
are the release's. What a save does and asks in full is [Save your
work](../use/save-your-work.md).

You should now see the script's summary of the files committed and,
where a remote exists, pushed.

## What you have afterwards

In `projects/my-idea/`:

- an approved brief, `00-brief.md`, with its history companion;
- a first intent, `10-intent.md`, with its history companion;
- the project file, the decisions file, the two recipes and the
  empty resource folders with their catalogues;
- a ledger, `ledger.md`, built by the script and kept out of git;
- a git repository on the branch `main`, with one commit holding all
  of the above, pushed where you gave it a remote.

The next sitting starts with `/forge intent` again, on the matters
the first round left open, or with whatever the full job of
[Start a project](../use/start-a-project.md) names as the next step.

## If something goes wrong

- **The slug is refused.** A slug is lowercase, with hyphens and no
  spaces. Choose one that fits.
- **`projects/my-idea/` already exists.** `/new-project` stops and
  reports; it never overwrites. Choose another slug, or work in the
  existing project.
- **The brief was not approved.** Approval happens only on your
  explicit word that the text is finished. Say so, or leave the
  draft and finish it in a later round.
- **The save commits nothing and names its cause.** Two causes are
  known to the owners:
  - no repository: the project is not under git, which is a
    property, not a defect; run step 4 and save again;
  - no git identity for the host: git has no name and e-mail to
    sign commits on this machine, and the login that cloned the
    repository is a different thing; the save commits nothing until
    git resolves one. The ways out are the identity step of
    `/setup`; the forge writes no identity itself.
- **The light check finds something.** The findings are put to you
  one at a time; the save does not wait on a finding you have not
  asked to fix.
- **The ledger script fails or names files it could not parse.**
  The check reads the ledger as it lies, the save goes on and says
  so: a save is what does not lose work.
- **The save leaves a conflict standing.** This happens only where
  a remote already holds work the clone does not. The conflict is
  not aborted: Claude lays both sides out, you decide, and the
  finishing commands of git run on your yes; then save again.

## The other door: a project you already have

Where the project already lives in a git repository, bring it in
with its URL:

```
/import-project <git-url>
```

Claude runs `scripts/forge-clone.py` on your word; the project lands
in `projects/<repository name>`, the name taken from the URL, and
the command stops if that directory already exists. The script
reports the commit identity git resolves on this host, or says that
it resolves none. Nothing is written into the imported project.
Then select it by naming it, since the engine does not track
projects and cannot guess which one you mean:

```
/forge <project-slug>
```

The slug is the repository's name. The full job is [Bring in an
existing project](../use/bring-in-an-existing-project.md).

## See also

- [Set up the forge](setup.md): the first run that comes before.
- [Start a project](../use/start-a-project.md): the full job of
  starting a project.
- [Bring in an existing project](../use/bring-in-an-existing-project.md):
  a project you already have, cloned into `projects/`.
- [Forge the intent](../use/forge-the-intent.md): the full job of
  iterating the intent.
- [Save your work](../use/save-your-work.md): what a save does and
  asks.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
