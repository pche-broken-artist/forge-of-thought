---
project: <slug>
purpose: release-notes
audience: humans tracking the project's evolution
version: 0.1
updated: YYYY-MM-DD
output: RELEASE-NOTES.md
---

# Recipe — release-notes

<!-- Release-notes-genre recipe, scaffolded by /new-project for a
thought project and iterated via /recipe release-notes. A recipe is
the iterated thing; its render is generated output. Never polish
RELEASE-NOTES.md by hand: change this recipe, run
/render release-notes — and every /save that touches the project
regenerates the Unreleased head. Recipes are tools: bare version +
updated date in front-matter, no status, no Version History — history
lives in git. -->

## Inputs
- 10-intent.md          # Version History — the fine-grained log
- decisions.md          # DEC records of the era
- RELEASE-NOTES.md      # previous edition — released sections carried
                        # over verbatim (absent on the first render)

## Instructions
- Rendered by every `/save` that touches the project, and as part of
  approving a major version of the intent. On an ordinary save only
  the Unreleased head is recomposed; the released sections below it
  are **carried over verbatim**.
- The file opens with an **Unreleased** section — heading
  `Unreleased — <major>.x since <last major>` (before the first
  approval: `Unreleased — towards 1.0`) — summarising the changes
  since the last approved major, distilled from the Version History
  rows and the DEC records of the span: themes, not a row-by-row
  replay. One plain opening sentence that these changes are not yet
  approved; recomposed freely on every render; omitted entirely when
  nothing has changed since the last major.
- Below it, one section per approved major version, **newest first**.
  At a major approval the Unreleased head is recast as the new
  major's section; released sections are carried over verbatim from
  the previous edition — published notes never change retroactively.
  Only factual corrections ordered by the principal may touch a
  released section, through this recipe.
- A major section: a short narrative opening (two to four sentences
  on what the era meant), thematic groups of changes distilled from
  the Version History rows and DEC records of the span, and a close
  on what remains open by design (THR items) at approval.
- Every claim derivable from the inputs; invent nothing. UK English,
  plain and direct.
- Open with YAML front-matter provenance like any render.

## Template
# <Project title> — Release Notes

<one sentence: an Unreleased section covering the changes since the
last approved major, then one section per approved major version of
the intent, newest first; the fine-grained log lives in 10-intent.md>

## Unreleased — <major>.x since <last major>

<one sentence: not yet approved, covering intent versions <range>>

<thematic groups, each a bold lead-in phrase plus a few sentences;
the whole section omitted when nothing has changed since the last
major>

## <version> — <date>

<short narrative: what this era meant>

<thematic groups of changes>

**Open by design:** <THR items open at approval>
