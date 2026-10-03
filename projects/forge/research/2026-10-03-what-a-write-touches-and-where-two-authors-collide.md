---
project: forge
type: research
topic: what one write in the forge touches, file by file, and where two people working on the same project collide when their branches or clones meet in git, including the case of two different versions of the engine
date: 2026-10-03
derived_from: the engine's own definitions in the working tree of 2026-10-03, after commit 1d8d4d2 (CLAUDE.md; .claude/skills/*/SKILL.md with the state files and the three contracts; .claude/agents/check-light.md and check-project.md; templates/*.md; scripts/forge-save.ps1, forge-pull.ps1, forge-branch.ps1; .claude/settings.json; .gitattributes); the project projects/forge as a sample (ledger.md, 10-intent.md v4.50, 10-intent.history.md, 10-intent.threads.md, research/00-INDEX.md, RELEASE-NOTES.md); 00-brief-next-gen.md v0.1, section "Several people on one project"
status: immutable
---

# What a write touches and where two authors collide

## Question

What does one write in the forge touch, and where would two people
working on the same project collide when their work meets in git?
For every operation that writes: which files, and what in each. For
every shared structure: is the collision a textual conflict git
reports, a silent semantic collision git merges cleanly, or none.
And the second dimension the draft brief `next-gen` names: two
people on different versions of the engine producing documents of
different structure.

## How it was read

No web source: the subject is the engine, and its definitions are
the primary source. The skills, state files, contracts, templates
and the three git scripts were read in full; the project
`projects/forge` was read as a real sample of what the definitions
produce. Git was not run, in any form.

Three marks are used throughout:

- **[V]** verified on a file, named with its line.
- **[G]** reasoning from how git's line-based three-way merge is
  generally known to behave (two sides changing the same or adjacent
  lines conflict; two sides inserting at the same position conflict;
  changes in separate regions merge cleanly; the same path added on
  both sides with different content conflicts; identical changes on
  both sides merge cleanly). Not verified by experiment here.
- **[H]** the author's hypothesis, beyond what the files say.

"Two authors" means two people, each in a clone of his own (or on a
branch of his own), each writing rounds on the same project, whose
commits later meet by a merge or by the rebase `forge-save` runs.

## Key findings

### 1. No write touches one file

Every write fans out. The table lists what each operation writes;
"row" is a table row, "append" a line or block added at the end.

| Operation | Files written, and what in each | Evidence [V] |
|---|---|---|
| a round on the intent | `10-intent.md`: body rewritten for coherence, front-matter `version`, `date`, `last_change`; `10-intent.threads.md`: threads added, rewritten, removed; `10-intent.history.md`: one appended line per change; `ledger.md`: Documents row, Briefs row (Mined, Note), Waiting section, header `updated`; where a verdict was `reject`, `decisions.md`: appended DEC | states/intent.md:78-81, 99-108; CLAUDE.md:473-488, 599-612; walkthrough/SKILL.md:86-90 |
| a round on a brief | `00-brief[-name].md`: body and front-matter; its `.history.md`: appended lines; `ledger.md`: Briefs row; at birth, both files created | states/brief.md:118-146 |
| a round on the assignment | `20-assignment.md`: body and front-matter; `20-assignment.history.md`: appended lines; `ledger.md`: Documents row; a substance change also runs the intent row above | states/assignment.md:68-79, 110-116 |
| a critique run | new file `reviews/YYYY-MM-DD-critique-<lens>.md`; `ledger.md`: new Findings rows, changed states of re-tested rows, document states | critic-contract/SKILL.md:79-80, 116-119 |
| a challenge run | new file `challenges/YYYY-MM-DD-challenge-<persona>.md`; `ledger.md`: new Challenges rows | challenger-contract/SKILL.md:72-73, 107-109 |
| a check run with findings | new file `reviews/YYYY-MM-DD-check-<name>.md`; `ledger.md`: new Findings rows, reopened states | check/SKILL.md:34-48 |
| the walkthrough that settles a run | `ledger.md`: state and Resolution of each row; `decisions.md`: a DEC per `reject`; for `accept`, a round on the artefact (first row) | walkthrough/SKILL.md:79-93; critique/SKILL.md:40-45 |
| an ingest | new file or directory in `sources/`; `sources/00-INDEX.md`: new entry, header `updated`; `ledger.md`: Sources row or Dependencies row; possibly `sources/.gitignore` | ingest/SKILL.md:34-39, 61-62, 72-79, 92-95 |
| a research | new file `research/YYYY-MM-DD-<slug>.md`; `research/00-INDEX.md`: new entry; `ledger.md`: Research row | research/SKILL.md:18-25 |
| a recipe round | `recipes/<recipe>.md`: body, `version`, `updated`; `recipes/<recipe>.history.md`: appended lines | recipe/SKILL.md:42-44 |
| a render | `renders/<recipe>.md` or the recipe's `output:` path: whole file overwritten, provenance front-matter; `renders/<recipe>.docx` or `.pptx`: binary overwritten; `ledger.md`: Renders row, a Published row set to `stale` | render/SKILL.md:35-37, 55-69 |
| a publish | `published/<recipe>.<ext>`: binary overwritten; `ledger.md`: Published row | publish/SKILL.md:30-42 |
| a save | nothing in the project by itself; its `light` check may file a report (the check row); then one commit of everything staged, a rebase on the remote branch, a push | save/SKILL.md:23-27; forge-save.ps1:104, 124, 146, 153 |
| a release | the check rows; the README and the release notes re-rendered whole (two render rows); then the save | release/SKILL.md:23-34, 42-57, 58-73 |

