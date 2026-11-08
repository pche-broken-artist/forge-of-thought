---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 7e6d7b371c452648
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

Sources and research are the two resources of a project: a source
is an external input kept as it arrived, a research note is a
durable answer to one question that Claude looked up. This page
explains what each is, how the two directories and their indexes
work, and why a source and a research note are never edited once
filed. It is for the user who brings material into a project and for
the evaluator who wants to know what the forge promises about that
material. How a source is brought in is the page
[Register a source](../use/register-a-source.md); how a research is
run is the page [Research a topic](../use/research-a-topic.md). The
words of the forge used here are gathered in the
[Glossary](../reference/glossary.md).

## What it is

A **source** is an external input: a transcript, an offer, a
document, a standard. It lives in the project's `sources/` directory
under a plain slug filename. It is immutable once registered. A
source may arrive at any stage of a project's life: before the brief
as material for writing it, during the work on the intent, or after.

A source has one form. It is either text or a functional binary,
never both by default. A binary such as a deck template, a graphic or
a logo is kept as a thing that is used. A binary whose text is wanted
is converted to a Markdown extract, and the extract is then the
source; the original is not copied into the project. The conversion
happens only on the explicit word of the principal (the person whose
thinking is being forged), through `/ingest`, and only by the one
script of the forge, `scripts/doc2md.py`, never by ad-hoc parsing.

A **bundle** is a set of related files that counts as one source: a
downloaded site with its index, a document with its attachments. It
lives as a subdirectory `sources/<slug>/` and has one entry in the
index above it. A bundle is one of two things. Either it is a whole
that arrived at once, immutable as a whole from its registration. Or
it is a stream of one origin that keeps arriving, such as the issues
of a repository or the minutes of a standing meeting; such a bundle
grows file by file through `/ingest --bundle <name>`, each file
immutable from its own registration. The bundle's own index says in
its opening paragraph which of the two it is. Isolated files stay
directly in `sources/`.

A **research** note is a durable answer to one question. A research
of several questions is a bundle with the plan and the synthesis at
its head and one note per question per engine. Research notes live
in `research/`, named with the date they were made
(`YYYY-MM-DD-<topic>.md`), and are immutable from their filing.

Every `sources/` and every `research/` directory carries a resource
index, `00-INDEX.md`: a light catalogue of what exists there and what
it is for. The index is a document of kind `index`. Unlike the files
it catalogues, it is freely rewritten.

## How it works

`/ingest` stores, registers and catalogues a source, and nothing
more. Bare, it sweeps `sources/` for files the principal dropped in
by hand: it registers the new ones and reports the files changed
since their registration with a question, what to do with each. In a
thought project a changed source is a breach of immutability to be
settled: a new source beside it, the original restored, or the change
knowingly accepted. In a library project a changed file is the normal
case, the owner's maintenance: the index entry is corrected and its
date moved.

