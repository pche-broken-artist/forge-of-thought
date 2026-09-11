---
project: <slug>
kind: thought
language: en             # language of the chain's artefacts (ISO 639-1);
                         # English when absent; records, state, research,
                         # recipes and notation stay English
updated: YYYY-MM-DD
---

# Ledger — <Project>

<!-- Single source of truth for state. Freely rewritten (as are the resource indexes,
sources/00-INDEX.md and research/00-INDEX.md); every other document
is versioned or immutable. Keep current after every operation; /ledger
reads from here. Versions per CLAUDE.md, Versioning & status.
Kind: `thought` keeps every table below. `library` (POS.0960) keeps
only Renders, Sources, Dependencies, Research and Waiting on
principal; the Briefs, Documents, Findings and Challenges tables are
deleted at scaffold time. This comment is the one owner of that
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

## Sources
<!-- Registration only. External inputs, immutable once registered.
Date = best-effort origin date; origin: content | file | ingested. What
a source is and is for lives in sources/00-INDEX.md, never here.
Registration does not imply intake. Form (POS.1040): text | extract
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
<!-- State: open | resolved | overruled | obsolete. Resolution: assignment
version for resolved, DEC.NNNN for overruled. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|

## Challenges
<!-- State: open | accepted | rejected | parked | obsolete. Resolution:
intent version for accepted, DEC.NNNN for rejected. -->
| ID | State | Headline | Source review | Resolution |
|---|---|---|---|---|

## Waiting on principal
<!-- Open questions owned by the principal, findings and challenges
awaiting verdict, proposed spin-offs. What blocks the next iteration. -->
- …
