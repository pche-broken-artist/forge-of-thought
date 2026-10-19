---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: e849f920ee20b8c5
inputs:
  - .claude/skills/ingest/SKILL.md
  - scripts/doc2md.py
  - templates/index.md
  - templates/index-bundle.md
---

# Register a source

This page shows how you store, register and catalogue external input
(a transcript, an offer, a standard, a pasted text) in a project with
`/ingest`. It is for the principal, the person whose thinking the
project forges, who hands such material to Claude.

## When to use it

Use it whenever material from outside enters the project: a document
you were given, text you paste into the conversation, or files that
already lie in `sources/` and are not yet catalogued. Registration
only stores and describes the material. It does not carry anything
into your intent, because the principal alone decides how and when a
source is used (see [Sources and research](../about/sources-and-research.md)).

## The command

```
/ingest [file] [slug]
```

One line that can be typed as it stands:

```
/ingest vendor-offer.docx my-project
```

The three forms:

- With a file, that document is registered.
- With text pasted into the conversation, the text is the source.
  Claude stores it as `sources/<slug>.md`, proposing the slug from the
  content, with a two-line header (origin: pasted into the
  conversation; date).
- Bare, `/ingest` sweeps `sources/` for files that are not yet in the
  index and registers them all. It also reports files changed since
  registration, with a question for each: what to do with it.

The slug argument names the project. When it is missing and the
context does not say, Claude asks.

## What happens

1. **Personal matter stops the command.** If the text carries a named
   private person, an identifying detail, health or anything of the
   kind, Claude stops before storing and asks: store as it is, redact
   before registration, or drop. A registered source is immutable, so
   redaction can only happen before.
   You should now see a question, and nothing in `sources/` yet.
2. **The file is stored.** Claude copies it into `sources/` as
   `<short-slug>.<ext>`, a short descriptive name without a date; on a
   name collision it adds the suffix `-2`. A set of related files is
   stored as one folder, `sources/<slug>/`, and counts as one source
   with its own index.
   You should now see the file, or the folder, under `sources/`.
3. **Every binary gets one question: convert to Markdown?** This
   applies to each PDF, Word, PowerPoint or Excel file, alone or inside
   a set.
   - Yes: Claude runs `python scripts/doc2md.py <file> -o sources/`.
     The extract `<short-slug>.md` is then the source, and the original
     is not copied into the project. An original that already lies in
     `sources/` stays there, local only, and is added to
     `sources/.gitignore`.
   - No: the binary itself is the source, as a functional thing such as
     a deck template, a graphic or a logo. It is registered as it is,
     with no extract.

   Text files get no question. Keeping both the binary and its extract
   happens only on your explicit word.
   You should now see either `<short-slug>.md` or the binary, one form
   per source.
4. **Claude asks what the source is for.** The question is "what is it
   for?", one per source and one for the whole of a set. Your answer is
   the source's Role. You may instead tell Claude to infer it: then it
   writes what the file itself declares and marks it `(inferred)`. It
   never infers unasked, and it writes nothing about the source before
   you answer.
   You should now see that the question was asked before any entry
   exists.
5. **The index entry is written.** Claude adds the source to
   `sources/00-INDEX.md` (creating the index if it is missing) after
   reading enough of the file to say truthfully what it is. The entry
   has these fields:
   - **What:** what the resource is, in one or two sentences.
   - **Origin:** where it came from (an author, a meeting, a URL).
   - **Date:** the source's own date, best effort and never asked. It
     is taken from the content if possible, else from the file, else
     it is the day of the ingest, and the field says which.
   - **Form:** text, extract of the original, or binary.
   - **Role:** your answer from step 4.
   - **Use for:** what to reach for the source for.

   A set of related files carries its own `00-INDEX.md` inside its
   folder, made from the bundle skeleton: a short paragraph on what the
   whole is and why it entered, then one entry per file in the same
   fields. If the set arrives with an index, Claude checks it against
   the actual contents and reports gaps. In the main index the set is
   one entry that points to the inner index.
   You should now see the entry in `sources/00-INDEX.md`.
6. **A library document is cited, not copied.** If you point the
   project at a document that lives in a library, Claude stores
   nothing in `sources/`. It adds an index entry that names the path
   and says what the document is for. The project's ledger (its record
   of state) finds that citation by itself. Citing a library's
   document is described in
   [Share material through a library](share-material-through-a-library.md).
   You should now see an entry with a path and no new file.
7. **Claude remakes the ledger and replies.** The reply is two lines at
   most: the file stored with its index entry, and what the source adds
   to the intent in one line, or "nothing new". Claude gives no
   analysis of the content and implies no next step.
   You should now see the two lines, and the source waits for you.

## What you have afterwards

- The material in `sources/` as one file per source, in one form: text,
  extract or binary.
- An entry in `sources/00-INDEX.md` with its What, Origin, Date, Form,
  Role and Use for.
- Nothing carried into the intent or any other document.

## If something goes wrong

Messages of `scripts/doc2md.py`, as it prints them (the script is
described in [Scripts](../reference/scripts.md)):

- `ERROR: markitdown not found.` The conversion engine is not
  installed. Install it with
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"` and reopen the
  shell, or give its location with `--markitdown-path`. The script
  never installs anything itself.
- `WARNING: markitdown cannot read legacy format ...`. The legacy
  formats `.doc`, `.ppt`, `.rtf`, `.odt`, `.odp` and `.ods` are not
  converted. Resave the file as `.docx`, `.pptx` or `.xlsx` first.
- `WARNING: Unsupported extension ...`. The file type is not handled.
- `SKIP ... -> already exists (use --force)`. An extract of that name
  is already there, and the script does not overwrite it.
- `FAIL ... -> markitdown exited with code ...` or `markitdown
  produced no output file.` The conversion did not produce an extract.
  The final line `Done: N converted, M skipped, K failed.` counts them.

When a sweep reports a changed source, the meaning depends on the
project. In a thought project a changed source breaks immutability:
you choose between registering the new content beside it as a new
source, restoring the old, or accepting the change knowingly on your
word. In a library a changed document is the owner's ordinary
maintenance, and only the index entry is updated, its Date included.
Claude never re-registers silently.

## A worked example

You paste an excerpt of a supplier's offer into the conversation, in a
project called `my-project`:

```
/ingest my-project
```

Claude finds no personal matter and proposes the slug `supplier-offer`.
It stores the text as `sources/supplier-offer.md` with the two-line
header, then asks: "What is it for?" You answer: "A counter-example
for the pricing section." Claude writes the entry:

```
### `supplier-offer.md`
- **What:** An excerpt of a supplier's offer with three price tiers.
- **Origin:** pasted into the conversation
- **Date:** 2026-10-19, from the ingest
- **Form:** text
- **Role:** a counter-example for the pricing section
- **Use for:** how a competing offer words its tiers
```

The reply is two lines: the file `sources/supplier-offer.md` stored
and indexed, and "nothing new" for the intent.

## See also

- [Sources and research](../about/sources-and-research.md): why sources are immutable and why registration is not intake.
- [Share material through a library](share-material-through-a-library.md): citing a library's document.
- [Scripts](../reference/scripts.md): `doc2md.py`, its formats and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
