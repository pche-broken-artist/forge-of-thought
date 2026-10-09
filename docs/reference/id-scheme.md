---
generated: 2026-10-09
made: mirrored
inputs:
  - CLAUDE.md
---

# ID scheme

This page is the reference for the IDs that items carry in the forge's
documents: their format, the rules for numbering them and the table of
prefixes. It is for anyone who reads, extends or evaluates the forge.

## Format

An ID is written `PREFIX.NNNN`. Every prefix has three letters. IDs
are global and stable and are never renumbered. Items may move between
groups without a change of ID.

## Numbering

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- Overflow takes the next free number anywhere.
- Groups are plain headings: no IDs, no metadata, no lifecycle.
- Depth is two levels at most.

## Prefixes

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint, a deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment |
| DEL | deliverable, may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, solution design |
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion, optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread, an unresolved matter to elicit next; names the artefact it concerns and carries its origin: the principal's word (the default, unmarked), a document by path, or Claude's synthesis | the project's `threads.md` |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | `decisions.md` |

## See also

- [About stable IDs](../about/stable-ids.md): why IDs are never renumbered.
