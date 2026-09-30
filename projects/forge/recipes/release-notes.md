---
project: forge
purpose: release-notes
audience: the user of the engine who has cloned it and takes upgrades through forge-pull
version: 0.11
updated: 2026-09-30
last_change: 0.11 (2026-09-30): sections derived from the records of the history log, the Action carried word for word; a version before the log compiled from its archived Notes; the archive among the inputs.
output: /RELEASE-NOTES.md
---

# Recipe — release-notes

<!-- A recipe is the iterated thing; its render is generated output.
Never polish a render by hand: change the recipe, run
/render release-notes. Recipes are tools: version + updated date in
front-matter and no status (a recipe is never approved); its history
lives in the companion <recipe>.history.md, last_change derived from
the records of the newest version. -->

## Inputs
- projects/forge/10-intent.history.md  # the intent's history — its
                                       # records are the source of
                                       # each section
- projects/forge/10-intent.history.archive.md
                                       # the table before the log —
                                       # the Notes block of each row
                                       # is the source of its version
- projects/forge/10-intent.md          # current state: version, date,
                                       # status
- projects/forge/decisions.md          # DEC records, for the pointers
                                       # of Rejected lines
- RELEASE-NOTES.md                     # previous edition — sections of
                                       # earlier releases carried over
                                       # verbatim (absent on the first
                                       # render)

## Instructions
- Rendered by every `/release` of the engine, alongside the README.
  One section per release — every version of the intent, 3.12 as
  much as 3.0 — newest first, headed `## <version> — <date>`, the
  date being the row's. On a release only the new release's section
  is composed; the sections of releases already in the previous
  edition are **carried over verbatim**. A previous edition in the
  earlier narrative shape (an Unreleased head, one section per
  major) is not carried over: it is replaced whole, every release
  compiled from its row (the migration of 2026-09-05, POS.0730).
- A section is derived from the records of its version in the log:
  each record that reaches the reader becomes one bullet under the
  group its kind gives — `created` under Added, `changed` and
  `closed` under Changed, `removed` under Removed, a created REJ
  under Rejected, a change whose reason names a correction under
  Fixed — written from the reader's side: what changed with its ID
  in parentheses, then "For you:" and what it means. The groups
  stand as `### Action required`, `### Added`, `### Changed`,
  `### Removed`, `### Fixed`, `### Rejected`, in this order. The
  `Action` of a record is carried word for word into Action
  required. One change recorded across several IDs gives one bullet.
  Empty groups are omitted. Inside a group, what the reader must do
  or know first, then by weight. A record that touches nothing the
  reader uses gives none; a version with none gives the line
  "Nothing for the user of the engine." A version before the log is
  compiled from the Notes block of its row in the archive, as before.
- An approved major (an integer version) is headed
  `## <version> — <date> — approved` and opens, before its groups,
  with two to four sentences of highlights drawn from the rows since
  the previous major; the major's git tag (`v3.0`) is named in the
  highlights only where a row or a decision records it — the public
  repository's history starts at 3.0, so no earlier tag exists. No
  other section carries narrative.
- At a major the minors since the previous major **fold into it**:
  the major's section carries every line of the span — the
  major's own row and every minor's — in the six groups; a line that
  a later minor superseded (a mechanism replaced, a rule reversed
  within the span) is dropped so that only the final state remains;
  and the sections of those minors are not carried over — they leave
  the file, the detail per version staying in the history companion.
  Between majors every release keeps its section. The sections of
  3.1–3.x in the current edition are therefore carried over verbatim
  until 4.0 and folded then.
- No Unreleased section: at the moment of a render, which only
  `/release` runs, nothing is unreleased.
- Released sections never change retroactively. Only factual
  corrections ordered by the principal may touch one, and they go
  through this recipe like any change.
- Wording: UK English, plain and direct, one sentence per bullet, the
  intent's current vocabulary (resource index, document, artefact,
  history companion) even where an older row uses a word since
  renamed; invent nothing — every line is derivable from the inputs.
- Open with YAML front-matter provenance like any render.

## Template
# Forge of Thought — Release Notes

<one sentence: one section per release of the engine, newest first,
for the user who takes upgrades through forge-pull; Action required
first in every section; the fine-grained log with the reasons lives
in projects/forge/10-intent.history.md>

## <version> — <date>

### Action required
- <what changed (pointer). For you: what to do in your projects after pulling>

### Added
- <what changed (pointer). For you: what it means>

### Changed
- <what changed (pointer). For you: what it means>

### Removed
- <what is gone (pointer). For you: what it means>

### Fixed
- <what was fixed (pointer). For you: what it means>

### Rejected
- <a direction dropped (REJ or DEC). For you: what it means>

## <major version> — <date> — approved

<two to four sentences of highlights>

<groups as above, holding every line since the previous major,
superseded lines dropped; the minors' own sections do not follow>

## <earlier releases — carried over verbatim>
