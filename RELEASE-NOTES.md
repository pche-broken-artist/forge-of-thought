---
project: forge
render: release-notes
generated: 2026-10-23
recipe: recipes/release-notes.md v0.13
inputs:
  - projects/forge/10-intent.history.md
  - projects/forge/10-intent.history.archive.md
  - projects/forge/40-solution-design.history.md
  - projects/forge/10-intent.md v5.34
  - projects/forge/decisions.md
  - RELEASE-NOTES.md
---

# Forge of Thought - Release Notes

One section per release of the engine, newest first, for the user who
takes upgrades through `forge-pull`; Action required comes first in
every section; the fine-grained log with the reasons lives in
`projects/forge/10-intent.history.md`.

## 5.34 - 2026-10-23

### Changed
- The ledger script no longer promises to report a version given twice
  after a merge: that report was never built and cannot be built
  without false alarms, and git finds the case itself, the header's
  `version:` line conflicting whenever both sides raised it (POS.1640,
  POS.1790, SOL.0680). For you: a document raised to the same version
  on two branches shows up as a conflict at the merge, settled by
  whoever merges with the next number and one `changed` record.

### Fixed
- `/save` goes on with the step of a conflict when `forge-save` leaves
  a rebase standing, and reports when it refuses a rebase or merge
  already in progress (FND.2490). For you: a conflict at a save goes
  straight into the step of a conflict, both sides laid out for your
  decision.
- The `/forge` map asks `forge-status` whether a project is a
  repository instead of looking for a `.git`, and the `project` check
  no longer checks it (POS.0550, FND.2500). For you: a worktree or a
  linked directory is recognised as a repository like any other.
- The hint of `forge-clone` names `forge-config.py --identity` in place
  of absolute paths (POS.1050). For you: set the identity for a new
  host through the script, as `/setup` does.
- `/spinoff` writes the mining of the brief as a record in the
  intent's history in place of a Mined column (POS.1610). For you: a
  spin-off leaves its state where the ledger reads it.
- CLAUDE.md, `/setup`, `forge-config`, `forge-status` and the solution
  design speak of the one merge driver, `ours`, the records driver
  being gone since 5.31 (SOL.0150, FND.2500). For you: wording only;
  nothing merges differently.

## 5.33 - 2026-10-23

### Fixed
- The solution design no longer promises `fixture.py` or a bare
  `forge-save` that skips the fixture: the script was let go and the
  skip never built, and the fixture is one project made by hand
  (SOL.0830, SOL.0510, FND.2480). For you: a bare `/save` does not skip
  the fixture, contrary to what 5.19 announced.
- The rejected directions of the collaboration and the position on the
  ledger give their reasons on what stands since 5.31, the record files
  as text and IDs settled by detection (REJ.0270 to REJ.0320, POS.1600,
  FND.2450). For you: nothing changes in how the forge works.
- The fifth digit of an ID is kept on its own reason, the reservations
  of IDs it once served being let go (POS.0220, FND.2460). For you: an
  ID still takes a fifth digit beyond 9999, `POS.10000`.

## 5.32 - 2026-10-23

### Fixed
- `/setup` writes your global git configuration, the identity, the
  guard and the registration, only through `scripts/forge-config.py`,
  which goes through `git config --global`, names no path to the file
  and points an identity stanza to its file by a path relative to it
  (POS.1050, SOL.0150, SOL.0740, FND.2260). For you: where your global
  git file moves with HOME, run `/setup` once in each place.
- The comments of `templates/gitattributes` and of the engine's
  `.gitattributes` say "Way 2, derived", as POS.1560 numbers the ways
  since 5.31 (FND.2420). For you: a comment only; nothing merges
  differently.
- CLAUDE.md names `scripts/forge-check.py` with its module
  `forge_check.py` in the Repository layout (FND.2410). For you:
  `forge-check.py light <slug>` is the light check as a program, run on
  trial beside the `light` agent (THR.0530).
- `scripts/forge-report.py` refuses a report name that ends in a run
  number (FND.2430). For you: a report's name is completed by the
  script alone; reports already filed keep their names.

## 5.31 - 2026-10-23

### Added
- A conflicting rebase is left standing by `/save`, the commit made and
  nothing lost: the script prints the files in conflict and the step
  that follows, `forge-status` says a rebase or a merge is in progress,
  and the step of a conflict lays both sides out as a walkthrough, one
  conflict one question, Claude writing the chosen wording and a
  `changed` record (POS.1710, POS.1490, SOL.0840, SOL.0780). For you: a
  conflict at a save is settled in the session, in place of the abort
  and the four manual steps of 5.24; then `/save` again.
- The hook `scripts/hook-git.py` has a third answer, ask, for the
  commands that finish the step of a conflict: `git add`, `git rebase
  --continue` or `--abort`, `git merge --continue` or `--abort`, `git
  merge <branch>`, `git checkout --ours` or `--theirs` on a file; git
  inside `$(` is denied, and the shell's redirections are stripped
  before a verb is judged (POS.1200, POS.0550, SOL.0520). For you: these
  commands come to you as a permission question; every other write of
  git stays denied with the script to use named.
- `/save` refuses a repository with a rebase or a merge already
  standing before it stages anything, and pushes a branch without an
  upstream (POS.1710, SOL.0530, SOL.0780). For you: conflict markers
  are never committed, and a clone switched to a branch has a door to
  the push.
- IDs stay one sequence per project with no blocks; two branches that
  took one number are reported by the ledger script after the merge
  and settled in a walkthrough, the younger renumbered with a record;
  a version given twice is settled by whoever merges, the merged
  document taking the next number and one `changed` record naming the
  merge (POS.1790, POS.0220, POS.1110). For you: an ID or a version
  clash after a merge is mended by you, never by Claude alone.
- A change of the operating layer that needs a test goes brief first,
  then the build and its test on the fixture, then the rounds of the
  intent and the design, never across a release (POS.1780). For you:
  the intent describes what is built at every release.

### Changed
- Three ways of merging in place of four: the record files, the
  histories, the decisions, the resource indexes and the documentation
  map, merge as text, and a conflict in them is two tails kept both in
  the step of a conflict (POS.1560, POS.1690, SOL.0730). For you: no
  driver is needed for the record files on any machine.
- The forge promises two people git, with its help at a conflict; the
  integrator merges on the server or through the step of a conflict,
  and the engine's own project is an open-source repository whose
  issues enter as sources and threads and whose pull requests the
  integrator carries into the chain (POS.1750, POS.1770). For you: to
  contribute, open an issue or a pull request.
- Two windows of one person on one project are not solved by the
  forge: the answer is git's, a branch or a second clone (POS.1700).
  For you: a bare `/save` still commits every repository with changes,
  so keep one window per project or give the slug.

### Removed
- The second, third and fourth release of the brief `collaboration`
  are cancelled: the forge's driver for the record files, `/merge`, the
  worktree `projects/<slug>@<branch>/`, the version as a landing with
  its `+` records, `landed` and `v<base>+N`, the blocks of IDs in
  `ids.md` and the allocation over the branches, the conversion to one
  sentence per line, and the fixture script (POS.1580, POS.1660,
  POS.1670, POS.1730, POS.1760, SOL.0710, SOL.0750, SOL.0760, SOL.0770,
  SOL.0790, SOL.0820, DEC.0280). For you: none of these comes; the
  shape of the first release, 5.26, stands.
- The driver's key `merge.forge-records.driver`, never registered, is
  gone from `/setup`, `forge-config`, `forge-status` and `forge_repos`
  (SOL.0740). For you: the registration of `/setup` is `ours`, the
  backend, renormalize and rerere, with the offer of zdiff3.

### Rejected
- The version as a boundary in the history for branches (REJ.0330,
  DEC.0280). For you: a version given twice is settled by whoever
  merges.
- The forge's driver for the record files, and `merge=union` with it
  (REJ.0340, REJ.0280). For you: the record files are text.
- `/merge` as a command of the forge (REJ.0350). For you: the merge
  stays git's, with the step of a conflict as the help.
- The worktree of a branch and `<slug>@<branch>` as a slug (REJ.0360).
  For you: two windows on one project use a branch or a second clone.
- The blocks of IDs per author and the allocation over the local
  branches (REJ.0370). For you: a clash of IDs is found by detection
  and settled by renumbering.
- The conversion of the prose to one sentence per line (REJ.0380). For
  you: the hard wrap at about 72 columns stays.

## 5.30 - 2026-10-22

### Fixed
- `scripts/forge-ledger.py` finds the closing commit of a thread by the
  header line `status: closed` added or removed, no longer by a count
  of words that made the creating commit the closing one (FND.2350).
  For you: the ledger dates a closed thread by the commit that closed
  it.

## 5.29 - 2026-10-22

### Action required
- A project is a repository of its own only where git names its
  directory as the top (POS.0550, SOL.0510, SOL.0680). For you:
  solution design (SOL.0510, SOL.0680, SOL.0800, SOL.0830), CLAUDE.md
  Persistence, the skills import-project and migrate, the scripts, the
  reply in the issue.
- A project outside git is migrated the same (POS.1740, SOL.0800). For
  you: SOL.0800, the skill migrate, scripts/forge-migrate.py.

