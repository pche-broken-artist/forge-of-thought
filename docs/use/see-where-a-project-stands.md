---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - CLAUDE.md
---

# See where a project stands

This page is for a user who wants to know where a project is and what
to do next. It shows how to get the map of a project with bare
`/forge`, and how to read the same report from the ledger alone with
`/ledger`.

## Get the map

Run `/forge` with the project's slug: `/forge <slug>`. If the project
cannot be inferred from the context and the slug is ambiguous, you are
asked which one you mean.

The command reads the project's ledger and the list of target states,
and changes nothing. It reports, compactly:

- **Kind and git.** The project's kind, as the ledger header gives it,
  and whether it is under git (its own repository is present) or "not
  under git". The latter is a fact, not a defect.
- **Artefacts.** Which artefacts of the chain exist, at what version
  and with what status. The briefs come with their mining state; a
  draft brief, or one marked `pending` or `partial`, is named as work
  waiting. A layer the project does not have is not reported as
  missing.
- **Target states.** Which target states you can work on from here
  because their inputs exist, and which cannot yet, with what is
  missing.
- **Stale outputs.** Which renders are stale, and which published
  files are, as the ledger's Published table marks them `stale`. How
  staleness is decided is not repeated here; it is the business of
  `/render`.
- **Libraries.** Which libraries the project needs, from the ledger's
  Dependencies table, and whether each is cloned alongside.
- **Waiting on you.** What the ledger lists as waiting on the
  principal.

The map ends with a recommended next step. It is a recommendation, not
a gate. Where more than one matter waits on you, the map also offers a
walkthrough of them, in which they are worked one at a time (see
[Walk through a list](walk-through-a-list.md)).

## A library's map

A library is material, not a project waiting for a brief. Its map
reports its sources and research, taken from the ledger and the
indexes, and stops after the git line. It has no chain, no target
states and no next step beyond `/ingest`.

## Read from the ledger only

`/ledger [slug]` gives the same report, read from the ledger only. Give
a slug for one project; give none and it reports every project. It is
read-only.

The ledger may differ from the files on disk. `/ledger` does not
reconcile them; that is the work of the light check, `/check light`. If
a discrepancy is obvious while reporting, it is named and you are
pointed there.

For the ledger's tables and state words, see
[Ledger](../reference/ledger.md).

## See also

- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked one by one.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
