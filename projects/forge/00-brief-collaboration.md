---
project: forge
title: Work of several people, branches and windows on one project
date: 2026-10-17
author: PCHe
version: 0.8
status: draft
last_change: 0.8 (2026-10-17): the sixth critique worked in (sources/merge-brief-critique-6.md): a worktree addressed as <slug>@<branch>, the write step never fetching, the manual rebase steps corrected, IDs four-digit until 9999 with a numeric sort, the order of releases against the steps of one run, the engine's second root; two windows on two projects need no worktree, only /save with a slug.
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What prompted it

The biggest project problem of Forge of Thought is the ledger: the
one file every operation writes. As soon as two people work on the
same project, the merge goes badly; the same when one person works
on two branches, or in two windows at once, one matter in each. A
position written into the intent merges easily, but it also writes
the history and the ledger, and there the pain begins; a research
made from another account collides in several files instead of
being pulled. Work of several people on one project is not the
typical use, but it is to be made possible step by step, so that it
stops being a pain. IDs are a further problem of their own; they
are taken in a later step.

The evidence: both merges of the project agentic-platform
(2026-10-14 and the recipient review of intent 1.2) had the ledger
as the one file present in both, beside it the history logs, the
decisions, the index of sources, and the regenerated README and
RELEASE-NOTES.

## Principle

The forge still never merges, pulls or rebases on its own judgement
(POS.1490, POS.1110 hold). One thing changes: every file of a
project gets one of four ways of merging, and the forge tells git
which one. Derived state (the ledger) is not kept in git at all but
made at read time; derived documents for a reader (renders, the
documentation, a render of the state) are in git, made only on
main. What is a record is merged as a set of records. What is
composed text is merged by git block by block, and a person settles
only the same item changed twice. Immutability is a process rule, as
it is for reviews and research today: git knows no attribute for
it, the driver raises an alarm at a merge that breaches it, and
nothing is locked.

| Way | Files | At a merge |
|---|---|---|
| 1 composed text | artefacts, recipes, work specifications, threads (C1), the project file (B0), the engine's prose | git's text merge; the one legitimate conflict is the same item or sentence changed on both sides |
| 2 set of records | `*.history.md`, `decisions.md`, `**/00-INDEX.md`, `docs-map.md`, the ID reservation file `ids.md` (F2) | the forge driver `forge-records`: union of records by key; a line or a block, immutable or mutable, by path |
| 3 derived | state: `ledger.md`, never in git, made at read time; documents: renders, README, RELEASE-NOTES, CONTRIBUTING, `docs/`, `renders/state.md`, `published/`, in git, made only on main, `ours` at a merge and made again | never merged |
| 4 immutable, unique | reviews, challenges, research, sources, closed threads | never conflicts; the name unique across branches too; immutability a process rule |

## Mechanism

**A. A header without fields that change at every operation.**
`date` and `last_change` leave the header of the artefacts and the
specifications, `updated` and `last_change` the recipes (which carry
`updated` in place of `date`), `updated` the indexes, `generated`
and `previous` the map (the documentation run
takes the previous map from git through a script, `git show`, for
its keep, new and remove). All of it is derived from the history or
from the run, and the scripts (the map, `/ledger`, forge-history,
the README recipe) compute it. What stays in a header is what does
not change with the work: `project`, a brief's `title` and `author`,
an index's `directory`, and `version` and `status`, which change only
on main (F1); nothing that changes with a round enters a header, so
that no field ever asks for a write on a branch. Value: it removes
the certain conflict of every pair of rounds in every artefact,
whatever the rounds were about.

**A2. Prose one sentence per line instead of 72 columns.** For the
artefacts, the threads, the decisions, the skills, the agents, the
templates and CLAUDE.md; tables, headers and records stay as they
are. Pandoc and GitHub treat a soft line break as a space, the
render does not change. Value: a changed word changes one line
instead of the rest of the paragraph, diff and blame work by
sentence, and above all: the items of the intent are not separated
by a blank line today, so the reflow of the end of one position
reaches the lines of the neighbouring position, and two branches
editing two neighbouring positions make a false conflict. The
cheaper partial remedy is a blank line between items; one sentence
per line settles the same and the diffs with it. The 72-column rule
was made for legible diffs; one sentence per line serves that
purpose better. Two conditions: the conversion script guards the
traps of Markdown (a sentence beginning with a number and a full
stop or `1)` would become a list, with `-`, `*`, `+`, `>`, `|` or
`#` an item, a quote, a table row or a heading; continuation lines
of a list item keep their indentation; tables, code and front-matter
are skipped) and proves its result by comparing pandoc's syntax tree
(`-t json`) of every file before and after, a soft break read as a
space, since the HTML would differ in whitespace even when the
conversion is right; and `/check` carries a light rule "a line does
not carry two sentences" (approximate, abbreviations and IDs such as
`POS.0590.` tolerated), because without a check the reflow returns
at the first larger round. Decided 2026-10-17: in the first release,
before C1, so that the threads are cut already in sentences.

