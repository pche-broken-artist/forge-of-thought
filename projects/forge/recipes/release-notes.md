---
project: forge
purpose: release-notes
audience: humans tracking the system's evolution
version: 0.5
updated: 2026-09-05
last_change: 0.5 (2026-09-05): Instructions require the intent's current vocabulary even where an older history row uses a renamed word (check-forge finding of the 3.30 save — "material index" resurfaced in the Unreleased head).
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
                                       # the fine-grained log
- projects/forge/10-intent.md          # current state: version, status,
                                       # open threads
- projects/forge/decisions.md          # DEC records of the era
- RELEASE-NOTES.md                     # previous edition — released sections
                                       # carried over verbatim (absent on the
                                       # first render)

## Instructions
- Rendered by every `/save` that touches the core or
  `projects/forge/` (alongside the README), and as part of approving
  a major version of the forge intent. On an ordinary save only the
  Unreleased head is recomposed; the released sections below it are
  **carried over verbatim**.
- The file opens with an **Unreleased** section — heading
  `Unreleased — <major>.x since <last major>` — summarising the
  changes made since the last approved major (its minor versions in
  the intent's history companion), distilled from those rows and the
  DEC records of the span: themes, not a row-by-row replay. It opens
  with one plain sentence that these changes are not yet approved,
  needs no narrative opening and no "Open by design" close, and is
  recomposed freely on every render. When nothing has changed since
  the last approved major, the section is omitted entirely.
- Below it, one section per approved major version, **newest first**.
  At a major approval the Unreleased head is recast as the new
  major's section; the sections of already-released majors are
  carried over verbatim from the previous edition — published notes
  never change retroactively. Only factual corrections ordered by the
  principal may touch a released section, and they go through this
  recipe like any change.
- A major section synthesises what the era meant: a short narrative
  opening (two to four sentences), then thematic groups of changes
  distilled from the Version History rows and DEC records of that
  span — themes, not a row-by-row replay; the fine-grained log stays
  in the intent's history companion. Close each major section with what remains open by
  design (THR items) at the moment of approval.
- Every claim must be derivable from the inputs; invent nothing.
  UK English, plain and direct, no marketing.
- Open with YAML front-matter provenance like any render.

## Template
# Forge of Thought — Release Notes

<one sentence: what this file is — an Unreleased section covering the
changes since the last approved major, then one section per approved
major version of the system, newest first; the fine-grained log lives
in projects/forge/10-intent.history.md>

## Unreleased — <major>.x since <last major>

<one sentence: not yet approved, covering intent versions <range>>

<thematic groups of the changes since the last approved major, each a
bold lead-in phrase plus a few sentences; the whole section omitted
when nothing has changed since the last major>

## <version> — <date>

<short narrative: what this era meant>

<thematic groups of changes, each a bold lead-in phrase plus a few
sentences>

**Open by design:** <THR items open at approval>

## <previous versions — carried over verbatim>