### Fixed
- The scripts ask git once whether a project's directory is the top of
  a repository, never look for a `.git`, and run no git on anything
  else; a project whose top lies elsewhere, such as one linked into
  `projects/` from a subdirectory of another repository, is a project
  outside git whose files are written and whose surrounding repository
  is asked nothing (POS.0550, SOL.0510, SOL.0680, GitHub issue #3). For
  you: such a project is no longer refused; it comes in by hand, and
  its git is yours.
- The migration runs on a project outside git: none of the refusals of
  git, the way back your backup taken before `--apply`, `--undo`
  refused, and a run that stops midway finished by running it again
  (POS.1740, SOL.0800). For you: take a backup before `/migrate` on a
  project outside git.

## 5.28 - 2026-10-21

### Added
- A bundle may grow: `/ingest --bundle <name>` adds one file at a time
  to a bundle born at its first file, each file immutable from its own
  registration and its role asked per file; a bundle that arrived whole
  refuses it, and a bare sweep offers an unregistered file inside a
  bundle for registration there (POS.0180, SOL.0230). For you: issues
  or minutes of one origin are kept as one growing bundle, its index
  saying which kind it is.

### Changed
- Two items with one number from any cause, not only a merge, are the
  one exception to "never renumbered": the younger by its `created`
  record is renumbered, and the ledger reports the clash and never
  writes (POS.0220, DEC.0270, FND.2280). For you: the ASM and TBC items
  of a work specification take the next free number of the project.
- The hook composes an ask over the whole command where a rule would,
  since an ask holds in the automatic permission mode (POS.1200,
  SOL.0520). For you: nothing changes yet; no rule answers ask.
- A user runs the forge on Linux: the git scripts, the ledger and
  `docs-state` are verified there (POS.0830). For you: the
  conversions and the hooks are not yet verified beyond Windows.

### Fixed
- CLAUDE.md's Repository layout names `forge-config` and the two hooks
  and the deny rule of the other shell in `settings.json`, and the
  README says that the scripts are the door to a write of git, not to
  git as a whole (FND.2270, FND.2300, FND.2290). For you: the README
  and CLAUDE.md describe the engine as it is.

## 5.27 - 2026-10-21

### Changed
- Reading git is open to Claude and the scripts in `scripts/` are the
  only door to a write: the deny rule `Bash(git *)` is replaced by a
  `PreToolUse` hook, `scripts/hook-git.py`, on Bash, PowerShell closed
  whole as before; the hook allows a reading verb and denies a write,
  naming the script to use (POS.0550, POS.1200, SOL.0520, SOL.0030).
  For you: Claude reads the state of git without a prompt, and every
  commit, push or pull still goes through the scripts.

### Fixed
- `scripts/forge-ledger.py` refuses a project of the old shape whether
  or not it is under git, prints and says to run `/migrate`, where the
  `/forge` map and `/ledger` used to overwrite the hand-kept ledger of
  such a project outside git (SOL.0680, POS.1740). For you: an
  unmigrated project's ledger is never overwritten; migrate it first.

## 5.26 - 2026-10-19

### Action required
- The first release of the brief `collaboration` is built and changes
  the shape of the files of every project: the project file, headers
  without the fields that change, the state in records, threads as
  files, the attributes, the ledger made at read time and the
  migration with its door `/migrate` (SOL.0670 to SOL.0730, SOL.0800).
  For you: on every machine that holds the engine: `forge-pull`, then
  `/setup` for the registration of the merge drivers; then every
  project you keep, each on one clone: `/migrate <slug>` and `/save
  <slug>`, a project already migrated elsewhere `/pull <slug>`; nobody
  works in two on one project before the second release.

### Added
- `/migrate [slug]` is the door to `scripts/forge-migrate.py`: it
  recognises the shape of a project by its marks, runs only the steps
  that are missing, verifies each, commits nothing and undoes through
  `--undo`; it refuses a repository that is not clean, is behind its
  origin or is not on `main` (POS.1740, SOL.0800). For you: a project
  is migrated once, on one clone, and every other clone of it pulls; a
  project of the old shape is read, not written, until it is migrated
  (POS.0820).
- Every project has a project file, `project.md`, written once at its
  creation and carrying `project`, `kind` and `language`, read wherever
  the ledger's header was read (POS.1590, SOL.0670). For you: the kind
  and the language of a project are set in `project.md`, no longer in
  the ledger.
- The ledger is made at read time by `scripts/forge-ledger.py` from the
  documents and is no longer kept in git; an unparsable file drops its
  row aloud and the save goes on; the script reports two items with one
  ID, two versions with one number and a THR cited with neither a file
  nor a `closed` record (POS.1600, POS.1640, SOL.0680). For you: never
  edit `ledger.md` by hand; the map, `/ledger`, `/end` and the checks
  call the script, and the hand-kept ledger of a migrated project lies
  in `ledger.archive.md`.
- Threads are files, `threads/THR.NNNN.md`, with a header of `id`,
  `concerns`, `origin` and `status`; a thread closes by `status:
  closed` and a `closed` record in the intent's history, and a closed
  thread is immutable and is its own archive (POS.1680, POS.0120,
  SOL.0720). For you: `threads.md` is gone; a thread is opened, worked
  and closed in its own file.
- Every project carries a `.gitattributes` from
  `templates/gitattributes`: `merge=ours` on the renders, the
  documentation and the published companions, `binary` on the
  published files; the engine carries a list of its own (POS.1690,
  SOL.0730). For you: a render or a page in conflict keeps one side
  and is made again; the driver for the record files stays the second
  release's (DEC.0250).

### Changed
- A header carries nothing that changes with a round: `date` and
  `last_change` leave the artefacts and the work specifications,
  `updated` and `last_change` the recipes, `updated` the indexes,
  `generated` and `previous` the documentation map, all of it derived
  from the history or from the run (POS.1570, SOL.0700). For you: the
  date of a version is the date of its records; `version` and `status`
  stay.
- What only the ledger knew lives in records: the mining of a brief in
  the intent's history, a source's date and origin in its index entry,
  a finding or a challenge settled as a `closed` record, a work
  product's state in its specification's history, the provenance of a
  published file in a companion beside it, `published/<recipe>.md`
  (POS.1610, SOL.0690, FND.2230). For you: settle findings and mining
  by records; the ledger shows them.
- A record of state only carries the current version and does not
  raise it (POS.1630, SOL.0690). For you: a round that only closes
  findings after a check is no longer a version.

## 5.25 - 2026-10-19

### Fixed
- The position on recipes still spoke of an updated date after the
  field left the recipe templates (POS.0710). For you: a recipe carries
  `version` and no date; its date is computed from its history.
- The checks of 2026-10-19 found rules said in two places, mended so
  that each has one owner: `templates/ledger.md` says what each column
  holds and where it is read from, with the Waiting rule and the
  Reports list; `templates/project.md` what a project without the file
  is; `templates/history.md` the shapes of the state records; the
  intent's definition the rules of a thread; the documentation
  contract the kinds of a page (FND.2090 to FND.2220, FND.0980). For
  you: to know one of these rules, read its owner.
- The engine's own project is migrated: its ledger made at read time,
  the hand-kept one archived as `ledger.archive.md`, the fields `date`,
  `last_change` and `updated` out of every document and index
  (FND.2060, FND.2070, SOL.0700). For you: the engine's project shows
  what a migrated project looks like.

## 5.24 - 2026-10-18

### Added
- Every reviewer's report is named by its date, the time to the minute
  and four hex characters of a content hash, the name completed by
  `scripts/forge-report.py`, through which `/critique`, `/challenge`
  and `/check` file (POS.1720, SOL.0810). For you: reports are named
  `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`; the names given before
  stay as they are.
- `/setup` registers `merge.ours.driver`, `rebase.backend`,
  `merge.renormalize` and `rerere.enabled` in the global file git
  reads and offers `merge.conflictStyle zdiff3`, reading every key
  first and leaving an existing value; it adds the `Author` line to
  `CLAUDE.local.md` and offers an existing instance file the lines it
  lacks, on your word (SOL.0740, SOL.0150). For you: the handle in
  `Author` is the author of every record and is asked once.
- `forge-status` reports the registration keys missing on the machine
  (SOL.0740). For you: a machine without the registration is said so.
- `forge-save` pushes a clean repository that is ahead of its origin;
  a conflicting rebase is aborted and the four manual steps printed,
  the save the last of them (SOL.0780, POS.1710). For you: commits
  left unpushed by a rebase finished by hand go out with the next
  `/save`.
- An ID takes a fifth digit beyond 9999, `POS.10000`, never a zero
  added to an existing ID (POS.0220, SOL.0790). For you: no ID
  changes.

### Changed
- `/critique` and `/challenge` number and file the report and write
  its state as `/check` does; the agents write nothing (POS.1140,
  SOL.0300). For you: reviewers of any kind can run at once.
- `/ingest` asks "what is it for?" before the index entry is written,
  one question per source, a bundle one for the whole, and the entry
  carries the role from its birth (POS.1040, POS.0180). For you: the
  Role field is never left empty waiting for your answer.

### Fixed
- Positions that still spoke of ledger rows say where the state now
  comes from: a source's origin date is a field of its index entry,
  how far a brief is mined is the mining record, a work product
  touched by hand is a record, a finding's state is a `closed` record
  in the history that settled it (POS.0180, POS.0920, POS.1520,
  POS.1140, POS.0400, POS.0440). For you: these are what the ledger is
  made from since 5.26.
- A position cites its brief by path; the version it was mined at is
  the mining record's (POS.0110, POS.0920). For you: cite a brief
  without a version.
- The designed merge is made consistent: `/merge` refuses a repository
  behind only, a diverged main with no branch named merges
  `origin/main` into main, and the next free number is read over the
  local branches within the author's block where the project has one
  (POS.1760, POS.1490, POS.1690, POS.1730, POS.0220). For you: nothing
  changes; this is deferred (DEC.0250).

## 5.23 - 2026-10-18

### Added
- `/save --quick` leaves out the `light` check and nothing else, the
  message drafted and confirmed as always or given with `-m`
  (POS.1100). For you: a change settled in a round reaches the remote
  at once; `/release` keeps its checks.

## 5.22 - 2026-10-18

### Added
- A thread on the form of the deferred releases: the driver, `/merge`,
  the worktree and the allocation as designed, or git opened to Claude
  with the deny rule narrowed to the destructive verbs (THR.0710). For
  you: nothing changes yet.

### Changed
- The brief `collaboration` is built as the preparation and the first
  release now; the second and the fourth release are deferred, their
  form decided after the first from how it works, and the third stays
  optional (DEC.0250, THR.0620). For you: the driver, `/merge`, the
  worktrees and the blocks of IDs do not come with the first release.
- An ID on a branch of one clone is to be the next free number read
  over every local branch, with no network and no block; blocks per
  author wait for a second clone with a branch in flight (POS.1730,
  POS.1110, DEC.0240). For you: nothing changes until it is built.
- Two items with one number after a merge are the one exception to
  "never renumbered": one is given the next free number, and a thread
  is renamed with it (POS.0220, POS.1680). For you: an ID clash after
  a merge is mended by renumbering, and only then.
- The migration's instruction is said per project: a project is
  migrated once, on one clone, by whoever keeps it, and every other
  clone of it pulls (SOL.0800). For you: this is the shape of the
  Action required of 5.26.

## 5.21 - 2026-10-18

### Action required
- A change of the way or the why of a work product made in its file,
  its task, its inputs, its method or what it assumes, is carried into
  the specification in the same round; the states of the work and its
  wording are the file's alone (POS.1520). For you: the light check
  gains the rule; /work step 5 cites it.

## 5.20 - 2026-10-18

### Changed
- The first release of the brief `collaboration` is built on `main` in
  one stretch, the way back the tag `pre-r1` (DEC.0230, THR.0620). For
  you: the tag `pre-r1` on the engine marks the state before the new
  shape.

### Rejected
- Building the first release on a branch of the engine in a second
  working tree (DEC.0230). For you: the branch was complexity for a
  risk the principal controls.

## 5.19 - 2026-10-17

### Changed
- The brief `collaboration` is planned in four releases: the first the
  project file, the header, the ledger at read time, threads as files,
  the attributes, the registration, the unique names of reports and
  the migration; the second the driver, `/merge`, the worktree and the
  version as a boundary together; the third one sentence per line; the
  fourth the blocks of IDs, on a trigger (DEC.0220, POS.1580,
  POS.1730). For you: nothing changes yet.
- The migration takes a tag per project before it applies, and the way
  back is said truthfully (POS.1740). For you: a project can be
  returned to the state before its migration.
- The fixture, the test bed of the forge's own tests, is a project of
  its own that a bare `/save` skips (POS.1590, POS.1750). For you: the
  forge's tests never touch a clone of your projects.

## 5.18 - 2026-10-17

### Changed
- `/critique` and `/challenge` take as target any file of the project
  by its path, a work product with its specification; a reviewer that
  finds nothing to work on says so (POS.0410, POS.0420). For you: a
  plan or a work product can be challenged as an artefact can.

## 5.17 - 2026-10-17

### Action required
- The second challenge of the architect is settled and the order of
  the releases of the brief `collaboration` reversed, the conversion to
  one sentence per line last and on its own (DEC.0210). For you: nobody
  works in two on one project before the second release of the brief
  collaboration: the first alone merges the histories as text and
  leaves a merge to raw git.

### Changed
- The command, not the agent, numbers and files the report of every
  reviewer, the critic and the challenger as the check (POS.1120,
  POS.1140). For you: reviewers of any kind may run at once.
- The designed merge gains both directions, `/merge <branch>` on main
  and `/merge main` on a branch, the record of every verdict and the
  push as the last step; "join the landing" replaces "land first";
  rerere is a convenience (POS.1760, POS.1660, POS.1690, POS.1730,
  POS.1580, POS.1740). For you: nothing changes until it is built.

## 5.16 - 2026-10-17

### Added
- A merge is git's through the forge's door: `/merge` on the user's
  word, the driver merging the record files and what remains in
  conflict worked in a walkthrough, one conflict one question
  (POS.1760). For you: nothing changes until it is built.
- One integrator and N contributors: a contributor works and saves on
  a branch, the integrator merges it locally through `/merge` and saves
  on main, a merge request on the server is for reading (POS.1770).
  For you: a protected main is the normal case.
- A thread on whether `/save` takes the conflict walkthrough of
  `/merge` in place of aborting a conflicting rebase (THR.0700). For
  you: nothing changes yet.

### Changed
- IDs on a branch come from blocks per author assigned by hand, a
  thousand per prefix (POS.1730, POS.0220). For you: nothing changes
  until it is built.
- The ledger script degrades aloud instead of failing the save
  (POS.1600). For you: an unparsable file never stops a save.
- A release, the documentation and a publish refuse a repository that
  is behind or diverged (POS.1710). For you: pull before a release.
- The migration refuses while branches are in flight, and undoes a
  changed file from the index and the rest from its manifest
  (POS.1740). For you: land or give up every branch before migrating.
- After an upgrade that changes the shape of files, a project of the
  old shape is read, not written, until it is migrated (POS.0820). For
  you: the migration stays your decision, project by project.

### Rejected
- The reservation of ID blocks by a push onto `origin/main` from a
  branch, by plumbing (REJ.0320). For you: a hosted main is protected
  by default and refuses such a push.

## 5.15 - 2026-10-17

### Changed
- One sentence per line is to hold in the renders too, since a model
  writes them, and `md2video` joins and wraps lines itself (POS.1580).
  For you: nothing changes until the conversion is built.

## 5.14 - 2026-10-17

### Changed
- Every report of a reviewer, not only the second of a day, is to
  carry the time and a hash in its name, since the first report of a
  day on two branches collides too (POS.1720). For you: built at 5.24.

## 5.13 - 2026-10-17

### Added
- The brief `collaboration` is mined: several people, branches and
  windows on one project become possible, built in releases planned in
  THR.0620 (POS.1560 to POS.1750, POS.1110, THR.0690). For you:
  nothing changes until a release builds it.
- Every file of a project has one of four ways of merging, and the
  forge tells git which one: composed text, a set of records merged by
  the forge's driver, derived documents made again at a merge, and
  immutable files with unique names (POS.1560, POS.1670). For you: the
  forge still never merges on its own judgement.
- A project file, a header with nothing that changes with a round, the
  ledger made at read time, the state in records and threads as files
  (POS.1590, POS.1570, POS.1600, POS.1610, POS.1680). For you: built
  at 5.26.
- Waiting on principal is a rule, not a hand-kept list: the open
  threads, the TBCs the principal owns, the open findings of a critic
  and the open challenges, the parked ones under a heading of their
  own (POS.1620). For you: free text without an ID has no place there.
- The ledger script reports what the merged files cannot, among them
  two items with one ID and records of two authors in one landing
  (POS.1640). For you: a silent merge of two sentences is reported for
  review.
- Where the state is wanted on the remote, a release on main writes
  `renders/state.md` from the ledger script (POS.1650). For you: the
  ledger itself never reaches git.
- The version is a boundary written on main only: a branch never
  changes an artefact's header, and the records written on it are
  landed on main (POS.1660). For you: nothing changes until it is
  built.
- Every project carries a `.gitattributes` from a template of the
  engine (POS.1690). For you: built at 5.26.
- Two windows of one person on one project are two working trees,
  `projects/<slug>@<branch>/`, and a bare `/save` is for one window
  (POS.1700). For you: with two windows open, save with a slug.
- The map ends with the state of every repository against its origin
  and its offer, and a state behind is a recommendation to pull before
  anything is written (POS.1710). For you: read the map's last line
  first.
- A release that changes the shape of files comes with a migration,
  `/migrate [slug]`, run on the user's word (POS.1740, POS.0940). For
  you: built at 5.26.
- Prose is to be written one sentence per line instead of wrapped at
  72 columns (POS.1580). For you: nothing changes until the conversion
  is built.

### Changed
- The language and the kind of a project move to the project file,
  since the ledger leaves git (POS.0060, POS.0960). For you: built at
  5.26.
- An ID may take a fifth digit beyond 9999 and IDs sort numerically
  (POS.0220). For you: built at 5.24.
- A closed thread stays as its file, and the rule of 5.4 that its last
  text goes into `Was` is withdrawn (POS.0310, POS.0120). For you: a
  closed thread is read in its own file.

### Rejected
- IDs on a branch from a hash of the branch name, hash IDs, lazy IDs
  at the landing or a hundred reserved across all prefixes per branch
  (REJ.0270). For you: a block from a hash collides among ten branches
  with a probability near 40 %.
- `merge=union` for the record files, and the ledger committed only at
  a release (REJ.0280). For you: union duplicates and does not order.
- The entries of the resource indexes as immutable blocks (REJ.0290).
  For you: a typo corrected in an entry is never a conflict.
- `<base>+` written into an artefact's header on a branch (REJ.0300).
  For you: the version on a branch is computed and reported, never
  written.
- A file per record for the histories and the decisions, an event log,
  and the splitting of directories in advance (REJ.0310). For you: a
  record stays one line in one file.

## 5.12 - 2026-10-15

### Added
- A thread on a question put to the manual in free text, `/man <free
  text>` (THR.0680). For you: nothing changes yet.

## 5.11 - 2026-10-15

### Added
- A thread on a chain handed over whole, for a small project where
  little is at stake (THR.0670). For you: nothing changes yet.

## 5.10 - 2026-10-15

### Fixed
- The `html-player` format is the timed events wrapped as a script
  call, `renders/<recipe>.<lang>.html-player.js`, so that the player
  page plays a file from disk as well as from Pages; the spelling
  `.json` never existed on disk (POS.1530, SOL.0650). For you: look
  for the `.js` file beside the render.
- The player page, `docs/videos/index.html`, is written anew by
  `md2video` from `templates/html-player.html` whenever a file is
  written into the folder; the skeleton is what is edited, and the page
  has no document kind of its own (POS.1540, SOL.0660, TBC.0040). For
  you: never edit the page by hand.
- A position claimed a check that keeps a solution design true against
  what realises it, which the roster does not have (POS.1420). For you:
  no check verifies a solution design against the files.

## 5.9 - 2026-10-14

### Added
- A recipe of the genre `screenplay`, the fourth genre, renders a
  screenplay of a terminal conversation, made into a video or the
  events of the player page by `scripts/md2video.py`, with no designed
  step (POS.1530, POS.0590, POS.0770, SOL.0650). For you:
  `/recipe screenplay` composes one; `/render` makes the file and
  `/publish` has no part.
- A recipe may render in several languages, `languages:`, the first
  primary, the rest translated in the same run, one render per
  language, `renders/<recipe>.<lang>.md` (POS.1550, SOL.0400). For
  you: a recipe with one language keeps `renders/<recipe>.md`.
- A project's recipe may send its file into the engine's
  `docs/videos/` by its `output:` path, the one public place, served by
  GitHub Pages and left alone by `/document` (POS.1540, SOL.0660). For
  you: read the file before the engine is saved; that is its clearing
  for the public.
- A thread on the course of the teaching videos (THR.0660). For you:
  nothing changes yet.

## 5.8 - 2026-10-13

### Changed
- The verdict line of a walkthrough gains `(q)uestion`: a question on
  the open item, nothing changes, Claude answers and closes the item
  again, and `q` writes nothing (POS.0850). For you: none; the hook
  prints the new line from the next prompt.

## 5.7 - 2026-10-13

### Action required
- The specification of a work product is `work/<name>.spec.md` with
  its history `work/<name>.spec.history.md`, and the file keeps the
  bare name `work/<name>.<ext>` (POS.1520, SOL.0640). For you: an
  existing work product's specification and history are renamed to
  `.spec.md` and `.spec.history.md`, its file to the bare name, the
  ledger's Work row and the file's header with them.

## 5.6 - 2026-10-12

### Added
- A new document kind, **work**: an output of the project made with
  work of its own, the file holding the content and a specification
  beside it holding the way and the why, versioned with its history
  and approvable, worked through `/work <name> [slug]` (POS.1520,
  POS.1080, POS.0310, SOL.0640). For you: a model, an analysis or a
  worked task has its own home in `work/`.

### Fixed
- The table of document kinds has six groups since the kind work, and
  the position says so (POS.1080). For you: nothing to do.

## 5.5 - 2026-10-11

Nothing for the user of the engine.

## 5.4 - 2026-10-11

### Added
- A thread on what of a thread survives its closing (THR.0640), and a
  thread on testing the new output of `forge-pull` (THR.0650). For
  you: nothing changes yet.

### Changed
- A thread that closes carries its last text in the `Was` of its
  `closed` record (POS.0310). For you: the way to a decision stays
  searchable in the log.

## 5.3 - 2026-10-11

### Action required
- The generator of the documentation, the writer's definition and
  the contract, is hashed with the inputs of every page, so that a
  change of the rule a page is made by regenerates every page made by
  the old one; the choice against a switch that forces a run is
  recorded (SOL.0460). For you: run `/document` in a new session;
  every page regenerates, as its hash changed.

### Added
- The command `/history <ID> [slug]` is born with its script,
  `scripts/forge-history.py`: the script gathers what the project
  holds of one item, its wording today, every record whose subject it
  is, the records of other items that mention it, the rows of the
  archive that mention it and every other place that cites it, and
  prints it as one wrapped timeline, taking the short form of an ID;
  Claude adds a few sentences of its own on top, marked as such, and
  nothing is derived from them (POS.1510, SOL.0630; the row of the
  Commands table and the scripts comment of CLAUDE.md). For you:
  none; the command works on every project as it stands, and
  `/history <ID>` gives you the whole way to an item in one call.

### Changed
- The rule of Versioning & status cites `/history` instead of
  describing the search: this is the one way Claude reads an item's
  history before proposing a change to it (POS.1510, POS.0310). For
  you: the history is still never loaded whole; a proposal to change
  an item now rests on the script's gathering, the same every time.
- The planner's definition says that every page is reached from
  another page, at least one other entry naming it under `links`
  (operating layer, solution design 0.13). For you: no page of the
  documentation hangs from the index alone.
- The writer's outline of a how-to names the heading "A worked
  example" (operating layer, solution design 0.13). For you: one
  spelling of that heading on every how-to page.
- The contract's sentence: an enumeration whose members carry a gloss
  is a list, one member per line, and a rule, its reason, its
  exception and its purpose are separate sentences (operating layer,
  solution design 0.13). For you: shorter sentences on the pages at
  the next `/document`.
- The second run of the redrawn generator was compared against the
  audit's measurements M.01 to M.18 (SOL.0460, THR.0630). For you: the
  three changes above are what the comparison found.

### Fixed
- The first run of the redrawn generator, 86 pages, three new, the
  check clean after four regenerations, found three defects, mended:
  the reader of the map takes a block by its bold label, the
  definitions' shape; the state script honours the planner's
  `remove`, which it overwrote; the planner's entry agrees with itself
  (SOL.0460). For you: a page the planner removes stays removed, and
  `/document` runs clean.

## 5.2 - 2026-10-11

### Added
- A thread on what remains of the documentation audit of 2026-10-11
  after the round on the operating layer: the owners outside the
  generator, then `/document` in a new session and the comparison
  against the audit's measurements (THR.0630). For you: nothing
  changes yet.

### Changed
- The documentation's rules are amended from the audit of 2026-10-11:
  the kind of a page says what content belongs on it and one rule has
  one home page; a generic example in the shape an owner defines, and
  a diagram from the owners, are mirrors, not inventions; a reason the
  inputs do not give stays off the page and is listed by the run; an
  input may be a named part of a file, hashed as that part; one voice
  on the pages, the full rule the documentation contract's (POS.1450).
  For you: About no longer restates the how-tos and the references, a
  page carries no reason its inputs do not give, and a change of one
  section or one item regenerates the pages made from it and no
  others, where 78 of 83 pages regenerated at 5.1 for about a dozen
  changed.
- The generator is redrawn to those rules: inputs as files or named
  parts hashed as the part, the index from a line per entry and the
  reader paths of the map, one outline per kind of page and the
  version a page was made for, the contract owning the voice and the
  sentence and what never reaches a page; the choices recorded
  (SOL.0460). For you: `/document` works as before; the pages it makes
  follow the amended rules.
- The criterion that separates the guarded commands from the rest is
  stated, where the list implied it and never said it (POS.1090). For
  you: you can tell of any command whether it runs on your word only.

### Fixed
- A session can no longer be said to end "without loss": the
  sentence contradicted `/end` and prime directive 9; `/end` says
  what the conversation holds that the files do not, and `/ledger`
  re-orients from the ledger (POS.0330, POS.1500). For you: end a
  session with `/end` to know what closing it would lose.
- `/save` rebases your commits onto the remote; the sentence that left
  merge, rebase and conflicts to git by hand predated it (POS.1110,
  POS.1490). For you: on a diverged repository `/save` rebases your
  commits, or you merge by hand; merge requests stay git's.
- A citation of a library document carries no version; the sentence
  that called the version a visible, unguarded pin was written before
  that decision (POS.0970, POS.1020). For you: cite a library document
  by path alone.

## 5.1 - 2026-10-11

### Added
- The forge looks at the remote and offers, it never pulls or merges
  on its own: the `/forge` map and the new command `/pull` ask
  `forge-status --remote` for the state of the engine and of the
  project against its origin and say it as a fact, up to date, behind,
  ahead, diverged or no origin, each state with one offer; `/pull`
  pulls only a clean repository that is behind, and after a pull of
  the engine shows the Action required lines of these notes crossed
  and offers the checks (POS.1490, SOL.0180, THR.0490 closed). For
  you: a clone behind its origin is shown at every map; take the
  upgrade through `/pull` from inside a session or through
  `forge-pull` as before, and nothing is pulled or merged unasked.
- A session ends with `/end`: it says what lives only in the
  conversation and would be lost, an unwritten round, carried
  verdicts, a promise, offers the write, reports every repository with
  unsaved changes and offers `/save`, names stale renders as a fact
  and closes with one sentence saying whether shutting the command
  line loses anything; it writes nothing itself (POS.1500, SOL.0180,
  THR.0430). For you: end a session with `/end` and you know what
  closing the command line loses; the measurement of what a session
  carries stays open, to be stored per user.
- `forge-status --remote` reports the state against the origin
  through a function shared in `forge_repos.py`, and `forge-pull`
  prints the state before, the state after and the commits between
  (SOL.0510). For you: the scripts say what they found and what they
  did.

### Changed
- The step after a pull of the engine is `/pull`, which shows the
  Action required lines crossed and offers the checks (POS.0940). For
  you: after `forge-pull`, run `/pull` instead of running `/check
  light` and `/check project` on each project by hand.
- `/pull` is among the guarded commands, since it changes the disk
  (POS.1090). For you: it runs on your word only.

## 5.0 - 2026-10-10 - approved

This major closes how a thought is found and how the forge is read,
and is the point to pull to, tagged `v5`. Between 4.0 and 5.0 every
artefact got a definition of its elicitation in the state files of
`/forge`, the working methods stand named with their reasons, the
chain grew below the intent to the solution design with the cut
between what is wanted and what realises it, the history of a
document became a log these notes derive from, and the forge explains
itself from its own definitions: the documentation by `/document`,
the scripts in Python, `CONTRIBUTING.md` for feedback. The test of a
major ran on 2026-10-09 and was settled at 4.65: the check
`single-source-of-truth`, both critic lenses and the challenge `cto`;
the major approves the intent as the record of what the principal
holds at this date, the solution design staying a draft at 0.8 and
the open threads open. The sections of 4.1 to 4.65 are folded here;
the detail per version stays in `projects/forge/10-intent.history.md`
and its archive.

### Action required
- Version 5 approved: the forge found and read (POS.0300, THR.0570).
  For you: `v5` is the point to pull to once released; nothing changes
  for a project on 4.x.
- The nine PowerShell scripts are replaced by Python scripts of the
  same names, with the shared modules `forge_repos.py` and
  `forge_tools.py`, and `.claude/settings.json` starts the hook with
  `python` (POS.0830, SOL.0620, THR.0150 closed). For you: PowerShell 7
  is no longer needed; Python 3.8 or newer must be on PATH as `python`
  (on Linux or macOS alias `python3` to it or install
  `python-is-python3`). Where you typed `./scripts/<name>.ps1 -Tag x`,
  type `python scripts/<name>.py --tag x`; `-Engine`, `-Recipe`,
  `-Reference`, `-Template`, `-OutDir`/`-Out` are `--engine`,
  `--recipe`, `--reference`, `--template`, `-o`.
- The engine's `.claude/settings.json` carries a `UserPromptSubmit`
  hook, anchored at the project root so that it does not depend on the
  working directory (POS.1170). For you: after `forge-pull`, restart
  the session once so the hook loads; it adds its lines of context at
  every prompt.
- The history of a versioned document is a log of changes, one line
  per change (CLAUDE.md, Versioning & status; `templates/history.md`;
  POS.0310, SOL.0200). For you: in each project, for every versioned
  document, have Claude move `<file>.history.md` as it stands to
  `<file>.history.archive.md`, untouched, and begin a new
  `<file>.history.md` from `templates/history.md` with its header and
  comment only; the log begins with the document's next version. One
  project at a time, on your word.
- The open threads of a project live in one file beside the intent,
  `threads.md`, and every thread names the artefact it concerns, the
  intent included (POS.0120; CLAUDE.md, Document chain). For you: in
  each thought project, have Claude create `threads.md` from
  `templates/threads.md`, move the section Open threads of
  `10-intent.md` into it word for word and in its order, mark each
  thread with the artefact it concerns, remove the section from the
  intent, verify that the two files together give the old text
  exactly, then bump the intent's version with a history row and set
  the new version in the ledger; a project that already has
  `10-intent.threads.md` renames it to `threads.md` and marks its
  threads at its next write. One project at a time, on your word.
- The commit identity is git's, per host through `includeIf` in your
  `~/.gitconfig` (POS.0950). For you: after `forge-pull`, delete your
  `identities.local.md`; where your repositories carry a local
  `user.name`/`user.email` set by the forge, unset them so your
  includes govern, or keep them, since git lets the local one win;
  `/setup` writes the stanzas and the guard on a new machine.
- The status `in_review` is cancelled; the statuses are `draft`,
  `approved` and `superseded` (POS.0300, REJ.0230). For you: a document
  whose front-matter says `status: in_review` is set to `draft`.
- The locking of a brief is withdrawn: a brief is versioned like every
  artefact, approved at 1.0 and changed after that, mined when the
  principal says so, and no longer among the immutable documents
  (POS.0110, POS.0920, POS.0320). For you: an approved brief stays as
  it is and may be changed from now on; a position mined from a brief
  cites the brief's version at its next write.
- The verdict words of a walkthrough are one set: `accept`, `modify`,
  `reject`, `park`, `obsolete` (POS.0850,
  `.claude/skills/walkthrough/SKILL.md`). For you: in `/check`,
  `accept` now means "do the fix" and `reject` means "leave it as it
  is", the reverse of before; `fix`, `overrule`, `defer` and `leave
  open` are gone.
- A recipe says its format in a `## Format` section; the section
  `## Build instructions` is retired and no longer copied into the
  render (POS.0590, `templates/recipe.md`). For you: at the next
  iteration of a recipe that is to become a file, rename the section
  and give it the three lines of the skeleton; until then `/publish`
  reads the old section and asks for the format.
- A check that finds something leaves a report in `reviews/` and rows
  in the ledger's Findings table (POS.1140). For you: nothing to do in
  a thought project beyond refreshing the ledger's comments from
  `templates/ledger.md` when the `light` check reports them; a library
  receives its Findings table and `reviews/` from `/check` at its first
  finding.
- The migration path names both checks a release runs on a project
  (POS.0940). For you: after `forge-pull`, run `/check light` as well
  as `/check project` on each project.
- The points of Document chain in CLAUDE.md are cited by name and no
  longer by number, and the ledger's `terminal:` left the engine
  (POS.0160, POS.1400). For you: a recipe or a document of a project
  that cites `Document chain 5` or `Document chain 7` cites `Document
  chain, External inputs` or `Document chain, Renders` at its next
  write; the `terminal:` line of a project's ledger header may be
  deleted.
- The skeletons of the reviewers are renamed to one pattern,
  `<type>-definition.md`: `templates/critic-definition.md`,
  `templates/challenger-definition.md` and
  `templates/check-definition.md`, beside the new
  `templates/artefact-definition.md` (POS.1430). For you: a persona, a
  lens or a check of your own is unaffected; a document of yours that
  cites `templates/critic.md`, `templates/challenger.md` or
  `templates/check.md` cites the new name at its next write.
- The solution design has its definition,
  `.claude/skills/forge/states/solution-design.md`, its template,
  `templates/solution-design.md`, and a challenger persona of its own,
  `architect` (POS.1310, POS.0420). For you: run `/challenge architect
  solution-design` once a solution design stands; the readme recipe is
  iterated for the table of artefacts before the next release.
- The command `/document [slug]` generates the documentation of a
  project into `docs/`, pages of one topic each and their index, from
  the map `docs-map.md` beside the ledger (POS.1450, SOL.0460). For
  you: nothing for an existing project; a project's documentation is
  made by `/document <slug>` when wanted.
- `templates/recipe-readme.md` owns what a project's README carries:
  what the project is, what you get, how to start, where it stands,
  documentation; the tables of renders, waiting matters and the layout
  leave for the ledger and the documentation (POS.1450). For you: the
  README of a project follows the new shape at its next `/recipe
  readme`; until then its recipe renders the old one.

### Added
- Every artefact has a definition of its elicitation in seven blocks,
  Target, Inputs, Aim, Partner, Map, Instruments, Course, living in the
  state files of `/forge` and paired with the artefact's template; the
  definitions are used at once and mended where they live (POS.1310,
  POS.1330 to POS.1350, POS.1380, SOL.0120). For you: `/forge brief`,
  `/forge intent`, `/forge assignment` and `/forge solution-design` run
  by their definitions, and what holds for an artefact is read in its
  state file under `.claude/skills/forge/states/`.
- The solution design is an artefact of the chain,
  `40-solution-design.md`, derived from the lowest layer the project
  has above it and made of SOL items with what is open as TBC; an
  intent says what the principal wants and why and does not solve, the
  test of a sentence being whether it would still hold if the thing
  were realised in a wholly different way (POS.1390, POS.1400,
  POS.1420). For you: a project takes the layers it needs, and many
  end at the intent; how a thing is built belongs to the solution
  design, whoever said it.
- How an artefact is composed is the principal's choice, artefact by
  artefact: found together by elicitation, or handed over to Claude,
  who returns a proposal with what he assumed and what he chose
  (POS.1410, CLAUDE.md, Working methods). For you: you can hand an
  artefact over in a word and judge the proposal he returns; nothing
  is derived from it before you have judged it.
- `/new-artefact <name>` adds a new kind of artefact to the forge and
  leads to everything a kind needs: its position in the forge intent,
  its definition and template from `templates/artefact-definition.md`,
  its prefixes, its reviewers and its place in the solution design
  (POS.1430, POS.1090, `.claude/skills/new-artefact/SKILL.md`). For
  you: you alone start it, it decides nothing, and for now it adds to
  the engine, for every user of it.
- The documentation of a project is a set of pages of one topic each,
  for the user, the extender and the evaluator, in five sections
  filled only where the project has material, generated and never
  composed by hand; two kinds of document carry it, `map` (state) and
  `page` (rendering); `/document` runs a planner that writes the map
  and a writer per page, with `scripts/docs-state.py`,
  `scripts/docs-check.py`, `scripts/docs-index.py` and
  `scripts/docs_map.py` behind it (POS.1450, POS.1080, SOL.0460,
  THR.0340 closed). For you: the engine's documentation is in `docs/`,
  its index first; a page mirrors its owner or is derived from the
  project's documents, and is never a source of truth.
- Three working methods stand in the forge for every instance: Step by
  step as its own position, with the birth of a new versioned document
  as such a step and the rule that a remark, a question or a
  counter-thought in answer to "shall I change it?" is not a yes
  (POS.1460); Plain speech, a message opening with the outcome, a
  thread or a position named by what it is with its ID in brackets as
  an address, no invented word for a mechanism (POS.1470); Kind, not
  count, a rule saying what kind of content belongs and never a count
  or a length (POS.1480). For you: Claude's messages open with the
  point and name things in words; a rule he proposes names a kind, not
  a number.
- One write per round among the working methods (POS.1210, CLAUDE.md).
  For you: say it in a word when you want everything agreed so far
  carried to one write at the round's end.
- In pieces (POS.1160). For you: send a long thought in several
  messages and close with "done"; Claude reacts to the whole, not to
  the parts.
- Every proposition closes with the line
  `(a)ccept / (m)odify / (r)eject / (p)ark`, and a single letter
  answers it (POS.0850). For you: type `a`, `m`, `r` or `p` as your
  whole message; every other word of the forge is typed in full.
- `write` orders the bulk write of everything carried in the round
  (POS.1210). For you: say `write` when you want the round written;
  Claude shows you the whole round first and writes on your yes.
- The sign `??` asks for Claude's honest opinion (POS.0860, CLAUDE.md,
  Working methods). For you: end a message with `??` standing alone
  and you get three points at most, marked as Claude's own, with
  nothing written.
