---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: ea40c979392de49c
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how you store, register and catalogue external input (a transcript, an offer, a standard, a pasted text) in a project with `/ingest`. It is for the principal, the person whose thinking is forged, who brings the material in.

## When to use it

Use it whenever material that did not come from you or from Claude should become part of the project: a document, a set of related files, or text you paste into the conversation. Registration only stores and catalogues the material. It never carries anything into your intent. The reasons are on [Sources and research](../about/sources-and-research.md).

## The command

```
/ingest [file] [slug]
```

Both arguments are optional. The slug names the project; when it is left out, Claude takes it from the context and asks if that is ambiguous.

- With a file: that document is registered.
- With text pasted into the conversation: the text is the source. Claude stores it as `sources/<slug>.md`, proposes the slug from the content, and gives it a two-line header (origin: pasted into the conversation; date).
- Bare: a sweep. Claude looks in `sources/` for files not yet recorded in the ledger (the project's table of state) and registers them all. It also reports files changed since registration and asks what to do with each.

A typed example:

```
/ingest vendor-offer.docx my-project
```

## What happens

1. Claude checks the material for personal matter, such as a named private person, an identifying detail or health information. If it finds any, the command stops and asks: store as it is, redact before registration, or drop.
   You should now see a question about the personal matter, and nothing stored yet. A registered source cannot be changed, so redaction always comes before registration.
2. Claude stores the file in `sources/` as `<short-slug>.<ext>`, with a short descriptive slug and no date in the name. On a name collision the slug gets the suffix `-2`.
   You should now see the file under `sources/`.
3. A related set of files is stored as a bundle, `sources/<slug>/`, and counts as one source. In a sweep, Claude registers a subdirectory as one bundle, never file by file. If the bundle has no `00-INDEX.md`, Claude creates one from the bundle index template. If it came with one, Claude checks it against the actual contents and reports gaps.
   You should now see one source for the whole set, with its own index.
4. For every binary file (PDF, DOCX, PPTX, XLSX and the like), Claude asks one question: convert to Markdown?
   - Yes: `scripts/doc2md.py` makes the Markdown extract, and the extract is the source. The original is not copied into the project. If it already lies in `sources/`, Claude adds its path to `sources/.gitignore` and leaves it there, local only.
   - No: the binary itself is the source, as a functional thing (a deck template, a graphic, a logo). It is stored and registered as it is, with no extract.

   Text files get no question. Keeping both the original and the extract is an exception, made only on your explicit word.
   You should now see either the extract `<short-slug>.md` or the binary, one of them and not both.
5. Claude adds an entry to `sources/00-INDEX.md`, after reading enough of the file to say truthfully what it is. The entry has four fields:
   - What: what the resource is.
   - Origin: where it came from, with a date as best known.
   - Role: what the source is for.
   - Use for: the questions to reach for it with.

   You should now see the new entry in the index, with Role still empty.
6. Claude records the source in the project's ledger, and in a sweep it also fills index gaps for files already registered.
   You should now see a reply of three lines at most: the file stored and its index entry, what the source adds to the intent (in one line, or "nothing new"), and the question "what is it for?".
7. You answer that question. Your answer is the Role. You may instead tell Claude to infer it. Claude then writes what the file itself declares and marks it as inferred. It never infers unasked, and the Role stays empty until you answer.
   You should now see the Role in the index entry.

A document that lives in a library is not copied. When you point a project at one, nothing is stored in `sources/`. Claude adds an index entry that names its path and says what it is for, and records the dependency in the ledger. See [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`, a file or a bundle, which is never changed from this moment.
- An entry in `sources/00-INDEX.md` with its Role.
- A row for it in the project's ledger.
- Nothing carried into your intent or any other document. Registration is not intake: you direct every use of a source, and anything you later take from it is cited with the file.

## If something goes wrong

- Personal matter in the text: the command stops before storing and asks what to do. Nothing is stored until you answer.
- A name collision in `sources/`: the new file gets the suffix `-2`, and the existing one is never renamed or changed.
- A file changed after registration, found by a bare sweep: Claude never re-registers silently and asks what to do with each such file.
  - In a thought project this is a breach of immutability. You choose: re-register it beside the old one as a new source, restore the original, or accept the change knowingly on your word.
  - In a library the change is the owner's ordinary maintenance. Claude updates the index entry and the ledger date and nothing else.
- A format `scripts/doc2md.py` cannot convert: the legacy formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported. Resave them as `.docx`, `.pptx` or `.xlsx` first. Which formats the script handles and what it needs installed is on [Scripts](../reference/scripts.md).
- The conversion engine missing: the script never installs anything. It uses markitdown, which you install yourself with `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.

## A worked example

You have a meeting record as a Word file and want it in the project `my-project`.

```
/ingest meeting-record.docx my-project
```

Claude finds no personal matter and stores nothing yet. It asks: convert `meeting-record.docx` to Markdown? You answer yes. Claude runs `python scripts/doc2md.py meeting-record.docx -o sources/`, and `sources/meeting-record.md` becomes the source. Claude adds the entry to `sources/00-INDEX.md` and replies in three lines: the file stored and indexed, "nothing new" for the intent, and "what is it for?". You answer "a record of the decisions taken, to verify the intent against". That sentence is the Role, and the source waits until you decide to use it.

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
