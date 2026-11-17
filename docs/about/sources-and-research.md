---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 849c8f0015578a7d
inputs:
  - CLAUDE.md#Document chain
  - CLAUDE.md#Document kinds
  - templates/index.md
  - templates/index-bundle.md
  - projects/forge/10-intent.md#POS.0050
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.0840
  - projects/forge/10-intent.md#POS.1040
---

# Sources and research

Sources and research are the two kinds of resource a project keeps
beside its chain (the numbered documents of a project: a brief, the
[intent](../reference/glossary.md) and the layers the project needs
below it). A source is an external input, kept as it arrived. A
research is a durable answer to a question. This page explains why
both are immutable, why registering a source is not the same as
taking it in, and what the index of each directory is for. It is
written for someone who works with the forge and for someone who
weighs it.

## What it is

A **source** is an external input, such as a transcript, an offer, a
document or a standard. It comes from outside the project and is
registered through `/ingest` (the procedure:
[Register a source](../use/register-a-source.md)). It lives in the
`sources/` directory of its project under a plain slug filename. It
is immutable once it is registered. It may arrive at any stage of a
project's life.

A source has one form, and never both by default:

- text: a text file, or the Markdown extract of a binary file;
- a functional binary: a file that is used as a thing, such as a
  deck template, a graphic or a logo.

A **bundle** is a set of related files that is kept as one source: a
subdirectory `sources/<slug>/` with one entry in the index. A
downloaded site with its index is a bundle. So is a document with
its attachments. A bundle is one of two things:

- a whole that arrived at once: it is immutable as a whole from its
  registration;
- a stream of one origin that keeps arriving, such as the issues of
  a repository or the minutes of a standing meeting: it grows, and
  each file is immutable from its own registration.

A **research** is a durable answer to one question, written by
Claude through `/research` (the procedure:
[Research a topic](../use/research-a-topic.md)). It lives in the
`research/` directory of its project. A research has one of two
shapes:

- a single note: the answer to one question;
- a bundle: a research of several questions, with the plan and the
  synthesis at its head and one note per question per
  [engine](../reference/glossary.md).

A research note is immutable and dated: the name of its file opens
with the date, as in `YYYY-MM-DD-<topic>.md`. How a research is
planned before it is searched and run on two model families where it
carries weight is explained in
[How a research is made](the-research.md).

Every `sources/` and `research/` directory carries an **index** (the
file `00-INDEX.md`). It is a light catalogue of what resources exist
and what they are for. With it Claude and the principal (the person
whose thinking is forged) know both without reading the files again.

```
sources/
  00-INDEX.md              the index, one entry per source
  <slug>.md                a text source, or the extract of a binary
  <slug>.<ext>             a functional binary
  <slug>/                  a bundle: one source, one entry above
    00-INDEX.md            the bundle's own index, one entry per file
    <file>
research/
  00-INDEX.md              the index of the research
  YYYY-MM-DD-<topic>.md    a research note
```

## How it works

### Registration is not intake

`/ingest` stores, registers and catalogues a source. It does nothing
more. What a source is for is individual, for example:

- a standard to verify against;
- inspiration;
- a counter-example;
- a meeting record;
- material to absorb.

This is the source's Role: a free-text field of its entry in the
index. The Role is the principal's word. Before the entry is
written, Claude always asks "what is it for?". It never infers the
role unasked. The principal answers with the role, or tells Claude
to infer it. An inferred role is written with the mark *(inferred)*.

The principal alone directs how and when a source is used, in
whatever work the principal chooses. When content of a source does
enter the intent, that is the principal's explicit act, cited with
provenance to the file. What someone said in a meeting is never
silently promoted to the principal's own position.

### One form per source

When a source is registered, every binary file gets one question:
convert to Markdown? The question comes for a file that stands alone
and for a file inside a bundle alike.

- Yes: one script of the forge (`scripts/doc2md.py`) writes the
  extract as a Markdown file. That extract is the source, and the
  original is not copied into the project.
- No: the binary is the source, as a functional thing.

Keeping both is the exception, on the principal's explicit word. An
extract is never produced by ad-hoc parsing.

### A newer state is a new file

A source or a research note is not edited when the world it records
moves on. A newer state is a new file:

- for a research: the research is run again;
- for a document that arrives in a new version: a further file of a
  bundle of one origin, whose index says which file is the newest
  and which it supersedes.

A growing bundle takes each new file on the principal's word,
through `/ingest`, with an entry of its own in the bundle's index.

### The index

An index has one entry per resource, in fixed fields of free text.
The entry of a source has these fields:

- **What**: what the resource is, in one or two sentences.
- **Origin**: where it came from, such as an author, a URL or a
  meeting.
