---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 2ae97f4024ce1948
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

The ID scheme is the format and the numbering rules by which every item of a project's documents is named, with the table of prefixes. This page is for anyone who reads or writes items and needs the exact form: the user, the extender and the evaluator. The principal is the person whose thinking is being forged. The ledger is the file that holds a project's state.

## Format

An ID has the form `PREFIX.NNNN`.

- The prefix is three letters.
- The number is four digits.
- IDs are global and stable. They are never renumbered.
- An item may move between groups without a change of ID.

## Numbering rules

| Rule | What holds |
|---|---|
| Tens | Items are numbered in tens, for example `REQ.0010`, `REQ.0020`. |
| Next hundred | Each new group starts at the next hundred, for example `REQ.0100`, `REQ.0110`. |
| Overflow | When a group runs out of numbers, the next free number anywhere is taken. |
| Groups | Groups are plain headings: no IDs, no metadata, no lifecycle. |
| Depth | Depth is at most two levels. |

## Prefixes

| Prefix | Meaning | Lives in |
|---|---|---|
| `REQ` | requirement | assignment |
| `OOS` | out of scope / do-not | assignment |
| `CON` | constraint, a deliberate boundary, not to be challenged | assignment |
| `ASM` | assumption | assignment |
| `DEL` | deliverable, which may delegate work ("produce NFRs and return") | assignment |
| `TBC` | open question / to be confirmed, with owner | assignment, solution design |
| `SOL` | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| `SCR` | success criterion, optional or delegated | assignment |
| `POS` | position the principal currently holds | intent |
| `THR` | open thread: an unresolved matter to elicit next; it names the artefact it concerns and carries its origin, which is the principal's word (the default, unmarked), a document by path, or Claude's synthesis | the project's `threads.md` |
| `REJ` | rejected direction, with the reason it was dropped | intent |
| `FCT` | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| `FND` | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| `CHL` | peer-review challenge (substance) | ledger, challenges |
| `DEC` | decision, including rejected findings and challenges | `decisions.md` |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
