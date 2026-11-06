---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 49d57045158abee7
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

Sources and research are the resources of a project: the external
material that arrived and the durable answers Claude found to the
project's questions. This page explains what they are, how they are
kept and why they are kept that way, for anyone who works with a
project or judges how the forge treats what it did not make. It
explains; the procedures are [Register a source](../use/register-a-source.md)
and [Research a topic](../use/research-a-topic.md).

## What it is

A **source** is an external input as it arrived: a transcript, an
offer, a document, a standard. It lives in the project's `sources/`
directory under a plain slug filename and is immutable once
registered. A source has one form. It is either text or a functional
binary (a deck template, a graphic, a logo), never both by default.
A binary is turned into a Markdown extract only on the explicit word
of the principal (the person whose thinking is being forged); the
extract is then the source, and the original is not copied into the
project. Sources may arrive at any stage of a project's life, before
the brief as material for writing it, during the work on the intent,
or after.

A set of related files is a **bundle**: a subdirectory
`sources/<slug>/` that counts as one source with one entry in the
index and one row in the ledger (the project's state report, made at
read time). A bundle is one of two things. Either it is a whole that
arrived at once, immutable as a whole from its registration. Or it is
a stream of one origin that keeps arriving, such as the issues of a
repository or the minutes of a standing meeting; such a bundle grows
file by file, each file immutable from its own registration. Which of
the two a bundle is, its own index says in its opening paragraph.

A **research** is a durable answer to one question, stored in
`research/` rather than left in the conversation. A research of one
question is a single note for one card (one question of the plan) on
one engine (one model family). A research of several questions is a
bundle: a plan and a synthesis at its head, and one note per card per
engine. A research is dated and immutable from its filing. It is
planned before it is searched and, where it carries weight, run on
two model families; how that is done and kept honest is
[How a research is made](the-research.md).

Every `sources/` and every `research/` directory carries an
**index**, `00-INDEX.md`: a light catalogue of what exists there and
what it is for, so that Claude and the principal know the resources
without re-reading the files. A bundle carries an index of its own
inside and appears in the directory's index as one entry pointing
into it: two levels, never deeper. The index is freely rewritten,
like the ledger, while the files it catalogues stay immutable. The
other terms of the forge used on this page are in the
[Glossary](../reference/glossary.md).

## How it works

`/ingest` stores, registers and catalogues a source, and does nothing
more. Called bare, it sweeps `sources/` for unregistered files. For a
binary it asks one question, whether to convert it to Markdown;
extracts are produced by one script of the forge,
`scripts/doc2md.py`, never by ad-hoc parsing. A file of a growing
bundle is added through `/ingest --bundle <name>`, with its own entry
in the bundle's index.

Before a source is stored, personal matter stops the command. A named
private person, an identifying detail, health, anything of the kind,
is put to the principal as a question before anything is written.

Registration is not intake. What a source is for is individual: a
standard to verify against, an inspiration, a counter-example, a
meeting record, material to absorb. That purpose is the principal's
word, asked before the index entry is written and never inferred
unasked; he answers with the role, or tells Claude to infer it, and an
inferred role is written marked *(inferred)*. The answer stands in the
entry as its free-text Role. The ledger's row shows registration
only. The principal alone directs how and when a source is used, in
whatever work he chooses. When source content does enter the intent
(the trunk artefact of the chain, the principal's positions), it is
his explicit act, cited with provenance to the file; where the source
is a bundle, the citation names the individual file by path.

The index tracks nothing: no processing state, no positions. It is an
automatic input of no command. `/forge`, `/critique` and the
challengers do not confront the chain with the material on their
own, and a contradiction between the intent and a resource is not a
finding (a reviewer's result). Claude reaches for a file by its own
judgement or when the principal asks, for example to check an
assessment against the requirements in a named file. `/ingest` and
`/research` write the entries; `/check` verifies the index against
the directory.

Each entry has fixed fields in free text. A source's entry carries
what the resource is, its origin, its date, its form, its Role and
what to reach for it for. The date is best effort, taken from the
content, the file or the ingest, and never demanded from the
principal. A research entry carries the question, the answer in
short and when to consult the note. A bundle's own index has a
header with the bundle's slug, project, date and origin, an opening
paragraph that says what the whole is and whether it arrived whole or
grows, and then one entry per file in the same shape as a source
entry of the directory index. The directory index never repeats the
bundle's contents.

A changed source is read according to the project's kind. In a
thought project a source changed since its registration is a breach
of immutability; the bare `/ingest` reports it with a question, and
it is settled by a new source beside it, by restoring the original or
by knowingly accepting the change. In a library project a changed
file is the owner's normal maintenance: the index entry is corrected
and its date moved.

## Why

A source and a research note are immutable because they record a
moment: a state of the world the forge did not make and has no
business editing. A newer state is a new file. A research is run
again rather than amended. A document that arrives in a new version
becomes a further file of a bundle of one origin, whose index says
which is the newest and which it supersedes. This is so that every
citation of the intent keeps pointing at the text it was made from.

Personal matter stops an ingest before the store because a source is
immutable from its registration and travels into git. What has
entered cannot be taken back, so the question must come before the
store.

A source has one form because the repository carries what the forge
works with, which is text, and a binary nobody reads from git is
weight without use. A binary that is used as a thing is kept because
it is used.

The role of a source is asked before the entry is written so that the
entry carries its role from its birth and no later hand changes it.
Registration does not imply intake, and source content enters the
intent only by the principal's explicit act, so that what someone
said in a meeting is never silently promoted to the principal's own
position. A contradiction between the intent and a resource is not a
finding because the source may be a counter-example, a mere
inspiration or a record of what someone else said.

The index exists so that Claude and the principal know what resources
exist and what they are for without re-reading the files. It is a
working aid, not a record of thinking. Every index has one shape
because Role and Use for are what an index is for, and a table does
not carry them. The ledger holds registration only, with no content
columns, so that nothing is described in two places. Research is kept
in `research/` because outside inspiration is a legitimate input and
durable findings should not be left in chat. Why a bundle is
catalogued in two levels and never deeper is not recorded.

## A worked example

A project `example-project` receives the transcript of a vendor
workshop as a Word file. At `/ingest` Claude asks whether to convert
it; the principal says yes, and `sources/vendor-workshop.md` is the
source. Before the entry is written Claude asks what it is for; the
principal answers that it is a record of what the vendor claimed, to
be checked rather than adopted. The entry in `sources/00-INDEX.md`
then reads, in the shape the index skeleton gives:

```
### `vendor-workshop.md`
- **What:** Transcript of a half-day workshop with a vendor on their
  platform's capabilities.
- **Origin:** Workshop recording, transcribed by the vendor.
- **Date:** 2026-03-12, from the content
- **Form:** extract of vendor-workshop.docx
- **Role:** A record of what the vendor claimed; to be verified, not
  adopted.
- **Use for:** What the vendor promised on integration and licensing.
```

Nothing of this transcript is in the intent yet. If the principal
later decides that one claim is his own position, he says so, and the
position cites `sources/vendor-workshop.md`. If the vendor sends a
corrected transcript, it does not replace the file: it is registered
as a new source, or the two become a growing bundle whose index says
which is the newest.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [How a research is made](the-research.md): how a research is
  planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
