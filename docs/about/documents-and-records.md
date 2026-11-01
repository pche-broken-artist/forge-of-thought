---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 45e4707d32be0bc1
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

A document is any file of a project, and every document has one
kind. This page explains what the kinds are, how each kind behaves,
and why the state of a project lives in files rather than in the
conversation. It is for the user who works a project, for the
extender who adds to the forge, and for the evaluator who judges how
the forge keeps what it knows.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the ones the principal (the
person whose thinking is being forged) composes with Claude, the
reviewers read, and the renders are generated from.

Every document has one kind. The kind says what the document is, who
writes it, whether it is versioned, and how it behaves. The kinds
fall into six groups. The full table, with every column, is on
[Document kinds](../reference/document-kinds.md); here the groups
are described in words.

- **Artefacts.** One kind, the artefact: a document of the chain.
  The principal writes it with Claude. It is versioned and rewritten
  freely. What each artefact is, its definition says. Which
  artefacts the forge has is the listing of the definitions
  directory, `.claude/skills/forge/states/`, one definition each;
  they are listed nowhere else.
- **Records.** Three kinds. The history says what changed in a
  versioned document and why; it is append-only. The decisions are
  the principal's decisions with reasons; they are append-only. A
  review and a challenge are one dated reviewer run each; they are
  immutable. The forge writes the first two, a reviewer agent the
  third.
- **State.** Five kinds. The ledger is the single source of truth
  for state; a script makes it at read time, and it is never in git.
  The project file holds the slug, the kind and the language of the
  project; it is written once, by `/new-project`. A thread is one
  open matter of the intent; it is rewritten freely while open and
  immutable once closed. An index is the catalogue of a resource
  directory; it is rewritten freely. The documentation map holds one
  entry per page and everything a page is made from; the
  documentation run rewrites it freely.
- **Rendering.** Three kinds. A recipe says how a render is made;
  Claude writes it, the principal iterates it, and it is versioned.
  A render is an audience-specific output, never a source of truth;
  `/render` overwrites it. A page is a page of the documentation or
  its index, never a source of truth; the documentation run
  overwrites it.
- **Work.** One kind, the work product: an output of the project
  made with work of its own. The file holds the content; the
  specification beside it holds the way and the why. The
  specification is versioned. The file is remade from the
  specification, and the principal works with it freely.
- **Resources.** Two kinds. A source is external input as it
  arrived; it is immutable. A research note is the durable answer to
  one question; it is immutable. A research of several questions is
  a bundle: the plan and the synthesis at its head, and one note per
  question per engine.

Three files have no kind, and the forge reads none of them as a
document:

- a file of the engine's working folder `tmp/`;
- the player page of `docs/videos/`;
- the principal's own file beside the forge's in `renders/` or
  `published/`, such as a copy under a new name or a PDF saved by
  hand (see [Renders and recipes](renders-and-recipes.md)).

A functional binary, such as a `.potx` template or a graphic, is a
source. So a library's assets are resources without a kind of their
own. A library carries no artefacts and no records but the history
companion of its recipe.

## How it works

Every versioned kind keeps its history in an append-only companion
beside it, `<file>.history.md`; the body of the document is its
current state, the companion is the record. How a version is counted
and what a companion holds is on
[Versioning and history](versioning-and-history.md). An integer
version is approved. A recipe is never approved: it takes an integer
only on the principal's word, as his own mark.

Immutable documents are never edited. A source is immutable from its
registration. A review, a challenge and a research note are immutable
from their creation. A correction to any of them happens downstream,
in the documents that use them.

An append-only record is never edited either. A later decision
supersedes an earlier one by a new record that names it. The
decisions file numbers its records `DEC.NNNN` in the global sequence
of the ID scheme, newest last. Each record carries the decision in
one line, what was decided, the reason with what was weighed against
it, and the date. Where the decision rules on a finding (a reviewer's
result) or a challenge, it carries one Verdict line per ID it rules
on: `rejected`, `parked until <what>` or `obsolete`. A partial
verdict is read as the verdict on the whole ID; the rest becomes a
record of the history.

The ledger (the one file that says where a project stands) is the
single source of truth for state, made from the other files of the
project and never written by hand; what it is made from and why
nobody writes a row is on
[The ledger, made from the records](the-ledger.md). The ledger cites
and never copies. An unfinished conversation is saved into its thread
of the intent, as a write of whatever is agreed so far, never into
the ledger.

State lives in files, never only in the conversation. `/end` says
what lives only in the conversation at the end of a session (one
conversation with Claude); the command is on
[End a session](../use/end-a-session.md). `/ledger` re-orients from
the ledger. One project per session is the hygienic default.

The documentation map is state of the project that owns the
documentation. It is never shown to the reader of the documentation;
the pages and the index are what the reader reads. The map and the
pages are on [The documentation](the-documentation.md). The work
product is on [The work product](the-work-product.md).

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

One table carries the kinds. It is the one page from which all of
this is read, in the intent of the forge's own project, in
`CLAUDE.md` and in the README alike.

State lives in files because what is in a file survives the session.
What lives only in the conversation does not.

Immutability is a process rule, enforced by convention and not by
git. Git protects nothing from a commit that rewrites a file. The
rule costs nothing. A mechanism would be one more layer to maintain,
and it still would not stop a hand edit.

Prose is hard-wrapped so that git diffs stay legible.

The reason the records are append-only rather than rewritten is not
recorded.

## A worked example

A project with the slug `<slug>` closes a round of work on its
intent. Four documents of four kinds move.

The intent, an artefact, is rewritten: its version goes from `0.3`
to `0.4`. Its history companion, `10-intent.history.md`, receives
one record per change the round made; nothing earlier in it is
touched. The principal decided one thing during the round, so
`decisions.md` receives one record at its end:

```
## DEC.0010 — The pilot runs in one team before the rollout
- **Decision:** the pilot is limited to one team for one quarter
- **Reason:** a single team makes the result readable; a wider pilot
  was weighed and set aside until the first measures exist
- **Date:** 2026-03-02
```

Two rounds later the principal changes his mind. The first record
stays as it is, and a new one names it:

```
## DEC.0020 — The pilot runs in two teams
- **Decision:** the pilot takes a second team from the start;
  supersedes DEC.0010
- **Reason:** one team cannot show whether the process carries
  across a boundary, and the first measures now exist
- **Date:** 2026-05-11
```

A critique run on the intent in between produced a review in
`reviews/`, dated and immutable: where it was wrong, the correction
went into the intent, never into the review. The ledger of `<slug>`
was not written by anyone in all of this; it is made from these
files when it is read.

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
- [Renders and recipes](renders-and-recipes.md): the principal's own
  files beside the forge's, which have no kind.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
