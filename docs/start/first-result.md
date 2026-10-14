---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 9346e8466075f3ed
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

A first result is a project of your own with an approved brief and
a first intent, saved in git, reached in one sitting. This page is
for you, the user who has set up the forge once and now wants to see
it work on an idea of yours. It walks the sitting step by step: what
you type, what Claude does, what you see, and the one act you do
yourself outside Claude. Where a step is a whole job of its own, the
page of that job says more; this page says only what the first
sitting needs.

## When to use it

Use this page once, right after the first run of the forge on your
machine (see [Set up the forge](setup.md)), with an idea in your
head and Claude Code started from the engine root. You are the
principal here: the person whose thinking is forged, who supplies
the idea and the answers and decides what is written. The sitting
needs nothing prepared beyond the idea; the brief can be as rough
as five lines.

If you already have a project in a git repository, the end of this
page shows the other door: bring it in and name it, then work.

## What you do

Starting a new project, in order:

```
/new-project my-idea
/forge intent
```

Then, in your own terminal at the engine root, the one act Claude is
not allowed to run:

```
git -C projects/my-idea init -b main
```

Then, back in Claude Code:

```
/save
```

Bringing an existing project instead:

```
/import-project <project url>
/forge <project-slug>
```

`my-idea` stands for the slug of your project: lowercase, hyphens,
no spaces. Every act outside Claude is a step of its own below;
nothing outside Claude happens as a side effect of a command.

## What happens

1. **Scaffold the project.** Type `/new-project my-idea`. Claude
   creates the files of a project under `projects/my-idea/`: the
   folders for sources, research, reviews and challenges, a ledger
   (the project's one file of state), a decisions file, the recipes
   of the project's README and release notes with their history
   companions, and the two resource indexes. It creates no git
   repository: a project is a repository of its own that the engine
   does not track, and initialising it is yours to do, in step 4.
   Claude asks on the way only for what your words leave open: the
   language of the project's artefacts (English unless you name
   another) and the kind of project. Then it asks for the brief. You
   should now see Claude report the files it created and ask you to
   paste or dictate the brief.

2. **Give the brief.** The brief is your thought written down, in
   whatever words it arrived. Paste it whole. A generic sample, five
   lines you may use as it stands to see the sitting through:

   ```
   A shared reading list for the team.
   We recommend books and articles to each other in chat and they get lost.
   I want one place where anyone adds a recommendation with a line on why.
   Adding one should take a minute, and nothing should need maintaining.
   Not a library system: no lending, no reviews, no ratings.
   ```

   Claude stores the text verbatim as `00-brief.md`, with its history
   companion and its row in the ledger, and asks whether the text is
   finished. Say that it is: the brief is approved at once, on your
   word and only on your word. Had you said it is not, Claude would
   work on from where the text stops, one round at a time, and write
   once per round on your confirmation. You should now see Claude
   name the brief's state, propose `/forge intent`, and remind you
   once that the project is not under git until you initialise its
   repository.

3. **Forge the intent.** Type `/forge intent`. The intent is the
   artefact Claude mines from the brief. With no intent yet, Claude
   reads the brief and consolidates it into the first one through an
   interview: one question per message, one theme at a time, until
   the brief is mined whole. Answer as you can; what you do not know
   stays open. Nothing is written while you talk. Before writing,
   Claude reflects back what it understood; when you say `write`, it
   writes the intent once for the whole round, as `10-intent.md`
   with its history companion, and keeps the brief's Mined column in
   the ledger. Claude ends by naming what changed and what stays
   open; where the intent is complete enough, it names the layers
   that can follow, as a recommendation, never a gate. You should
   now see `10-intent.md` in `projects/my-idea/` and Claude's summary
   of what it wrote and what is still open. The full job, with
   everything an intent round can take in, is
   [Forge the intent](../use/forge-the-intent.md).

4. **Put the project under git.** In your own terminal, at the engine
   root, run `git -C projects/my-idea init -b main`. This is a
   one-off act and it is yours: the scripts in `scripts/` are the
   only door Claude has to git, and they never initialise a
   repository or carry a remote. A remote is optional; add one with
   git's own command if you want the project pushed somewhere. The
   commit identity is git's, resolved per host from your own
   configuration, and the forge sets none. You should now see
   `projects/my-idea/.git/` exist: that is how the scripts recognise
   the project as a repository.

