# Collaboration cutover

The building of the operating layer for the brief `collaboration`: the
preparation and the first release now, the second and the fourth
deferred and their form decided after the first release from how it
works, the third optional (DEC.0250, THR.0710). The way and the why:
`work/collaboration-cutover.spec.md`. States: todo, doing, done,
dropped. The order of the rows is the order of building; an id is an
address, keeps the prefix of the release it was born in and does not
change when a row moves. Dependencies: the second release needs the
first, the third the second, the fourth the first and its trigger, a
second author writing into a project or a second clone of the same
author with a branch in flight. What touches nothing the migration
migrates is built first, the preparation, shipped by its saves on
main and the tag pre-r1, not by a release of its own (DEC.0260). The
first release is then built on main, in one stretch, with no work on
the projects between its sittings and no pull of the engine on the
second machine until its release (DEC.0230, DEC.0240); estimated at
five to seven sittings; the way back is the tag `pre-r1`, taken
immediately before the first commit of the shape. Worked by hand since 2026-10-17
(`sources/cutover-plan-critique.md`,
`sources/cutover-challenge-review.md`, DEC.0230,
`sources/cutover-challenge-review-2.md`, DEC.0240, DEC.0250).

## Preparation, before the stretch: what touches nothing the migration migrates

| id | step | part | files | closes with | state |
|---|---|---|---|---|---|
| R1.01 | filing by the command: the ledger step leaves the two contracts, `/critique` and `/challenge` number and file the report as `/check` does | SOL.0300, SOL.0330 | critic-contract, challenger-contract, critique, challenge skills | a critique run and filed | done |
| R1.18 | unique names of reports | SOL.0810 | critique, challenge, check skills | two runs on one day | done |
| R1.08 | the fifth digit: the regular expressions and the numeric sort in the scripts, the text NNNN in CLAUDE.md, the templates and the skills | SOL.0790 | scripts/forge-history.py, scripts/docs_map.py, CLAUDE.md, templates, skills | check engine; forge-history on an existing ID | done |
| R1.12 | the push of an ahead repository; the registration check | SOL.0780, SOL.0740 | scripts/forge-save.py, scripts/forge-status.py, scripts/forge_repos.py | a save and a status on the fixture | done |
| R1.14 | `/setup`: the registration of `ours`, the backend, renormalize, rerere; `author:` in the instance file | SOL.0740, SOL.0150 | setup skill, templates/CLAUDE.local.md | a run on this machine | done |
| R1.28 | `/ingest` asks what a source is for before the entry is written | SOL.0750 | ingest skill | an ingest on the fixture | done |
| R1.00 | the fixture by hand, once: a bare remote in `tmp/fixture.git` and one project `projects/fixture` cloned from it by the principal's git, a copy of a small real project's files in the old shape; on it `--apply`, `--undo` and the test of `ours` run; the fixture script, the shapes and the skip by name deferred (DEC.0250) | SOL.0830, TBC.0050 | none; the principal's git | the project cloned, forge-status clean | done |
| R0.01 | `/document`, `/release` on main: an ordinary release, no migration, no Action; dropped 2026-10-18 (DEC.0260): the preparation ships by its saves and the tag, the documentation and the release notes catch up at the first release | SOL.0530 | docs/, README.md, RELEASE-NOTES.md | the release pushed | dropped |

## Release 1, on main in one stretch: the project file, the header, the ledger at read time, threads as files, the attributes with ours and binary, the registration, unique names of reports, the migration

