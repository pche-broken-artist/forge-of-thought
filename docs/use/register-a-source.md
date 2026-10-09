---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.ps1
  - templates/index.md
  - templates/index-bundle.md
  - CLAUDE.md
---

# Register a source

This page is for the person who has outside material, such as a
transcript, an offer, a standard or a pasted text, and wants it
registered in a project. It says what `/ingest` does, what it asks you
and what it leaves alone.

`/ingest [file] [slug]` stores, registers and catalogues external
input in the project's `sources/` directory, and does nothing more. If
the project is not clear from the second argument or the context,
Claude asks.

## Choose how to start

- **With a file:** `/ingest <file>` registers that document.
- **With text pasted into the conversation:** the text itself is the
  source. It is stored as `sources/<slug>.md`, with the slug proposed
  from its content and a two-line header saying it was pasted into the
  conversation, and when. It is then registered like any file.
- **Bare:** `/ingest` sweeps `sources/` for files not yet registered
  and registers them all. A subdirectory is registered as one bundle,
  never file by file. The sweep also reports files changed since they
  were registered and asks what to do with each. What a change means
  depends on the kind of project:
  - In a thought project a changed source is a breach of immutability.
    You settle it: register the new version beside the old as a new
    source, restore the original, or accept the change knowingly.
  - In a library a changed document is the owner's ordinary
    maintenance. The index entry and the registration date are
    updated and nothing else.

  Nothing is ever re-registered silently.

## What happens, in order

1. **Personal matter stops the command.** If the text carries
   personal matter, such as a named private person, an identifying
   detail or health, Claude stops before storing and asks whether to
   store it as it is, redact it first, or drop it. This is
   unconditional. A registered source is immutable, so redaction can
   only happen before registration.
2. **The file is stored** in `sources/` under a short descriptive
   slug, such as `vendor-offer.docx`, with no date in the name. If the
   name is taken, `-2` is added. A file already registered is never
   renamed or modified.
3. **A date is noted if it can be found for free**, from the content,
   then the file metadata, then the day of registration. You are never
   asked for a date.
4. **Every binary gets one question.** For each binary file (PDF, Word,
   PowerPoint, Excel and the like), alone or inside a bundle, Claude
   asks: convert to Markdown?
   - **Yes:** `scripts/doc2md.ps1` makes the Markdown extract, and the
     extract is the source. The original is not copied into the
     project. If it already lies in `sources/`, as can happen in a
     sweep, it stays there as a local file only and is kept out of git.
   - **No:** the binary is the source as a functional thing, such as a
     deck template or a graphic. It is stored and registered as it is,
     with no extract.

   Text files get no question. Keeping both the binary and an extract
   is the exception, and only on your explicit word. The script is the
   only way a conversion is made. What it reads and what it needs
   installed are on the Scripts page.
5. **The source is catalogued** in the `sources/` index, in four
   fields: what it is, where it came from, its role, and what to reach
   for it for.
6. **Claude asks what the source is for.** Your answer goes into the
   index as its Role. You may instead tell Claude to infer the role. It
   then writes what the file itself declares, marked as inferred.
   Claude never infers it unasked, and until you answer the Role stays
   empty.
7. **The ledger's Sources table is updated.** What a source is and is
   for lives in the index alone.

The reply after registration is three lines at most: the file stored
and its index entry; what the source adds to the intent, in one line,
or "nothing new"; and the question "what is it for?". There is no
analysis of the content and no next step. The sources wait for you.

## A set of related files

A set of related files, such as a downloaded site with its pages, is a
bundle. It lives in `sources/<slug>/` and counts as one source with
one registration. It carries its own index, which `/ingest` creates
from the bundle skeleton if the bundle arrives without one. If one
arrives with an index, `/ingest` checks it against the actual contents
and reports gaps. The main index holds one entry for the bundle,
pointing to its inner index, and no deeper.

## A document of a library

A document that lives in a library is cited, not copied. Nothing is
stored in `sources/`. The index gets an entry that names the path and
says what the document is for, and the dependency is registered in the
ledger. See the page on sharing material through a library. Moving a
document out of a project into a library is the reverse: it is
ingested into the library, the project's entry is replaced by the
citation, and the dependency is registered.

## Registration is not intake

`/ingest` never carries content into the intent or any other
document. Whether, how and when a source is used is directed by you
alone. When source content does enter the intent, it is your explicit
act, cited with its provenance.

## See also

- [About sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document from a project.
- [Scripts](../reference/scripts.md): `doc2md.ps1`, its formats and what it needs.
