---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 34893bcb887df671
inputs:
  - projects/forge/recipes/readme.md#Instructions
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/forge/states/brief.md#Course
  - .claude/skills/forge/states/intent.md#Course
  - .claude/skills/save/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - CLAUDE.md#Persistence (git)
---

# Get a first result

A first result is a project of your own with its brief approved,
its first intent written and the whole saved to git, reached in one
sitting. This page is for you as the principal (the person whose
thinking is forged): it names every act of that sitting as a step
of its own, the acts Claude does for you and the acts you do in your
own terminal, and says what you see after each. The full jobs behind
the steps have pages of their own, listed under See also.

## When to use it

Use this page the first time you work in the forge, once the set-up
is done ([Set up the forge](setup.md)) and before any project of
yours exists. It starts from nothing: an idea you carry and a few
lines you can paste. A project that already lives in a git
repository somewhere comes in through the other door, the second
block below.

## What you do

Start `claude` from the engine root. Then, in order:

```
/new-project my-idea                    # Claude scaffolds the files, then asks for the brief
/forge intent                           # the interview; the first intent is written at the round's end
git -C projects/my-idea init -b main    # in your own terminal at the engine root; a remote may follow
/save my-idea                           # the light check, then commit and push
```

`my-idea` is a placeholder. Replace it with your own slug: lowercase,
hyphens, no spaces.

The other door, for a project you already have:

```
/import-project <git-url>               # clones into projects/
/forge <project-slug>                   # the slug is the repository's name
```

## What happens

