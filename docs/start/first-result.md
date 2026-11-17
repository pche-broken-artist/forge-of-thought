---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 56fdecea56d169c3
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
---

# Get a first result

A first result is a saved intent, reached from nothing in one
sitting. This page is for you if you have set the forge up and now
bring an idea of your own. In the forge's words you are the
[principal](../reference/glossary.md) (the person whose thinking is
forged).

## When to use it

Use it for your first project, once the forge is set up. The first
run that comes before is [Set up the forge](setup.md).

The same sitting is shown on real work in the teaching videos of the
[course page](https://pche-broken-artist.github.io/forge-of-thought/videos/):
every video is a real session of the forge (one conversation with
Claude), cut to a few minutes, nothing staged.

A project that already lives in a git repository comes in by the
other door:

```
/import-project <git-url>
/forge <project-slug>
```

`/import-project` clones the repository into `projects/`, and Claude
runs the clone on your word. The command writes nothing into the
project. The [slug](../reference/glossary.md) (the short name of a
project and of its folder) is the repository's name. The
[engine](../reference/glossary.md) (the forge itself, as you cloned
it) does not track a project and cannot guess which one you mean. You
select the project by naming it, with `/forge <project-slug>`, before
any work. The job in full is
[Bring in an existing project](../use/bring-in-an-existing-project.md).

## What you do

Five acts, in this order. Four are typed to Claude, which you start
from the engine root (the folder you cloned the forge into). One is
typed in your own terminal.

| Step | Where | What you type |
|---|---|---|
| 1 | Claude | `/new-project my-idea` |
| 2 | Claude | your brief, pasted, and the word that it is finished |
| 3 | Claude | `/forge intent`, and `write` at the end of the round |
| 4 | your own terminal, at the engine root | `git -C projects/my-idea init -b main` |
| 5 | Claude | `/save` |

`my-idea` is a placeholder slug. Yours is lowercase, with hyphens and
no spaces.

## What happens

### 1. Scaffold the project

Type `/new-project my-idea`. Claude creates the folder
`projects/my-idea/` from the templates. Among what it creates:

- `project.md` (the project file): the slug, the kind and the
  language of the project.
- `decisions.md`, with no record in it yet.
- The folders `sources/`, `research/`, `reviews/`, `challenges/`,
  `threads/` and `recipes/`.

The language is the one the brief, the intent and what follows them
are written in. It is English by default. Name another and the
project takes it. Claude asks when your words leave it open.

The command writes files only: it never touches git. The job in full
is [Start a project](../use/start-a-project.md).

You should now see the folder `projects/my-idea/` with `project.md`
in it, and Claude asking you to paste or dictate the brief.

### 2. Paste the brief and say it is finished

A [brief](../reference/glossary.md) is your idea as you put it: the
text the intent is mined from. Paste it whole when Claude asks. A
sample of the shape, invented and taken from no project:

```
Our weekly status meeting takes ninety minutes and decides little.
Most of the time goes to updates everyone could have read beforehand.
I want a meeting of half an hour that ends with decisions.
I do not know yet what should happen to the updates.
Whoever runs the meeting next should be able to start from this alone.
```

Claude stores the text word for word in
`projects/my-idea/00-brief.md`, with its history file beside it, and
asks whether it is finished. Say that it is. That word approves the
brief at once. Without it the brief stays a draft.

Claude then proposes `/forge intent` and reminds you that the project
is not under git until you initialise its repository. That line is a
fact, not an error: a new project starts outside git, and step 4
changes it.

You should now see `00-brief.md` in `projects/my-idea/`, holding your
text as you pasted it, and Claude proposing `/forge intent`.

### 3. Forge the intent

Type `/forge intent`. The [intent](../reference/glossary.md) is the
document your brief is mined into. The project has no intent yet.
Claude therefore consolidates the brief into the first one.

It works through an interview:

- One question per message.
- Your answer is acknowledged before the next question is asked.
- One theme at a time.

Nothing is written while the interview runs. What you agree is
carried in the conversation, and Claude says that it is nowhere yet.
When the [round](../reference/glossary.md) (the stretch of
conversation that ends in one write) looks finished, Claude offers
the word `write`. Type `write`. Claude restates the whole round and,
on your yes, writes everything carried as one round. It ends by
naming what changed and what stays open.

The job of iterating the intent in full is
[Forge the intent](../use/forge-the-intent.md).

You should now see `10-intent.md` in `projects/my-idea/`, and Claude
naming what changed and what stays open.

### 4. Initialise the project's repository, in your own terminal

This is the one act of the sitting outside Claude. It is a one-off
act, and Claude is not allowed to run it: Claude writes nothing into
git itself. Open your own terminal at the engine root and type:

```
git -C projects/my-idea init -b main
```

The project is now a git repository of its own, which the engine does
not track. A remote is optional, and adding one is your act as well.

You should now see the project named with its branch, `main`, at the
next save, and no longer as "not under git".

### 5. Save

Type `/save`. The save has three parts, in this order:

1. The [light check](../reference/glossary.md) (the check a save runs
   before it commits). Claude settles what the check reports. A save
   never waits on a [finding](../reference/glossary.md) (a result of
   the check) that you have not asked to fix.
2. The commit message. Claude drafts one line in English that
   summarises the round and proposes it to you. The commit carries
   the wording you confirm or adjust.
3. The commit and the push, on whatever branch is checked out. They
   are made by the script `scripts/forge-save.py`.

A save that commits nothing names its cause. What a save does and
asks beyond this is [Save your work](../use/save-your-work.md).

You should now see the summary of the files in the commit, printed by
the script.

## What you have afterwards

- `projects/my-idea/`: a git repository of its own, on the branch
  `main`. The engine does not track it.
- `00-brief.md`: your brief, word for word, approved.
- `10-intent.md`: the first intent, written in one round.
- The first commit of the project.

The engine cannot guess which project you mean. In a later sitting
you select it by naming it before any work: `/forge my-idea`.

## If something goes wrong

- **`/new-project` stops: `projects/my-idea/` already exists.**
  Claude stops and reports. The command never overwrites a folder.
- **Claude says the project is "not under git".** This is a fact, not
  an error, until step 4 is done. A save names such a project when it
  has changes and otherwise leaves it alone.
- **`/save` commits nothing: no repository.** The project is not
  under git. Do step 4 in your own terminal and save again.
- **`/save` commits nothing: no git identity for the host.** Git has
  no name and e-mail to sign commits on this machine. The login that
  cloned a repository is a different thing. The save commits nothing
  until git resolves an identity, and the forge writes none. The
  usual causes and the ways out are in the identity step of the
  setup: [Set up the forge](setup.md).
- **`/import-project` stops: the target folder already exists.** The
  target is `projects/<repository name>`, and the name falls out of
  the address. Claude stops and reports.

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

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
