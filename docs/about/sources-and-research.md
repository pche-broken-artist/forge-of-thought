---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: e466f701cb51122e
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

A source is an external input to a project, kept as it arrived, and a
research is a durable answer to a question, kept beside it. This page
explains for the user and the evaluator of the forge why sources are
immutable, why registering a source does not mean using it, what a
research is for, and what the indexes of both directories hold.

## What it is

A project has two directories of resources:

- `sources/`: the external inputs, such as transcripts, offers,
  documents and standards.
- `research/`: the research notes, each a durable answer to one
  question.

A source may arrive at any stage of a project, even before the brief
(the principal's own short text of what he wants). The principal is
the person whose thinking is being forged, and he has the final word
on all content.

A source lives in `sources/` under a plain slug filename. It is
immutable once registered: from that moment it is never edited, and
corrections happen downstream.

A source has one form. It is either text or a functional binary,
never both by default. A binary such as a document can be converted
to a Markdown extract, and then the extract is the source and the
original is not copied into the project. A binary that is used as a
thing, such as a deck template, a graphic or a logo, stays the source
as it is. Keeping both forms is the exception, on the principal's
explicit word.

A set of related files is a bundle. A downloaded site with its index,
or a document with its attachments, lives as a subdirectory
`sources/<slug>/` and counts as one source. A bundle is one of two
kinds:

- a whole that arrived at once: immutable as a whole from its
  registration.
- a stream of one origin that keeps arriving, such as the issues of a
  repository or the minutes of a standing meeting: it grows file by
  file, each file immutable from its own registration.

A research is either a single note or a bundle. A single note answers
one question. A research of several questions is a bundle: the plan
and the synthesis stand at its head, and there is one note per
question per engine (the model family that answered it). A research
is immutable, and its filename opens with its date. How a research is
planned before it is searched and kept honest is explained in
[How a research is made](the-research.md).

## How it works

### Registration is not intake

Registering a source means storing it, recording it and cataloguing
it, and nothing more. The command that registers is `/ingest`; the
steps are in [Register a source](../use/register-a-source.md).

What a source is for is individual. One source is a standard to verify
against, another an inspiration, a counter-example, a meeting record,
or material to absorb. That purpose is the source's Role, a free-text
field of its index entry.

The Role is the principal's word, never inferred unasked. Before the
entry is written, Claude asks what the source is for. The principal
answers with the role, or tells Claude to infer it, and an inferred
role is written marked *(inferred)*. Asking first is so that the entry
carries its role from its birth and no later hand changes it.

The principal alone directs how and when a source is used, in
whatever work he chooses. Content of a source enters the intent (the
document of the principal's positions, the trunk of every project)
only by his explicit act. That act cites the source file as
provenance. A bundle is cited file by file, by path. This rule is so
that what someone said in a meeting is never silently promoted to the
principal's own position.

### Personal matter stops an ingest before the store

Before a source is stored, personal matter stops `/ingest`, and
Claude asks the principal. Personal matter is a named private person,
an identifying detail, health, or anything of the kind. The question
comes before the store because a source is immutable from its
registration and travels into git. What has entered cannot be taken
back.

### A changed source

The principal may drop files into `sources/` by hand at any time.
`/ingest` without arguments sweeps the directory: it registers new
files and asks about each file that changed since its registration.
What a change means depends on the kind of project:

- in a thought project: a breach of immutability, settled by a new
  source beside it, the original restored, or the change knowingly
  accepted.
- in a library (a project of shared material with no chain): the
  normal case, the owner's maintenance; the entry is corrected and its
  date moved.

### The index

Every `sources/` and `research/` directory carries a `00-INDEX.md`,
the resource index. It is a light catalogue, so that Claude and the
principal know what resources exist and what they are for without
re-reading the files. Its skeleton is `templates/index.md`.

The index tracks nothing: no processing state and no positions. It is
freely rewritten, while the files it catalogues stay immutable.

The index is an automatic input of no command. Neither the work on an
artefact nor a reviewer confronts the chain with the material on its
own. A contradiction between the intent and a source is not a
finding (the result of a reviewer). The reason is that the source may
be a counter-example, a mere inspiration or a record of what someone
else said. Claude reaches for a file by its own judgement, or when the
principal asks.

Each entry of a source has fixed fields in free text:

- **What:** what the resource is.
- **Origin:** where it came from.
- **Date:** best effort, taken from the content, the file or the
  ingest, and never asked of the principal.
- **Form:** text, an extract of an original, or a binary.
- **Role:** what the source is for, in the principal's word.
- **Use for:** the questions it answers best.

Each entry of a research has three fields:

- **Question:** what the note set out to answer.
- **Answer in short:** the conclusion in a few lines.
- **Consult when:** the situations in which the note is worth opening.

A bundle appears in the top index as one entry that points into the
bundle. The bundle carries its own `00-INDEX.md` inside, created at
registration where it lacks one, from the skeleton
`templates/index-bundle.md`. Its header names the bundle, its date and
its origin. Its opening paragraph says what the whole is, why it
entered `sources/`, and whether it arrived whole or grows. Each file
of the bundle has the same entry as a source in the top index. There
are two levels, never deeper, and the top index never repeats the
contents of a bundle.

The ledger (the state of a project, made from its documents when it is
read) holds registration only: a table of sources and a table of
research, with no content columns.

## Why

- Durable findings are kept in `research/` rather than left in the
  chat, because the forge researches current practice for key topics
  rather than inventing.
- A source has one form because the repository carries what the forge
  works with, which is text. A binary that nobody reads from git is
  weight without use. A binary that is used as a thing is kept because
  it is used.
- The Role is asked before the entry is written so that the entry
  carries it from its birth.
- Source content enters the intent only by the principal's explicit
  act so that nothing someone else said becomes his position in
  silence.
- Personal matter is asked about before the store because what has
  entered an immutable source in git cannot be taken back.
- The index is no automatic input because a source may stand against
  the intent on purpose, as a counter-example or another person's
  record.
- The ledger holds registration only so that nothing is described in
  two places.
- Every index has one shape of free-text fields because Role and Use
  for are what an index is for, and a table does not carry them.
- Why a source is immutable once registered, beyond the point about
  personal matter: the reason is not recorded.
- Why a research note is immutable: the reason is not recorded.

## A worked example

A generic entry of a source in the top index, for an extract of a
standard; every value is a placeholder:

```markdown
### `<example-standard>.md`
- **What:** the text of an industry standard for a process, extracted from its published document.
- **Origin:** the publisher's website.
- **Date:** YYYY-MM-DD, from the content
- **Form:** extract of <example-standard>.pdf
- **Role:** a standard to verify against
- **Use for:** checking whether a requirement names every step the standard demands.
```

How to run a research of your own is in
[Research a topic](../use/research-a-topic.md). Every term of the
forge is defined in one line in the [Glossary](../reference/glossary.md).

## See also

- [Register a source](../use/register-a-source.md): the ingest procedure.
- [Research a topic](../use/research-a-topic.md): the research procedure.
- [How a research is made](the-research.md): how a research is planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
