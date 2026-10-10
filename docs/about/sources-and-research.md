---
generated: 2026-10-10
made: derived
inputs-hash: 8beb9570c89132f1
inputs:
  - CLAUDE.md
  - templates/index.md
  - templates/index-bundle.md
  - projects/forge/10-intent.md
---

# About sources and research

This page explains what the forge keeps in a project's `sources/`
and `research/` directories, how those files behave once they are
there, and why the rules are as they are. It is for a user who wants
to know what happens to material he brings in, and for an evaluator
who wants to see the reasoning behind the rules. It was put together
from the rules in `CLAUDE.md` (Document chain, the paragraphs on
external inputs and resource indexes), the two index skeletons
`templates/index.md` and `templates/index-bundle.md`, and the
positions of the forge's own intent that give the reasons.

## Sources: external input as it arrived

A source is external input, kept as it arrived: a transcript, an
offer, a document, a standard. Sources live in the project's
`sources/` directory under plain slug filenames. They may arrive at
any stage of a project's life, even before the brief, as material
for writing it, or during intent work, or after. Origin dates are
metadata, not ceremony: they are recorded in the ledger as best the
forge can tell and never demanded from the principal.

The command that brings a source in is `/ingest`. It stores,
registers and catalogues the file, and nothing more. Run without
arguments it sweeps `sources/` for files the principal dropped there
by hand and registers what it finds. The step-by-step procedure is
on the page Register a source (See also).

### One form each

A source has one form: text, or a functional binary. A binary that
is to be read, such as a document or a presentation, is converted to
a Markdown extract, and that extract is then the source; the
original is not copied into the project. A binary that is used as a
thing, such as a deck template, a graphic or a logo, stays a binary.
The conversion happens only on the principal's explicit word, asked
at ingest, and keeping both forms is the exception, again on his
word.

The reason is weight against use: the repository carries what the
forge works with, which is text, and a binary nobody reads from git
is weight without use, while a binary used as a thing is kept
because it is used.

Extracts are produced by one script of the forge, `scripts/doc2md.py`,
and never by ad-hoc parsing: no reading of a PDF by improvised code,
no manual transcription. What the script needs installed and how the
conversion runs is said in the script's own header and in the ingest
skill.

### Immutable once registered

From the moment a source is registered it is never edited.
Corrections happen downstream, in the artefacts that use the source,
never in the source itself. If a bare sweep of `sources/` finds a
file changed since its registration, it reports the change and asks
what to do with it; in a thought project a changed source is a breach
to be settled (a new source beside it, the original restored, or the
change knowingly accepted).

### A related set is a bundle

A set of related files, such as a downloaded site with its index or
a document with its attachments, may live as a subdirectory
`sources/<slug>/`. The bundle counts as one source: one ledger entry,
immutable as a whole from registration. File-level detail is not
lost, because provenance in the intent cites individual files by
path, and the bundle carries its own catalogue, a `00-INDEX.md`
inside the directory, created at registration where the bundle lacks
one. Isolated files stay directly in `sources/`.

## Registration is not intake

Registering a source says only that it exists. What it is for is a
separate matter, and it is the principal's word. After registration
Claude asks once what the source is for, and the answer is recorded
as the free-text Role in the resource index: a standard to verify
against, inspiration, a counter-example, a meeting record, material
to absorb. Until the principal gives it, the Role stays empty; it is
never inferred unasked. He may tell Claude to infer it, and then the
inferred role is written and marked as inferred.

The principal alone directs how and when each source is used, in
whatever work he chooses. When source content does enter the intent,
that is his explicit act, cited with provenance to the file. What
someone said in a meeting is never silently promoted to the
principal's own position: a transcript records what others said, and
only the principal decides what of it becomes his.

## Research: a durable answer to one question

The forge researches before it invents. For key topics Claude looks
up current best practice rather than inventing, because outside
inspiration is a legitimate input and the principal does not want to
reinvent what the world has solved. A durable finding is not left in
the conversation: it is stored as a research note in `research/`,
named `YYYY-MM-DD-<topic>.md`, and indexed.

A research note is the durable answer to one question. Like a source
it is immutable: never edited from its creation, dated by its name,
with corrections made downstream in later work rather than in the
note. The command is `/research <topic>`; its procedure is on the
page Research a topic (See also).

## The resource index

Every `sources/` and every `research/` directory carries a
`00-INDEX.md`, the resource index. It is a light catalogue so that
Claude and the principal know what resources exist and what they are
for without re-reading the files. A bundle has the same catalogue
one level down and appears in the top index as one entry pointing
into it: two levels, never deeper, and the top index never repeats
the bundle's contents.

Each entry has fixed fields in free text. For a source they say what
the resource is, where it came from, what its role is and what to
reach for it for; for a research note they say what question it set
out to answer, the answer in short and when the note is worth
opening. The fields are free text rather than a table because the
role and the use of a resource are what an index is for, and a
table does not carry them. The ledger, by contrast, holds
registration only, with no content columns, so that nothing is
described in two places.

The index is a working aid, not a record of thinking. It tracks
nothing: no processing state, no positions. Unlike the files it
catalogues, it is freely rewritten, like the ledger: `/ingest` and
`/research` write its entries, and `/check` verifies that the index
and the directory agree.

### Why a contradiction with a source is not a finding

The index is an automatic input of no command. The state map, the
critics and the challengers do not confront the chain with the
material in `sources/` on their own, and a contradiction between the
intent and a source is not a finding. The reason is that a source's
role is individual: it may be a counter-example, a mere inspiration
or a record of what someone else said, and none of those obliges the
intent to agree with it. Claude reaches for a file by his own
judgement or when the principal asks him to, for instance to check
an assessment against the requirements in a named file.

## Why personal matter stops an ingest before the store

Before storing, personal matter in what is to be ingested, such as a
named private person, an identifying detail or anything about
health, stops the command and asks the principal what to do. The
question must come before the store, not after, because a source is
immutable from its registration and travels into git: what has
entered cannot be taken back. The same holds for text pasted into
the conversation, which `/ingest` takes as well as a file.

## See also

- [Register a source](../use/register-a-source.md): the ingest procedure.
- [Research a topic](../use/research-a-topic.md): the research procedure.