Three things follow.

- **The ledger is in every row but the recipe round.** It is one
  file of about 300 lines in the sample, "freely rewritten", kept
  current "after every operation" (CLAUDE.md:605-606) [V]. Any two
  operations by two authors, however unrelated in subject, meet in
  it.
- **The intent is rewritten, not appended.** "A write rewrites for
  coherence, never appends" (states/intent.md:102-103) [V], and
  prose is hard-wrapped at about 72 columns (CLAUDE.md, Document
  kinds) [V]. A reworded sentence reflows its paragraph, so a small
  change of wording touches several lines [G]; one round of the
  sample left thirteen records of change, spread over the whole
  intent (the records of 4.50 in `10-intent.history.md`) [V].
- **Appends land at one position.** The history log is "appended at
  the end, never rewritten" (templates/history.md:9-10) [V]; DEC
  records are "newest last" (templates/decisions.md:9) [V]; ledger
  rows, index entries and, in the sample, threads are added at the
  end of their table or file (ledger.md:195-200; the sample's
  threads file ends THR.0490, THR.0500, THR.0510) [V]. Two authors
  appending to the same file both insert at the same position.

### 2. How an ID is taken

There is no allocator. The next free ID is read from the local copy
at the moment of the write:

- POS, FCT, THR, REJ, REQ and the other item prefixes: "items in
  tens ... each new group starting at the next hundred ... Overflow
  takes the next free number anywhere" (CLAUDE.md:509-512) [V].
- FND: "continue the global FND sequence" (critic-contract/
  SKILL.md:57), "the next free `FND.NNNN` of the project's
  sequence, in tens" (check/SKILL.md:40) [V].
- CHL: "Continue the global CHL sequence" (challenger-contract/
  SKILL.md:108) [V]. DEC: "numbered DEC.NNNN in the global sequence"
  (templates/decisions.md:8) [V].

The forge already treats this as a critical section inside one
session: "Reports of several checks on one target are filed one
after another, never at once, so that no ID is given twice"
(check/SKILL.md:46-48) [V]. Between two clones nothing serialises
it. The intent knows it: "the known hole, left until it happens:
two parallel branches taking the same next free ID"
(10-intent.md:1146-1147, POS.1110) [V].

In the sample the next free numbers are POS.1390, THR.0520,
REJ.0240, FND.0890, CHL.0200 and DEC.0190 (10-intent.md, threads
file, ledger.md:200, 228, decisions.md:258) [V]. Two authors who
each add one item of a kind from the same starting point both take
exactly these.

An ID, once out, is cited from places that cannot be edited: an
immutable review or challenge file carries its FND or CHL in its
headings (critic-contract/SKILL.md:102; challenger-contract/
SKILL.md:92), the history log is "never rewritten", DEC records are
"never edited", and IDs are "never renumbered" (CLAUDE.md:506-507)
[V]. So a duplicate cannot be repaired within the rules: the repair
itself breaks either immutability or the stability of IDs [H].

### 3. The collision of each shared structure

