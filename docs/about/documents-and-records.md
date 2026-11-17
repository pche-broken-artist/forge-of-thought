---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 15a84cbad625cb2c
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

A document is any file of a project of the forge, and every document
has one kind. This page explains the kinds, group by group, and why
the state of a project lives in files and never only in the
conversation. It is for whoever uses the forge, extends it or weighs
it, and wants to know what a file of a project is before opening it.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain. The principal (the person
whose thinking is forged) composes them. The reviewers read them. The
renders are generated from them. A reviewer is an agent whose dated
run is kept as a review or a challenge. A render is an output
generated for one audience
([Renders and recipes](renders-and-recipes.md)). The chain is defined
in the [Glossary](../reference/glossary.md), as is every other term
of the forge that this page uses without a gloss.

Every document has one kind. The kind says four things:

- what the document is
- who writes it
- whether it is versioned
- how it behaves

The kinds fall into six groups. The table of kinds, word for word, is
on the page [Document kinds](../reference/document-kinds.md).

### Artefacts

An artefact is a document of the chain. The definition of an artefact
says what it is. The artefacts the forge has are the listing of
`.claude/skills/forge/states/`, one definition each, and they are
listed nowhere else. The principal writes an artefact with Claude. An
artefact is versioned and rewritten freely. An assignment, like the
intent, is rewritten freely between approvals: it is not frozen in any
sense the file would show. What its recipients hold is a version
reached by a link into git.

### Records

- history: what changed in a versioned document, and why. The forge
  writes it. It is append-only
  ([Versioning and history](versioning-and-history.md)).
- decisions: the decisions of the principal, with their reasons, in
  the file `decisions.md`. The forge writes them. The file is
  append-only.
- review and challenge: one dated run of a reviewer each, in
  `reviews/` and `challenges/`. The reviewer agent writes it. It is
  immutable.

### State

- ledger (the file `ledger.md`, which holds the state of a project):
  the single source of truth for state, made by a script from the
  other files at read time, never written by hand and never in git
  ([The ledger, made from the records](the-ledger.md)).
- project: the project file. It holds the slug of the project, its
  kind as a project and its language. The command `/new-project`
  writes it once.
- thread: one matter of a project set aside to be taken up later. The
  principal writes it with Claude. It is freely rewritten while open
  and immutable once closed.
- index: the catalogue of a resource directory. The forge writes it,
  and it is freely rewritten.
- map: the documentation map. It has one entry per page, with
  everything a page is made from. It is generated, and the
  documentation run rewrites it freely. It is state of the project
  that owns the documentation, and the reader of the documentation
  never sees it ([The documentation](the-documentation.md)).

### Rendering

- recipe: how a render is made. Claude writes it and the principal
  iterates it. It is versioned. It takes an integer version only on
  the principal's word, and the integer is his own mark, not an
  approval.
- render: an output for one audience, never a source of truth. It is
  generated, and the command `/render` overwrites it.
- page: a page of the documentation, or its index, never a source of
  truth. It is generated, and the documentation run overwrites it.

### Work

The group has one kind: the work product
([The work product](the-work-product.md)). A work product is an
output of the project made with work of its own. The file holds the
content. The specification beside the file holds the way and the why.
Claude writes a work product and the principal judges it. The
specification is versioned. The file is remade from the
specification, and the principal works with the file freely.

### Resources

- source: an external input as it arrived. It comes from outside,
  through the command `/ingest`. It is immutable. A functional binary,
  such as a `.potx` template or a graphic, is a source too.
- research: a durable answer to one question, in `research/`. Claude
  writes it, through the command `/research`. It is immutable. A
  research of several questions is a bundle: the plan and the
  synthesis stand at its head, with one note per question per engine.

### Files with no kind

Three files have no kind, and the forge reads none of them as a
document:

- a file of `tmp/`, the working folder of the engine (the repository
  of the forge itself, apart from the repositories of the projects)
- the player page of `docs/videos/`
- the principal's own file in `renders/` or `published/`, beside the
  files of the forge ([Renders and recipes](renders-and-recipes.md))

