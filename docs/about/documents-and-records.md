---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 0c165b157a74cf56
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

A project of Forge of Thought is a set of files, and every file has
one kind that says what it is and how it behaves. This page explains
the six groups those kinds fall into, why the state of a project
lives in files and never in the conversation, and why some files are
never edited. It is for anyone who uses the forge, extends it or
weighs it, and wants to know what a project directory holds and
which files may change.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain. These are the documents the
principal (the person whose thinking is being forged) composes with
Claude, the reviewers read, and the renders are generated from.

Every document has exactly one kind. The kind says four things:

- what the document is;
- who writes it;
- whether it is versioned;
- how it behaves once it exists.

The full table of kinds is on the page
[Document kinds](../reference/document-kinds.md). Every term used
here has one line in the [Glossary](../reference/glossary.md).

## How it works

The kinds fall into six groups.

- **Artefacts:** the documents of the chain. They are versioned,
  written by the principal with Claude, and rewritten freely. What
  each artefact is, its definition says.
- **Records:** what has happened. The history of a versioned
  document and the decisions of the principal are append-only. A
  review or a challenge (one dated run of a reviewer) is immutable.
- **State:** where the project stands. The ledger is made at read
  time by a script. The project file (slug, kind, language) is
  written once, when the project is created. A thread (one open
  matter of the intent) is freely rewritten while open and immutable
  once closed. An index (the catalogue of a resource directory) is
  freely rewritten. The documentation map is freely rewritten by the
  documentation run.
- **Rendering:** what is generated for readers. A recipe says how a
  render is made; it is versioned, iterated and never approved. A
  render and a page of the documentation are overwritten each time
  they are generated, and neither is ever a source of truth.
- **Work:** an output of the project made with work of its own. The
  file holds the content and a specification beside it holds the way
  and the why.
- **Resources:** what comes from outside or from looking things up.
  A source is external input as it arrived. A research note is a
  durable answer to one question. Both are immutable.

The behaviours differ in what they allow:

- **Rewritten freely:** the file is the current state, and it changes
  as the work changes.
- **Append-only:** new entries are added at the end, and nothing
  already written is changed.
- **Immutable:** the file is never edited after it exists. A source
  is fixed from its registration. A review, a challenge and a
  research note are fixed from their creation. A correction happens
  downstream, in a later document, never in the immutable one.
- **Overwritten:** the file is generated again from its inputs, so a
  hand edit would be lost.

Every versioned kind keeps its history in a companion file beside
it, described on the page
[Versioning and history](versioning-and-history.md). The work kind
has a page of its own, [The work product](the-work-product.md). The
documentation map and the pages are described on the page
[The documentation](the-documentation.md). The map is state of the
project that owns the documentation. It is never shown to the
documentation's reader.

The ledger is the single source of truth for the state of a project,
made by a script from the other files and never written by hand
([The ledger, made from the records](the-ledger.md)).

A decision is one record in the project's decisions file, newest
last. A record is never edited. A later decision supersedes an
earlier one by a new record that names it. A decision that rules on a
finding (a result of a critic or a check) or on a challenge carries
one verdict line for each item it rules on.

A functional binary, such as a presentation template or a graphic, is
a source. So the assets of a library (a project of shared material
without a chain) are resources without a kind of their own. A library
carries no artefacts and no records, apart from the history companion
of its recipe.

All prose in every document is hard-wrapped at about 72 columns.
Tables, code blocks and front-matter are never wrapped.

## Why

**Why state lives in files.** What is in a file survives the session
(one sitting of work with Claude, from start to close). What lives
only in the conversation does not. So nothing of a project's state is
kept only in the conversation. The command described on
[End a session](../use/end-a-session.md) says what still lives only in
the conversation before you close. The ledger lets Claude find its
bearings again from the files in the next session. An unfinished
conversation is saved into its thread, never into the ledger. One
project per session is the recommended default.

**Why immutability is a process rule.** Immutability is kept by
convention, not enforced by git. Git protects nothing from a commit
that rewrites a file. The rule costs nothing. A mechanism would be one
more layer to maintain, and it still would not stop a hand edit.

**Why records are append-only or immutable.** The reason is not
recorded. What is recorded is the consequence: corrections happen
downstream.

**Why prose is hard-wrapped.** Hard-wrapped prose keeps git diffs
legible.

## A worked example

A generic thought project, `example-project`, shortly after its intent
was first written, might hold these files. Each is marked with its
group and kind.

```
example-project/
  project.md                       state: project (written once)
  00-brief.md                      artefact (versioned)
  00-brief.history.md              records: history (append-only)
  10-intent.md                     artefact (versioned)
  10-intent.history.md             records: history (append-only)
  threads/<thread>.md              state: thread (open, rewritten)
  decisions.md                     records: decisions (append-only)
  ledger.md                        state: ledger (made at read time)
  sources/00-INDEX.md              state: index (rewritten)
  sources/<slug>.md                resources: source (immutable)
  research/00-INDEX.md             state: index (rewritten)
  research/YYYY-MM-DD-<topic>.md   resources: research (immutable)
  reviews/<dated report>.md        records: review (immutable)
  recipes/readme.md                rendering: recipe (versioned)
  recipes/readme.history.md        records: history (append-only)
  README.md                        rendering: render (overwritten)
```

When the principal later decides something, one record is added to
the end of `decisions.md` in the shape the decisions template gives:

```
## DEC.NNNN — <the decision in one line>
- **Decision:** <what was decided>
- **Reason:** <why, including what was weighed against it>
- **Date:** YYYY-MM-DD
```

The records above it stay as they are. If the decision is later
reversed, a new record names the one it supersedes.

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

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
