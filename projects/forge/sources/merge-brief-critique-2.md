origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the brief `00-brief-collaboration.md` v0.2; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the brief `collaboration` 0.2

## 1. F1: `<base>+` in the header makes a conflict exactly in the case F1 solves

Base version: 5.12. Branch A writes version: 5.12+. Branch B too. A
lands first, forge-land rewrites the header to 5.13. B lands: base
5.12, ours 5.13, theirs 5.12+, both sides changed the same line
differently, conflict. The same happens whenever main moved between
the creation of the branch and the landing, which is the common
case. Test 2 ("each changes a different position and raises the
version; the merge without conflict only with F1") does not pass with
`<base>+` in the header.

Fix: a branch never changes the artefact's header. Everything "not
landed" is carried by the history as records with +; the header
(version, status) is written only by forge-land on main. The header
is then unchanged on the branch against the base, and if main moved,
its version wins without a conflict. Consequences to be written: an
approval is an act on main (it changes status), not on a branch; an
artefact with an approved integer version and + records in a branch
is reported as "5.0 with N unlanded records" by the ledger script,
the map and /history, the header says nothing of it; the exception
"integer = approved" thereby falls away entirely. After A the header
has only version, status, project, so "a branch does not touch the
header" is a simple rule for the write step.

## 2. F2 is internally inconsistent, and the mechanism of writing to main is missing

- "forge-branch appends a block and pushes" versus "reserved per
  author on demand, not per branch". One or the other. Per branch:
  one reservation at forge-branch, then offline; the price a hundred
  per branch. Per author: the write step reserves only when the block
  is exhausted, in the middle of a round, with the network required.
  I recommend per branch at creation, a second hundred on demand,
  because "offline the last reserved block holds" is weak comfort
  per author when it is exhausted.
- How does a branch write to main while standing on the branch? A
  checkout is out (dirty tree), forge-branch must not rewrite
  history. Feasible with plumbing without a checkout: fetch
  origin/main, read the reservation file from it, commit-tree with
  the appended line on top of origin/main, push <sha>:refs/heads/main;
  a refused push means fetch again and again. The working tree is
  not touched, the driver does not run. The brief must say this,
  otherwise the reservation is only a sentence. And mind: branch
  protection on main (GitHub/GitLab) forbids a direct push and the
  reservation stops working; a known limit.
- What is reserved? IDs are per prefix (POS 1550, THR 0680, DEC 0200,
  FND 1440). Either one hundred across all prefixes ("hundred 16:
  branch X"), or per prefix. One hundred across is simpler; at step
  10 that is ten IDs per prefix per hundred, which a long branch with
  many THRs exhausts, hence the second reservation on demand.
- The allocation on main must read the reservation file too,
  otherwise "next hundred" on main walks into a reserved block.
  Today the write step allocates from the highest existing number;
  after F2 from the highest number and the reservations.
- "What does not change: the ID scheme" contradicts "ID scheme (the
  reservation)" in Where it lands. The reservation is a change of
  the rule "overflow takes the next free number anywhere": a free
  number is one that is neither used nor reserved.

## 3. Indexes as immutable blocks mean that every correction of an index conflicts

C says: a record of an immutable unit changed on either side is a
conflict, never a silent write. That is right for histories and
decisions (an alarm over a breach). For the indexes it means that a
correction of a source's description on a branch (a typo, a sharpened
"Use for" after the proposals P.01 to P.16 were decided) gives a
conflict at the merge even though the other side did not touch it.
The index is today "freely rewritten, verified by /check", so
corrections are normal operation. A mutable block costs the driver
nothing extra, it has that case already for the map.
Recommendation: both indexes as mutable blocks (a change on one side
is taken, on both a conflict), /ingest asking for the Role before the
write kept, because it is good in itself, but not as a reason for
immutability. If the principal insists on immutability, let the
brief say that a correction of an index is knowingly a conflict.

## 4. The order on main: a round written before the landing breaks the attribution of versions

