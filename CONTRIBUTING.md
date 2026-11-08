---
project: forge
render: contributing
generated: 2026-11-08
recipe: recipes/contributing.md v0.10
inputs:
  - projects/forge/10-intent.md v7.0
  - CLAUDE.md
  - docs/README.md
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is to hear how
the forge worked for you and what you would do differently: feedback
and ideas first, a finished change gladly too. I wrote the forge
alone and I read every word that is sent to me.

## Before you start

A GitHub account is the one thing you need to say something; a free
one is enough. If you have not run the forge yet, the start is in
`docs/start/`: [install what it needs](docs/start/install.md),
[set it up](docs/start/setup.md) and
[get a first result](docs/start/first-result.md). If something there
did not work, say which page you followed. The code of conduct,
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), holds everywhere the forge
is talked about.

## Find your way

The documentation lives in [`docs/`](docs/README.md): pages of one
topic each, generated from the engine as it stands. It has three
readers and each begins somewhere else: the user at
[what the forge is](docs/start/what-it-is.md), the extender at
[what the forge is made of](docs/extend/what-it-is-made-of.md), the
evaluator at
[what the forge is and is not](docs/about/what-it-is-and-is-not.md).
If you want to change something, two pages say what you will touch
and how a change is made:
[What the forge is made of](docs/extend/what-it-is-made-of.md) and
[Make a change to the forge](docs/extend/how-a-change-is-made.md).

## Tell me what you found

What worked, what did not, what was missing, where you got lost: all
of it helps, and a few sentences are enough. The place for it is
Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions.
On the repository's page click the "Discussions" tab at the top,
then "New discussion", and pick the category that fits. If you pick
the wrong one, no harm is done; I move it.

## Something is broken

A command does something other than it says, a file is missing, a
link is dead: that is an issue. The place for it is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues. On
the repository's page click the "Issues" tab at the top, then "New
issue". There is no form to fill; write the following in your own
words:

- what you ran
- what you expected
- what happened
- the version of the forge you run (the top section of
  `RELEASE-NOTES.md`)
- your operating system

Everything posted there is public. Put no names in it, no company
content, nothing of a project that is not yours to show; for that,
use the private way at the end of this page. A security problem
never goes into an issue: it takes the way
[SECURITY.md](SECURITY.md) says.

## You have an idea

An idea needs nothing but itself: no design, no plan, no change.
Open a discussion for it, the same way as above. I take it into the
intent, the document that says what the forge wants and why, or I
say why not.

## You want to send a change

There are two kinds of change, and the line between them is drawn by
what the change does, never by its size. A change of how the forge
behaves, a command, a rule, a convention, what a reviewer looks for,
goes through the forge's own chain of documents before it is built;
how is said below. A change that alters no behaviour, a wording, a
broken path, a slip, does not: send the pull request as it is, and
nothing else is needed.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine, I decide. The forge is run
through its own process: what it wants is written in its intent
before anything is built, and how the things wanted are realised is
written in its solution design. A change that skips this would be
the one change in the forge that nobody can read the reason for.

The pull request for such a change carries four things: the
position in `projects/forge/10-intent.md` saying what is wanted and
why, with its record in the history beside it,
`projects/forge/10-intent.history.md`; the item in
`projects/forge/40-solution-design.md` where the change solves
something; the change itself; and one line on what you ran. A script
in `scripts/` is changed with its test in `tests/`, run by `/test` or
`python -m pytest`, and the pull request says what was run. The
engine and the forge's own project are two repositories, so a change
that touches both comes as two pull requests, one on the engine with
the change itself, one on the forge's own project with the position
and the design item, each naming the other. Git cannot merge two
repositories as one, so I merge both or neither, in one sitting, the
project first and the engine second, with no release between them;
if one of them is declined, both are closed with the reason.

It does not carry a release, nor a regenerated README, release notes
or documentation; I make those at the next release. A brief, the
rough first statement of an idea, may come first and need not.
Everything that enters the forge's own project is written in
English, a brief included: the project is public and read by
everyone, and the engine's rule that a brief keeps the language it
was written in holds for your own instance, not here. A brief sent
in another language is translated at the merge and its original
stays in git.

The easiest way is to open a discussion first, so that we agree on
what is wanted before you write it. The forge's own commands do the
rest: `/forge intent forge` works the position into the intent with
its history record, and the solution design follows from it.

### The way to a pull request

If you have never sent a pull request, this is the whole way, in the
steps the forge and GitHub have:

1. On the repository's page on GitHub, click "Fork". You now have a
   copy of the repository under your own account.
2. Clone your fork onto your machine as your engine, the way
   [the install page](docs/start/install.md) clones the public one,
   with your fork's address in place of the public one.
3. Clone the forge's own project beside your engine:
   `/import-project https://github.com/pche-broken-artist/forge.git`.
   A change of behaviour is recorded there, and the author's commands
   read it from there.
4. Work through the forge: `/forge intent forge` for a change of
   behaviour, then the change itself.
5. For a change of more than a few lines, make a branch first,
   `python scripts/forge-branch.py forge <name>`, and work on it.
   Your fork's `main` stays clean for the upgrades of the engine, and
   the branch goes away with the merge.
6. `/save`. It commits and pushes to your fork, to the branch you are
   on.
7. On your fork's page on GitHub, click "Contribute", then "Open pull
   request", from the branch if you made one.

If you are unsure at any step, stop at a discussion and say what you
wanted to change; I make the change.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are renders: outputs
generated from the forge's documents, never edited by hand. Each is
made from a recipe, the file that says what the render is made of
and how, in `projects/forge/recipes/`. A change to one of them goes
into its recipe or into what the recipe reads, and the file is
regenerated from there. The pages of `docs/` are generated the same
way, by `/document` from the files that own each topic, and are never
edited by hand either: a fix goes into the file the page mirrors, as
[Change a documentation page](docs/extend/change-a-documentation-page.md)
says.

## Try it first

Try your change yourself before you send it: run the command, render
the file, open the page, and see that it does what you meant. A
change written with an AI is welcome on the same rule, and the pull
request says what was run.

## Privately

For anything that should not be public, write to me; my contacts are
on my profile, https://github.com/pche-broken-artist.
