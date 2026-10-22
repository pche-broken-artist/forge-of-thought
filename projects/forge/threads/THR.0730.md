---
id: THR.0730
concerns: intent, solution-design
origin: sources/github-issues/issue-3-repo-detection.md
status: closed
---

A project directory and its repository are two things: the scripts
must ask git where the repository is, not test `projects/<slug>/.git`
and assume the project is its top. Opened 2026-10-21.

Reported 2026-10-21 by a contributor (GitHub issue #3, the source):
his forge project is a subdirectory `specs/` of the repository of
the thing it specifies, reached through a symlink from
`projects/<slug>`; every script says "not under git", /save, /pull,
forge-branch and forge-migrate refuse or skip it, and forge-ledger's
`tracked` guard, seeing no repository, writes over a ledger.md the
outer repository tracks. Nine sites verified on main (forge_repos
46, 206, 215; forge-status 49; forge-branch 59; forge-migrate 147,
472, 562; forge-ledger 81, 468, 586; docs-state 149). Underneath a
second assumption: pathspecs relative to the project directory,
.gitignore and .gitattributes written there.

Direction accepted 2026-10-21, reversed 2026-10-22: one helper
asking `git rev-parse --show-toplevel`; the engine required to be
the top of its repository; `proj` and `repo` kept apart in every
script; pathspecs relative to the repository; the forge managing a
project inside another's repository.

Decided the same day on the way and written 2026-10-21: GitHub
issues enter the project as a growing bundle
`sources/github-issues/`, one file per issue, each immutable from
its registration, the bundle's index rewritten; POS.0180, SOL.0230,
CLAUDE.md External inputs and the Commands table, the ingest skill
(`--bundle`), the light check and the bundle skeleton.

Decided 2026-10-22, written at intent 5.29 and solution design 0.37
(POS.0550, POS.1740, SOL.0510, SOL.0680, SOL.0800, SOL.0830,
CLAUDE.md Persistence, the skills migrate and import-project): the
forge's git acts only on a repository the forge owns whole, and a
project inside another's repository is not that. Two sentences
replace the direction of the day before. A project is a repository
of its own when git names its directory as the top, resolved paths
compared, never a `.git` looked for; everything else, a directory of
another's repository or no git at all, is a project outside git, on
which the forge runs no git and asks the repository above it
nothing, not even what it tracks (the guard condition of
`sources/repo-detection-challenge-2.md`): the owner who built the
layout runs git himself. The migration runs without git, since a
project outside git is a property, not a defect: none of the refusals
of git, no `--undo`, the user's backup before `--apply`, a run that
stops midway finished by running it again; the first release's
migration refused every project outside git while the ledger script
sent such a project to the migration, a dead end none of the ten
challenges of the cutover plan saw. What the first release of the
engine had already protected, the hand-kept ledger of the old shape
(pull request #2), is what made the question of the other's index
unnecessary. The way through the round: a map of nine layouts and
every operation showed that only three things change, the detection,
the migration without git and one sentence; the principal's measure
for the rest, as little mechanism around git as possible.

The challenge of the proposal (`sources/repo-detection-challenge.md`,
six points) settled 2026-10-22: point 2 taken (a run that stops
midway is finished by running again, written into POS.1740 and
SOL.0800); point 5 taken (the import sentence reworded, the skill
import-project); point 3 confirms the resolved paths, nothing
changed; points 1 and 4 made moot by the simplification, since the
other's index is not asked and there is no refusal to test; point 6
does not apply, docs-state resolving the repository once per run
for one file. No REJ written for 1, 4 and 6: none is a direction
dropped, the first two fell with the simplification and the third
misreads the code (the principal's judgement on this stands open).

What the contributor gets against what he asked: the detection as he
proposed and the dead end of the migration opened; not the forge's
save, pull and branch acting on his repository.

Closed 2026-10-22: the scripts built and saved on main at c71285a
(forge_repos.own_repo, the `.git` tests gone from status, branch,
migrate, ledger and docs-state, forge-migrate without git, the
`tracked` guard of forge-ledger for the forge's own repository only),
tested on a copy of the fixture without a repository (dry run,
`--apply`, the ledger, `--undo` refused, a second run with nothing to
do), the copy removed; the light check's one finding fixed
(FND.2340); the contributor answered in the issue and the issue closed
by the principal. What stays for later lives in the solution design:
`fixture.py --no-git` when the fixture script is built (SOL.0830).
