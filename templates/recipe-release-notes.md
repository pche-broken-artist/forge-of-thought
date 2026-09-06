---
project: <slug>
purpose: release-notes
audience: the recipients and the principal tracking the project's releases
version: 0.1
updated: YYYY-MM-DD
last_change: <one line from the newest row of $1>
output: RELEASE-NOTES.md
---

# Recipe — release-notes

<!-- Release-notes-genre recipe, scaffolded by /new-project for a
thought project and iterated via /recipe release-notes; every /release
of the project adds the new release's section. What a recipe is and
how it is versioned is templates/recipe.md's. -->

## Inputs
- 10-intent.history.md      # the intent's Version History — the Notes
                            # block of each row is the source; the
                            # prose is the log
- 20-assignment.history.md  # the assignment's, likewise; one line per
                            # later layer as the chain grows
- 10-intent.md              # current state: version, date, status
- decisions.md              # DEC records, for the pointers of Rejected
                            # lines
- RELEASE-NOTES.md          # previous edition — sections of earlier
                            # releases carried over verbatim (absent
                            # on the first render)

## Instructions
- Rendered by every `/release` of the project. One section per
  release — the release number is the intent's version at the
  release, every version — newest first, headed
  `## <version> — <date>`. On a release only the new release's
  section is composed; the sections of releases already in the
  previous edition are **carried over verbatim**.
- A section is **compiled, never distilled**: its bullets are the
  Notes lines of the rows written since the previous release in every
  input companion — the intent's row for this version and the rows of
  the assignment and later layers since the last release — each
  placed under its group: `### Action required`, `### Added`,
  `### Changed`, `### Removed`, `### Fixed`, `### Rejected`, in this
  order, one bullet per line, the wording carried from the row —
  what changed with the pointer in parentheses, then "For you:" and
  what it means for the reader, both sides kept; where more than one
  document contributes, the bullet opens with the document's name.
  Empty groups are omitted. Inside a group, what the reader must do
  or know first, then by weight. Rows whose Notes say nothing for the
  reader give a section with the one line "Nothing for the
  recipients." A row without a Notes block is compiled from its prose
  into the same groups — the only case in which the render
  classifies.
- An approved major (an integer version) is headed
  `## <version> — <date> — approved` and opens, before its groups,
  with two to four sentences of highlights drawn from the rows since
  the previous major; the major's git tag is named in the highlights
  only where a row or a decision records it. No other section carries
  narrative.
- At a major the minors since the previous major **fold into it**:
  the major's section carries every Notes line of the span in the
  six groups, a line superseded by a later minor dropped so that only
  the final state remains, and the sections of those minors are not
  carried over — they leave the file, the detail per version staying
  in the history companions. Between majors every release keeps its
  section.
- No Unreleased section: at the moment of a render, which only
  `/release` runs, nothing is unreleased.
- Released sections never change retroactively. Only factual
  corrections ordered by the principal may touch one, through this
  recipe.
- Wording: UK English, plain and direct, one sentence per bullet;
  invent nothing — every line is derivable from the inputs.
- Open with YAML front-matter provenance like any render.

## Template
# <Project title> — Release Notes

<one sentence: one section per release of the project, newest first;
Action required first in every section; the fine-grained log with the
reasons lives in the history companions of the chain>

## <version> — <date>

### Action required
- <what changed (pointer). For you: what to do after this release>

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
