origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a critique of the work product `work/collaboration-cutover.md` (the plan of the five releases of the brief `collaboration`, made 2026-10-17 from its specification 0.2); translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Critique of the cutover plan

The plan is complete against the design and the order of the
releases agrees with DEC.0210. What is missing are the dependencies
between steps and two closings weaker than the risk of their step:

## Missing steps

- The fixture. Eight steps close "on the fixture" (R1.10, R1.12,
  R2.02, R2.05 to R2.09, R3.02 and on), but the fixture is born
  nowhere. A step R1.00: a test project with an origin, two
  branches, histories of both shapes, a DEC with a Verdict, threads,
  an index, a render and a published companion; the throwaway clone
  for R1.02 and R2.01 from it.
- A tag before the migration. `--undo` holds only until the first
  `/save`; after the push the only way back is a tag. R1.13 and
  R1.25: `forge-save --tag pre-r1` on every project before `--apply`
  (and the same before R5).
- The entries of the map before `/document`. R1.24 renders the
  documentation, but nobody authors the new and regenerated entries
  of `docs-map.md` (SOL.0460 names them). A step before R1.24; the
  same in R2.11.
- Release 3: `/release` calls forge-land (R3.02 has forge-save only)
  and the release-notes recipe tolerates a version without content
  changes (SOL.0530); neither has a step.
- Release 5: `/setup` sets `blame.ignoreRevsFile
  .git-blame-ignore-revs`; the file alone local git does not honour
  (GitHub does). And `md2video.py` reads a screenplay's answers line
  by line ("hard-wrapped" in the skeleton is for the player); verify
  before the conversion what it does with one sentence per line, or
  take the screenplays out of A2, they are scores, not prose to
  merge.

## Closings and order

- R1.09 cannot close as written. The script reads the new shape
  (threads as files, states in records); over today's projects of
  the old shape it gives no Findings, Challenges or Waiting. The
  test is: migrate a throwaway clone of every project (R1.13
  `--apply`), run the script and diff against the original hand-kept
  ledger. So R1.09 depends on R1.13, not the other way round, and
  both belong right after the fixture, since R1.16 and R1.21 stand
  on the script's output.
- R1.13 closes with a "dry run", which is little for a script that
  rewrites every project: `--apply` and `--undo` on a throwaway
  clone, then a dry run everywhere.
- R1.17 before R1.16. If the skills stop writing the ledger before
  the definitions write the records, the engine's project is without
  state in between. Both steps in one go, or the records first.
- R2.06 and the version token. The record of a `/merge` verdict
  carries `+` "since it belongs to the landing", but `+` and `landed`
  are R3. In the second release it carries the current version as a
  state record; from the third `+`. One sentence, or the builder
  invents it.
- R2.12, test 2 (the same artefact, different positions, the version
  raised) fails by definition before R3; let the closing "results
  recorded" say "test 2 expectedly red until the third release".
