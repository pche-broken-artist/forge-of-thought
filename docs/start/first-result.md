---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 3c13754d09d301a3
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

This page takes you from nothing to a saved intent in one sitting.
It is for you if the forge is set up on your machine and you want to
see a first project through: a brief, a first intent, and a commit
in git. You are the **principal** here (the person whose thinking is
being forged and who decides on all of it). Every act outside Claude
is a step of its own, and the page says which ones are yours. Every
term of the forge is in the [Glossary](../reference/glossary.md) in
one line.

## When to use it

Use it the first time you work with the forge, or whenever you start
a project from an idea that is not written down anywhere yet. It
assumes you have run the first run of the forge on this machine
([Set up the forge](setup.md)). If the project already exists as a
git repository somewhere, take the other door at the end of this
page.

The course page of the teaching videos,
<https://pche-broken-artist.github.io/forge-of-thought/videos/>,
shows this sitting on real work: how a brief is born, and how the
brief is taken into the intent.

## The command

The sitting is four acts, in this order. Three are typed to Claude,
started from the engine root. One is typed in your own terminal.

```
/new-project my-idea
```

```
/forge intent
```

```
git -C projects/my-idea init -b main
```

```
/save
```

`my-idea` is a placeholder slug. Use your own: lowercase, hyphens,
no spaces.

## What happens

1. **Scaffold the project.** Type `/new-project my-idea`. Claude
   creates `projects/my-idea/` with its files: the project file
   `project.md`, the folders for sources, research, reviews,
   challenges and threads, the decisions file and the recipes of the
   project's README and release notes. It writes files only and
   never touches git. If the project's language is not clear from
   what you said, Claude asks. It is English unless you name
   another. If `projects/my-idea/` already exists, Claude stops and
   overwrites nothing.
   You should now see the folder `projects/my-idea/` and Claude
   asking you for the brief.

2. **Paste the brief.** A **brief** is your idea put together, made
   yours by your approval. When Claude asks, paste it whole. Claude
   stores it verbatim as `projects/my-idea/00-brief.md` and asks
   whether the text is finished. Say that it is, and Claude approves
   it at once. A brief is approved only on your explicit word. A
   brief can be as short as this invented sample:

   ```
   Our team loses a day each week to status meetings nobody reads the notes of.
   I want a way to share progress that takes ten minutes, not an hour.
   It must work for people in three time zones.
   Not a new tool to buy: we use what we already have.
   Success is the weekly meeting cancelled for good.
   ```

   You should now see Claude name the state of the brief and propose
   `/forge intent`, with a reminder that the project is not under
   git until you initialise its repository.

3. **Forge the first intent.** Type `/forge intent`. The **intent**
   is the project's current positions (what you hold and what you
   have rejected), worked out of the brief. With no intent yet,
   Claude consolidates the brief into the first one through an
   interview. It works one theme at a time and asks you about what
   the brief says and leaves open. What you agree is carried in the
   conversation and written once at the end of the round, on your
   confirmation. Claude creates the intent as version 0.1, with its
   history beside it and a `threads/` folder for what stays open.
   You should now see `projects/my-idea/10-intent.md`, and Claude
   naming what changed and what stays open.

4. **Put the project under git.** In your own terminal, at the
   engine root, type:

   ```
   git -C projects/my-idea init -b main
   ```

   This is a one-off act at the creation of the project, and it is
   yours. Claude is not allowed to run git itself. Adding a remote
   is optional and may follow. Until this step, the project is "not
   under git". That is a property of the project, not an error.
   You should now see a folder `projects/my-idea/.git`.

5. **Save.** Type `/save`. Claude first runs the `light` check and
   settles what it reports with you. A save never waits on a finding
   you have not asked to fix. Claude then drafts a one-line commit
   message from the records the round wrote and proposes it. It
   commits with the wording you confirm or adjust, and pushes.
   You should now see the commit's file summary, as the save script
   prints it.

## What you have afterwards

A project in `projects/my-idea/` that is a git repository of its own.
It holds an approved brief, a first intent at version 0.1 with its
history, and the threads that stay open. The engine does not track
the project. That is why every later command names it by its slug.

## If something goes wrong

- **The save commits nothing.** The save names its cause. There are
  two:
  - **No repository.** The project is still "not under git". Claude
    names it in the report and leaves it alone. Run step 4, then
    `/save` again.
  - **No git identity for this host.** Git has no name and e-mail to
    sign commits with on this machine. The login you use for the
    remote is a different thing. The save commits nothing until git
    resolves an identity. The forge sets none. The usual causes and
    the ways out are in the identity step of
    [Set up the forge](setup.md).
- **The slug is taken.** `/new-project` stops when
  `projects/my-idea/` already exists. Choose another slug.
- **The check or the ledger script fails.** The save goes on and
  says so. The reason is that the save is what keeps your work from
  being lost.

## The other door: a project you already have

If the project already lives in a git repository, bring it in
instead of starting one:

```
/import-project <git-url>
```

On your word, Claude clones the repository into
`projects/<repository name>` and reports the git identity the clone
resolves. It writes nothing into the project. Then select the project
by naming it, before any work:

```
/forge <project-slug>
```

The slug is the repository's name. Claude cannot guess it. The
reason is that the engine does not track the project.

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

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
