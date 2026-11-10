---
project: forge
render: contributing
generated: 2026-11-10
recipe: recipes/contributing.md v0.11
inputs:
  - projects/forge/10-intent.md v7.7
  - CLAUDE.md
  - docs/README.md
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is your
feedback and your ideas: what worked for you, what did not, and what
you wish the forge did. I wrote the forge alone, and I read every word
you send me.

## Before you start

To say something, you need a GitHub account, and a free one is
enough. Nothing else is needed. If you are still getting started, the
pages for that are here: [Install what the forge
needs](docs/start/install.md), [Set up the forge](docs/start/setup.md)
and [Get a first result](docs/start/first-result.md). If something
goes wrong there, tell me which page you followed. The [code of
conduct](CODE_OF_CONDUCT.md) holds everywhere the forge is talked
about.

## Find your way

The [documentation](docs/README.md) lives in `docs/`: pages of one
topic each, generated from the engine as it stands. If you use the
forge, begin with [What Forge of Thought is](docs/start/what-it-is.md);
if you want to extend it, with [What the forge is made
of](docs/extend/what-it-is-made-of.md); if you are weighing it up,
with [What the forge is and is not](docs/about/what-it-is-and-is-not.md).
Before you change something, read [What the forge is made
of](docs/extend/what-it-is-made-of.md) and [Make a change to the
forge](docs/extend/how-a-change-is-made.md).

## Tell me what you found

Tell me what worked, what did not, what was missing, and where you
got lost. Small things count too. The place for this is Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions

To get there, open the repository's page on GitHub, click the
Discussions tab at the top, then "New discussion". Pick the category
that fits. If you pick the wrong one, it does no harm: I move it.

## Something is broken

A command does something other than it says, a file is missing, a
link is dead. The place for this is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues

To get there, open the repository's page, click the Issues tab at the
top, then "New issue". Fill in this short list:

- what you ran,
- what you expected,
- what happened,
- the version of the forge you run (the top section of
  `RELEASE-NOTES.md`),
- your operating system.

Everything posted there is public. Leave out names, company content
and anything of a project that is not yours to show; for that, use
the private way at the end of this file. A security problem never
goes into an issue: it takes the way [SECURITY.md](SECURITY.md) says.

## You have an idea

An idea needs nothing but itself: no plan, no code, no polish. Bring
it to Discussions, the same way as above. I either take it into the
intent, the document where the forge says what it wants and why, or I
tell you why not.

## You want to send a change

There are two kinds of change, and what tells them apart is what the
change does, never how big it is. A change of how the forge behaves,
a command, a rule, a convention, what a reviewer looks for, goes
through the chain of documents first. A change that alters no
behaviour, a wording, a broken path, a slip, does not: send the pull
request as it is, with one sentence saying what it fixes, and nothing
else is needed.

For both kinds, a pull request carries one matter and whatever that
matter needs, never several unrelated changes. A second matter goes
in a second pull request, so that each can be judged, merged or
declined on its own.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine, I decide. The forge is built
on its own rule: what it should do is written down before it is
built. The intent says what is wanted and why, and the solution
design, `projects/forge/40-solution-design.md`, says how it is
realised; so a change of behaviour starts as a position in the intent.

Such a pull request carries:

- the position in `projects/forge/10-intent.md` saying what is
  wanted and why, with its record in the history beside it,
  `projects/forge/10-intent.history.md`;
- the item in the solution design, where the change solves something;
- the change itself;
- a description, in plain words, of what it changes and why, item by
  item, and of what you ran, so that I can judge it without reading
  the change line by line. A pull request without it is sent back to
  be described. A script in `scripts/` is changed together with its
  test in `tests/`, run by `/test` or `python -m pytest`, and the
  description says what was run.

The forge's own project is a repository of its own, beside the
engine. When your change touches both, send two pull requests: one on
the engine with the change itself, one on the forge's own project
with the position and the design item, each naming the other. Git
cannot merge two repositories as one, so I merge both or neither, in
one sitting, the project first and the engine second, with no release
between them. If one of them is declined, both are closed, with the
reason.

A pull request does not carry a release, nor a regenerated README,
release notes or documentation: I make those at the next release. A
brief, the rough first note of an idea, may come first, and need not.
Everything that enters the forge's own project is written in English,
a brief included: the project is public and read by everyone. The
engine's rule that a brief keeps the language it was written in holds
for your own instance, not here; a brief sent in another language is
translated at the merge, and its original stays in git.

The easiest way is to open a discussion first. The forge's own
commands do the work of writing the position: `/forge intent forge`.

### The way to a pull request

If you have never sent one, these are the steps:

1. On GitHub, fork the repository.
2. Clone your fork as your engine, the way
   [Install what the forge needs](docs/start/install.md) clones the
   public one.
3. Clone the forge's own project beside your engine, since a change
   of behaviour is recorded there:
   `/import-project https://github.com/pche-broken-artist/forge.git`
4. Work through the forge: `/forge intent forge` for a change of
   behaviour.
5. Run `/save`, which pushes to your fork.
6. On your fork's page on GitHub, click "Contribute", then "Open pull
   request".

For a change of more than a few lines, make a branch first, `python
scripts/forge-branch.py forge <name>`, then work and `/save` on it;
the save pushes that branch to your fork, and you open the pull
request from the branch. Your fork's `main` stays clean for the
upgrades of the engine, and the branch goes away with the merge.

If you are unsure at any step, stop at a discussion. Tell me what you
want, and I make the change.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are renders: outputs
generated from the forge's documents by a recipe, a file that says
what a render reads and how it is made. They are never edited by
hand. A change goes into the recipe in `projects/forge/recipes/` or
into what the recipe reads. The pages of `docs/` are generated the
same way, by `/document` from the files that own each topic, and are
never edited by hand either: a fix goes into the file the page
mirrors, as [Change a documentation
page](docs/extend/change-a-documentation-page.md) says.

## Try it first

Try your change yourself before you send it. Run what you changed and
see that it does what you meant. A change written with an AI is
welcome on the same rule: try it, and say in the pull request what you
ran.

## Privately

For anything that should not be public, write to me; my contacts are
on my profile, https://github.com/pche-broken-artist