- A `walkthrough` skill holds the shape of the walkthrough and the
  elicitation interview (POS.0850). For you: CLAUDE.md is shorter and
  the method is read when one runs; nothing to do.
- `/publish <recipe>` makes the designed `.pptx` or `.docx` from the
  render through a model, into `published/` (POS.0590,
  `.claude/skills/publish/SKILL.md`). For you: you alone start it; it
  converts the Markdown you have read and renders nothing.
- The ledger's Published table says what each published file was made
  from and whether it is `current` or `stale` (`templates/ledger.md`).
  For you: `/forge` shows a published file that is older than its
  render.
- `scripts/md2docx.py`: a Markdown render to Word, through pandoc or
  through a model, styles from a reference `.docx`, `.dotx` or `.dotm`
  named by path, A4 when no reference is given (POS.0590, SOL.0440).
  For you: you install pandoc once and hand recipients a Word file;
  your `.docx` outputs print on A4 without a template, and you can
  point the conversion at a company template as it is; Mermaid
  diagrams arrive as code for now.
- `/man [command or method]`, alias `/manual`: the forge's manual, read
  from CLAUDE.md, the skills and the agents (POS.1190). For you: `/man`
  lists the commands and the working methods, `/man check` shows every
  check and what it looks for.
- `/ingest` takes pasted text, always asks what a source is for, and
  stops before storing personal matter (POS.1040). For you: paste a
  source into the conversation and `/ingest` stores it; expect one
  question per source.
