---
project: <slug>
updated: YYYY-MM-DD
---

# Ledger — <Project>

<!-- Single source of truth for state, made at read time by
scripts/forge-ledger.py from the records and never in git: CLAUDE.md,
Ledger (POS.1600, POS.1610). This skeleton owns the shape of the
ledger: what each table holds and which record or field each column
is read from; the script keeps these comments. The header carries
the slug and the day the ledger was made; kind and language are the
project file's (templates/project.md), echoed under the header as
read from it. Kind: `thought` keeps every table below. `library`
(POS.0960) keeps only Renders, Sources, Dependencies, Research and
Waiting on principal; the Findings table returns with a check's
first finding. This comment is the one owner of that reduction
(POS.1070).
`ledger.archive.md`: the hand-kept ledger as it stood at the
migration, immutable; its Briefs, Work, Findings and Challenges rows
are read for every item without a record of the new shape, a newer
record overriding (POS.1610). -->

## Briefs
<!-- One row per brief (00-brief.md and 00-brief-<name>.md): Version
and Status from the brief's header; Mined and Note from the newest
mining record of the intent's history (templates/history.md, the
records of state), `pending` and `—` until one exists. Mined:
pending | partial | mined | dropped — how far the intent has absorbed
it; Note says what remains (partial) or the REJ (dropped). -->
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | 0.1 | draft | pending | — |

## Documents
<!-- One row per layer of the chain below the briefs: Version and
Status from the header, Date from the newest content record of the
history (a state record does not move it, POS.1630); a layer the
project does not have gets no row (CLAUDE.md, Ledger). -->
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 0.1 | draft | YYYY-MM-DD |

## Renders
<!-- One row per render file, from the render's own provenance
front-matter (CLAUDE.md, Document chain, Renders; a translation cites
the primary render): Audience from its recipe, Recipe, Inputs and
Generated as the provenance says. The documentation index has a row
from its own front-matter: Recipe "none: derived by
scripts/docs-index.py", Inputs the map and the intent's version. -->
| Render | Audience | Recipe | Inputs | Generated |
|---|---|---|---|---|

## Published
<!-- One row per designed file, from its companion
published/<recipe>.md (the shape: /publish step 6): File, Recipe,
From render, Model and Published as the companion says; State
current when the render's generated date is the one the companion
names, stale when the render is newer or missing. -->
| File | Recipe | From render | Model | Published | State |
|---|---|---|---|---|---|

## Work
<!-- One row per work product (CLAUDE.md, Document kinds; POS.1520):
File and Specification from the specification's header; Inputs, Made
and State from the newest state record of its history
(templates/history.md, the records of state): current | stale | by
hand; `—` and stale until a record exists. -->
| File | Specification | Inputs | Made | State |
|---|---|---|---|---|

## Sources
<!-- Registration only, one row per entry of sources/00-INDEX.md:
Date, Date origin and Form from the entry's Date and Form fields
(templates/index.md; POS.1040). What a source is and is for lives in
the index, never here (CLAUDE.md, Document chain, External inputs). -->
| File | Date | Date origin | Form |
|---|---|---|---|

## Dependencies
<!-- Registration only: the citations of another project's documents,
a library's or any other's (POS.1020), found in the chain, the
indexes, the recipes, the work and the research, one row per cited
directory, Library the cited project's slug, Used by the citing
files. No version: another project's documents are maintained by
their owner. What the document is for lives where it is used. -->
| Path | Library | Used by | Note |
|---|---|---|---|

## Research
<!-- Registration only, one row per note in research/, or per bundle
of one research read by its head 00-plan.md: Date and
Derived from out of the front-matter. What a note answers
lives in research/00-INDEX.md, never here. -->
| File | Date | Derived from |
|---|---|---|

## Findings
<!-- Findings of the critic and of the checks, one sequence. A
finding is born by its report in reviews/: ID, Severity and Category
from the heading (a check's category is conformance), Source review
the first report that names it, State open. State and Resolution
then come from the newest of: a `closed` record with the finding as
its subject (resolved, the record's reason), a decision's Verdict
(rejected | parked | obsolete, the DEC), a later report that names it
as reopened under Known as (open again). `overruled` in an older
record reads as `rejected`. -->
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|

## Challenges
<!-- One sequence, born by the report in challenges/: Headline from
the heading with the severity in brackets, Source review the report,
State open. State and Resolution then come from the newest of: a
`closed` record (accepted, the record's reason) or a decision's
Verdict (rejected | parked | obsolete, the DEC). -->
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
