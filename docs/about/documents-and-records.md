---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 3c7bc0408942249e
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

A document is any file of a project, and every document has one
kind that says what it is, who writes it, whether it is versioned
and how it behaves. This page explains the five groups the kinds
fall into, how each group behaves, why the state of a project lives
in files and never only in the conversation, and why some documents
are never edited. It is for anyone who works in a project, extends
the forge or evaluates it.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the ones the principal
(the person whose thinking is being forged) composes with Claude,
the reviewers read and the renders are generated from. Every
document has one kind. The kind says four things: what the
document is, who writes it, whether it is versioned, and how it
behaves. The table of kinds, with all four columns, is on
[Document kinds](../reference/document-kinds.md). This page gives
the groups and the reasons behind them.

The kinds fall into five groups.

- Artefacts: the documents of the chain, such as the brief and the
  intent. They are versioned and rewritten freely. Which artefacts
  the forge has is the listing of `.claude/skills/forge/states/`,
  one definition each.
- Records: what happened and why. The history of a versioned
  document and the principal's decisions are append-only. A review
  and a challenge, each one dated run of a reviewer, are immutable.
- State: where the project stands now. The ledger (the one file
  that holds a project's state), the index of each resource
  directory and the documentation map are freely rewritten.
- Rendering: what is generated from the chain. A recipe says how a
  render is made; it is versioned, iterated and never approved. A
  render and a page of the documentation are generated and
  overwritten by the next run. Neither is a source of truth.
- Resources: what came from outside. A source is external input as
  it arrived. Research is a durable answer to one question. Both
  are immutable.

Every term of the forge used here has a one-line entry in the
[Glossary](../reference/glossary.md).

## How it works

The behaviour of a document is one of four.

- Rewritten freely. An artefact's body is its current state, and
  it changes between approvals without ceremony. The assignment is
  not frozen in any sense the file would show: it is rewritten
  freely like the intent, and what the recipients hold is a version
  reached by a link into git. The ledger and the resource indexes
  are rewritten as the state they describe changes.
- Append-only. Every versioned kind keeps its history in a
  companion beside it, `<file>.history.md`, to which records are
  added and from which nothing is removed; how that companion works
  is on [Versioning and history](versioning-and-history.md). The
  decisions file holds one record per decision of the principal,
  numbered `DEC.NNNN` in the global sequence of the ID scheme,
  newest last. A decision record is never edited. A later decision
  supersedes it by a new record that names it.
- Immutable. A review, a challenge, a source and a research note
  are never edited: a source from its registration, the others
  from their creation. Corrections happen downstream, in the
  documents that are written from them.
- Overwritten. A render is overwritten by `/render`. A page of the
  documentation and the documentation map are overwritten by the
  documentation run. The map is state of the project that owns the
  documentation and is never shown to the documentation's reader;
  the pages and the index are what the reader sees. Both generated
  kinds are on [The documentation](the-documentation.md).

The ledger is the single source of truth for state. It is one file,
`ledger.md`, with one table per thing the project tracks: briefs,
documents, renders, published files, sources, dependencies,
research, findings and challenges, and a list of what waits on the
principal. Its tables and the states each row can take are on
[Ledger](../reference/ledger.md). It is freely rewritten and kept
current after every operation. For resources and dependencies the
ledger is registration only. What a source or a research note is
and is for lives in the `00-INDEX.md` of its directory, never in
the ledger. A library document that a project depends on is cited
by path and carries no version. A layer below the intent that a
project does not have is not missing: it has no row, and `/forge`
and the checks say nothing of it.

The ledger cites and never copies. Under Waiting on principal, a
matter that has an ID gets one line: the ID, a few words, its
state. Its substance stays in the thread or in the record that owns
it. Free text stands there only for a matter with no ID yet, and it
gets one at the next write. An unfinished conversation is saved
into its thread of the intent, as a write of whatever is agreed so
far, never into the ledger.

A library carries no artefacts and no records but the history
companion of its recipe. A functional binary, such as a `.potx`
template or a graphic, is a source. So a library's assets are
resources without a kind of their own.

Prose in every document is hard-wrapped at about 72 columns.
Tables, code blocks and front-matter are never wrapped.

## Why

State lives in files because what is in a file survives a session
(one working conversation with Claude, from its start to its end).
What lives only in the conversation does not survive it. So `/end`
says what would be lost if the session ended now; that command is
on [End a session](../use/end-a-session.md). And `/ledger`
re-orients from the ledger at the start of the next session. One
project per session is the hygienic default.

The ledger cites and never copies. The reason is not recorded.

Immutability is a process rule, enforced by convention, and not a
git mechanism. Git protects nothing from a commit that rewrites a
file. The rule costs nothing to keep. A mechanism would be one more
layer to maintain, and it still would not stop an edit made by
hand.

Corrections to an immutable document happen downstream. The reason
is not recorded.

Prose is hard-wrapped at about 72 columns so that git diffs stay
legible: a change to one sentence shows as a change to a few lines,
not to a whole paragraph.

The table of kinds is one page from which everything on this topic
is read, in the intent, in `CLAUDE.md` and in the README alike.
The reason for keeping it in one place is not recorded.

## A worked example

A project `sample-project` holds a brief `00-brief.md`, an intent
`10-intent.md`, the history companion of each, `decisions.md`,
`ledger.md`, a `sources/` directory with its `00-INDEX.md`, and a
`reviews/` directory with one critique report from an earlier
round.

In one round the principal and Claude agree a change to the intent.
On the principal's word Claude rewrites the intent, raising its
version from 0.4 to 0.5: an artefact, rewritten freely. In the same
step it appends a record to `10-intent.history.md` saying what
changed and why: a record, append-only, so the earlier records stay
as they were. It then updates the row of the intent in the
Documents table of `ledger.md` to 0.5: state, freely rewritten.

The critique report in `reviews/` is not touched, although the
change just made answers one of its findings. The report is a
record of one dated run and stays as it was written. What moves is
the row of that finding in the Findings table of the ledger: its
state goes from open to resolved, and its Resolution column names
the version that fixed it. The correction has happened downstream,
in the intent, not in the report.

The principal rejects another finding of the same report. Claude
appends one record to `decisions.md`, numbered in the global
sequence, with the decision and the reason it was weighed against.
The Findings row of that finding goes to rejected, and its
Resolution column names the decision record. Under Waiting on
principal the ledger keeps one line for a third finding that is
still open: its ID, a few words, and the state. What the finding
says in full stays in the report.

## See also

- [Document kinds](../reference/document-kinds.md): the table of
  kinds, verbatim.
- [Ledger](../reference/ledger.md): the ledger's tables and states.
- [End a session](../use/end-a-session.md): the command that says
  what lives only in the conversation.
- [Versioning and history](versioning-and-history.md): the history
  companion of every versioned kind.
- [The documentation](the-documentation.md): the map and the pages,
  the two generated kinds.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
