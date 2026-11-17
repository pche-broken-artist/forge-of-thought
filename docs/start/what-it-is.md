---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: d677bf13acb98966
inputs:
  - CLAUDE.md#What this workspace is
  - CLAUDE.md#Roles
  - projects/forge/10-intent.md#Essence
  - projects/forge/10-intent.md#POS.0780
  - projects/forge/10-intent.md#POS.0600
  - projects/forge/recipes/readme.md#Pinned facts (not rendered)
  - .claude/reference/repository-layout.md
---

# What Forge of Thought is

Forge of Thought is a workshop in which a thought is tempered into a
chain of versioned documents: an idea of any kind is put together in
a first document and worked from one document to the next, under
review by agents that never saw the conversation in which they were
written. This page says in a few plain sentences what the forge is,
before anything is installed. It is for a reader who is about to use
the forge and for a reader who is weighing it.

## What it is

The forge runs in Claude Code (Anthropic's agent for the command
line). The slash commands, the skills, the agents and the hooks of
Claude Code are the mechanisms of the forge, and the forge is what
they are told. Claude (an AI working here as that agent) is one of
the two roles of the forge. The other is the
[principal](../reference/glossary.md) (the person whose thinking is
forged).

The principal supplies the ideas and the answers and decides
everything about the content. The forge is not tied to one person:
anyone can be the principal. Claude is the principal's cognitive
extension. It owns the structure, the order and the discipline of
the process. It proposes and never decides.

The subject is deliberately left open: a process redesign, a
platform initiative, an organisational topic, anything. The name
says the same: thoughts are the raw material, of whatever kind, and
the forged documents are the product.

## How it works

One person starts from a rough [brief](../reference/glossary.md)
(the idea put together as a first document). With Claude that person
works the brief into an [intent](../reference/glossary.md) by
interview: Claude asks and the principal answers. The intent is the
document below which a project takes the layers it needs (further
documents of the chain, such as an assignment or a solution
design). Many projects end at the intent. Isolated AI reviewers put
the thinking under adversarial pressure from different angles. They
never saw the working conversation: they are deliberately blind to
it. Outputs for each audience are generated from the documents. The
forge calls such an output a [render](../reference/glossary.md).

A run of the forge ends where the principal is satisfied. Its
outcome is a document the principal stands behind and nothing
further. Nothing is implemented in the forge: it specifies. The
mechanics are the same for any subject. The machinery that forges a
platform assignment would forge the campaign of a role-playing
game: an intent of the story, then materials rendered for the one
who leads the game.

Technically, Forge of Thought is a git repository of slash commands,
isolated agents, templates, scripts and conventions, bound to no
domain.

The place to see the forge at work before reading on is the course
page of the teaching videos at
<https://pche-broken-artist.github.io/forge-of-thought/videos/>: each
video of the course shows one job of the forge, is made from a
[screenplay](../about/the-screenplay-and-its-player.md) render and
is played on a page in the browser.

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
