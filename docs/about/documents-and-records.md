---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - templates/ledger.md
  - templates/decisions.md
  - projects/forge/10-intent.md
---

# About documents and records

This page explains how Forge of Thought sorts the files of a project,
why each sort behaves as it does, and why the state of a project lives
in a file and not in the conversation. It is for anyone who uses the
forge, extends it, or weighs whether to adopt it. It was put together
from `CLAUDE.md` (its sections Document kinds, Ledger and Versioning &
status), the skeletons `templates/ledger.md` and
`templates/decisions.md`, and the design positions of the forge's own
intent, `projects/forge/10-intent.md`, which give the reasons.

## Documents and artefacts

"Document" is the word for every file of a project. "Artefact" is
kept for a narrower set: the documents of the chain, the ones the
principal composes, the reviewers read and the renders are generated
from. A brief or an intent is an artefact; a ledger or a review is a
document but not an artefact.

Every document has exactly one kind, and the kind says what the
document is, who writes it, whether it is versioned and how it
behaves. The kinds fall into five groups. The full table lives on the
reference page; what follows is what each group is for.

## The five groups

**Artefacts.** The documents of the chain. They are written by the
principal with Claude, they are versioned, and between versions they
are rewritten freely. Even an assignment is not "frozen" in any way
the file would show: it is rewritten freely between approvals, and
what its recipients hold is a version reached by a link into git.

**Records.** What has happened, kept as it happened. The history of a
versioned document and the decisions of the principal are
append-only: new records are added, old ones stay. A review or a
challenge is one dated run of a reviewer and is immutable from the
moment it is created. The decisions file shows the shape of a record:
one entry per decision, numbered in the global sequence, with the
decision, the reason (including what was weighed against it) and the
date. A record is never edited; a later decision supersedes an earlier
one by a new record that names it.

**State.** Where things stand now. The ledger and the resource
indexes (the `00-INDEX.md` in every `sources/` and `research/`
directory) are written by the forge and freely rewritten. An index is
a light catalogue of what resources exist and what they are for, so
that nobody has to re-read them to know; it tracks nothing else.

**Rendering.** How outputs for an audience are made. A recipe says
how a render is made; it is versioned and iterated, but never
approved. A render is generated from its recipe, overwritten by every
new run, and never a source of truth: the artefacts stay that.

**Resources.** What comes from outside or is found out once. A source
is external input as it arrived; research is a durable answer to one
question. Both are immutable: a source from its registration,
research from its creation. A functional binary, such as a
presentation template or a graphic, counts as a source, so a
library's assets are resources without a kind of their own.

Every versioned kind, artefact and recipe alike, keeps its history in
a companion file beside it rather than in its own body.

## Why state lives in files

The forge holds that state lives in files and never only in the
conversation. The reason is that a session can be ended at any point
without loss: the next session re-orients from the ledger through
`/ledger`. For the same reason, an unfinished conversation is saved
into its thread of the intent, as a write of whatever has been agreed
so far, rather than left to live in the chat. One project per session
is the hygienic default.

## The ledger

`ledger.md` is the single source of truth for the state of a project.
Its tables cover the briefs, the documents, the renders, the
published files, the sources, the research, the dependencies, the
findings and the challenges, with a closing list of what waits on the
principal. It is freely rewritten and kept current after every
operation.

The ledger cites and never copies. Resources and dependencies are
registration only: what a resource is and is for lives in its
directory's index, not in the ledger. Under Waiting on principal, a
matter that already has an ID gets one line (the ID, a few words, its
state) while its substance stays in the thread or the record. Free
text appears only for a matter that has no ID yet, and it gets one at
the next write.

A layer below the intent that a project does not have is not missing:
the ledger gets no row for it, and `/forge` and the checks say nothing
of it.

## Immutability and corrections downstream

Reviews, challenges, sources and research are never edited: a source
from its registration, the others from their creation. This
immutability is a rule of the process, not a mechanism of git: it
holds because the forge works that way, not because the repository
enforces it.

Because these documents stay as they were, a correction does not go
back into them; corrections happen downstream. The decisions file
shows the pattern: a record is never edited, and a later decision
supersedes an earlier one by a new record that names it. A dated
reviewer run, or a source as it arrived, therefore stays what it was
on its day.

## Prose wrapped at about 72 columns

Prose in every document is hard-wrapped at about 72 columns so that
git diffs stay legible. Tables, code blocks and front-matter are
never wrapped.

## See also

- [Document kinds](../reference/document-kinds.md): the table of kinds, verbatim.
- [Ledger](../reference/ledger.md): the ledger's tables and states.
- [About versioning and history](versioning-and-history.md): the history companion of every versioned kind.
