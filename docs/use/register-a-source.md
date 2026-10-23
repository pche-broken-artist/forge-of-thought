---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: fa74b71a263ec185
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how you store, register and catalogue external input
with `/ingest`. It is for the principal (the person whose thinking is
being forged) who has a document, a pasted text or a set of files that
a project should know about. Registering a source only files it and
describes it. Nothing of it enters the project's thinking until you
say so.

## When to use it

Use it when something from outside arrives: a transcript, an offer, a
standard, a deck template, a pasted passage. Use it also when files
have been dropped into `sources/` by hand and are not yet in the
index.

## The command

```
/ingest [file] [slug] [--bundle name]
```

A line you can type as it stands:

```
/ingest vendor-offer.docx my-project
```

The forms of the command:

- With a file: Claude registers that document.
- With text pasted into the conversation: the text becomes
  `sources/<slug>.md`, the slug proposed from its content, with a
  two-line header (origin: pasted into the conversation; date).
- With `--bundle <name>`: the file goes into a bundle of one origin
  that keeps arriving. The bundle is born at its first file, and each
  file is immutable from its own registration.
- Bare: a sweep of `sources/` for files not yet in the index, and a
  report of files changed since registration.

The slug is the project's; when it is ambiguous, Claude asks.

## What happens

1. **Personal matter stops the command.** If the text carries personal
   matter (a named private person, an identifying detail, health,
   anything of the kind), Claude stops and asks: store as it is,
   redact before registration, or drop. It never stores first and
   asks afterwards, because a registered source is immutable.
   You should now see a question only if the text holds such matter;
   otherwise the command goes on.

2. **Store.** Claude copies the document into `sources/` as
   `<short-slug>.<ext>`, a short descriptive name without a date. On a
   name collision it adds the suffix `-2`. A file already in the index
   is never renamed or modified.
   You should now see the file under `sources/`.

3. **Bundles.** A related set that arrives whole is stored as
   `sources/<slug>/` with one index entry and its own `00-INDEX.md`
   (made from `templates/index-bundle.md` if it came without one; a
   supplied one is checked against the contents and gaps are
   reported). With `--bundle <name>`, a missing `sources/<name>/` is
   born as a growing bundle, its index opening by saying that it
   grows. If it exists and grows, the file is stored inside it with an
   entry of its own in the bundle's index. If it exists and arrived
   whole, Claude refuses and says why. In a sweep, a subdirectory is
   registered as one bundle, never file by file, and Claude asks
   whether a new one grows.
   You should now see the bundle directory with its index.

4. **The date.** The index entry carries the document's date, found
   for free: from the content, else from the file's metadata, else
   the day of registration. The entry says which. You are never asked
   for a date.
   You should now see the date in the entry once it is written.

5. **One form per source.** Every binary file (PDF, DOCX, PPTX, XLSX
   and the like) gets one question: convert to Markdown?
   - Yes: `python scripts/doc2md.py <file> -o sources/` makes the
     extract, and the extract is the source. The entry's origin reads
     "extract of `<original>` (markitdown)". The original is not
     copied into the project. If it already lay in `sources/` (in a
     sweep), its path goes into `sources/.gitignore` and it stays
     there, local only.
   - No: the binary is the source as a functional thing (a deck
     template, a graphic, a logo). It is stored and indexed as it is,
     with no extract.

   Text files get no question. Keeping both forms is the exception and
   needs your explicit word. The script is the only conversion path,
   and it needs `markitdown` installed; its formats and needs are on
   the page [Scripts](../reference/scripts.md).
   You should now see either `<short-slug>.md` or the binary, one of
   them.

6. **Role.** Before the index entry exists, Claude asks one question:
   what is it for? A bundle gets one question for the whole, and a
   file added to a growing bundle one of its own. You answer with the
   role, or tell Claude to infer it. Then Claude writes what the file
   itself declares and marks it *(inferred)*. It never infers
   unasked, and it writes nothing of the source before you answer.
   You should now see the question, and after your answer the entry.

7. **The index entry.** Claude adds the source to
   `sources/00-INDEX.md` (made from `templates/index.md` if missing).
   The entry has these fields:
   - What: what the resource is, in one or two sentences.
   - Origin: where it came from.
   - Date: as in step 4.
   - Form: text, extract of an original, or binary.
   - Role: as you answered.
   - Use for: the questions the source answers best.

   You should now see the entry in `sources/00-INDEX.md`.

8. **Another project's document is cited, not copied.** When you point
   a project at a document that lives in another project (a library's
   among them), nothing is stored in `sources/`. The index entry names
   the path and says what it is for. The ledger finds the citation by
   itself. For a library's document see
   [Share material through a library](share-material-through-a-library.md).
   You should now see an entry with a path and no file in `sources/`.

9. **Bookkeeping and the reply.** Claude remakes the ledger (the
   state report made at read time from the documents). In a sweep it
   also fills gaps in entries of files already registered. The reply
   is two lines at most: the file stored and its entry, and what the
   source adds to the intent in one line, or "nothing new".
   You should now see those two lines and nothing more.

## The sweep and changed files

In a sweep, Claude also reports files whose modification time is later
than the date of their index entry, and asks what to do with each. What
a change means depends on the kind of project:

- In a thought project it is a breach of immutability. You choose:
  re-register beside as a new source, restore the file, or accept the
  change knowingly on your word.
- In a library it is the owner's ordinary maintenance. Claude updates
  the entry, its date included, and nothing else.

Claude never re-registers silently.

## What you have afterwards

- The source stored in `sources/`, in one form, or cited by path.
- An entry in the index with its role, date and form.
- Nothing carried into the intent or any other document. Registration
  is not intake: you direct every use, and anything that later enters
  the intent is cited with its file. The reasons are on the page
  [Sources and research](../about/sources-and-research.md).

## If something goes wrong

- Personal matter in the text: the command stops before storing and
  asks. Choose to store, redact or drop.
- `markitdown` is not found: `doc2md.py` prints an error naming the
  install command, `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
  Install it and ask again, or pass the executable with
  `--markitdown-path`.
- A legacy format (`.doc`, `.ppt`, `.rtf`, `.odt`, `.odp`, `.ods`):
  the script reports it as unsupported. Resave it as `.docx`, `.pptx`
  or `.xlsx` first.
- An existing extract of the same name: the script prints `SKIP` and
  leaves it unless forced.
- A bundle that arrived whole and is addressed with `--bundle`:
  Claude refuses and says why.

## A worked example

You have a supplier's price offer as a Word file, `offer.docx`, for a
project with the placeholder slug `my-project`.

```
/ingest offer.docx my-project
```

Claude finds no personal matter and asks: "Convert to Markdown?" You
answer yes. It runs `python scripts/doc2md.py offer.docx -o sources/`,
and `sources/supplier-offer.md` is the source. It asks: "What is it
for?" You answer: "a price to compare other offers against". Claude
reads the offer and finds its date in the header. It writes the entry
in `sources/00-INDEX.md`:

```
### `supplier-offer.md`
- **What:** a supplier's price offer for a service.
- **Origin:** extract of `offer.docx` (markitdown)
- **Date:** 2026-03-02, from the content
- **Form:** extract of offer.docx
- **Role:** a price to compare other offers against
- **Use for:** what the service costs and on what terms
```

The reply is two lines: the file stored with its entry, and "nothing
new" for the intent.

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
