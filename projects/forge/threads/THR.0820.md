---
id: THR.0820
concerns: intent, solution-design
origin: the principal
status: closed
---

`/save` flattened a merge made by hand: it pulled with rebase before
every push, and a rebase drops a merge commit and replays, one by
one, every commit the merge brought in. The contributor of pull
request #8 met it on 2026-11-06: after merging the engine's main
into his branch, the save began replaying the engine's thirteen
commits onto his fork and stopped at a conflict; he aborted it and
pushed the merge by hand. The integrator after a merge of a branch
into main stands in the same place, the remote unchanged and the
branch merely ahead, and CLAUDE.md, Persistence, promises him that
he merges with git itself and saves. What the thread must settle:
when the save may rebase at all. Opened 2026-11-07.

Closed 2026-11-08: two tests on the fixture reproduced both cases,
the integrator's merge of a branch into main and a contributor's
merge of the main into a branch, the merge commit gone after the
save; `forge-save` now rebases only where `forge_repos.remote_state`
says the histories diverged after its fetch and pushes a branch
merely ahead as it stands, the two tests green with the rest of the
suite; POS.1690 and SOL.0780 brought to it (intent 6.17, design
0.57).

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
