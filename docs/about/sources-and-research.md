---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 1fc0e15e0bcf6db1
inputs:
  - CLAUDE.md#Document chain
  - templates/index.md
  - templates/index-bundle.md
  - projects/forge/10-intent.md#POS.0050
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.0840
  - projects/forge/10-intent.md#POS.1040
---

# Sources and research

A source is an external input kept as it arrived, and a research
note is a durable answer to one question; together they are the
resources a project keeps beside its chain of documents. This page
says what each is, how it is stored and catalogued, why a source is
immutable, why registering a source is not the same as taking it
into the thinking, and why an ingest stops before it stores anything
when it meets personal matter. It is written for the user of the
forge and for an evaluator who wants to judge the rules. The
procedures are on the how-to pages linked under See also.

## What it is

### A source

A source is an external input to a project: a transcript, an offer,
a document, a standard, or text pasted into the conversation. It
lives in the project's `sources/` directory under a plain slug
filename. A source may arrive at any stage of a project's life:
before the [brief](../reference/glossary.md) as material for writing
it, during the work on the intent, or after. From its registration
on, a source is immutable.

A source has one form. A file in `sources/` is either text or a
functional binary, never both by default. A binary is converted to a
Markdown extract only on the explicit word of the principal (the
person whose thinking is forged); the extract is then the source,
and the original is not copied into the project. Where the principal
says no, the binary is the source as a functional thing, such as a
deck template, a graphic or a logo. Keeping both the binary and the
extract is the exception, again on the principal's explicit word.
Extracts are produced by one script of the forge,
`scripts/doc2md.py`, never by ad-hoc parsing.

A set of related files may live as a bundle: a subdirectory
`sources/<slug>/`. Examples are a downloaded site with its index, or
a document with its attachments. A bundle counts as one source with
one entry in the ledger (the project's single source of truth for
state) and is immutable as a whole from its registration. File-level
detail is not lost: provenance in the intent cites individual files
of the bundle by path, and the bundle's own index lists its contents.
Isolated files stay directly in `sources/`.

### A research note

A research note is a durable answer to one question. Claude
researches current best practice for key topics rather than
inventing; outside inspiration is a legitimate input. What it finds
and what is worth keeping is stored in the project's `research/`
directory, not left in the conversation. A note is a dated file,
`YYYY-MM-DD-<topic>.md`, and like a source it is immutable once
written.

### The resource index

Every `sources/` and every `research/` directory carries a
`00-INDEX.md`, the resource index. It is a light catalogue of what
exists in the directory and what it is for, in fixed fields written
in free text. It is a working aid, not a record of thinking: it
tracks nothing, neither a processing state nor a position, and it is
an automatic input of no command. Unlike the files it catalogues,
the index is freely rewritten, like the ledger.

## How it works

### Registration

The command `/ingest` stores a source, registers it and catalogues
it, and does nothing more. Without arguments it sweeps `sources/`:
it registers files the principal has dropped there by hand and
reports files changed since their registration, with a question what
to do with each. The command also takes text pasted into the
conversation. How the command is run is the page
[Register a source](../use/register-a-source.md).

Before anything is stored, personal matter stops the command and
asks. Personal matter is a named private person, an identifying
detail, a matter of health, or anything of that kind.

At the ingest, every binary file gets one question: convert to
Markdown? Yes means the extract becomes the source; no means the
binary is the source as a functional thing.

The date of origin is recorded best-effort in the ledger and is
never demanded from the principal.

After registration, Claude asks the principal once what the source
is for. The answer is the source's Role, free text in the resource
index. The Role stays empty until the principal gives it and is
never inferred unasked. The principal may instead tell Claude to
infer it; the inferred Role is then written marked *(inferred)*.

The ledger holds registration only: a Sources table and a Research
table, with no content columns. What a source is and what it is for
stands in the index alone.

### Intake

Registration does not imply intake. What a source is for is
individual: a standard to verify against, inspiration, a meeting
record, material to absorb. The principal alone directs how and when
each source is used, in whatever work he chooses.

When content of a source does enter the intent, it is the
principal's explicit act, cited with provenance to the file. What
someone said in a meeting is never silently promoted to the
principal's own position.

### A changed source