| id | step | part | files | closes with | state |
|---|---|---|---|---|---|
| R1.26 | the engine's tag before the first commit of the shape, R1.03; the projects take theirs in R1.25, each before its migration; the way back is the principal's git, the engine and every project together (DEC.0230) | SOL.0800 | the engine | `forge-save forge --tag pre-r1` on main, on the last commit of the preparation and before R1.03 (DEC.0260); done 2026-10-19: the tag on 638dd10, nothing committed, the tag pushed to origin | done |
| R1.03 | the project file: the template; CLAUDE.md prime directive 6, the `project` row of Document kinds and the layout | SOL.0670 | templates/project.md (new), CLAUDE.md | check engine; done 2026-10-19: the template with the header and a comment only, the ledger template's header left for R1.09, no project carrying the file until its migration | done |
| R1.04 | the header fields leave the templates; CLAUDE.md Versioning & status names the fields that stay | SOL.0700 | templates/intent.md, brief.md, assignment.md, solution-design.md, recipe.md and the genre skeletons, index.md, work.md, docs-map.md; CLAUDE.md; the one clause of the work skill | check engine; done 2026-10-19: index-bundle.md unchanged, its date and origin facts of the bundle written once; "only on main" left to R3.04; the projects' documents carry the fields until their migration | done |
| R1.05 | the state records: the mined and state records of the history, the Verdict field of a decision, the index fields date, origin, form, the archive's shape | SOL.0690 | templates/history.md, decisions.md, index.md, ledger.md; the one sentence of CLAUDE.md, External inputs | check engine; done 2026-10-19: index-bundle.md unchanged, a bundle's fields in its entry of the sources index; the ledger template's table comments say where each column is read from, the rest of it R1.09 | done |
| R1.06 | threads as files: the template; CLAUDE.md ID scheme (the THR row), the `thread` row of Document kinds and the layout; the old threads template dropped; the history template's `Was` of a closing thread dropped | SOL.0720 | templates/thread.md (new), templates/threads.md (dropped), templates/history.md, CLAUDE.md | check engine; done 2026-10-19: the projects' threads.md stays until the migration (C1) | done |
| R1.07 | the attributes: the template with `ours` and `binary`, the engine's own list, `.gitignore` with the engine's ledger | SOL.0730, SOL.0500 | templates/gitattributes (new), .gitattributes, .gitignore, CLAUDE.md (the layout) | check project; done 2026-10-19: the check does not know the attributes until R1.19, so it verifies that nothing broke; the behaviour of `ours` is R1.02's; the ignore of the ledger takes effect at R1.23 | done |
| R1.13 | the migration script: the marks, the steps A, B0, B, C1, D, the undo, the refusals, the manifest | SOL.0800 | scripts/forge-migrate.py (new) | `--apply` and `--undo` on the fixture, then a dry run over every project in place; no clone of a real project (DEC.0240); done 2026-10-19: both run on the fixture, the dry run over the six other projects clean; the whole hand-kept ledger goes to the archive, the manifest lives in tmp/, the author is the handle of the instance file | done |
| R1.09 | the ledger script: eleven kinds read, the tables of the template, the Waiting rule, the reports, the archive, degrading aloud | SOL.0680 | scripts/forge-ledger.py (new), scripts/forge_docs.py (new, shared with forge-migrate; forge-history in R1.11), templates/ledger.md (the Waiting rule, the Reports section), CLAUDE.md (the layout, Portability) | run over the migrated fixture and with `--out tmp/<slug>-ledger.md` over every project in place, the script refusing to write a tracked `ledger.md`; the output differing from the hand-kept ledger only in Waiting from the rule, lines named unrecognised and origins guessed, the old tables read as the archive, everything else equal (TBC.0050); done 2026-10-19: the fixture's ledger made from the migrated shape, the dry run over the six other projects equal to the hand-kept ledgers but for Waiting by the rule, the index's words for a date's origin and the research notes' own derived_from; the Reports section named the specification's own TBC.0020 as a number already taken, settled the same day by renumbering it TBC.0090 (the specification's record of 0.7) | done |
| R1.10 | the project file read by the scripts | SOL.0670 | scripts/forge_repos.py, scripts/forge-clone.py | the help and a clone of the fixture; done 2026-10-19: `project_file` in forge_repos the one reader, forge-clone, forge-ledger and forge-migrate read through it; a clone of a copy of the fixture's remote reported the shape before the migration | done |
| R1.11 | version and date computed from the records; the previous map taken from git | SOL.0700 | scripts/forge-history.py, scripts/docs_map.py, scripts/docs-state.py, the document skill (step 1) | docs-state and forge-history run; done 2026-10-19: forge-history's head line carries the version and the date of the last record, `docs-state --previous` writes the committed map through forge_repos, /document calls it | done |
| R1.23 | the engine's own project migrated, right after the two scripts and the scripts that read the new header, so that the rest of the release exercises the new shape on a real project at every save | SOL.0800 | projects/forge | `python scripts/forge-migrate.py forge --apply` directly, the skill being R1.19; no checks, `/release` runs them in R1.24 | todo |
| R1.29 | the origins of the engine's 35 threads: a walkthrough over the script's printed guesses, by hand, the default "the principal" being most often wrong exactly here | SOL.0800 | projects/forge/threads/ | the thread files saved | todo |
| R1.17 | threads as files and the state records in the definitions and the contracts; in one go with R1.16 | SOL.0690, SOL.0720 | states/intent.md, walkthrough, end, work, publish, ingest, research skills (ingest, research and the index fields added 2026-10-19 at R1.05), the three contracts, check-engine and docs-planner agents (added 2026-10-19 at R1.06, they name threads.md) | check engine | todo |
| R1.16 | the 26 skills stop writing the ledger; the map, `/ledger`, `/end` and the two checks call the script | SOL.0680 | the 26 writing skills, ledger, forge, end skills, check-light, check-project agents | check single-source-of-truth | todo |
| R1.02 | test `ours` under rebase on the fixture, after the attributes and the registration exist | TBC.0050 | none; the fixture | green: recorded in THR.0650; red: stop, back to SOL.0530, TBC.0050 open, the release does not run | todo |
| R1.15 | `/new-project` and `/import-project`: the project file, the attributes, `threads/`; `forge-clone` reads the project file | SOL.0160 | new-project, import-project skills | a scaffold in tmp/ | todo |
| R1.20 | the refusals when behind or diverged; the save on a failed ledger build | SOL.0530, SOL.0460, SOL.0420 | release, document, publish, save skills | check engine | todo |
| R1.27 | `/release` writes `renders/state.md` from the ledger script | SOL.0530, POS.1650 | release skill | a release on the fixture leaving the render | todo |
| R1.21 | the readme recipe reads the ledger script's output | SOL.0680 | templates/recipe-readme.md, the projects' readme recipes | a render of the engine's README | todo |
| R1.19 | `/migrate`: the skill; `/pull` Action required; the map and the writing skills refusing the old shape, `/forge` and `/recipe` reading the project file in place of the ledger's header (SOL.0670, added 2026-10-19 at R1.03), the last code step before the release; the map's last word, the state against the origin (POS.1710), done 2026-10-19 (FND.2030) | SOL.0800, SOL.0670 | migrate skill (new), pull, forge skills, check-project agent, CLAUDE.md Commands | check engine | todo |
| R1.24 | `/document`, `/release` on main; the marks of the first release turned over; the release notes' Action: migrate every project, nobody in two before the second release; and for whoever pulls the engine: `forge-pull`, `/setup`, then every project he keeps pulled if migrated elsewhere, migrated there on one clone if not | SOL.0530, SOL.0800 | docs/, README.md, RELEASE-NOTES.md, 40-solution-design.md | the release pushed; the planner of `/document` makes the map's new and regenerated entries, no step of its own | todo |
| R1.25 | every other project migrated, one clone each, the tag immediately before its `/migrate`, then saved | SOL.0800 | the projects | `forge-save <slug> --tag pre-r1`, `/migrate <slug>`, `/save <slug>` per project | todo |
| R1.22 | the release's checks | — | — | dropped 2026-10-17 (CHL.0390): `/release` runs the checks itself | dropped |

