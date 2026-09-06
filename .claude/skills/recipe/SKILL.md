---
description: Compose a render recipe by genre — bare = genre roster, with a genre = guided composition
argument-hint: "[genre-or-recipe] [project-slug]"
---

Role: dispatcher for composing render recipes. A recipe is composed
conversationally with the principal; a genre definition carries the
elicitation checklist and points at the canonical skeleton for one
kind of render. Definitions live in `.claude/skills/recipe/genres/<genre>.md`
— one file per genre, its skeleton in `templates/recipe-<genre>.md`.
Adding a genre means adding those two files; this dispatcher never
changes.

**Bare `/recipe` — report the roster.**
1. List `.claude/skills/recipe/genres/` for the available genres, each with
   its one-line description.
2. Infer the current project from context ($1 may be a slug; if
   ambiguous, ask) and list its existing recipes from `recipes/` with
   versions.
3. Recommend a fit where the conversation suggests one. A recipe
   outside any genre stays legitimate: compose it conversationally
   from `templates/recipe.md`.

**`/recipe <genre>` — compose or iterate through that genre.**
1. Resolve `.claude/skills/recipe/genres/$1.md`. If it does not exist,
   check whether `recipes/$1.md` exists in the project — if so,
   iterate that recipe (through its genre definition when one fits,
   otherwise conversationally). If neither exists, list the genres
   that do and stop.
2. Read the genre file and follow it: it declares the elicitation
   checklist and the skeleton. A genre file's arguments are those
   following the genre name. The recipe is composed with the
   principal — options and trade-offs offered, decisions his — and
   written once per round on confirmation, per CLAUDE.md, Versioning
   & status (a recipe: version and updated date, no status), into
   `recipes/<recipe>.history.md` — created from `templates/history.md`
   with the recipe. Register the
   recipe in the ledger's Renders table when its first render exists.
3. After writing, offer `/render <recipe>` as the natural next step.