Scenario: a branch is merged locally into main (the history has +
records), then a round runs on main which, by "a round on main is a
landing", writes 5.13 | POS.x | changed and raises the header, then
/save calls forge-land, which finds the + records and appends 5.14 |
landed. The file now holds +, 5.13, landed 5.14; the + records read
their version from the next landed, that is 5.14, but they lie before
the 5.13 record. The rule that closes it: the write step on main
refuses to write while the history holds unlanded + records ("land
first: /save"). forge-land thus always precedes a round. Also: one
landed record may cover the records of several branches merged one
after another, so "branch <name>" in it cannot be filled reliably; N
records is enough, the branches can be added from git log of the
merge commits since the last landed, if the script wants.

## 5. The driver's specification has gaps that decide whether it is written right

- The key of a unit is not defined. "Changed" versus "deleted +
  added" cannot be told apart for a line without a key. I propose:
  history key (date, version token, author, subject, kind), the text
  is the payload; DEC key the ID; index key the file name; map key
  the page path; reservation key the start of the block. Then "same
  key, different text, both sides added" = side by side (immutable)
  or conflict (mutable), and "base has the key with text T1, ours T2,
  theirs T1" = a change on one side = alarm.
- Regions outside the records. The map has an opening paragraph and
  a ## Paths section, the indexes and the decisions a header with a
  comment. The driver receives the whole file; for the parts outside
  the blocks it must have a rule (a textual three-way merge, or
  ours). Without it the spec is not complete.
- Kinds of record. FND.NNNN resolved and CHL.NNNN accepted are not
  kinds of the history template (created | changed | closed |
  removed | approved); landed the brief adds, resolved and accepted
  must be added the same way, or expressed as closed with a reason.
  Write one of the two, for PD2.
- The same item, two records, one landing. With A2 git silently
  merges two sentences of the same position changed on two branches;
  nobody sees the semantic conflict. The ledger script can report it:
  an item with two + records by different authors in one landing,
  "merged unseen, review". One line in B.
- A closed thread changed after closing. Branch A closes the thread
  (header), branch B adds a paragraph to it (body): different lines,
  git merges silently, immutability breached unseen. The check: git
  log -1 --format=%cs -- threads/THR.NNNN.md newer than the date of
  the closed record is a finding; the scripts are the only door to
  git, so this belongs in the ledger script.
- The version of the driver. The global registration points at one
  engine; a second clone of the engine on the same machine (the
  brief itself counts with two clones) may be a release elsewhere.
  The driver should tolerate the shape one release back, or
  forge-status report the difference of versions.

## 6. M, migration

- ledger.archive.md must be read by the script, not only stored.
  Findings open from before the migration have their state only
  there; if the ledger script does not read the archive, they vanish
  from Waiting and from the Findings table. Rule: the archive is the
  source of records for items that have no record of the new shape;
  a newer record overrides the archive.
- --undo "restore from the index" is not enough. The migration
  changes the index (git rm --cached ledger.md) and creates untracked
  files (threads/*.md, project.md, .gitattributes); a restore from
  the index does not undo those. The script must keep a list of what
  it created and what it took out of the index, and undo by it; git
  clean is forbidden, so it deletes by its own list.
- The shape is a set of markers, not one state. The releases go in
  four steps; /migrate must detect every step separately (the project
  file exists; headers without date; threads/ exists; .gitattributes
  exists) and run only the missing ones. The brief hints at it ("each
  step verifies itself"), let it say it outright.
- The engine. The .gitattributes template has paths from the
  project's root; in the engine the project lies in projects/forge/,
  so the engine needs the same patterns with a prefix, not a copy of
  the template. And the engine's .gitignore gets
  projects/forge/ledger.md.

## 7. The ledger on GitHub: tables in the README are the wrong place, a render of the state is the right one

The README is a render for an audience (public for the engine);
Waiting on principal in it is the state of the forge project in a
foreign document. Cleaner, and without contradiction with "never add
-f": /release on main writes renders/state.md (or another name) as
the output of forge-ledger. It is a normal tracked render of way 3,
ours at a merge, made only on main, nothing added by force. The
variant "only at a release" of 0.1 thereby comes back in a legal
form, only under another name than ledger.md.

## 8. The worktree, two facts for the open point

- A worktree has .git as a file, not a directory; forge_repos.py
  recognises a project repository by the .git directory, so it would
  not see a worktree today.
- A worktree in projects/<slug>-<branch>/ is read by the engine as
  another project with the slug <slug>-<branch>. Either the worktree
  lies outside projects/, or the engine knows the pattern
  <slug>@<branch> and maps it to the slug.

## 9. The order of the releases

- B before C1 means that the ledger script parses threads.md in the
  first release and threads/ in the third: two parsers, one to be
  thrown away. Either C1 into the first release with B, or accept it
  knowingly.
- Split D: .gitattributes with ours and binary, /setup with
  rebase.backend, renormalize, rerere, zdiff3 and the check in
  forge-status do not depend on the driver and can go in the first
  release; the attributes of way 2 only with C.

## 10. Minor

- A: previous: tmp/docs-map.previous.md out of the map's header is
  right, but the documentation run uses it for keep/new/remove; the
  replacement is the previous version of the map from git, by a
  script (git show HEAD:...), let A say it.
- C: "the indexes become immutable blocks by one change of /ingest"
  while the sources index allows a bundle with two levels
  (sources/<bundle>/00-INDEX.md); the pattern in .gitattributes is
  **/00-INDEX.md.
- Principle: "immutability is a process rule, git knows no
  attribute" and C at the same time makes a breach a conflict at the
  merge. More precisely: a process rule, the driver raises an alarm
  at the merge, nothing locks.
- B: the ledger script parses at every call all the reviews in
  reviews/ for severity and category; for the engine dozens of files
  of daily check-light reports. Under a second, but let the brief
  know it when /forge map comes at every prompt.
- Test 1: "makes a research" on both branches needs different
  questions, otherwise the same file name; and after F1 without
  `<base>+` test 2 passes as written.
