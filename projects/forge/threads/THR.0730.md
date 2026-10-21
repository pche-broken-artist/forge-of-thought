---
id: THR.0730
concerns: intent, solution-design
origin: sources/github-issues/issue-3-repo-detection.md
status: open
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

Direction accepted 2026-10-21 (to be written into the intent): one
helper in forge_repos asking `git rev-parse --show-toplevel`; a
project inside the engine's own tree with no repository of its own
is "not under git", the engine itself required to be exactly the
top of its repository (the contributor's exclusion compared the
top with ENGINE_ROOT literally, which a copied engine under another
git would pass); `proj` and `repo` kept apart in every script as
forge-migrate already does for the engine's project; pathspecs
relative to the repository; .gitignore and .gitattributes stay in
the project directory, git honouring both below it. POS.0550's
"every project a repository of its own" widens to "or a directory
of one"; CLAUDE.md Persistence's "recognised through
projects/<slug>/.git" changes with it.

Decided the same day on the way and written 2026-10-21: GitHub
issues enter the project as a growing bundle
`sources/github-issues/`, one file per issue, each immutable from
its registration, the bundle's index rewritten; POS.0180, SOL.0230,
CLAUDE.md External inputs and the Commands table, the ingest skill
(`--bundle`), the light check and the bundle skeleton.

State 2026-10-21: open. Next: the intent round (POS.0550,
POS.1200), the solution design (forge_repos, the five
scripts), CLAUDE.md Persistence and External inputs, the ingest
skill; then the scripts, tested on the fixture with a project that
is a subdirectory of a repository; the contributor told in the
issue when the thread exists.
