---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - templates/index.md
  - templates/index-bundle.md
  - projects/forge/10-intent.md
---

# About sources and research

This page explains the two kinds of resource a project of the forge
holds beside its chain: sources, the external inputs as they
arrived, and research, the durable answers to questions. It is for
someone who uses the forge and wants to know how material from
outside is kept and why, and for someone weighing whether the forge
handles outside material soundly. It was put together from the rules
in `CLAUDE.md` (Document chain: External inputs and Resource
indexes), the index skeletons `templates/index.md` and
`templates/index-bundle.md`, and the positions of the forge's own
intent (`projects/forge/10-intent.md`) that give the reasons.

## Sources

A source is an external input: a transcript, an offer, a document, a
standard. Sources live in the project's `sources/` directory under
plain slug filenames. They may arrive at any stage of a project's
life: before the brief, as material for writing it, during work on
the intent, or after. The date a source came from is recorded on a
best-effort basis in the ledger and is never demanded.

A source is immutable once it is registered. It is never edited;
corrections happen downstream, in the documents that use it.

`/ingest` stores, registers and catalogues a source, and nothing
more. Run without arguments, it sweeps `sources/` for files dropped
there by hand and registers them. It also takes text pasted into the
conversation, not only a file.

### One form per source

A source has one form: it is either text or a functional binary,
never both by default. When a binary arrives, `/ingest` asks once
whether to convert it to Markdown. If the answer is yes, the
Markdown extract becomes the source and the original is not kept in
the project. If the answer is no, the binary is kept as a functional
thing: a deck template, a graphic, a logo. Keeping both is an
exception that needs the principal's explicit word.

The reason is that the repository carries what the forge works with,
which is text. A binary nobody reads from git is weight without use;
a binary that is used as a thing is kept because it is used.

Extracts are made by one script of the forge, `scripts/doc2md.ps1`,
and never by ad-hoc parsing: no improvised PDF reading, no manual
transcription.

### Bundles

A set of related files, such as a downloaded site with its index or
a document with its attachments, may live together as a subdirectory
`sources/<slug>/`. A bundle counts as one source with one ledger
entry and is immutable as a whole from registration. Detail at the
level of single files is not lost: where the intent cites a bundle,
it cites the individual file by path. If the files of a bundle ever
need separate fates, a file can be split out to its own ledger row.

Every bundle carries its own catalogue, a `00-INDEX.md` inside it,
which `/ingest` creates at registration if it is missing. Its header
records the bundle, the project, a date and where the whole came
from; a short paragraph says what the bundle is and why it entered
the sources; each file then gets the same fields as an entry in the
directory's index.

## Registration is not intake

Registering a source says nothing about what it is for. A source may
be a standard to verify against, an inspiration, a counter-example, a
record of a meeting or material to absorb, and that role is
individual to each source. The role is the principal's word: after
registration he is asked once what the source is for, and the answer
is recorded as free-text Role in the resource index. Until he gives
it, the Role stays empty; it is never inferred unasked. If he asks
for the role to be inferred, it is written marked as inferred. The
ledger row records registration only.

The principal alone directs how and when a source is used. When the
content of a source does enter the intent, that is his explicit act,
cited with provenance to the file. What someone said in a meeting is
never silently promoted to the principal's own position: the intent
holds what he holds, and what others said stays theirs until he takes
it up.

### When personal matter stops an ingest

Before storing, `/ingest` stops and asks when the input carries
personal matter: a named private person, an identifying detail,
health, anything of the kind. The command goes on only on the
principal's answer.

## Research

Research is a durable answer to one question. For key topics the
forge looks up current best practice rather than inventing; outside
inspiration is a legitimate input. What is found is stored in the
project's `research/` directory as a dated note,
`research/YYYY-MM-DD-<topic>.md`, so that it is not left in a
conversation and lost with it. `/research` writes the note and
indexes it.

A research note is immutable from its creation. Like a source, it is
never edited; a later question gets a note of its own, and
corrections happen downstream.

## Resource indexes

Every `sources/` and `research/` directory carries a `00-INDEX.md`,
the resource index. It is a light catalogue, so that the principal
and Claude know what resources exist and what they are for without
re-reading the files. Each entry has fixed fields in free text:

| Directory | Fields of an entry |
|---|---|
| `sources/` | What, Origin, Role, Use for |
| `research/` | Question, Answer in short, Consult when |

The index has one shape for every directory, because Role and Use
for are what an index is for and a table would not carry them. A
bundle appears in the directory's index as one entry pointing to its
inner index: two levels, never deeper, and the top index never
repeats what the bundle's own index lists. The ledger holds
registration only, so that nothing is described in two places.

The index is a working aid, not a record of thinking. It tracks
nothing: no processing state, no positions. Unlike the immutable
files it catalogues, it is freely rewritten, like the ledger.
`/ingest` and `/research` write its entries, and `/check` verifies
the index against the directory.

### Why the index feeds no command

The index is an automatic input of no command. The commands that
work the chain and the reviewers do not confront the chain with the
material on their own, so a contradiction between the intent and a
source is not a finding. The reason is that a source may be a
counter-example, a mere inspiration or a record of what someone else
said: disagreeing with it may be exactly the point. A file is
reached for by judgement or on request, for example when the
principal asks for an assessment to be checked against the
requirements in a given file.

## See also

- [Register a source](../use/register-a-source.md): the ingest procedure.
- [Research a topic](../use/research-a-topic.md): the research procedure.