- The check `history` reads a document with its history and proposes
  what moves between them (POS.1140). For you: run it when a document
  is to be cleaned; it moves nothing itself.
- The intent may carry facts as `FCT` items beside positions, on the
  principal's word or with provenance to a source (POS.0230). For you:
  write down what is so without dressing it as a position, and without
  being asked for proof.
- A project declares the language of its documents in its ledger
  header, `language: en` in the template, English when the line is
  absent (POS.0060). For you: a project may now be written in Czech or
  any other language; add the line to a new project's ledger, existing
  ledgers need nothing.
- `templates/decisions.md`, the skeleton of `decisions.md` and of a DEC
  record (POS.1070). For you: a new project gets its decisions file in
  the forge's shape; an existing one keeps what it has.
- `scripts/forge-status.py` opens with the global git configuration
  file git reads. For you: one look tells you where your identity
  stanzas live.
- The per-prompt hook repeats three rules of conduct to Claude: use
  the forge's scripts, explain and ask before running a command of its
  own, change nothing that was not agreed and approved (THR.0400,
  `scripts/hook-walkthrough.py`). For you: Claude is reminded of these
  at every prompt; nothing is enforced yet, so an automatic permission
  mode still lets commands through.
- The forge is open to those who use it, feedback and ideas wanted
  most and a finished change welcome on the forge's own rule, and
  `CONTRIBUTING.md` in the repository root, a render of the new recipe
  `projects/forge/recipes/contributing.md`, says how (POS.1440,
  SOL.0450). For you: you can give feedback, bring an idea or send a
  change you have tried yourself, as `CONTRIBUTING.md` says.
- Three threads stay open at the major: what the documentation leaves
  undecided, the language of a project's pages among it (THR.0590), a
  test of the forge's behaviour, not before 5.0 (THR.0600), and the
  horizon statement the intent lacks (THR.0610). For you: nothing
  changes yet.

### Changed
- A major of the forge intent approves the intent as the record of
  what the principal holds at that date: the package it names is
  finished and goes out, what is open stays open in its thread, and
  the test of a major attests the documents, not the behaviour
  (POS.0300). For you: a major claims nothing about readiness for a
  deployment; what is open is in `threads.md`.
- One model for the whole forge, with two exceptions: the headless
  conversions behind `/publish`, and a mirrored page of the
  documentation on a faster model, chosen by the page's entry in the
  map, a derived page and the planner staying on the session model
  (POS.0930, POS.0530). For you: the strongest model you run the forge
  on is a decision and never an accident of an aged pin.
- A subagent sees the session's whole context, memory included, and
  may take it for the disk: every agent that writes an outward-facing
  file reads CLAUDE.md from disk like every other input, and what it
  wrote is scanned mechanically for instance facts (POS.0950,
  THR.0580 closed). For you: no name, address or host of yours reaches
  a page, a render or a report.
