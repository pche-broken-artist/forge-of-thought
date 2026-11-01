---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: e247fa90380f9fd1
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

`/ingest` stores external input in the `sources/` folder of a project, asks what it is for and catalogues it in the folder's index. This page is for you when a transcript, an offer, a standard or a pasted text has to enter a project. Nothing is processed: the command registers a source and does no more. The principal (the person whose thinking is being forged) decides if and how the source is ever used.

## When to use it

- A document, or text you have at hand, should be kept as an immutable input of the project.
- Several files of one origin keep arriving and belong together.
- You want to find files that lie in `sources/` without an entry, or files that changed after they were registered.
- A document of another project should be pointed at without a copy.

## The command

```
/ingest [file] [slug] [--bundle name]
```

The second argument is the project slug. Where it is left out, Claude takes it from the context and asks if that is ambiguous.

One line that can be typed as it stands, with a placeholder:

```
/ingest path/to/offer.pdf <slug>
```

The forms of the command:

- With a file, that document is registered.
- With text pasted into the conversation, the text becomes the source and is stored as `sources/<slug>.md`. Claude proposes the slug from the content and adds a two-line header: the origin (pasted into the conversation) and the date.
- With `--bundle <name>`, the file goes into a bundle of one origin that keeps arriving.
- Bare, `/ingest` sweeps `sources/` for files that are not yet in the index and registers them. It also reports files changed since their registration.

## What happens

1. **Personal matter stops the command.** Before anything is stored, Claude checks the text for personal matter, such as a named private person, an identifying detail or health. If it finds some, it asks you to choose: store as it is, redact before registration, or drop. You should now see a question and no file in `sources/` yet. A registered source cannot be changed, so redaction can only happen before registration.
2. **The file is stored.** It is copied into `sources/` as `<short-slug>.<ext>`, a short descriptive slug without a date. On a name collision the slug gets the suffix `-2`. You should now see the file in `sources/`.
3. **Every binary gets one question: convert to Markdown?** A binary is a PDF, a Word, PowerPoint or Excel file and the like. Text files get no question.
   - Yes: `scripts/doc2md.py` makes the extract. The extract is then the source, and its entry names the original as its origin. The original is not copied into the project. If it already lay in `sources/`, it stays there as a local file that git does not track.
   - No: the binary is the source as a functional thing, such as a deck template or a graphic. It is stored and registered as it is, with no extract.
   - Keeping both is the exception, and only on your explicit word.

   You should now see either the `.md` extract or the binary in `sources/`.
4. **Claude asks what the source is for.** The question comes before the index entry exists, so that the entry carries your answer from its birth. Your answer is the Role of the source. You may instead tell Claude to infer it. Then Claude writes what the file itself declares and marks it as inferred. Claude never infers it unasked, and it writes nothing about the source before you answer. A bundle gets one question for the whole, and a file added to a growing bundle one of its own. You should now see the question, and after your answer the entry.
5. **The index entry is written** in `sources/00-INDEX.md`, which is created from its template if it is missing. The entry has these fields:
   - What: what the source is, in one or two sentences.
   - Origin: where it came from.
   - Date: the date of the source, found for free and never asked. The field says whether it comes from the content, from the file or from the ingest.
   - Form: text, extract of the original, or binary.
   - Role: your answer.
   - Use for: what to reach for the source for.

   You should now see the entry in the index.
6. **Claude remakes the ledger** (the project's state report, built from its documents) and replies in two lines at most: the file stored and its index entry, then what the source adds to the intent in one line, or "nothing new". There is no analysis of the content and no next step implied. You should now see those two lines.

## Bundles

A related set that arrives whole is stored as `sources/<slug>/` and counts as one source with one entry in the main index. Its own `00-INDEX.md` is made from the bundle template if it arrives without one. A supplied one is checked against the real contents and gaps are reported. In a sweep, a subdirectory is registered as one bundle and never file by file.

A bundle of one origin that keeps arriving is registered with `--bundle <name>`:

- If `sources/<name>/` does not exist, it is born at the first file as a growing bundle. Its index opening paragraph says that it grows.
- If it exists and grows, the file is stored inside it, never beside it, with its own entry in the bundle's index. Each file is immutable from its own registration.
- If it exists and arrived whole, the command refuses and says why.

## Another project's document

A document that lives in another project, a library's among them, is cited and not copied. Nothing is stored in `sources/`. Claude adds an index entry that names the path and says what the document is for. The ledger finds the citation by itself. How a library is used is described in [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`: a text file, an extract or a binary, never changed again.
- An entry in the index with its Role, Date and Form.
- For a bundle, its folder, its own index and one entry in the main index.
- Nothing carried into the intent. Registration is not intake: you direct every later use of the source. The reasons are in [Sources and research](../about/sources-and-research.md).

## Sweep and changed files

A bare `/ingest` also reports files whose modification time is later than the Date of their entry, and asks what to do with each. The answer depends on the kind of project:

- In a thought project, a changed source breaches immutability. You choose between registering it beside the old one as a new source, restoring it, or accepting the change on your word.
- In a library, a changed document is the owner's ordinary maintenance. Claude updates the entry, its Date included, and nothing else.

Claude never re-registers silently.

## If something goes wrong

- The text carries personal matter: the command stops and asks before storing. Decide to store, redact or drop.
- A file is already in the index: it is never renamed or modified. A changed file is handled as in the sweep above.
- `--bundle` names a bundle that arrived whole: the command refuses. Register the file as its own source or choose another bundle name.
- The conversion fails: `doc2md.py` needs markitdown, which it never installs itself. It also reports the legacy formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` as unsupported. Resave them as `.docx`, `.pptx` or `.xlsx` first. The formats and the installation are described in [Scripts](../reference/scripts.md).

## A worked example

You have a PDF offer and a project with the slug `<slug>`.

```
/ingest path/to/offer.pdf <slug>
```

1. Claude finds no personal matter and copies the file into `sources/` as `example-offer.pdf`.
2. It asks: convert to Markdown? You answer yes. It runs the conversion and keeps `sources/example-offer.md` as the source, and the PDF stays out of the project.
3. It asks what the source is for. You answer: a price list to compare against.
4. It writes the entry in `sources/00-INDEX.md` with Origin "extract of the PDF (markitdown)", the Date from the content, Form "extract" and your Role.
5. It replies in two lines: the extract stored with its entry, and "nothing new" for the intent.

Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