## Deferred (DEC.0250, THR.0710): the rows kept with their ids, their form decided after the first release

### Release 2, collaboration: the driver, /merge, the worktree, the version as a boundary

| id | step | part | files | closes with | state |
|---|---|---|---|---|---|
| R2.02 | the driver: the three cases by path, the keys, the union, the conflicts in standard markers, the ordering rule, the shape verified, one release back tolerated | SOL.0750 | scripts/forge-records.py (new) | the three cases and their conflicts on the fixture | todo |
| R2.03 | the attributes of way 2 in the template and the engine's list | SOL.0730 | templates/gitattributes, .gitattributes | check project; a merge on the fixture | todo |
| R2.04 | `/setup` registers the driver | SOL.0740 | setup skill | a run on this machine; forge-status clean | todo |
| R2.01 | a stub driver under rebase on the fixture, after the attributes of way 2 and the registration exist: the backend, the reversal of ours, renormalize | TBC.0050 | none; the fixture | green: recorded in THR.0650; red: stop, back to SOL.0740, TBC.0050 open, the release does not run | todo |
| R2.05 | the merge script: both directions, the source by where the branch lives, no commit, the conflict list, the commit and the push, the merge on a refused push | SOL.0820 | scripts/forge-merge.py (new) | a merge in each direction on the fixture | todo |
| R3.01 | the history template: the `+` token and the `landed` record | SOL.0760 | templates/history.md, CLAUDE.md Versioning & status | check engine | todo |
| R3.02 | the landing script; `forge-save` lands first, before the add | SOL.0760 | scripts/forge-land.py (new), scripts/forge-save.py | a landing on the fixture | todo |
| R3.06 | `/release` lands first, through the same script as the save | SOL.0760, SOL.0530 | release skill | check engine; a release on the fixture | todo |
| R3.03 | versions computed from `landed`; `N unlanded records` reported as a state | SOL.0760 | scripts/forge-history.py, scripts/forge-ledger.py | the fixture | todo |
| R3.04 | the write step: `+` on a branch, joining the landing on main; `v<base>+N` in a provenance | SOL.0760 | states/*.md, walkthrough, render, research skills, the critic and challenger contracts | check engine | todo |
| R3.07 | the release-notes recipe tolerates a version without content changes | SOL.0530 | recipes/release-notes.md | a render after a state-only landing | todo |
| R2.06 | `/merge`: the skill with the walkthrough of conflicts and the `changed` record of every verdict with `+` | SOL.0820 | merge skill (new), CLAUDE.md Commands and Persistence | a conflicting merge on the fixture settled | todo |
| R2.07 | the worktree and the end of a branch; `<slug>@<branch>` as a slug | SOL.0770 | scripts/forge-branch.py, scripts/forge_repos.py | a worktree made, saved and ended on the fixture | todo |
| R2.08 | `/save` with a slug for two windows; the map's `slug, branch name` | SOL.0770 | save, forge skills | check engine | todo |
| R2.09 | `forge-save` pulls a merge commit by merge, never by rebase | SOL.0530 | scripts/forge-save.py | a save after a merge on the fixture | todo |
| R2.10 | CLAUDE.md Persistence: the four ways, the driver, the worktree, the roles, the promise | SOL.0730, SOL.0820 | CLAUDE.md | check engine, single-source-of-truth | todo |
| R2.13 | the allocation over the local branches: `forge_repos` lists the branches and the highest number per prefix, file by file over the refs; the write step takes the maximum plus the step | SOL.0790 | scripts/forge_repos.py, walkthrough skill, states/*.md | two branches of the fixture each opening a thread, a decision and a position, the second allocating after the save of the first, no duplicate after the merge; the highest number read per file, the thread files, decisions.md and the intent alike | todo |
| R2.14 | the remedy of an ID clash: `/merge` runs the ledger script after the merge and settles a duplicate in its walkthrough, the item of the branch that landed second renumbered by the allocation, the record, a thread's file renamed, the citations corrected; the light check reports a duplicate as a finding | SOL.0820, SOL.0790, POS.0220 | merge skill, check-light agent | the race run once on the fixture: both branches allocating before either saves, the duplicate shown by the script, the remedy run, no duplicate after | todo |
| R2.12 | the four tests of THR.0650 on the fixture, the first without a tolerated collision, the long-branch test among them | TBC.0050 | none; the fixture | all four green, else the release does not run; results recorded in THR.0650 | todo |
| R2.11 | the release's checks; `/document`; `/release`; the marks of the second release turned over; the Action for every other machine: `forge-pull` of the engine, `/setup`, `/pull` of every project | SOL.0530 | docs/, README.md, RELEASE-NOTES.md, 40-solution-design.md | the release pushed | todo |
| R3.05 | the release's checks; `/document`; `/release`; the marks turned over; the long-branch test again | SOL.0530, TBC.0050 | docs/, README.md, RELEASE-NOTES.md, 40-solution-design.md | dropped 2026-10-17 (DEC.0220): merged into R2.11 and R2.12 | dropped |

### Release 3, optional, when nothing is in flight: one sentence per line

| id | step | part | files | closes with | state |
|---|---|---|---|---|---|
| R5.01 | the conversion script: its name, the traps of Markdown, the proof by pandoc's syntax tree | SOL.0710, TBC.0060 | scripts/<name>.py (new) | a dry run over the engine proven by the syntax tree; a screenplay's player events file equal before and after | todo |
| R5.02 | the light rule: a line does not carry two sentences | SOL.0710 | check-light agent | a run | todo |
| R5.03 | the wrapping rule of CLAUDE.md and the render skill's line | SOL.0710 | CLAUDE.md Document kinds, render skill | check engine | todo |
| R5.08 | `/setup` sets `blame.ignoreRevsFile .git-blame-ignore-revs`, since local git does not honour the file alone | SOL.0710 | setup skill | a run on this machine | todo |
| R5.04 | the migration's conversion step: the branch check, `--abandon`, the mark `wrapping: sentences`, the commit through forge-save and the hash into `.git-blame-ignore-revs` by a second save | SOL.0800 | scripts/forge-migrate.py | `--apply` on the fixture of shape N-1, then a dry run on every project | todo |
| R5.05 | every branch of every project landed or given up; the engine's fork told | SOL.0800 | the projects and their origins | forge-status on every clone: no branch in flight | todo |
| R5.09 | the engine's tag before its own conversion | SOL.0800 | the engine | `forge-save forge --tag pre-r3` | todo |
| R5.06 | the engine and its project converted; the checks | SOL.0710 | the engine, projects/forge | light, project, engine, single-source-of-truth clean | todo |
| R5.07 | the release's checks; `/document`; `/release`; the marks turned over; every other project converted on one clone, the tag immediately before; the Action for every other machine: `forge-pull` of the engine, `/setup` (the blame file among its registrations), `/pull` of every project | SOL.0530, SOL.0800 | docs/, README.md, RELEASE-NOTES.md, 40-solution-design.md, the projects | the release pushed; `forge-save <slug> --tag pre-r3` then `/migrate <slug>` per project; `fixture.py` taught the new shape and keeping the previous; THR.0690 closed | todo |

### Release 4, on the trigger of a second author or a second clone with a branch in flight: the blocks of IDs

| id | step | part | files | closes with | state |
|---|---|---|---|---|---|
| R4.01 | the reservation file: the template; `/new-project` creates it | SOL.0790 | templates/ids.md (new), new-project skill | check project | todo |
| R4.02 | the allocation from the author's block; the refusal where none matches | SOL.0790 | walkthrough skill, states/*.md | a write on the fixture | todo |
| R4.03 | the overlap check: block over block, block over a used number | SOL.0790 | check-project agent | a run | todo |
| R4.04 | CLAUDE.md ID scheme: the free number within a block | SOL.0790 | CLAUDE.md | check engine | todo |
| R4.05 | the engine's and the projects' `ids.md`: a block per author, by the integrator | SOL.0790 | projects/forge/ids.md, the projects | a save | todo |
| R4.06 | the release's checks; `/document`; `/release`; the marks turned over; the Action for every other machine: `forge-pull` of the engine, `/setup`, `/pull` of every project | SOL.0530 | docs/, README.md, RELEASE-NOTES.md, 40-solution-design.md | the release pushed | todo |
