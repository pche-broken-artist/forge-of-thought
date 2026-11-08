---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: af41d287825ed3d3
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how to store external input in a project, record what it is for and catalogue it, with `/ingest`. It is for you, the principal (the person whose thinking is being forged), when a document, a transcript or a pasted text arrives and the project should know about it. A source is the term for such an input once it is registered; see the [Glossary](../reference/glossary.md).

## When to use it

- A document arrives that the project may draw on later.
- You paste text into the conversation that should be kept as it is.
- A related set of files arrives, or files of one origin keep arriving.
- You want to know which files in `sources/` are not yet registered, or have changed since registration.
- A document of another project should be pointed at from this one.

Registration is not intake. `/ingest` stores, records and catalogues, and nothing more: it carries no content into the intent or any other document. You direct every later use. The reasons are on [Sources and research](../about/sources-and-research.md).

## The command

```
/ingest [file] [slug] [--bundle name]
```

Examples as they can be typed:

```
/ingest vendor-offer.docx my-project
/ingest minutes.pdf my-project --bundle meeting-notes
/ingest
```

Without a slug, Claude takes the project from the context and asks if it is ambiguous.

## What happens

1. **Personal matter stops the command.** Before anything is stored, Claude checks the text for personal matter, such as a named private person, an identifying detail or health information. If it finds some, it stops and asks: store as it is, redact before registration, or drop. You should now see that question, and nothing stored yet. A registered source is immutable, so redaction can only happen before registration.

2. **The source is stored.** What is stored depends on what you give it.
   - A file: that document is copied into `sources/` under a short descriptive slug, `<short-slug>.<ext>`, with no date in the name. On a name collision the slug gets `-2`.
   - Text pasted into the conversation: the text is stored as `sources/<slug>.md`, the slug proposed from its content, with a two-line header giving its origin (pasted into the conversation) and its date.
   - A related set that arrives whole: it is stored as `sources/<slug>/`, a bundle with one entry and its own index.
   - `--bundle <name>`: the file goes into a bundle of one origin that keeps arriving. If `sources/<name>/` does not exist, it is born with this first file, and its index says that the bundle grows. If it exists and grows, the file is stored inside it, never beside it, and gets its own entry in the bundle's index. If it exists and arrived whole, Claude refuses and says why.

   You should now see the file under `sources/`.

3. **Every binary gets one question.** For each binary file (PDF, DOCX, PPTX, XLSX and the like), alone or inside a bundle, Claude asks: convert to Markdown? Text files get no question.
   - Yes: `scripts/doc2md.py` makes the extract, `<short-slug>.md`, and the extract is the source. Its origin is recorded as an extract of the original. The original is not copied into the project. If it already lies in `sources/`, it is added to `sources/.gitignore` and stays there, local only.
   - No: the binary is the source as a functional thing, such as a deck template, a graphic or a logo. It is stored and registered as it is, with no extract.

   Keeping both is the exception and needs your explicit word. The formats `doc2md.py` handles and what it needs installed are on [Scripts](../reference/scripts.md). You should now see one file per source, either the extract or the binary.

4. **Claude asks what the source is for.** The question comes before the index entry exists, so the entry carries your answer from its birth. It is one question per source, one for a whole bundle, and one of its own for each file added to a growing bundle. Your answer is the entry's Role. Alternatively you tell Claude to infer it; then Claude writes what the file itself declares and marks it *(inferred)*. It never infers unasked, and writes nothing about the source before you answer.

5. **The index entry is written.** Claude adds the source to `sources/00-INDEX.md`, creating the index if it is missing. An entry has these fields:
   - What: what the resource is.
   - Origin: where it came from.
   - Date: the origin date of the document, found for free from its content, else from the file, else the ingest date. The field says which. You are never asked for a date.
   - Form: text, extract of an original, or binary.
   - Role: what it is for, as you answered.
   - Use for: the questions it answers best.

   A bundle appears in the top index as one entry pointing to its own `00-INDEX.md`, made from the bundle skeleton: its opening paragraph says what the whole is and whether it arrived whole or grows, and each file has an entry in the same shape. If a bundle arrives with an index, Claude checks it against the actual contents and reports gaps. You should now see the new entry in `sources/00-INDEX.md`.

6. **The ledger is remade and Claude replies.** The reply is two lines at most: the file stored with its index entry, and what the source adds to the intent in one line, or "nothing new". There is no analysis of the content and no next step implied.

## Sweeping for what is unregistered

Bare `/ingest` scans `sources/` for files not yet in the index and registers them one by one, asking the Role question source by source. A subdirectory is registered as one bundle, never file by file, and Claude asks whether it grows when it asks for its role. A file inside a bundle that has no entry in the bundle's index is offered for registration there.

The sweep also reports files changed since registration, with a question for each, and never re-registers silently. What a change means depends on the kind of project:

- In a thought project, a changed source breaches immutability. You choose: register the changed file beside the old one as a new source, restore it, or accept the change knowingly on your word.
- In a library, a changed document is the owner's ordinary maintenance. Claude updates the index entry, its Date included, and nothing else.

## Citing a document of another project

A document that lives in another project, a library's among them, is cited by path and not copied. Nothing is stored in `sources/`. Claude adds an index entry that names the path and says what it is for, and the ledger finds the citation by itself. Moving a document out of a project into a library is the reverse: it is ingested there, and the project's entry is replaced by the citation. How a library is used is on [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`, immutable from its registration: either a text file, an extract, or a functional binary.
- An entry in `sources/00-INDEX.md` (or in a bundle's own index) with its Role, Date and Form.
- Nothing carried into the intent or any other document.

## If something goes wrong

- Personal matter is found: the command stops before storing and asks whether to store as it is, redact or drop.
- The bundle named by `--bundle` arrived whole: Claude refuses and says why. Nothing is stored in it.
- A source in a thought project has changed since registration: the sweep reports it and asks. It never re-registers by itself.
- The conversion does not run: `doc2md.py` needs `markitdown` on the path and never installs anything. Legacy formats (`.doc`, `.ppt`, `.rtf`, `.odt`, `.odp`, `.ods`) are reported as unsupported; resave them as `.docx`, `.pptx` or `.xlsx` first. The details are on [Scripts](../reference/scripts.md).

## A worked example

A vendor sends a PDF offer, and you want it in the project `my-project`.

```
/ingest vendor-offer.pdf my-project
```

Claude finds no personal matter and asks: convert to Markdown? You answer yes. `doc2md.py` writes `sources/vendor-offer.md`, and Claude asks what the source is for. You answer: "to compare the price and terms with our own estimate". Claude adds this entry to `sources/00-INDEX.md`:

```
### `vendor-offer.md`
- **What:** the vendor's offer for the work, with price and terms
- **Origin:** extract of `vendor-offer.pdf` (markitdown)
- **Date:** 2026-03-02, from the content
- **Form:** extract of vendor-offer.pdf
- **Role:** to compare price and terms with our own estimate
- **Use for:** what the vendor commits to, and at what price
```

Claude replies in two lines: the file stored and its entry, then "nothing new" for the intent. The offer is catalogued and waits for you to use it.

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