- The staging area of the intent is named for the layer below, not for
  an assignment, and a position without an ID does not exist
  (POS.1340, `templates/intent.md`). For you: the section "Candidate
  structure for the layer below" of an intent holds what the next
  layer will need, whichever layer that is; every position carries an
  ID from the start.
- The project's language covers the artefacts of the chain only;
  ledger, decisions, history, reviews, challenges, indexes, research
  and recipes stay English in every project; the briefs are kept in
  whatever language they are written in, and the demand for British
  English left the Requirement style (POS.0060, POS.0250). For you:
  write a project in your language and keep its bookkeeping in
  English; `/check project` flags a ledger or a decision written in the
  project's language; an assignment of a project in another language
  is written in full, correct sentences of that language.
- A brief holds what the principal chose from the finding, not
  everything the finding yielded, carries no mark of authorship, and
  its usual shape is light: topics with the research beside them,
  composed in a round or two (POS.0110, REJ.0220). For you: `/forge
  brief` leads you to a short brief and leaves the chiselling to the
  intent; a brief carries a citation or a remark only where it matters
  to the thought.
- In the brief's definition Claude forms the record: on the principal's
  word to write he takes what the talk arrived at and writes it down
  so that it is understood, and the brief is the principal's by his
  approval, whoever first said a thought; the Map of a brief names the
  thought and not whose words it is in, and the boundaries are its
  fifth area (POS.1330, THR.0440, THR.0450 closed). For you: a brief
  found together need not be word for word what you said, and before
  the write Claude also asks what you do not want and what is out of
  scope.
- An assignment is complete also when its recipients know the end and
  the reason well enough to act rightly where the plan no longer fits,
  and the questions up front are bounded by their kind, not by their
  number (POS.1350). For you: completeness no longer pulls an
  assignment towards specifying too much; a question on substance
  sends the work back to the intent, however few the questions are.
- A Map names also what is consciously verified, the last area of the
  assignment's Map is named self-containment, and at the walk Claude
  says of each area how it stands, aloud and unrecorded; the questions
  of worth and feasibility are Claude's way of challenging an idea in
  the intent, nothing recorded per idea (POS.1320, POS.1340,
  POS.1350). For you: you hear how each area stands when a Map is
  walked, and no matrix of good and feasible is kept for every idea.
- A change of substance goes into the intent and propagates from there
  down the whole chain the project has, and may come from below, when
  solving shows that what is wanted must change; POS.0140 is the one
  owner of the rule and the method Intent-first names it (POS.0140,
  POS.0900). For you: the intent still changes first, also where the
  change was found while solving.
- How the things wanted are realised moved out of the forge intent
  into the solution design of the forge's project: the positions keep
  what is wanted and why, and the files, scripts and settings that
  realise them are named in its SOL items; what realises an item is
  named in the solution design where the project has one, and no
  longer in the item (POS.0120, THR.0520). For you: to find the file
  that realises a position of the forge, read
  `projects/forge/40-solution-design.md`.
- How `/setup` writes the git identity, where a clone lands and how its
  name is fixed, and what `/ingest` does with a bundle's index moved
  from the intent to the solution design (POS.1050, POS.1060,
  POS.0180, SOL.0150, SOL.0160, SOL.0230). For you: nothing to do; the
  commands run as before.
- From the artefacts of the chain the thing must be buildable without
  the finished product; the solution design stays the architecture,
  and a technical specification is a layer a project takes where the
  one who builds needs the detail (POS.1400). For you: the technical
  specification is not introduced as a layer now.
- An open question of a solution design says whether it blocks
  realisation, and the design is read by whoever realises it, a person
  or an agent (POS.1420). For you: you can tell from its TBC items
  whether a solution design is complete enough to build from.
- An accepted challenge is mended wherever it needs to be, and goes
  above its layer only as a thread, where what is wanted cannot be
  realised or only at a price not worth paying (POS.0440). For you:
  accepting a challenge no longer obliges you to change the intent.
- A thread may arise from any document, a challenge, a finding or an
  item of a layer among them, not from a source alone, and carries its
  origin (POS.0230). For you: a thread that comes from a document
  names that document by path.
- The lens `clarity` judges the scope of every artefact by the Aim of
  its own definition and proposes the move, and its advisory checklist
  is gone (`.claude/skills/critic-contract/SKILL.md`). For you: a
  report of `/critique clarity` no longer closes with a checklist.
- The names of the artefacts left the engine: which artefacts the forge
  has is the listing of `.claude/skills/forge/states/`, CLAUDE.md
  carries the artefact as one kind and speaks of the layers below the
  intent; the README's table of artefacts is rendered from the
  definitions (POS.1080). For you: to see which artefacts the forge
  has, look at the definitions; a layer your project does not have is
  not reported.
- The rules of particular artefacts left CLAUDE.md for the definitions
  in the state files of `/forge`, and a paragraph in Document chain
  says what a definition is; every rule of the operating layer is
  written once and cited elsewhere, the Commands table of CLAUDE.md is
  cut to the purpose of each command, no member of a roster is named
  outside its file, and the critic lenses say their fit in their
  descriptions (POS.1310, POS.1380, POS.1070). For you: read what holds
  for a brief, an intent or an assignment in its state file; CLAUDE.md
  keeps the rule in short and tells you which file owns a mechanism.
- Six positions of the forge intent carry the reason the documentation
  writers found missing, and the intent is cleaned whole: the way to
  an item lives in its records of the log, the table written before
  the log in `projects/forge/10-intent.history.archive.md` (POS.0200,
  POS.0250, POS.0550, POS.1040, POS.1140, POS.1310, THR.0470). For you:
  the intent reads as the current state; the way to an item is in its
  history.
- Release notes are derived from the records of the history log of
  every input history, what you must do carried word for word from the
  record's `Action` (POS.0730). For you: nothing to do; a version
  before the log still comes from its archived Notes.
- A change of the operating layer that touches no item of the intent
  has a subject of its own in the log of the forge's project (POS.0310,
  `templates/history.md`). For you: nothing to do; the subject serves
  the forge's own project.
- The ledger cites and never copies: Waiting on principal cites threads
  and records, and an unfinished conversation is saved into its thread
  (POS.0160). For you: read the ledger for state and follow the ID for
  substance; your own ledgers may be swept the same way at their next
  save.
- `/render` makes the plain file beside the Markdown through pandoc,
  where the recipe names a format, and `scripts/md2pptx.py` and
  `scripts/md2docx.py` each have two engines, `--engine pandoc |
  claude` (POS.0590, SOL.0430, SOL.0440). For you: a Word file or a
  deck for reading is fresh after every render; without pandoc the
  Markdown is made and the file is not; a call without the switch does
  what it did before.
- Finding states in the ledger: `overruled` is now `rejected`, and
  `parked` is new (POS.0440, `templates/ledger.md`). For you: nothing
  to do; the `light` check offers the conversion of your ledger as an
  immediate fix, and an unconverted ledger is read correctly.
- Claude cannot run `git` directly in the engine: `.claude/settings.json`
  denies it in both shells, the scripts stay the only door, and
  commits made through the forge carry no `Co-Authored-By` or
  `Claude-Session` trailer (POS.1200, SOL.0520). For you: the deny
  rules apply from the next session and your own git from the shell
  is untouched; the commit message is the one you confirmed and
  nothing more.
- `/setup` no longer interviews for git identities; it asks the
  conversation language before the role, offers the `includeIf`
  stanzas and the guard, and learns the path of your global git
  configuration from `scripts/forge-status.py`; the clone script sets
  no identity and `/import-project` and `/new-project` propose none
  (POS.1050, POS.0550, POS.1060). For you: one interview less on a new
  machine; a clone reports the identity git resolves, and none
  resolved is caught by `forge-save`.
- The tag `v<major>` is proposed at the release of any repository whose
  intent stands at an integer version, not of the engine alone
  (`.claude/skills/release/SKILL.md`). For you: your own project is
  offered its tag at 1.0, on your word.
- The README says the scripts are the only door to git for Claude and
  for every command of the forge (CLAUDE.md, Persistence). For you:
  nothing forbids you your own git from the shell; the rule binds the
  forge, not you.
- The `project` check no longer verifies a render's provenance against
  the ledger's Renders table, the `light` check does; the `project`
  check no longer reports a stale README or release notes; and a
  one-line reminder that names its owner is not a restatement
  (POS.0570, POS.1070, `.claude/agents/check-project.md`,
  `.claude/agents/check-light.md`). For you: a mismatch is reported
  once, at `/save` as well as at `/release`; `/forge` still shows
  staleness, and `/release` regenerates both regardless; the
  `single-source-of-truth` check still raises repeated steps, rules
  and shapes.
- `/ledger` reports as the bare `/forge` map does, and the `/forge` map
  names the waiting matters in words and the rest as a count,
  recommending in words with the ID as an address (POS.1470). For you:
  the same report from either door, readable without the IDs in your
  head.
- The release skill reports the age of the documentation and offers
  `/document`; the document skill hands a writer its task by path; the
  description of `/setup` names the forge's default model and not its
  name; the examples in the help of five scripts say what the example
  is (SOL.0530). For you: at a release you are told whether the
  documentation is stale; a script's help reads as an example and not
  as a fact of someone's instance.
- The engine's public address has one owner, the pinned facts of the
  readme recipe; the solution design cites it (SOL.0500). For you: the
  address a clone and a project's README point to is read from one
  place.

### Removed
- Five positions of the forge intent that were wholly solution, moved
  to the solution design: the layout of the repository to SOL.0500, the
  protection to SOL.0520, the two conversion scripts to SOL.0430 and
  SOL.0440, the file shape of a command to SOL.0100 (POS.0500, POS.0520,
  POS.0740, POS.1150, POS.1130). For you: nothing to do; what is wanted
  of each stands in the positions that remain.
- `/walkthrough` no longer appears among the commands: the walkthrough
  is a method, not a command (`.claude/skills/walkthrough/SKILL.md`).
  For you: one entry less in the slash menu, nothing to change in how
  you work.

### Fixed
- Wording of the forge intent brought to the chain of today after the
  two critic lenses of 2026-10-09: the solution design and the first
  library exist, the product is the artefact and not the assignment
  alone, intent-first and the birth step are said once each, the lock
  is withdrawn where sentences still named it, and the staging area
  names the recipients of the engine (FND.1220 to FND.1350, POS.0100,
  POS.0600, POS.0620, POS.0700, POS.0970, POS.0860, POS.1380). For you:
  nothing to do; the intent no longer contradicts its own positions.
- A project without a repository is a legitimate shape; the sentence
  that said every project is one is gone (POS.0550, POS.0940). For you:
  you may keep sensitive work local without a finding.
- The single-source-of-truth check of 2026-10-09 settled, sixteen
  findings fixed: the documentation agents share the contract skill
  `docs-contract` and the map has the skeleton `templates/docs-map.md`;
  the ledger skeleton owns the `kind:` header rule and the Renders row;
  `/spinoff` records a spin-off intent-first; the Format section's rule
  stands in `/render` alone; `forge_tools.py` owns what the conversions
  need; dispatchers, reviewer files, reminders, state files and script
  headers cite their owner instead of restating it (FND.1060 to
  FND.1170, FND.0980 to FND.1010, FND.0620, FND.0630). For you: nothing
  to do; a rule is found at its owner.
- The head of the forge's solution design says of its items what holds
  of them, and SOL.0010 names the working methods it realises
  (FND.1310, FND.1340). For you: nothing to do.
- The skills `ingest` and `render` cite CLAUDE.md, Document chain, by
  the item's name and no longer by a number that ceased to exist
  (FND.0970). For you: nothing to do.
- The Essence of the forge intent says the chain ends where the project
  needs it to, in place of the sentence that version 1 ends at the
  assignment (POS.1400). For you: nothing to do.
- The positional arguments of nine skills are counted from zero, as
  Claude Code counts them: `forge`, `recipe`, `render`, `publish`,
  `ledger`, `new-project`, `import-project`, `spinoff` and `man`. For
  you: a command receives its arguments in the right places; `/forge
  brief <name>` no longer takes the name for the state.
- CLAUDE.md opens with the chain starting at the idea put together,
  cites POS.1320 for the walk of a Map and says a recipe carries
  `updated` in place of `date`; the skeletons of the readme and
  release-notes recipes name a language in place of UK English
  (FND.0740 to FND.0820). For you: the README and the release notes of
  your project are no longer told to be UK English.
- `/ingest` settles a changed source in a thought project in the three
  ways the intent has, a new source beside it, the original restored or
  the change knowingly accepted; in a library the sweep moves the
  ledger date and corrects the index entry (POS.0180,
  `.claude/skills/ingest/SKILL.md`). For you: a bare `/ingest` offers
  you all three ways for a changed source.
- The FCT row of CLAUDE.md says apart that a source's fact cites its
  file and that verification is never demanded (POS.0230). For you: a
  fact taken from a source names its file, and no fact has to be
  proved.
- The help and the identity message of the save script no longer set
  the commit identity at a project's creation (POS.0950). For you: the
  script says what the forge does; the identity is git's and the forge
  sets none.
- The checks `light` and `single-source-of-truth` run again, the
  agents `check-engine` and `critic-essence` have their descriptions
  quoted, and every reviewer skeleton says when to quote
  (`.claude/agents/`, `templates/`). For you: `/save` can run its
  check; when you write an agent file, quote a description that
  carries a colon and a space.
