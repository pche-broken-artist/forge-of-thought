---
project: forge
render: contributing
generated: 2026-11-01
recipe: recipes/contributing.md v0.5
inputs:
  - projects/forge/10-intent.md v6.9
  - CLAUDE.md
  - docs/README.md
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is your
feedback and your ideas: what worked, what did not, what you would
want instead. I wrote the forge alone, and I read every word that is
sent to me.

## Before you start

To say something you need a GitHub account, and a free one is
enough. Nothing else is needed. If you have not yet run the forge,
start where the documentation starts: [install what the forge
needs](docs/start/install.md), [set it up](docs/start/setup.md) and
[get a first result](docs/start/first-result.md). A report of a
setup problem is easiest to answer when it says which of these pages
you followed. The [code of conduct](CODE_OF_CONDUCT.md) holds
everywhere the forge is talked about.

## Find your way

The documentation lives in [`docs/`](docs/README.md): pages of one
topic each, generated from the engine itself, written for three
readers. The user begins at [what Forge of Thought
is](docs/start/what-it-is.md), the extender at [what the forge is
made of](docs/extend/what-it-is-made-of.md), the evaluator at [what
the forge is and is not](docs/about/what-it-is-and-is-not.md). If
you want to change something, two pages say what you need: [what the
forge is made of](docs/extend/what-it-is-made-of.md) and [how a
change is made](docs/extend/how-a-change-is-made.md).

## Tell me what you found

Tell me what worked, what did not, what was missing and where you
got lost. A short note is as welcome as a long one. The place for it
is Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions.
On the repository's page on GitHub, open the Discussions tab at the
top, then "New discussion", and pick the category that fits best.
Choosing wrong does no harm; I move it.

## Something is broken

A command does something other than it says, a file is missing, a
link is dead: that is an issue. The place for it is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues. On the
repository's page on GitHub, open the Issues tab at the top, then
"New issue". Write it in your own words and give me these five
things:

- what you ran
- what you expected
- what happened
- the version of the forge you run: the top section of
  `RELEASE-NOTES.md` says it
- your operating system

Everything posted there is public. Leave out names, company content
and anything of a project that is not yours to show; for that there
is the private way at the end of this file. A security problem never
goes into an issue: it takes the way [`SECURITY.md`](SECURITY.md)
says.

## You have an idea

An idea needs nothing but itself: no plan, no change, no proof. Open
a discussion, the same way as above, and tell me what you would want
and why. I take it into the intent, the document that says what the
forge wants and why, or I tell you why not.

## You want to send a change

There are two kinds of change, and the line between them is what the
change does, never how big it is. A change of how the forge behaves,
a command, a rule, a convention, what a reviewer looks for, goes
through the chain first, the versioned documents a thought travels
through; the next section says how. A change that alters no
behaviour, a wording, a broken path, a slip, does not: send the pull
request as it is, and nothing else is needed.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine, I decide. The forge's own
rule is that nothing is built before it is wanted on record: the
intent says what is wanted and why, and the solution design says how
it is realised. A change of behaviour that skips them would leave
the engine doing one thing and saying another.

Your pull request carries four things: a position in
`projects/forge/10-intent.md` saying what is wanted and why, with its
record in the history beside it, `10-intent.history.md`; the item in
`projects/forge/40-solution-design.md` where the change solves
something; the change itself; and one line on what you ran. It
carries no release and no regenerated README, release notes or
documentation; I make those at the next release. A brief, a short
text of what you want and why, may come first and need not.

The easiest way is to open a discussion first, so that we agree on
what is wanted before you write a line. The forge's own commands do
the work of the chain for you: `/forge intent forge` opens the
engine's intent for your change.

### The way to a pull request

If you have never sent one, these are the steps, and nothing beyond
them:

1. Fork the repository on GitHub.
2. Clone your fork as your engine, the way
   [`docs/start/install.md`](docs/start/install.md) clones the public
   one, with your fork's address in its place.
3. Work the change through the forge: `/forge intent forge` for a
   change of behaviour.
4. `/save`: it commits and pushes to your fork.
5. On your fork's page on GitHub, "Contribute", then "Open pull
   request".

If you are unsure at any step, stop at a discussion and tell me what
you want. I make the change.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are generated and are
never edited by hand. Each is a render, an output made from a
recipe, and the recipe says what it reads and how it is written. A
change goes into the recipe in `projects/forge/recipes/` or into
what the recipe reads, and the file is regenerated. The pages of
`docs/` are generated the same way, by `/document`, from the files
that own each topic, and are never edited by hand either: a fix goes
into the file the page mirrors, as
[`docs/extend/change-a-documentation-page.md`](docs/extend/change-a-documentation-page.md)
says.

## Try it first

Try your change yourself before you send it: run it in your own
clone and see that it does what you say. A change written with an
AI is welcome on the same rule, and the pull request says what was
run.

## Privately

For anything that should not be public, write to me. My contacts are
on my profile: https://github.com/pche-broken-artist.
