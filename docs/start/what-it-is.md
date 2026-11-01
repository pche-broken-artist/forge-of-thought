---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: f3636551169b49d7
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
into a chain of versioned documents, under review by agents that never
saw the conversation. This page says what it is in plain words, for
anyone who wants to know before installing anything and for anyone
weighing whether it fits.

## What it is

Forge of Thought runs in Claude Code, Anthropic's AI assistant for the
command line. The person who uses it is the principal: the one whose
thinking is being forged. The principal supplies the ideas, the answers
and the decisions, and has the final word on all content. Claude acts
as the principal's cognitive extension. It owns structure, order and
the discipline of the process. It proposes and never decides.

The name says what the system works on. Thoughts are the raw material,
of whatever kind, and nothing is presumed about them. The forged
documents are the product.

## How it works

One person starts from a rough brief: a short text of what is wanted
and why. Claude works it with the principal into an intent, by
interview: questions that draw out what the principal has not yet put
into words. Below the intent, a project takes the layers of documents
it needs, and many projects end at the intent. A run ends where the
principal is satisfied: the outcome is a document the principal stands
behind, nothing further.

Along the way the thinking is attacked by isolated reviewers. Each is a
subagent (a separate run of Claude with its own brief) that is
deliberately blind to the working conversation and reads only the
documents. From the documents, outputs for every audience are
generated, such as a pitch or a summary, while the documents stay the
source of truth.

Technically, Forge of Thought is a git repository of slash commands,
isolated agents, templates, scripts and conventions. It is bound to no
domain: the same machinery that forges a platform initiative would
forge the story of a role-playing campaign and the materials for the
one who runs it.

## Why

The reviewers are blind to the conversation so that they bring
adversarial pressure from different angles. The chain ends where the
project needs it to, because a project takes only the layers it needs.
The subject matter is deliberately unconstrained, because anyone can be
the principal and the recipients may be teams, colleagues or the
principal's own future self.

To see the forge at work before reading on, the course page of the
teaching videos plays them in the browser, together with a set of
short clips: https://pche-broken-artist.github.io/forge-of-thought/videos/

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