Registration is not intake. What a source is for is individual: a
standard to verify against, an inspiration, a meeting record,
material to absorb. That purpose is recorded as free text in the
`Role` field of the index entry. It is the principal's word: before
the entry is written, Claude asks "what is it for?", and the
principal answers with the role or tells Claude to infer it, in which
case the inferred role is written marked *(inferred)*. The ledger
(the project's state report, made at read time) shows registration
only. The principal alone directs how and when a source is used.

Source content enters the intent only by the principal's explicit
act, cited with provenance to the file. Where the source is a bundle,
the provenance cites the individual file by its path. What someone
said in a meeting is never silently promoted to the principal's own
position.

Before a source is stored, `/ingest` stops and asks when the material
carries personal matter: a named private person, an identifying
detail, health, anything of the kind. The question comes before the
store, not after.

The index tracks nothing: no processing state, no positions. It is
an automatic input of no command. `/forge`, `/critique` and the
challengers do not confront the chain with the material on their
own; a contradiction between the intent and a source is not a
finding. Claude reaches for a file by its own judgement or when the
principal asks, for instance to check an assessment against the
requirements in a named file. `/ingest` writes the entries of
`sources/00-INDEX.md`, `/research` those of `research/00-INDEX.md`;
`/check` verifies each index against its directory.

An index entry has fixed fields in free text, the same shape in
every index. A source entry carries:

- `What`: what the resource is, in one or two sentences.
- `Origin`: where it came from, such as an author, a URL or a
  meeting.
- `Date`: the date of the source, best effort, taken from the
  content, the file or the ingest; it is never demanded from the
  principal.
- `Form`: `text`, `extract of <original>` or `binary`, one form per
  source.
- `Role`: what the source is for, the principal's word.
- `Use for`: what to reach for it for, the questions it answers
  best.

A research entry carries `Question`, `Answer in short` and
`Consult when`.

A bundle keeps its own `00-INDEX.md` inside, the same catalogue one
level down: a header with the bundle's slug, project, date and
origin, one opening paragraph that says what the whole is, why it
entered `sources/` and whether it arrived whole or grows, then one
source entry per file in the fields above. In the top index the
bundle appears as one entry pointing into it. There are two levels,
never deeper, and the top index never repeats the bundle's contents.

A research is planned before it is searched and, where it carries
weight, run on two model families; how that is done and how the
result is kept honest is described on the page
[How a research is made](the-research.md).

## Why

A source and a research note are immutable because they record a
moment: a state of the world the forge did not make and has no
business editing. A newer state is a new file. A research is run
again; a document that arrives in a new version becomes a further
file of a bundle of one origin, whose index says which is the newest
and which it supersedes. So every citation of the intent keeps
pointing at the text it was made from.

Personal matter stops `/ingest` before the store because a source is
immutable from its registration and travels into git. What has
entered cannot be taken back, so the question must come before the
store.

Registration is not intake because a source may be a counter-example,
a mere inspiration or a record of what someone else said. If the
forge confronted the chain with every source on its own, a
disagreement with a counter-example would be reported as a defect.
The same reason keeps the index out of every command's automatic
inputs.

The role of a source is asked before its entry is written so that the
entry carries its role from its birth and no later hand changes it.

A source has one form because the repository carries what the forge
works with, which is text. A binary nobody reads from git is weight
without use; a binary that is used as a thing is kept because it is
used.

The index exists so that Claude and the principal know what resources
exist and what they are for without re-reading the files. It is a
working aid, not a record of thinking. Every index has one shape of
fixed fields rather than a table because `Role` and `Use for` are
what an index is for, and a table does not carry them. The ledger
holds registration only, a Sources table and a Research table with
no content columns, so that nothing is described in two places. The
reason for the limit of two index levels is not recorded.

The date of a source is best effort and never demanded because origin
dates are metadata, not ceremony.

Research is kept in `research/` because for key topics Claude looks
up current best practice rather than inventing; outside inspiration
is a legitimate input, and a durable finding belongs in a file, not
in the conversation.

## A worked example

A generic entry of `sources/00-INDEX.md`, in the shape the template
`templates/index.md` defines, for a text source of a placeholder
project:

```markdown
### `supplier-offer-platform.md`
- **What:** The offer of a platform supplier for the hosting of the
  new service: scope, prices and the terms of the contract.
- **Origin:** Sent by the supplier's account team by e-mail; extracted
  from the attached document.
- **Date:** 2026-03-12, from the content
- **Form:** extract of supplier-offer-platform.pdf
- **Role:** A counter-example: the offer shows what the service would
  cost without the shared platform; the intent argues for the shared
  platform.
- **Use for:** The price of running the service alone; the supplier's
  own view of the migration risks.
```

The entry says what the file is, where it came from and what the
principal wants it for. It records no position of the intent and no
state of processing. The `Role` is the principal's word, given before
the entry was written. Should a newer offer arrive, it becomes a new
file with its own entry, and this file stays as it is.

## See also

- [Register a source](../use/register-a-source.md): the ingest
  procedure.
- [Research a topic](../use/research-a-topic.md): the research
  procedure.
- [How a research is made](the-research.md): how a research is
  planned before it is searched and kept honest.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
