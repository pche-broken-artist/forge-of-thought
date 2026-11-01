---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 44482e8ebd7366c5
inputs:
  - CLAUDE.md#What this workspace is
  - CLAUDE.md#Roles
  - projects/forge/10-intent.md#Essence
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0600
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - CLAUDE.md#Repository layout
---

# What Forge of Thought is

Forge of Thought is a workshop in which a thought is tempered into a
chain of versioned documents, under review by agents that never saw
the conversation that made them. This page says, in one reading,
what that thing is before you install anything: for the person who
wants to use it and for the one who wants to judge it.

## What it is

Forge of Thought is a place for forging thoughts. A thought of any
kind is the raw material: a process redesign, a platform initiative,
an organisational topic, anything. The thought travels a chain of
versioned documents, from the idea as it was first put together
onward, and every step of the chain is open to adversarial review by
isolated agents, that is, reviewers that read the documents and
nothing of the working conversation.

The forge runs in Claude Code, Anthropic's agent for the command
line. Its slash commands, skills, agents and hooks are the forge's
mechanisms; the forge is what they are told.

Two roles meet in it. The principal is the person whose thinking is
being forged: he supplies the ideas, the answers and the decisions,
and he is the final authority on all content. Claude is the
principal's cognitive extension: it owns structure, order, process
discipline and document hygiene, and it proposes but never decides.
Anyone can be the principal, and the recipients of what the forge
produces may be teams, colleagues or the principal's future self.

Technically, Forge of Thought is a git repository of slash commands,
isolated agents, templates, scripts and conventions, bound to no
domain.

## How it works

One person starts from a rough [brief](../reference/glossary.md)
and works it, by interview, into an
[intent](../reference/glossary.md): the document that holds the
positions the principal currently stands behind. Below the intent
the project takes the layers it needs, such as an assignment, a
business requirements document or a solution design, and many
projects end at the intent. The chain ends where the project needs
it to, and a run of the forge ends where its owner is satisfied: the
outcome is a document the principal stands behind, nothing further.

Along the way the principal has the thinking attacked by blind
reviewers, agents that are deliberately kept from seeing the
conversation and so press on the documents from different angles.
From the documents, outputs for every audience are generated: a
pitch, a summary, a picture, a README. Nothing is implemented in the
forge; it specifies.

The forge is cloned, not copied: it is a git repository, and its
scripts refuse an engine that is not one.

## Why

The name says thought, not assignment. The forge was built with the
whole chain in view, from a raw idea to a specification ready for
realisation, so that an assignment is one place a chain may end and
not its goal. Thoughts are the raw material, of whatever kind, and
nothing is presumed about them.

The reviewers are deliberately blind to the working conversation.
They provide adversarial pressure from different angles. Why
blindness is the way to that pressure is not recorded.

The mechanics are domain-agnostic. The same machinery that forges a
platform assignment would forge the story of a game campaign, with
the materials rendered for its game master. Sponsorship, funding,
adoption and delivery are outside the forge's scope and outside its
sight.

## See it at work

Before reading on, watch the teaching videos on their course page,
https://pche-broken-artist.github.io/forge-of-thought/videos/. Each
video is played in the browser and shows one job of the forge: a
brief found by questions, a list settled one item at a time, a
critic's findings walked, a check at a save, a challenger attacking
the substance, the history of one item, a new layer of the chain,
and a research planned before it is run.

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
