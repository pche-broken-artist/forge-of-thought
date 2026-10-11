---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: e8097fe1929a34da
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

Sources and research are the two kinds of resource a project keeps
beside its chain of documents: a source is external input kept as it
arrived, a research note is a durable answer to one question. This
page says what the two are, how they are kept and catalogued, and why
the forge treats them the way it does. It is for the user who brings
material into a project and for the evaluator who asks what becomes
of that material. The procedures themselves are on the pages
[Register a source](../use/register-a-source.md) and
[Research a topic](../use/research-a-topic.md).

## What it is

A **source** is an external input: a transcript, an offer, a
document, a standard. It lives in the project's `sources/` directory
under a plain slug filename. Once registered it is immutable. It has
one form: text, or a functional binary such as a deck template, a
graphic or a logo. A source may arrive at any stage of a project's
life: before the brief, as material for writing it; during the work on
the intent (the trunk of the chain, where the
[principal](../reference/glossary.md), that is, the person whose
thinking is forged, states his positions); or after.

A **bundle** is a set of related files that belong together, such as
a downloaded site with its index or a document with its attachments.
It lives as a subdirectory `sources/<slug>/` and counts as one source:
one entry in the [ledger](../reference/glossary.md), the project's
single source of truth for state, and immutable as a whole from its
registration. Isolated files stay directly in `sources/`.

A **research note** is a durable answer to one question. It lives in
the project's `research/` directory as a dated file,
`YYYY-MM-DD-<topic>.md`, and is not left in the conversation.

The **resource index** is the catalogue of a resource directory.
Every `sources/` and every `research/` directory carries one, named
`00-INDEX.md`. It is a light catalogue: what exists here and what it
is for, in fixed fields written in free text. Every bundle carries a
`00-INDEX.md` of its own inside it. Unlike the files it catalogues,
the index is freely rewritten, like the ledger.

## How it works

### Registration

The command `/ingest` stores, registers and catalogues a source, and
does nothing more. It takes a file or text pasted into the
conversation. Run without arguments it sweeps `sources/`: it registers
the files the principal has dropped there by hand and reports the
files that have changed since their registration, with a question
what to do with each. The origin date of a source is recorded in the
ledger as well as it is known and is never demanded from the
principal.

Before a source is stored, personal matter stops the command: a named
private person, an identifying detail, health, anything of the kind.
Claude asks before it stores.

A binary file, isolated or inside a bundle, gets one question at
registration: convert to Markdown? If yes, the script
`scripts/doc2md.py` writes the extract `sources/<slug>.md`, and that
extract is the source; the original is not copied into the project.
If no, the binary itself is the source, kept as a functional thing.
Keeping both is the exception, on the principal's explicit word.
Extracts come from that one script and never from ad-hoc parsing.

A bundle that arrives without a catalogue gets its `00-INDEX.md` at
registration.

### The role of a source

Registration does not imply intake. What a source is for is
individual: a standard to verify against, an inspiration, a
counter-example, a meeting record, material to absorb. After
registration Claude asks the principal once what the source is for.
His answer is written as the free-text Role in the resource index. The
field stays empty until he gives it. He may instead tell Claude to
infer the role; a role inferred on his word is written marked
*(inferred)*. The ledger row of a source is registration only and
carries no content columns.

The principal alone directs how and when a source is used, in
whatever work he chooses. When the content of a source does enter the
intent, it is his explicit act, cited with provenance to the file.
Inside a bundle the provenance cites the individual file by path, so
that file-level detail is not lost.

### What the index does and does not do

The index tracks nothing: no processing state, no positions. It is an
automatic input of no command. The state map of a project, the critics
and the challengers do not confront the chain with the material on
their own. Claude reaches for a file by its own judgement or when the
principal asks, for instance to check an assessment against the
requirements in a named file. A contradiction between the intent and
a source is not a finding.

The index has two levels and never more. A bundle appears in the top
index as one entry pointing into the bundle's own `00-INDEX.md`, and
the top index never repeats the bundle's contents. The bundle index is
the same catalogue one level down: its header and opening paragraph
are its own, its per-file entries have the fields of the sources
entry. `/ingest` and `/research` write the entries; `/check` verifies
the index against the directory.

### A source that changed

The sweep of `/ingest` reports a file changed since its registration.
What that means depends on the kind of the project. In a thought
project, the kind that carries a chain, a changed source is a breach
of immutability to be settled: a new source beside it, the original
restored, or the change knowingly accepted. In a
[library](../reference/glossary.md), a project of shared material
without a chain, a changed file is the normal case, its owner's
maintenance: the date in the ledger is moved and the index entry is
corrected.

### Research

For a key topic Claude researches current best practice rather than
inventing. Outside inspiration is a legitimate input. The durable
findings are stored in `research/` as a dated note and catalogued in
the directory's index with three fields: the question the note set
out to answer, the answer in short, and the situations in which the
note is worth opening.

## Why

**Why research.** Because the principal does not want to reinvent
what the world has already solved: for a key topic Claude looks up
current best practice rather than inventing. The findings are stored
so that they stay durable instead of being lost in the conversation.

**Why a source is immutable.** The inputs state the rule and build on
it. The reason a source is immutable at all is not recorded.

**Why personal matter stops the command before the store.** Because a
source is immutable from its registration and travels into git. What
has entered cannot be taken back. So the question must come before
the store, not after it.

**Why one form.** Because the repository carries what the forge works
with, which is text. A binary nobody reads from git is weight without
use. A binary that is used as a thing, a deck template or a logo, is
kept because it is used.

**Why dates are never demanded.** Origin dates are metadata, not
ceremony. They are recorded as well as they are known.

**Why registration is not intake.** Because what a source is for is
individual. The same file may be a standard to verify against, a
counter-example, a mere inspiration or a record of what someone else
said. So the role is the principal's word, and he alone directs how
and when a source is used. The reason the role is asked for and never
inferred unasked is not recorded.

**Why a contradiction is not a finding.** Because a source may be a
counter-example, a mere inspiration or a record of what someone else
said. A disagreement between the intent and such a file says nothing
about the intent. For the same reason what someone said in a meeting
is never silently promoted to the principal's own position: it enters
the intent only by his explicit act, with provenance.

**Why an index.** So that Claude and the principal know what
resources exist and what they are for without re-reading the files.
The index is a working aid, not a record of thinking.

**Why one shape, not a table.** Because Role and Use for are what an
index is for, and a table does not carry them. The same shape serves
every index, the bundle's included.

**Why the ledger holds registration only.** So that nothing is
described in two places: the ledger says that a resource exists, the
index says what it is and what it is for.

## A worked example

A sources entry of a resource index, in the shape the skeleton
`templates/index.md` defines, filled for a made-up offer that arrived
as a PDF and was converted on the principal's word:

```
### `vendor-offer.md`
- **What:** The offer of one vendor for the platform, as the Markdown extract of the PDF they sent.
- **Origin:** Sent by the vendor after the second meeting; spring of this year, date best effort.
- **Role:** a counter-example: what the solution looks like when the vendor shapes the question
- **Use for:** the vendor's price structure and the limits of its licence terms.
```

The original PDF is not in the project; the extract is the source.
The entry says what the file is and what it is for, and nothing of
what the project has done with it: no processing state, no position.
A research entry has the same place in `research/00-INDEX.md` with its
own three fields: Question, Answer in short, Consult when.

## See also

- [Register a source](../use/register-a-source.md): the ingest procedure.
- [Research a topic](../use/research-a-topic.md): the research procedure.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
