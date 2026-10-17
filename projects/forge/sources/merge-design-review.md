origin: pasted into the conversation by the principal on 2026-10-17 in three parts; written in Czech by a model in a session outside the forge as a review of Claude's proposal for the merge mechanism of the forge's files, the second and third parts answering Claude's replies; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Review of the proposed merge mechanism, in three parts

## Part one: review of the complete proposal

The attachment is damaged in places (the table and paragraphs 5, B,
C, E, F have cut-off sentences); I judge what can be read of it and
I verified the shapes of the files in the repository.

Overall

The taxonomy of four ways (composed text, set of records, derived
file, immutable unique) is the right frame, and A+B is the core
that solves the problem. The proposal, however, promises more than
A to D deliver, and in several places relies on git behaving in a
way it does not. Concretely:

1. merge=ours is not a built-in attribute driver

Git knows only text, binary and union in .gitattributes. merge=ours
works only after git config merge.ours.driver true. An unregistered
clone silently falls back to the text merge, which is "as today",
but point D claims that derived files do not conflict without
registration. That does not hold. /setup must register both
drivers, and forge-status should report when the driver is missing
from the config or the path to the script leads nowhere (the engine
moves on a host, the driver disappears without a word).

2. ours turns around in a rebase

In git rebase, "ours" is the upstream and "theirs" is the commit
being replayed. /save rebases your own commits onto the remote, so
merge=ours on the ledger throws away the ledger you have just
generated in favour of the remote one. For a derived file that does
no harm only if the regeneration runs after the rebase. The proposal
says "/save runs it before the commit", which is the wrong order.
Correct: fetch, rebase, regenerate, commit, push. The same for
rerere, which with ours/theirs reversed remembers the reversed
resolution.

3. Derived files committed on branches keep conflicting on the
server

The proposal admits it ("a conflicting MR is merged locally") and
leaves it at that. But the ledger changes at every operation on
every branch, so every MR of two concurrent branches will have a
conflict on the server. The sharper solution, which makes the whole
thing disappear: do not commit ledger.md (.gitignore) and generate
it at read time. /ledger, the map and /check call the script
anyway, as proposal B already assumes; the argument "it stays
committed so that the map and the checks can read it" does not hold
when the same script can produce it in a second. The one price: the
ledger is not readable on GitHub in the web. The alternative, if you
want it on GitHub: commit it only at /release on main, the same rule
that already holds for the README. Then nobody changes the ledger on
branches and the whole machinery of ours plus regeneration for the
ledger falls away. The same holds for docs-map.md.

4. F is not "the next step", it is the first thing the test runs
into

