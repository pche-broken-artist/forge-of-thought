---
generated: 2026-10-09
made: mirrored
inputs-hash: e77900bf4602119c
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
  - CLAUDE.md
---

# Register a source

This page is for a user who has external input, such as a document, a
transcript or a piece of text, and wants it on record in a project.
`/ingest [file] [slug]` stores, registers and catalogues that input in
the project's `sources/` directory, and does nothing more.

## What you run

- `/ingest <file>` registers that document.
- `/ingest` with text pasted into the conversation takes the text as the
  source. It is stored as `sources/<slug>.md`, with the slug proposed
  from the content and a two-line header giving the origin (pasted into
  the conversation) and the date.
- Bare `/ingest` is a sweep. It looks in `sources/` for files not yet
  registered and registers them. It also reports files changed since
  their registration and asks what to do with each. In a thought project
  a changed source is a breach of immutability to settle. In a library it
  is the owner's ordinary maintenance, and the index entry and the date
  are updated. A changed file is never silently re-registered.

The project is the slug you give as the second argument, or the one
from context. If that is ambiguous, you are asked.

## What happens, step by step

1. **Personal matter stops the command.** If the text carries personal
   matter, such as a named private person, an identifying detail or
   health, the command stops before storing. You choose: store as it is,
   redact before registration, or drop. This comes first because a
   registered source is immutable, so redaction can only happen before
   registration.
2. **The file is stored** in `sources/` under a short descriptive slug
   taken from its content or original name, with no date in the name. On
   a name collision `-2` is added. A file already registered is never
   renamed or modified.
3. **A binary gets one question: convert to Markdown?**
   - Yes: `scripts/doc2md.py` makes a Markdown extract. The extract is
     then the source, with its origin noted as an extract of the
     original. The original is not copied into the project. If it
     already lies in `sources/` (as in a sweep), it is listed in
     `sources/.gitignore` and stays local only.
   - No: the binary itself is the source, as a functional thing, such as
     a deck template or a graphic. It is stored, registered and indexed
     as it is.

   Text files get no question. Keeping both the original and the extract
   is an exception, on your explicit word. The conversion needs
   markitdown installed; see [Scripts](../reference/scripts.md) for the
   formats `doc2md.py` handles and what it needs.
4. **The source is catalogued** in `sources/00-INDEX.md`, created if
   missing. Each entry has four fields: what the resource is, its origin,
   its role and what to use it for.
5. **Claude asks what the source is for.** Your answer goes into the
   index as its Role. You may instead tell Claude to infer it, and then
   it writes what the file itself declares, marked as inferred. Until you
   answer, the Role stays empty. It is never inferred unasked.
6. **The ledger's Sources table is updated.** What a source is and is for
   lives in the index alone.

The reply after registration is short: the file stored and its index
entry, what the source adds to the intent in one line or "nothing new",
and the question about its role.

## A set of related files

A set of related files, such as a downloaded site with its index, is a
bundle: it lives in `sources/<slug>/` and counts as one source with one
ledger entry. In a sweep, a subdirectory is registered as one bundle,
never file by file. Each bundle has its own `00-INDEX.md`. If the bundle
arrives without one, it is created from the bundle index skeleton, which
holds a short paragraph on what the whole is and why it entered, then
one entry per file. If it arrives with one, that index is checked
against the actual contents and any gaps are reported. The project's own
index shows the bundle as a single entry pointing to the inner index.

## A library's document

A document that lives in a library is cited, not copied. Nothing is
stored in `sources/`. Instead the index gets an entry naming the path
and saying what it is for, and the document is registered as a
dependency in the ledger. See
[Share material through a library](share-material-through-a-library.md).

## Registration is not intake

`/ingest` never carries content into the intent or any other document.
The principal alone directs how and when a source is used, and when its
content does enter the intent, it is cited with provenance. Why sources
are immutable and why registration is not intake is explained in
[About sources and research](../about/sources-and-research.md).

## See also

- [About sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document from a project.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