| # | Shared structure | What two authors do to it | Class | Why |
|---|---|---|---|---|
| 1 | next free POS, FCT, REJ in the intent body | each adds an item with the same ID, in different groups of the file | **silent** | insertions in separate regions merge cleanly [G]; the document then carries one ID twice with two meanings; every later citation is ambiguous |
| 2 | next free THR | each appends the same THR at the end of the threads file | textual, with the duplicate inside it | same position [G]; whoever resolves by keeping both keeps the duplicate ID unless he reads it |
| 3 | next free FND, CHL | each run adds rows at the end of the ledger table and a report file | textual in the ledger; **silent** in the report files when their names differ | rows at the same position conflict [G]; two immutable reports each defining FND.0890 merge cleanly as two files |
| 4 | next free DEC | each appends a record at the end of `decisions.md` | textual, with the duplicate inside it | same position [G] |
| 5 | next free REQ, OOS, CON, ASM, DEL, TBC, SCR | as row 1, in the assignment | **silent** or textual | separate groups merge cleanly, the same group conflicts [G] |
| 6 | `version` of a versioned document | both bump x.y to x.y+1 | **silent** | identical change on both sides merges cleanly [G]; two different rounds now carry one version number, and "a round is one version" (CLAUDE.md:476) no longer holds |
| 7 | `date` | both set the same day, or different days | none, or textual | identical lines merge, different ones conflict [G] |
| 8 | `last_change` | both rewrite the one line | textual, always | one unwrapped line (697 characters in the sample, 10-intent.md:5) [V]; the rule says it is derived, "never by hand" (CLAUDE.md:486-488), so the resolution is a re-derivation, not a choice of side [H] |
| 9 | history log | both append records at the end | textual, always; then a **silent** disorder | same position [G]; mechanically trivial (keep both), but "the order of the file is the order of the changes" (10-intent.md:831-834) no longer holds, and two rounds share one version label (row 6) |
| 10 | intent body, same item or neighbouring items | both reword | textual | same or adjacent lines [G]; made wider by the reflow of wrapped paragraphs |
| 11 | intent body, distant items | each changes his own | none textually; **silent** where the two changes contradict each other | "everything coherent, nothing twice" (states/intent.md:28) is a property of the whole that no line-merge checks [H] |
| 12 | ledger, Documents and Briefs rows | both change the same row (version, date, Mined, Note) | textual | same line [G] |
| 13 | ledger, Sources, Research, Renders, Published, Dependencies | each adds a row at the end, or changes the same Renders row | textual | same position or same line [G] |
| 14 | ledger, Findings and Challenges states | each settles different rows | none, or textual where rows are adjacent | [G] |
| 15 | ledger, Waiting on principal | each rewrites lines of a free-text list | textual where lines are adjacent, else none; **silent** staleness | a line one author's round made moot survives if the other did not touch it [H]; the section is kept by judgement, with no source to re-derive it from |
| 16 | ledger header `updated` | both set a date | none or textual | as row 7 |
| 17 | resource indexes | each appends an entry; both set `updated` | textual | same position [G]; trivial to resolve |
| 18 | a source stored twice | each ingests the same document under his own slug | **silent** | two files, two rows, two index entries, all valid; "on a name collision, suffix `-2`" (ingest/SKILL.md:37) sees only the local directory [V] |
| 19 | dated report file names | both run the same lens, persona or check on the same day | textual (the same path added on both sides) | "suffix `-2` if one exists for today" (critic-contract/SKILL.md:80; check/SKILL.md:36-37) sees only the local directory [V]; one of two immutable files must then be renamed [H] |
| 20 | research note file names | both research on one day | none, unless the slugs are equal | the slug is free text |
| 21 | a render (Markdown) | both regenerate the same recipe | textual, over the whole file | generated text differs run to run [H]; the resolution is a new render, never a hand merge, since "a render is never edited by hand" (CLAUDE.md, Document chain 7) [V] |
| 22 | plain and published files (`.docx`, `.pptx`) | both regenerate | textual in the sense that git reports it, but unmergeable | binaries; one side is taken or the file is remade [G] |
| 23 | render provenance | one author renders from his intent x.y+1, the other writes a different x.y+1 | **silent** | a render is stale "when any version cited ... differs from the current version" (render/SKILL.md:51-53) [V]; after the merge the version matches and the content does not, so the staleness test passes on a render made from text that no longer exists |
| 24 | a regression test of the critic | one author's critic verified a finding resolved against his copy; the other's round changed the same place | **silent** | the ledger says "verified" for a text the merge replaced [H] |
| 25 | a locked brief, a registered source | one locks or registers, the other still edits the draft | textual | same file; after the lock the file is immutable, so the other side's edit has no legitimate landing [H] |

