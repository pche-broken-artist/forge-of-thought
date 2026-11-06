---
id: THR.0780
concerns: intent
origin: the principal
status: open
---

The forge's own project as a repository of its own, so that a user
clones the engine without the workshop. The principal's word of
2026-11-01, after the release of 6.8 and with the rollout among
colleagues running: whoever pulls the engine to use it does not
develop it and needs none of the briefs, the research, the reviews,
the sources or the threads of `projects/forge`; he asked first for a
production branch and a development branch, then, told that nothing
a user runs reads `projects/forge`, proposed the simpler cut: the
forge's own project becomes a git repository of its own, like every
other project, the last exception to POS.0940 removed. The research
of 2026-10-10
(`research/2026-10-10-a-user-only-distribution-of-the-engine.md`)
advised against a filtered branch for reasons that have since moved:
the ledger is made at read time (POS.1600), so a tree without the
workshop no longer fails the checks, and real users exist. What was
read in the engine on 2026-11-01: the user's commands (`/forge`,
`/save`, `/pull`, `/render`, `/research`, `/ingest`, `/check light
<slug>`) touch nothing of `projects/forge`; `/man` reads `docs/` and
names an open thread of the forge's project only where the forge has
nothing, a soft pointer; the hook and the walkthrough skill cite
POS.0850 as an address. The author's commands do read it: `/check
engine`, `/document` bare, `/release forge`, `/new-artefact` and the
renders of README, release notes and CONTRIBUTING, which keep working
on a clone that has the project beside the engine, the release then
landing in two commits. What the cut changes in the engine:
`.gitignore` loses `!projects/forge` and the ledger line; the
`projects/forge` lines of `.gitattributes` move into the project's
own file, the shape `templates/gitattributes` has; `forge_repos.py`,
`forge-ledger` and `forge-check`, which read "forge" as the engine's
project and exclude the directory from the project list; and the 84
documentation pages, the README and the release notes, which cite
`projects/forge/...` by relative path, dead on GitHub unless the
workshop is a public repository of its own and the citations point
into it. Open: whether the workshop goes public; whether its history
is cut out with it (`git subtree split`) or the new repository starts
clean with the old history left in the engine's past; the order of
the cut. To be explored as a round over the intent, one position at
its end, with THR.0230, which asks whether the forge can be split
into an engine and the rest, read beside it. Opened 2026-11-01.

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
