---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 6fe78e773da19345
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how you store, register and catalogue external input with `/ingest`. It is for the principal (the person whose thinking is being forged) who has a document, a pasted text or a set of files that the project should keep as a source.

A source is external input as it arrived: a transcript, an offer, a standard. Registering it stores it in `sources/` and writes one entry for it in the index `sources/00-INDEX.md`. Nothing more happens.

## When to use it

- You have a file, or a text you can paste, that belongs to the project as input.
- A set of related files arrives whole, or files of one origin keep arriving.
- You want to find out which files in `sources/` are not yet registered, or which have changed since they were.
- You want the project to point at a document that lives in another project.

Registration is not intake. The source waits until you decide how and when to use it, and nothing of it is carried into the intent. Why sources are immutable and why registration is not intake is explained in [Sources and research](../about/sources-and-research.md).

## The command

```
/ingest [file] [slug] [--bundle name]
```

The slug names the project and is taken from context when you leave it out. The forms are:

- `/ingest vendor-offer.docx my-project`: registers that document.
- Text pasted into the conversation, with `/ingest`: Claude stores the text as `sources/<slug>.md`, the slug proposed from its content. The file opens with a two-line header: the origin (pasted into the conversation) and the date.
- `/ingest minutes-1.pdf my-project --bundle meeting-notes`: puts the file into a bundle of one origin that keeps arriving. The bundle is born with its first file.
- `/ingest` with no arguments: a sweep, described below.

## What happens

1. **Personal matter stops the command.**
   Before anything is stored, Claude checks whether the text carries personal matter, such as a named private person, an identifying detail or health. If it does, Claude asks whether to store it as it is, redact it first, or drop it. Redaction happens before registration because a registered source cannot be changed.
   You should now see a question from Claude, or no question at all when nothing personal is in the text.

2. **The file is stored.**
   Claude copies the document into `sources/` as `<short-slug>.<ext>`, a short descriptive name with no date in it. On a name collision it adds the suffix `-2`. A file already registered is never renamed or modified.
   You should now see the file in `sources/`.

3. **Every binary gets one question: convert to Markdown?**
   A text file gets no question. For a binary (PDF, Word, PowerPoint, Excel and the like) Claude asks once per file.
   - Yes: Claude runs `python scripts/doc2md.py <file> -o sources/`. The Markdown extract is then the source, and the original is not copied into the project. If the original already lay in `sources/`, it stays there as a local file only.
   - No: the binary is the source as a functional thing, such as a deck template or a logo. It is stored and registered as it is, with no extract.
   Keeping both is an exception, made only on your explicit word. The script is the only way a conversion is made. Its formats and what it needs are in [Scripts](../reference/scripts.md).
   You should now see the extract `<short-slug>.md` in `sources/`, or the binary itself.

4. **Claude asks what the source is for.**
   This is asked before the index entry exists, so the entry carries the answer from its birth. You answer with the role, for example a standard to verify against, inspiration, a counter-example or a meeting record. Or you tell Claude to infer it. Then Claude writes what the file itself declares and marks it as inferred. Claude never infers it unasked, and it writes nothing of the source before you answer. A bundle gets one question for the whole, and each file added later to a growing bundle gets one of its own.
   You should now see your answer, or the marked inference, carried into the next step.

5. **The index entry is written.**
   Claude adds the entry to `sources/00-INDEX.md`, creating the index if it is missing. The entry has these fields:
   - What: what the source is, in one or two sentences.
   - Origin: where it came from, such as an author, a meeting or an extract of the original.
   - Date: the document's own date, best effort. It comes from the content if it can be found, else from the file, else it is the day of registration. The field says which. You are never asked for a date.
   - Form: text, extract of the original, or binary. Each source has one form.
   - Role: your answer from the previous step.
   - Use for: the questions the source answers best.
   You should now see the new entry in `sources/00-INDEX.md`.

6. **Claude replies in two lines at most.**
   The first line names the file stored and its index entry. The second says in one line what the source adds to the intent, or "nothing new". There is no analysis of the content and no next step implied.
   You should now see those two lines.

### A related set that arrives whole

A set of related files, such as a downloaded site with its index, is stored as a subdirectory `sources/<slug>/`. It counts as one source with one entry in the main index. It carries its own index `00-INDEX.md`. Claude creates that index from the bundle template if the set arrives without one. If one was supplied, Claude checks it against the actual contents and reports the gaps. The index opens with a short paragraph saying what the whole is, why it entered the project, and that it arrived whole.

### A bundle that keeps growing

With `--bundle <name>`, the bundle is for one origin that keeps arriving. If `sources/<name>/` is missing, it is born at the first file, its index saying in the opening paragraph that it grows. If it exists and grows, the file is stored inside it, never beside it, and gets its own entry in the bundle's index. Each file is immutable from its own registration. A bundle that arrived whole refuses new files, and Claude says why.

### Bare `/ingest`: the sweep

Without arguments, Claude scans `sources/` for files that have no index entry and registers them, source by source, with the questions above. A new subdirectory is registered as one bundle, never file by file, and Claude asks whether it grows. A file inside an existing bundle that has no entry in the bundle's index is offered for registration there.

The sweep also reports files whose modification time is later than the date of their entry, and asks what to do with each. What a change means depends on the kind of project:

- In a thought project, a changed source is a breach of immutability. You resolve it by registering the new version beside the old as a new source, by restoring the original, or by accepting the change knowingly. Claude never re-registers silently.
- In a library, a changed document is its owner's ordinary maintenance. Claude updates the index entry, its date included, and nothing else.

### A document of another project

When you point a project at a document that lives in another project, nothing is stored in `sources/`. Claude adds an index entry that names the path and says what the document is for. The ledger (the file that shows the state of the project, made when it is read) finds the citation by itself. This is how a library's document is used; the whole way is in [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`: the text file, the extract, the binary, or the bundle directory.
- One entry in `sources/00-INDEX.md` with its role, date and form, and for a bundle its own index.
- A remade ledger. What the source is and is for lives in the index alone.
- Nothing carried into the intent or any other document.

## If something goes wrong

- Claude stops with a question about personal matter. Answer with one of the three choices: store as it is, redact before registration, or drop. Nothing is stored before you answer.
- A registered source has changed. In a thought project, Claude lists it in the sweep and asks what to do. Pick one of the three ways above.
- A bundle that arrived whole refuses a new file. Register the file as a source of its own, or as the first file of a growing bundle with another name.
- The conversion does not run. `doc2md.py` uses markitdown, which it never installs itself. Install it as the script's help says. The legacy formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported, so resave them as `.docx`, `.pptx` or `.xlsx` first. See [Scripts](../reference/scripts.md).
- You do not know what a source is for. Tell Claude to infer the role. The entry then says so.

## A worked example

You have a Word file with a supplier's offer and a project called `my-project`.

```
/ingest supplier-offer.docx my-project
```

Claude finds no personal matter. It asks: "supplier-offer.docx is a binary. Convert to Markdown?" You answer yes. It runs `python scripts/doc2md.py supplier-offer.docx -o sources/` and the extract `sources/supplier-offer.md` is the source. It asks: "What is it for?" You answer: "a price to compare against". Claude writes the entry in `sources/00-INDEX.md` with the origin "extract of `supplier-offer.docx` (markitdown)", the date taken from the offer's own header, the form "extract of supplier-offer.docx" and your role. Then it replies:

```
Stored sources/supplier-offer.md and indexed it.
Adds nothing new to the intent.
```

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
