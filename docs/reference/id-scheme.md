---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: fb7f45a65ec0c0f4
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

This page states the format of the IDs that name every item of a project, the rules that number them and the table of prefixes. It is for anyone who reads or writes items: the principal (the person whose thinking is forged), an extender and an evaluator. For the reasons behind the rules, see [Stable IDs](../about/stable-ids.md). For any term of the forge, see the [Glossary](glossary.md).

## Format

An ID is written `PREFIX.NNNN`.

- The prefix is three letters.
- `NNNN` stands for the number. In the templates and in the skills it is written the same way.
- The number has four digits as long as it fits. A fifth digit comes only beyond 9999 (`POS.10000`).
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

## Stability

- IDs are global and stable. They are never renumbered.
- The one exception: two items that carry one number. The younger is renumbered, and the renumbering is recorded.
- Items may move between groups without a change of ID.

## Numbering

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- On overflow, an item takes the next free number anywhere.
- Groups are plain headings: they carry no IDs, no metadata and no lifecycle.
- Depth is two levels at most.

## Prefixes

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment, BRD |
| CON | constraint: a deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment, BRD, work specification |
| DEL | deliverable: may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment, BRD, solution design, work specification |
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on | solution design |
| SCR | success criterion: optional or delegated | assignment, BRD |
| BR | business requirement: one rule of the business, testable, citing the REQ or POS it carries | BRD |
| UC | use case: behaviour agreed as a sequence, at user-goal level | BRD |
| DEP | dependency: what the BRD relies on outside itself | BRD |
| NFR | non-functional requirement: a quality by category, its value the stakeholders' or a TBC | BRD |
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

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