1. **`/new-project my-idea`: Claude scaffolds the files.** The
   command writes files only and never touches git. Claude checks
   the slug and refuses to overwrite a folder that exists. It asks
   two things only where your words leave them open: the kind of
   the project (a thought project, the default, or a library) and
   the language of its artefacts (English unless you name another).
   Then it creates under `projects/my-idea/`:
   - the folders `sources/`, `research/`, `reviews/` and
     `challenges/`, with an index file in the first two
   - `ledger.md`, the ledger (the project's single file of state),
     filled with the slug, the kind, the language and today's date
   - `decisions.md`, empty of records
   - `recipes/readme.md` and `recipes/release-notes.md`, each with
     its history companion; their outputs are made later, by a
     release, not now

   It mentions once that a `logo.png` in the project root is yours
   to supply and optional. It does not create the intent: that file
   is born from its own first `/forge intent`. You should now see
   the folder `projects/my-idea/` with those files, and Claude
   asking you to paste or dictate the brief.

2. **Paste the brief and say it is finished.** The brief is your
   idea put together in your own words, the file every project
   starts from. Pasted whole, the text is stored verbatim in
   `00-brief.md`, with its history companion beside it and a row in
   the ledger's Briefs table. Claude asks whether the text is
   finished. Say it is, and the brief is approved at once; Claude
   approves only on your explicit word. If you would rather talk
   the brief out than paste it, Claude works from your first word,
   and the text is written once per round on your confirmation.
   Claude ends by naming the state of the brief, proposing
   `/forge intent`, and reminding you that the project is not
   under git until you initialise its repository. "Not under git"
   is a fact about the project at this point, not an error. You
   should now see `projects/my-idea/00-brief.md` as an approved
   brief and the proposal to forge the intent.

3. **`/forge intent`: Claude mines the brief into the first
   intent.** The intent is what you want and why, mined from the
   brief. No intent exists yet, so the way in is to consolidate the
   brief into the first one. Claude reads the brief and works
   through it with you by questions, one theme at a time; the
   reality check comes last. Nothing is written while the round
   runs: what you agree is carried in the conversation and written
   once, at the round's end, on your confirmation. The write creates
   `10-intent.md` as version 0.1, with its history companion
   `10-intent.history.md` and the file `threads.md` for what stays
   open, and brings the brief's row in the ledger up to date. Claude
   ends by naming what changed and what stays open. You should now
   see `projects/my-idea/10-intent.md` at 0.1 and a list of what is
   still open.

4. **In your own terminal, at the engine root:
   `git -C projects/my-idea init -b main`.** This is your act, not
   Claude's. Every project is a git repository of its own that the
   engine does not track, and initialising it is the user's one-off
   act at creation. Claude is not allowed to run it: the scripts in
   `scripts/` are its only door to git, enforced by the deny rules
   of its settings, and this line is the way into git for a
   project. A remote may follow if you want one; the scripts carry
   no URL. The commit identity is git's, resolved per host from
   your own configuration (the `includeIf` stanzas in
   `~/.gitconfig` that `/setup` offers); the forge sets none. You
   should now see `projects/my-idea/.git/` in the project folder.

5. **`/save my-idea`: Claude checks, then commits and pushes.** The
   save runs on whatever branch is checked out and renders nothing.
   Claude first reads the state through the status script, which
   reports the engine and each project with the branch each is on.
   It then runs the light check (a mechanical check of the
   conventions) on the repository and reports what it found; a save
   never waits on a finding you have not asked to fix. It drafts a
   one-line commit message from the records the round appended to
   the histories and proposes it to you; the commit carries the
   wording you confirm or adjust. Only then does it run the save
   script, which commits and pushes. You should now see the
   commit's file summary, printed by the script.

   Bare `/save` saves every repository with changes, the engine
   among them, one message per repository.

**If you came through the other door.** `/import-project <git-url>`
clones the repository into `projects/<repository name>` through the
clone script; the directory's name falls out of the URL. On your
word the clone runs, and Claude relays the script's facts: the last
commit, the origin, the commit identity git resolves and whether the
project carries a ledger with a `kind:` header. Nothing is written
into the imported project. Then `/forge <project-slug>` selects the
project as the first act of work: the engine does not track the
project and cannot guess it, so you name it before any work. You
should now see Claude working on that project.

## What you have afterwards

- `projects/my-idea/`, a project with an approved brief, a first
  intent at 0.1, their history companions, the open threads, the
  ledger, the decisions file and two recipes
- a git repository of its own in that folder, with the sitting
  committed, and a remote if you added one
- Claude's word on where to continue: what stays open in the
  intent, or the layers that can follow once the intent is
  complete

## If something goes wrong

- **`/new-project` stops and reports.** The slug is not lowercase
  with hyphens and no spaces, or `projects/my-idea/` already exists.
  Nothing is overwritten; pick another slug.
- **The brief stays a draft.** You did not say the text is finished.
  Claude approves only on your explicit word; say it when the text
  is what you want.
- **`/save` commits nothing and names its cause.** Two causes are
  recorded:
  - no repository: the project is "not under git", a property, not
    a defect; the status report names it with its changes and leaves
    it alone, and the save relays the script's note. Run the `git -C`
    line of step 4 and save again.
  - no git identity for the host: with the recommended guard
    `user.useConfigOnly = true` and no global name or e-mail, a
    repository on a host with no stanza fails aloud instead of
    taking a default. Add the stanza for the host in `~/.gitconfig`,
    as `/setup` offers, and save again.
- **The light check found something.** The findings are reported
  and settled with you; a save never waits on a finding you have not
  asked to fix.
- **`/import-project` stops and reports.** `projects/<repository
  name>/` already exists. A clone for which git resolves no identity
  is not stopped at the import: the save catches it, reports it and
  commits nothing.

## A worked example

A sitting with the placeholder slug `my-idea`. The brief is generic
and invented.

```
/new-project my-idea
```

Claude creates the folder and its files, takes English as the
language of the project, and asks for the brief. You paste:

```
Handovers between our teams take too long because each one is
written in its own way. I want one shape for a handover that says
what is wanted, what is out of scope and who decides what. It
should fit on one page and be usable by anyone who writes one.
The first recipients are two teams; later it may serve everyone.
```

Claude stores the text verbatim in `00-brief.md` and asks whether
it is finished. You say yes. Claude approves the brief, proposes
`/forge intent` and reminds you that `my-idea` is not under git.

```
/forge intent
```

Claude reads the brief and works through it with you, one theme at
a time: what a handover is for, where the one shape ends, who the
first recipients are. At the round's end it reflects back what you
agreed and, on your confirmation, writes `10-intent.md` at 0.1 with
its history companion and `threads.md`, and tells you what stays
open.

In your own terminal, at the engine root:

```
git -C projects/my-idea init -b main
```

Then, back in Claude:

```
/save my-idea
```

Claude runs the light check, proposes a one-line commit message,
and on your word the script commits and prints the file summary.

## See also

- [Set up the forge](setup.md): the first run that comes before.
- [Start a project](../use/start-a-project.md): the full job of
  starting a project, thought or library.
- [Bring in an existing project](../use/bring-in-an-existing-project.md):
  the other door, a project you already have, cloned into
  `projects/`.
- [Forge the intent](../use/forge-the-intent.md): the full job of
  iterating the intent.
- [Save your work](../use/save-your-work.md): what a save does and
  asks.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
