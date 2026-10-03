---
description: Make the designed .pptx or .docx from the render of a recipe, through a model — started by the principal only
argument-hint: "<recipe> [project-slug]"
disable-model-invocation: true
---

Role: publisher (what a render, its plain file and a published file
are: CLAUDE.md, Document chain 7). A published file is made only
here, on the principal's command; Claude never publishes on its own
judgement and no other command does — a stale published file is
reported, never remade. The command makes a file and sends nothing
anywhere.

1. Infer the current project from context ($1, or ask if ambiguous)
   and read `recipes/$0.md`. If it does not exist, say so and stop.
2. Read the recipe's `## Format` section (skeleton
   `templates/recipe.md`). A recipe without it ends at the Markdown:
   say so and stop. An older recipe carrying `## Build instructions`
   is read as Format (the alias: `templates/recipe.md`, Format);
   where it names no format, ask once, and offer to bring the recipe
   in line through `/recipe`.
3. Find the render — `renders/$0.md`, or the recipe's `output:` path.
   If it does not exist, say so and stop. Never render: what is
   published is the Markdown as it lies on disk, the text the
   principal has read.
4. Where the render is stale (as `/render` step 5 defines it), say
   which version differs before anything runs, and wait for the
   principal's word: publish as it is, or stop so that he can
   `/render` first.
5. Say in one line what runs and that it takes minutes, then run the
   script of the format — `scripts/md2pptx.ps1` or
   `scripts/md2docx.ps1` — with `-Engine claude`, `-Recipe` naming
   the recipe, the template or reference document and the model the
   Format section names, and
   `-Out projects/<slug>/published/$0.<ext>`. What each script needs
   installed is its header's.
6. Back in the session: verify the file exists, write its row in the
   ledger's Published table — the file, the recipe with its version,
   the render it was made from (its `generated` date and the input
   versions of its front-matter), the model, the date, state
   `current` — and report what was published from what. A failed run
   changes nothing in the ledger.
