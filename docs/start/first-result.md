---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 42c4146a628366b2
inputs:
  - projects/forge/recipes/readme.md#Instructions
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - .claude/skills/new-project/SKILL.md
  - .claude/skills/forge/states/brief.md#Course
  - .claude/skills/forge/states/intent.md#Course
  - .claude/skills/walkthrough/SKILL.md#The elicitation interview
  - .claude/skills/walkthrough/SKILL.md#From verdicts to the write
  - .claude/skills/save/SKILL.md
  - .claude/skills/import-project/SKILL.md
  - CLAUDE.md#Persistence (git)
---

# Get a first result

A first result is a project of your own with its brief approved, its
first intent written and both saved in git, reached in one sitting.
This page is for you as the user of the forge: it takes you from an
empty `projects/` folder to that saved intent in five steps, four
typed to Claude and one typed in your own terminal. On this page you
are the principal, the person whose thinking is forged. The page
assumes the first run on this machine is done: [Set up the
forge](setup.md).

## When to use it

Use this page the first time you bring an idea to the forge, when no
project of yours exists yet. It is the short form of two full jobs,
[Start a project](../use/start-a-project.md) and [Forge the
intent](../use/forge-the-intent.md), which say each step in full.
Every act that happens outside Claude is a step of its own here, so
that nothing is done for you that you did not ask for. A project you
already keep in a git repository takes the other door, at the end of
this page.

## What you do

Typed to Claude, in this order, with one visit to your own terminal
in between. `my-idea` is a placeholder for your slug: lowercase,
hyphens, no spaces.

```
/new-project my-idea
```

When Claude asks for the brief, paste it and say that it is finished.

```
/forge intent
```

In your own terminal, at the engine root:

```
git -C projects/my-idea init -b main
```

Back with Claude:

```
/save
```

## What happens

### 1. Scaffold the project

`/new-project my-idea` creates `projects/my-idea/` from the
templates. It makes files only: the command never touches git. Where
your words leave them open, Claude asks two things before it writes:

- the kind of the project: `thought`, the default, a chain of
  documents that starts at a brief; or `library`, material shared
  across projects, with no chain
- the language of the project's documents: English, unless you name
  another

For a thought project it creates:

- `project.md`: the project file, with the slug, the kind and the
  language, written once
- `.gitattributes` and `.gitignore`: how git merges each kind of
  file, and what never enters git
- `decisions.md`: where your decisions will be recorded
- `sources/00-INDEX.md` and `research/00-INDEX.md`: the catalogues
  of external input and of research, empty for now
- `recipes/readme.md` and `recipes/release-notes.md`, each with its
  history companion ([Glossary](../reference/glossary.md)): how the
  project's README and release notes are rendered later, by a
  release and not by this command
- the empty folders `reviews/`, `challenges/` and `threads/`

A logo (`logo.png`) is mentioned once as optional and never asked
for. The intent is not created here. It is born from its own first
`/forge intent`, in step 3.

You should now see Claude asking you to paste or dictate the brief.

### 2. Paste the brief and say it is finished

A brief is your idea put together, in your own words and in whatever
language you wrote it. Paste it whole. Claude stores the text
verbatim as `00-brief.md`, with its history companion beside it, and
asks whether the text is finished. Say that it is: the brief is then
approved at once. Approval happens only on your explicit word, never
on Claude's own judgement. A brief that is not finished is kept as a
draft and worked from where it stops.

A brief for a first sitting can be as short as this one, invented
here as a shape and taken from no project:

```
We lose track of who agreed to what in our weekly planning.
I want one place where every decision of the week is written down
with its reason, so that nobody asks the same question twice.
It has to work for a team of ten without a new tool to learn.
Out of scope: anything that replaces the weekly meeting itself.
```

After the brief, Claude makes the ledger once (the project's state
report, made from its documents by a script and never kept in git)
and ends by naming the state of the brief. It proposes `/forge
intent` as the next step. It reminds you once that the project is
not under git until you initialise its repository. That line is a
fact about the project, not an error: a project "not under git" is a
property, not a defect, and the forge runs no git on it.

You should now see the brief named as approved, `/forge intent`
proposed and the one line that the project is not under git.

### 3. Forge the intent

An intent is the brief chiselled into the positions you hold. No
intent exists yet, so Claude consolidates the brief into the first
one through an interview. The interview runs one question per
message. Claude acknowledges your answer before it asks the next
question. When you send a thought in several messages, Claude asks
nothing until your closing word. Within the round Claude keeps to one
theme at a time.

