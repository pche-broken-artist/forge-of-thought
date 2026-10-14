---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: dd09da901c0627f4
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

The ID scheme is the format and the numbering rules by which every item of the forge's documents is named, with the table of the prefixes. It is for the user, the extender and the evaluator who need the exact rules. Terms of the forge are defined in the [Glossary](glossary.md); the reason IDs are never renumbered is in [Stable IDs](../about/stable-ids.md).

## Format

- An ID has the form `PREFIX.NNNN`.
- Every prefix has three letters.
- IDs are global and stable. They are never renumbered.
- Items may move between groups without a change of ID.

## Numbering

- Items are numbered in tens: `REQ.0010`, `REQ.0020`.
- Each new group starts at the next hundred: `REQ.0100`, `REQ.0110`.
- Overflow takes the next free number anywhere.
- Groups are plain headings: no IDs, no metadata, no lifecycle.
- Depth is two levels at most.

## Prefixes

The principal is whoever's thinking is being forged. The ledger is the file that is the single source of truth for a project's state.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint: deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment, work specification |
| DEL | deliverable: may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, solution design, work specification |
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion: optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread: unresolved matter to elicit next; names the artefact it concerns and carries its origin: the principal's word (the default, unmarked), a document by path, or Claude's synthesis | the project's `threads.md` |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | `decisions.md` |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
