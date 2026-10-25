---
project: forge
render: contributing
generated: 2026-10-25
recipe: recipes/contributing.md v0.4
inputs:
  - projects/forge/10-intent.md v6.0
  - CLAUDE.md
  - docs/README.md v5.34
---

# Contributing to Forge of Thought

Thank you for wanting to help with the forge. What I want most is
your feedback and your ideas; a finished change is welcome too. I
wrote the forge alone, and I read every word you send me.

## Before you start

To say something, you need a GitHub account. A free one is enough,
and nothing else is needed. If you have not run the forge yet, a
start is made in three pages: [install what the forge
needs](docs/start/install.md), [set it up](docs/start/setup.md) and
[get a first result](docs/start/first-result.md). If something goes
wrong on the way, tell me which of these pages you followed.

## Find your way

The documentation lives in [docs/](docs/README.md): pages of one
topic each, generated from the engine as it stands. If you use the
forge, begin with [What Forge of Thought is](docs/start/what-it-is.md);
if you want to extend it, with [What the forge is made
of](docs/extend/what-it-is-made-of.md); if you are weighing it up,
with [What the forge is and is not](docs/about/what-it-is-and-is-not.md).
If you want to change something, read [What the forge is made
of](docs/extend/what-it-is-made-of.md) and [Make a change to the
forge](docs/extend/how-a-change-is-made.md) first. Every page stands
on its own, so start where your question is.

## Tell me what you found

Tell me what worked, what did not, what was missing and where you got
lost. This is the thing that helps the forge most.

The place for it is Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions

On the repository's page, click the Discussions tab at the top, then
"New discussion", and pick the category that fits. If you pick the
wrong one, no harm is done: I move it.

## Something is broken

A command does something other than it says, a file is missing, a
link is dead. The place for that is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues

On the repository's page, click the Issues tab at the top, then "New
issue". Please fill in:

- what you ran,
- what you expected,
- what happened,
- the version of the forge you run (the top section of
  `RELEASE-NOTES.md`),
- your operating system.

Everything you post in Discussions and Issues is public. Leave out
names, company content and anything of a project that is not yours
to show. For that, there is the private way at the end of this page.

## You have an idea

An idea needs nothing but itself: no plan, no code, no proof. Bring
it to Discussions, as above. I either take it into the intent, the
document where the forge says what it wants and why, or I tell you
why not.

## You want to send a change

There are two kinds of change, and the line between them is what the
change does, never how big it is. A change of how the forge behaves,
a command, a rule, a convention, what a reviewer looks for, goes
through the chain of documents first. A change that alters no
behaviour, a wording, a broken path, a slip, does not: send the pull
request as it is, and nothing else is needed.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine I decide. The forge is built
the way it asks its users to build: what is wanted and why is written
down before anything is made, so that a change can be judged by its
reason and not only by its code. That is why a change of behaviour
starts in the chain and not in a script.

Such a pull request carries:

- the position in `projects/forge/10-intent.md`, the intent, saying
  what is wanted and why, with its record in the history beside it
  (`projects/forge/10-intent.history.md`);
- where the change solves something, the item in
  `projects/forge/40-solution-design.md`, the solution design, which
  says how the things wanted are realised;
- the change itself;
- one line on what you ran.

It does not carry a release, or a regenerated README, release notes
or documentation: I make those at the next release. A brief, your
own short text of what you want, may come first, and need not.

The easiest way is to open a discussion first, and we talk it
through. The forge's own commands do the work of the chain for you:
`/forge intent forge` walks you through the intent of the forge
itself.

### The way to a pull request

If you have never sent one, these are the steps:

1. Fork the repository on GitHub: the "Fork" button on its page
   makes your own copy.
2. Clone your fork as your engine, the same way
   [the install page](docs/start/install.md) clones the public one,
   with your fork's address in its place.
3. Work through the forge: `/forge intent forge` for a change of
   behaviour.
4. Run `/save`, which commits and pushes to your fork.
5. On your fork's page on GitHub, click "Contribute", then "Open pull
   request".

If you are unsure at any step, stop at a discussion and tell me what
you want. I make the change.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are renders: they are
generated from a recipe, a file that says what goes into the output
and how, and they are never edited by hand. A change goes into the
recipe in `projects/forge/recipes/`, or into what the recipe reads.
The pages of `docs/` are generated the same way, by `/document` from
the files that own each topic, and are never edited by hand either: a
fix goes into the file the page mirrors, as [Change a documentation
page](docs/extend/change-a-documentation-page.md) explains.

## Try it first

Try your change yourself before you send it. If you wrote it with an
AI, that is welcome on the same rule: run it, and say in the pull
request what you ran.

## Privately

For anything that should not be public, write to me. My contacts are
on my profile: https://github.com/pche-broken-artist
