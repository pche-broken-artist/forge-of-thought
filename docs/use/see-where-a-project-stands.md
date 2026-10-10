---
generated: 2026-10-10
made: mirrored
inputs-hash: bad86933fab1112e
inputs:
  - .claude/skills/forge/SKILL.md
  - .claude/skills/ledger/SKILL.md
  - CLAUDE.md
---

# See where a project stands

This page is for the person who wants a quick picture of a project: what
exists, what can be worked on next and what waits on them. It covers
bare `/forge` and `/ledger`.

## Ask for the map

Run `/forge` with no state name, and a project slug if the project is
not clear from context. If it is ambiguous, you are asked which one.

The command reads the project's ledger and reports compactly:

- the project's kind, and whether it is under git. "Not under git" is
  stated as a fact, never as a defect;
- the artefacts that exist, with version and status. The briefs come
  with their mining state; a draft brief, or one marked `pending` or
  `partial`, is named as work waiting. A layer the project does not
  have is not reported as missing;
- which target states can be worked from here because their inputs
  exist, and which cannot yet, with what is missing;
- which renders are stale, and which published files are stale (state
  `stale` in the ledger's Published table). How a render becomes stale
  is the render command's to say;
- which libraries the project needs, from the ledger's Dependencies
  table, and whether each is cloned alongside;
- what waits on you: the few live matters named in words, each with its
  ID in brackets as an address, and the rest as a count.

It ends with a recommended next step in words. The recommendation is
never a gate: you are free to do something else. Where more than one
matter waits on you, the report offers a walkthrough of them.

## A library's map

A library is material, not a project waiting for a brief. Its map
reports its sources and research, from the ledger and the indexes, and
stops after the git line. It has no chain, no target states and no next
step beyond `/ingest`.

## Read the ledger only

`/ledger [slug]` gives the same report, read from the ledger alone, for
one project or, with no slug, for all of them. It only reads. It does
not reconcile the ledger with reality (versions, files on disk,
indexes): that is the light check's (`/check light`). If a discrepancy
is obvious while reporting, the command names it and points there.

## See also

- [Walk through a list](walk-through-a-list.md): how the matters waiting on the principal are worked one by one.
- [Ledger](../reference/ledger.md): the ledger's tables and state words.
