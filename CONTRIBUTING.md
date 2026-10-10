---
project: forge
render: contributing
generated: 2026-10-10
recipe: recipes/contributing.md v0.2
inputs:
  - projects/forge/10-intent.md v5.0
  - CLAUDE.md
  - docs/README.md v5.0
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is your
feedback and your ideas; a finished change is welcome too. I wrote
the forge alone, and I read every word you send me.

## Find your way

The documentation lives in [`docs/`](docs/README.md): pages of one
topic each, generated from the engine as it stands. If you use the
forge, begin in [`docs/start/`](docs/start/) and go on to
[`docs/use/`](docs/use/) for every job. If you want to extend it,
begin in [`docs/extend/`](docs/extend/), with
[`docs/reference/`](docs/reference/) for the shapes. If you want to
judge it, begin in [`docs/about/`](docs/about/), the concept pages.
If you want to change something, two pages say
[what the forge is made of](docs/extend/what-it-is-made-of.md) and
[how a change is made](docs/extend/how-a-change-is-made.md).

## Tell me what you found

Tell me what worked, what did not, what was missing and where you
got lost. You need no proposal and no fix: what you saw is enough,
and it is the most useful thing you can send me. Write it as a
discussion:

https://github.com/pche-broken-artist/forge-of-thought/discussions

## Something is broken

A command does something other than it says, a file is missing, a
link is dead. Open an issue and tell me three things: what you ran,
what you expected, what happened. That is all I need to find it:

https://github.com/pche-broken-artist/forge-of-thought/issues

## You have an idea

An idea needs nothing but itself: no design, no change, no proof.
Write it as a discussion, in the same place as your feedback:

https://github.com/pche-broken-artist/forge-of-thought/discussions

Here is what happens to it. I take it into the intent, the document
in which I say what I want of the forge and why, and from there it
shapes what gets built. Or I say why not. What enters the forge is
my decision, and I give you the reason either way.

## You want to send a change

There are two kinds of change, and the line between them is drawn
by what the change does, never by its size. A change of how the
forge behaves, a command, a rule, a convention, what a reviewer
looks for, goes through the chain before it is built; the next
section says how. A change that alters no behaviour, a wording, a
broken path, a slip, does not: send the pull request as it is, and
nothing else is needed.

### A change of how the forge behaves

The forge is a chain of versioned documents, and the forge is itself
run through its own chain: the intent says what is wanted and why,
and the solution design, the layer below it, says how what is wanted
is realised. A change that skips the chain makes the forge do
something its own documents do not say, and from then on the two
drift apart.

So a pull request that changes behaviour carries three things: a
position in `projects/forge/10-intent.md` saying what is wanted and
why, with its record in the history beside it,
`projects/forge/10-intent.history.md`; the item in
`projects/forge/40-solution-design.md` where the change solves
something; and the change itself. A brief, a few sentences of what
you want and why, may come first, and need not.

The easiest way is to open a discussion first, before you write any
of it. And if you run the forge, its own commands do this work for
you: `/forge intent forge` takes your idea into the intent the way
the forge takes every idea.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are renders: outputs
generated from the chain for one audience each, never edited by
hand. What is iterated is the recipe, one file in
`projects/forge/recipes/` that names the inputs, the audience, the
instructions and the output template; `/render` regenerates the
file from it. So a change to one of these documents goes into its
recipe, or into what the recipe reads, and the document is made
anew.

The pages of `docs/` are generated the same way, by `/document`,
from the files that own each topic. A fix goes into the file the
page mirrors, never into the page; how to find that file is on the
page [Change a documentation page](docs/extend/change-a-documentation-page.md).

## Try it first

Try your change yourself before you send it: run the command, open
the render, read the page as it comes out. A change written with an
AI is welcome on the same rule, and the pull request says what you
ran.

## Privately

For anything that should not be public, write to me; my contacts
are on my profile, https://github.com/pche-broken-artist
