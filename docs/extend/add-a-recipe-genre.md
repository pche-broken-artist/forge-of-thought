---
generated: 2026-10-10
made: derived
inputs-hash: 0c233b78aa724aee
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
  - CLAUDE.md
---

# Add a recipe genre

This page is for someone extending the forge who wants `/recipe` to
guide the composition of a new kind of render. It says what a genre
is made of, how to write its two files and how to prove they work.
It was put together from the `/recipe` skill, the presentation genre
and its skeleton, the base recipe skeleton and `CLAUDE.md`: the
procedure below is derived from that model pair, not stated as such
anywhere.

## What a genre is

A recipe is the versioned file a render is generated from: its
inputs, its audience, its instructions and the output template in
one place. A recipe may be composed through a genre interview:
`/recipe <genre>` reads a genre definition, works through its
elicitation checklist with the principal and composes the recipe
from the genre's skeleton.

A genre is exactly two files:

| File | What it is |
|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the definition: what the genre produces, the role Claude takes and the numbered checklist of what is elicited |
| `templates/recipe-<genre>.md` | the skeleton: the recipe shape, pre-filled with what the genre fixes |

Adding a genre means adding those two files and nothing else. The
dispatcher, `.claude/skills/recipe/SKILL.md`, never changes: bare
`/recipe` lists the genres directory and shows each genre by its
one-line description, and `/recipe <genre>` resolves the definition
by its file name. A new file in the directory is a new genre the
moment it is there.

## Step 1: write the definition

Model it on `.claude/skills/recipe/genres/presentation.md`. The
shape, top to bottom:

1. **Front-matter with one `description` line.** This is the line
   the roster shows. Say what the genre composes and what comes out
   of it.
2. **The genre name and its skeleton.** One line:
   `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`
3. **What the product is.** A short paragraph saying what the render
   of such a recipe is, and, where the render has a file beside it,
   that the file is made in the two steps of `CLAUDE.md`, Document
   chain, Renders, with what each step needs standing in the
   recipe's Format section.
4. **The role.** Claude is the interviewer: the answers are elicited
   from the principal, options and trade-offs offered, decisions
   his, and only then is the recipe composed from the skeleton.
5. **The elicitation checklist.** A numbered list, one question per
   item, each with the options worth naming. It is the genre's own
   substance: what must be known before a recipe of this kind can
   be written. The presentation genre, for instance, asks after the
   audience, the one message, the inputs, the arc, the density of a
   slide, the diagram policy and the format; a genre of yours asks
   after whatever its render turns on. Where an item concerns the
   Format section, point at the script header that owns the
   details (`scripts/md2pptx.py`, `scripts/md2docx.py`) rather than
   repeating them.
6. **The closing line.** Say that the language question and the
   composition from the skeleton close every genre, citing
   `/recipe`, step 2. Do not put the language question into the
   checklist: the dispatcher asks it.

A definition carries no instruction the dispatcher already gives:
how the recipe is written, versioned and followed by `/render` is
the dispatcher's, and a genre file only points at it.

## Step 2: write the skeleton

Model it on `templates/recipe-presentation.md`, which is
`templates/recipe.md` with the genre's choices filled in. The base
skeleton owns the shape; a genre skeleton extends it and never
replaces it. Keep:

- **The same front-matter fields:** `project`, `purpose`,
  `audience`, `version: 0.1`, `updated`, `last_change`, and the
  optional commented `output` that overrides where the render
  lands. A recipe carries `updated` in place of `date` and no
  status, and stays at 0.x.
- **The same sections in the same order:** `## Inputs`,
  `## Instructions`, `## Format`, `## Template`.

Then fill in what the genre fixes:

- A `purpose` line and a title that say what kind of render this
  is, with a placeholder for the particular one.
- An opening template comment saying the recipe is composed via
  `/recipe <genre>` and what its render is.
- Under Instructions, the bullets every recipe of this genre needs,
  with angle-bracket placeholders where the interview fills a value
  (audience, register, language, what must not appear, and so on).
  Where the render has a fixed per-section form, give it literally,
  as the presentation skeleton gives its per-slide format.
- Under Format, the genre's format where its render has a file
  beside it: the plain file `/render` makes through pandoc and the
  published file `/publish` makes through a model, each with the
  placeholders the interview fills (reference or template, model,
  anything else the model must know). A genre whose render ends at
  the Markdown leaves the section out: a recipe without it ends at
  the Markdown.
- Under Template, the literal skeleton of the render with
  placeholders, always Markdown.

Placeholders the interview does not use, and every template
comment, are deleted when a recipe is composed; write the skeleton
knowing that.

Prose in both files is hard-wrapped at about 72 columns; tables,
code blocks and front-matter are never wrapped.

## The frame every genre runs in

You write only the two files; the rest is the dispatcher's and the
same for every genre:

- The checklist closes with the language question. The render's
  language is what the recipe declares; the project's language is
  proposed from its ledger header and asked, never assumed.
- The recipe is composed from the genre's skeleton, with unused
  placeholders and all template comments removed.
- It is composed with the principal, written once per round on his
  confirmation, with version and updated date, and its history
  companion `recipes/<recipe>.history.md` is created with it from
  `templates/history.md`.
- After the write, `/render <recipe>` is offered as the next step.

A genre that needed any of this to be different would be asking
for a change of the dispatcher, which is a different piece of work.

## Step 3: prove it

- Run bare `/recipe`: the new genre appears in the roster with its
  description line.
- Run a check on the engine (`/check`, with the engine as its
  target): the checks verify mechanical conformance with the
  conventions, and the two new files are among what they read.
- Compose a recipe on a project with `/recipe <genre>` and then
  `/render` it. The interview should reach the language question
  last, the written recipe should carry no leftover placeholder or
  template comment, and the render should come out in the shape
  the Template section gave it.

## See also

- [Recipe genres](../reference/recipe-genres.md): the genres that exist.
- [About renders and recipes](../about/renders-and-recipes.md): what a recipe is.
