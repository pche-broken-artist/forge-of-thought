---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 42689998635e49a6
inputs:
  - CLAUDE.md#Document kinds
  - CLAUDE.md#Ledger
  - templates/ledger.md
  - templates/decisions.md
  - projects/forge/10-intent.md#POS.1080
  - projects/forge/10-intent.md#POS.0160
  - projects/forge/10-intent.md#POS.0320
  - projects/forge/10-intent.md#POS.0330
  - projects/forge/10-intent.md#POS.0550
---

# Documents and records

A document is any file a project holds, and every document has one
kind that says what it is, who writes it, whether it is versioned and
how it behaves. This page is for the user who works a project, for
the extender who adds to the forge and for the evaluator who judges
it. It explains the six groups the kinds fall into, which documents
are records and which hold state, why state lives in files rather
than in the conversation, and why some documents are never edited.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the documents the principal
(the person whose thinking is forged) composes with Claude, the
reviewers read and the renders are generated from. The chain is the
line of versioned documents a project travels, from the brief through
the intent to whatever layers the project takes below it.

Every document has one kind. The kind says four things about a
document:

- what it is
- who writes it
- whether it is versioned
- how it behaves: whether it is rewritten freely, appended to, or
  never touched once written

The kinds fall into six groups:

- artefacts: the artefact, a document of the chain; what each one is,
  its definition says
- records: the history, what changed in a versioned document and
  why, append-only; the decisions, the principal's decisions with
  their reasons, append-only; the review and the challenge, one dated
  reviewer run each, immutable
- state: the ledger, the single source of truth for state; the
  index, the catalogue of a resource directory; the documentation
  map, one entry per page with everything a page is made from
- rendering: the recipe, how a render is made; the render, an
  audience-specific output; the page, a page of the documentation or
  its index
- work: the work product, an output of the project made with work of
  its own
- resources: the source, external input as it arrived; the research,
  a durable answer to one question

The table of kinds with all its columns is the reference page
[Document kinds](../reference/document-kinds.md). The other terms of
the forge are in the [Glossary](../reference/glossary.md).

## How it works

### The artefacts

An artefact is written by the principal with Claude. It is versioned
and rewritten freely between approvals. The intent is rewritten this
way, and so is the assignment: nothing in the file freezes it. What
the recipients of an assignment hold is one version, reached by a
link into git. Which artefacts the forge has is the listing of the
directory `.claude/skills/forge/states/`, one definition per
artefact; they are listed nowhere else.

### The records

A record says what happened, and it is never rewritten.

The history is a companion file beside every versioned document,
named `<file>.history.md`. It holds what changed in that document and
why, and it is only appended to. Every versioned kind keeps one: an
artefact, a recipe and a work specification alike. How the companion
is shaped and how a version is counted is on
[Versioning and history](versioning-and-history.md).

The decisions live in one file of the project, `decisions.md`. It
holds one record per decision of the principal, numbered `DEC.NNNN`
in the global sequence of the ID scheme, newest last. A record says
what was decided, why, including what was weighed against it, and on
what date. A record is never edited. A later decision supersedes an
earlier one by a new record that names it.

A review and a challenge are each one dated run of a reviewer agent.
Reviews are filed in `reviews/`, challenges in `challenges/`. Once
written, they are immutable.

### The state

The ledger is the project's single source of truth for state, the
file `ledger.md`. It is written by the forge and freely rewritten,
and it is kept current after every operation. Its header carries the
project's kind (a thought project or a library) and the language of
the chain's artefacts. Its tables are:

- briefs
- documents
- renders
- published files
- work products
- sources
- dependencies
- research
- findings
- challenges

The ledger closes with a list "Waiting on principal". A library keeps
fewer tables than a thought project. The tables and the states each
row can take are on [Ledger](../reference/ledger.md).

The rows for sources, research and dependencies are registration
only. What a resource is and what it is for lives in the index of its
directory, `sources/00-INDEX.md` or `research/00-INDEX.md`, never in
the ledger. A library document a project depends on is cited by path
and carries no version.

The ledger cites and never copies. Under "Waiting on principal", a
matter that has an ID gets one line: the ID, a few words and its
state. Its substance stays in the thread or in the record. Free text
stands there only for a matter that has no ID yet, and that matter
gets one at the next write. An unfinished conversation is saved into
its thread of the intent, never into the ledger.

