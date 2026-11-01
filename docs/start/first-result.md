---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 80e0dbf306e9e795
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
intent, saved in git, all made in one sitting. This page walks you
through that sitting, from nothing to a saved intent. It is for you if
you are the principal (the person whose thinking is being forged) and
you have just set the forge up. Every act that happens outside Claude
is a step of its own on this page.

## When to use it

Use this the first time you work with the forge, or whenever you start
a project from an idea that has no files yet. You need the first run of
the forge behind you: see [Set up the forge](setup.md). Start `claude`
from the engine root, the folder you cloned.

If the project already exists in a git repository, take the other door
described under "If you already have a project" below.

## The command

The whole sitting, in order:

```
/new-project my-idea
/forge intent
git -C projects/my-idea init -b main
/save
```

`my-idea` is a placeholder: choose your own slug, lowercase with
hyphens and no spaces. The third line is typed in your own terminal at
the engine root, not to Claude.

## What happens

1. **Scaffold the project.** Type `/new-project my-idea` to Claude.
   Claude creates the folder `projects/my-idea/` and its files. It
   creates files only and never touches git. If Claude cannot tell
   from your words which language the project's documents should be
   in, it asks. English is the default. If a folder of that name
   already exists, Claude stops and overwrites nothing.

   You should now see a new folder `projects/my-idea/` holding
   `project.md`, `decisions.md`, a `recipes/` folder and the empty
   folders `sources/`, `research/`, `reviews/`, `challenges/` and
   `threads/`.

2. **Give the brief.** Claude asks you to paste or dictate the brief.
   The brief is your own text of what you want, why, and what you do
   not want. Paste it whole. Claude stores it word for word in
   `00-brief.md` and asks whether the text is finished. Say that it
   is. Claude approves the brief only on your explicit word. A brief
   can be as short as this invented sample:

   ```
   Our team answers the same customer questions by mail again and again.
   I want one shared place where a good answer is written once and found again.
   Why: new colleagues take weeks to learn what the others already know.
   Not wanted: a new tool to buy, or a bot that answers for us.
   Success: fewer repeated questions three months from now.
   ```

   Claude then makes the ledger (the file that states where the
   project stands, built from its documents). It proposes
   `/forge intent` as the next step. It also reminds you that the
   project is not under git yet.

   You should now see `00-brief.md` in the project folder, with its
   history file `00-brief.history.md` beside it, and the brief named
   as approved.

3. **Forge the first intent.** Type `/forge intent`. The intent is the
   project's record of what you currently hold, the trunk every later
   document grows from. With no intent yet, Claude mines the brief
   into the first one through an interview. Claude asks one question
   per message and works one theme at a time. A check against
   reality comes last. Your answers are carried in the conversation.
   They are written once, at the end of the round, when you give the
   word `write`. Claude ends by naming what changed and what stays
   open.

   You should now see `10-intent.md` in the project folder, with its
   history file `10-intent.history.md` beside it. Whatever is still
   open stands as files in `threads/`.

4. **Put the project under git.** In your own terminal, at the engine
   root, type:

   ```
   git -C projects/my-idea init -b main
   ```

   This is a one-off act that is yours. Claude writes nothing into git
   itself, and it is not allowed to run this command. Adding a remote
   is optional and also yours. Until this step the project is "not
   under git", and that is a fact about the project, not an error.

   You should now see git confirm a new repository in
   `projects/my-idea/`.

5. **Save.** Type `/save`. Claude runs the light check (a quick check
   of the project's conventions) and settles what it finds with you.
   A save never waits on a finding you have not asked to fix. Claude
   then drafts a one-line commit message from the round's records
   and proposes it. It commits with the wording you confirm or adjust,
   and pushes.

   You should now see Claude report the commit with its file summary.

## What you have afterwards

- A project folder `projects/my-idea/` that is a git repository of its
  own. The engine does not track it, which is why you name the project
  when you work on it.
- An approved brief, `00-brief.md`.
- A first intent, `10-intent.md`, with its history.
- The open matters of the intent as thread files in `threads/`.
- One commit holding all of it.

From here, the next round of the intent is again `/forge intent`. See
[Forge the intent](../use/forge-the-intent.md) for the full job, and
[Start a project](../use/start-a-project.md) for everything
`/new-project` can do.

## If something goes wrong

- **The folder already exists.** `/new-project` stops and overwrites
  nothing. Choose another slug.
- **The slug is refused.** A slug is lowercase, with hyphens and no
  spaces.
- **The save commits nothing.** The save names its cause. There are
  two causes:
  - No repository: the project is still "not under git". Run step 4,
    then `/save` again.
  - No git identity for the host: git has no name and e-mail to sign
    commits on this machine. The login you used for a remote is a
    different thing. The ways out are the identity step of
    [Set up the forge](setup.md). The forge sets no identity itself.
- **A conflict at the save.** Claude leaves it standing, not aborted,
  and lays both sides out for you to decide. See
  [Save your work](../use/save-your-work.md).

## If you already have a project

A project that already lives in a git repository is cloned in instead
of scaffolded:

```
/import-project <git-url>
/forge <project-slug>
```

`/import-project` clones the repository into `projects/`, under the
repository's name. It writes nothing into the project. If git resolves
no identity for the clone, Claude says so. Then select the project with
`/forge <project-slug>`, where the slug is the repository's name. The
engine does not track the project and cannot guess it. See
[Bring in an existing project](../use/bring-in-an-existing-project.md).

## A worked example

This sitting is shown on real work in the teaching videos, on the
course page https://pche-broken-artist.github.io/forge-of-thought/videos/.

For the terms on this page, see the [Glossary](../reference/glossary.md).

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

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
