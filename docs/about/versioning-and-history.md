---
generated: 2026-10-10
made: derived
inputs-hash: 3e7693b6571033dd
inputs:
  - CLAUDE.md
  - templates/history.md
  - projects/forge/10-intent.md
---

# About versioning and history

This page explains how a versioned document of the forge is numbered,
what its status means, what approving a major of an intent does and
does not do, and why every versioned document keeps its history in a
companion file beside it rather than in its own body. It is for the
user who writes with the forge, the extender who adds to it and the
evaluator who wants to know what a version number and a history
record can be trusted to say. It was put together from `CLAUDE.md`
(Versioning & status), `templates/history.md` and the forge's own
intent, and pairs each rule with the reason the inputs give for it.

## The version scheme

The scheme is the house scheme, aligned with the group BRD standard:
integers denote signed-off versions.

- `0.1, 0.2, ...` are drafts before the first approval.
- `1.0` is approved.
- `1.1, 1.2, ...` are changes made after approval, not yet approved
  themselves.
- `2.0` is the next approved version, incorporating all changes
  since `1.0`.

The front-matter of a versioned document carries `version`, `date`,
`status` (`draft | approved | superseded`) and `last_change`. Status
must agree with the number: an integer version is `approved`,
anything else is not. `last_change` is derived from the records of
the newest version by the write step that appends them, never by
hand.

A recipe is the one versioned kind that behaves differently. It
carries `updated` in place of `date`, has no status, and stays `0.x`
for life: a recipe is a tool that is iterated, never approved, so it
never reaches an integer.

Why integers mean approval and nothing else: a scheme where the
major number meant a change of scope was considered and dropped. A
scope change is a reason for re-approval anyway, so the number need
only say whether the document was signed off, and the group
convention already says that.

## What a major of an intent is

An intent is versioned like every artefact: a draft until the
principal approves it, then an integer. Approving a major is more
than bumping the number, and the inputs say precisely what it does.

A major closes a package the principal names. His word closes it;
what the word attests is said by a test the major passes before its
tag. The major approves the intent as the record of what the
principal holds at that date: the package it names is finished and
goes out.

A major signs nothing over. It says what is done, not that nothing is
left. What is open stays open in its thread, and a position marked
for a later pass stays marked. Approval is a statement about the
record, not a promise that the thinking is complete.

The test a major passes attests two things: that the documents
conform to the conventions and to each other, and that the thinking
has been challenged. It attests nothing of how the model behaves on
those documents. Until the forge has a test of behaviour, behaviour
is verified by the author's own use. Where the tag of a major is
proposed and what the release does around it is the release's own
page.

## The history companion

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it, never in its body. The body
is the current state; the companion is the record. This holds for
every artefact and every recipe alike, with no exception: brief,
intent, assignment, every later layer, and the recipe.

The history is a log. One record is one change and one line,
appended at the end of the file and never rewritten, so the order of
the file is the order of the changes. A round of work is one version
and as many records as it made changes; a version may hold several
records, of the same item too. The shape of a record is owned by
`templates/history.md`: date, version, author, subject, kind, reason,
then `Action` and `Was` where the record has them. The kinds are
`created`, `changed`, `closed` (a thread or an open question
settled), `removed` (an item leaves the document and its ID is never
used again) and `approved` (of the document as a whole: the approval
of a brief or of a major). A record of creation needs no reason: the
wording is in the document.

The subject of a record is an ID, several IDs where the whole line
holds for each, or a place without an ID: the heading of a section,
or the file name where the change is of the document as a whole. At
the birth of a document the log opens with one record of the file and
one naming every item born with it.

Two fields deserve a word of their own.

- `Action` is what the user must do after the change. It is written
  with the change, by whoever made it, because it is the one thing
  that is never derived later: the release notes carry it into their
  *Action required* word for word.
- `Was` is, word for word, the part of the wording that ceased to
  hold. It is written wherever wording leaves an item or a place; a
  record of a change to the document as a whole carries none. It
  always stands last in the line.

The author of a record is the one who decided the change, by the
handle the instance gives its principal, never the one who typed it.
The field is there from the first record, because a log is never
rewritten and a field it lacks cannot be added to what was already
written.

### Why the history lives beside the document, not in it

The inputs give three reasons.

The way to an item does not belong in the item. Why it changed, what
was said, trials, measurements, which research turned it: all of that
goes into the record, never into the item. The item says what is to
be achieved and why; the record says how it came to say so. The
record is written in the same step as the change it records, and the
reflection before a write shows both the new wording of every item
touched and the record the history will receive, `Was` included.

The log is the single primary. The commit messages that a save and a
release draft, and the release notes, are derivations from the
records. A release's notes are derived from the records of the log
since the previous release; at a major the minors since the previous
major are folded into it, which is the scheme's own reading of a
major as the next approved version incorporating all changes since.
Keeping one primary means the derivations can be regenerated and
never disagree with the record.

A history is searched, never loaded whole. Before Claude proposes a
change to an item, he searches the history and its archive for the
item's ID and says what he found only where it bears on the change,
a direction once tried and dropped above all. A companion that grows
by one line per change stays searchable where a body full of
narrative would not.

### The companion is part of its document

The companion has no row of its own in the ledger; it is handed over
with its document by the link into git.

### The archive

A companion written before the log had this shape is kept exactly as
it stands. It moves, untouched, to `<file>.history.archive.md`,
immutable from then on, and the log begins with the next version.
Nothing is converted: its rows are a record and stay in the words
they were written in. The history of an item is then a search of
both files. A Version History table found in the body of a document
or in its companion is a finding of a check, settled by that move on
the principal's word, project by project.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
