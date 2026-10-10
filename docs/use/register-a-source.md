---
generated: 2026-10-10
made: mirrored
inputs-hash: 197493dd79f6694b
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
  - CLAUDE.md
---

# Register a source

This page is for a user who has outside material, such as a transcript,
an offer or a standard, and wants it stored in a project. `/ingest
[file] [slug]` stores it in `sources/`, registers it, catalogues it and
does nothing more.

## Give it a file, text or nothing

- **A file:** `/ingest <file> [slug]` registers that document. The slug
  is the project's, taken from context if you leave it out.
- **Text pasted into the conversation:** the text is the source. It is
  stored as `sources/<slug>.md`, the slug proposed from its content,
  under a two-line header that says it was pasted into the conversation
  and gives the date. It is then registered like any file.
- **Nothing:** bare `/ingest` sweeps `sources/` and registers every file
  not yet recorded. It also reports files changed since their
  registration and asks what to do with each. In a thought project a
  changed source is a breach of immutability to settle: register it
  beside as a new source, restore it, or accept the change knowingly. In
  a library a changed document is the owner's ordinary maintenance, so
  the index entry and the date are updated and nothing else. A changed
  file is never silently re-registered.

A file is stored under a short descriptive slug taken from its content or
its original name, with no date in the name. On a name collision the
slug gets the suffix `-2`. A file already registered is never renamed or
modified.

## Personal matter stops the command

Before anything is stored, the text is looked at for personal matter: a
named private person, an identifying detail, health, anything of the
kind. If there is any, the command stops and asks whether to store it as
it is, redact it before registration, or drop it. It is never stored
first and asked about afterwards, because a registered source cannot be
changed.

## Binary files: one question each

For every binary file, such as a PDF, a Word, PowerPoint or Excel file,
you are asked once: convert to Markdown?

- **Yes:** `scripts/doc2md.py` makes the Markdown extract, and the
  extract is the source. It is registered and indexed, with its origin
  noted as an extract of the original. The original is not copied into
  the project. If it already lies in `sources/`, as in a sweep, it is
  added to `sources/.gitignore` and stays there, local only.
- **No:** the binary itself is the source, as a functional thing such as
  a deck template or a graphic. It is stored, registered and indexed as
  it is, with no extract.

Text files get no question. Keeping both the binary and its extract is
an exception, made only on your explicit word. The script is the only
conversion path, and it needs the markitdown tool installed, which it
never installs itself. Its formats and requirements are on the Scripts
page.

## A set of related files is a bundle

Related files, such as a downloaded site with its index, are stored as
`sources/<slug>/` and count as one source with one ledger entry. In a
sweep a subdirectory is registered as one bundle, never file by file.
Each bundle has its own index, `00-INDEX.md`, made from the bundle
skeleton if the bundle arrives without one. A supplied index is checked
against the actual contents, and any gaps are reported. The bundle
index opens with a short paragraph on what the whole is and why it
entered `sources/`, then lists each file with the same fields as an
ordinary entry.

## What the registration records

The origin date goes into the ledger when it can be found without
asking you: from the content, such as a meeting date in a transcript
header, otherwise from the file's metadata, otherwise the day of
registration. You are never asked for a date.

The source is added to `sources/00-INDEX.md`, an entry of four fields:
what it is, where it came from, its role, and what to reach for it for.
The index is created if it is missing, and the entry is written only
after enough of the file has been read to describe it truthfully.

## Say what it is for

After registration Claude always asks what the source is for. Your
answer goes into the index as its Role. You may instead tell Claude to
infer it, and then it writes what the file itself declares, marked as
inferred. It is never inferred unasked, and the Role stays empty until
you answer.

The reply after registration is short: the file stored and its index
entry, what the source adds to the intent in one line or "nothing new",
and the question what it is for. It carries no analysis of the content
and implies no next step.

## A library's document is cited, not copied

When you point a project at a document that lives in a library, nothing
is stored in `sources/`. The index gets an entry that names the path and
says what the document is for, and the ledger records the dependency.
Moving a document out of a project into a library is the reverse: it is
registered in the library, the project's entry is replaced by the
citation, and the dependency is registered.

## Registration is not intake

`/ingest` never carries content into the intent or any other document.
What someone said in a source is not promoted to your position. You
alone direct how and when each source is used, and when its content does
enter the intent, that is your explicit act, cited with the file as
provenance.

## See also

- [About sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document from a project.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
