---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 8f0eb0ba6e986bd2
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
intent, saved in a git repository of its own, all in one sitting.
This page is for you if you have set up the forge and want to go from
nothing to that saved intent. You are the principal here: the person
whose thinking is being forged, with the final word on every piece of
content. Each act you take outside Claude is a step of its own.

## When to use it

Use it the first time you start a project, once the first run of the
forge is done ([Set up the forge](setup.md)). If you already have a
project in a git repository somewhere, take the other door described
under "If you already have a project" below.

## The command

Start `claude` from the engine root, then type:

```
/new-project my-idea
```

`my-idea` is a placeholder slug: use your own, in lowercase with
hyphens and no spaces.

## What happens

1. **Claude scaffolds the project.** It creates `projects/my-idea/`
   with its project file (`project.md`, holding the slug, the kind and
   the language), the folders for sources, research, reviews,
   challenges and threads, the decisions file and the recipes of the
   project's README and release notes. It writes files only and never
   touches git. Where your words leave the language of the project
   open, it asks; English is the default.
   You should now see the new folder and Claude asking you to paste or
   dictate the brief.

2. **You paste the brief and say it is finished.** The brief is your
   own text of what you want, why, and what not. Paste it whole. Claude
   stores it verbatim as `00-brief.md` and asks whether the text is
   finished. Say yes, and the brief is approved at once. A sample of
   the shape, invented for this page:

   ```
   Our team loses a week every time someone new joins.
   I want a way of onboarding that a newcomer can follow alone.
   It should work for the first ten days, not the first year.
   Not a new tool: what we already use is enough.
   Why now: three people start next quarter.
   ```

   You should now see Claude name the state of the brief and propose
   `/forge intent`.

3. **You forge the first intent.** Type:

   ```
   /forge intent
   ```

   The intent is the versioned document that holds your positions on
   the idea, mined from the brief. Claude mines the brief through an
   interview: one question per message, one theme at a time. The
   answers are carried in the conversation, not written one by one. At
   the round's natural end Claude asks whether to write. Say `write`.
   Claude writes once for the whole round, on your confirmation. The
   first intent is created as version 0.1 with its history beside it
   (`10-intent.md` and `10-intent.history.md`).
   You should now see Claude name what changed and what stays open.

4. **You put the project under git, in your own terminal.** This is a
   one-off act that Claude is not allowed to run: Claude writes
   nothing into git itself. In a terminal of your own, at the engine
   root, type:

   ```
   git -C projects/my-idea init -b main
   ```

   Add a remote afterwards if you want one; it is optional. Until this
   step the project is "not under git". That is a property of the
   project, not an error.
   You should now see that the next save no longer calls the project
   "not under git".

5. **You save.** Back in Claude, type:

   ```
   /save
   ```

   Claude runs the light check (a quick check of the conventions) and
   settles its report. A save never waits on a finding you have not
   asked to fix. Claude then drafts a one-line commit message from the
   records of the round and proposes it. You confirm or adjust it, and
   Claude commits and pushes.
   You should now see the file summary of the commit, printed by the
   save script.

## What you have afterwards

- A project of its own under `projects/my-idea/`, in a git repository
  that the engine does not track.
- An approved brief, `00-brief.md`.
- A first intent at version 0.1, `10-intent.md`, with its history.
- The whole sitting committed, and pushed where a remote exists.

The full jobs behind these steps are on their own pages:
[Start a project](../use/start-a-project.md),
[Forge the intent](../use/forge-the-intent.md) and
[Save your work](../use/save-your-work.md). The teaching videos on the
course page,
https://pche-broken-artist.github.io/forge-of-thought/videos/, show
this sitting on real work.

## If you already have a project

A project that already lives in a git repository comes in by cloning:

```
/import-project <git-url>
```

On your word Claude clones it into `projects/<repository name>`; the
name falls out of the URL. Nothing is written into the imported
project. Then select it by naming it, because the engine does not
track the project and cannot guess it:

```
/forge <project-slug>
```

The slug is the repository's name. The whole job is on
[Bring in an existing project](../use/bring-in-an-existing-project.md).

## If something goes wrong

- **The slug is refused.** A slug is lowercase with hyphens and no
  spaces. If `projects/my-idea/` already exists, `/new-project` stops
  and reports it: it never overwrites.
- **The save commits nothing.** The save names its cause. Either the
  project has no repository yet (do step 4), or git has no identity
  for this host. An identity is the name and e-mail git signs commits
  with; the login that cloned a repository is a different thing. The
  forge sets none: the usual causes and the ways out are in the
  identity step of [Set up the forge](setup.md).
- **The save meets a conflict.** The script leaves the conflicting
  rebase standing instead of aborting it. Claude lays out both sides
  for you to decide, then saves again. Where a rebase or merge is
  already standing, the save refuses and names the step to take.
- **The import stops.** If `projects/<repository name>` already exists,
  `/import-project` stops and reports it.

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
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