A layer below the intent that a project does not have is not
missing. The ledger has no row for it, and the state map and the
checks say nothing of it.

The index is the catalogue of a resource directory, and it is freely
rewritten. The documentation map is state of the project that owns
the documentation. It is never shown to the reader of the
documentation; the pages and their index are what the reader sees.
The map and the pages are explained on
[The documentation](the-documentation.md).

### The rendering

A recipe says how a render is made. It is written by Claude and
iterated by the principal, and it is versioned. A recipe is never
approved. A render is generated from its recipe and overwritten by
`/render` at every run; it is never a source of truth. A page of the
documentation is generated likewise and overwritten by the
documentation run.

### The work product

A work product is two files: the file that holds the content, and the
specification beside it that holds the way and the why. The
specification is versioned; the file is remade from it. The principal
works with the file freely. The kind is explained on
[The work product](the-work-product.md).

### The resources

A source is external input as it arrived. It is immutable from its
registration. A functional binary, such as a `.potx` template or a
graphic, is a source too. A library's assets are therefore resources
without a kind of their own. A library carries no artefacts and no
records but the history companion of its recipe.

Research is a durable answer to one question, written by Claude
through `/research`. It is immutable from its creation.

### Immutable documents

Reviews, challenges, sources and research are never edited. A source
is immutable from its registration; the others from their creation.
A correction happens downstream, in a later document, never in the
immutable one.

Immutability is a process rule, kept by convention. Git does not
enforce it.

### Wrapping

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## Why

The kind decides everything else about a document: what it is, who
writes it, whether it is versioned and how it behaves. The table of
kinds is the one page from which all of this is read, in the forge's
own intent, in `CLAUDE.md` and in the README alike. Why the kinds
fall into six groups rather than another number is not recorded.

State lives in files because what is in a file survives the session
(one conversation with Claude, from its start to its end). What lives
only in the conversation does not survive it. The command `/end` says
what that is at the end of a session; the page
[End a session](../use/end-a-session.md) explains it. The command
`/ledger` re-orients Claude from the ledger. One project per session
is the hygienic default.

The ledger cites and never copies, and the substance of a matter
stays in the thread or in the record. The reason for this rule is not
recorded.

Immutability is a process rule and not a mechanism of git for three
reasons the inputs give. Git protects nothing from a commit that
rewrites a file. The rule costs nothing. A mechanism would be one
more layer to maintain, and it still would not stop a hand edit.

Why a correction to an immutable document happens downstream rather
than in a new copy of the document is not recorded.

Prose is hard-wrapped at about 72 columns so that git diffs stay
legible. Why tables, code blocks and front-matter are left unwrapped
is not recorded.

## A worked example

A thought project with the slug `my-project` holds these files after
its intent has been revised twice and one critique has run. The kind
of each stands beside it.

```
projects/my-project/
  00-brief.md                            artefact
  00-brief.md.history.md                 history
  10-intent.md                           artefact, version 0.3
  10-intent.md.history.md                history
  threads.md                             the open threads
  decisions.md                           decisions
  ledger.md                              ledger
  sources/00-INDEX.md                    index
  sources/vendor-offer.md                source
  research/00-INDEX.md                   index
  research/2026-02-03-review-cadence.md  research
  recipes/readme.md                      recipe
  recipes/readme.history.md              history
  README.md                              render
  reviews/2026-02-10-critique-<lens>.md  review
```

One change travels the kinds like this. The principal and Claude
revise the intent from 0.2 to 0.3. The intent is rewritten, and its
history companion gets one record per change, with the reason. The
ledger's Documents row for `10-intent.md` now says 0.3. The critique
of 2026-02-10 stays as it was written; it is not touched by the
revision. One of its findings the principal rejects, and that rejection
becomes a record in `decisions.md`, say `DEC.0010`, with the reason.
The ledger's Findings row for that finding changes its state to
rejected and cites `DEC.0010`; the reason itself stands only in the
decision record. The README is regenerated from its recipe when the
project is released, and nobody edits it by hand.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [Ledger](../reference/ledger.md): the ledger's tables and states.
- [End a session](../use/end-a-session.md): the command that says
  what lives only in the conversation.
- [Versioning and history](versioning-and-history.md): the history
  companion of every versioned kind.
- [The documentation](the-documentation.md): the map and the pages.
- [The work product](the-work-product.md): the work kind.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