5. **Save.** Back in Claude Code, type `/save`. Claude first asks the
   state of every repository through `python scripts/forge-status.py`,
   which reports the engine and each project separately with the
   branch each is on. It runs the light check on every repository it
   will save and reports what the check found; a save never waits on
   a finding you have not asked to fix. It drafts a one-line English
   commit message from the history records of the round and proposes
   it; confirm it or adjust the wording. Only then it runs
   `python scripts/forge-save.py`, which commits and pushes on the
   branch that is checked out and prints the commit's file summary.
   No render is made by a save. You should now see the file summary
   of the commit in `projects/my-idea/`. What a save does and asks in
   full is [Save your work](../use/save-your-work.md).

6. **The other door: a project you already have.** Type
   `/import-project <project url>`. On your word Claude runs
   `python scripts/forge-clone.py <url>`, which clones the repository
   into `projects/<repository name>/`; the name falls out of the
   URL. Claude relays the script's facts: the last commit, the
   origin, the commit identity git resolves on this host, and whether
   the project carries a ledger with a `kind:` header. Nothing is
   written into the imported project. Then type
   `/forge <project-slug>`, the slug being the repository's name:
   the engine does not track your projects and cannot guess which
   one you mean, so the project is selected by naming it before any
   work. You should now see the project under `projects/` and
   Claude's report of the clone's facts. The full job is
   [Bring in an existing project](../use/bring-in-an-existing-project.md).

The teaching videos at the course page,
[https://pche-broken-artist.github.io/forge-of-thought/videos/](https://pche-broken-artist.github.io/forge-of-thought/videos/),
show this sitting on real work.

## What you have afterwards

Under `projects/my-idea/`:

- `00-brief.md`, approved, with `00-brief.history.md` beside it
- `10-intent.md`, the first intent, with `10-intent.history.md`
  beside it
- `ledger.md`, the project's state: its briefs, its documents and
  what is waiting on you
- `decisions.md`, empty of records until you decide something
- `sources/` and `research/`, each with its `00-INDEX.md`
- `reviews/` and `challenges/`, empty until a reviewer runs
- `recipes/readme.md` and `recipes/release-notes.md` with their
  history companions; their renders are made by a release, not yet
- `.git/`, a repository on `main` with your first commit

A `logo.png` in the project root is yours to supply if you want a
repository avatar; it is optional and nobody asks for it. Until
step 4 the project is "not under git": that is a property of the
project, not a defect, and nothing in the forge treats it as an
error.

From here the project grows by iterating the intent and by adding the
layers it needs; the full job of starting is
[Start a project](../use/start-a-project.md), and every term of this
page is in the [Glossary](../reference/glossary.md).

## If something goes wrong

- **`/new-project` stops and reports.** `projects/my-idea/` already
  exists; the command never overwrites. Choose another slug, or work
  the project that is there. The slug must be lowercase, with
  hyphens and no spaces.
- **`/save` says the project is "not under git" and has changes.**
  You have not run step 4 yet. The project is named in the report
  and otherwise left alone; nothing is lost. Initialise the
  repository and save again.
- **`/save` commits nothing and names its cause.** The two causes it
  names: there is no repository, or git resolves no identity for
  this host. The identity comes from your own `~/.gitconfig`, from
  the `includeIf` stanzas that `/setup` offers; with the recommended
  guard `user.useConfigOnly = true` and no global name or e-mail, a
  repository on a host with no stanza fails aloud instead of taking
  a default. Give the host its stanza (see
  [Set up the forge](setup.md)) and save again.
- **The light check reports findings.** Claude lays them out; a save
  never waits on a finding you have not asked to fix. Fix what you
  want fixed, or let the save go on.
- **Claude declines to run `git`.** By design: the scripts are the
  only door to git, enforced by the deny rules of
  `.claude/settings.json`. The `git init` of step 4 is yours, in
  your own terminal.
- **`/import-project` stops and reports.** `projects/<repository
  name>/` already exists. A clone for which git resolves no identity
  is not an error at the clone; it is caught at the first `/save`,
  which reports and commits nothing, as above.

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

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
