---
project: <slug>
kind: thought
language: en             # language of the chain's artefacts (ISO 639-1);
                         # CLAUDE.md, prime directive 6
updated: YYYY-MM-DD
---

# Ledger — <Project>

<!-- Single source of truth for state: CLAUDE.md, Ledger. Versions
per CLAUDE.md, Versioning & status. /ledger reads from here.
kind: thought | library; a ledger without it reads as `thought`: at
an import that is a fact the command reports, at a check a finding
with the one-line fix (the one owner of this rule).
Kind: `thought` keeps every table below. `library` (POS.0960) keeps
only Renders, Sources, Dependencies, Research and Waiting on
principal; the Briefs, Documents, Published, Work, Findings and
Challenges tables are deleted at scaffold time; the Findings table returns with
a check's first finding (`.claude/skills/check/SKILL.md`). This
comment is the one owner of that reduction (POS.1070).
`ledger.archive.md`: the hand-kept ledger's Briefs, Work, Findings
and Challenges tables as they stood at the migration, immutable,
read for every item without a record of the new shape, a newer
record overriding (POS.1610). -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md). Status:
draft (being composed) | approved (1.0 and on, changed after that as
any artefact is).
Mined: pending | partial | mined | dropped — how far the intent has
absorbed it; Note says what remains (partial) or the REJ (dropped).
Mined and Note are read from the mining record of the intent's
history (templates/history.md). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | 0.1 | draft | pending | — |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 0.1 | draft | YYYY-MM-DD |
<!-- One row per layer below the intent, added when the layer is
born; a layer the project does not have gets no row (CLAUDE.md,
Ledger). -->

## Renders
<!-- Generated outputs (CLAUDE.md, Document chain, Renders): one row
per rendered recipe, written by /render step 6 at the first render
and kept by every later one, the row mirroring the render's
front-matter provenance. The documentation index has a row too,
written by /document: Recipe "none, derived by scripts/docs-index.py",
Inputs the map with its generated date and the intent's version. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|

## Published
<!-- Designed files made by /publish, one row per file (CLAUDE.md,
Document chain, Renders). State: current | stale — set to current by
/publish, to stale by every /render of that recipe. -->
| File | Recipe | From render | Model | Published | State |
|---|---|---|---|---|---|

## Work
<!-- Work products (CLAUDE.md, Document kinds; POS.1520): one row per
work product, written by /work at the specification's birth and kept
by every making. Specification = its version. State: current — set by
the making; stale — set by a write of the specification not followed
by a making; by hand — set on the principal's word when he has worked
the file and does not want it remade. Made, Inputs and State are
read from the records of the specification's history. -->
| File | Specification | Inputs | Made | State |
|---|---|---|---|---|

## Sources
<!-- Registration only. External inputs, immutable once registered.
What a source is and is for lives in sources/00-INDEX.md, never here
(CLAUDE.md, Document chain, External inputs). Form (POS.1040): one
form per source. Date, its origin and Form are read from the fields
of the source's index entry (templates/index.md). -->
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
<!-- Findings of the critic and of the checks, one sequence. State:
open | resolved | rejected | parked | obsolete. Resolution:
assignment version, or for a check's finding what fixed it, for
resolved; DEC.NNNN for rejected. `overruled` in an older record reads
as `rejected`. State and Resolution are read from the `closed` record
of a history, or from the Verdict of a decision. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|

## Challenges
<!-- State: open | accepted | rejected | parked | obsolete. Resolution:
intent version for accepted, DEC.NNNN for rejected. State and
Resolution are read from the `closed` record of a history, or from
the Verdict of a decision. -->
| ID | State | Headline | Source review | Resolution |
|---|---|---|---|---|

## Waiting on principal
<!-- What waits on the principal, one line per matter: cite, never
copy — CLAUDE.md, Ledger. The rule (POS.1620): the open threads, each
by its first sentence and its last dated paragraph; the TBCs whose
owner is the principal; the open findings of a critic and the open
challenges; under Parked the parked findings and challenges with
their decision. Free text without an ID has no place here. -->
- …

## Reports
<!-- What the merged files cannot say, found by the ledger script
(POS.1640); the section stands only when there is something: an ID
defined twice, a closed thread touched by a later commit, a THR cited
with neither a thread file nor a closed record. A file the script
could not parse is a line `unparsed:` of the header, not a row. -->
- …
