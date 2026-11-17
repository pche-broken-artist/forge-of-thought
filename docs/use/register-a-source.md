---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 9ec8a60acf2c131e
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

`/ingest` stores external input in the `sources/` folder of a project,
asks what it is for and catalogues it in the index of that folder. This
page is for you, the principal (the person whose thinking is forged), when a
document, a transcript or a piece of text has arrived and the project
should keep it.

## When to use it

Use it when something from outside the project, such as an offer, a
standard or minutes, should be kept as it arrived. It may arrive at any
stage, even before the brief. Registering a source does not use it: the
command never carries content into the intent or any other document, and
you direct every use. See [Sources and research](../about/sources-and-research.md)
for why sources are immutable and why registration is not intake.

## The command

```
/ingest [file] [slug] [--bundle name]
```

The slug is the project's. If it is ambiguous, Claude asks.

A real line, with a placeholder file:

```
/ingest vendor-offer.docx my-project
```

The forms of the command:

- With a file: that document is registered.
- With text pasted into the conversation: the text becomes
  `sources/<slug>.md`, the slug proposed from its content, under a
  two-line header (origin: pasted into the conversation; date).
- With `--bundle <name>`: the file goes into a bundle of one origin that
  keeps arriving.
- Bare: a sweep. Claude looks for files in `sources/` that are not yet in
  the index and registers them. It also reports files changed since their
  registration.

## What happens

1. **Personal matter stops the command.** If the text carries a named
   private person, an identifying detail, health or anything of the kind,
   Claude stops before storing and asks: store as it is, redact before
   registration, or drop.
   You should now see that question, and nothing stored. A registered
   source is immutable, so redaction can only happen before it.
2. **The file is stored.** It is copied into `sources/` as
   `<short-slug>.<ext>`, with a short descriptive slug, no date in the
   name, and a `-2` suffix on a name collision. A file already in the
   index is never renamed or modified.
   You should now see the file in `sources/` under its slug.
3. **Every binary gets one question: convert to Markdown?** A binary is a
   PDF, a Word, PowerPoint or Excel file and the like. A text file gets no
   question.
   - Yes: Claude runs `python scripts/doc2md.py <file> -o sources/`. The
     extract `<short-slug>.md` is the source, and the original is not
     copied into the project. If the original already lies in `sources/`,
     it is listed in `sources/.gitignore` and stays there, local only.
   - No: the binary is the source as a functional thing, such as a deck
     template, a graphic or a logo. It is stored and indexed as it is,
     with no extract.

   Keeping both is the exception and needs your explicit word.
   You should now see either the extract beside the index or the binary
   alone, one form per source.
4. **Claude asks what the source is for.** The answer is its Role. You may
   instead tell Claude to infer it. Then Claude writes what the file
   itself declares and marks it *(inferred)*. Claude never infers unasked,
   and writes nothing about the source before you answer. One question is
   asked per source, one per message. A bundle gets one question for the
   whole, and in a sweep the sources are taken one by one.
   You should now see the question "what is it for?" before any entry
   exists.
5. **The entry is written** in `sources/00-INDEX.md`, created from the
   template if it is missing. The entry has these fields:
   - What: what the source is, in one or two sentences.
   - Origin: where it came from.
   - Date: the document's date, best effort and never asked. It comes from
     the content, else from the file, else it is the day of the ingest,
     and the field says which.
   - Form: text, extract of the original, or binary.
   - Role: your answer to step 4.
   - Use for: what to reach for the source for.

   You should now see the new entry in the index.
6. **Claude remakes the ledger** (the state record built from the
   documents) and replies.
   You should now see a reply of two lines at most: the file stored with
   its index entry, and what the source adds to the intent in one line,
   or "nothing new". There is no analysis of the content and no next
   step implied.

### A related set that arrives whole

A downloaded site with its index, say, is stored as `sources/<slug>/`: one
source with one entry in the project index, which points to the bundle's
own `00-INDEX.md`. Bundles go two levels and never deeper. If the set
arrives without an index, Claude creates one from the bundle template. If
it arrives with one, Claude checks it against the actual contents and
reports gaps. In a sweep a subdirectory is registered as one bundle, never
file by file.

### A source that keeps arriving

`/ingest <file> --bundle <name>` is for one origin that keeps sending
files.

- If `sources/<name>/` does not exist, it is born at the first file as a
  growing bundle. Its index opening paragraph says that it grows.
- If it exists and grows, the file is stored inside it, never beside it.
  The file gets its own entry in the bundle's index.
- If it exists and arrived whole, the command refuses and says why.

Each file of a growing bundle is immutable from its own registration, and
a file added to it gets one Role question of its own. What cites such a
bundle cites the file by its path.

### A document of another project

A document that lives in another project, a library's among them, is cited
by path in an index entry and not copied. The entry names the path and
says what it is for. The ledger finds the citation by itself. See
[Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`, in one form, immutable.
- An entry in `sources/00-INDEX.md` (and in the bundle's own index for a
  bundle file) with its Role from birth.
- The ledger remade.
- The intent and every other document unchanged.

## If something goes wrong

- Claude stops and asks about personal matter, as in step 1. Nothing is
  stored until you answer.
- `--bundle` names a bundle that arrived whole: the command refuses. Use
  another name or register the file as a source of its own.
- A file already in the index has changed since registration, as a sweep
  reports. In a thought project this is a breach of immutability, and
  Claude asks what to do with each file: re-register it beside as a new
  source, restore it, or accept the change on your word. In a library the
  change is the owner's ordinary maintenance, and Claude only updates the
  entry, its date included. Nothing is re-registered silently.
- `doc2md.py` reports a format as unsupported. It handles `.pdf`, `.docx`,
  `.docm`, `.pptx`, `.pptm`, `.xlsx`, `.xlsm`, `.xls`, `.epub`, `.html`,
  `.htm`, `.csv`, `.json`, `.xml` and `.msg`. The legacy `.doc`, `.ppt`,
  `.rtf`, `.odt`, `.odp` and `.ods` must be resaved as `.docx`, `.pptx` or
  `.xlsx` first.
- The conversion needs markitdown, which the script never installs for
  you. The script's help gives the install line, and
  [Scripts](../reference/scripts.md) lists what it needs.
- A binary that already sits in git beside its extract is taken out of git
  only by your own act, by hand. No script does it, and no sweep.

## A worked example

A PDF with a made-up name, `acme-offer.pdf`, has arrived, and the project
slug is `my-project`.

```
/ingest acme-offer.pdf my-project
```

1. The text has no personal matter, so Claude goes on.
2. Claude asks whether to convert the PDF to Markdown. You say yes.
3. Claude runs `python scripts/doc2md.py acme-offer.pdf -o sources/`, and
   `sources/acme-offer.md` appears.
4. Claude asks what the source is for. You answer: "a price to compare
   against".
5. Claude writes the entry in `sources/00-INDEX.md`: What, Origin, the
   date from the content, Form "extract of acme-offer.pdf", Role "a price
   to compare against", Use for.
6. Claude replies in two lines: `sources/acme-offer.md` stored and
   indexed, and the source adds nothing new to the intent.

For terms of the forge see the [Glossary](../reference/glossary.md).

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
