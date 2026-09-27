---
project: <slug>
kind: thought
language: en             # language of the chain's artefacts (ISO 639-1);
                         # CLAUDE.md, prime directive 6
terminal: assignment     # where the chain ends — CLAUDE.md, Ledger
updated: YYYY-MM-DD
---

# Ledger — <Project>

<!-- Single source of truth for state: CLAUDE.md, Ledger. Versions
per CLAUDE.md, Versioning & status. /ledger reads from here.
Kind: `thought` keeps every table below. `library` (POS.0960) keeps
only Renders, Sources, Dependencies, Research and Waiting on
principal; the Briefs, Documents, Published, Findings and Challenges
tables are deleted at scaffold time. This comment is the one owner of that
reduction (POS.1070). -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md). Status:
draft (being composed, editable) | approved (locked at 1.0, immutable).
Mined: pending | partial | mined | dropped — how far the intent has
absorbed it; Note says what remains (partial) or the REJ (dropped). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | 0.1 | draft | pending | — |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 0.1 | draft | YYYY-MM-DD |
| 20-assignment.md | — | not started | — |

## Renders
<!-- Generated outputs, one row per recipe in recipes/ (CLAUDE.md,
Document chain 7). Row mirrors the render's front-matter provenance. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|

## Published
<!-- Designed files made by /publish, one row per file (CLAUDE.md,
Document chain 7). State: current | stale — set to current by
/publish, to stale by every /render of that recipe. -->
| File | Recipe | From render | Model | Published | State |
|---|---|---|---|---|---|

## Sources
<!-- Registration only. External inputs, immutable once registered.
Date = best-effort origin date; origin: content | file | ingested. What
a source is and is for lives in sources/00-INDEX.md, never here
(CLAUDE.md, Document chain 5). Form (POS.1040): text | extract
of <original> | binary — one form per source. -->
| File | Date | Date origin | Form |
|---|---|---|---|

## Dependencies
<!-- Registration only. Documents of other repositories this project
relies on — typically library documents (POS.1020): cited by path from
an index entry, a recipe or the chain. No version: library documents
are maintained by their owner. What the document is for lives where it
is used (the index entry, the recipe). -->
| Path | Library | Used by | Note |
|---|---|---|---|

## Research
<!-- Registration only. Immutable dated notes written by /research (or
recorded expert estimates). What a note answers lives in
research/00-INDEX.md, never here. -->
| File | Date | Derived from |
|---|---|---|

## Findings
<!-- State: open | resolved | rejected | parked | obsolete. Resolution:
assignment version for resolved, DEC.NNNN for rejected. `overruled`
in an older record reads as `rejected`. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|

## Challenges
<!-- State: open | accepted | rejected | parked | obsolete. Resolution:
intent version for accepted, DEC.NNNN for rejected. -->
| ID | State | Headline | Source review | Resolution |
|---|---|---|---|---|

## Waiting on principal
<!-- What waits on the principal, one line per matter: cite, never
copy — CLAUDE.md, Ledger. -->
- …