The verification scenario ("two branches, each appends a history
record, opens a thread...") means both branches raise the intent's
version to 5.13. The front-matter version: of the artefact is way 1,
text merge, hence a conflict; and the histories of both branches
have records | 5.13 | with different meanings, which do merge, but
5.13 then denotes two different things. The same with IDs: both
branches open THR.0690. The promise in the section "What the forge
promises" therefore holds only for branches that do not touch the
same artefact, which is narrower than written. Either write it so,
or put F before C and D.

On F itself. A version assigned only on main is right; on the
branch the record carries 5.12+ and /release (or the merge into
main) rewrites it. That is not a renumbering of a stable ID, it is
the filling of a placeholder, so it does not cross "never
renumbered". For IDs the simplest is a block per branch, because
the numbers are sparse already (step 10) and gaps do not matter.
What remains is where to take the block from without a shared
counter file (that would conflict): derive it from the branch name,
forge-branch prints it and writes it into the branch's first
history record, a check on main reports an overlap. Hash IDs are
mathematically cleaner but change the scheme; lazy IDs mean a sed
over all files of the branch at the merge, I would not do that.

5. The driver for sets of records

The wording "a record added on one side and untouched on the other
disappears" is either a typo or an error; added on one side and
absent from the base stays. Deleted on one side and untouched on the
other disappears, that is the standard three-way semantics. For
histories, decisions, reviews, however, a deletion is a breach of
immutability; the driver should refuse a deletion in record files
or report it as a conflict, not perform it silently.
The key of a history record is (date, version, item ID, verb). It
is not unique, see point 4. Until you solve F, the driver must be
able to leave two records with the same key and different text side
by side (which is actually what you want), not report them as a
block conflict.
merge=union loses nothing, it only duplicates and does not guarantee
order. The conclusion (own driver) holds, the reason in "What we
know" is imprecise.
Registration in the global config per machine is fine; see point 1
for the existence check.

6. E, unique names

Today 2026-10-14-check-light-2.md: two branches make the same name
for certain. The proposal says "must be unique across branches" but
not how. Add to the name the time to the minute and four hex
characters of a content hash; the time alone is not enough for two
people.

7. Minor

A: date and last_change out of the header is right and is a
necessary condition of B; but status changes at approval too, that
is a legitimate conflict, name it so.
mined: in the brief's header is fine; mind that the brief is way 1,
so two people changing mined at the same time conflict; that is
acceptable.
"Waiting on principal" derived from open threads, TBCs and parked
findings: good, but then the line "who waits for what" in
threads.md must have a fixed shape too, otherwise the script has
nothing to read from.
text=auto is already in .gitattributes; let the template not
overwrite it with another value.

Recommended order

A, then the ledger out of the commit on branches (point 3) instead
of ours plus regeneration, then F for versions (placeholder on the
branch), then C and D for record files, E with them, F for IDs last.
Split the "Verification" test in two: branches not touching the
same artefact (must pass after A to D), and branches raising the
version of the same artefact (passes only with F).

## Part two: on F1, threads as files, and D

F1 and the append-only history. Rewriting 5.12+ to 5.13 is a write
into a record that is otherwise never written; you name that
correctly as an open question. Cleaner than an exception from
append-only is not to write the placeholder into the history at
all: a record on the branch carries the version column empty (or
+), and the version number is received only by the record that is
born on main at the merge or the release: one new line "5.13 =
these records", hence an append, not a rewrite. The version is then
not an attribute of the record but a boundary in the sequence of
records, which incidentally is what a version factually is.
forge-history.py assigns it to the records at read time by
computation. The front-matter version: of the artefact on the branch
then holds 5.12 and changes only on main, so that does not conflict
either.

Threads as files. I agree and add one more reason: threads.md has
1011 lines today and is the only file of way 2 where the record is
not one line but a block with an inner state of its own. A file per
thread turns it into way 1 with a unique name (threads/THR.0680.md),
the driver for blocks is then not needed at all, and C narrows to
histories, decisions and indexes, that is to files where record =
line. That is a considerably smaller driver.

D and renders. The ours driver on renders solves only the local
merge; on the server an MR with a regenerated README conflicts the
same way the ledger does. But because by your rule the renders are
made only at /release on main, branches do not change them and the
conflict does not really arise. It is worth writing that condition
into D explicitly, otherwise someone breaks it with a render on a
branch and wonders why ours did not help. docs-map.md into
.gitignore yes; the pages of docs/ themselves are renders, and the
same holds for them as for the README.

## Part three: on the critique of threads as files

I verified it against threads.md, 10-intent.history.md and CLAUDE.md
(line 600). The critique is right in most of it and in one point, in
my view, not.

I take without remainder.

2: opened/resolved duplicate created/closed in the history, out.
concerns and origin are mandatory fields of the kind THR by
CLAUDE.md and I left them out because I was looking at ## THR
headings, which are not in the file; the record is
- **THR.0680** [intent] .... The header is therefore id, concerns,
origin, status.
3: states open | closed, and how it closed is said by the closed
record in the history. Parking stays text, as it is today.
4, 5, 8: supersedes, waiting_on and the splitting of the directory
out. There is one waiting room; an open thread that is not being
worked waits on the principal by definition.
7: the migration cuts by - **THR.NNNN**, concerns is taken from the
bracket, origin from the text (default the principal, unmarked).
9: in the table of kinds versioned: no, history: the intent's; a
thread has the intent's history even where it concerns the solution
design, as today.

Point 1 I accept with one addition. The file is the archive, Was at
the closed record is dropped (THR.0640). But then it must be written
that a closed thread is no longer rewritten: today the thread is a
living text and Was was the only snapshot of the state at closing.
Without it the file is an archive only if it is immutable after
status: closed, that is the same process rule as for reviews and
research. Otherwise the archive changes silently and the history
points at it with no guarantee of what was there.

Point 6, decisions: here I disagree with the dichotomy. The critique
says "either a file per decision, or the driver handles blocks".
There is a third option and it is the cheapest: decisions.md is
append-only and the blocks never change, so the merge is not a
three-way merge of blocks, it is a union of a set of blocks keyed by
## DEC.NNNN. A driver that merges history lines by key can merge
blocks by key too, provided a block never changes its content; the
difference is only in what the unit of a record is (a line with the
key in the first column, or a block from the heading ## DEC. to the
next). That is one parameter of the driver by path, not a second
driver. A file per decision (ADR practice) is legitimate, but it
introduces a second directory with dozens of files for something
that is never read one at a time; decisions are read as a list. I
therefore recommend: decisions stay one file, the driver has two
units of record, the line and the unmutated block. The open
question is only the ID collision of two DECs on two branches,
which is F2, and a file per decision would not solve it any better.

Title. I would leave it out of the header: the first sentence of
the record stands in for a title today, and the script that makes
the list of threads can take it. A field that would have to be kept
in agreement with the text is one more place for one fact.

So C1: threads/THR.NNNN.md, header id, concerns, origin, status:
open | closed, a closed thread immutable and without Was, no title,
no further fields; decisions one file with a driver for unmutated
blocks.
