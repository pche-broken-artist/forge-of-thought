---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 7f176efec3f981e5
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

A first result is a new project with an approved brief and a first
intent, saved to git, made in one sitting. This page is for you when
the forge is set up and you want to go from nothing to a saved
intent. You are the principal: the person whose thinking is forged
and who decides on everything that is written. Every act outside
Claude is a step of its own, and the page says which one is yours.

## When to use it

Use it the first time you work in the forge, after
[Set up the forge](setup.md). Use it again whenever you start a
fresh idea from nothing. If the project already exists in a git
repository somewhere, use the other door at the end of
"What you do".

The same sitting is shown on real work in the teaching videos, on
the course page
https://pche-broken-artist.github.io/forge-of-thought/videos/.

## What you do

Start `claude` from the engine root, then type these, one at a time,
answering Claude between them:

```
/new-project my-idea
/forge intent
```

In your own terminal, at the engine root:

```
git -C projects/my-idea init -b main
```

Back in Claude:

```
/save
```

Claude writes nothing into git itself. Initialising the project's
repository, and adding a remote if you want one, is your one-off act.

The other door, for a project you already have in a git repository:

```
/import-project <project url>
/forge <project-slug>
```

The slug is the repository's name. You name the project first
because the engine does not track it and cannot guess it. The full
job is [Bring in an existing project](../use/bring-in-an-existing-project.md).

## What happens

1. **`/new-project my-idea` scaffolds the files.** Claude checks the
   slug (lowercase, hyphens, no spaces) and creates `projects/my-idea/`
   with its folders, its project file, its decisions file and the
   recipes of its README and release notes. It may ask in which
   language the project's documents are written. English holds
   unless you name another. It creates files only and never touches
   git. The full job is [Start a project](../use/start-a-project.md).
   You should now see Claude asking you to paste or dictate the brief.

2. **You paste the brief and say it is finished.** A brief is your
   idea put together, in your own words. Claude stores what you paste
   as it stands and asks whether the text is finished. When you say
   it is, the brief is approved at once. A brief can be as short as
   this invented sample:

   ```
   Our team loses half a day each week to status meetings.
   I want a way to share progress that needs no meeting.
   It must work for people in three time zones.
   It must not add a new tool everyone has to learn.
   I am not sure yet whether written updates are enough.
   ```

   Claude then makes the ledger (the file that states where the
   project stands, built from its documents) and proposes the next
   step. You should now see Claude proposing `/forge intent` and
   reminding you that the project is not under git until you
   initialise its repository.

3. **`/forge intent` mines the brief into the first intent.** The
   intent is the document of the positions you hold on the idea.
   Claude reads the approved brief and works it with you in an
   interview, one theme at a time, drawing out what the brief leaves
   open. Your answers are carried in the conversation. Nothing is
   written until the round ends and you confirm. Then the first
   intent is created as version 0.1, with its history beside it and a
   `threads/` folder for what is still open. The full job is
   [Forge the intent](../use/forge-the-intent.md). You should now see
   Claude naming what changed and what stays open.

4. **You initialise the repository in your own terminal.** At the
   engine root you type `git -C projects/my-idea init -b main`, then
   add a remote if you want one. A remote is optional. Claude is not
   allowed to run this step. Until it is done, "not under git" is a
   fact about the project, not an error. You should now see the
   project inside a repository of its own, so that the next save
   treats it as one.

5. **`/save` checks, commits and pushes.** Claude runs the light
   check (a mechanical check of the forge's conventions) on the
   project and settles anything it finds with you. A save never waits
   on a finding you have not asked to fix. Claude then drafts a
   one-line commit message from what the round changed and proposes
   it. You confirm or adjust it. The full job is
   [Save your work](../use/save-your-work.md). You should now see the
   commit's file summary printed by the save.

## What you have afterwards

- `projects/my-idea/` as a git repository of its own, which the
  engine does not track.
- An approved brief, `00-brief.md`, with its history beside it.
- A first intent, `10-intent.md`, at version 0.1, with its history
  and its open threads.
- A commit that holds them, pushed where a remote exists.

The terms used here are listed in the [Glossary](../reference/glossary.md).

## If something goes wrong

- **`projects/my-idea/` already exists.** `/new-project` stops and
  reports. It never overwrites. Choose another slug.
- **The save commits nothing.** The save names its cause: there is
  no repository, or git has no identity for this host. With no
  repository, do step 4. With no identity, git has no name and e-mail
  to sign commits on this machine. The login that cloned a repository
  is a different thing. The usual causes and the ways out are in the
  identity step of [Set up the forge](setup.md). The forge writes no
  identity itself.
- **The save names the project as "not under git".** A project
  without a repository that has changes is named in the save's report
  and otherwise left alone. Do step 4 and save again.
- **The save stops on a rebase or merge.** Where the save meets a
  conflict, it leaves the conflict standing and names the step to
  take. Where a rebase or merge is already standing, it refuses and
  says so. Claude lays both sides out for you, you decide, and the
  save is run again.
- **`/import-project` finds the directory taken.** The target is
  `projects/<repository name>`. If it already exists, the command
  stops and reports.

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

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
