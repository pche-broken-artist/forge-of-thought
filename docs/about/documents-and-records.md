---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 3a0ddbd513451a5f
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
one kind. This page explains the kinds a project holds, how they fall
into six groups, and why the state of a project lives in files. It is
for anyone who uses the forge, extends it or evaluates it. The full
table of kinds stands on its own page,
[Document kinds](../reference/document-kinds.md).

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain (the versioned documents a
project's thinking travels through; every term is in the
[Glossary](../reference/glossary.md)). The artefacts are the
documents that the principal (the person whose thinking is being
forged) composes with Claude, that the reviewers read and that the
renders are generated from. Every other file is a document of another
kind.

A document's kind says four things about it:

- what it is;
- who writes it;
- whether it is versioned;
- how it behaves once it exists.

The kinds fall into six groups.

- **Artefacts**: the documents of the chain. Each is written by the
  principal with Claude, is versioned and is rewritten freely. What
  each artefact is is said by its definition.
- **Records**: what changed, what was decided and what a reviewer
  found.
  - The history says what changed in a versioned document, and why.
    It is append-only.
  - The decisions are the principal's decisions with their reasons.
    They are append-only.
  - A review or a challenge is one dated run of a reviewer agent (an
    isolated helper that reads the documents and reports). It is
    immutable.
- **State**: what the project is at the moment.
  - The ledger (the single report of a project's state) is made at
    read time by a script and is never in git.
  - The project file holds the slug, the kind and the language of the
    project. It is written once.
  - A thread is one open matter of the intent. It is rewritten freely
    while open and is immutable once closed.
  - An index is the catalogue of a resource directory. It is
    rewritten freely.
  - The documentation map holds one entry per page of the
    documentation, with everything a page is made from. It is
    rewritten freely by the documentation run and never shown to the
    reader of the documentation. See
    [The documentation](the-documentation.md).
- **Rendering**: what is generated for an audience.
  - A recipe says how a render is made. It is versioned, iterated and
    never approved.
  - A render is an audience-specific output. It is overwritten by
    `/render` and is never a source of truth.
  - A page is a page of the documentation, or its index. It is
    overwritten by the documentation run and is never a source of
    truth.
- **Work**: the work product, an output of the project made with work
  of its own. The file holds the content, and the specification beside
  it holds the way and the why. The specification is versioned. The
  file is remade from the specification, and the principal works with
  the file freely. See [The work product](the-work-product.md).
- **Resources**: what comes from outside or answers a question.
  - A source is external input as it arrived. It is immutable.
  - A research note is a durable answer to one question. It is
    immutable. A research of several questions is a bundle, with the
    plan and the synthesis at its head and one note per question per
    engine.

A functional binary (such as a `.potx` template or a graphic) is a
source. A library's assets are therefore resources without a kind of
their own. A library carries no artefacts and no records except the
history companion of its recipe.

## How it works

Each kind behaves in one of a few ways, and the way is part of the
kind.

- **Rewritten freely**: the file is changed in place as the work goes
  on. Artefacts, open threads, indexes and the documentation map
  behave so.
- **Versioned**: every versioned kind keeps its history in a companion
  file beside it. See
  [Versioning and history](versioning-and-history.md).
- **Append-only**: a new record is added and no record is edited. The
  history and the decisions behave so. A decision is never changed: a
  later decision supersedes it by a new record that names it.
- **Immutable**: the file is never edited. A source is immutable from
  its registration. A review, a challenge and a research note are
  immutable from their creation. A correction happens downstream, in
  a later document, never in the immutable one.
- **Generated**: the file is remade from its inputs. Renders, pages
  and the ledger behave so.

The ledger is the single source of truth for state: a script makes it
from the other files, and nobody writes it by hand (see
[The ledger, made from the records](the-ledger.md)).

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

**State lives in files, never only in the conversation.** What is in
a file survives the session (one sitting of work with Claude). What
lives only in the conversation does not survive it. `/end` says what
lives only in the conversation before a session closes (see
[End a session](../use/end-a-session.md)). `/ledger` lets Claude find
its bearings again from the ledger. An unfinished conversation is
saved into its thread of the intent, as a write of whatever is agreed
so far, never into the ledger. One project per session is the
default; the reason is not recorded.

**Immutability is a process rule, not a mechanism of git.** Git
protects nothing from a commit that rewrites a file. The rule costs
nothing. A mechanism would be one more layer to maintain, and it
still would not stop an edit by hand.

**Prose is hard-wrapped.** The purpose is that the differences git
shows between two versions stay legible.

**One kind per document.** The kind determines what a document is,
who writes it, whether it is versioned and how it behaves. So all of
this is read from one table, the same in every place that states it.

Why records are append-only rather than rewritten is not recorded.
Why reviews and challenges are immutable, beyond the rule that
corrections happen downstream, is not recorded.

## A worked example

A generic project `<slug>` at an early stage might hold these files,
each with its kind:

```
projects/<slug>/
  project.md                 project file: written once
  00-brief.md                artefact: rewritten freely, versioned
  10-intent.md               artefact: rewritten freely, versioned
  10-intent.history.md       history: append-only
  decisions.md               decisions: append-only
  threads/THR.NNNN.md        thread: rewritten while open
  ledger.md                  ledger: made at read time, not in git
  sources/00-INDEX.md        index: rewritten freely
  sources/<name>.md          source: immutable
  reviews/<dated-name>.md    review: immutable
  recipes/readme.md          recipe: versioned, never approved
  README.md                  render: overwritten by /render
```

Suppose the principal rules on a finding of a review. The review file
stays as it is. A new record is added to `decisions.md` in the shape
the decisions template defines:

```
## DEC.NNNN — <the decision in one line>
- **Decision:** <what was decided>
- **Reason:** <why, including what was weighed against it>
- **Verdict:** <ID> rejected
- **Date:** YYYY-MM-DD
```

If the principal later decides otherwise, this record is not edited.
A new record is added that names it. The next time the ledger is
made, it is made from these files as they now stand.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [The ledger, made from the records](the-ledger.md): what the ledger
  is made from and why nobody writes it.
- [End a session](../use/end-a-session.md): the command that says what
  lives only in the conversation.
- [Versioning and history](versioning-and-history.md): the history
  companion of every versioned kind.
- [The documentation](the-documentation.md): the map and the pages.
- [The work product](the-work-product.md): the work kind.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
