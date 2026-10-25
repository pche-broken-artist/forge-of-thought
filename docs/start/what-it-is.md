---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 545d890a98618360
inputs:
  - CLAUDE.md#What this workspace is
  - CLAUDE.md#Roles
  - projects/forge/10-intent.md#Essence
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0600
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
---

# What Forge of Thought is

Forge of Thought is a workshop where a thought is tempered and shaped
into a chain of versioned documents. This page says in a few lines
what it is before you install anything. It is for someone who wants
to use the forge and for someone who is weighing whether to.

## What it is

Forge of Thought runs in Claude Code, which is Anthropic's assistant
that you start from the command line. Any idea can go through it:
a process redesign, a platform initiative, an organisational topic,
or something with no delivery at all, such as the story of a game
campaign. The idea travels a chain of versioned documents, and
reviewers that never saw the working conversation attack it on the
way.

Two roles share the work:

- The principal: the person whose thinking is forged. The principal
  supplies the ideas, the answers and the decisions, and has the
  final word on all content. Anyone can be the principal.
- Claude: the principal's cognitive extension. It owns structure,
  order, process discipline and the hygiene of the documents. It
  proposes and never decides.

Technically the forge is a git repository that holds what Claude
works with: isolated reviewer agents, scripts and the rules of the
process. It is bound to no domain. The same machinery that forges a
platform initiative would forge a game campaign.

## How it works

One person starts from a rough brief, the first statement of what
is wanted. Claude works the brief into an intent by asking questions
one at a time. The intent is the trunk of the chain: the positions
the principal holds, the directions rejected and the matters still
open. The terms are explained in one line each in the
[Glossary](../reference/glossary.md).

Below the intent a project takes the layers it needs, such as an
assignment, a BRD or a solution design. Many projects end at the
intent. A run of the forge ends where the principal is satisfied:
the outcome is a document the principal stands behind, and nothing
further.

Along the way the principal can have the thinking attacked by
reviewers that see only the documents. From the documents Claude
then generates outputs for each audience, such as a deck or the
materials a game master needs. The documents stay the source of
truth.

The longer explanation of what the forge is, what it is not and why
is [What the forge is and is not](../about/what-it-is-and-is-not.md).

## Why

The reviewers are kept blind to the working conversation. They
provide adversarial pressure from different angles.

The name says thought, not assignment. Thoughts of any kind are the
raw material, and the forged documents are the product. An
assignment is one of those documents and one place a chain may end,
not its goal.

## See the forge at work

The teaching videos are short pieces played in the browser on the
course page,
<https://pche-broken-artist.github.io/forge-of-thought/videos/>.
They are the place to see the forge at work before you read on.
What the videos are made of and where they are played is explained
in [The screenplay and its player](../about/the-screenplay-and-its-player.md).

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
