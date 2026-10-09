---
description: Register external input (a file, or text pasted into the conversation) in sources/ — store, catalogue, ask what it is for, nothing more
argument-hint: "[file-or-path] [project-slug]"
disable-model-invocation: true
---

Ingest external input into the project (slug from the second argument or
context; if ambiguous, ask).

**With a file argument:** register that document.
**With text pasted into the conversation:** the text is the source —
store it as `sources/<slug>.md`, the slug proposed from its content,
with a two-line header (origin: pasted into the conversation; date),
and register it like any file.
**Without arguments:** sweep mode — scan `sources/` for files not yet
recorded in the ledger and register them all; and report files
changed since registration (modification time later than the
ledger's registration date) with a question — what to do with each.
The meaning depends on the project's kind (POS.0180, POS.0960): in a
`thought` project a changed source is a breach of immutability to
resolve (re-register beside as a new source, restore, or accept the
change knowingly on the principal's word); in a
`library` a changed document is the owner's ordinary maintenance
(POS.0970) — update the index entry and the ledger date, nothing
else. Never silently re-register.

0. **Personal matter stops the command.** Before storing, if the text
   carries personal matter — a named private person, an identifying
   detail, health, anything of the kind — stop and ask: store as it
   is, redact before registration, or drop. Never stored first and
   asked afterwards; a registered source is immutable, so redaction
   happens before registration. Unconditional: no rule in the project
   needs to declare it.
1. **Store.** Copy the document into `sources/` as `<short-slug>.<ext>` —
   a short descriptive slug derived from the content or original name
   (e.g. `steerco-transcript.pdf`, `vendor-offer.docx`). No dates in
   filenames. On a name collision, suffix `-2`. Never rename or modify a
   file already recorded in the ledger: sources are immutable from the
   moment of registration (CLAUDE.md, Versioning & status).
   **Bundles** (CLAUDE.md, Document chain, External inputs): store a set of related
   files as `sources/<slug>/`, one ledger row; in sweep mode, register
   a subdirectory as one bundle, never file by file. Create its
   `00-INDEX.md` from `templates/index-bundle.md` if the bundle
   arrives without one; validate a supplied one against the actual
   contents and report gaps. A file may later be split out to its own
   ledger row if it needs separate tracking.
2. **Date, best effort, never a question** (CLAUDE.md, Document
   chain, External inputs). Record the document's origin
   date in the ledger if it can be determined for free: from the content
   (meeting date in a transcript header, offer date), else from file
   metadata, else the ingest date. Note the origin in the words
   `templates/ledger.md` gives the Sources table. Do not ask the
   principal for dates.
3. **One form per source (POS.1040).** For every binary file (PDF,
   DOCX, PPTX, XLSX, …) — isolated or inside a bundle — ask one
   question, per file: convert to Markdown?
   - **Yes:** run `python scripts/doc2md.py <file> -o sources/` (or the
     bundle directory); the extract `<short-slug>.md` is the source —
     registered, indexed (Origin: "extract of `<original>` (markitdown)"),
     immutable. The original is not copied into the project; if it
     already lies in `sources/` (sweep mode), add its path to
     `sources/.gitignore` and leave it there, local only.
   - **No:** the binary is the source as a functional thing (a deck
     template, a graphic, a logo): store, register and index it as is,
     no extract.
   Text files get no question. Keeping both is the exception, on the
   principal's explicit word. The script is the only conversion path
   (CLAUDE.md, Document chain, External inputs). Extracts made before this rule keep their
   `.extract.md` names; a binary already in git beside its extract
   is taken out of git only by the principal's own act there, by
   hand: no script of the forge does it, and never a sweep.
4. **Index entry.** Add the source to `sources/00-INDEX.md` as an
   entry in the shape of `templates/index.md` (create the index from
   it if missing), having read enough of the file to say truthfully
   what it is. Role is the principal's word: after registration
   Claude always asks "what is it for?"; the principal answers with
   the role, or tells Claude to infer it — then Claude writes what the
   file itself declares, marked *(inferred)*. Never inferred unasked;
   `—` until he answers.
5. **A library document is cited, not copied.** When the principal
   points a project at a document that lives in a library
   (`projects/lib-<name>/…`), nothing is stored in `sources/`: add an
   index entry that names the path and says what it is for, and a
   row in the ledger's Dependencies table as `templates/ledger.md`
   has it (POS.1020). Moving a document out of a project into a
   library is the reverse: ingest it there, replace the project's
   entry with the citation, register the dependency.
6. **Nothing is processed.** `/ingest` never carries content into the
   intent or any other document; the rule — registration is not
   intake, the principal directs every use, provenance cites the
   file — is CLAUDE.md, Document chain, External inputs.
7. **Bookkeeping and summary.** Update the Sources table in
   `ledger.md`, a row as `templates/ledger.md` has the table;
   what the source is and is for lives in the index alone. In sweep
   mode, also fill index gaps for files already registered. The
   reply after registration is three lines at most: the file stored
   and its index entry; what the source adds to the intent, in one
   line, or "nothing new"; the question "what is it for?" (step 4).
   No analysis of the source's content and no next step implied; the
   sources wait for the principal.
