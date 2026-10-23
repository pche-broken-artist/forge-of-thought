---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: 7826e80fe88194ae
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

This page is the reference for the IDs that mark the items of a project: their format, the rules that number them and the table of prefixes. It is for anyone who reads, writes or checks items that carry an ID. The principal is the person whose thinking is forged, and the ledger is the state report that is made from the documents when it is read.

## Format

An ID has the format `PREFIX.NNNN`.

- The prefix is always three letters.
- `NNNN` stands for the number. It has four digits as long as the number fits. A fifth digit is used only beyond 9999 (`POS.10000`).
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

## Stability

IDs are global and stable. An ID is never renumbered.

The one exception is two items that carry one number. The younger item is renumbered, and the renumbering is recorded.

Items may move between groups without a change of ID.

## Numbering rules

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- Overflow takes the next free number anywhere.
- Groups are plain headings. They have no IDs, no metadata and no lifecycle.
- Groups nest to a depth of two levels at most.

## Prefixes

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint, a deliberate boundary not to be challenged | assignment |
| ASM | assumption | assignment, work specification |
| DEL | deliverable, which may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, solution design, work specification |
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion, optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread: an unresolved matter to elicit next; it names the artefact it concerns and carries its origin, which is the principal's word (the default), a document by path, or Claude's synthesis | the project's `threads/`, one file per thread |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | decisions.md |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered, and how the one exception is settled.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
