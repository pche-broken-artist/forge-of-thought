---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 968694d87d634a38
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

Forge of Thought is a workshop in which a thought is tempered into
a chain of versioned documents, under review by agents that never
saw the conversation. This page says in a few plain sentences what
that means, for a reader who has installed nothing yet and wants to
know whether to read on.

## What it is

Forge of Thought is a place for forging thoughts: a workshop where a
thought is tempered and shaped. Any idea can enter it, a process
redesign, a platform initiative, an organisational topic, anything.
The idea travels a chain of versioned documents, from the idea put
together onward, and each document of the chain is reviewed by
isolated reviewers: agents that never see the working conversation
and attack the thinking from different angles. The forge runs in
Claude Code, Anthropic's agent for the command line. Its slash
commands, its skills, its agents and its hooks are the forge's
mechanisms, and the forge is what they are told. The person who
uses it is the principal: whoever's thinking is being forged. The
principal supplies the ideas, the answers and the decisions, and is
the final authority on all content. Claude is the principal's
cognitive extension: it owns structure, order, process discipline
and document hygiene, proposes, and never decides. The forge is not
tied to one person or one management relationship. Anyone can be
the principal, and the recipients of what the forge produces may be
teams, colleagues, or the principal's future self.

Technically, Forge of Thought is a git repository of slash commands,
isolated agents, templates, scripts and conventions, bound to no
domain.

## How it works

One person starts from a rough [brief](../reference/glossary.md),
a few sentences of what he wants. Claude works the brief into an
intent by interview: Claude asks, the principal answers, and the
intent grows from the answers. Below the intent the project takes
the layers it needs, and many projects end at the intent. The chain
grows layer by layer, and a layer is added without reworking
anything that exists. Along the way the principal has the thinking
attacked by reviewers that never saw the conversation. Outputs for
every audience are generated from the documents of the chain, so
that the documents stay the one source of truth. Nothing is
implemented in the forge: it specifies. A run ends where the
principal is satisfied. The outcome is a document the principal
stands behind, nothing further.

The quickest way to see all this is the course page of the teaching
videos, <https://pche-broken-artist.github.io/forge-of-thought/videos/>:
videos played in the browser, each showing one piece of the forge at
work, from a brief found by questions to a critic and its findings;
what the videos are made of is said in
[The screenplay and its player](../about/the-screenplay-and-its-player.md).
It is the place to see the forge at work before reading on.

## Why

The name says thought, not assignment. Thoughts are the raw material,
of whatever kind, and nothing is presumed about them. Forged
documents are the product, an assignment among them. The name was
chosen with the whole chain in mind, from a raw idea to a
specification ready for realisation.

The reviewers are deliberately blind to the working conversation.
Blind, they provide adversarial pressure from different angles,
which a reader of the conversation could not.

The mechanics of the chain are domain-agnostic. The same machinery
that forges a platform assignment would forge a tabletop game
campaign: an intent of the story, then materials rendered for the
game master. Sponsorship, funding, adoption and delivery outcomes are
outside the forge's scope and outside its sight.

## See also

- [Install what the forge needs](install.md): what must be on the
  machine and how it gets there.
- [What the forge is and is not](../about/what-it-is-and-is-not.md):
  the longer explanation of what the forge is, is not, and why.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what the teaching videos are made of and where they are played.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
