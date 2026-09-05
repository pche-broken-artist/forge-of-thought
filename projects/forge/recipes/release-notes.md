---
project: forge
purpose: release-notes
audience: the user of the engine who has cloned it and takes upgrades through forge-pull
version: 0.10
updated: 2026-09-05
last_change: 0.10 (2026-09-05): At an approved major the minors since the previous major fold into its section, superseded lines dropped, and their sections leave the file (POS.0730, intent 3.38).
output: /RELEASE-NOTES.md
---

# Recipe — release-notes

<!-- A recipe is the iterated thing; its render is generated output.
Never polish a render by hand: change the recipe, run
/render release-notes. Recipes are tools: version + updated date in
front-matter and no status (a recipe is never approved); its Version
History lives in the companion <recipe>.history.md, last_change
summarising the newest row. -->

## Inputs
- projects/forge/10-intent.history.md  # the intent's Version History —
                                       # the Notes block of each row is
                                       # the source of that release's
                                       # section; the prose is the log
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
- A section is **compiled, never distilled**: its bullets are the
  Notes lines of the row for that version, each placed under its
  group — `### Action required`, `### Added`, `### Changed`,
  `### Removed`, `### Fixed`, `### Rejected`, in this order — one
  bullet per line, the wording carried from the row: what changed
  with the pointer in parentheses, then "For you:" and what it means
  for the reader, both sides kept. Empty groups are omitted. Inside a group, what the
  reader must do or know first, then by weight. A row whose Notes say
  nothing for the reader gives a section with the one line "Nothing
  for the user of the engine." A row without a Notes block is
  compiled from its prose into the same groups — the only case in
  which the render classifies.
- An approved major (an integer version) is headed
  `## <version> — <date> — approved` and opens, before its groups,
  with two to four sentences of highlights drawn from the rows since
  the previous major; the major's git tag (`v3.0`) is named in the
  highlights only where a row or a decision records it — the public
  repository's history starts at 3.0, so no earlier tag exists. No
  other section carries narrative.
- At a major the minors since the previous major **fold into it**:
  the major's section carries every Notes line of the span — the
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

<groups as above, holding every Notes line since the previous major,
superseded lines dropped; the minors' own sections do not follow>

## <earlier releases — carried over verbatim>
