---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 8dca17e602aef097
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

Every file of a project is a document, and every document has one
kind that says what it is, who writes it and how it behaves. This
page explains the six groups those kinds fall into, why the state of
a project lives in files and never only in the conversation, and why
some documents are never edited. It is for anyone who uses the
forge, extends it or weighs it, and wants to know what the files of
a project are before opening them.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain. The chain is the series of
versioned documents a thought travels, from a brief through the
intent to whatever layers the project takes. The artefacts are the
documents the principal composes, the reviewers read and the renders
are generated from. The principal is the person whose thinking is
being forged, with final authority on all content.

Every document has exactly one kind. The kind says four things:

- what the document is;
- who writes it;
- whether it is versioned;
- how it behaves (rewritten freely, append-only, immutable, written
  once, or regenerated).

The kinds fall into six groups. The full table of kinds stands on
[Document kinds](../reference/document-kinds.md); this page explains
it and does not repeat it. Each term is also given in one line in
the [Glossary](../reference/glossary.md).

## How it works

### Artefacts

An artefact is a document of the chain, written by the principal
with Claude. It is versioned and rewritten freely between versions.
What each artefact is, its definition says. Every versioned kind
keeps its history in a companion file beside it; that companion is
explained on [Versioning and history](versioning-and-history.md).

### Records

Records say what happened, and they only grow.

- **History**: what changed in a versioned document, and why.
  Append-only.
- **Decisions**: the principal's decisions with their reasons, in
  `decisions.md`. Append-only.
- **Review and challenge**: one dated run of a reviewer agent.
  Immutable from its creation.

A decision record is never edited. A later decision supersedes it by
a new record that names the old one. Records are numbered in one
global sequence, newest last.

### State

State says where a project stands now.

- **Ledger**: the single source of truth for state. A ledger is the
  state report of one project. It is made at read time by a script
  and never kept in git.
- **Project file**: the project's slug, kind and language. Written
  once, at creation.
- **Thread**: one open matter of the intent. Freely rewritten while
  open, immutable once closed.
- **Index**: the catalogue of a resource directory. Freely
  rewritten.
- **Map**: the documentation map, one entry per page with everything
  that page is made from. Freely rewritten by the documentation run.

The ledger is made from the other files of the project and is never
written by hand; how, is said on
[The ledger, made from the records](the-ledger.md).

### Rendering

Rendering covers what is generated for a reader.

- **Recipe**: how a render is made. Versioned, iterated, never
  approved.
- **Render**: an output for one audience. Overwritten each time it
  is generated, and never a source of truth.
- **Page**: a page of the documentation, or its index. Overwritten
  by the documentation run, and never a source of truth.

The map and the pages are explained on
[The documentation](the-documentation.md).

### Work

A work product is an output of the project made with work of its
own. Its file holds the content. A specification beside it holds the
way and the why, and only the specification is versioned. The file
is remade from the specification, and the principal works with it
freely. The kind is explained on
[The work product](the-work-product.md).

### Resources

Resources come into a project from outside or from research.

- **Source**: external input as it arrived. Immutable from its
  registration.
- **Research**: a durable answer to one question. Immutable from its
  creation.

A research of several questions is a bundle. The plan and the
synthesis stand at its head, with one note per question per engine
below them. A functional binary, such as a `.potx` template or a
graphic, is a source. A library's assets are therefore resources
without a kind of their own. A library carries no artefacts and no
records, except the history companion of its recipe.

### Writing prose

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

**Why state lives in files.** What is in a file survives the
session. A session is one working conversation with Claude, from its
start to its close. What lives only in the conversation does not
survive it. An unfinished conversation is therefore saved into its
thread of the intent, as a write of whatever is agreed so far, and
never into the ledger. Before a session closes, one command says what
lives only in the conversation; it is described on
[End a session](../use/end-a-session.md).

**Why the ledger never holds a conversation.** The ledger cites the
other documents and never copies them. The reason is not recorded.

**Why "artefact" is kept narrow.** The artefacts are the documents
the principal composes, the reviewers read and the renders are made
from. The reason the word is reserved for them alone is not
recorded.

**Why immutability is a process rule.** Reviews, challenges, sources
and research are never edited. Corrections happen downstream. This
rule is kept by convention, not by git. Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain, and it still would not stop a
hand edit.

**Why prose is hard-wrapped.** Prose is wrapped at about 72 columns
so that git diffs stay legible.

**Why records are append-only.** The reason records are append-only
rather than rewritten is not recorded.

**Why six groups.** The reason the kinds are grouped in exactly
these six is not recorded.

## A worked example

A small thought project, `<slug>`, after a few rounds of work might
hold these files. The kind of each stands after it.

```
projects/<slug>/
  project.md                  state: project file, written once
  00-brief.md                 artefact
  00-brief.history.md         record: history, append-only
  10-intent.md                artefact
  10-intent.history.md        record: history, append-only
  threads/THR.NNNN.md         state: thread, rewritten while open
  decisions.md                record: decisions, append-only
  ledger.md                   state: ledger, made at read time, not in git
  sources/00-INDEX.md         state: index, rewritten freely
  sources/<source>.md         resource: source, immutable
  research/YYYY-MM-DD-<topic>.md   resource: research, immutable
  reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md   record: review, immutable
  recipes/readme.md           rendering: recipe, iterated
  README.md                   rendering: render, overwritten
```

One record in `decisions.md` has this shape:

```
## DEC.NNNN — <the decision in one line>
- **Decision:** <what was decided>
- **Reason:** <why, including what was weighed against it>
- **Date:** YYYY-MM-DD
```

A decision that rules on a finding or a challenge carries one more
line per ID it rules on, a `Verdict`. When the principal changes his
mind, the old record stays as it is and a new record names it.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [The ledger, made from the records](the-ledger.md): what the
  ledger is made from and why nobody writes it.
- [End a session](../use/end-a-session.md): the command that says
  what lives only in the conversation.
- [Versioning and history](versioning-and-history.md): the history
  companion of every versioned kind.
- [The documentation](the-documentation.md): the map and the pages.
- [The work product](the-work-product.md): the work kind.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
