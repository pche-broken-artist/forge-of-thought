---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 3cb8529952054982
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

Sources are the external inputs of a project, and research notes are
the durable answers Claude has looked up for it. This page explains
why a source never changes once it is registered, why registering a
source does not mean using it, and what a research note is for. It is
written for the person who works with the forge and for the person
who evaluates it. Here the principal is the person whose thinking is
being forged and who has the final word on all content.

## What it is

A **source** is an external input as it arrived. Examples are a
transcript, an offer, a document or a standard. Sources live in the
`sources/` directory of a project. They may arrive at any stage of a
project's life:

- before the brief, as material for writing it;
- during the work on the intent;
- after it.

A source has a plain slug filename and one form. The form is one of
these:

- text;
- an extract, that is a Markdown text made from a binary file, which
  then is the source;
- a functional binary, such as a deck template, a graphic or a logo.

A **bundle** is a set of related files kept together as one source in
a subdirectory `sources/<slug>/`. An example is a downloaded site
with its index, or a document with its attachments. A bundle is one
of two kinds:

- a whole that arrived at once, immutable as a whole from its
  registration;
- a stream of one origin that keeps arriving, such as the issues of a
  repository or the minutes of a standing meeting, which grows file by
  file.

A **research note** is a durable answer to one question. It lives in
the `research/` directory of a project, and its filename opens with
its date: `YYYY-MM-DD-<topic>.md`.

A **resource index** is the file `00-INDEX.md` that every `sources/`
and every `research/` directory carries. It is a light catalogue of
what the directory holds and what each file is for. Every bundle
carries an index of its own inside it.

The terms of the forge used here are each defined in one line in the
[Glossary](../reference/glossary.md).

## How it works

### Registering a source

`/ingest` stores a source, registers it and catalogues it, and does
nothing more. Bare, it sweeps `sources/` for files the principal has
dropped there by hand and registers the new ones. A file of a growing
bundle is added through `/ingest --bundle <name>`. How you run it step
by step is on [Register a source](../use/register-a-source.md).

A binary file gets one question at registration: convert it to
Markdown or not.

- Converted, the extract is the source, and the original is not
  copied into the project.
- Not converted, the binary itself is the source, kept as a
  functional thing.
- Keeping both is the exception, on the principal's explicit word.

Extracts are produced by one script, `scripts/doc2md.py`. They are
never produced by ad-hoc parsing or by manual transcription.

Before anything is stored, personal matter stops the command. A named
private person, an identifying detail or a matter of health are such
matter. Claude then asks the principal what to do before it stores the
file.

### Immutable once registered

From its registration a source is never edited. A file in a bundle
that grows is immutable from its own registration. A sweep that finds
a source changed since its registration reports it with a question.
In a thought project a changed source is a breach of immutability to
be settled in one of these ways:

- a new source is put beside it;
- the original is restored;
- the change is knowingly accepted.

In a library project a changed source is the normal case. It is the
owner's maintenance, and the index entry is corrected and its date
moved.

### Registration is not intake

Registering a source does not mean its content is taken into the
project. What a source is for is individual. It may be a standard to
verify against, an inspiration, a counter-example, a meeting record or
material to absorb.

That purpose is the source's **Role**, a free-text field of its index
entry. The Role is the principal's word. Before the entry is written,
Claude always asks what the source is for. The principal answers with
the role, or tells Claude to infer it. An inferred role is written
marked *(inferred)*.

The principal alone directs how and when a source is used. When the
content of a source does enter the intent, it is the principal's
explicit act, cited with provenance to the file by its path. What
someone said in a meeting is never silently promoted to the
principal's own position. In a bundle the provenance cites the single
file, so that no detail is lost by keeping the files together.

### The resource index

Each entry of an index has fixed fields in free text. The fields are
those of the template `templates/index.md`.

A sources entry holds:

- **What:** what the resource is.
- **Origin:** where it came from.
- **Date:** the date, best effort, from the content, the file or the
  ingest; it is never demanded from the principal.
- **Form:** text, an extract of an original, or a binary.
- **Role:** what the source is for, in the principal's word.
- **Use for:** the questions the source answers best.

A research entry holds:

- **Question:** what the note set out to answer.
- **Answer in short:** the conclusion in a few lines.
- **Consult when:** the situations in which the note is worth
  opening.

A bundle appears in the top index as one entry that points to the
bundle's own index. The nesting has two levels and never more. The
top index never repeats the bundle's contents. The bundle's index has
its own header, with the bundle's slug, the project, a date and the
origin of the whole. Its opening paragraph says what the bundle is,
why it entered the sources, and whether it arrived whole or grows. Its
per-file entries have the fields of a sources entry, in the same
order. `/ingest` creates the bundle's index at registration where it
is missing.

The index tracks nothing. It holds no processing state and no
positions. It is an automatic input of no command: neither `/forge`
nor `/critique` nor the challengers confront the chain with the
material on their own. A contradiction between the intent and a
resource is therefore not a finding. Claude reaches for a file by its
own judgement, or when the principal asks.

Unlike the files it catalogues, the index is freely rewritten.
`/ingest` writes the entries for sources and `/research` writes them
for research. `/check` verifies that the index agrees with the
directory. The ledger (the project's single source of truth for
state) shows registration only, with no columns for content.

### Research

For key topics Claude looks up current best practice rather than
inventing. Outside inspiration is a legitimate input. The durable
findings are stored as a research note in `research/`, not left in
the conversation. How a research run goes is on
[Research a topic](../use/research-a-topic.md).

## Why

- **Why a source is immutable.** The reason is not recorded.
- **Why personal matter stops an ingest before the store.** A source
  is immutable from its registration and travels into git. What has
  entered cannot be taken back. So the question must come before the
  file is stored.
- **Why a source has one form.** The repository carries what the
  forge works with, and that is text. A binary nobody reads from git
  is weight without use. A binary that is used as a thing is kept
  because it is used.
- **Why registration is not intake.** A source may be a
  counter-example, a mere inspiration or a record of what someone else
  said. Its content is not the principal's position until he makes it
  so.
- **Why the Role is asked before the entry is written.** The entry
  then carries its role from its birth, and no later hand changes it.
- **Why the index is an automatic input of no command.** A
  contradiction between the intent and a source is not a defect,
  because the source may be a counter-example, a mere inspiration or a
  record of what someone else said. The index is a working aid, not a
  record of thinking.
- **Why there is an index at all.** Claude and the principal know what
  resources exist and what they are for without re-reading the files.
- **Why one shape of entry, in free text.** Role and Use for are what
  an index is for, and a table does not carry them.
- **Why the ledger shows registration only.** Nothing is described in
  two places.
- **Why research is stored in files.** The reason given is only that
  durable findings belong in `research/` and not in the conversation;
  a further reason is not recorded.

## A worked example

A generic sources entry, taken from no project, for an offer received
as a PDF and converted to Markdown:

```markdown
### `supplier-offer.md`
- **What:** A supplier's offer for a hosted ticketing service, with prices and service levels.
- **Origin:** Sent by the supplier's sales team as a PDF.
- **Date:** 2026-01-15, from the content
- **Form:** extract of supplier-offer.pdf
- **Role:** A counter-example: what the project does not want to buy. *(inferred)*
- **Use for:** Comparing service levels; the questions to ask the next supplier.
```

The Role here was inferred because the principal told Claude to infer
it, and it is marked so. Because the Role says counter-example, a
contradiction between this offer and the intent is expected, not a
finding.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
