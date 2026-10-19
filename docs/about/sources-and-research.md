---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: c91a9b0e61851941
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

A source is an external input that a project keeps as it arrived, and
a research note is a durable answer to one question. This page
explains how both are kept, why a source is never changed once it is
registered, why registering a source does not mean using it, and what
the index beside them is for. It is written for anyone who works in a
project and for anyone who evaluates how the forge treats outside
material.

## What it is

A project of the forge holds two directories of resources.

- `sources/` holds the external inputs: transcripts, offers,
  documents, standards. They may arrive at any stage of a project,
  even before the brief.
- `research/` holds the research notes. Each note answers one
  question, and its file name carries its date
  (`YYYY-MM-DD-<topic>.md`).

Both kinds of file are immutable: once a source is registered, or a
research note is written, it is not edited again.

Every `sources/` and `research/` directory carries an index,
`00-INDEX.md`. The index is a light catalogue. It lets Claude and the
principal (the person whose thinking the project forges) know what
resources exist and what they are for without re-reading them. The
[Glossary](../reference/glossary.md) gives every term of the forge in
one line.

## How it works

### A source

A source is stored under a plain slug filename. It is registered by
the command `/ingest`, which stores, registers and catalogues the
file and does nothing more. Run bare, `/ingest` sweeps `sources/` for
files that are not registered yet. The procedure is on
[Register a source](../use/register-a-source.md).

A source has one form. It is either text or a functional binary,
never both by default.

- **Text:** the source is read as it stands.
- **An extract:** a binary such as a PDF or a document is converted
  to Markdown, on the principal's explicit word, by the script
  `scripts/doc2md.py`. The extract is then the source, and the
  original is not copied into the project. Extracts are never made by
  ad-hoc parsing.
- **A functional binary:** a file used as a thing, such as a deck
  template, a graphic or a logo, is kept as the source itself.

Keeping both the binary and its extract is the exception, on the
principal's explicit word.

Before anything is stored, personal matter stops the ingest and
Claude asks. Personal matter is a named private person, an
identifying detail, health or anything of the kind.

A set of related files, such as a downloaded site with its index or a
document with its attachments, is a bundle. A bundle lives as a
subdirectory `sources/<slug>/` and counts as one source with one
ledger entry (the ledger is the project's single record of state).
It is immutable as a whole from its registration. Every bundle
carries its own `00-INDEX.md`, made from the template
`templates/index-bundle.md`, and `/ingest` creates it at registration
where it is missing. Isolated files stay directly in `sources/`.

When a registered source changes, what that means depends on the kind
of project.

- **A thought project** (a project with a chain of documents): a
  changed source is a breach of immutability, to be settled by a new
  source beside it, by restoring the original, or by accepting the
  change knowingly.
- **A library** (a project of shared material, with no chain): a
  changed source is the owner's normal maintenance. Its index entry is
  corrected and its date moved.

### Registration is not intake

Registering a source says only that it is there. What a source is for
is individual: a standard to verify against, inspiration, a meeting
record, material to absorb. That purpose is the principal's word, and
it is written as the free-text Role of the source's entry in the
index. Claude asks what the source is for before the entry is written.
The principal answers with the role, or tells Claude to infer it. An
inferred role is written marked *(inferred)*. A role is never
inferred unasked.

The principal alone directs how and when each source is used. When
the content of a source does enter the intent, that is his explicit
act, cited with provenance to the file. A file of a bundle is cited
by its own path. What someone said in a meeting is never silently
promoted to the principal's own position.

### A research note

For key topics Claude looks up current best practice rather than
inventing. The durable findings are stored in `research/` as a note,
written by the command `/research`. The procedure is on
[Research a topic](../use/research-a-topic.md).

### The index

Each entry of an index has fixed fields in free text, in the shape
the template `templates/index.md` shows.

A source entry holds:

- **What:** what the resource is.
- **Origin:** where it came from, such as an author, a URL or a
  meeting.
- **Date:** taken best effort from the content, the file or the
  ingest, and never asked of the principal.
- **Form:** text, an extract of an original, or a binary.
- **Role:** what the principal says the source is for.
- **Use for:** the questions it answers best.

A research entry holds:

- **Question:** what the note set out to answer.
- **Answer in short:** the conclusion in a few lines.
- **Consult when:** the situations in which the note is worth
  opening.

A bundle appears in the top index as one entry pointing to its inner
index. That is two levels, never deeper, and the top index never
repeats the contents of the bundle. The inner index opens with a
short paragraph on what the whole bundle is and why it entered
sources, then gives one source entry per file.

The index tracks nothing: no processing state and no positions. It is
an automatic input of no command. A contradiction between the intent
and a resource is therefore not a finding. Claude reaches for a file
by its own judgement or when the principal asks. Unlike the files it
catalogues, the index is freely rewritten. `/ingest` and `/research`
write the entries, and `/check` verifies the index against the
directory.

## Why

- **One form per source.** The repository carries what the forge
  works with, which is text. A binary that nobody reads from git is
  weight without use. A binary that is used as a thing is kept because
  it is used.
- **Personal matter stops the ingest before the store.** A source is
  immutable from its registration and travels into git. What has
  entered cannot be taken back, so the question must come before the
  store.
- **Sources are immutable.** The reason is not recorded.
- **Registration is not intake.** A source may be a counter-example, a
  mere inspiration or a record of what someone else said. Because of
  this, the commands do not confront the chain with the material on
  their own, and a contradiction with a source is not a finding.
- **The role is asked before the entry is written.** The entry then
  carries the principal's word from its birth, and the role is never a
  guess of Claude's.
- **Provenance when a source enters the intent.** What someone else
  said stays distinguishable from what the principal holds.
- **Research is stored.** Durable findings belong in `research/`, not
  left in the conversation, and research comes before inventing.
- **An index at all.** Claude and the principal know what exists and
  what it is for without re-reading the files.
- **One shape for every index, in fields of free text.** Role and Use
  for are what an index is for, and a table does not carry them.
- **The ledger holds registration only.** Nothing is described in two
  places.

## A worked example

A generic entry in the index of `sources/`, in the shape the template
gives, for a source taken from no project:

```markdown
### `example-standard.md`
- **What:** An extract of a published standard for writing requirements.
- **Origin:** The standard's publisher, downloaded as a PDF.
- **Date:** 2026-01-15, from the content
- **Form:** extract of example-standard.pdf
- **Role:** a standard to verify against
- **Use for:** checking the wording of requirements before they are written.
```

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
