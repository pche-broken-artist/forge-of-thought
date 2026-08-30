---
description: Careful consistency check of the Forge system itself (core + projects/forge)
---

Cross-check the universal core and `projects/forge/` against each other
and report in Czech, compactly. Read-only: report findings and proposed
fixes and apply only what the principal approves. Pure ledger
bookkeeping (stale versions, dates, counts) may be offered as an
immediate fix.

1. **Core internal consistency**
   - CLAUDE.md commands table ↔ actual files in `.claude/commands/`;
     described agents ↔ `.claude/agents/`.
   - Scripts on disk ↔ CLAUDE.md: every file in `scripts/` is
     described in CLAUDE.md (layout comment and its governing rule)
     and nothing described there is missing on disk.
   - README ↔ CLAUDE.md: same chain, same conventions, same command
     set, no contradictions.
   - README is current: it promises to describe the actual present
     state of the system, so every claim in it must hold today —
     command names, file layout, conventions, planned extensions.
     Anything superseded by a later decision is a finding; the fix is
     re-rendering via its recipe, never editing the file.
   - `templates/` agree with the conventions (front-matter fields,
     Version History, prefixes, numbering, statuses;
     `templates/recipe.md` carries the recipe exemption — bare
     version, no status, no Version History).
2. **Core ↔ forge intent** (`projects/forge/10-intent.md`)
   - Every POS is honoured by the core documents; nothing withdrawn or
     rejected (REJ items, closed THR items) is still advertised
     anywhere in the core.
   - Decisions referenced from the intent exist in `decisions.md` and
     every DEC record is reflected in the intent where it applies.
3. **Forge project internal**
   - Front-matter version/date/status agreement (integer version =
     `approved`); top Version History row matches the front-matter.
   - Ledger agrees with reality: document versions and dates, DEC
     count, open threads ↔ "Waiting on principal".
   - ID hygiene: unique IDs, items in tens, groups starting at the next
     hundred, prefixes in their proper documents, groups as plain
     headings, depth ≤ 2.
   - Stale references: renamed commands, closed threads, removed items,
     dangling file references.
4. **Recipes and renders** (shape and freshness, never content)
   - Recipes in `projects/forge/recipes/` conform to
     `templates/recipe.md`: front-matter complete (project, purpose,
     audience, version, updated; `output:` optional), sections
     Inputs / Instructions / Template present; every declared input
     exists on disk; the `output:` path is valid. Genre skeletons
     (`templates/recipe-<genre>.md`) extend that shape with genre
     sections, never replace it.
   - Render staleness: each render's front-matter provenance (recipe
     version, input versions) against the files as they are now — a
     render generated from versions that have since moved is a
     finding, fixed by `/render`.
   - The ledger's Renders table mirrors the renders' front-matter.
   - Content stays out of scope: whether a recipe's instructions or a
     render's message still match the principal's thinking is
     substance, not conformance.
5. **Rename/removal sweep** — grep for the old names recorded in DEC
   records (e.g. a renamed command) and for terms the principal has
   explicitly dropped; only historical records (changelogs, DEC, REJ)
   may still contain them.
6. **Report** — findings ranked by severity, each with `file:line` and
   a proposed fix. If everything is consistent, say so in one line.

Do not judge substance or document quality — that is `/critique` and
`/challenge` territory. This command checks consistency only.
