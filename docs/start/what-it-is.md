---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: c012f49353d10435
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
into a chain of versioned documents. This page says what it is in
plain words, before anything is installed. It is for anyone who
wants to use it and for anyone who wants to judge whether it is
worth using.

## What it is

Forge of Thought takes an idea of any kind and works it into a chain
of versioned documents, under review by AI reviewers that never saw
the conversation. It runs in Claude Code, an AI assistant started
from the command line. Two roles work in it:

- the principal: the person whose thinking is being forged, who
  supplies the ideas, the answers and the decisions, and who has the
  final word on all content;
- Claude: the principal's cognitive extension, which keeps the
  structure, the order and the discipline of the process, and which
  proposes but never decides.

Anyone can be the principal. The subject is deliberately left open:
process redesign, platform initiatives, organisational topics, or
anything else. The same machinery that forges a platform assignment
would forge the story of a role-playing campaign and the materials
for the one who runs it.

Technically it is an engine kept in a git repository, which runs in
Claude Code and is bound to no domain.

## How it works

One person starts from a rough brief: the principal's own text of
what he wants. Claude draws the thinking out by questions and works
the brief into an intent: the positions the principal holds, what he
rejected, and what is still open. Below the intent a project takes
only the layers it needs, such as an assignment, a BRD or a solution
design, and many projects end at the intent. Isolated reviewers
(agents that run apart from the working conversation and see only
the documents) attack the quality of the documents and the substance
of the thinking from different angles. Outputs for each audience are
then generated from the documents, which stay the source of truth.

A run ends where the principal is satisfied: the outcome is a
document he stands behind, and nothing further. Funding, adoption
and delivery are outside what the forge looks at.

The quickest way to see it at work before reading on is the course
page of the teaching videos, played in the browser:
<https://pche-broken-artist.github.io/forge-of-thought/videos/>.
The [Glossary](../reference/glossary.md) gives every term of the
forge in one line.

## Why

- **The name.** Thoughts are the raw material, of whatever kind, and
  the forged documents are the product. The name says thought, not
  assignment, because the chain is meant to grow layer by layer
  beyond any single kind of document.
- **Blind reviewers.** The reviewers are kept blind to the working
  conversation so that they put pressure on the thinking from
  outside it.
- **Claude proposes, the principal decides.** Every decision about
  content remains the principal's, while Claude owns the order and
  the discipline. The reason for this split is not recorded beyond
  that statement.

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
