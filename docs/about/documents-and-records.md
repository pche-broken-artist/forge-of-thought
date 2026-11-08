---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 6972ef1a7734e058
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

A document is every file of a project in Forge of Thought, and every
document has one kind that says what it is, who writes it, whether it
is versioned and how it behaves. This page explains the kinds and the
six groups they fall into, names the few files that have no kind, and
says why the state of a project lives in files and never only in the
conversation. It is for the user who works a project, for the
extender who adds to the forge and for the evaluator who judges how
the forge keeps its records.

## What it is

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the [chain](../reference/glossary.md):
the ones the principal composes, the reviewers read and the renders
are generated from. The principal is the person whose thinking is
being forged. Every other file of a project is a document of some
other kind, and never an artefact.

Every document has one kind. The kind says four things about the
document:

- what it is
- who writes it
- whether it is versioned
- how it behaves

The kinds fall into six groups. The full table, kind by kind, is the
page [Document kinds](../reference/document-kinds.md); here the groups
in words.

- **Artefacts.** One kind, the artefact: a document of the chain,
  written by the principal with Claude, versioned and rewritten
  freely. What each artefact is, its definition says (the definition
  is the state file that owns one artefact).
- **Records.** Three kinds. The history says what changed in a
  versioned document, and why; it is append-only and the forge writes
  it. The decisions are the principal's decisions with their reasons;
  they are append-only and the forge writes them. The review and the
  challenge are each one dated reviewer run; they are immutable and a
  reviewer agent writes them. A reviewer agent is Claude run as a
  subagent, that is in a run of its own that sees nothing of the
  conversation.
- **State.** Five kinds. The ledger is the single source of truth for
  the state of a project; a script makes it at read time and it is
  never in git. The project file holds the slug, the kind and the
  language of the project; `/new-project` writes it once. A thread is
  one open matter of the intent, written by the principal with Claude,
  rewritten freely while open and immutable once closed. An index is
  the catalogue of a resource directory, rewritten freely. The
  documentation map holds one entry per page of the documentation and
  everything a page is made from; it is generated and rewritten freely
  by the documentation run ([The documentation](the-documentation.md)).
- **Rendering.** Three kinds. A recipe says how a render is made;
  Claude writes it and the principal iterates it; it is versioned, and
  it takes an integer version only on the principal's word, as his own
  mark and not as an approval. A render is an audience-specific
  output, generated and overwritten by `/render`, never a source of
  truth. A page is a page of the documentation or its index, generated
  and overwritten by the documentation run, never a source of truth
  ([Renders and recipes](renders-and-recipes.md)).
- **Work.** One kind, the work product: an output of the project made
  with work of its own. The file holds the content; the specification
  beside it holds the way and the why. Claude writes it and the
  principal judges it. The specification is versioned; the file is
  remade from the specification, and the principal works with it
  freely ([The work product](the-work-product.md)).
- **Resources.** Two kinds. A source is external input as it arrived,
  brought in from outside or through `/ingest`, immutable. A research
  note is the durable answer to one question, written by Claude
  through `/research`, immutable. A research of several questions is a
  bundle: the plan and the synthesis at its head and one note per
  question per engine.

A functional binary, such as a `.potx` template or a graphic, is a
source. So the assets of a library are resources without a kind of
their own. A library carries no artefacts and no records but the
history companion of its recipe.

Three files have no kind, and the forge reads none of them as a
document:

- a file of `tmp/`, the engine's working folder
- the player page of `docs/videos/`
- the principal's own file beside the forge's in `renders/` or
  `published/` ([Renders and recipes](renders-and-recipes.md))

The reason these three have no kind is not recorded in the inputs of
this page.

Every versioned kind keeps its history in an append-only companion
beside it, `<file>.history.md`
([Versioning and history](versioning-and-history.md)). An integer
version is approved; a recipe never is.

Prose in every document is hard-wrapped at about 72 columns. Tables,
code blocks and front-matter are never wrapped.

## How it works

The kind of a document decides how it behaves day by day. Four
behaviours cover all the kinds.

