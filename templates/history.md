---
project: <slug>
document: <file>          # the versioned document this companion belongs to
---

# Version History — <file>

<!-- Append-only companion of a versioned document (CLAUDE.md, Document
kinds and Versioning & status): brief, intent, assignment, later
artefacts and recipes alike. One row per version bump, newest first,
human-readable — what changed and why. Appended by the write step that
bumps the document's version, which also rewrites last_change: in the
document's front-matter from the newest row; never edited by hand, rows
never rewritten. Not a ledger row: the companion is part of its
document.
For the intent, the assignment and every later layer (not the brief,
not a recipe) the row closes with a Notes block after the prose:
`<br>**Notes:**` and then one line per change that reaches the reader
of the release notes, `<br><Group> — <one sentence> (<pointer>).`,
groups in this order — Action required, Added, Changed, Removed,
Fixed, Rejected — a group repeated for every line of it, empty groups
absent; a row with nothing for the reader carries
`<br>**Notes:** nothing for the reader.` Each line has two sides in
this order: what changed — the fact, its position or decision as the
pointer in parentheses — then `For you:` and what it means for the
reader: what they can now do, must do or can no longer do. Neither
side alone is a line. The release notes are compiled from these lines
(POS.0730), never classified afterwards. -->

| Version | Modification | Author | Date |
|---|---|---|---|
| 0.2 | <what changed and why>.<br>**Notes:**<br>Action required — <what changed> (<pointer>). For you: <what to do after this change>.<br>Added — <what changed> (<pointer>). For you: <what it means>.<br>Changed — <what changed> (<pointer>). For you: <what it means>. | <author> | YYYY-MM-DD |
| 0.1 | Initial draft.<br>**Notes:** nothing for the reader. | <author> | YYYY-MM-DD |