- `/new-project` takes a slug and nothing else, as it always did; the
  hint of a working title is gone
  (`.claude/skills/new-project/SKILL.md`). For you: the command's help
  matches what it does.
- The intent's kind names facts beside positions, threads and
  rejections (POS.1080). For you: the kinds table in CLAUDE.md lists
  all four prefixes of the intent.

### Rejected
- A claim of readiness for a company rollout by the major 5.0
  (DEC.0190, CHL.0210). For you: a major closes a package of features
  and sends it out; whom the engine is published for says nothing of a
  rollout date.
- A marking of positions into walls and defaults with a degraded form
  (DEC.0200, CHL.0230). For you: the rules of the forge bind Claude,
  not you; your recorded exception stands in `decisions.md`.
- A recipe per page, the documentation as renders of `/render`
  (REJ.0240); a site or a wiki for the documentation now (REJ.0250); a
  hand-kept file of the philosophy in the project root (REJ.0260). For
  you: the pages are Markdown in the repository, readable without a
  build, and the why is read from the brief and the intent.
- An intent consolidated by Claude held `in_review` until every
  position has been walked through (REJ.0230). For you: a walkthrough
  of an intent runs when you ask for one, and no lower layer waits for
  it.
- A fate recorded for every part of a brief at mining (REJ.0210); marks
  of authorship in a brief (REJ.0220). For you: a brief carries no
  *(Claude)* mark and no per-part bookkeeping.
- A "notes" kind or an intent beside a draft brief (REJ.0180), a
  "parked" kind (REJ.0190), an edit mechanism for large artefacts
  (REJ.0200). For you: nothing changes.
- Stating the caveat on quoting an agent's description once in
  CLAUDE.md; it stays in the three reviewer skeletons (DEC.0180,
  FND.0720). For you: the skeleton a new lens, persona or check starts
  from still tells you when to quote the description.
- Leaving the detection of changed sources to the `project` check alone
  (DEC.0170, FND.0710). For you: a bare `/ingest` goes on reporting
  sources changed since registration and asks what to do with each.

## 4.0 - 2026-09-06 - approved

This major closes the engine's operating layer and is the point to
pull to, tagged `v4`. Between 3.0 and 4.0 the forge gained the two git
doors - `/save` with the `light` check, `/release` from `main` with its
checks, the README and the release notes - the history companions with
a Notes block per row and release notes compiled from them, the
critic's lenses and the checks as rosters of isolated reviewers sharing
one contract skill per kind, the commands as skills, `/setup` and
`/import-project`, and the instance facts split between
`CLAUDE.local.md` and `identities.local.md`. The test of a major ran
before the tag: every check, the `clarity` lens three times and one
CTO challenge, the `essence` lens declined by the principal's word. The
Action required lines below say what to move after pulling: the
Version History tables into companions, a Notes block into every row,
the git identities into `identities.local.md`. The sections of
3.1 to 3.49 are folded here; the detail per version stays in
`projects/forge/10-intent.history.md`.

### Action required
- Every versioned document keeps its Version History in an append-only
  companion `<file>.history.md`, never in its body; `/check` reports a
  table in the body (POS.0310). For you: move the tables of your
  projects into companions, one project at a time; `/check` guides you.
- Version History rows of the intent, the assignment and later layers
  close with a Notes block (POS.0310, `templates/history.md`). For you:
  when you write a version, add the block; rows without one are compiled
  from their prose until you migrate them.
- The release-notes genre skeleton and `/recipe release-notes` take the
  new shape (`templates/recipe-release-notes.md`). For you: run `/recipe
  release-notes` on each thought project; until then its release notes
  keep the old shape.
- The git identities move out of `CLAUDE.local.md` into
  `identities.local.md` beside it (POS.0950). For you: create
  `identities.local.md` from `templates/identities.local.md` with your
  hosts' name and e-mail, delete the Git identities line from
  `CLAUDE.local.md` - or ask Claude to do it; until then `/new-project`
  and `/import-project` find no roster.

### Added
- `/release`: from `main` only, its checks with walkthrough, README and
  release notes, the release commit and the tag (POS.1100,
  `.claude/skills/release/SKILL.md`). For you: one command publishes a
  checked, rendered state.
- `forge-save -Tag <name>`; `v<major>` at every release of an approved
  major (POS.1100). For you: you can tag any commit with `/save -Tag` or
  `/release -Tag`, and a major is always tagged.
- `forge-branch <name>` creates or switches to a branch, `forge-branch
  main` switches back (POS.1110, `scripts/forge-branch.ps1`). For you:
  you can work on a branch without typing git; merging stays yours.
- `/release` offers `critique essence` once; no reviewer runs on its own
  (POS.0400). For you: you get one offer of the drift check before
  publishing and are never surprised by a reviewer.
- `/setup`: creates `CLAUDE.local.md` by interview and
  `.claude/settings.local.json` with the model set to Fable, never
  overwriting (POS.1050). For you: after cloning you run one command
  instead of the manual install steps.
- `/import-project <git-url>` through `scripts/forge-clone.ps1`, into
  `projects/<repository name>` (POS.1060, POS.0550). For you: you bring
  an existing project in with one command.
- The critic has lenses: `clarity` reads each artefact on its own,
  `essence` reads the chain for drift; bare `/critique` lists the roster
  (POS.0400, POS.0410). For you: you can run `/critique essence` to see
  where an assignment drifted from its intent, which the old critic
  never guarded.
- `templates/critic.md`; agents `critic-clarity` and `critic-essence`.
  For you: you add a lens the way you add a persona: copy the skeleton,
  write its Lens section.
- `/critique <lens> [artefact]` and `/challenge <persona> [artefact]`
  take an optional target (POS.0400, POS.0410, POS.0420). For you: you
  can aim a reviewer at one artefact or leave the target off for the
  whole chain.
- Every project gets a README and, a thought project, release notes as
  renders of its own recipes; genre skeletons `readme` and
  `release-notes`, scaffolded by `/new-project` (POS.1000). For you:
  your projects get a README and release notes without writing them.
- An optional `logo.png` in the project root (POS.1010). For you: your
  repository can carry an avatar.
- A project's documents have a kind: five groups, thirteen kinds, one
  table in CLAUDE.md (POS.1080). For you: you can look up what any file
  is, who writes it and whether it is versioned.
- `templates/history.md`; `last_change` in the front-matter of every
  versioned document, written by the write step (POS.0310). For you: you
  create a companion from the skeleton and never write `last_change` by
  hand.
- Prime directive 10: one mechanism lives in one place; a restated
  procedure is a `/check single-source-of-truth` finding (POS.1070). For
  you: what you read in one place is what runs everywhere.
- Step by step as a named working method; an accept recommendation
  carries the concrete text; one research, one question (POS.1030,
  CLAUDE.md). For you: you can invoke Step by step in a word, and an
  accept shows you the text before it is written.
- A Dependencies table in the ledger for documents of other
  repositories; `/check` verifies the paths, `/forge` reports the
  libraries (POS.1020, `templates/ledger.md`). For you: a project's
  reliance on a library document is visible and checked.
- `templates/brief.md` owns the brief's header; `/forge brief`,
  `/new-project` and CLAUDE.md cite it. For you: one place to look up
  what a brief's header must carry.
- `templates/index-bundle.md`; the library reduction of the ledger in
  `templates/ledger.md`. For you: a skeleton exists for a bundle index
  and a library ledger.
- Research `2026-09-05-good-release-notes.md`, how the two standards and
  nine established projects write release notes. For you: you can read
  why this file looks the way it does.
- Research `2026-09-03-version-history-placement.md`. For you: you can
  read why the Version History leaves the document.

### Changed
- Version 4 approved: the engine's operating layer closed as a set
  (POS.0300). For you: `v4` is the point to pull to; the Action required
  lines of this section say what to do after.
- Checks run like the reviewers: `/check <check> [slug]` from a roster
  of one agent per check, four to start - `project`, `light`, `engine`,
  `single-source-of-truth` (POS.1140). For you: `/check` bare shows the
  roster; a new check is one file from `templates/check.md`.
- `/save` runs the `light` check first; `/release` runs `light` and
  `project`, for the engine `engine` too (POS.1140, POS.1100). For you:
  a save catches broken bookkeeping in seconds; the expensive
  restatement sweep runs only when you call `/check
  single-source-of-truth`.
- The release notes are rendered by every `/release`, not by every save
  (release-notes recipe 0.6). For you: your release notes move only when
  you release.
- `/release` without a slug asks which repository (POS.1100). For you: a
  bare `/release` never sweeps all your repositories.
- Renders are regenerated only by `/release` or an explicit `/render`
  (POS.0810). For you: Claude never re-renders behind your back.
- The commands are skills: every command lives as
  `.claude/skills/<name>/SKILL.md`, the state and genre files as
  supporting files beside their dispatcher, `.claude/commands/` gone
  (POS.1130). For you: the slash commands work as before; a local copy
  of the engine takes the move through `forge-pull`; the state and genre
  files no longer appear in the `/` menu.
- The shared behaviour of the critic and the challenger lives in two
  contract skills preloaded into the reviewer files, which carry their
  Lens section only (POS.1120). For you: a new lens or persona is one
  short file from `templates/critic.md` or `templates/challenger.md`; a
  change to the shared behaviour is one edit of the contract.
- The reviewers' contract skills are named `<kind>-contract`:
  `critic-contract`, `challenger-contract`, `check-contract` (POS.1120).
  For you: a new lens, persona or check names its kind's contract by
  that name; the roster shows what they are.
- Every reviewer contract forbids instance facts in a report (POS.0950).
  For you: no name, address or host of yours appears in a review,
  challenge or check.
- The `cto` persona is a CTO in its own right, no longer defined as the
  principal's peer (FND.0250). For you: the persona reads the same
  whoever the principal is.
- The challenger's default target is the whole chain (POS.0420). For
  you: a bare `/challenge cto` reads everything, not the intent alone.
- `/check` reports findings only; informal observations are forbidden.
  For you: a check gives you a list of verdicts to give, nothing else.
- `/check` reports a project without a repository as a fact; a
  local-only project is a legitimate shape (POS.0940, POS.0960). For
  you: you may keep sensitive work local without a finding.
- The staleness of any render other than the README and the release
  notes is never a `/check` finding; the `/forge` map shows it
  (POS.0570, POS.0810). For you: you decide when to re-render a pitch or
  a deck; the check stays quiet.
