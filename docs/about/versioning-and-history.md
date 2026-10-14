---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: b0bfaabfb262f7e8
inputs:
  - CLAUDE.md#Versioning & status
  - templates/history.md
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0310
  - projects/forge/10-intent.md#POS.0730
  - projects/forge/10-intent.md#POS.1510
  - projects/forge/10-intent.md#REJ.0110
---

# Versioning and history

A version number in the forge says whether a document has been
signed off, and the history of a document is a log kept in a
companion file beside it. This page explains what the numbers mean,
what a major is, where the history lives and why it is arranged so.
It is for the user who works a project, for the extender who adds
to the forge and for the evaluator who wants to know what a version
attests. The exact fields of the front-matter are in
[Versioning and front-matter](../reference/versioning-and-front-matter.md);
the exact shape of a record is in
[History companion](../reference/history-companion.md).

## What it is

The version scheme is the house scheme, aligned with the group BRD
standard: integers denote signed-off versions. A document runs
through numbers in this order:

- `0.1, 0.2, …`: drafts before the first approval
- `1.0`: approved
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves
- `2.0`: the next approved version, incorporating all changes
  since 1.0

The front-matter of a versioned document carries `version`, `date`,
`status` and `last_change`. The status is one of `draft`,
`approved` and `superseded`. The status must agree with the number:
an integer version is `approved`, and anything else is not.

A recipe (the file a render is generated from) is the one versioned
document with a scheme of its own. It carries `updated` in place of
`date`, it carries no status, and it stays 0.x for life.

A major is an integer version of an intent. The rule that says what
a major closes is stated for the intent of the forge's own project.
A major closes a set of features the principal names. The principal
is the person whose thinking is being forged, the final authority
on all content. Before its tag a major passes more than a minor: a
test whose findings are settled or deferred by the principal's
word. The word closes the major; the test says what the word
attests. Where the tag of a major is proposed is said in
[Release a version](../use/release-a-version.md).

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it, never in its body. The
rule has no exception: every [artefact](../reference/glossary.md)
(a document of the chain, such as the brief, the intent or the
assignment), every recipe and every work specification alike. The
body is the current state; the companion is the record.

## How it works

The companion is a log. One record is one change and one line.
Records are appended at the end of the file and are never
rewritten, so the order of the file is the order of the changes. A
record names its date, the version it belongs to, its author, its
subject, its kind and its reason. It may carry `Action`, what the
user must do after the change, and `Was`, the wording that ceased
to hold. `Was` is word for word the part of the wording that ceased
to hold, and it always stands last. The kinds of a record are:

- `created`: an item or a document is born; the reason is left out,
  because the wording is in the document
- `changed`: wording changed
- `closed`: a thread or an open question is settled
- `removed`: an item leaves the document, and its ID is never used
  again
- `approved`: the document as a whole is approved, such as a brief
  or a major

The subject is an ID, or several IDs where the whole line holds for
each. Where a change touches what has no ID, the record names the
place: the heading of the section, or the file name where the
change is of the document as a whole. A record of a change to the
document as a whole carries no `Was`. At the birth of a document
the log receives two records: one of the file and one naming every
item born with it.

The author of a record is the one who decided the change, by the
handle the instance (one installation of the forge) gives its
principal, never the one who typed it. The field is present from
the first record.

A round of work is one version and as many records as it made
changes. A version may hold several records, of the same item too.
The record is written in the same step as the change it records.
Before a write, Claude reflects back both the new wording of every
item touched and the record the history will receive, `Was`
included. The `last_change` of the front-matter is derived from the
records of the newest version by the write step that appends them,
never by hand.

The way to an item goes into its record, never into the item: why
it changed, what was said, the trials and measurements, which
research turned it. A thread that is settled leaves the project's
`threads.md`; its `closed` record says what was decided and where
it now stands, and carries the thread's last text word for word in
`Was`.

Before Claude proposes a change to an item, it reads the item's
history through `/history <ID>`. A script gathers what the project
holds of the item: its wording today, every record whose subject it
is, the records of other items that mention it, the rows of the
archive that mention it, and every other place in the project that
cites it. The history is searched by the script and never loaded
whole. What Claude finds is said in the proposal only where it
bears on the change, a direction once tried and dropped above all.
How the command is used is in
[Read the history of an item](../use/read-the-history-of-an-item.md).

