---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: e07ac446fa718ee0
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

Sources and research are the two kinds of resource a project holds
beside its chain of documents. A source is external input as it
arrived. A research is a durable answer to a question. This page is
for the user who works with them and for the evaluator who wants to
know why they behave as they do: why a source never changes, why
storing a source is not the same as using it, what a research is
for, and what the index of each directory does and does not do.

## What it is

The principal is the person whose thinking is being forged (see the
[Glossary](../reference/glossary.md) for every term of the forge in
one line). Claude works with the principal on that thinking.

A **source** is an external input: a transcript, an offer, a
document, a standard. Sources live in the project's `sources/`
directory under plain slug filenames. A source may arrive at any
stage of a project, even before the brief. Once registered, a source
is immutable.

A source has one form:

- text, such as a Markdown file or a Markdown extract of a document;
- a functional binary, such as a deck template, a graphic or a logo,
  kept because it is used as a thing.

A set of related files (a downloaded site with its index, a document
with its attachments) lives as one subdirectory `sources/<slug>/`.
Such a set is a **bundle**. It counts as one source with one entry
in the index. A bundle is one of two things:

- a whole that arrived at once, immutable as a whole from its
  registration;
- a stream of one origin that keeps arriving (the issues of a
  repository, the minutes of a standing meeting), which grows file
  by file, each file immutable from its own registration.

A **research** is a durable answer to a question. It lives in the
project's `research/` directory. It takes one of two shapes:

- a single note, dated in its file name (`YYYY-MM-DD-<topic>.md`),
  for one question;
- a bundle, for a research of several questions: the plan and the
  synthesis at its head, and one note per question per engine (an
  engine here is the model that did the searching).

A research is written by Claude through `/research`. It is immutable
once filed. How a research is planned before it is searched and kept
honest is explained in
[How a research is made](../about/the-research.md).

Every `sources/` and `research/` directory carries an **index**, a
file named `00-INDEX.md`. The index is a light catalogue of what the
directory holds and what each resource is for.

## How it works

### Registering a source

`/ingest` stores a source, registers it and catalogues it in the
index. It does nothing more. The steps you follow are on
[Register a source](../use/register-a-source.md). The command takes
a file or text pasted into the conversation. Run bare, it sweeps
`sources/` for files nobody has registered yet.

Before anything is stored, personal matter stops the command.
Personal matter is a named private person, an identifying detail,
health, or anything of that kind. Claude asks the principal what to
do with it before the store, never after.

Every binary file gets one question at the ingest: convert it to
Markdown? On yes, the script `scripts/doc2md.py` writes the extract,
and the extract is the source. The original is not copied into the
project. On no, the binary itself is the source. Keeping both is the
exception, on the principal's explicit word. Extracts are always made
by that one script and never by parsing a file some other way.

The sweep also reports files that changed since their registration,
with a question about each. In a thought project, a changed source is
a breach of immutability. It is settled in one of three ways:

- a new source is stored beside it;
- the original is restored;
- the change is knowingly accepted.

In a library project, a changed source is the normal case: it is the
owner's maintenance, and its index entry is corrected.

### Registration is not intake

Registering a source says nothing about how it will be used. What a
source is for is individual to it. It may be a standard to verify
against, an inspiration, a counter-example, a meeting record, or
material to absorb.

That purpose is the principal's word. Before the index entry is
written, Claude always asks what the source is for. The answer is
written as the entry's free-text **Role**. The principal may instead
tell Claude to infer the role. The inferred role is then written
marked *(inferred)*. Claude never infers the role unasked.

The principal alone directs how and when each source is used. When
the content of a source does enter the intent, that is his explicit
act. It is cited with provenance: the path to the file, down to the
single file inside a bundle.

### The index

The index of `sources/` has one entry per source. Each entry has
fixed fields in free text:

- **What:** what the resource is;
- **Origin:** where it came from;
- **Date:** best effort, taken from the content, the file or the
  ingest, and never asked of the principal;
- **Form:** text, an extract of an original, or a binary;
- **Role:** what the principal says the source is for;
- **Use for:** the questions it answers best.

The index of `research/` has one entry per note, with three fields:

- **Question:** what the note set out to answer;
- **Answer in short:** the conclusion in a few lines;
- **Consult when:** the situations in which the note is worth
  opening.

A bundle keeps its own `00-INDEX.md` inside it. Its header names the
bundle, its date and its origin. Its opening paragraph says what the
bundle is and whether it arrived whole or grows. Each file inside has
an entry with the same fields as a source entry. The top index shows
the bundle as one entry pointing to that inner index: two levels,
never deeper. The top index never repeats the bundle's contents.

`/ingest` and `/research` write the entries. `/check` verifies each
index against its directory. The index is freely rewritten, while
the files it catalogues stay immutable.

The index tracks nothing: no processing state, no positions. It is
an automatic input of no command. No command confronts the chain
with the resources on its own, and a contradiction between the
intent and a resource is not a finding. Claude reaches for a file by
its own judgement, or when the principal asks.

The ledger (the record of a project's state, built from its
documents each time it is read) holds registration only. Its Sources
and Research tables carry no description of the content.

## Why

**Sources are immutable.** The reason for immutability as such is not
recorded. What follows from it is recorded. A source travels into
git from its registration, so what has entered cannot be taken back.

**Personal matter stops the ingest before the store.** A source is
immutable from its registration and travels into git. What has
entered cannot be taken back, so the question has to come before the
store.

**A source has one form.** The repository carries what the forge
works with, and that is text. A binary nobody reads from git is
weight without use. A binary that is used as a thing is kept because
it is used.

**Registration is not intake.** A source's purpose differs from
source to source, so storing it cannot decide how it is used. The
role is asked before the entry is written so that the entry carries
its role from its birth and no later hand changes it.

**Source content enters the intent only by the principal's act.**
What someone said in a meeting is never silently promoted to the
principal's own position.

**The index tracks nothing and feeds no command.** A source may be a
counter-example, a mere inspiration or a record of what someone else
said. A contradiction between it and the intent is therefore no
defect of the intent. The index is a working aid so that Claude and
the principal know what exists and what it is for without re-reading
the files.

**One shape for every index.** Role and Use for are what an index is
for, and a table does not carry them.

**The ledger holds registration only.** Nothing is described in two
places.

**Research is kept.** For key topics Claude researches current best
practice rather than inventing. Durable findings are stored in
`research/` so that they are not left in the conversation. Why a
research note is immutable is not recorded. The steps of a research
are on [Research a topic](../use/research-a-topic.md).

## A worked example

A generic entry of a `sources/` index, for an extract of a standard
the principal wants to check his work against:

```markdown
### `example-standard.md`
- **What:** An extract of a published standard for the subject of the project.
- **Origin:** The standard's publisher, downloaded as a PDF.
- **Date:** 2026-01-01, from the content
- **Form:** extract of example-standard.pdf
- **Role:** a standard to verify against
- **Use for:** checking whether the requirements cover what the standard asks
```

The Role is the principal's answer to "what is it for?". The Date
came from the document itself and was not asked for. The Form says
the PDF was converted, so the extract is the source and the PDF is
not in the project.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [How a research is made](../about/the-research.md): how a research
  is planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
