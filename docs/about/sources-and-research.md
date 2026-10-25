---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: ea175bbe31d5b105
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
beside its chain of documents. A source is an external input as it
arrived. A research is a durable answer to a question. This page
explains why sources are immutable, why registering a source is not
the same as taking it into the thinking, and what a research is for.
It is written for anyone who uses the forge and for anyone weighing
whether its handling of material can be trusted.

## What it is

A **source** is an external input: a transcript, an offer, a
document, a standard. Sources live in the project's `sources/`
directory under plain slug filenames. They may arrive at any stage of
a project, even before its brief.

A source is immutable once it is registered. Each source has one
form:

- text: a file the forge reads as it stands;
- a Markdown extract: the text made from a binary file, which then
  is the source;
- a functional binary: a file used as a thing, such as a deck
  template, a graphic or a logo.

A set of related files (for example a downloaded site with its index)
lives as a subdirectory `sources/<slug>/`. Such a set is called a
bundle, and it counts as one source.

A **research** is a durable answer to one question. It comes in one
of two shapes:

- a single note: one question answered in one file, named by its
  date and topic (`YYYY-MM-DD-<topic>.md`);
- a bundle: a research of several questions, with the plan and the
  synthesis at its head and one note per question per engine (an
  engine is the model that searched and wrote the note).

A research is immutable: it is never edited after it is filed. How a
research is planned before it is searched and kept honest is
explained in [How a research is made](the-research.md).

Every `sources/` and `research/` directory carries an index, the file
`00-INDEX.md`. The index is a light catalogue of what exists in the
directory and what each item is for.

## How it works

### Registration is not intake

The command `/ingest` stores a source, registers it and catalogues it
in the index. It does nothing more. How you run it is shown in
[Register a source](../use/register-a-source.md).

Registering a source does not take its content into the project's
thinking. What a source is for is individual: a standard to verify
against, an inspiration, a counter-example, a meeting record,
material to absorb. That purpose is the Role field of the source's
index entry.

The Role is the word of the principal (the person whose thinking is
being forged). Before the entry is written, Claude asks what the
source is for. The principal answers with the role, or tells Claude
to infer it. An inferred role is written marked *(inferred)*. Claude
never infers a role unasked.

The principal alone decides how and when a source is used. When the
content of a source does enter the intent (the project's statement of
the principal's positions), that is his explicit act. The intent then
cites the file the content came from.

### One form per source

At `/ingest` every binary file gets one question: convert it to
Markdown? On yes, the script `scripts/doc2md.py` writes the extract,
and the extract is the source; the original is not copied into the
project. On no, the binary itself is the source. Keeping both is the
exception, on the principal's explicit word.

### Personal matter stops the ingest

Before a source is stored, personal matter stops the command and
Claude asks. Personal matter is a named private person, an
identifying detail, health, or anything of the kind.

### Bundles

A bundle is one of two things, and its index's opening paragraph says
which:

- a whole that arrived at once, immutable as a whole from its
  registration;
- a stream of one origin that keeps arriving (the issues of a
  repository, the minutes of a standing meeting), which grows file
  by file through `/ingest --bundle <name>`, each file immutable from
  its own registration.

Every bundle carries its own `00-INDEX.md`, created by `/ingest` at
registration where the bundle lacks one. Its header names the bundle,
the project, a date and the origin of the whole. Each file in it has
an entry with the same fields as a source entry in the top index.

### The index

The index of a directory tracks nothing. It holds no processing state
and no positions. It is an automatic input of no command: no command
confronts the chain with the material on its own. Claude reaches for
a file by its own judgement or when the principal asks.

A contradiction between the intent and a resource is therefore not a
finding (a finding is a reviewer's result).

The index has two levels and never more. A bundle appears in the top
index as one entry that points to the bundle's own index, and the top
index never repeats the bundle's contents.

A source's date, origin and form are fields of its index entry. The
date is recorded on a best-effort basis, from the content, the file
or the day of the ingest, and is never demanded from the principal.

The index is freely rewritten, while the files it catalogues stay
immutable. `/ingest` writes the entries for sources and `/research`
for research. The ledger (the table of the project's state, made from
its documents when it is read) holds registration only: a row per
source and per research, with no content.

### In a library

In a library project (a project of shared material with no chain),
a changed source is the owner's normal maintenance: the index entry
is corrected and its date moved. In a thought project, a changed
source is a breach of immutability to be settled. The principal
settles it by adding a new source beside it, by restoring the
original, or by accepting the change knowingly.

### Research

Research is how Claude looks up current practice on a key topic
instead of inventing. Outside inspiration is a legitimate input. How
you start one is shown in [Research a topic](../use/research-a-topic.md).

## Why

- **Why a source is immutable.** A source travels into git from its
  registration, so what has entered cannot be taken back. The broader
  reason a source may not change after registration is not recorded.
- **Why personal matter stops the ingest before the store.** A source
  is immutable from its registration and travels into git. What has
  entered cannot be taken back, so the question must come before the
  store.
- **Why the role is asked before the entry is written.** The entry
  carries its role from its birth, so that no later hand changes it.
- **Why source content enters the intent only by the principal's act.**
  What someone said in a meeting is never silently promoted to the
  principal's own position.
- **Why one form per source.** The repository carries what the forge
  works with, which is text. A binary nobody reads from git is weight
  without use. A binary that is used as a thing is kept because it is
  used.
- **Why the index tracks nothing and feeds no command.** A source may
  be a counter-example, a mere inspiration or a record of what someone
  else said. A contradiction with it therefore says nothing about the
  quality of the intent.
- **Why the ledger holds registration only.** Nothing is described in
  two places.
- **Why one shape for every index, with free-text fields.** Role and
  Use for are what an index is for, and a table does not carry them.
- **Why research is stored.** Durable findings belong in `research/`,
  not left in the conversation.
- **Why a research is immutable.** The reason is not recorded.

## A worked example

A generic entry of a `sources/` index, in the shape the index
template gives. The names are placeholders.

```markdown
### `example-standard.md`
- **What:** An industry standard for the topic of the project.
- **Origin:** The publisher's website.
- **Date:** 2026-01-15, from the content
- **Form:** extract of example-standard.pdf
- **Role:** a standard to verify against
- **Use for:** checking whether the requirements cover its clauses
```

A research entry has three fields instead: Question, Answer in short
and Consult when.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [How a research is made](the-research.md): how a research is
  planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
