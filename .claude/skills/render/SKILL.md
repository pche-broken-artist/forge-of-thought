---
description: Regenerate a render from its recipe in recipes/
argument-hint: "<recipe> [project-slug]"
disable-model-invocation: true
---

Role: renderer. A render is generated output, never edited by hand:
dissatisfaction with a render is fixed in its **recipe**, then
re-rendered. A render is regenerated only here, on the principal's
explicit command, or by `/release` (POS.0810); Claude never regenerates
on its own judgement — it reports a stale render and offers. Iterating the recipe is working conversation like any
other; generating the render is mechanical.

1. Infer the current project from context ($2, or ask if ambiguous) and
   read `recipes/$1.md`. If it does not exist, offer to compose it
   through `/recipe` (a genre where one fits, else bare from
   `templates/recipe.md`) and stop; what a recipe is and how it is
   versioned is stated there (POS.1070).
2. Read the recipe's declared inputs at their current versions.
3. Generate in isolation: spawn one subagent (Agent tool, type
   `general-purpose`, session model — never a model override) whose
   prompt names the project, the recipe path, the output path and the
   render date, and instructs it to read the recipe and its declared
   inputs, follow the Instructions and Template exactly, and write the
   file — nothing else. The prompt carries the front-matter block of
   step 5 verbatim, so the subagent never derives the provenance shape
   from a previous render. The subagent sees only the recipe and its
   inputs, never this conversation: a render is derived from the
   artefacts, not from what was said about them. It must not read the
   previous render unless the recipe declares it among its inputs
   (the release-notes genre does, for the released sections), and
   must not touch the ledger. Prose is hard-wrapped at about 72
   columns, like every artefact of the forge, so that git diffs stay
   legible; tables, code blocks and front-matter are never wrapped.
   Content only, always Markdown — a deck render may later be turned
   into an actual PowerPoint file by `scripts/md2pptx.ps1`, any render
   into a Word file by `scripts/md2docx.ps1`; all other format
   conversion happens outside the forge.
4. The subagent writes to `renders/$1.md`, or to the recipe's
   `output:` path if it declares one (e.g. the repository README).
   Overwrite freely; history lives in git.
5. The render opens with YAML front-matter provenance, written by the
   subagent:
   ```yaml
   ---
   project: <slug>
   render: <recipe>
   generated: YYYY-MM-DD
   recipe: recipes/<recipe>.md v<version>
   inputs:
     - <path> v<version>
   ---
   ```
   Inputs without a version of their own (e.g. CLAUDE.md) are cited by
   path alone. A render is **stale** when any version cited in this
   front-matter differs from the current version of that file, or a
   cited file no longer exists. This is the one definition; `/forge`
   and `/check` cite it (POS.1070).
6. Back in the session: verify the file exists and its provenance is
   correct, update the ledger's Renders table to mirror it, and report
   what was rendered
   from what.