**B0. The project file.** `kind` and `language` live today only in
the ledger's header, and a library's repository is at its creation
the ledger alone; after B they would have no home. A small file in
git, `project.md` (decided 2026-10-17), header `project`, `kind`,
`language`, written once at the creation, way 1; read by
forge-clone, `/import-project`, `/new-project`, `/forge`, `/recipe`
and prime directive 6 in place of the ledger's header. Without it B
cannot be done.

**B. The ledger made at read time, outside git.** A script,
`scripts/forge-ledger.py <slug>`, builds the ledger from the
documents; `ledger.md` goes into the project's `.gitignore`; the
map, `/ledger`, `/end` and the checks call the script. What only the
ledger knows today gets a home where it belongs, and every home is a
record, never a header field, so that a branch can write it; a
record stands in the history of the document that changed, as the
forge's rule has it:

- Mined and its note: a record in the intent's history, since the
  mining changes the intent and not the brief, with the brief's file
  as its subject, `00-brief-<name>.md | changed | mined: partial,
  <note>`; the script reads the last such record, and its version
  column says which version of the intent mined the brief, today's
  "mined into intent 4.32"; the note cites a REJ where there is one.
- A source's date, origin and form (`extract of <original>`; text
  or binary follows from the extension): fields of its entry in the
  sources index; the library a project relies on: found by the
  script as citations of `projects/lib-*/` anywhere in the project,
  no field.
- The provenance of a published file: a companion
  `published/<recipe>.md`, the state current or stale computed by
  the script.
- The state and the resolution of a finding or a challenge: a
  record of kind `closed` with the finding or the challenge as its
  subject (`FND.NNNN | closed | <what fixed it>`), in the history of
  the artefact whose version settled it; where no version settled it
  (a corrected index, a renamed file) and for a check of the engine,
  in the history of the project's intent, the subject still the
  finding, since the script keys on it, and what was fixed (the
  operating layer, the index, the file) named in the reason; for a
  finding it reads resolved, for a challenge accepted; `rejected`,
  `parked` and `obsolete` from a DEC, since all three are the
  principal's verdict; severity, category and headline from the
  report. No new kind of record for it.
- A work product's state: records in the specification's history,
  the making's record for Made and Inputs, a `changed` record
  `state: by hand` on the principal's word; no field.
- Waiting on principal, an explicit rule in place of today's
  hand-curated list, which differs from any rule in both directions:
  the open threads; the TBCs whose owner is the principal; the open
  findings of a critic and the open challenges, which wait for his
  verdict; not the open findings of a check, which Claude mends in a
  walkthrough; the parked findings and challenges under a heading of
  their own with the note of their DEC, since the script cannot
  judge whether the event a parking waits for has come; a decision
  with an unfinished action becomes a thread. Free text without an
  ID has no place there. A thread's line is made by a written
  convention: its first sentence is its headline, its last dated
  paragraph its state, the script shows both.
- From before the migration, `ledger.archive.md` (M): the source of
  records for every item that has no record of the new shape; a
  newer record overrides it.

State records and the version: a record of state only (mined,
`state: by hand`, `FND | closed`, `THR | closed`) carries the
current version and does not raise it, so a round on main that only
closes findings after a check and changes no content is not a
version; a landing (F1) always raises, state records or not, and the
release-notes recipe tolerates a version without content changes,
the simpler of the two rules; `+N` in a provenance counts state
records too, so a state record marks a render stale, as every raise
does today.

