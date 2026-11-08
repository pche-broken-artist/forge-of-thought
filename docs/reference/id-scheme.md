---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: a730f379f07433f8
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

The ID scheme is the format and the numbering rules by which every item of the forge is addressed, with the table of prefixes. This page is for the user, the extender and the evaluator who need the format and the table exactly. For a term of the forge not glossed here, see the [Glossary](glossary.md).

## Format

An ID has the format `PREFIX.NNNN`.

- The prefix is two or three letters.
- `NNNN` stands for the number: four digits as long as the number fits.
- A fifth digit comes only beyond 9999 (`POS.10000`).
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

## Stability

IDs are global and stable. They are never renumbered.

The one exception: two items with one number. The younger is renumbered, with a record.

Items may move between groups without a change of ID.

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
| OOS | out of scope / do-not | assignment, BRD |
| CON | constraint, a deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment, BRD, work specification |
| DEL | deliverable, may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, BRD, solution design, work specification |
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion, optional or delegated | assignment, BRD |
| BR | business requirement: one rule of the business, testable, citing the REQ or POS it carries | BRD |
| UC | use case: behaviour agreed as a sequence, at user-goal level | BRD |
| DEP | dependency: what the BRD relies on outside itself | BRD |
| NFR | non-functional requirement: a quality by category, its value the stakeholders' or a TBC | BRD |
| US | user story: behaviour seen from outside, with its acceptance criteria, citing the BR, NFR, UC, DEP or POS it serves | user stories |
| POS | position the principal currently holds | intent |
| THR | open thread: an unresolved matter to elicit next; names the artefact it concerns and carries its origin | the project's `threads/`, one file per thread |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | decisions.md |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered, and how the one exception is settled.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
