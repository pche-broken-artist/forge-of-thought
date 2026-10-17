origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the brief `00-brief-collaboration.md` v0.1 against the repository; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the brief `collaboration` 0.1 against the repository

I went through the brief against the current state of the repository
(CLAUDE.md, the templates, the scripts, projects/forge/*). The core
holds: the four ways of merging are the right taxonomy, A+B+C1 solve
the evidenced problem, and F1 is the right shape for versions. Below
is what does not stand against the repository, what is missing and
what I would sharpen. Ordered by weight, not by letter.

## 1. Factual errors verified against the repository

**1.1 docs-map.md is not a derived file, it is a source.** The brief
places it in way 3 ("never merged, not in git, generated at read
time"). I opened projects/forge/docs-map.md: every page entry carries
title, line, kind, reader, says, inputs, links, must-not, evidence,
state. That is the authored plan of the documentation from which the
pages are rendered; says and must-not are nowhere else. It must not
go into .gitignore; after a clone the documentation could neither be
regenerated nor checked. The right place: way 2 with mutable blocks
keyed by the page's path (### docs/start/what-it-is.md), the same
semantics as the sources index. The header fields generated: and
previous: tmp/... change at every run, A applies to them. The field
state: regenerate | keep is a state inside an authored file; I would
leave it, but knowingly.

**1.2 The research index is not derivable in the state it is in.**
The brief places it in way 3. research/00-INDEX.md carries for every
note Question, Answer in short, Consult when; the note's header has
only topic, date, derived_from, status. Answer in short and Consult
when exist only in the index. Derivation becomes possible only after
a change of the note's shape: those two texts move into the note as
fixed sections (## Answer in short, ## Consult when) from which the
script reads. The note is immutable, so this is a write once. The
brief does not name this condition; for Mined of the brief it does,
here not. And it must be said why the sources index is way 2 and the
research index way 3: sources are foreign files without a header, the
description has nowhere else to be.

**1.3 kind and language have no home after B.** Both fields live only
in the ledger's header (templates/ledger.md); they are read by
forge-clone.py, /import-project, /new-project, /forge, /recipe, prime
directive 6. A library (kind: library) is, by /new-project, at its
creation only ledger.md. After B the repository of a library would
contain nothing, and kind and language would disappear. A small
project file in git is needed (name to be decided, say project.md),
header project, kind, language, written once, way 1. That is B0;
without it B cannot be done.

**1.4 F2 does not work arithmetically.** An ID has the shape
PREFIX.NNNN, step 10, a group from the next hundred, so at most about
1 000 IDs per prefix; POS is at 1550. A block "derived from the branch
name" is a hash into a space of about 85 free hundreds (with a block
of 100 numbers = 10 IDs) or 8 thousands. With ten branches the
probability of two blocks colliding is of the order of 40 %, with
twenty above 90 % (the birthday paradox over 85 bins). And a block of
10 IDs per branch is at the same time small for one longer session.
So no hash from the branch name. Two working paths: (a) sequential
reservation through git itself: a reservation file on main (a line
"block 1600 to 1690: <author>"), forge-branch appends to it and pushes
before the first allocation; the push is a compare-and-swap on the
ref, a refused push means "pull and try again", so two people never
receive the same block. Reserved per author on demand, not per
branch, so the space grows with the IDs used, not with the number of
branches. (b) Widening to five digits; forge-history.py has \d{4} in
ID_RE and SHORT_RE, a change of the scheme the brief rejects, but a
smaller intervention than hash IDs. I recommend (a).

**1.5 The order in /save is written backwards, and the regeneration
step is unnecessary after B.** forge-save.py today does add -A,
commit, pull --rebase, push, and on a failed rebase rebase --abort.
A rebase needs a clean tree, so "fetch, rebase, regenerate, commit,
push" does not work without autostash, and autostash is another
merge. After B there is nothing to regenerate into git, the derived
files are not in it; the renders are made only on main at /release.
Today's order stays, the driver runs inside that rebase. The sentence
on the order in D goes.

**1.6 The verification in the section Verification cannot pass as
written.**

- Test 1 has both branches "regenerate a pitch". renders/ of recipe
  renders is not under ours in D (only the renders of a release and
  docs/), so two renders of the same recipe conflict textually, also
  locally. Either different recipes, or renders/ under ours too with
  re-rendering.
- Test 1 has both branches "add a decision" and "open a thread"
  before F2. Both take DEC.0210 and THR.0690; the driver leaves them
  side by side, the ledger script reports a duplicate, so /check
  light is not clean. Before F2 the test must assign IDs by hand from
  different hundreds, or expect the report.
- Test 1 "each appends a history record": each branch into a
  different history, so the history driver is not exercised by test 1
  at all; test 2 exercises it. Fine, just know it.

## 2. What in B has no home

I went through the ledger's tables against the list in B. Missing:

- Work: the state by hand is "on the principal's word", only in the
  ledger; Made and Inputs too. Home: the header of the work
  specification (state: by hand) plus a record in its history, or a
  DEC.
- Briefs: the column Note (what remains for partial, the rejected
  direction for dropped). Beside mined: therefore also mined_note: in
  the brief's header, or a citation of a REJ.
- Dependencies: the brief says "the path of a cited library into the
  entry of the sources index", but a dependency may be cited from a
  recipe or from the chain, not only from the index. Either
  dependencies: in the recipe's header, or the script searches for
  paths projects/lib-*/ in the whole project.
- The states of findings and challenges: the brief covers resolved
  (a history record) and rejected (a DEC). parked and obsolete have
  no write; today they are only in the ledger (FND.0650 parked). Both
  are the principal's verdict, they belong in a DEC like rejected.
  And it must be said which history carries FND.NNNN resolved: the
  history of the artefact whose version resolved the finding; for
  checks of the engine the forge intent (the subject "the operating
  layer" is allowed by the history template).
- Waiting on principal: the rule "open threads, open TBCs, parked
  findings" leaves out open findings and challenges that wait for a
  verdict (it is rather the inverse: parked ones do not wait, open
  ones do), and leaves out decisions with an unfinished action (today
  DEC.0120). Either such an action becomes a thread, or the rule says
  that an Action without a record of fulfilment waits.
- The Waiting line is today an orienting sentence ("steps 1 to 5
  done, step 6 paused", "the soft half done, the hard half open"). A
  derived line will be the ID plus something from the thread. C1 has
  no title and no state field, so a written convention is necessary:
  the first sentence of a thread is its headline, the last dated
  paragraph its state, the script shows both. Without it the map
  loses what it is read for.
- /check light "compares the generated ledger with what the documents
  say" is a circle: the generated ledger is what the documents say.
  The value of the check is in what the script reports: duplicate
  IDs, a finding resolved without a version, a THR citation without a
  file, a disagreement of header and history. Reword.
- The ledger script will be the most complex script of the engine:
  parsers for eight kinds of documents (histories, reviews,
  challenges, threads, indexes, specifications, companions, DECs). A
  shift in the shape of any of them silently drops a row. The same
  rule as for the driver: over an unparsable file, exit with an
  error, never silently omit.

## 3. F1, sharpening

- 5.0+ is a wrong example. A branch from main at 5.12 (a draft after
  the approval 5.0) carries 5.12+, otherwise what the branch came
  from is lost; the exception to "integer = approved" arises only for
  a branch directly over an approved integer version. Write <base>+.
- An empty version column breaks the parser. RECORD_RE in
  forge-history.py requires at least one character in every column. A
  token, not emptiness: +.
- The boundary record fits the history template, the subject may be a
  file, the kind approved exists already; a kind landed is added:
  - 2026-10-19 | 5.13 | PCHe | 10-intent.md | landed | branch <name>,
  N records. A boundary has one history per versioned document, the
  brief writes "one boundary record" in the singular; one per
  document with + records.
- Who performs the landing. The forge does not merge, a person (or
  the server) merges. The + records are therefore brought by /pull or
  a local merge, and the landing must be done by the first /save or
  /release on main that finds + records. By PD10 one mechanism in one
  place: forge-land.py, called by both.
- On main a round is a landing. Then PD9 need not change its wording:
  on main one round = one version as today, + exists only on a
  branch, "one version per landing" holds for branches. The brief
  changes the doctrine for all, for branches is enough.
- The driver must not order the history by date. C says "the
  histories by date and version boundary". Scenario: branch B1
  (records of 17 Oct, +), meanwhile B2 landed on main with the
  boundary 5.13 of 18 Oct. B1 lands on 19 Oct; ordering by date puts
  B1's records before the boundary 5.13 and forge-history attributes
  them to version 5.13 instead of 5.14. Correctly: a history is never
  reordered, the other side's new records are appended after the end,
  the boundary is appended after the merge. In that order the
  attribution comes out right at a merge and at a rebase (ours is in
  both cases the one that has the boundary). Ordering by date fails
  besides on two machines with different clocks.
- Two clones on main at the same time F1 does not cover. Both raise
  5.12 to 5.13 with different content, a conflict in the header at
  the rebase. The evidenced case (a research from another account)
  passes after B, because only the ledger and the index collided; a
  round over an artefact does not. Write it as a rule: concurrent work
  = branches, forge-branch is one command; two clones on main are
  sequential, not concurrent.

## 4. C, D, details that decide whether it runs

- rebase.backend. A merge driver is used in a rebase only with the
  backend merge (the default since git 2.26); with apply it is
  ignored. /setup sets it or forge-status checks it.
- merge.renormalize true. The project has text=auto and the primary
  platform is Windows; files committed before normalisation with CRLF
  give a whole-file conflict at a merge. One line in /setup.
- The driver and line endings. The temporary files %O %A %B reach the
  driver in the form of blobs; with text=auto LF, but let it tolerate
  both and write LF.
- The driver runs per file, it must be fast: no heavy import, no
  reading of the repository, only three files and a path.
- Added on both sides with different text is not described
  separately in C: for immutable records they stay side by side
  (written), for the mutable blocks of the index and the map it is a
  block conflict (to add).
- /document only on main, like /release; the rule of D on the renders
  of a release does not hold otherwise, because docs/ is written by
  /document today, not by /release.
- The companion published/<recipe>.md on a branch conflicts like a
  render; the same sentence as for the render of a recipe.
- The server never merges. Two people who both touch any history or
  decisions.md give a conflicting MR on GitHub always, because both
  append at the end. The brief knows it, but the consequence should
  be written outright: the forge's path is a branch, /save (a rebase
  with the driver), a local merge into main, /save; an MR is at most a
  tool for reading, not for merging.
- The name of the globally registered driver, let it be unambiguous
  (forge-records), so that a foreign repository with the same name in
  .gitattributes does not call the forge's script.

## 5. A2

Pandoc and GitHub treat a soft line break as a space, the render does
not change, verified in md2docx.py (pandoc). The claim about the
items of the intent without a blank line holds (lines 1268 to 1269 of
10-intent.md). Two things to add:

- The conversion script has traps. A sentence beginning with a number
  and a full stop ("2026. The year...") becomes a numbered list, a
  sentence beginning with - or # a list item or a heading;
  continuation lines inside a list item must keep the indentation;
  tables, code and front-matter are skipped. The script must guard
  this and the result must go through /check.
- A rule without a check degenerates. Claude, editing one sentence,
  reformats the paragraph and the reflow is back. A light check
  "a line does not carry two sentences" is needed (approximate,
  abbreviations and IDs like POS.0590. tolerated). Without it A2
  lasts until the first larger round.

## 6. What the brief does not mention and belongs here

- Two windows of one person. "They are two branches or two clones" is
  a rule, not a mechanism; two sessions in one working tree overwrite
  each other's files, and none of the points A to F solves that. The
  mechanism git gives for free: git worktree. forge-branch <name>
  --worktree creates the branch and its own working tree beside, the
  second window is opened in it. Cheap, and it turns the rule into a
  fact.
- Migration of existing projects: .gitignore does not remove a
  tracked file, git rm --cached ledger.md is needed; and the option
  "commit only at a release" collides with the forge-save.py rule
  "never git add -f", so in reality only the variant outside git
  remains. Readability on GitHub can be given to the README render:
  the README recipe can, at a release, insert the tables Documents
  and Waiting, without a second tracked file.
- The naming of states in the wording of the principle: "What is
  derived is not generated into git but at read time" contradicts the
  table, where renders (derived) are in git. Distinguish derived
  state (outside git) and derived documents for the reader (in git,
  only from main).
- Way 4 for closed threads cannot be expressed in .gitattributes, a
  thread is a text file and the state is in the header; immutability
  is a process rule as for reviews. Let the table say so, otherwise
  the reader expects a mechanism.

## 7. Revised order

B0 (the project file with kind, language) and A in one release; B
with it, including the change of the research note's shape (1.2); F1
narrowly (branches only, +, landed, forge-land); C with docs-map.md
and the indexes as mutable blocks and histories without ordering; C1;
D with rebase.backend, renormalize, /document on main; E; F2 as a
reservation through push, not a hash; A2 at any time, best before C1,
with the conversion script and the check. Split the test in three, as
the brief has it, with the corrections of 1.6.

To the open points for the principal I would add two: project.md as a
new file (or another home for kind and language), and sequential
reservation of IDs instead of a hash.