### In a library

A library carries no artefacts. Of the records it carries only the
history companion of its recipe. The other groups are unchanged. A
functional binary is a source. The assets of a library therefore fall
under resources and have no kind of their own.

## How it works

### State lives in files

State lives in files, never only in the conversation. What is in a
file survives the session (one run of the conversation with Claude).
What lives only in the conversation does not. The command `/end` says
what lives only in the conversation
([End a session](../use/end-a-session.md)). The command `/ledger`
re-orients from the ledger. An unfinished conversation is saved into
its thread of the intent, as a write of whatever is agreed so far, and
never into the ledger. One project per session is the hygienic
default.

### Versioned kinds keep a history

Three kinds are versioned: the artefact, the recipe and the
specification of a work product. Every versioned kind keeps its
history in an append-only companion file, `<file>.history.md`
([Versioning and history](versioning-and-history.md)). An integer
version is approved. A recipe never is.

### Records are appended, never edited

The file `decisions.md` holds one record per decision of the
principal. The records are numbered `DEC.NNNN`, and the newest stands
last. A record is never edited. A later decision supersedes an earlier
one by a new record that names it. A record opens with a heading that
carries its number and the decision in one line. Under the heading
stand its fields:

- Decision: what was decided
- Reason: why, including what was weighed against it
- Verdict: only where the decision rules on a finding (a result of a
  reviewer) or on a challenge, one line per ID it rules on, each
  saying `rejected`, `parked until <what>` or `obsolete`
- Date: the day of the decision

### Immutable documents stay as they are

Reviews, challenges, sources and research are never edited. A source
is immutable from its registration. The others are immutable from
their creation. Corrections happen downstream, and the immutable file
stays as it is. Immutability is a process rule, enforced by
convention and not by git.

### Prose is hard-wrapped

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

State lives in files and never only in the conversation. The reason
is what survives: what is in a file survives the session, and what
lives only in the conversation does not.

Immutability is a process rule and not a mechanism of git, for three
reasons:

- git protects nothing from a commit that rewrites a file
- the rule costs nothing
- a mechanism would be one more layer to maintain, and it still would
  not stop a hand edit

Why a record is append-only, and why a review, a challenge, a source
and a research are immutable at all: the reason is not recorded.

Why the three files named above have no kind: the reason is not
recorded.

Prose is hard-wrapped at about 72 columns. The wrap keeps the diffs
of git legible.

## A worked example

A project with the placeholder slug `my-project` plans a pilot. In a
conversation the principal decides that the pilot starts with one
team. As long as the decision stands only in the conversation, it
would not survive the session. It is written as a record at the end
of `decisions.md`:

```
## DEC.0010 — The pilot starts with one team
- **Decision:** The pilot starts with one team. The other teams join after the first month.
- **Reason:** One team shows whether the process holds before more people depend on it. Weighed against a start with three teams, which gives more to compare and no room to correct.
- **Date:** 2026-03-02
```

Two weeks later the principal changes his mind. The first record is
not edited. A new record is appended below it and names the record it
supersedes:

```
## DEC.0020 — The pilot starts with two teams
- **Decision:** The pilot starts with two teams. This supersedes DEC.0010.
- **Reason:** A second team asked to join and gives a comparison from the first day. Weighed against one team, which is simpler to run.
- **Date:** 2026-03-16
```

What happens around the two records follows from the kinds:

- The artefact that speaks of the pilot is rewritten to say two teams.
  An artefact is rewritten freely. What changed and why is appended to
  its history companion.
- A review filed before the second decision stays as it was written.
  A review is immutable, and corrections happen downstream.
- Nobody writes the decision into the ledger. The ledger is made from
  the files the next time it is read.
- A file of his own on the pilot that the principal puts in
  `published/`, beside the files of the forge, has no kind. The forge
  does not read it as a document.

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
- [Renders and recipes](renders-and-recipes.md): the principal's own
  files beside the forge's, which have no kind.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