Your answers are carried in the conversation and written once, at
the end of the round. Until then nothing is in a file, and Claude
says so. When the round looks finished, Claude adds `write` to the
verdict line, the line each of its propositions closes with. On
`write` Claude reflects the whole round back to you. On your yes it
writes everything carried as one round: `10-intent.md` is born, with
its history companion beside it. Claude ends by naming what changed
and what stays open. Where the intent is complete enough, it names
the layers that can follow from it, as a recommendation and never as
a gate.

You should now see `projects/my-idea/10-intent.md` named as written,
with what changed and what stays open.

### 4. Put the project under git, yourself

In your own terminal, at the engine root, run
`git -C projects/my-idea init -b main`. Add a remote afterwards if
you want one; it is optional. This is the one act of the sitting
Claude is not allowed to run. The scripts in `scripts/` are Claude's
only door to a write of git, and a hook denies every direct write.
Initialising a project's repository and adding its remote are your
one-off act at the project's creation. The identity that signs the
commits is git's, resolved per host from your own configuration,
which `/setup` offered to write; the forge sets none.

You should now see git confirm the new repository. From now on the
forge's scripts recognise `projects/my-idea` as a repository by
asking git whether its directory is the top of one.

### 5. Save

`/save` saves to git in three moves. First, Claude reads the state
through `python scripts/forge-status.py`, which reports the engine
and each project separately, with the branch each is on. Then it runs
the light check on every repository with changes and settles the
check's report with you; a save never waits on a finding you have not
asked to fix. Then it drafts a one-line English commit message from
the records the round appended to the documents' histories and
proposes it to you; the commit carries the wording you confirm or
adjust. Only after that does Claude run `python
scripts/forge-save.py`, which commits and pushes and prints the
commit's file summary. When more than one repository has changes, one
message is drafted per repository, or you save one repository by its
slug: `/save my-idea`. `/save --quick` leaves the check out and
changes nothing else.

Where `projects/forge`, the forge's own project, is cloned beside the
engine, the report names it too. It belongs to whoever develops the
engine, and you never need to open it.

You should now see the script's file summary of the commit for
`projects/my-idea`.

## What you have afterwards

- `projects/my-idea/`, a git repository of its own on the branch
  `main`, which the engine does not track
- `00-brief.md`, approved, with its history beside it
- `10-intent.md`, the first intent, with its history beside it
- the project file, the decisions file, the two catalogues and the
  two recipes, each recipe with its history
- `ledger.md`, made at read time and ignored by git
- one commit of all of it, with the message you confirmed

From here the intent grows by further rounds of `/forge intent`. The
project's README and release notes are made by a release, not by
this sitting.

## If something goes wrong

- `projects/my-idea/` already exists: `/new-project` stops and
  reports it. It never overwrites.
- The slug is refused: a slug is lowercase, with hyphens and no
  spaces.
- `/save` commits nothing and names its cause. There are two causes.
  No repository: step 4 has not been done, and the save's report
  names the project as "not under git" with changes and leaves it
  alone. No git identity for the host: git has no name and e-mail to
  sign commits on this machine, which is a different thing from the
  login that cloned the engine, and `forge-save` commits nothing
  until git resolves one; the ways out are the identity step of
  `/setup`.
- The ledger script fails or names files it could not parse: the
  check reads the ledger as it lies, the save goes on and says so.
  The save is what does not lose work.
- The save leaves a conflict standing: Claude lays both sides out,
  you decide, Claude writes the wording, the finishing commands of
  git run on your yes, and you save again.
- The sitting ends before `write`: everything agreed in the interview
  is nowhere yet, and Claude says so. Nothing of the intent exists in
  a file until the write.

## The other door: a project you already have

A project that already lives in a git repository is cloned, not
scaffolded. `/import-project <git-url>` clones it through
`scripts/forge-clone.py` into `projects/<repository name>`; the name
falls out of the URL. The command stops if that directory already
exists. The script reports the commit identity git resolves on this
host, and the command writes nothing into the project. Then
`/forge <project-slug>` selects the project, the slug being the
repository's name. You name it first because the engine does not
track the project and cannot guess it. A project already on this
machine is copied or linked into `projects/<slug>` by hand, and the
forge knows it from `/forge <slug>` on. The full job is [Bring in an
existing project](../use/bring-in-an-existing-project.md).

## Where it is shown on real work

This sitting is shown on real work in the teaching videos at the
course page,
<https://pche-broken-artist.github.io/forge-of-thought/videos/>: the
first video, how a brief is born, and the third, from the brief to
the intent.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
