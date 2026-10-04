---
project: forge
render: contributing
generated: 2026-10-04
recipe: recipes/contributing.md v0.1
inputs:
  - projects/forge/10-intent.md v4.58
  - CLAUDE.md
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is your feedback
and your ideas; a finished change is welcome too. I wrote the forge
alone and I read every word that is sent to me.

## Tell me what you found
If you have used the forge, tell me how it went: what worked, what did
not, what was missing, where you got lost. You do not need a proposal
or a fix. What happened to you is enough, and it is what I learn from
most.

The place for it is Discussions:
https://github.com/pche-broken-artist/forge-of-thought/discussions

## Something is broken
A command does something other than it says. A file is missing. A link
is dead. Tell me three things: what you ran, what you expected, and
what happened.

The place for it is Issues:
https://github.com/pche-broken-artist/forge-of-thought/issues

## You have an idea
An idea needs nothing but itself. You do not have to work it out, and
you do not have to know how it would be built. Write it down in
Discussions, the same place as above.

What happens to it then: what enters the forge is my decision. Either
I take your idea into the intent, the document that says what the
forge is wanted to do and why, or I tell you why not.

## You want to send a change
There are two kinds of change, and the line between them is drawn by
what the change does, never by how big it is.

A change of how the forge behaves is one kind: a command, a rule, a
convention, what a reviewer looks for. It goes through the chain, the
forge's own versioned documents, before it is built. The next section
says how.

A change that alters no behaviour is the other kind: a wording, a
broken path, a slip. Send the pull request as it is. Nothing else is
needed.

### A change of how the forge behaves
The forge is run through its own process: what it does is first
written down as something wanted, with the reason, and only then
built. A change that arrives without that leaves me with something
built and nowhere it says what was wanted or why.

So a pull request that changes behaviour carries three things:

- The position in `projects/forge/10-intent.md`, the intent, saying
  what is wanted and why. With it comes its record in the history
  beside it, `projects/forge/10-intent.history.md`, which says what
  changed and for what reason.
- The item in `projects/forge/40-solution-design.md`, the solution
  design, which is the document that says how the things wanted are
  realised. This one is needed where your change solves something.
- The change itself.

A brief, a short text of what you want and why, may come first. It
need not.

The easiest way is to open a discussion before you write anything. We
can settle there what is wanted, and you save yourself work that might
not fit. The forge's own commands do this work with you: `/forge
intent forge` takes you through the intent.

### A change of a document
Three files in the root of the repository are renders, outputs
generated from the forge's documents: `README.md`, `RELEASE-NOTES.md`
and this file. They are never edited by hand. Each is made from its
recipe, the file that says what the render reads, who it is for and
what shape it has.

If you want to change one of them, change its recipe in
`projects/forge/recipes/`, or change what the recipe reads. The file
is then generated again from there. A pull request that edits the
generated file directly would be overwritten at the next render.

## Try it first
Please try your change yourself before you send it. Run it, see that
it does what you meant, and say in the pull request what you ran.

A change written with an AI is welcome on the same rule. You tried it
yourself, and the pull request says what was run.

## Privately
For anything that should not be public, write to me. My contacts are
on my profile: https://github.com/pche-broken-artist
