---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: ef85bb7c59f13194
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

This page states the format of an ID, the rules for numbering items and the table of prefixes, for anyone who reads, writes or checks the items of a project. Terms of the forge are explained in the [Glossary](glossary.md).

## Format

An ID has the form `PREFIX.NNNN`.

- The prefix is three letters.
- `NNNN` stands for the number, here and in the templates and skills.
- The number has four digits as long as it fits. A fifth digit is used only beyond 9999 (for example `REQ.10000`).
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

IDs are global and stable. They are never renumbered. Items may move between groups without a change of ID. The reasons are on [Stable IDs](../about/stable-ids.md).

## Numbering

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- Overflow takes the next free number anywhere.
- Groups are plain headings: they carry no IDs, no metadata and no lifecycle.
- Depth is two levels at most.

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
| THR | open thread: an unresolved matter to elicit next; names the artefact it concerns and carries its origin, which is the principal's word (the default), a document by path, or Claude's synthesis | the project's `threads/`, one file per thread |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | `decisions.md` |

The principal is the person whose thinking is being forged. The ledger is the file that holds the state of a project.

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
