origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the brief `00-brief-collaboration.md` v0.3; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the brief `collaboration` 0.3

## 1. A merge of main into a branch breaks the attribution of versions

F1 solves the merge of a branch into main and the rebase. It does not
cover the third common operation: a long branch pulls main into
itself by a merge. Scenario: main has R1..Rn, landed 5.13; branch B
from before 5.13 has R1..Rk, B1+, B2+. git merge main on the branch:
ours = B, theirs = main, the driver appends the other side's new
records after the end: R1..Rk, B1+, B2+, R(k+1)..Rn, landed 5.13. On
the branch B1 and B2 now read the version 5.13 from the next landed,
although they did not land; /history and the map lie on the branch.
(At the final landing of B into main it comes out right, because the
base is a commit of main and B1, B2 are new against it, so they are
appended after landed 5.13 and receive 5.14.)

Two fixes, I recommend the first:

- An ordering rule in the driver: at a merge the new records of the
  side whose new records contain a landed go first; otherwise ours. A
  merge of main into a branch: theirs (main) has the landed, goes
  first, the + records of the branch after it, right. A landing into
  main and a rebase: ours (main) has the landed or no side has, ours
  first, as before. The rebase satisfies it by construction. The rule
  is one more condition, without depending on people's git habits.
- A process rule: a branch takes main only by a rebase, never by a
  merge into itself. Works, but a rebase of a pushed branch rewrites
  history and the rule must be held by a person.

## 2. mined: in the brief's header and state: in the specification's header contradict "a branch does not change the header"

B puts Mined into the brief's header and the state of a work product
into the specification's header; F1 says the header of an artefact
does not change on a branch. The mining of a brief happens in a round
of the intent, so on a branch too; by hand is said at any time. The
fix in the spirit of B: both as a record, not a field. The brief:
00-brief-x.md | changed | mined: partial, <note> in the brief's
history (with + on a branch), the script reads the last such record.
The specification: B already has a record in the history, the field
state: is then redundant, drop it. The headers stay untouched on the
branch. Threads are an exception that must be written explicitly:
the header of a thread is its state and changes on a branch too; a
thread is not an artefact.

## 3. F2: a hundred per branch across prefixes consumes the space at the rate of branches, not of use

Every branch takes a hundred for all prefixes, even if it opens two
threads. At one branch a week the 85 free hundreds are gone in about
85 weeks regardless of how many IDs were actually used. Two things:

- Reserve per prefix on demand: the first THR on a branch reserves a
  hundred of THR, the first POS a hundred of POS (a line THR 1600 to
  1690: <branch>). The consumption matches the use; the price is a
  network round per prefix per branch, which is still little.
- The four-digit space is small even without F2. POS is at 1550 after
  about two months of intensive work on the engine, groups by
  hundreds, 99 groups per prefix; the pace will slow, but by order of
  magnitude it is a year or two to "overflow anywhere" for the
  engine's POS. Five digits will come anyway; deciding it now, before
  the reservations, is cheaper than afterwards (ID_RE and SHORT_RE in
  forge-history are \d{4} and \d{1,4}, old IDs stay valid with
  \d{4,5}). The brief may refuse it, but let it refuse knowingly,
  with this number on the table.

Two details of the mechanism: a branch created offline has no
reservation, so the write step must not allocate new IDs until the
reservation has happened (not silently take a number from main's
sequence); a project without an origin needs no reservation and
allocates from the sequence. And the plumbing commit onto origin/main
leaves the local main behind, so forge-status reports "behind" after
every reservation; it is true, just say it so that it surprises
nobody.

## 4. Provenance on a branch cites a version that does not exist yet

A render cites inputs: projects/forge/10-intent.md v4.58, a research
derived_from: ... v4.41. A render of a recipe on a branch is allowed,
a research too; the intent's header on the branch says the base
(5.12), the content is beyond it. The render would cite v5.12 over
content that is not 5.12, and the ledger script would compute
current/stale wrongly from it. Rule: provenance on a branch cites
v5.12+N (N unlanded records, the script can do it) or the commit
(forge-status gives HEAD); after the landing the script recomputes. A
review of check light cites only a path, those are not affected; a
critique cites a version, that is.

## 5. The render-equivalence check of A2 fails on every file

Pandoc turns a soft break into a space when rendering, but in the
HTML source the difference between SoftBreak and Space shows as
different whitespace (and --wrap=auto breaks the output its own way
besides). Compare either after normalising whitespace outside <pre>,
or the AST (pandoc -t json) with SoftBreak mapped to Space. Otherwise
the test is red even on a correct conversion.

## 6. The check of a closed thread gives false alarms

"A closed thread whose file git dates later than its closed record":
the closing is written on the 17th, /save runs on the 18th, the date
of the commit is later than the date of the record, alarm. Compare
with the commit that closed the thread (the first commit in which the
header says closed): a finding is any later commit that touched the
file.

## 7. The order of releases: C before F1

C changes no doctrine and removes the second biggest pain (histories,
decisions); F1 reaches into PD9, into the write step of every
artefact and into the release. Between the first and the third
release by 0.3 the colleagues would keep merging histories by hand. I
propose: 1) B0, A, B, C1, part of D, M; 2) C, the rest of D, E;
3) F1; 4) F2. The driver works with numeric versions in the key just
as with +.

## 8. Minor

- The write step refuses to write "while a history holds unlanded +
  records": per document is enough, not per project; + in the
  intent's history does not block a round over the solution design.
- "Two immutable records with the same key and different text stay
  side by side until F2 decides" holds for DEC blocks; for history
  lines F2 changes nothing (the key has no ID allocation), they
  simply stay side by side. Drop "until F2".
- A finding not settled by a version of an artefact (a corrected
  index, a renamed file): B says "the history of the artefact whose
  version settled it"; when there is none, the project's intent, as
  for the engine. Add.
- M does not name the migration of the Work state (by hand from the
  column State into a record of the specification's history) and
  silently drops the Sources column Form (text | extract of
  <original> | binary); text/binary follows from the extension,
  extract of must go into the index entry.
- "forge-branch reserves ... a second on demand": on demand it is the
  write step that calls, not a person; name it (forge-branch
  --reserve).
- The verdicts in the Open points are really only two new ones: the
  ordering in the driver (point 1) and per prefix versus five digits
  (point 3). The rest is writing up.