The script also reports: two items with one ID and two versions with
one number (until F2; and for ever the unsupported case of two
clones on main landing the same version, which this path reports and
no other); an item with `+` records of two authors in one landing,
"merged unseen, review", because with A2 git merges two sentences of
one position silently; a closed thread touched by any commit later
than the commit that closed it (the first commit whose header says
closed; the scripts are the one door to git, so this check is the
script's); an artefact with unlanded records (F1). On a branch the
script states a version as `v5.12+N`, N the unlanded records, and
every provenance written on a branch (a render's inputs, a
research's or a critique's derived_from) cites it so, the script
recomputing after the landing; a path cited alone, as a check cites
it, is not affected. All 26 skills that write a ledger row today
stop. `/check light` no longer compares anything with the ledger; it
reports what the script finds: a duplicate ID, a finding resolved
without a version, a THR cited without a file, a header in
disagreement with its history. The script is the most complex of the
engine, parsers for eight kinds of documents, and it reads every
report in `reviews/` at every call, dozens of files for the engine,
under a second but known, since the map comes at every prompt; over
an unparsable file it exits with an error and never silently drops a
row, the same rule as the driver's. Value: the one file present at
both evidenced merges stops existing as a thing to merge, and merge
requests on the server stop conflicting on it. Price: the ledger is
not on GitHub; where the state is wanted there, `/release` on main
writes `renders/state.md` from the script's output, a tracked render
of way 3 like the README, nothing added by force (forge-save never
adds a file by force, so committing `ledger.md` only at a release is
out).

**F1. The version as a boundary in the history, for branches.** A
branch never changes an artefact's header: `version` and `status`
are written only by forge-land on main, so the header on a branch
stays what the base had, and when main moved meanwhile its header
wins without a conflict. A record written on a branch carries `+` in
the version column (a token, the parser needs one); at the landing
on main one record of kind `landed` is appended per versioned
document that has `+` records, "5.13 | <file> | landed | N records"
(no branch name, since one landing may cover several branches merged
one after another), and forge-history computes the version of each
record at read time from the next `landed` after it. The landing is
done by the first `/save` or `/release` on main that finds `+`
records, through one script, `forge-land.py`, called by both; the
merge itself stays a person's. The write step on main refuses to
write a document while its own history holds unlanded `+` records
("land first: `/save`"), per document, so a landing always precedes
a round and the attribution holds. An approval is an act on main; an
artefact with an approved version and `+` records on a branch is
reported by the ledger script, the map and `/history` as "5.0 with N
unlanded records", its header says nothing of it, and "integer =
approved" holds without exception. On main a round is a landing, so
prime directive 9 keeps its wording; "one version per landing" holds
for branches. The driver never reorders a history: at a merge the
new records of the side whose new records contain a `landed` go
first, otherwise ours, and the boundary is appended after the merge.
That one condition keeps the attribution right in all three
operations: a landing into main (ours has the `landed`), a rebase
(the upstream has it, by construction), and a merge of main into a
long branch (theirs has it, so main's records and its `landed` go
before the branch's `+` records, which stay unlanded), and it does
not depend on two machines' clocks or on people's git habits. Two
clones on main at the same time F1 does not cover: both would raise
5.12 to 5.13; the rule is that concurrent work is a branch
(forge-branch is one command) and two clones on main are sequential;
where it happens anyway, the driver leaves the two `landed` side by
side and the ledger script reports two versions with one number.
Value: the version conflict disappears when two branches touch the
same artefact, without an exception to the append-only history.

**C. The driver for sets of records.** A script,
`scripts/forge-merge.py`, registered under the unambiguous name
`forge-records` as git's merge driver (base, ours, theirs, path).
Three cases, none new to the design, chosen by path: an immutable
line (the histories, `ids.md`), an immutable block from a heading to
the next (`## DEC.` in the decisions), a mutable block
(`` ### `file` `` in both indexes, `### docs/…` in the map). Every
unit has a key, and the text is its payload: a history record (date,
version token, author, subject, kind); a decision its ID; an index
entry its file name; a map entry its page path; a reservation its
prefix with the start of its block (THR 0700 and POS 0700 are two
keys). Behaviour: a record added on one side is taken;
a record of an immutable unit whose payload changed or that was
deleted on either side (the key in the base, another text or none on
one side) is a conflict, never a silent write; a mutable block
changed on one side is taken, on both sides it is a conflict of the
block, and so is a block added on both sides with different text;
two immutable records with the same key and different text stay
side by side, for two decisions with one ID until F2 reserves IDs,
for two history lines simply so. The regions outside the records
(the front-matter, the comment, the map's `## Paths`) merge as text,
three-way. The histories are never reordered and the side with the
`landed` goes first (F1); the decisions, the indexes and the map
append at the end, nothing is reshuffled. After writing, the script
verifies the file's shape and exits with an error when it fails,
never with zero over a damaged file. It tolerates CRLF and writes
LF, imports nothing heavy and reads no repository, only three files
and a path, works with numeric versions in the key as with `+`, and
tolerates the shape one release back, since two clones of the engine
on one machine may differ by a release (forge-status reports the
difference). `merge=union` no: it duplicates and does not order, by
git's own documentation. `/ingest` asks "what is it for?" before the
entry is written, so that Role is in the entry from its birth; a
later correction of an index is normal operation and merges as a
one-sided change (remark: the first critique's derivation of the
research index was not taken, the notes stay untouched; the second
critique's mutable blocks were taken because a correction of a typo
must not be a conflict and the driver has the mutable case for the
map anyway; the principal's first word had been immutable blocks,
decided mutable 2026-10-17).
Value: the histories, the decisions, the indexes and the map stop
halting a merge, and stay as they are.

**C1. Threads as files.** `threads/THR.NNNN.md`, header `id`,
`concerns` (the artefact from today's bracket), `origin`,
`status: open | closed`. A thread is not an artefact: its header is
its state and changes on a branch too, the one header that does. A
thread is never moved, renamed or deleted; closing is `status:
closed` and a `closed` record in the intent's history that says when
and by what; a closed thread is immutable and is the archive, `Was`
for threads is dropped (the answer to THR.0640); what returns is a
new thread citing the old one. No title, no further fields; no
`threads.md`, the list is made by the ledger script by the
convention of B (first sentence, last dated paragraph). A thread
stays without a version and without a history of its own, the
intent's history records it as today. Value: two people on different
threads never conflict, Claude reads only the threads he needs, and
the driver need not handle blocks with an inner state. Migration: M.

**D. `.gitattributes`, registration and where things are made.** A
template `templates/gitattributes`: `text=auto` unchanged, way 2 on
the histories, the decisions, `**/00-INDEX.md`, the map and
`ids.md`, `merge=ours` on the renders, the documentation, the state
render and the published companions, `binary` on
`published/*.pptx|docx`. `/new-project` creates it, `/check project`
reports a project without it with the fix; the engine carries the
same patterns with the prefix `projects/forge/`, not a copy of the
template, and its `.gitignore` gets `projects/forge/ledger.md`.
Neither `ours` nor `forge-records` is built in, both must be in the
config: `/setup` registers them in the global config once for every
repository of the machine, sets `rebase.backend merge` (a driver is
ignored under the apply backend) and `merge.renormalize true` (files
committed with CRLF before normalisation would conflict whole), and
offers `rerere` and `zdiff3`; forge-status reports a missing
registration or a script path that leads nowhere, because an
unregistered clone silently falls back to today's conflict.
forge-save keeps its order (add, commit, rebase, push); the driver
runs inside that rebase, and after B there is nothing to regenerate
into git. Where things are made: the renders of a release, the
documentation (`/document`), the state render and the published
files are made only on main, so branches do not change them; a
render of a recipe or a published companion on a branch is allowed,
cites `v<base>+N` (B), and is made in the knowledge that two
branches making the same one conflict on the server and are settled
by making it again. The server never merges with a driver, and two
people who both append to any history or to the decisions will
always have a conflicting merge request there: the forge's path is a
branch, `/save` (a rebase with the driver), a local merge into main,
`/save`; a merge request is a tool for reading, not for merging. Two
windows of one person on two projects collide nowhere: each project
is a repository of its own, and the one thing that touches both is a
bare `/save`, which commits every repository with changes, the other
window's half-written work included, so in that mode `/save` takes a
slug. Two windows on one project are two working trees:
`forge-branch <name> --worktree` creates the branch and its own
working tree, the second window opens in it. The tree lies at
`projects/<slug>@<branch>/` (decided 2026-10-17): inside the one
tree the forge knows and gitignores. Both windows run from the
engine's root with the same cwd, so the tree is named by the slug,
never read from the cwd: `<slug>@<branch>` is the slug of the second
tree for every command (`/save platform@rework`,
`/forge platform@rework`), the bare slug is `projects/<slug>`, the
map says "platform, branch rework", and forge-save without a slug
visits both trees. The one exception is the engine itself, whose
project lives in the engine's repository, so its second tree is a
second root beside it, `../forge-of-thought@<branch>/`, and the
second window opens in that root; it carries in `projects/` only
`projects/forge`, since the engine gitignores every other project, a
property to know, not a defect. forge_repos recognises a worktree's
`.git`, which is a file, not a directory.

The path through git, from the collision at the save of 0.6 on
2026-10-17 (the ledger on both sides, a double FND.1690): the map
`/forge` ends with the state of every repository against its origin
and that state's offer, as its last word, since the map runs over
several screens and the state is its key message; a state "behind"
is a recommendation to pull before anything is written into the
project, because a rebase over a foreign commit in the ledger is
exactly the collision this brief is about. The reflection before a
write reads that state from the last `forge-status --remote`, where
it also makes the reservation (F2), and `/save` reads it itself; the
write step never fetches, it only repeats the state the reflection
knew, and an unknown or stale state never blocks a write, since F2
drove the network out of the write so that an outage cannot spoil
the round. forge-save pushes a clean repository that is ahead of its
origin (today it stops at "nothing to save"), so that a rebase
finished by hand has a door to the push. forge-save aborts a rebase
that conflicts, so finishing one stays a person's work through git,
step by step and beginning anew: `git pull --rebase`, resolve, add,
`rebase --continue` (a merge instead ends in a commit and has no
continue), then the push through forge-save.

**E. Unique names of reports.** A second run on the same day gets,
instead of `-2`, the time to the minute and four hex characters of a
content hash. Value: two branches do not make the same name; the
time alone is not enough for two people.

**F2. IDs on a branch.** Not a block from a hash of the branch name:
the ID space is about 85 free hundreds per prefix and ten branches
would collide with a probability near 40 % (the birthday paradox).
Instead a sequential reservation through git itself: a reservation
file `ids.md` in the project's root (for the engine
`projects/forge/ids.md`) on main, one line per block ("THR 0700 to
0790: <branch>, <author>"), way 2 immutable lines, one hundred per
prefix, the nearest free hundred of that prefix (THR at 0680
reserves 0700), reserved on demand: the first THR a branch needs
reserves a hundred of THR, the first POS a hundred of POS, a second
hundred when one is exhausted, so that the space is consumed by use
and not by the number of branches (a hundred across all prefixes per
branch would spend the 85 free hundreds in as many weeks at one
branch a week). The reservation happens at the reflection before the
write, which already knows which prefixes the round brings new items
for, never inside the write step: a write is one per round on
confirmation, and a network that drops inside it would fail the
whole round, whose content until then lives only in the
conversation. The reflection calls `forge-branch --reserve <prefix>`,
which writes the reservation to main without a checkout, by
plumbing: fetch origin/main, read the file from it, commit-tree with
the appended line on top of origin/main, push the commit to main, a
refused push means fetch and try again, the working tree untouched
and the driver not run. The push is the compare-and-swap, so two
people never hold the same block; it needs the network at each
reservation and nothing else; a branch without a reservation (made
offline) allocates no new ID until one has happened, never a number
from main's sequence; a project without an origin needs no
reservation and allocates from the sequence; after a reservation the
local main is behind its origin and forge-status says so, which is
true and surprises nobody told. Where main is protected against a
direct push the reservation does not work, a known limit to be said.
Blocks are never released, with a known consequence: a group born on
a branch keeps the hundred its branch reserved, and after the
landing main adds to that group by "overflow anywhere", not inside
its hundred, so "group = hundred" no longer reads for groups from
branches; acceptable, and one more reason for five digits, where a
dead hundred costs nothing. The allocation on main reads the
reservations too, so the next free number is one neither used nor
reserved: the format of the ID scheme stays, the rule of the free
number changes. `/new-project` creates `ids.md` from its template; a
project without the file (made before it, or without an origin)
reads as no reservations, for the allocation and for the driver
alike, so M does not create it. A check on main reports an overlap.
Hash IDs change
the scheme and lazy IDs rewrite the whole branch; neither. Five
digits are another matter, decided 2026-10-17 (remark: 0.3 refused
them as a widening of the scheme; the numbers put on the table
changed the recommendation): POS of the engine stands at 1550 after two
months, a prefix has 99 hundreds, and reservations by the hundred
spend them faster than use. The shape: an ID keeps four digits as
long as the number fits, no zero is added (`POS.0010` stays
`POS.0010`, the next ID after `POS.1550` is `POS.1560`), and the
fifth digit comes only beyond 9999 (`POS.10000`); the scripts read
both, `\d{4,5}` keeps every old ID valid, and every sorting of IDs
in the scripts is numeric by (prefix, number), since as a string
`POS.10000` comes before `POS.9990`. The scope is known: 15 files,
two of them code (forge-history, docs_map), the rest the text `NNNN`
in CLAUDE.md, eight templates and four skills, all of it M's; it
costs less now, before the reservations, than after, and no
existing ID or example changes. Value: it closes the last hole of
POS.1110. It is the last part, because until then the ledger script
at least reports a collision.

**M. Migration.** The forge's position on upgrades (decided
2026-08-29) says that no migration tool exists, knowingly: `/pull`
shows the Action required lines, offers the checks, and Claude
migrates on the user's word. That was made for upgrades of a few
lines; this one rewrites files of every project, here and in every
colleague's clone, and must come out the same everywhere. The
position narrows to: a migration script for a release that changes
the shape of files, always on the user's word. A script,
`scripts/forge-migrate.py <slug>`, door `/migrate [slug]`: a dry run
by default, `--apply` performs; it recognises the shape of a project
not as one state but as a set of marks, one per step (the project
file exists, the headers carry no `date`, `threads/` exists,
`.gitattributes` exists), never by an engine version in the project,
and runs only the steps that are missing; each step verifies itself
and an unfinished project is reported; it commits nothing, `/save`
follows; `--undo` works from the script's own manifest of what it
created and what it took out of git's index, since a restore from
the index would undo neither, and `git clean` stays forbidden. It
refuses to run when the repository is not clean, is behind its
origin or is not on main: the migration is itself one large change
and runs once, on one clone; everyone else pulls before working on.
What it does: A (the header fields), B0 (the project file from the
ledger's header), B (Mined and its note as a record in the intent's
history with the brief as its subject, the Work state as a record in
the specification's history, date, origin and form into the index
entries, the published companions; the Findings and Challenges
tables frozen into `ledger.archive.md`, immutable, the same pattern
as `history.archive.md`, which the ledger script reads for every
item without a record of the new shape; the ledger and nothing else
taken out of git's index and into `.gitignore`; a Waiting line
without an ID printed for the principal), C1 (`threads.md`, in
flow-ba `10-intent.threads.md`, cut by `- **THR.NNNN**` into files,
`concerns` from the bracket, `origin` guessed from the text and the
guesses printed for review, default the principal), D (the
`.gitattributes` from the template, for the engine with its prefix),
then A2 where it holds (the conversion with the syntax-tree check),
and at the end `/check light` and `/check project`; this is the
order of the steps of one run, not the order of the releases below,
and the conversion goes last so that it walks the threads already
cut into files. For a library
only A, B0, B and D. F1 rewrites nothing: a record with a version is
its own boundary, a record with `+` reads from the next `landed`. C
and E need no migration; F2 none in the projects (a missing
`ids.md` reads as no reservations), but the fifth digit is a textual
migration of the engine, 13 files of `NNNN` and two scripts (the
regular expressions and the numeric sort), no ID rewritten.
`/migrate` is the one command (decided 2026-10-17): the script does
every deterministic step, Claude within the same command what needs
judgement (the origin of the threads, from the script's printed
guesses), and the user says `/migrate` and then `/save`; the result
is the same on every clone. The registration of the drivers is
`/setup`'s on every machine, not the project's. `/pull` of the
engine says in Action required: run `/migrate <slug>` on every
project, on one clone, then `/save`; the map, `/check project` and
every skill that would write into a project of the old shape say
"shape before the migration, run `/migrate`" and do not write.

## Promise, impact, order, verification

**What the forge promises.** On the clone, at a local merge and at
the rebase of `/save`: the record files merge by themselves, the
derived state is made anew at read time, the threads and the
artefacts conflict only where two people changed the same item or
sentence. A merge request on GitLab or GitHub does not know the
driver; the path is the branch, `/save`, a local merge, `/save`, and
`/pull` says so at the state "diverged". Two windows of one person
on one project are two working trees, on two projects two
repositories and `/save` with a slug; two clones on main are
sequential.

**What does not change.** The chain, the artefacts and their
definitions, the immutability of records, one write per round on
main, IDs never renumbered, the format of the ID scheme but for the
fifth digit, git only through the scripts, no merge on the
forge's judgement, forge-save's order, no file per record for the
histories and the decisions, no splitting of directories in advance,
the research notes, the kinds of a history record but for `landed`,
the brief's history as the history of the brief's own changes.

**Where it lands.** CLAUDE.md: Document kinds (the ledger made at
read time, the new kinds `thread` and project file, the map as an
authored record file, the wrapping), Ledger (the Waiting rule),
Persistence (the four ways, the driver, `.gitattributes`, the
worktree, the promise, the path through branches), Versioning (the
header written on main only, `+`, `landed`, land first, `v+N` in a
provenance, state records and the version), ID scheme (the THR row,
the free number as neither used nor reserved, `ids.md`, the fifth
digit), the position on upgrades. Templates: ledger (its header
moves to the project file), index (date, origin, form), history
(`landed`, `+`, the `mined` and `state` records), thread new,
threads dropped, gitattributes new, project file new, ids new,
headers without `date` and `last_change`, docs-map (fields under A).
Scripts: forge-ledger, forge-merge, forge-land, forge-migrate new;
forge-history computing the version and reading five digits;
forge-branch the reservation by plumbing (`--reserve`) and
`--worktree`; forge-status the registration and the version check;
forge-save pushing an ahead repository; forge-clone reading the
project file; forge_repos recognising a worktree; the documentation
scripts taking the previous map from git. Skills: the 26 writing the
ledger, `/setup`, `/new-project`, `/import-project`, `/save` (pull
first when behind), `/release` (the state render), `/pull`,
`/check light`, `/check project`, `/forge` (the state against origin
as the map's last word), `/end`, `/ledger`,
`/ingest` (Role before the write), `/document` (main only),
`/migrate` new, the definition of the intent (the mining recorded in
its history), the walkthrough (the reservation at the reflection),
the write step of every artefact (the header untouched on a branch,
land first per document, state records without a raise), `/render`,
`/research` and `/critique` (the `v+N` provenance), the contracts of
the reviewers for the `closed` record of a finding, the recipe
`release-notes` (a landing without content changes). The forge
intent: POS.1110 narrowed, the position on upgrades narrowed, new
positions for the four ways, the ledger at read time, the driver,
threads as files, the version as a boundary, the reservation of
IDs, the worktree, the promise; THR.0090 and THR.0640 moved; a
thread for A2's conversion.

**Order.** First release: A2 first (its conversion and its check),
then B0, A, B and C1 together (one parser of threads, never two),
the `.gitattributes` with `ours` and `binary`, `/setup` with the
config and forge-status with its check, the map's last word and
forge-save's push, and M for all of it. Second release: C with the
attributes of way 2, the rest
of D, and E: it changes no doctrine and removes the second pain, the
histories and the decisions merged by hand, before F1 reaches into
the write step and the release. Third: F1 (`+`, `landed`,
forge-land, land first, the ordering rule). Fourth: F2; the fifth
digit is part of the first release's migration, so that the scripts
read five digits before any reservation needs them.

**Verification.** A throwaway clone (THR.0650), four tests.
Branches on different artefacts: each appends a record to a
different history, opens a thread and adds a decision with IDs from
different hundreds (or, before F2, with the ledger script's report
expected), makes a research on a different question, renders a
different recipe, and one of them runs a round of state only, a
finding closed without a change of the intent; the merge without
conflict, `/check light` clean, the state-only round raising no
version, after the first and second release. Branches over the same
artefact: each changes a different position, the headers untouched;
the merge without conflict with F1, and this is the test that
exercises the history driver. A long branch pulling main into itself
after a landing on main: its `+` records stay unlanded in `/history`
and the map (the ordering rule). The same position changed on both
sides must remain a conflict exactly there.

## Open, for the principal to decide

Nothing. The eleven points of 0.6 were decided on 2026-10-17 in a
walkthrough, all eleven accepted: A2 in the first release before C1;
the project file `project.md`; the state on GitHub as
`renders/state.md` at a release; the version as a boundary (F1) as
written; the reservation of IDs (F2) as written; five digits now,
within the first migration; both indexes as mutable blocks; the
`closed` record and the mining in the intent's history; the Waiting
rule as written; the worktree at `projects/<slug>@<branch>/`;
`/migrate` as the one command of the migration. The brief is ready
to be mined (`/forge intent`).

## Material

- `research/2026-10-17-mergeable-shared-records-in-git.md`: what the
  field does with shared record files; the forge's cascade
  measured; the options.
- `research/2026-10-17-git-merge-drivers-and-their-limits.md`: what
  git itself offers and where it does not reach.
- `sources/ledger-merge-review.md`: a second look at the ledger's
  shape, from another model; the five defects of the file's shape,
  the event-log alternative and lazy IDs come from it.
- `sources/merge-design-review.md`: the review of the proposal in
  three parts, from the same model; `ours` not built in, `ours`
  reversed in a rebase, the ledger out of git, F before the test,
  deletion as a breach, the version as a boundary, decisions as
  unmutated blocks and the immutability of a closed thread come
  from it.
- `sources/merge-brief-critique.md`: the critique of 0.1 against the
  repository; B0, the map as an authored file, the homes B lacked,
  `+`, `landed`, forge-land, no reordering, the birthday arithmetic
  of F2 and the reservation through push, rebase.backend,
  renormalize, `/document` on main, the worktree, `git rm --cached`
  and the corrected verification come from it; its proposal to
  derive the research index was not taken (remark: the notes stay
  untouched, the index is a record file).
- `sources/merge-brief-critique-2.md`: the critique of 0.2; the
  header untouched on a branch, land first, the reservation by
  plumbing and its limit, the free number as neither used nor
  reserved, the driver's keys and regions, the merged-unseen and
  closed-thread reports, the archive read, the undo by manifest,
  the shape as marks, the engine's prefixes, the state render, the
  worktree facts, C1 with B and D split come from it; its two
  alternatives were settled thus: both indexes mutable (taken, over
  the principal's first word, for the reason in C), and the settled
  finding as a `closed` record rather than new kinds (remark: fewer
  conventions, the same information).
- `sources/merge-brief-critique-3.md`: the critique of 0.3; the
  ordering rule of the driver for a merge of main into a branch,
  mined and the work state as records with threads the named
  exception, the reservation per prefix on demand through
  `forge-branch --reserve` with the offline and no-origin cases, the
  `v+N` provenance on a branch, the syntax-tree check of A2, the
  closed-thread check against the closing commit, land first per
  document, a finding settled by no version, the Work state and the
  Form in M, and C before F1 come from it; its case for five digits
  reversed the brief's refusal (remark: Claude's recommendation on
  the numbers, the principal decides).
- `sources/merge-brief-critique-4.md`: the critique of 0.4; the
  mining recorded in the intent's history with the brief as subject,
  state records carrying the version without raising it and a
  landing always raising, the reservation at the reflection into the
  nearest free hundred, blocks never released and "group = hundred"
  lost for branches, `ids.md` named, the scope of five digits (15
  files, verified), the Waiting rule made explicit with the parked
  under their own heading, the header wording, the added Markdown
  traps, the double `landed` reported, and the state-only round in
  the test come from it.
- `sources/merge-brief-critique-5.md`: the critique of 0.5; `updated`
  leaving the recipes too, the prefix in the key of a reservation, a
  missing `ids.md` as no reservations with `/new-project` creating
  it, and the finding as the subject of its `closed` record for the
  engine come from it.
- `sources/merge-brief-critique-6.md`: the critique of 0.7; the
  worktree addressed as `<slug>@<branch>`, the write step never
  fetching, the manual rebase steps corrected, IDs four-digit until
  9999 with a numeric sort (remark: the walkthrough of 2026-10-17
  had taken five digits from the migration on; the principal took
  the critique's shape), the order of the steps of a run against the
  order of releases, and the engine's second root come from it.
- The combined diff of the two merge commits of agentic-platform
  (f748539, d7216ca), read on 2026-10-17: the files merged from both
  sides.
- The analysis of the files of the project forge and of the engine
  on 2026-10-17: records one per line, prose wrapped at 72 columns,
  measured by file group.