A sweep by `/ingest` reports a file that changed after its
registration. What that means depends on the kind of the project. In
a thought project the change is a breach of immutability, settled in
one of three ways:

- a new source is registered beside the changed one,
- the original is restored,
- the change is knowingly accepted.

In a library project a changed file is the normal case, the owner's
maintenance: the date in the ledger is moved and the index entry is
corrected.

### The index at work

The index has one shape for every directory. A sources entry carries
four fields:

- **What**: what the resource is, in one or two sentences.
- **Origin**: where it came from, such as an author, a URL or a
  meeting, with the date as far as it is known.
- **Role**: free text, the principal's word on what the source is
  for.
- **Use for**: what to reach for the file for, that is, the
  questions it answers best.

A research entry carries three fields:

- **Question**: what the note set out to answer.
- **Answer in short**: two or three lines of the conclusion.
- **Consult when**: the situations in which the note is worth
  opening.

A bundle keeps its own `00-INDEX.md` inside and appears in the top
index as one entry pointing into it. The bundle index is the same
catalogue one level down: its own header and opening paragraph say
what the whole bundle is and why it entered `sources/`, and each file
of the bundle gets the fields of a sources entry. There are two
levels, never deeper, and the top index never repeats the bundle's
contents. Where a bundle lacks its index, `/ingest` creates it at
registration.

`/ingest` writes the entries of the sources index and `/research`
those of the research index; how research is run is the page
[Research a topic](../use/research-a-topic.md). The check of the
forge verifies that the index agrees with the directory.

No command reads the index on its own. The state map of a project,
the critics and the challengers do not confront the chain with the
material by themselves. A contradiction between the intent and a
source is not a finding. Claude reaches for a file by its own
judgement or when the principal asks, for example "check the
assessment against the requirements in file X".

## Why

Research is kept in `research/` so that durable findings are not
lost in the conversation. The reason behind researching at all is
that current best practice is looked up rather than invented, and
outside inspiration is a legitimate input.

Why a source is immutable from its registration is not recorded in
the inputs of this page. What is recorded is what follows from it:
a source travels into git as it was registered, and a change after
registration in a thought project is a breach to be settled, never
a silent correction.

Personal matter stops an ingest before the store because of that
immutability. A source is immutable from its registration and
travels into git, so what has entered cannot be taken back. The
question must therefore come before the store, not after.

Registration is not intake because what a source is for differs
from source to source. A source may be a counter-example, a mere
inspiration or a record of what someone else said. That is why a
contradiction between the intent and a source is not a finding, and
why no command confronts the chain with the material on its own.
For the same reason, source content enters the intent only by the
principal's explicit act with provenance: what someone else said is
his position only once he has made it so. The inputs record that
the Role is the principal's word; a reason beyond that for asking it
rather than inferring it is not recorded.

A source has one form because the repository carries what the forge
works with, which is text. A binary nobody reads from git is weight
without use. A binary that is used as a thing, such as a template or
a logo, is kept because it is used.

The resource index exists so that Claude and the principal know what
resources exist and what they are for without re-reading the files.
It tracks nothing because it is a working aid, not a record of
thinking. The ledger holds registration only, with no content
columns, so that nothing is described in two places. Every index has
one shape, in free-text fields rather than a table, because Role and
Use for are what an index is for, and a table does not carry them.
The reason for the limit of two levels of index is not recorded.

Dates of origin are recorded best-effort and never demanded because
they are metadata, not ceremony.

## A worked example

One entry of a sources index, as the skeleton shapes it, for a
transcript registered under the slug `kickoff-transcript`:

```
### `kickoff-transcript.md`
- **What:** Transcript of the kickoff meeting of the initiative, as
  exported from the meeting tool.
- **Origin:** The kickoff meeting of 2026-03-02, exported by its
  organiser; the date is the one on the export.
- **Role:** A meeting record: what was said in the room, not the
  principal's position.
- **Use for:** Which objections were raised at the start and what
  was promised to the attendees.
```

The entry shows the rules at work. The filename is a plain slug. The
Role is the principal's word; before he gave it, the field stood
empty. Nothing in the entry says whether the transcript has been
read or what the intent took from it: that is the intent's
provenance, not the index's business. The ledger has one row for the
same file, with its registration and nothing of this content.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
