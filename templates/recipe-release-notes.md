---
project: <slug>
purpose: release-notes
audience: the recipients and the principal tracking the project's releases
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/release-notes.history.md>
output: RELEASE-NOTES.md
---

# Recipe — release-notes

<!-- Release-notes-genre recipe, iterated via /recipe release-notes.
The rules: CLAUDE.md, Document chain 7. -->

## Inputs
- 10-intent.history.md      # the intent's history — its records are
                            # the source of each section
- 10-intent.history.archive.md  # the table before the log, where the
                            # project has one — the Notes block of each
                            # row is the source of its version
- 20-assignment.history.md  # the assignment's, likewise, with its
                            # archive; one line per later layer as the
                            # chain grows
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
- A section is derived from the records of its version in the log
  of every input history — the intent's and those of the assignment
  and later layers since the last release: each record that reaches
  the reader becomes one bullet under the group its kind gives —
  `created` under Added, `changed` and `closed` under Changed,
  `removed` under Removed, a created REJ under Rejected, a change
  whose reason names a correction under Fixed — written from the
  reader's side: what changed with its ID in parentheses, then "For
  you:" and what it means; the groups and their order as the Template
  below lists them. The `Action` of a record is carried word for word
  into Action required. One change recorded across several IDs gives
  one bullet; where more than one document contributes, the bullet
  opens with the document's name. Empty groups are omitted. Inside a
  group, what the reader must do or know first, then by weight. A
  record that touches nothing the reader uses gives none; a version
  with none gives the line "Nothing for the recipients." A version
  before the log is compiled from the Notes block of its row in the
  archive, as before.
- An approved major (an integer version) is headed
  `## <version> — <date> — approved` and opens, before its groups,
  with two to four sentences of highlights drawn from the history
  since the previous major; the major's git tag is named in the
  highlights only where a record or a decision names it. No other section carries
  narrative.
- At a major the minors since the previous major **fold into it**:
  the major's section carries every line of the span in the
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

<groups as above, holding every line since the previous major,
superseded lines dropped; the minors' own sections do not follow>

## <earlier releases — carried over verbatim>
