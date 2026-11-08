---
id: THR.0780
concerns: intent
origin: the principal
status: open
---

The forge's own project as a repository of its own, so that a user
clones the engine without the forge's own project. The principal's word
of 2026-11-01, after the release of 6.8 and with the rollout among
colleagues running: whoever pulls the engine to use it does not develop
it and needs none of the briefs, the research, the reviews, the sources
or the threads of `projects/forge`; he asked first for a production
branch and a development branch, then, told that nothing a user runs
reads `projects/forge`, proposed the simpler cut: the forge's own
project becomes a git repository of its own, like every other project,
the last exception to POS.0940 removed. The research of 2026-10-10
(`research/2026-10-10-a-user-only-distribution-of-the-engine.md`)
advised against a filtered branch for reasons that have since moved: the
ledger is made at read time (POS.1600), so a tree without the forge's
own project no longer fails the checks, and real users exist. What was
read in the engine on 2026-11-01: the user's commands (`/forge`,
`/save`, `/pull`, `/render`, `/research`, `/ingest`, `/check light
<slug>`) touch nothing of `projects/forge`; `/man` reads `docs/` and
names an open thread of the forge's project only where the forge has
nothing, a soft pointer; the hook and the walkthrough skill cite
POS.0850 as an address. The author's commands do read it: `/check
engine`, `/document` bare, `/release forge`, `/new-artefact` and the
renders of README, release notes and CONTRIBUTING, which keep working on
a clone that has the project beside the engine, the release then landing
in two commits. What the cut changes in the engine: `.gitignore` loses
`!projects/forge` and the ledger line; the `projects/forge` lines of
`.gitattributes` move into the project's own file, the shape
`templates/gitattributes` has; `forge_repos.py`, `forge-ledger` and
`forge-check`, which read "forge" as the engine's project and exclude
the directory from the project list; and the 84 documentation pages, the
README and the release notes, which cite `projects/forge/...` by
relative path, dead on GitHub unless the forge's own project is a public
repository of its own and the citations point into it. Decided
2026-11-07 in one round (POS.1980): the boundary, the engine is what a
user clones, CLAUDE.md, `.claude/`, `scripts/`, `templates/`, `docs/`,
`tests/`, the root files and `tmp/`, and the forge's own project is the
whole of `projects/forge`, one project among the others, special only in
that its root renders land in the engine; the name, the forge's own
project, "workshop" dropped; public, a repository of its own named
`forge` beside the engine under the same account; a clean start, the
history the engine's; `forge` in the commands of git names the whole;
the order of the cut. Read beside THR.0230, which asks a different
question: this cut parts the project from the engine with the forge
framework on it, not the engine from the framework; the exercise of the
day, every file a user clones sorted by layer, is
`research/2026-11-07-engine-and-forge-framework-by-file.md`, THR.0230's
material. The static analysis of the cut, every place the engine treats
`projects/forge` specially, classified, is `tmp/cut-manifest.md`,
working material, no source of truth; the dry run on a clone without the
project found no hole on the user's path. Open: the cut itself, the
scripts' change recorded in the solution design when it is made; the
thread closes at the first release in the new shape. Opened 2026-11-01.

2026-11-08: the cut planned in detail, the plan's tables in
`tmp/cut-plan.md` beside the manifest (working material). The course:
the engine prepared on a branch of its own, `cut-forge-project`, `main`
left quiet for the users of the rollout until the merge; the scripts
changed so that `forge` means the engine and, where `projects/forge` is
a repository of its own, that project too, so the branch works before
the cut and after it and the cut itself is git alone; the texts
(CLAUDE.md, the skills `release`, `save`, `pull`, `migrate`, the recipes
readme and contributing, POS.0940) on the same branch, the engine's
`.gitignore` and `.gitattributes` untouched until the cut, so that the
project keeps `merge=ours` on its renders meanwhile; the cut rehearsed
on a copy of the engine with a bare repository as a false origin; then
the merge into `main`, the project's repository born, the engine letting
the directory go in a `forge-save forge` of two commits; then the first
release, 7.0 on the principal's approval, which closes this thread and
settles FND.3900. Decisions waiting on the way: the tag of a major on
the engine alone (recommended) or on both repositories; whether `main`
stays quiet; the approval of 7.0; the wording of the project's first
commit.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
