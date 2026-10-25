---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 86266f4a38c05c11
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how to store external input in a project, catalogue it and say what it is for, with `/ingest`. It is for the principal (the person whose thinking is being forged) who has a document, a pasted text or a set of files to bring in. Registration only stores and describes the input. Nothing of it enters the intent until you say so, which is why [Sources and research](../about/sources-and-research.md) calls registration not intake.

## When to use it

Use it when something from outside the project should be kept as it arrived: a transcript, an offer, a standard, a deck template, a graphic. A registered source is immutable from then on.

## The command

```
/ingest [file] [slug] [--bundle name]
```

The slug names the project; when it is left out, Claude takes it from the context and asks if that is ambiguous. What the command does depends on what follows it:

- With a file: that document is registered.
- With text pasted into the conversation: the text becomes the source, stored as `sources/<slug>.md`. The slug is proposed from the content, and the file opens with a two-line header (origin: pasted into the conversation; date).
- With `--bundle <name>`: the file goes into a bundle of one origin that keeps arriving. The bundle is born at its first file. Each file is immutable from its own registration.
- Bare: a sweep. Claude looks in `sources/` for files not yet in the index and registers them. It also reports files changed since registration and asks what to do with each.

A typed example:

```
/ingest vendor-offer.docx my-project
```

## What happens

1. Personal matter stops the command. If the text carries personal matter (a named private person, an identifying detail, health, anything of the kind), Claude stops before storing and asks: store as it is, redact before registration, or drop. Redaction happens first because a registered source cannot be changed. You should now see the question, and no file in `sources/` yet.
2. Claude stores the file in `sources/` under a short descriptive slug taken from the content or the original name, with no date in the name. On a name collision it adds `-2`. You should now see the file under `sources/`.
3. A set of related files that arrives whole is stored as `sources/<slug>/`, one index entry for the set. It gets its own index, made from the bundle template if the set came without one; a supplied index is checked against the contents and gaps are reported. In a sweep, a subdirectory is registered as one bundle, never file by file. You should now see one entry for the bundle.
4. Every binary (PDF, DOCX, PPTX, XLSX and the like) gets one question, per file: convert to Markdown?
   - Yes: `scripts/doc2md.py` makes the extract, and the extract is the source. The original is not copied into the project. If the original already lies in `sources/`, it stays there as a local file only, kept out of git.
   - No: the binary is the source as a functional thing, such as a deck template, a graphic or a logo. It is stored and indexed as it is.

   Text files get no question. You should now see either the extract `<slug>.md` or the binary in `sources/`.
5. Claude asks what the source is for. The answer is its Role. You may instead tell Claude to infer it, and then Claude writes what the file itself declares and marks it as inferred. It never infers unasked, and it writes nothing of the source before you answer. A bundle gets one question for the whole, and each file added to a growing bundle gets one of its own. In a sweep the question comes source by source. You should now see your answer, or the inferred Role marked as such, in the entry.
6. Claude writes the entry into `sources/00-INDEX.md`, creating the index if it is missing. The entry has these fields:
   - What: what the resource is, in one or two sentences.
   - Origin: where it came from. For an extract it reads "extract of `<original>` (markitdown)".
   - Date: the document's own date, best effort and never asked. Claude takes it from the content, else from the file, else the day of ingest, and the field says which.
   - Form: text, extract of the original, or binary.
   - Role: your answer.
   - Use for: the questions the source answers best.

   You should now see the entry in the index.
7. Claude remakes the [ledger](../reference/glossary.md) (the record of state, made when read) and replies in two lines at most: the file stored with its index entry, and in one line what the source adds to the intent, or "nothing new". It does not analyse the content and implies no next step.

### A bundle that keeps arriving

With `--bundle <name>`, a missing `sources/<name>/` is born as a growing bundle. Its index opens with a paragraph that says it grows. Later files are stored inside it, never beside it, each with its own entry in the bundle's index. If the bundle arrived whole, Claude refuses to add to it and says why. In a sweep, a file inside a bundle without an entry is offered for registration there, and a new subdirectory is asked whether it grows when the role is asked.

### A document of another project

A document that lives in another project, such as a library's, is cited and not copied. Nothing goes into `sources/`. Claude adds an index entry that names the path and says what the document is for, and the ledger finds the citation by itself. See [Share material through a library](share-material-through-a-library.md).

## What you have afterwards

- The source in `sources/`, unchanged from now on.
- An entry in `sources/00-INDEX.md`, or in the bundle's own index, with its Role, Date and Form.
- A remade ledger.
- No change to the intent or any other document.

## If something goes wrong

- Personal matter in the text: the command stops and asks. Choose store as it is, redact first, or drop.
- A file changed since its registration, found by a sweep: in a thought project this is a breach of immutability. Claude asks whether to re-register it beside the old one as a new source, restore it, or accept the change on your word. In a library, a changed document is the owner's ordinary maintenance, and Claude only updates the index entry, its Date included. It never re-registers silently.
- A bundle that arrived whole: adding a file with `--bundle` is refused.
- A format `doc2md.py` cannot read: the old binary formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are reported as unsupported. Resave them as `.docx`, `.pptx` or `.xlsx` first. The script needs `markitdown` installed and never installs it. Its formats and needs are on [Scripts](../reference/scripts.md).
- A binary already in git beside its extract: it leaves git only by your own act, by hand. No script does it, and a sweep never does.

## A worked example

You have a supplier's offer as a Word file and want it on record in a project called `my-project`.

```
/ingest vendor-offer.docx my-project
```

Claude finds no personal matter and stores nothing yet. It asks: convert to Markdown? You say yes, and it runs `doc2md.py`, which writes `sources/vendor-offer.md`. Claude then asks what the offer is for. You answer "a price to compare against". Claude writes the entry:

```
### `vendor-offer.md`
- **What:** a supplier's offer for a service, with prices and terms
- **Origin:** extract of `vendor-offer.docx` (markitdown)
- **Date:** 2026-03-02, from the content
- **Form:** extract of vendor-offer.docx
- **Role:** a price to compare against
- **Use for:** what the service costs and on what terms
```

The reply is two lines: the file stored with its entry, and "nothing new" for the intent.

Terms are in the [Glossary](../reference/glossary.md).

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