Of the silent collisions, rows 1, 3, 6 and 23 are the ones the
forge's own guarantees rest on: stable unique IDs, one version per
round, and staleness read from version numbers.

### 4. What happens at the moment of meeting

- `forge-save` stages everything, commits, then runs `git pull
  --rebase origin <branch>`; on a conflict it aborts the rebase and
  stops with "Remote changes ... conflict with yours. Nothing was
  lost - ask Claude for help" (forge-save.ps1:104, 124, 146-150)
  [V]. The commit stays local and unpushed.
- `forge-pull` is fast-forward only and, on diverged history, says
  "Run scripts/forge-save.ps1 (it reconciles both), or ask Claude"
  (forge-pull.ps1:77-80) [V].
- Claude is denied git: `.claude/settings.json:10-11` denies
  `Bash(git *)` and `PowerShell(git *)`, and "the scripts in
  `scripts/` are the only door to git" (CLAUDE.md:420) [V]. No
  script resolves a conflict; "merge, rebase and conflicts stay
  git's, by hand or by merge request" (10-intent.md:1141-1142) [V].

So the two scripts point at each other and then at Claude, who has
no door. Given finding 1, where almost any two concurrent writes
conflict textually in the ledger, the second author to save is
stopped at nearly every save and must leave the forge to continue
[H]. This matches the brief's "very unpleasant for the user".

- A stale clone is not announced: `forge-status` "neither fetches
  nor reports ahead/behind" (10-intent.threads.md:838-839, THR.0490)
  [V], and a pull refuses while there are unsaved changes
  (forge-pull.ps1:69-75) [V]. With one write per round (CLAUDE.md:
  71), a long round is prepared on a copy as old as the session, so
  the window in which IDs and versions are taken blind is the
  length of a round, not of a save [H].
- After a merge, nothing in the definitions names duplicate IDs as
  a thing to look for. `check-project` verifies "ID hygiene -
  against the ID scheme in CLAUDE.md, every rule there"
  (check-project.md:57-58) [V]; the scheme says "global and stable -
  never renumbered" and does not say in words that an ID is unique
  (CLAUDE.md:506-512) [V]. Whether the check would report a
  duplicate is therefore not guaranteed by the text [H]. `light`
  compares front-matter with the companion's newest records
  (check-light.md:20-26) [V] and would likely find row 8 and row 9
  if mis-resolved; no check compares a render's content with its
  inputs (row 23) [V, check-project.md:71-76].

### 5. The second dimension: two versions of the engine

**A project records no engine version.** "A project records no
engine version: `/check` measures it against the current
conventions" (10-intent.md:1295-1296, POS.0940) [V]. The ledger
header has no such field (templates/ledger.md:1-8), a history
record has none (templates/history.md:11), and a render's
provenance cites the recipe and inputs only, CLAUDE.md "by path
alone" (render/SKILL.md:40-51) [V]. The engine itself has a version
only at a release (the forge intent's version in the release
message, a tag at a major: release/SKILL.md:58-69) [V]; between
releases `/save` changes `main` with no number, so "which engine"
is, between releases, only a commit [H].

**What in a project depends on the engine version.** Read from the
"Action required" lines of the engine's release notes and from the
templates:

| What depends on the engine | Evidence [V] |
|---|---|
| the shape of every history companion (a table before, a log with an archive now) | RELEASE-NOTES.md:209-215, 679-682; templates/history.md |
| where the threads live (a section of the intent before, a file beside it now) | RELEASE-NOTES.md:232-238; templates/threads.md |
| the ledger's tables, their columns, comments and state words | RELEASE-NOTES.md:171-177; templates/ledger.md:74-79 |
| the status words of the front-matter (`in_review` cancelled) | RELEASE-NOTES.md:23-26 |
| whether a check leaves a report and FND rows at all | RELEASE-NOTES.md:171-173 |
| the meaning of a verdict word (`accept` in `/check` reversed) | RELEASE-NOTES.md:314-320 |
| the sections of a recipe (`Build instructions` read as `Format`) | publish/SKILL.md:18-21 |
| the shape of reports, of provenance, of index entries, the set of prefixes | the contracts; render/SKILL.md:38-49; templates/index.md; CLAUDE.md, ID scheme |

