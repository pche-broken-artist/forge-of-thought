---
description: Register external documents (transcripts, offers, specs, standards) in sources/ — store, catalogue, nothing more
argument-hint: "[file-or-path] [project-slug]"
disable-model-invocation: true
---

Ingest external input into the project (slug from the second argument or
context; if ambiguous, ask).

**With a file argument:** register that document.
**Without arguments:** sweep mode — scan `sources/` for files not yet
recorded in the ledger and register them all; and report files
changed since registration (modification time later than the
ledger's registration date) with a question — what to do with each.
The meaning depends on the project's kind (POS.0180, POS.0960): in a
`thought` project a changed source is a breach of immutability to
resolve (re-register beside as a new source, or restore); in a
`library` a changed document is the owner's ordinary maintenance
(POS.0970) — update the index entry and the ledger date, nothing
else. Never silently re-register.

1. **Store.** Copy the document into `sources/` as `<short-slug>.<ext>` —
   a short descriptive slug derived from the content or original name
   (e.g. `steerco-transcript.pdf`, `vendor-offer.docx`). No dates in
   filenames. On a name collision, suffix `-2`. Never rename or modify a
   file already recorded in the ledger: sources are immutable from the
   moment of registration.
   **Bundles:** a set of related files (a downloaded site with its
   index, a document with attachments) lives as a subdirectory
   `sources/<slug>/` and is treated as ONE source: one ledger row,
   immutable as a whole from registration. In sweep mode, register a
   subdirectory as one bundle, never file by file. Provenance in the
   intent still cites individual files by path
   (`sources/<slug>/<file>`). A file may later be split out to its own
   ledger row if it needs separate tracking.
   **Bundle index:** every bundle carries `00-INDEX.md`, shaped by
   `templates/index-bundle.md` (the one owner of the bundle index —
   header and opening paragraph its own, the entry carried verbatim
   from `templates/index.md`; POS.1070). If the bundle arrives without one, create it from the
   skeleton at registration; if one is supplied, validate it against
   the actual contents and report gaps. Per-file origin and dates are
   best effort, never asked for.
2. **Date, best effort, never a question.** Record the document's origin
   date in the ledger if it can be determined for free: from the content
   (meeting date in a transcript header, offer date), else from file
   metadata, else the ingest date. Note the origin as
   `content | file | ingested`. Do not ask the principal for dates.
3. **One form per source (POS.1040).** For every binary file (PDF,
   DOCX, PPTX, XLSX, …) — isolated or inside a bundle — ask one
   question, per file: convert to Markdown?
   - **Yes:** run `scripts/doc2md.ps1 <file> -OutDir sources/` (or the
     bundle directory); the extract `<short-slug>.md` is the source —
     registered, indexed (Origin: "extract of `<original>` (markitdown)"),
     immutable. The original is not copied into the project; if it
     already lies in `sources/` (sweep mode), add its path to
     `sources/.gitignore` and leave it there, local only.
   - **No:** the binary is the source as a functional thing (a deck
     template, a graphic, a logo): store, register and index it as is,
     no extract.
   Text files get no question. Keeping both is the exception, on the
   principal's explicit word. Never parse binaries by hand or with
   ad-hoc code (e.g. Python PDF libraries): the script is the only
   conversion path. Extracts made before this rule keep their
   `.extract.md` names; a binary already in git beside its extract
   leaves the index only on the principal's word, never in a sweep.
4. **Index entry.** Add the source to `sources/00-INDEX.md` (skeleton
   `templates/index.md`; create the index from it if missing):
   **What** (one or two sentences, read enough of the file to say it
   truthfully), **Origin** (author, URL, meeting — best effort),
   **Role** and **Use for**. Role is free text — a standard to verify
   against, inspiration, a counter-example, a meeting record, material
   to absorb — taken from the principal in a sentence when he offers
   one; otherwise write what the file itself declares, or `—`. Do not
   ask a mandatory question; a light "what is it for?" is fine when the
   conversation invites it. A bundle is one entry pointing to its
   inner `00-INDEX.md`; never repeat the bundle's contents in the top
   index. The index tracks nothing — no processing state.
5. **A library document is cited, not copied.** When the principal
   points a project at a document that lives in a library
   (`projects/lib-<name>/…`), nothing is stored in `sources/`: add an
   index entry that names the path and says what it is for, and a
   row in the ledger's Dependencies table (path, library, used by,
   note — POS.1020). Moving a document out of a project into a
   library is the reverse: ingest it there, replace the project's
   entry with the citation, register the dependency.
6. **Nothing is processed.** `/ingest` never carries content into the
   intent or any other document. Registration does not imply intake:
   the principal alone directs how and when a source is used — in
   `/forge intent`, while drafting, in ordinary conversation ("check the
   brief against the NFRs in file X"). When source content does enter
   the intent, it is the principal's explicit act and is cited with
   provenance to the file (`sources/<file>` or `sources/<slug>/<file>`);
   what someone said in a meeting is never silently promoted to the
   principal's own position.
7. **Bookkeeping and summary.** Update the Sources table in `ledger.md`
   — registration only: file, date, date origin, form (`text` |
   `extract of <original>` | `binary`);
   what the source is and is for lives in the index alone. In sweep
   mode, also fill index gaps for files already registered. Finish
   with a short summary:
   what was stored or registered, with
   what role — and no next step implied; the sources wait for the
   principal.
