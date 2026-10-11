---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: a1fc728b3c97dab4
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

`/ingest` stores external input in the `sources/` directory of a project, records it in the project's ledger (the single record of its state) and catalogues it in the resource index. This page is for you, the one who has a document, a transcript or some pasted text and wants it in the project. The principal is the person whose thinking is being forged; where this page says "you", that is usually the principal.

## When to use it

Use it whenever material from outside enters the project: a document, a transcript, an offer, a standard, or text you paste into the conversation. A source may arrive at any stage, even before the brief.

Registering a source does not use it. Nothing of it enters the intent or any other document, and you decide when and how each source is used. The reasons are on [Sources and research](../about/sources-and-research.md).

## The command

```
/ingest [file] [slug]
```

Both arguments are optional. The slug names the project; where it is left out, Claude takes it from the context and asks if that is ambiguous.

- With a file: that document is registered.
- With text pasted into the conversation: the text is the source. Claude proposes a slug from its content and stores it as `sources/<slug>.md`, with a two-line header that gives its origin (pasted into the conversation) and the date.
- Bare, `/ingest` sweeps. It looks in `sources/` for files that are not yet registered and registers them all. A subdirectory counts as one bundle, never file by file.

A sweep also reports files that changed after their registration, and asks what to do with each. The answer depends on the kind of project:

- In a thought project a changed source is a breach of immutability. You settle it: register the new file beside the old one as a new source, restore the old one, or accept the change knowingly.
- In a library (a project that holds shared material and has no chain) a changed document is the owner's ordinary maintenance. Claude updates the index entry and the date in the ledger, and nothing else.

Claude never re-registers a changed file silently.

## What happens

1. **Personal matter stops the command.** Before anything is stored, Claude checks the text for personal matter: a named private person, an identifying detail, health, anything of the kind. If it finds some, it stops and asks you: store as it is, redact before registration, or drop. You should now see a question and no new file. This is asked first because a registered source cannot be changed afterwards.
2. **The file is stored.** Claude copies it into `sources/` under a short descriptive slug taken from its content or original name, with no date in the filename. On a name collision it adds the suffix `-2`. A file already registered is never renamed or modified. You should now see the file in `sources/`.
3. **A binary gets one question.** For every binary file (PDF, Word, PowerPoint, Excel and the like), alone or inside a bundle, Claude asks one question: convert to Markdown? Text files get no question.
   - Yes: `python scripts/doc2md.py <file> -o sources/` makes an extract, `<short-slug>.md`. The extract is the source. The original is not copied into the project. If the original already lies in `sources/` (as in a sweep), it is added to `sources/.gitignore` and stays there on your machine only.
   - No: the binary itself is the source, as a functional thing such as a deck template, a graphic or a logo. It is stored and registered as it is, with no extract.

   Keeping both is the exception and needs your explicit word. You should now see either the extract or the binary in `sources/`. What the converter reads and what it needs installed is on [Scripts](../reference/scripts.md).
4. **The source is catalogued.** Claude adds an entry to `sources/00-INDEX.md`, creating the index if it is missing. The entry has four fields:
   - What: what the resource is.
   - Origin: where it came from, with the date as far as it is known.
   - Role: what it is for, in your word.
   - Use for: the questions it answers best.

   For an extract, the origin reads "extract of the original (markitdown)". You should now see the new entry in `sources/00-INDEX.md`.
5. **Claude asks what the source is for.** After every registration Claude asks "what is it for?". You answer with the role, or tell Claude to infer it. If you do, Claude writes what the file itself declares and marks it as inferred. It never infers unasked; until you answer, the role stays a dash. You should now see the question at the end of a reply of three lines at most.
6. **The ledger is updated.** Claude records the source in the ledger. The date is the document's own date where it can be found for free (in its content, else in its file metadata) and the date of the ingest otherwise. You are never asked for a date.

## A related set of files

A set of related files, such as a downloaded site with its index, is stored as a directory `sources/<slug>/`. It counts as one source with one ledger row. It has its own `00-INDEX.md`, with a short paragraph on what the whole is and why it entered, followed by one entry per file in the shape above. Claude creates that index if the bundle arrives without one. If one arrives with it, Claude checks it against the actual contents and reports the gaps. In the project's own index the bundle appears as a single entry that points to the inner index.

## A document of a library

A document that lives in a library is cited, not copied. When you point a project at one, nothing is stored in `sources/`. Claude adds an index entry that names the path and says what it is for, and registers the library as a dependency in the ledger. Citing a library's document from a project is described on [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`: the file, the extract, or the bundle directory.
- An entry in `sources/00-INDEX.md`, with its Role once you have answered.
- A record of the source in the ledger.
- Nothing carried into the intent or any other document.

## If something goes wrong

- Personal matter in the text: the command stops before storing and asks. Answer store, redact or drop.
- `markitdown` is not installed: `doc2md.py` prints "ERROR: markitdown not found" and the install line, `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`. It never installs anything itself. Install it, reopen the shell, and ingest again.
- A legacy format (`.doc`, `.ppt`, `.rtf`, `.odt` and the like): the converter warns that it cannot read it. Resave the file as `.docx`, `.pptx` or `.xlsx` and ingest that.
- An extract of that name already exists: the converter prints "SKIP" and leaves it, unless it is forced.
- A conversion fails: the converter prints "FAIL" with the exit code of `markitdown`, and the run ends with a count of converted, skipped and failed files.
- A changed source found in a sweep: see the command above; Claude waits for your choice.

## A worked example

You have a Word document, `example-offer.docx`, and you are working in a thought project.

```
/ingest example-offer.docx <slug>
```

1. Claude finds no personal matter and goes on.
2. It asks: convert to Markdown? You answer yes.
3. It runs `python scripts/doc2md.py example-offer.docx -o sources/` and prints a line of the form "OK  example-offer.docx -> example-offer.md".
4. It adds an entry for `example-offer.md` to `sources/00-INDEX.md`, with the origin "extract of `example-offer.docx` (markitdown)", and records the source in the ledger.
5. It replies in three lines: the file stored and its index entry; what the source adds to the intent, or "nothing new"; and the question "what is it for?".
6. You answer, for instance "a price list to check the budget against". Claude writes that as the Role.

You should now see `sources/example-offer.md` and its entry in the index. Nothing else has changed.

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document from a project.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