**Rewritten freely.** An artefact, an open thread, an index and the
documentation map are rewritten in place. For an artefact, what
changed and why goes into its history companion, not into its body.
An assignment is not frozen in any sense its file would show: it is
rewritten freely between approvals like the intent, and what the
recipients hold is a version reached by a link into git.

**Append-only.** A history and the decisions file grow at the end
and nowhere else. One record is added per change or per decision,
newest last; a record, once written, is never edited. A later
decision that changes an earlier one does not touch it: it supersedes
it by a new record that names it. A decision that rules on a finding
or on a challenge carries one Verdict line per ID it rules on. A
partial verdict is read as the verdict on the whole ID; the rest of
the ruling is a `changed` record of the history.

**Immutable.** A review, a challenge, a source and a research note
are never edited: a source from its registration, the others from
their creation. A thread joins them once it is closed. Corrections
happen downstream, in a later document, never in the immutable one.

**Generated.** A render, a page and the ledger are made from other
files by a command or a script and are overwritten by the next run;
none of them is a source of truth. The ledger is the single source of
truth for state, made from the other files of the project and never
written by hand ([The ledger, made from the
records](the-ledger.md)). The ledger cites and never copies.

State lives in files, never only in the conversation. What is in a
file survives the session, that is one sitting of the conversation
with Claude; what lives only in the conversation does not. `/end`
says what that is ([End a session](../use/end-a-session.md)), and
`/ledger` re-orients from the ledger. An unfinished conversation is
saved into its thread of the intent, as a write of whatever is agreed
so far, never into the ledger. One project per session is the
hygienic default.

## Why

**Why "artefact" is a reserved word.** The artefacts are the
documents the principal composes, the reviewers read and the renders
are generated from. Every other document serves them: a record says
what happened to them, a state file says where they stand, a render
is made from them. The word keeps that line visible.

**Why every document has one kind.** The kind determines what a
document is, who writes it, whether it is versioned and how it
behaves. One table is the one place from which all of this is read.
Why the kinds fall into exactly six groups is not recorded in the
inputs of this page.

**Why state lives in files.** What is in a file survives the session;
what lives only in the conversation does not. A file is therefore the
only place a project's state can be trusted to be found again.

**Why nobody writes the ledger.** The ledger is made from the other
files at read time. Why that is so is explained on the page
[The ledger, made from the records](the-ledger.md).

**Why immutability is a process rule and not a mechanism of git.**
Git protects nothing from a commit that rewrites a file. The rule
costs nothing. A mechanism would be one more layer to maintain, and
it still would not stop a hand edit. So immutability is enforced by
convention: the forge never edits an immutable document, and a
correction is made downstream. Why corrections go downstream rather
than anywhere else is not recorded beyond the rule itself.

**Why prose is hard-wrapped at about 72 columns.** So that git diffs
stay legible. Tables, code blocks and front-matter are not wrapped,
because wrapping would break them.

## A worked example

A project with the placeholder slug `my-project` holds a decisions
file, `projects/my-project/decisions.md`. It is a record of the
records group: the forge writes it, the principal decides what it
says, and it is append-only. Its shape is the skeleton
`templates/decisions.md`. After two decisions it reads like this:

```markdown
---
project: my-project
---

# Decisions

## DEC.0010 — The pilot runs in one region first
- **Decision:** the pilot is limited to one region before any rollout.
- **Reason:** one region gives a measurable result; a wider pilot was
  weighed and dropped as too slow to read.
- **Date:** 2026-03-02

## DEC.0020 — The pilot runs in two regions, superseding DEC.0010
- **Decision:** a second region joins the pilot.
- **Reason:** the first region alone cannot show the effect of a
  shared supplier; the cost of a second region was weighed and
  accepted.
- **Verdict:** FND.0030 rejected
- **Date:** 2026-04-15
```

Three things of this page show in the example. The first record is
untouched when the principal changes his mind: the second record
supersedes it by naming it, and the file has only grown. The second
record rules on a finding of a reviewer, so it carries one Verdict
line for that finding's ID; the verdict stands in this record, and
the ledger, which cites and never copies, holds nothing written by
hand about it. And the decision lives in a file: when the session
ends, the two records are still there, while whatever was said about
them in the conversation and not written is gone.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
