---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 2928724f2fa6a5bb
inputs:
  - CLAUDE.md#Document kinds
  - templates/decisions.md
  - projects/forge/10-intent.md#POS.1080
  - projects/forge/10-intent.md#POS.0160
  - projects/forge/10-intent.md#POS.0320
  - projects/forge/10-intent.md#POS.0330
  - projects/forge/10-intent.md#POS.0550
---

# Documents and records

A document is any file of a project, and every document has exactly
one kind. This page explains the kinds a project holds, how they are
grouped, and why the state of a project lives in files. It is for
anyone who uses the forge, extends it or evaluates it. The full table
of kinds is on [Document kinds](../reference/document-kinds.md); this
page explains it and does not repeat it.

## What it is

"Document" is the word for every file of a project. "Artefact" is
kept for one narrower thing: the documents of the chain (the
versioned documents a thought travels through in a project). An
artefact is a document the principal composes, the reviewers read
and the renders are generated from. The principal is the person
whose thinking is being forged. Terms of the forge are each given in
one line in the [Glossary](../reference/glossary.md).

The kind of a document says four things about it:

- what it is;
- who writes it;
- whether it is versioned;
- how it behaves once it exists.

The kinds fall into six groups.

- **Artefacts:** the documents of the chain. The principal writes
  them with Claude, they are versioned, and they are rewritten
  freely.
- **Records:** what happened, kept so that it can be read later.
  The history of a versioned document and the decisions of the
  principal are append-only. A review and a challenge are each one
  dated run of a reviewer agent (a subagent: a separate Claude that
  sees nothing of the working conversation), and they are immutable.
- **State:** where the project stands. The ledger is made at read
  time by a script. The project file (slug, kind, language) is
  written once, when the project is created. A thread holds one open
  matter of the intent: it is rewritten freely while open and
  immutable once closed. An index catalogues a resource directory
  and is rewritten freely. The documentation map holds one entry per
  page of the documentation and is rewritten by the documentation
  run.
- **Rendering:** how outputs for an audience are made. A recipe says
  how a render is made; it is versioned and iterated but never
  approved. A render and a page of the documentation are generated,
  overwritten on every run, and never a source of truth.
- **Work:** an output of the project made with work of its own. The
  file holds the content and a specification beside it holds the way
  and the why. It is explained on
  [The work product](the-work-product.md).
- **Resources:** what comes from outside or is found out once. A
  source is external input as it arrived. A research note is the
  durable answer to one question. Both are immutable.

## How it works

Each kind behaves in one of a few ways.

- **Rewritten freely:** the file shows only its current state.
  Artefacts work this way between versions.
- **Append-only:** new entries are added at the end and old ones are
  never changed. The history and the decisions work this way.
- **Immutable:** once created, the file is never edited.
  Corrections happen downstream. Reviews, challenges and research
  are immutable from their creation, and a source from its
  registration.
- **Generated:** the file is made again from its inputs and never
  edited by hand. Renders, pages and the ledger work this way.

Every versioned kind keeps its history in an append-only companion
file beside it, never in its own body. How versions and histories
work is explained on
[Versioning and history](versioning-and-history.md).

A decision record has a fixed shape. One record is written per
decision of the principal, numbered in the global sequence of IDs,
newest last. A record is never edited. A later decision that changes
it is a new record that names the old one. Each record carries the
decision, its reason including what was weighed against it, and its
date. A decision that rules on a finding or a challenge also carries
one verdict line for each ID it rules on.

The ledger is the single source of truth for the state of a project,
made by a script from the other files and never written by hand; what
it is made from is explained on
[The ledger, made from the records](the-ledger.md). The ledger cites
and never copies: the substance of a matter stays in its thread or
its record. An unfinished conversation is saved into its thread,
never into the ledger.

The documentation map and the pages generated from it are explained
on [The documentation](the-documentation.md). The map is state of
the project that owns the documentation and is never shown to the
reader of the pages.

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

The kinds exist so that one place says what any file is. The kind
decides what a document is, who writes it, whether it is versioned
and how it behaves. The table of kinds is the one page all of this is
read from.

"Artefact" is kept for the chain because it marks the boundary to a
render. An artefact is composed by the principal. A render is
generated from artefacts and is never a source of truth.

State lives in files, never only in the conversation. What is in a
file survives the session (one run of Claude, from start to close).
What lives only in the conversation does not survive it. The command
on [End a session](../use/end-a-session.md) says what lives only in
the conversation before a session closes.

Immutability is a process rule kept by convention, not a mechanism of
git. Git protects nothing from a commit that rewrites a file. The
rule costs nothing to keep. A mechanism would be one more layer to
maintain, and it still would not stop an edit by hand.

Prose is hard-wrapped so that the differences git shows between two
versions stay legible.

The reason the ledger is kept out of git is not recorded. The reason
the project file is written only once is not recorded. The reason
the history and the decisions are append-only rather than immutable
is not recorded.

## A worked example

A generic project, `<slug>`, after a few rounds of work might hold
these files, each named with its group:

```
projects/<slug>/
  <artefact>.md               artefact: rewritten freely
  <artefact>.history.md       record: its history, append-only
  decisions.md                record: append-only
  reviews/<dated report>.md   record: immutable
  challenges/<dated run>.md   record: immutable
  research/<dated note>.md    resource: immutable
  ledger.md                   state: made at read time, never in git
```

A decision record in `decisions.md` follows the shape of the
template:

```
## DEC.NNNN — <the decision in one line>
- **Decision:** <what was decided>
- **Reason:** <why, including what was weighed against it>
- **Date:** YYYY-MM-DD
```

If the principal later changes his mind, the old record stays as it
is. A new record is appended that names the old one and says what
now holds.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [The ledger, made from the records](the-ledger.md): what the ledger
  is made from and why nobody writes it.
- [End a session](../use/end-a-session.md): the command that says
  what lives only in the conversation.
- [Versioning and history](versioning-and-history.md): the history
  companion of every versioned kind.
- [The documentation](the-documentation.md): the map and the pages.
- [The work product](the-work-product.md): the work kind.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