- Requirement style is the critic's to judge, bookkeeping the `light`
  check's (POS.1140). For you: a style breach comes from `/critique
  clarity`, a broken companion from `/check light`, never both.
- The commit identity is set locally per repository at creation or
  import, proposed from `identities.local.md` by the origin's host
  (POS.0950). For you: you confirm the identity once per repository and
  never inherit a wrong one.
- `/setup` offers `user.useConfigOnly = true` as the one global guard
  (POS.1050); `/import-project` passes `-Name` and `-Email` by default
  (POS.1060). For you: a repository without an identity fails aloud
  instead of committing as someone else.
- `forge-status` reports the current branch (POS.0550). For you: you see
  at a glance which branch each repository is on.
- The repository is `forge-of-thought`, `forge` the project slug
  (POS.0500, POS.0600). For you: you clone `forge-of-thought` and
  address the engine's own project as `forge`.
- `RELEASE-NOTES.md` is one section per release in six fixed groups,
  compiled from the Notes lines; no Unreleased section; an approved
  major opens with highlights (POS.0730, release-notes recipe 0.7). For
  you: you see per release what you must do, what you gained, what
  changed, what is gone, what was fixed and what was rejected, instead
  of a story.
- At an approved major the minors since the previous major fold into its
  section, superseded lines dropped, and their sections leave the
  release notes (POS.0730, release-notes recipe 0.10). For you: after a
  major you read one merged section for the whole span, and go to
  `10-intent.history.md` for the detail per version.
- A Notes line carries both sides - what changed, then what it means for
  the reader (POS.0310, `templates/history.md`). For you: every release
  note tells you the change and its consequence in one breath, never one
  without the other.
- A major's heading in the release notes says "approved" only; a tag is
  named in the highlights where one exists (release-notes recipe 0.8).
  For you: no release note claims a tag that is not in the repository.
- The release-notes recipe and its skeleton name the history companion
  as the fine-grained log (recipe 0.4). For you: the release notes point
  you to the right file for the reasons.
- The release-notes recipe requires the intent's current vocabulary
  (recipe 0.5). For you: release notes no longer pick up words since
  renamed from old rows.
- The genre skeleton names a major's tag in the highlights where a row
  records it (POS.0730). For you: your project's release notes will show
  the tag `/release` set at an approved major.
- `/render` lets the subagent read the previous render when the recipe
  declares it among its inputs. For you: a render such as the release
  notes can carry its earlier sections forward.
- Recipes keep a Version History again, in their companion (POS.0710).
  For you: you can trace how a recipe changed.
- A source has one form: at `/ingest` every binary gets one question,
  convert to Markdown or keep as a functional binary; no `.extract.md`
  sibling; the ledger's Extract column becomes Form (POS.1040,
  POS.0180). For you: you answer one question per binary and get either
  a Markdown source or the binary, never both.
- One shape for every resource index: a bundle index carries the same
  per-file entries as the directory index (POS.0840,
  `templates/index-bundle.md`). For you: every index you open reads the
  same way.
- `templates/index-bundle.md` is the full skeleton `/ingest` creates a
  bundle index from, one entry per file, no table (POS.0840). For you: a
  bundle index you ingest looks like the directory index.
- "Material index" is now "resource index"; "artefact" means a document
  of the chain only, "document" any file (POS.1080). For you: one word
  for one thing when you read CLAUDE.md.
- Authorship is the boundary between chain and render (POS.0710). For
  you: what you compose is a chain artefact; what is generated from it
  is a render.
- Every project README closes with the fixed sentence that maintaining
  needs Forge of Thought (POS.1000). For you: readers of your project
  README learn where the tooling is.
- The engine's own README is exempt from the fixed closing sentence
  (POS.1000). For you: nothing to do.
- The README's Quickstart: a common head, then a new project and an
  existing one; the chain diagram a star with future layers dashed
  (readme recipe 0.27). For you: a newcomer sees the first act of work
  and what does not exist yet.
- The README's "Saving and syncing" describes the two doors (readme
  recipe 0.37). For you: the README tells you when to `/save` and when
  to `/release`.
- The walkthrough runs one item per message, the verdict acknowledged
  before the next; an interview one question at a time (POS.0850,
  CLAUDE.md Working methods). For you: you never face a questionnaire.
- `disable-model-invocation: true` on the seven writing commands and the
  six state and genre files; the state files name their arguments in
  words (POS.1090, FND.0190, FND.0210). For you: Claude can no longer
  run a writing command on its own; only you can, by typing it.
- The reviewer agents and both skeletons list `Edit` among their tools
  (FND.0200). For you: a reviewer can amend its report file instead of
  failing on a write.
- Twelve commands cite the mechanism they use instead of restating it
  (POS.1070). For you: no command drifts from the mechanism it names.
- The conversation-language clause left thirteen commands; CLAUDE.md's
  prime directive 6 is its one owner (FND.0280). For you: nothing to do.
- CLAUDE.md states rules and cites their owners: the skills, agents,
  contracts, templates and script headers own what they do (POS.1070).
  For you: read a mechanism where it runs; CLAUDE.md tells you which
  file that is.
- CLAUDE.md cites the release-notes recipe and `templates/history.md` as
  the owners of the release-notes shape and the Notes block instead of
  restating them (POS.1070). For you: one place to read each rule, the
  skeleton or the recipe.
- POS.1100 alone says what `/save` and `/release` do; POS.0840 alone
  says what a resource index is (FND.0300, FND.0340). For you: one place
  to read each rule.
- What a position carries (POS.0120), what a major of the forge intent
  means (POS.0300), where the chain grows (POS.0700), how any instance
  migrates (POS.0940). For you: after `forge-pull`, `/check project` and
  the Action required lines tell you what to do, and Claude migrates on
  your word.
- What a position carries, made precise: one date, no measurements
  (POS.0120). For you: a position tells you the rule and the day it took
  shape; the numbers and the story are in this companion.
- Nineteen positions of the intent cut to stance, reason and citations
  by the rule of POS.0120, their story left to this companion. For you:
  the intent reads as the current state; the story of a decision is in
  the history row the position names.

### Removed
- `/check-forge`. For you: check the engine with `/check engine`, the
  forge project with `/check project forge`.
- The single `critic` agent and `templates/critique.md`. For you:
  `/critique` without a lens no longer runs anything; it shows you the
  roster.
- The per-host `includeIf` identity model and the `~/.gitconfig-<host>`
  files of 3.6 and 3.7 (POS.0950). For you: nothing is written into your
  `~/.gitconfig` beyond the guard.
- "Frozen" from the assignment's description; the scripts' count from
  POS.0550. For you: nothing to do.

### Fixed
- Thirteen commands and a template had the conversation language
  hard-coded as Czech (POS.0060, POS.0950). For you: the commands speak
  the language you set in `CLAUDE.local.md`.
- `/check` names its own path to the subagent; `/render` carries the
  front-matter block in the subagent prompt; `$ARGUMENTS` in `/research`
  and `/save` (FND.0220 to 0240). For you: the commands pass your arguments
  correctly.
- The `/save` row of the commands table said "no check" (FND of the
  single-source-of-truth check). For you: nothing to do.
- Five positions and two threads said "save" where the procedure is
  `/release`; CLAUDE.md reduced to the two-doors sentence, `release.md`
  owning the procedure (POS.0310, POS.0930, POS.1070, THR.0210,
  THR.0270). For you: what you read about saving and releasing is
  consistent everywhere.
- `release.md` and POS.1000 said what POS.0730 no longer says (a tag on
  the heading; notes distilled). For you: nothing to do.
- POS.1100 says what `/save` and `/release` run since 3.44; four smaller
  alignments of the intent (FND.0350 to 0390). For you: nothing to do.
- Four alignments of the intent after the sweep (FND.0400 to 0430). For
  you: nothing to do.
- Counts, the retired "skeleton" meaning and two typographic slips in
  the intent (FND.0310 to 0330). For you: nothing to do.
- Nine clarity findings of the intent and the ledger (FND.0100 to 0180).
  For you: the intent you read is more consistent.
- The brief's header lists `last_change` (POS.0110, CLAUDE.md); POS.1070
  names the scripts without a count. For you: the brief header you
  scaffold is complete.
- `/check` step 8 and `/save` step 2 aligned with POS.0570. For you: a
  stale render other than the README and the release notes is no longer
  reported to you as a finding.
- THR.0220 states DEC.0090 beside the fact it ruled on; the write-once
  sentence dropped from two genre files; a stale ledger item removed.
  For you: nothing for you beyond consistency.

### Rejected
- A migration tool for third-party instances (DEC.0100). For you: the
  check and the release notes are the tool.
- Stale-only regeneration at every save (REJ.0160); a fixed working
  branch with a forge-side merge (REJ.0170). For you: the forge will not
  grow into a wrapper of git.
- FND.0090 overruled: the scripts' branch capability does not contradict
  the position (DEC.0090). For you: nothing changes in the scripts.

## 3.0 - 2026-08-30 - approved

This major made the engine public. Between 2.0 and 3.0 the forge gained
deck generation through `scripts/md2pptx.ps1`, guided recipe composition
with `/recipe`, the resource indexes, the named working methods with the
walkthrough at their centre, briefs that are composed and then locked
with more than one per project, one model for the whole forge with
`/render` in an isolated subagent, the read-only `forge-status.ps1` and
scripts that run beyond Windows. The brief `public-engine` was mined
into the split: the engine is a public repository `forge-of-thought` of
its own under CC BY 4.0 with a fresh history tagged `v3.0`, every
project a repository of its own under a gitignored `projects/`, no
instance facts in the engine, and library projects for shared material.
For the user of the engine this is the first version that can be cloned,
upgraded through `forge-pull` and kept apart from private work.

### Action required
- The engine is a public repository of its own with a fresh history;
  projects are repositories of their own under `projects/`, gitignored
  (POS.0940, POS.0950,
  `research/2026-08-29-split-migration-runbook.md`). For you: clone the
  engine, keep each project as its own repository under `projects/`, set
  the commit identity in each.

### Added
- The public face: repository `forge-of-thought`, licence CC BY 4.0, the
  author credited (POS.0990, LICENSE). For you: you may use and share
  the engine under attribution.

### Changed
- The forge project's locked brief and both CTO challenges rewritten
  once for the public boundary (POS.0980). For you: nothing
  company-specific reaches you.
- CLAUDE.md, `.gitignore`, scripts, templates and commands rebuilt for
  the split (readme recipe 0.25). For you: the engine you clone works
  stand-alone.

## 2.21 - 2026-08-29

### Added
- The engine/projects split: nested repositories in a gitignored
  `projects/*`, scripts recognising a project by its `.git`, upgrade by
  `forge-pull`, a git tag per approved major (POS.0940). For you: you
  upgrade the engine with `forge-pull` and your projects never collide
  with it.
- No instance facts in the engine: `CLAUDE.local.md`,
  `settings.local.json`, the git identity from your configuration
  (POS.0950). For you: your name, language and identities stay on your
  machine.
- Project kind `thought | library` (POS.0960); the library project with
  its knowingly unguarded cross-repository citation (POS.0970). For you:
  you can keep shared material in `lib-<name>` and cite it by path.

### Changed
- A bare `/ingest` reports changed sources with a question (POS.0180);
  the model lives in `settings.local.json` (POS.0930); a deck template
  is named by path (POS.0740). For you: changed sources are noticed, the
  model is yours to set, templates come from a library.

### Removed
- `local/` (POS.0750, REJ.0140). For you: user-local files move to a
  library project.

### Rejected
- Submodules, subtree, a template repository, copying the engine,
  plugin-only distribution (REJ.0150). For you: the split stays nested
  repositories and nothing else.

## 2.20 - 2026-08-29

### Added
- Brief `00-brief-public-engine.md` locked at 1.0 after the first CTO
  challenge of a brief (CHL.0070 to 0130). For you: you can read how the
  public engine was decided.

### Fixed
- Reviewers no longer pin a model; POS.0400 says "isolated" (POS.0530,
  POS.0930). For you: a reviewer runs on your session model.

### Rejected
- Path-filtered history for the public engine; a fresh history instead,
  the company copy read-only (DEC.0080). For you: the public repository
  starts at 3.0.

## 2.19 - 2026-08-29

### Changed
- A brief's free form means no required structure; a structured summary
  is stored as shown (POS.0110, `/forge brief`). For you: you may write
  a brief with headings, tables and use cases, and what you paste stays
  as pasted.

## 2.18 - 2026-08-29

### Added
- Research notes on framework distribution, Claude Code packaging and
  the engine/projects git separation (`research/2026-08-29-*.md`). For
  you: you can read what the field does and what Claude Code allows.

## 2.17 - 2026-08-27

### Changed
- One model for the whole forge; the agents `model: inherit` (POS.0930).
  For you: everything runs on the session model you chose.
- `/render` generates in an isolated subagent (POS.0930). For you: a
  render is faster and cheaper on any model.

### Rejected
- Per-command pinning to a faster model; a per-recipe `model:` deferred
  (POS.0930). For you: no command silently runs on a weaker model.

## 2.16 - 2026-08-27

### Fixed
- A brief is immutable from its lock, other immutables from creation,
  carried through CLAUDE.md, the commands, the templates and the
  reviewers (POS.0320, POS.0060). For you: every file says the same
  about immutability.

## 2.15 - 2026-08-27

### Changed
- `/forge brief` runs under the principal's moderation; Claude clarifies
  and correlates with reality through `/research` and `/ingest`, never
  adds content (POS.0110). For you: in a brief conversation you steer
  and nothing enters without your word.

## 2.14 - 2026-08-27

### Added
- Briefs redefined: draft while written, locked at 1.0; `/forge brief
  [name]`; more than one brief per project; the ledger's Briefs table
  with a mining state (POS.0110, POS.0920, `templates/ledger.md`). For
  you: you can compose a brief in the forge and add later briefs to a
  running project.

### Changed
- CLAUDE.md, `templates/ledger.md`, the `/forge` map, `/forge intent`,
  `/new-project` and `/check` aligned to the brief's states. For you:
  every command knows a draft brief from a locked one.

## 2.13 - 2026-08-27

### Changed
- The portability rule in CLAUDE.md Persistence; the Windows-flavoured
  examples in `doc2md.ps1` and `md2pptx.ps1` neutralised (POS.0830). For
  you: the scripts' help reads the same on Linux and macOS.

### Fixed
- The heading "Two isolated reviewers"; the ledger header no longer
  calls the ledger the only rewritten file (FND.0060, FND.0080). For
  you: nothing to do.

## 2.12 - 2026-08-27

### Added
- Working methods named in CLAUDE.md: Walkthrough, Propose never decide,
  Elicitation interview, Draft early, Reflect back, Intent-first,
  Recommend do not push (POS.0850 to 0910). For you: you can invoke any of
  them in a word.

### Changed
- `/critique` and `/challenge` end by offering a walkthrough; the README
  gains a Working methods section (readme recipe 0.17). For you: a
  review ends with the first item in front of you.

### Removed
- `/resolve`, without alias (POS.0850). For you: you give verdicts
  inside a walkthrough.

## 2.11 - 2026-08-27

### Added
- Resource indexes: every `sources/` and `research/` carries a freely
  rewritten `00-INDEX.md`, written by `/ingest` and `/research`,
  verified by `/check` (POS.0840, `templates/index.md`). For you: you
  know what a project's sources and research are for without re-reading
  them.

### Changed
- The ledger reduced to registration: Purpose leaves the Sources table,
  a Research table is added (POS.0160, POS.0180). For you: what a
  resource is for lives in one place, the index.

## 2.10 - 2026-08-25

Nothing for the user of the engine.

## 2.9 - 2026-08-25

### Changed
- The forge runs beyond Windows: `scripts/` is cross-platform PowerShell
  7 with nothing Windows-only (POS.0830). For you: you can run the forge
  on Linux and macOS.

## 2.8 - 2026-08-18

### Added
- Five positions from the first CTO challenge: the forge ends where its
  owner is satisfied (POS.0780); isolation is not independence
  (POS.0790); challengers on another model family to come (POS.0800);
  regenerated renders pass under the principal's eyes, recipes pin
  wording (POS.0810); artefacts do not expire with the conventions
  (POS.0820). For you: reviewer agreement is never sold to you as
  validation, and your old artefacts stay valid.

### Changed
- `/save` reports the material delta of regenerated renders (POS.0810).
  For you: you rule on what a re-render changed before it is committed.

### Rejected
- The growth path as a contradiction (CHL.0030, DEC.0060); the meta-work
  as a budgeted work stream (CHL.0060, DEC.0070). For you: nothing
  changes.

## 2.7 - 2026-08-17

### Fixed
- README re-rendered at the current version; the decisions header
  updated; DEC.0050 appended (FND.0010 to 0040). For you: the README title
  matches the version you have.

## 2.6 - 2026-08-17

### Changed
- Release notes continuously current: an Unreleased section on top,
  regenerated at every `/save` of the core (POS.0730, release-notes
  recipe 0.2). For you: the release notes no longer end at the last
  major.
- The README restructured for scannability (readme recipe 0.12 to 0.15).
  For you: you find the challenge, the capabilities and the reference in
  that order.

## 2.5 - 2026-08-17

### Added
- `scripts/forge-status.ps1`, read-only; `forge-save.ps1` prints the
  committed file summary (POS.0550). For you: you can see unsaved
  changes without touching git, and a save shows what it committed.

### Changed
- `/save` determines its scope through `forge-status`; the scripts-only
  door covers reading state (POS.0550). For you: no command calls git
  directly, reading included.

## 2.4 - 2026-08-17

### Changed
- An assignment assigns, it does not solve: the enumerated ban of
  delivery apparatus dropped (POS.0210, CLAUDE.md directive 8, `/forge
  assignment`). For you: you may put a stakeholder matrix or an impact
  analysis into an assignment where it sets direction.

## 2.3 - 2026-08-17

### Changed
- The README overhauled after an external critique (readme recipe 0.10).
  For you: the README tells you how to obtain the forge and shows a real
  requirement.
- The forge dictates only the output language; the conversation language
  is per-instance (POS.0060). For you: your conversation language never
  appears in a render.

## 2.2 - 2026-08-17

### Added
- `/recipe <genre>`: guided composition of a render recipe; first genre
  `presentation` (POS.0770, `templates/recipe-presentation.md`). For
  you: you compose a recipe by interview instead of from a blank
  skeleton.
- A render may serve as an input of another render (POS.0710). For you:
  a slide of yours can cite an architecture picture.

### Changed
- `md2pptx.ps1` gains `-Model` (POS.0740). For you: you choose the model
  for a deck conversion.

## 2.1 - 2026-08-17

### Added
- `scripts/md2pptx.ps1` turns a Markdown deck render into a `.pptx`
  through headless Claude Code (POS.0740). For you: you can hand over a
  PowerPoint file without leaving the forge.
- `local/` for user-local files, gitignored; `.potx` templates by bare
  name (POS.0750; removed at 2.21). For you: your deck templates had a
  home outside git.

### Changed
- Course set for splitting the engine from private projects (POS.0760,
  THR.0130). For you: the engine will become shareable.

## 2.0 - 2026-08-15 - approved

The second baseline reworked how the chain is operated. Between 1.0 and
2.0 `/clarify` and `/draft` gave way to `/forge` with one definition
file per state, renders became a first-class concept with recipes
iterated and outputs generated, the README among them, the challenger
grew into a persona panel with severity and anti-fabrication discipline
that can be aimed at any chain artefact, `/ingest` was reduced to
registration with bundles and `scripts/doc2md.ps1` as the only
conversion path, git persistence arrived with `/save` and the pre-save
check, and the assignment turned from short and airy to complete and
precise. Release notes were introduced with this approval. For the user
of the engine this is the version that works the chain by naming the
artefact wanted and generates its outputs instead of editing them by
hand.

### Added
- `RELEASE-NOTES.md`, rendered from `recipes/release-notes.md`
  (POS.0730). For you: you can read what each version of the system
  brought.

## 1.24 - 2026-08-15

### Changed
- An assignment carries the complete in-scope substance, length whatever
  fidelity requires; "short and airy" dropped (POS.0130, CLAUDE.md
  directive 8). For you: your assignment is as long as the subject needs
  and omits nothing silently.

## 1.23 - 2026-08-15

### Added
- `scripts/doc2md.ps1` (markitdown) as the only document-to-Markdown
  path, with `-Suffix` (POS.0180, `/ingest`). For you: you convert
  documents with one script, and `/ingest` uses it.

## 1.22 - 2026-08-15

### Changed
- `/save` re-renders the README unconditionally on a save touching the
  core (POS.0570). For you: the README is current after every core save.

### Rejected
- Staleness detection for the README (POS.0570). For you: nothing to
  configure.

## 1.21 - 2026-08-15

### Changed
- `/render <recipe>`: the argument relabelled from `<purpose>`. For you:
  the argument's name says what you pass.

## 1.20 - 2026-08-15

### Changed
- `/challenge <persona> [artefact]` may target any chain artefact,
  default `intent` (POS.0420, POS.0450, DEC.0020). For you: you can
  challenge an assignment as well as an intent.

## 1.19 - 2026-08-15

### Changed
- Challenges carry a severity (dealbreaker | major | minor) and a wider
  epistemic scale; anti-fabrication discipline (POS.0420). For you: you
  see how serious each challenge is and how sure the challenger is.

### Rejected
- Proposing rewrites, interactivity, unbounded breadth for the
  challenger (POS.0420). For you: a challenger stays sharp and few.

## 1.18 - 2026-08-15

### Added
- Challenger personas: `/challenge <persona>`, one agent per persona,
  bare `/challenge` lists the roster; first persona `cto` (POS.0400,
  POS.0420). For you: you choose who challenges you.

### Changed
- Challenge files carry the persona in their name. For you: you see at a
  glance which persona wrote a challenge.

## 1.17 - 2026-08-15

### Added
- `/check-forge` gains "Recipes and renders" and `/check` the
  per-project equivalent (POS.0540). For you: your recipes and renders
  are checked for shape, inputs and staleness.

### Changed
- The README's "How it is used" splits into the general flow and a
  worked example (readme recipe 0.2). For you: you see a real project's
  flow.

## 1.16 - 2026-08-15

### Added
- `recipes/readme.md` v0.1; the README rendered for the first time
  (POS.0720). For you: the README is generated, and you change it
  through its recipe.

### Changed
- A recipe's template fixes structure and placement, never wording
  (POS.0710). For you: each render re-derives the words from the current
  inputs.

## 1.15 - 2026-08-15

### Changed
- Recipes exempt from the versioning apparatus (POS.0710; reversed at
  3.21). For you: your recipes carried only a version and a date.
- CLAUDE.md's Ledger section enumerates all ledger tables. For you: you
  can look up every table in one place.

## 1.14 - 2026-08-15

### Added
- `/forge`: bare a state map, `/forge <state>` works on that artefact,
  one definition file per state (POS.0580). For you: you work the chain
  by naming the artefact you want.
- Renders: `recipes/<purpose>.md` iterated, `/render <purpose>`
  generates `renders/<purpose>.md` with provenance;
  `templates/recipe.md`; the ledger's Renders table (POS.0710). For you:
  you iterate the recipe and regenerate the output.

### Changed
- README.md is a render of the forge project (POS.0720); everything the
  forge produces is Markdown (POS.0590). For you: you convert formats
  outside the forge.

### Removed
- `/clarify` and `/draft`, without aliases; `derivatives/`, migrated to
  `renders/`. For you: use `/forge intent` and `/forge assignment`.

## 1.13 - 2026-08-09

### Added
- Derivatives: audience-specific condensations of the intent in
  `projects/<slug>/derivatives/` as dated editions (POS.0710; replaced
  at 1.14). For you: you could keep a pitch or a summary beside the
  chain.

## 1.12 - 2026-08-08

### Removed
- The fixed assignment size limit (POS.0130, CLAUDE.md directive 8). For
  you: your assignment may be as long as the subject needs.

## 1.11 - 2026-08-08

### Changed
- `/ingest` stores, registers and catalogues only; the ledger's State
  column replaced by free-text Purpose (POS.0180). For you: you decide
  how and when each source is used.

## 1.10 - 2026-08-08

### Added
- Every source bundle carries a `00-INDEX.md`, created by `/ingest` when
  missing (POS.0180). For you: a bundle you ingest is catalogued for
  you.

## 1.9 - 2026-08-08

### Added
- Source bundles: `sources/<slug>/` as one source with one ledger entry
  (POS.0180). For you: you can ingest a set of related files as one
  source.

## 1.8 - 2026-08-08

### Changed
- `/new-project` creates `00-brief.md` with the header pre-filled
  (POS.0110). For you: you paste your text into a ready file.

## 1.7 - 2026-08-04

### Changed
- `/save` drafts the commit message unless `-m` is given. For you: you
  confirm a proposed message instead of writing one.

## 1.6 - 2026-08-04

### Added
- `/save`: the scope-routed check, findings settled, then the script
  (POS.0570). For you: you save through one command with the check built
  in.

## 1.5 - 2026-08-04

### Added
- POS.0070: Claude criticises, challenges, inspires and lays out
  options; the principal composes (CLAUDE.md Roles). For you: nothing
  becomes content because Claude proposed it.

## 1.4 - 2026-08-04

### Changed
- OS-level sandboxing dropped for the permission system (POS.0520). For
  you: the shell works on Windows; you approve through prompts and
  allowlists.

## 1.3 - 2026-08-04

### Added
- The pre-save conformance check (POS.0570); shared
  `.claude/settings.json` with the model pin and the permission policy.
  For you: a save through Claude is checked first, and the settings come
  with the clone.

## 1.2 - 2026-08-04

### Added
- Git persistence: `forge-save.ps1` and `forge-pull.ps1`, linear history
  on `main` (POS.0550); `logo.png` as the project avatar (POS.0560). For
  you: you save and sync with two scripts.

## 1.1 - 2026-08-03

### Changed
- The forge's self-description: "a workshop where thought is tempered
  and shaped" (POS.0620). For you: the README no longer presents the
  forge as a machine for assignments.

## 1.0 - 2026-08-02 - approved

The first baseline declared the engine as designed: a chain ending at
the assignment, two independent reviewers, conformance commands and the
write-once-per-round cadence. On the way from 0.1 the forge was reframed
as a general engine usable by anyone with the growth path beyond the
assignment as its primary ambition, gained `sources/` with `/ingest`,
the `/check-forge` and `/check` commands and the `/ledger` report, and
settled that `/challenge` runs before the first draft. For the user of
the engine this is a working engine with a fixed vocabulary and a
process that writes once per round, on confirmation.

Nothing for the user of the engine.

## 0.11 - 2026-08-02

### Changed
- Write once per iteration round for any working conversation, promoted
  to a prime directive (POS.0190). For you: the intent is written at the
  round's end on your confirmation, or whenever you order it.

## 0.10 - 2026-08-02

### Added
- `/check-forge` and `/check [slug]`, advisory and read-only (POS.0540).
  For you: you can check conformance without anything being changed.

## 0.9 - 2026-08-02

### Changed
- "Chaotic" dropped from the tagline and the essence (POS.0600); the
  README's planned extensions match the intent. For you: the forge
  presumes nothing about your thoughts.

### Fixed
- README title typo; a heading level; a REJ.0125 citation. For you:
  nothing to do.

## 0.8 - 2026-08-02

Nothing for the user of the engine.

## 0.7 - 2026-08-02

### Changed
- `/status` renamed `/ledger` (DEC.0030); the expansion intent recorded
  as POS.0700. For you: you call `/ledger` for the state report.

### Removed
- The premature `/elaborate` mechanics (THR.0020, THR.0030). For you:
  nothing to do.

### Rejected
- Back-filling DEC records (DEC.0040). For you: decisions are recorded
  from now on, not retroactively.

## 0.6 - 2026-08-02

### Changed
- `/challenge` runs before the first draft, further runs at the solver's
  discretion (POS.0450, DEC.0020). For you: you challenge once before
  drafting and again when you choose.

## 0.5 - 2026-08-01

### Changed
- `/clarify` writes the intent once per iteration, not per answer
  (POS.0190). For you: you answer freely and see one write at the end.

## 0.4 - 2026-07-31

### Changed
- No dates in source filenames; origin dates best-effort in the ledger;
  a bare `/ingest` sweeps `sources/`; `/status` reports unregistered
  sources. For you: you drop a file into `sources/` under a plain name
  and it gets registered.

## 0.3 - 2026-07-31

### Added
- `sources/` per project and `/ingest`; the ledger's Sources table
  (POS.0180). For you: you can register external inputs in a project.

## 0.2 - 2026-07-31

### Changed
- The forge is a general engine usable by anyone; the growth path toward
  BRD and beyond as the primary ambition, version 1 ending at the
  assignment (00-brief.md). For you: the forge is for your thinking
  whoever you are.

## 0.1 - 2026-07-31

### Added
- The core (CLAUDE.md), the templates and the command set; the group BRD
  conventions and the Forge of Thought naming. For you: you get a
  working engine.
