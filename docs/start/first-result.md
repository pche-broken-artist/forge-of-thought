---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 4289087bbc6a0c27
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

A first result is one sitting that takes you from nothing to a saved
intent: a new project, a brief, the first intent and a save into git.
This page is for you as the principal (the person whose thinking is
forged, who decides everything of substance) on your first sitting
with the forge. It names the five acts of that sitting in order, what
Claude does at each and what you see when it worked. The full job
behind each act has a page of its own, linked at the end.

## When to use it

Use it once, right after [Set up the forge](setup.md) has run on
your machine. You have an idea in your head or on a page and no
project yet. You want to see the whole way through once before you
read the rest.

Every act that happens outside Claude is a step of its own on this
page. Claude writes nothing into git itself: initialising the
project's repository is your one-off act, in your own terminal.

## What you do

Five lines, in this order. The first three you type to Claude, the
fourth in your own terminal at the engine root, the fifth to Claude
again.

```
/new-project my-idea
/forge intent
git -C projects/my-idea init -b main
/save
```

`my-idea` is a placeholder slug: lowercase, hyphens, no spaces.
Between the first and the second line Claude asks you for the brief,
and you paste it.

## What happens

### 1. Scaffold the project

Type `/new-project my-idea`. Claude creates `projects/my-idea/` from
the templates: files only, never git. Each project has a kind. The
default is a thought project, the one that carries a chain of
documents. Each project also declares the language of its documents,
English unless you name another. Claude asks when your words leave
either open.

Claude creates the project file, the folders for sources, research,
reviews, challenges and threads, the decisions file and the two
render recipes of the project. It does not create the intent yet.
The intent is born from its own first `/forge intent`. Claude
mentions once that `logo.png` is yours to supply and optional. It
never asks for it.

You should now see the folder `projects/my-idea/` and Claude's
question for the brief.

### 2. Paste the brief

A brief is the text of your idea as you hand it in. Claude asks you
to paste or dictate it now. Paste it whole and say that it is
finished. Claude stores the text verbatim, approves it on your
word and creates `00-brief.md` with its history companion beside it.

A brief may also be begun outside and finished here, or born here
from a rough idea in conversation. The quickest first result is the
pasted one. A generic brief of five lines is enough to start:

```
Idea: replace the monthly status mail with a shared status page.
Why now: the mail is rewritten by hand each month and drifts.
Who it is for: the team leads who read it and the one who writes it.
What must hold: nothing is published that the writer has not approved.
What is open: who owns the page after the first quarter.
```

After the brief Claude makes the ledger (the project's state, made
by a script at read time and never in git), proposes `/forge intent`
as the next step and reminds you that the project is not under git
until you initialise its repository.

You should now see `projects/my-idea/00-brief.md` as approved and
Claude proposing `/forge intent`.

### 3. Forge the intent

Type `/forge intent`. The intent is the first document mined from
the brief, the trunk every later document grows from. Claude reads
the brief and, since there is no intent yet, consolidates it into
the first one through an interview: one question per message, one
theme at a time. The reality check comes last in the round.

Nothing is written while the round runs. At the round's natural end
Claude asks whether to write, and writes on your word `write`: one
version for the whole round. The first intent is created as
version 0.1 with its history companion and an empty `threads/`
folder. The mining of the brief is recorded in the intent's history.
Claude remakes the ledger after the write and ends by naming what
changed and what stays open.

You should now see `projects/my-idea/10-intent.md` at version 0.1
and Claude naming what stays open.

### 4. Put the project under git

This act is yours, in your own terminal at the engine root. Type:

```
git -C projects/my-idea init -b main
```

Until this line the project is not under git. That is a fact about
the project, not an error: the forge runs no git on such a project
and says so once. Every project under `projects/` is a repository
of its own, which the engine does not track. Initialising it and
adding a remote are your one-off act at creation. A remote is
optional. The forge carries no URL and no identity. The identity
git signs your commits with is resolved per host from your own
configuration, offered by `/setup`.

You should now see git report an empty repository on the branch
`main` in `projects/my-idea`.

### 5. Save

Type `/save`. Claude reads the state of the engine and of each
project by a script and names each with the branch it is on. Then it
runs the light check, a mechanical check of the conventions, on
every repository with changes. What the check finds is put to you.
A save never waits on a finding you have not asked to fix. Then
Claude drafts a one-line English commit message from the records of
the round and proposes it. You confirm or adjust the wording. Only
then Claude runs the save script, which commits and pushes on the
branch that is checked out. The script prints the commit's file
summary.

A save that commits nothing names its cause: no repository, or no
git identity for the host. What to do then is under If something
goes wrong.

You should now see the commit's file summary for `projects/my-idea`.

## The other door

A project that already lives in a git repository comes in by two
lines instead of the first four:

```
/import-project <git-url>
/forge my-idea
```

`/import-project` clones the repository into `projects/`. The slug
is the repository's name and falls out of the URL. `/forge my-idea`
is the first act of work: the engine does not track the project and
cannot guess it, so you select it by naming it. The job in full is
[Bring in an existing project](../use/bring-in-an-existing-project.md).

`projects/forge` is the forge's own project. You never need to open
it.

The sitting of this page is shown on real work in the teaching
videos at the course page,
<https://pche-broken-artist.github.io/forge-of-thought/videos/>:
"How a brief is born" and "From the brief to the intent".

## What you have afterwards

- `projects/my-idea/project.md`: the project file, with slug, kind
  and language.
- `projects/my-idea/00-brief.md`: your brief, approved, with its
  history companion beside it.
- `projects/my-idea/10-intent.md`: the first intent at version 0.1,
  with its history companion and the `threads/` folder.
- `projects/my-idea/decisions.md`, the two recipes under `recipes/`
  and the index files under `sources/` and `research/`.
- `projects/my-idea/ledger.md`: the state, remade by a script and
  never in git.
- A git repository on `main` with your first commit, pushed where
  you added a remote.

From here the intent grows by rounds of `/forge intent`. The job in
full is [Forge the intent](../use/forge-the-intent.md). What a save
does and asks is [Save your work](../use/save-your-work.md).

## If something goes wrong

- `/new-project` stops and reports when `projects/my-idea/` already
  exists. It never overwrites. Choose another slug.
- `/import-project` stops and reports when the target directory
  already exists.
- `/save` commits nothing and names no repository as the cause: step
  4 has not run. Run the `git -C projects/my-idea init -b main` line
  and save again.
- `/save` commits nothing and names no git identity for the host as
  the cause: git has no name and e-mail to sign commits on this host.
  The login that cloned the repository is a different thing. The
  ways out are the identity step of [Set up the forge](setup.md).
  The forge writes no identity itself.
- The light check finds something. Claude puts it to you; the save
  does not wait on a finding you have not asked to fix.
- The ledger script fails or names files it could not parse. The
  check reads the ledger as it lies, the save goes on and says so:
  the save is what does not lose work.
- The save script refuses because a rebase or a merge is already
  standing. Claude reports the refusal and the step it names.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
