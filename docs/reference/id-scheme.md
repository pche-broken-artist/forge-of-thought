---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: dae9b80e1d5c8b97
inputs:
  - CLAUDE.md#ID scheme
  - .claude/reference/id-prefixes.md
---

# ID scheme

This page states the format of an ID in the forge, the rules that
number it and the table of prefixes. It is for the user, the extender
and the evaluator who need the exact form of an ID and the place where
the items of a prefix live.

## The format

An ID has the form `PREFIX.NNNN`.

- The prefix has two or three letters.
- `NNNN` stands for the number: four digits as long as the number
  fits, a fifth only beyond 9999 (`POS.10000`).
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

## Stability

IDs are global and stable. They are never renumbered.

The one exception: two items with one number. The younger is
renumbered, with a record.

Items may move between groups without a change of ID.

## Numbering

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- Overflow takes the next free number anywhere.
- Groups are plain headings: no IDs, no metadata, no lifecycle.
- Depth is at most two levels.

## The prefixes

`/new-artefact` writes the row of a new prefix into this table's
owner, the file `.claude/reference/id-prefixes.md`.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment, BRD |
| CON | constraint - deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment, BRD, work specification |
| DEL | deliverable - may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, BRD, solution design, work specification |
| SOL | part of the solution - what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion - optional or delegated | assignment, BRD |
| BR | business requirement - one rule of the business, testable, citing the REQ or POS it carries | BRD |
| UC | use case - behaviour agreed as a sequence, at user-goal level | BRD |
| DEP | dependency - what the BRD relies on outside itself | BRD |
| NFR | non-functional requirement - a quality by category, its value the stakeholders' or a TBC | BRD |
| US | user story - behaviour seen from outside, with its acceptance criteria, citing the BR, NFR, UC, DEP or POS it serves | user stories |
| POS | position the principal currently holds | intent |
| THR | open thread - one matter set aside to be taken up later; names the artefact it concerns and carries its origin, its owner and its priority | the project's `threads/`, one file per thread |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact - what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. rejected findings and challenges | decisions.md |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered, and how the one exception is settled.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
