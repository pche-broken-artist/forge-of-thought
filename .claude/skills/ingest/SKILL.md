---
description: Register external input (a file, or text pasted into the conversation) in sources/ — store, ask what it is for, catalogue, nothing more
argument-hint: "[file-or-path] [project-slug] [--bundle name]"
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
in the index and register them all; and report files changed since
registration (modification time later than the Date of the index
entry) with a question — what to do with each.
The meaning depends on the project's kind (POS.0180, POS.0960): in a
`thought` project a changed source is a breach of immutability to
resolve (re-register beside as a new source, restore, or accept the
change knowingly on the principal's word); in a
`library` a changed document is the owner's ordinary maintenance
(POS.0970) — update the index entry, its Date included, nothing
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
   file already in the index: sources are immutable from the
   moment of registration (CLAUDE.md, Versioning & status).
   **Bundles** (CLAUDE.md, Document chain, External inputs): store a set of related
   files as `sources/<slug>/`, one index entry; in sweep mode, register
   a subdirectory as one bundle, never file by file. Create its
   `00-INDEX.md` from `templates/index-bundle.md` if the bundle
   arrives without one; validate a supplied one against the actual
   contents and report gaps. A file may later be split out to its own
   entry if it needs separate tracking.
   **Growing bundles** (`--bundle <name>`): a bundle of one origin
   that keeps arriving. `sources/<name>/` missing: it is born as
   growing, its `00-INDEX.md` from `templates/index-bundle.md` with
   the opening paragraph saying it grows, the file inside. Existing
   and growing: store the file inside it, never beside it, its own
   entry in the bundle's index, the top entry's What kept true.
   Existing and arrived whole: refuse and say why. In sweep mode a
   file inside a bundle without an entry in the bundle's index is
   offered for registration there, never reported as a changed
   source, and a new subdirectory is asked whether it grows at the
   question of its role.
2. **Date, best effort, never a question** (CLAUDE.md, Document
   chain, External inputs). The document's origin date goes into the
   `Date` field of its index entry if it can be determined for free:
   from the content (meeting date in a transcript header, offer
   date), else from file metadata, else the ingest date; the field
   says which, in the words `templates/index.md` gives it. Do not
   ask the principal for dates.
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
4. **Role, before anything is written.** Role is the principal's
   word, asked before the index entry exists, so
   that the entry carries it from its birth and no later hand
   changes it (POS.1040). One question,
   "what is it for?", per source — a bundle one question for the
   whole, a file added to a growing bundle one of its own — one per
   message, as the elicitation interview has it; in
   sweep mode source by source. The principal answers with the role,
   or tells Claude to infer it — then Claude writes what the file
   itself declares, marked *(inferred)*. Never inferred unasked, and
   nothing of the source written before he answers.
5. **Index entry.** Add the source to `sources/00-INDEX.md` as an
   entry in the shape of `templates/index.md` (create the index from
   it if missing), having read enough of the file to say truthfully
   what it is, the Role as answered, the Date of step 2 and the Form
   of step 3 (POS.1610: the entry is the one home of a source's
   registration; the ledger's Sources table reads it).
6. **Another project's document is cited, not copied.** When the
   principal points a project at a document that lives in another
   project, a library's (`projects/lib-<name>/…`) or any other's
   (`projects/<slug>/…`, POS.1020), nothing is stored in `sources/`: add an
   index entry that names the path and says what it is for; the
   ledger's Dependencies table finds the citation by itself
   (POS.1020, SOL.0680). Moving a document out of a project into a
   library is the reverse: ingest it there, replace the project's
   entry with the citation.
7. **Nothing is processed.** `/ingest` never carries content into the
   intent or any other document; the rule — registration is not
   intake, the principal directs every use, provenance cites the
   file — is CLAUDE.md, Document chain, External inputs.
8. **Bookkeeping and summary.** Remake the ledger from the records,
   `python scripts/forge-ledger.py <slug>`; what the source is and is for lives
   in the index alone. In sweep
   mode, also fill index gaps for files already registered. The
   reply after registration is two lines at most: the file stored
   and its index entry; what the source adds to the intent, in one
   line, or "nothing new". No analysis of the source's content and no
   next step implied; the sources wait for the principal.