**How two engine versions collide in one project.**

- *Textual, and hard.* The author on the newer engine migrates:
  the history table moves to an archive and a new log begins, the
  threads leave the intent. The author on the older engine meanwhile
  appends a table row to the old companion and edits the Open
  threads section in the intent. At the merge his changes point
  into text the other side moved to another file; git reports the
  conflict but cannot say where the change belongs now [G].
- *Silent.* Everything the older engine creates new merges cleanly
  and is simply of the old shape: a status word since cancelled, a
  check run that filed nothing, a verdict recorded under a word
  whose meaning has since reversed, a recipe with the old section
  [H].
- *The checks disagree.* Each author's `/check` measures "against
  the current conventions" of his own engine. The newer engine
  reports the older shapes as findings and "Claude migrates on the
  user's word" (10-intent.md:1300-1301) [V]; the older engine,
  shown the migrated project, reports the new shapes as findings by
  the same rule. Two instances can migrate one project back and
  forth, each correctly by its own lights [H].
- The migration path is defined per instance: "after `forge-pull`,
  `/check light` and `/check project` on each project"
  (10-intent.md:1297-1299) [V]. It assumes the project has one
  engine above it. A project shared by two instances has two, and
  nothing says which one the project is in step with [H].

A challenge on this ground was recorded and rejected for the
single-instance case (ledger.md:225, CHL.0160; DEC.0100), and an
earlier one was settled with "no engine version in projects"
(ledger.md:222, CHL.0130) [V]. Both verdicts predate a project
worked by two instances.

### 6. Collision points, ranked

Ranked by harm: silent before loud, frequent before rare,
irreparable before repairable. The ranking is the author's [H].

1. **The same ID given twice** (rows 1, 3, 5; inside 2 and 4).
   Silent for POS, FCT, REJ and for FND or CHL in report files; not
   repairable within the rules once cited from immutable files.
2. **Two engine versions over one project** (finding 5). Partly
   silent, self-reinforcing through the checks, and with no record
   in the project to detect it by.
3. **The ledger as the meeting point of every operation** (rows 12
   to 16). Loud and mostly trivial, but it turns nearly every pair
   of concurrent saves into a stop the forge has no door through
   (finding 4). The most frequent by far.
4. **One version number for two rounds, and what derives from it**
   (rows 6, 8, 9, 23). The number merges silently; `last_change`
   and the log conflict loudly; render staleness then reads a
   number that no longer identifies a text.
5. **Coherence of the intent across distant changes** (row 11).
   Silent, and found only by a reader or a critic run after the
   merge.
6. **Same-day report names** (row 19) and **a source ingested
   twice** (row 18). Rare; the first is loud, the second silent and
   cheap.
7. **Renders and binaries** (rows 21, 22). Loud, and settled by
   regenerating; a cost in time and tokens, not in truth.
8. **Resource indexes, appended decisions** (rows 4, 17). Loud and
   trivial.

## Options with trade-offs

Options only; none is designed here, and several can be combined.
Statements about git features are general knowledge, not verified
here [G].

**A. Keep one writer at a time (a convention, no mechanism).** One
person holds the project for a round; the other waits or works in
a draft brief of his own, which is already "the branch"
(10-intent.threads.md:35-42, THR.0170) [V]. Costs nothing and
removes every collision above; it is the present design said aloud
(POS.1110: "a single-user tool per instance"). It does not survive
two people who really work in parallel, and nothing enforces it.

**B. Make the stop survivable.** Leave the structures as they are
and give the forge a door for the moment of meeting: a status that
fetches and says ahead or behind before a round starts (THR.0490),
a pull before the write, and a defined way through a conflicted
save. Shrinks the window and ends the dead end of finding 4;
leaves every silent collision in place, and a conflict door is the
"wrapper of git" POS.1110 draws a boundary against.

**C. Make appends merge.** Git can be told per path to keep both
sides' lines (`merge=union` in `.gitattributes`; the file exists
and carries only line-ending normalisation today) [V for the file,
G for the feature]. Fits the history log, the indexes, and tables
whose rows are independent. Removes the most frequent loud
conflicts; it also removes the one moment a human would have seen
a duplicate ID, and it must never touch a file whose lines are not
independent (the intent, front-matter).

