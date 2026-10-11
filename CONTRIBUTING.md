---
project: forge
render: contributing
generated: 2026-10-11
recipe: recipes/contributing.md v0.3
inputs:
  - projects/forge/10-intent.md v5.3
  - CLAUDE.md
  - docs/README.md v5.3
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is to hear
what you found and what you would do differently: feedback and
ideas come first, and a finished change is welcome too. I wrote the
forge alone, and I read every word that is sent to me.

## Find your way

The documentation lives in [`docs/`](docs/README.md): pages of one
topic each, generated from the engine as it stands, for three
readers. If you use the forge, begin with
[What Forge of Thought is](docs/start/what-it-is.md); if you want to
add to it, with
[What the forge is made of](docs/extend/what-it-is-made-of.md); if
you want to understand it without running it, with
[What the forge is and is not](docs/about/what-it-is-and-is-not.md).
If you mean to change something, read
[What the forge is made of](docs/extend/what-it-is-made-of.md) and
[Make a change to the forge](docs/extend/how-a-change-is-made.md)
before you start.

## Tell me what you found

Tell me what worked, what did not, what was missing and where you
got lost. A sentence is enough; a page is welcome. There is no form
to fill in and nothing you need to have read first. The place for it
is Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions

## Something is broken

A command does something other than it says, a file is missing, a
link is dead: open an issue and tell me what you ran, what you
expected and what happened. The place for it is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues

## You have an idea

An idea needs nothing but itself: no design, no change, no proof.
Open a discussion and say what you would want the forge to do, or to
stop doing, and why, as far as you know it:
https://github.com/pche-broken-artist/forge-of-thought/discussions

What happens to it: I take it into the intent, the document in which
I say what I want of the forge and why, or I say why not. Either
way you hear from me.

## You want to send a change

There are two kinds of change, and the line between them is drawn by
what the change does, never by its size. A change of how the forge
behaves, a command, a rule, a convention, what a reviewer looks for,
goes through the chain of documents before it is built; the next
section says how. A change that alters no behaviour, a wording, a
broken path, a slip, does not: send the pull request as it is, and
nothing else is needed.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine, I decide. The forge keeps
what is wanted apart from how it is realised: the intent,
`projects/forge/10-intent.md`, says what I want and why, and the
solution design, `projects/forge/40-solution-design.md`, says how
the things wanted are realised. A change that arrives without its
place in those two cannot be read against what is wanted, and the
next change would have nothing to stand on.

So a pull request for a change of behaviour carries four things:
the position in `projects/forge/10-intent.md`, one numbered item,
saying what is wanted and why, with its record in the history
companion beside it; the item in `projects/forge/40-solution-design.md`
where the change solves something; the change itself; and one line
on what you ran. It does not carry a release, a regenerated
`README.md`, release notes or documentation: those I make at the
next release. A brief, the rough note a thought starts from, may come
first and need not.

The easiest way is to open a discussion first, before you write
anything, so that we agree on what is wanted while it is still
cheap. The forge's own commands do this work for you: `/forge intent
forge` iterates the intent of the forge in your clone, and writes
the position and its history record together.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are generated and are
never edited by hand. Each is a render, an output made from the
documents of the forge, and each has a recipe in
`projects/forge/recipes/`, the file that says what the render reads,
for whom it is made and in what shape. A change goes into the recipe
or into what the recipe reads, and the file is regenerated from it.

The pages of `docs/` are generated the same way, by `/document` from
the files that own each topic, and are never edited by hand either.
A fix goes into the file the page mirrors; how to find that file is
in [Change a documentation page](docs/extend/change-a-documentation-page.md).

## Try it first

Try your change yourself before you send it: run the command, render
the file, read the page, in your own clone, and say in the pull
request what you ran. A change written with an AI is welcome on the
same rule: you tried it, and the pull request says what was run.

## Privately

For anything that should not be public, write to me; my contacts are
on my profile, https://github.com/pche-broken-artist
