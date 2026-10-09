---
generated: 2026-10-09
made: mirrored
inputs-hash: f2a5621a930152be
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - CLAUDE.md
---

# See where a project stands

This page is for anyone working in the forge who wants a quick picture of a project: what exists, what can be worked on next and what waits for a decision. Two commands give it: `/forge` and `/ledger`.

## Get the map

Run `/forge` with a project slug, or without one when the project is clear from where you are. If it is ambiguous, you are asked which project you mean.

```
/forge [slug]
```

The forge reads the project's ledger and the list of available target states, then reports compactly:

- **Kind and git.** The project's kind, as the ledger header gives it, and whether it is under git, meaning it has its own repository. "Not under git" is stated as a fact about the project, not as a defect.
- **Artefacts.** Which artefacts of the chain exist, at what version and status. Briefs are listed with their mining state. A draft brief, or one that is `pending` or `partial`, is named as work waiting. A layer the project does not have is not reported as missing.
- **Target states.** Which target states can be worked from here because their inputs exist, and which cannot yet, with what is missing.
- **Stale files.** Which renders are stale and which published files are stale. For published files this is the `stale` state in the ledger's Published table.
- **Libraries.** Which libraries the project needs, from the ledger's Dependencies table, and whether each is cloned alongside.
- **Waiting on you.** What the ledger lists as waiting on the principal.

The report ends with a recommended next step. It is a recommendation, never a gate: you may do something else. Where more than one matter waits on you, the report also offers a walkthrough, which takes them one by one (see [Walk through a list](walk-through-a-list.md)).

## A library's map is shorter

A library is shared material, not a project waiting for a brief. Its map reports the sources and research it holds, from the ledger and the indexes, and stops after the git line. It has no chain, no target states and no next step beyond `/ingest`.

## Read the ledger only

```
/ledger [slug]
```

`/ledger` gives the same report, read from the ledger alone. Give a slug for one project, or none for every project. It only reads and changes nothing.

The ledger can differ from the files on disk. Reconciling the two, meaning versions, files and indexes, is the job of the light check, `/check light`. If `/ledger` meets an obvious discrepancy while reporting, it names it and points you to that check.

For the ledger's tables and the state words, see [Ledger](../reference/ledger.md).

## See also

- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked one by one.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