The log is the single primary. Two things derive from it by
mechanism: the commit messages that `/save` and `/release` draft,
and the release notes. The release notes are derived at a release
from the records since the previous release, one section per
release, newest first. One thing is never derived: what the reader
must do is written with the change, in `Action`, and the release
notes carry it into *Action required* word for word. At a major the
minors since the previous major are folded into it.

The companion is part of its document. It has no row of its own in
the ledger (the project's single source of truth for state), and it
is handed over with the document by the link into git.

A companion written before the log keeps its table untouched. It
moves as it stands to `<file>.history.archive.md`, immutable from
then on, and the log begins with the next version. Nothing is
converted: the rows of the archive are a record and stay in the
words they were written in. The history of an item is a search of
both the log and the archive. A Version History table, in the body
of a document or in its companion, is a finding of `/check`; the
move settles it, on the principal's word, project by project.

## Why

Integers denote approval. The alternative, MAJOR.MINOR with the
major meaning a scope change, was rejected. A scope change is a
reason for re-approval anyway, so the integer carries the one fact a
reader needs: whether the document was signed off.

A recipe stays 0.x. It carries no status, so no version of it can
be `approved`. An integer would claim a sign-off the recipe cannot
hold.

The test of a major attests that the documents conform to the
conventions and to each other, and that the thinking has been
challenged. It attests nothing of how the model behaves on them;
behaviour is verified by the author's own use until the forge has a
test of it. The approval signs nothing over: it says what is done,
not that nothing is left. The package the major names is finished
and goes out; what is open stays open in its thread, and a position
marked for a later pass stays marked.

The history lives beside the document, not in it. The body is the
current state and the companion the record, so a reader of the body
sees what holds and nothing of how it came to hold. The way to an
item is kept in the record. Because the log is searched and never
read whole, keeping the whole way there costs nothing, the last
text of a closed thread included.

The author field is there from the first record. A log is never
rewritten, so a field it lacks cannot be added to what was written.

The log is the single primary. Commit messages and release notes
derive from it by mechanism. The reason for the release notes is
that a reader wants to see plainly what was added, changed and
removed. `Action` is written with the change by whoever made it; it
is the one thing never derived. The reason it is never derived is
not recorded in the inputs. Folding the minors into a major is the
house scheme's own reading of a major: the next approved version,
incorporating all changes since the last.

The history is read by one command. The history of an item is
scattered over the log, the archive and the records of other items,
and reading a whole log is forbidden, so the search used to be done
by hand and differently every time. What is deterministic belongs to
a script; the judgement is what remains for the model.

A pre-log history is archived rather than converted. Its rows are a
record and stay in the words they were written in. The reason the
move waits for the principal's word, project by project, is not
recorded in the inputs.

## A worked example

A project `example-project` holds an assignment `20-assignment.md`.
Its companion `20-assignment.history.md` opens with the two records
of its birth and grows one line per change. After one draft round
and an approval, a later round changed one requirement and the user
had something to do afterwards. The log then reads:

```
- 2026-01-10 | 0.1 | <handle> | 20-assignment.md | created
- 2026-01-10 | 0.1 | <handle> | REQ.0010, REQ.0020, REQ.0100 | created
- 2026-01-24 | 1.0 | <handle> | 20-assignment.md | approved
- 2026-02-03 | 1.1 | <handle> | REQ.0100 | changed | the recipients asked for a monthly report instead of a weekly one | Action: tell the recipients the first report is due at the end of the month | Was: The team shall report progress weekly.
```

The first two lines are the birth: one record of the file and one
naming every item born with it, both without a reason. The third is
the approval of the document as a whole, which turned 0.1 into 1.0.
The fourth is a change after approval, so the version is 1.1 and
the status of the document is no longer `approved`. The record
names the item, gives the reason, says what the user must do in
`Action` and keeps the wording that ceased to hold in `Was`, last.
The front-matter's `last_change` is derived from this newest record
by the write that appended it. At the next release the `Action`
line goes into the release notes word for word, and the commit
message of the save is drafted from the records.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