- **Date**: the date and where it was taken from: the content, the
  file or the ingest. It is recorded best effort and never asked of
  the principal.
- **Form**: text, the extract of an original, or a binary.
- **Role**: what the source is for, in free text.
- **Use for**: what to reach for it for, that is the questions it
  answers best.

The entry of a research has these fields:

- **Question**: what the note set out to answer.
- **Answer in short**: two or three lines of the conclusion.
- **Consult when**: the situations in which the note is worth
  opening.

A bundle appears in the index of `sources/` as one entry, and that
entry points to the bundle's own `00-INDEX.md` inside it. The index
of `sources/` never repeats the bundle's contents. There are two
levels of index and never more. The bundle's index is the same
catalogue one level down:

- a header: the bundle's slug, the project, a date and the origin of
  the whole;
- an opening paragraph: what the whole bundle is, why it entered
  `sources/`, and whether it arrived whole or grows;
- one entry per file: the fields of a source's entry, in the same
  order.

Where a bundle arrives without an index, one is created at
registration. File-level detail is not lost: provenance in the
intent cites an individual file by its path, and the bundle's index
lists its contents.

The index tracks nothing: no processing state and no positions. It
is an automatic input of no command. Neither `/forge` (the command
through which a document of the chain is worked) nor the reviewers
(`/critique` and the challengers) confront the chain with the
material on their own. A contradiction between the intent and a
resource is not a finding (a reviewer's result). Claude reaches for
a file by its own judgement, or when the principal asks, for
example: "check the assessment against the requirements in file X".

The index is freely rewritten, while the files under it stay
immutable. The ledger (the one file that shows the state of a
project, made by a script at read time) holds registration only: a
Sources table and a Research table, with no content columns. The
date of a source is recorded in its index entry and shown in the
ledger.

### Personal matter stops an ingest before the store

`/ingest` takes a file, and it takes text pasted into the
conversation as well. Before anything is stored, personal matter
stops the command, and Claude asks. Personal matter is anything
such as a named private person, an identifying detail or health.

## Why

**Why a source and a research note are immutable.** Each records a
moment: a state of the world that the forge did not make and has no
business editing. A newer state is therefore a new file, never a
change to the old one. The purpose is that every citation in the
intent keeps pointing at the text it was made from.

**Why registration is not intake.** What a source is for differs
from one source to the next. A source may be a counter-example, a
mere inspiration or a record of what someone else said. For that
reason a contradiction between the intent and a source is not a
finding, and no command confronts the chain with a source on its
own. Content of a source enters the intent only by the principal's
explicit act, with provenance. The purpose is that what someone
said is never silently promoted to the principal's own position.

**Why the role is asked before the entry is written.** The entry
then carries its role from the moment it is written, and no later
hand changes it.

**Why a source has one form.** The repository carries what the
forge works with, and that is text. A binary that nobody reads from
git is weight without use. A binary that is used as a thing is kept
for that use.

**Why the index is a catalogue and nothing more.** The index is a
working aid, not a record of thinking. Its entries are free text in
one shape for every index: Role and Use for are what an index is
for, and a table does not carry them. The ledger holds registration
only. The purpose is that nothing is described in two places. A
date is never demanded from the principal: an origin date is
metadata, not ceremony. The reason for the limit of two levels of
index is not recorded.

**Why personal matter stops an ingest before the store.** A source
is immutable from its registration and travels into git. What has
entered cannot be taken back. The question must therefore come
before the store.

**Why a research is kept.** For a key topic Claude researches
current best practice rather than inventing. Outside inspiration is
a legitimate input. A durable answer is stored in `research/` and
is not left in the conversation.

## A worked example

One entry of the index of `sources/`, for an invented source of an
invented project:

```markdown
### `supplier-offer.md`
- **What:** The written offer of a supplier for the service the project is about, with prices and terms.
- **Origin:** Sent by the supplier after the first meeting.
- **Date:** 2026-03-02, from the content
- **Form:** extract of supplier-offer.pdf
- **Role:** a counter-example: the terms the principal does not want to accept
- **Use for:** the supplier's prices, the limits of the service, the wording of the terms
```

The entry reads as follows:

- The Form says the file is an extract. The PDF it was made from is
  not in the project.
- The Date says where the date was taken from. Nobody was asked for
  it.
- The Role is the principal's answer to "what is it for?". Had the
  principal told Claude to infer it, the line would carry the mark
  *(inferred)*.
- The Role names a counter-example. A contradiction between this
  offer and the intent is therefore expected, and it is not a
  finding.
- Nothing in the entry says whether the offer has been used. The
  index tracks no processing state.
- Should the supplier send a revised offer, the file above stays as
  it is. The newer state is a new file.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [How a research is made](the-research.md): how a research is
  planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
