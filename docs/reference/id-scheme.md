---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 91ee53b0126fd335
inputs:
  - CLAUDE.md#ID scheme
---

# ID scheme

This page states the format of the IDs that name the items of a project, the rules that number them and the table of their prefixes. It is for the user, the extender and the evaluator who need the scheme exactly.

## Format

An ID has the form `PREFIX.NNNN`.

- The prefix is three letters.
- `NNNN` stands for the number. It has four digits as long as the number fits, and a fifth digit only beyond 9999.
- No zero is added to an existing ID.
- Every sorting of IDs is numeric, by prefix and then by number.

## Stability

IDs are global and stable. They are never renumbered.

The one exception: when two items carry one number, the younger is renumbered, with a record.

Items may move between groups without a change of ID.

## Numbering

- Items are numbered in tens (`REQ.0010`, `REQ.0020`).
- Each new group starts at the next hundred (`REQ.0100`, `REQ.0110`).
- Overflow takes the next free number anywhere.
- Groups are plain headings: they carry no IDs, no metadata and no lifecycle.
- Depth is at most two levels.

## Prefixes

The principal is whoever's thinking is being forged. The BRD is the business requirements document, one artefact of the chain. The ledger is the state of a project, made at read time.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment, BRD |
| CON | constraint: deliberate boundary, not to be challenged | assignment |
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
| THR | open thread: unresolved matter to elicit next; names the artefact it concerns and carries its origin (as the intent's definition has it) | the project's `threads/`, one file per thread |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact: what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, including rejected findings and challenges | decisions.md |

## See also

- [Stable IDs](../about/stable-ids.md): why IDs are never renumbered, and how the one exception is settled.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
