---
generated: 2026-10-09
made: derived
inputs-hash: 7b899a13d98fed00
inputs:
  - CLAUDE.md
  - templates/index.md
  - templates/index-bundle.md
  - projects/forge/10-intent.md
---

# About sources and research

This page explains what the two resource directories of a project,
`sources/` and `research/`, hold, how a file gets there, what the
forge does and does not do with it, and why the rules are as they
are. It is for the user who brings material into a project and for
the evaluator who wants to know how outside input is kept apart
from the principal's own thinking. It was put together from
`CLAUDE.md` (Document chain: External inputs and Resource indexes),
the index skeletons `templates/index.md` and
`templates/index-bundle.md`, and the positions of the forge intent
`projects/forge/10-intent.md` that give the reasons.

## Sources: external input as it arrived

A source is an external input: a transcript, an offer, a document,
a standard. Sources live in `sources/` of the project, under plain
slug filenames, and they may arrive at any stage of a project's
life: before the brief as material for writing it, during intent
work, or after. The principal may drop files into `sources/` by
hand at any time; `/ingest` is the command that stores, registers
and catalogues them, and it does nothing more. Run without a file,
it sweeps `sources/` for files not yet registered and reports files
that changed since registration, asking what to do with each.
`/ingest` takes text pasted into the conversation as well as a
file.

Origin dates are metadata, not ceremony: they are recorded best
effort in the ledger and never demanded from the principal.

### Immutable once registered

From its registration a source is never edited; corrections happen
downstream, in the artefacts that use it. Immutability is a process
rule, not a git mechanism: nothing locks the file, the forge simply
does not touch it. What a changed source means depends on the kind
of project. In a thought project it is a breach to be settled: a
new source beside the old one, the original restored, or the change
knowingly accepted. In a library, whose material is maintained by
its owner, a changed file is the normal case, and the sweep moves
the ledger date and corrects the index entry.

### One form each

A file in `sources/` is either text or a functional binary, never
both by default. At `/ingest` every binary file gets one question:
convert to Markdown? If yes, the extract `sources/<slug>.md` is
written and that extract is the source; the original is not copied
into the project. If no, the binary is the source as a functional
thing: a deck template, a graphic, a logo, kept because it is used
as a thing. Keeping both is the exception, on the principal's
explicit word. The reason is weight: the repository carries what
the forge works with, which is text, and a binary nobody reads from
git is weight without use.

Extracts are produced by one script of the forge,
`scripts/doc2md.py`, and never by ad-hoc parsing: no reading a PDF
with improvised code, no manual transcription. How the conversion
runs and what it needs installed is said in the ingest skill and in
the script's own header.

### Bundles

A set of related files, such as a downloaded site with its index or
a document with its attachments, may live as a subdirectory
`sources/<slug>/`. It counts as one source: one ledger entry,
immutable as a whole from registration. File-level detail is not
lost, because provenance in the intent cites individual files by
path and the bundle's own catalogue lists its contents. Every bundle
carries a `00-INDEX.md` of its own, in the shape of
`templates/index-bundle.md`: a short paragraph on what the whole is
and why it entered sources, then one entry per file in the same
fields as the top-level index. `/ingest` creates it at registration
when the bundle lacks one and validates a supplied one against the
contents. Isolated files stay directly in `sources/`. Should a
bundle's files ever need separate fates, a file may be split out to
its own ledger row; the ledger is freely rewritten.

## Registration is not intake

Registering a source says only that it exists. What it is for is
individual: a standard to verify against, inspiration, a
counter-example, a record of a meeting, material to absorb. That
role is the principal's word. After registration Claude asks once
what the source is for, and the answer is written as free-text Role
in the resource index; until he gives it the field stays empty, and
it is never inferred unasked. He may instead tell Claude to infer
the role, and then it is written marked as inferred. The ledger row
is registration only.

The principal alone directs how and when each source is used, in
whatever work he chooses. When source content does enter the
intent, it is his explicit act, cited with provenance to the file:
what someone said in a meeting is never silently promoted to the
principal's own position. This is the boundary that keeps outside
material from passing for the principal's thinking: a source may be
a counter-example or a record of what someone else said, and only
his act turns any of it into a position of his own.

### Why personal matter stops an ingest before the store

Before storing, `/ingest` stops and asks when it meets personal
matter: a named private person, an identifying detail, health,
anything of the kind. The reason is the immutability just
described: a source is immutable from its registration and travels
into git, so what has entered cannot be taken back. The question
must therefore come before the store, not after.

## Research: a durable answer to one question

For key topics Claude researches current best practice rather than
inventing. Outside inspiration is a legitimate input, and durable
findings are stored in `research/`, not left in the conversation,
because the principal does not want to reinvent what the world has
already solved. A research note answers one question; it is written
by `/research`, dated in its filename (`research/YYYY-MM-DD-<topic>.md`),
immutable from creation and always in English, whatever the
project's language, because research is read by Claude, the
reviewers and the checks and never handed to the recipients.

## The resource index

Every `sources/` and every `research/` directory carries a
`00-INDEX.md`, in the shape of `templates/index.md`: a light
catalogue so that Claude and the principal know what resources
exist and what they are for without re-reading the files. Each
entry has fixed fields in free text. A sources entry says what the
resource is, where it came from, what its role is and what to reach
for it for; a research entry says the question the note set out to
answer, the answer in short, and when the note is worth opening.
One shape serves every index because Role and Use for are what an
index is for, and a table does not carry them. The ledger holds
registration only, a Sources table and a Research table with no
content columns, so that nothing is described in two places.

A bundle appears in the top index as one entry pointing into its
own inner index: two levels, never deeper, and the top index never
repeats the bundle's contents.

The index is a working aid, not a record of thinking. It tracks
nothing: no processing state, no positions. It is an automatic
input of no command: `/forge`, `/critique` and the challengers do
not confront the chain with the material on their own, so a
contradiction between the intent and a source is not a finding. The
source may be a counter-example, a mere inspiration or a record of
what someone else said. Claude reaches for a file by his own
judgement or when the principal asks, for instance to check an
assessment against the requirements in a named file. Unlike the
files it catalogues, the index is freely rewritten, like the ledger.
`/ingest` and `/research` write its entries; `/check` verifies the
index against the directory.

## See also

- [Register a source](../use/register-a-source.md): the ingest procedure.
- [Research a topic](../use/research-a-topic.md): the research procedure.
