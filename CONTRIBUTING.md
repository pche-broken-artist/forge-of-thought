---
project: forge
render: contributing
generated: 2026-11-19
recipe: recipes/contributing.md v0.12
inputs:
  - projects/forge/10-intent.md v7.15
  - CLAUDE.md
  - docs/README.md
---

# Contributing to Forge of Thought

Thank you for wanting to contribute. What I want most is your feedback
and your ideas; a finished change is welcome too. I wrote the forge
alone, and I read every word that is sent to me.

## Before you start

To say something you need a GitHub account, and a free one is enough.
Nothing else is needed.

A start with the forge is made on three pages of `docs/start/`:
[Install what the forge needs](docs/start/install.md),
[Set up the forge](docs/start/setup.md) and
[Get a first result](docs/start/first-result.md). If a step there does
not work for you, tell me which page you followed.

The [code of conduct](CODE_OF_CONDUCT.md) holds everywhere the forge is
talked about.

## Find your way

The documentation is in [`docs/`](docs/README.md): pages of one topic
each, generated from the engine, which is this repository. It is
written for three readers, and each has a page to begin at: the user,
who works with the forge, at
[What Forge of Thought is](docs/start/what-it-is.md); the extender, who
adds to it, at
[What the forge is made of](docs/extend/what-it-is-made-of.md); the
evaluator, who wants to understand it without running it, at
[What the forge is and is not](docs/about/what-it-is-and-is-not.md).
If you want to change something, two pages say what the forge is made
of and how a change is made:
[What the forge is made of](docs/extend/what-it-is-made-of.md) and
[Make a change to the forge](docs/extend/how-a-change-is-made.md).

## Tell me what you found

Tell me what worked, what did not, what was missing and where you got
lost. A few plain sentences are enough.

How to get there: on the repository's page, open the Discussions tab
at the top and press "New discussion". Pick the category that fits.
Choosing the wrong one does no harm, since I move it.

The channel is Discussions,
https://github.com/pche-broken-artist/forge-of-thought/discussions.

## Something is broken

A command does something other than it says, a file is missing, a link
is dead: that belongs in an issue. On the repository's page, open the
Issues tab at the top and press "New issue". Write these five things
in it:

- what you ran
- what you expected
- what happened
- the version of the forge you run (the top section of
  `RELEASE-NOTES.md`)
- your operating system

Everything you post, in a discussion or in an issue, is public: no
names, no company content, nothing of a project that is not yours to
show. For that, there is the private way at the end of this page.

A security problem never goes into an issue: it takes the way
[SECURITY.md](SECURITY.md) says.

The channel is Issues,
https://github.com/pche-broken-artist/forge-of-thought/issues.

## You have an idea

An idea needs nothing but itself. You do not have to know how it would
be built. Open a discussion, the same way as above. What happens to it
then: I take it into the intent, the document that says what is wanted
of the forge and why, or I tell you why not.

## You want to send a change

A change comes as a pull request, GitHub's way of offering a change to
a repository; how one is made is said below. There are two kinds of
change, and the line between them is drawn by what the change does,
never by its size.

A change of how the forge behaves, a command, a rule, a convention,
what a reviewer of the forge looks for, goes through the chain first.
The chain is the forge's own line of versioned documents, where what
is wanted is written down before anything is built. The next section
says what that means for you.

A change that alters no behaviour, a wording, a broken path, a slip,
does not go through the chain. Send the pull request as it is, with
one sentence saying what it fixes. Nothing else is needed.

For both kinds, a pull request carries one matter and what that matter
needs, never several unrelated changes. A second matter goes in a
second pull request, so that each can be judged, merged or declined on
its own.

### A change of how the forge behaves

In your own clone you decide everything, the forge there is yours;
what is merged into the public engine, I decide.

The forge is built by its own process: what it is to do is first
written down, with the reason, and only then built. A change that
lives in the engine alone would leave the forge doing one thing and
its own documents saying another.

Those documents stand in the forge's own project, a second public
repository cloned beside the engine into `projects/forge`. A pull
request for a change of behaviour carries:

- the position in `projects/forge/10-intent.md`, the item of the
  intent that says what is wanted and why, with its record in the
  history beside it, the file that keeps what changed and why;
- the item in `projects/forge/40-solution-design.md`, the solution
  design, which is the document that says how the things wanted are
  realised, where your change solves something;
- the change itself;
- a description in the pull request, in plain words, of what it
  changes and why, item by item, and of what you ran, so that I can
  judge it without reading the change line by line.

A pull request without that description is sent back to be described.
A script in `scripts/` is changed with its test in `tests/`, run by
`/test` or `python -m pytest`, and the pull request says what was run.

Where the change touches both repositories, it is two pull requests:
one on the engine with the change itself, one on the forge's own
project with the position and the design item, each naming the other.
Git cannot merge two repositories as one, so I merge both or neither,
in one sitting, the project first and the engine second, with no
release between them. If one of them is declined, both are closed,
with the reason.

What a pull request does not carry: no release, and no regenerated
README, release notes or documentation. I make those at the next
release.

A brief, a rough text of what you want and why, may come first and
need not. Everything that enters the forge's own project is written in
English, a brief included: the project is public and read by everyone.
The engine's own rule that a brief keeps the language it was written
in holds for your own work in your own clone, not here. A brief sent
in another language is translated at the merge, and its original stays
in git.

The easiest way is to open a discussion first. And the forge's own
commands do this work with you: `/forge intent forge`.

### The way to a pull request

If you have never sent one, these are the steps:

1. Fork the repository on GitHub. The fork is your own copy of it
   under your account.
2. Clone your fork as your engine, as
   [Install what the forge needs](docs/start/install.md) clones the
   public one.
3. Clone the forge's own project beside your engine, since a change of
   behaviour is recorded there:

   ```
   /import-project https://github.com/pche-broken-artist/forge.git
   ```

4. Work through the forge. For a change of behaviour that is
   `/forge intent forge`.
5. Run `/save`, which pushes to your fork.
6. On your fork's page on GitHub, press "Contribute", then "Open pull
   request".

For a change of more than a few lines, make a branch first:
`python scripts/forge-branch.py forge <name>`. Work and `/save` on it;
the save pushes that branch to your fork. Then open the pull request
from the branch. Your fork's `main` then carries no commits of your
own, and the branch goes away with the merge.

A fork does not follow the engine by itself, and the forge brings no
upgrade into it. You keep it current by hand: "Sync fork" on the
fork's page on GitHub, for each fork, and then `/pull`, which brings
the synced `main` down.

If you are unsure at any point, stop at a discussion and I make the
change.

### A change of a document

`README.md`, `RELEASE-NOTES.md` and this file are renders: documents
generated for a reader, each from its recipe, the file that says what
the render is made from and how. They are never edited by hand. A
change goes into the recipe in `projects/forge/recipes/`, or into what
the recipe reads.

The pages of `docs/` are generated too, by `/document`, from the files
that own each topic, and are never edited by hand either. A fix goes
into the file the page mirrors:
[Change a documentation page](docs/extend/change-a-documentation-page.md)
says how.

## Try it first

Try your change yourself before you send it: run it and see that it
does what you meant. A change written with an AI is welcome on the
same rule, and the pull request says what was run.

## Privately

For anything that should not be public, write to me; my contacts are
on my profile, https://github.com/pche-broken-artist
