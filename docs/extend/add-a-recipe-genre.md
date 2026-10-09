---
generated: 2026-10-09
made: derived
inputs-hash: 8699371702fad576
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
  - CLAUDE.md
---

# Add a recipe genre

This page is for someone extending the forge who wants `/recipe` to
guide the composition of a new kind of render. It was put together
from the `/recipe` skill, the presentation genre and its skeleton,
the base recipe skeleton and `CLAUDE.md`: the skill says what a
genre is made of and what frame every genre runs in, the base
skeleton says what shape a recipe has, and the presentation pair is
the model the procedure below is derived from.

## What a genre is

A recipe is composed conversationally with the principal. A genre
is what makes that conversation guided for one kind of render: it
carries the questions to ask and points at the skeleton the answers
are poured into. A genre is exactly two files:

| File | What it is |
|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the definition: what the genre produces, the role Claude takes and the numbered elicitation checklist |
| `templates/recipe-<genre>.md` | the skeleton: the shape of a recipe of this genre, with placeholders |

Adding a genre means adding those two files and nothing else. The
dispatcher, `.claude/skills/recipe/SKILL.md`, never changes: bare
`/recipe` lists the genres directory and reports each file's
one-line description, and `/recipe <genre>` resolves
`.claude/skills/recipe/genres/<genre>.md` and follows it. A new
file in that directory is a new genre the moment it is there.

A recipe outside any genre stays legitimate: it is composed from
`templates/recipe.md` directly. A genre is worth adding where one
kind of render recurs and the same questions come up every time.

## Step 1: write the definition

Create `.claude/skills/recipe/genres/<genre>.md`, modelled on
`.claude/skills/recipe/genres/presentation.md`. It has these parts,
in this order:

1. **Front-matter with a `description`.** One line saying what the
   genre composes and what comes out of it. This line is what bare
   `/recipe` shows in the roster, so it must stand on its own.
2. **The genre line.** `Genre: <genre>. Skeleton:
   templates/recipe-<genre>.md.` This is the only place the genre
   is tied to its skeleton.
3. **What the product is.** A short paragraph saying what the
   recipe's render is and what it is not. The presentation genre,
   for instance, says its render is source material for a deck and
   never the deck itself, and that the files beside the render are
   made in the two steps `CLAUDE.md`, Document chain, Renders
   describes. Where the genre's render has a file beside it, say
   here that what each step needs stands in the recipe's Format
   section and that the render carries content only.
4. **The role.** Interviewer: elicit the answers from the principal,
   options and trade-offs offered, decisions his, then compose the
   recipe from the skeleton. The decisions are the principal's; the
   genre file only says what to ask.
5. **The elicitation checklist.** A numbered list, one question per
   item, each with a bold heading and a sentence or two of what the
   item covers. Every item should map to a placeholder in the
   skeleton, so that when the checklist is answered the skeleton is
   filled. The presentation checklist runs from who the audience is
   through the inputs, the arc, density and vocabulary to what must
   not appear, and ends with the format; a new genre asks what its
   own kind of render needs decided. Where the render has a file
   beside it, the last item is the format: which file, what the
   plain file needs, what the model that designs the published file
   needs. Those answers stay in the recipe's Format section and are
   never copied into the render.
6. **The closing line.** The language question and the composition
   from the skeleton close every genre: say so by citing `/recipe`,
   step 2, and do not restate them.

Do not put the language question into the checklist. It is the
dispatcher's: every genre runs in the same frame, the checklist
closes with the language question, the project's language is
proposed from its ledger header and asked, never assumed, and the
recipe is then composed from the skeleton with unused placeholders
and all template comments deleted. The genre file leans on this
frame instead of repeating it.

## Step 2: write the skeleton

Create `templates/recipe-<genre>.md`, modelled on
`templates/recipe-presentation.md`. The base recipe skeleton,
`templates/recipe.md`, owns the shape of every recipe; a genre
skeleton extends it and never replaces it. That means the genre
skeleton keeps:

- **The same front-matter fields:** `project`, `purpose`,
  `audience`, `version` (0.1 at birth), `updated`, `last_change`
  (derived from the recipe's history, never written by hand) and
  the optional commented `output` that overrides the default
  `renders/<recipe>.md`. The genre may pre-fill a field: the
  presentation skeleton fills `purpose` with the genre's own
  phrasing and leaves a placeholder for the rest.
- **The same sections, in the same order:** `## Inputs`,
  `## Instructions`, `## Format` and `## Template`.
- **A `## Format` section where the render has a file beside it.**
  Its three lines are the base skeleton's: the format (`pptx` or
  `docx`), what the plain file made by `/render` through pandoc
  needs (a reference document or none), and what the published file
  made by `/publish` through a model needs (a template or none, the
  model, anything else the model must know). A genre whose render
  ends at the Markdown leaves the section out, as the base skeleton
  allows.

What the genre skeleton adds is specificity. Where the base
skeleton has a comment saying what belongs in a section, the genre
skeleton has the instructions themselves with placeholders in angle
brackets for what the checklist elicits: the presentation skeleton
turns the empty Instructions of the base into a list of concrete
rules, each with a placeholder (audience, register, language, the
one message, density limits, what must not appear) and a fixed
per-slide format, and turns the empty Template into a slide table.
A comment at the top of the skeleton says which genre composes it
and what its render is, citing `CLAUDE.md`, Document chain,
Renders for the recipe and its two steps rather than explaining
them again; a comment in the Format section points at the base
skeleton for the shape and at the conversion script's header for
how a template is named and where the file lands.

Angle-bracket placeholders and the comments are what `/recipe`
deletes when the recipe is composed, so put nothing in them that
must survive into the recipe.

## Step 3: prove it

Two proofs, in this order.

1. **Run the engine's checks.** `/check` with the engine as its
   target; bare `/check` lists the roster. The checks verify
   conformance with the conventions mechanically, so a skeleton that
   has drifted from the base shape shows up here.
2. **Compose a recipe on a project.** Run `/recipe <genre>` in a
   project. You see the interview run the checklist item by item,
   close with the language question, and compose the recipe from
   the skeleton into `recipes/<recipe>.md` with its history
   companion beside it, created from `templates/history.md`; the
   recipe is written once per round on the principal's confirmation.
   After the write `/recipe` offers `/render <recipe>` as the next
   step, and the recipe is registered in the ledger's Renders table
   when its first render exists. Run the render and look at what
   comes out: that is the genre's real test.

Bare `/recipe` now lists the new genre with its description among
the others, without any change to the dispatcher.

## See also

- [Recipe genres](../reference/recipe-genres.md): the genres that exist.
- [About renders and recipes](../about/renders-and-recipes.md): what a recipe is.
