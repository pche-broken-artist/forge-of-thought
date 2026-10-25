---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 27d643e93dbe1598
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
It is for you as the principal (the person whose thinking is forged
and who decides every piece of content; see the
[Glossary](../reference/glossary.md)), working with Claude in the
engine you have just set up. Every act outside Claude is a step of
its own, and the page names each one.

## When to use it

Use it the first time you start a project in the forge.

You need a finished setup first: [Set up the forge](setup.md).
Start `claude` from the engine root, as setup does.

This sitting is shown on real work in the teaching videos, on the
course page https://pche-broken-artist.github.io/forge-of-thought/videos/.

## The command

The sitting is five acts, in this order:

```
/new-project my-idea
(paste the brief when asked, and say it is finished)
/forge intent
git -C projects/my-idea init -b main
/save
```

`my-idea` is a placeholder slug: use a slug of your own, in
lowercase with hyphens and no spaces.

The fourth line is typed in your own terminal at the engine root,
not given to Claude.

## What happens

1. **Scaffold the project.** Type `/new-project my-idea`. Claude
   creates `projects/my-idea/` from the templates:
   - the project file;
   - the folders for sources, research, reviews, challenges and
     threads;
   - the decisions file;
   - the recipes of the project's README and release notes.

   It writes files only and never touches git. Where your words
   leave it open, it asks which language the project's documents are
   written in. English is the default. The intent is not created
   yet: it is born from its own first `/forge intent`.
   You should now see the folder `projects/my-idea/` and Claude
   asking you for the brief.

2. **Paste the brief.** A brief is your idea put together in your
   own words. Paste it whole when Claude asks for it. Claude stores
   it verbatim as `00-brief.md` and asks whether the text is
   finished. Say that it is. A brief you call finished is approved
   at once. Five lines are enough to start, for example:

   ```
   Our weekly team meeting runs long and decides little.
   I want a meeting format that ends with clear decisions and owners.
   It must fit in thirty minutes.
   Not in scope: tools or software for running meetings.
   Why now: two projects slipped because nobody owned the next step.
   ```

   You should now see Claude name the brief as approved and propose
   `/forge intent`.

3. **Forge the intent.** Type `/forge intent`. The intent is the
   statement of the positions you hold about the idea. With no
   intent yet, Claude consolidates the brief into the first one
   through an interview, one theme at a time. You answer, and Claude
   carries the answers in the conversation. The intent is written
   once, at the end of the round, on your confirmation. Claude ends
   by naming what changed and what stays open.
   You should now see `10-intent.md` in `projects/my-idea/` at
   version 0.1, with what stays open kept as threads in `threads/`.

4. **Put the project under git.** In your own terminal, at the
   engine root, type:

   ```
   git -C projects/my-idea init -b main
   ```

   This is a one-off act, and it is yours. Claude writes nothing
   into git itself: a guard in the engine denies it every write of
   git, so the init and a remote are left to you. A remote is
   optional; add one with git if you want the project pushed
   anywhere.
   Until this step the project is "not under git". That is a fact
   about the project, not an error.
   You should now see `projects/my-idea/` as a repository of its own,
   so the next save no longer reports it as not under git.

5. **Save.** Type `/save`. Claude runs the light check on the
   repository first. A finding of the check never holds the save
   back unless you ask for it to be fixed. Claude then drafts a
   one-line commit message from what the round changed and proposes
   it. Confirm it or adjust it. The save commits and pushes.
   You should now see the commit's file summary for
   `projects/my-idea` in the report.

## What you have afterwards

- A project of your own under `projects/my-idea/`, in a git
  repository of its own that the engine does not track.
- An approved brief.
- A first intent, with what stays open kept as threads.
- One commit holding all of it.

From here, [Forge the intent](../use/forge-the-intent.md) is the full
job of iterating the intent, and
[Start a project](../use/start-a-project.md) is the full job of
starting one.

## If something goes wrong

- **`/new-project` stops at once.** The folder
  `projects/my-idea/` already exists. Claude never overwrites it.
  Choose another slug.
- **`/save` commits nothing and says the project is not under git.**
  Step 4 has not been done. Run the `git init` line in your own
  terminal and save again.
- **`/save` commits nothing because git has no identity for this
  host.** Git has no name and e-mail to sign commits with on this
  machine. The login you use for a remote is a different thing. The
  forge sets no identity: it is resolved by your own git
  configuration, per host. Setup offers the per-host settings and a
  guard that makes a missing identity fail aloud instead of taking a
  default. Return to the identity step of
  [Set up the forge](setup.md), then save again.
- **`/save` refuses because a rebase or merge is already
  standing.** Claude reports the refusal and the step it names.
  What a save does and asks in full is on
  [Save your work](../use/save-your-work.md).

## The other door: a project you already have

Where the project already exists in a git repository, bring it in
instead of creating it:

```
/import-project <git-url>
/forge <project-slug>
```

`/import-project` clones the repository into `projects/`, under the
repository's name, and reports the commit identity git resolves for
it. Then name the project with `/forge <project-slug>`, the slug
being the repository's name. You select it before any work. The
reason is that the engine does not track the project and cannot
guess it. The full job is on
[Bring in an existing project](../use/bring-in-an-existing-project.md).

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