**D. Make IDs collision-free by construction.** Variants: a block
or a suffix per author; an allocation taken from the remote before
the write; IDs given at the merge, not at the write. Each attacks
rank 1 directly. Each changes the ID scheme, which is a convention
(prime directive 2), and the first two make IDs carry or depend on
who wrote them; the third leaves items uncitable until merged.

**E. Take state out of shared files.** The ledger's tables are
largely derivable: document versions from front-matter, findings
from report files, registrations from directories (`check-light`
already verifies exactly these correspondences, check-light.md:
27-39) [V]. A ledger generated from the files, or split so that
one operation owns one small file, has nothing to conflict on.
Removes rank 3 at the root; it reverses "the ledger is the single
source of truth for state" and leaves the Waiting section, which
is judgement and has no source.

**F. Divide the project by topic.** The brief's estimate is that
analysts mostly work each on a topic of his own. If the unit of
writing were smaller than the project (a brief per whole already
is; an intent or threads per topic would be new), two authors
would rarely share a file. Keeps git and the files; costs the one
consolidated intent, "nothing twice", and global sequences would
still need D.

**G. Meet lower down, not in the same files.** Each person keeps a
project of his own and the outputs meet in another system (the
brief names a BRD in a tracker as an example). No shared files, no
collisions here; the collaboration on the thinking itself is then
outside the forge, and the linkage is THR.0140's open question.

**H. For the engine dimension: record, pin or tolerate.** (1) The
project records the engine version or convention level it conforms
to, so a mismatch is detectable; reverses POS.0940 and needs the
engine to have a number between releases. (2) All authors of a
project hold the same engine, by agreement or by a check at the
start of a session; simple, and it slows the one who develops the
engine. (3) A stable line beside the developing one, as the brief
asks under "Upgrade and compatibility", with projects migrated
once, by one person, at a known moment. (4) Tolerate both shapes
in the checks for a time; the engine then carries its past.

## Relevance to this project

For the draft brief `next-gen`, section "Several people on one
project":

- The brief's sentence that a change "rewrites a whole row of
  files" is confirmed and can be said more sharply: the ledger is
  written by every operation but one, so two authors meet in it
  whatever their topics. The estimate "collisions will be few,
  because analysts mostly work each on a topic of his own" holds
  for the content of the intent and does not hold for the
  bookkeeping: with today's structures, textual collisions are the
  normal case of any two concurrent saves, and separate topics do
  not prevent the same next free ID [V for the structures, H for
  the frequency].
- The two prompts of the brief, colliding IDs and different engine
  versions, are the two highest-ranked points here, and they are
  the two with a silent half. They are different problems with
  different remedies and are better kept as two questions.
- The question "at which level it is solved" maps onto the options:
  A to E stay in git and the same files, F changes the unit, G
  leaves them.

Recommendation, offered once and marked as the author's:

1. Before choosing among D to G, say in the brief which case is
   meant: two people who take turns on one project, or two who
   write in the same days. A and B are enough for the first and
   cost little; only the second needs D, E or F.
2. Whatever is chosen, treat three matters as decisions to be
   made in words, since today nothing says them: that an ID is
   unique within a project and what happens when it is not; what a
   version number means when two rounds claim it; and whether a
   project shared by several instances records the engine it is in
   step with (POS.0940 answers no, for one instance).
3. The dead end of finding 4 (save says ask Claude, Claude has no
   door) is worth a thread of its own even for a single author on
   two machines, which THR.0490 says is already the normal case.

Nothing in this note changes any convention.

## What stays uncertain

- Every [G] line: the merge behaviour was reasoned, not run. In
  particular whether two appended table rows conflict or merge
  depends on exact adjacency, and a rebase replays one side's
  commits one by one, which can raise the same conflict more than
  once.
- Whether `check-project` reports a duplicate ID in practice: the
  rule it cites does not state uniqueness, and no run was made.
- Frequency: the ranking by "frequent" rests on the fan-out of
  finding 1, not on observation. The one real case the brief names
  (a project worked by two people) was not read for this note; its
  history would show which collisions actually occurred.
- How Claude Code or comparable frameworks handle several authors
  is a separate question, proposed in the brief and not answered
  here.
