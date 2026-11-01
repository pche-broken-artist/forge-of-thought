---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 42790dd2c3a95392
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
  - .claude/skills/man/SKILL.md
---

# Add a recipe genre

A recipe genre is one kind of render that `/recipe` can compose by
interview: a definition that carries the questions, and a skeleton
that carries the shape of the recipe the answers fill. This page is
for the extender who adds a genre to the forge: which two files make
one, what each holds, how the addition is proved, and how it is
recorded and released. What a recipe is, and how a render is made
from it, is explained in [Renders and recipes](../about/renders-and-recipes.md);
the genres that exist today are listed in
[Recipe genres](../reference/recipe-genres.md).

## Before you start

- How a change to the forge is made, proved, recorded and released
  is one page: [Make a change to the forge](how-a-change-is-made.md).
  A genre is recorded and released as any change of the forge.
- A genre needs no change to the dispatcher. `/recipe` reads its
  genre directory at the moment of the call. Adding a genre means
  adding two files and nothing else.
- A recipe outside any genre stays legitimate. Claude composes it
  conversationally with the principal (the person whose thinking is
  being forged) from the base skeleton `templates/recipe.md`. A genre
  adds a guided way for one kind of render.
- The presentation genre is the model of both files:
  `.claude/skills/recipe/genres/presentation.md` and
  `templates/recipe-presentation.md`. Read them beside this page.

## The files

| File | What it is | What it holds |
|---|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the definition of the genre | a one-line `description` in the front-matter; the genre's name and the path of its skeleton; what the product is; the role, interviewer; a numbered elicitation checklist; the closing sentence of the shared frame |
| `templates/recipe-<genre>.md` | the skeleton of a recipe of this genre | the base recipe shape of `templates/recipe.md`, with placeholders for what the checklist elicits; a `## Format` section where the render has a file beside it; `languages:` where the genre allows a primary and its translations |

The definition is what Claude follows when `/recipe <genre>` runs.
Its `description` is the one line that bare `/recipe` and
`/man recipe` print for the genre. Its checklist is what `/man recipe`
prints in full, so that the principal knows what the interview asks
before running it.

The skeleton is what the recipe is composed from. Its placeholders
stand in angle brackets. Its guidance stands in HTML comments. When a
recipe is written, all template comments and every unused placeholder
are deleted, so that the recipe carries only what was decided.

## Steps

1. Read the model. Read `templates/recipe.md` for the base shape,
   then the presentation definition and its skeleton for how a genre
   specialises it.
2. Write the definition `.claude/skills/recipe/genres/<genre>.md`.
   - Front-matter: one `description` line. It says what the recipe's
     render is and what is made from it.
   - First line of the body: `Genre: <genre>. Skeleton:
     templates/recipe-<genre>.md.`
   - A paragraph on the product: what the render is, and what is made
     from it afterwards and by which step.
   - The role: interviewer. Claude elicits the answers from the
     principal, options and trade-offs offered, decisions the
     principal's, then composes the recipe from the skeleton.
   - The elicitation checklist, numbered. Each item names one matter
     in bold and says what it settles. In the model, each question
     fills placeholders of the skeleton. Where the render has a file
     beside it, one question settles the `## Format` section: the
     format, and what the plain file and the published file each
     need.
   - Do not add a language question. The shared frame asks it after
     the checklist for every genre. Close the file with the sentence
     that the language question and the composition from the skeleton
     close every genre.
3. Write the skeleton `templates/recipe-<genre>.md`.
   - Start from `templates/recipe.md`. Keep its front-matter:
     `project`, `purpose`, `audience`, `version: 0.1` and the optional
     `output:` line.
   - Keep the optional `languages:` line where the genre allows a
     primary and its translations. The first language is primary,
     the rest are translated from it, one render per language as
     `renders/<recipe>.<lang>.md`. Leave the line out where the genre
     does not allow translations.
   - Keep the sections `## Inputs`, `## Instructions` and
     `## Template`. Fill `## Instructions` with placeholders for what
     the checklist elicits. Fill `## Template` with the literal
     skeleton of the render, always Markdown.
   - Keep `## Format` where the render has a file beside it. It holds
     the format line (`pptx`, `docx`, `video` or `html-player`), the
     line of the plain file made by `/render`, and the line of the
     published file made by `/publish` through a model. A
     screenplay's `video` or `html-player` has no published file.
     Leave `## Format` out where the render ends at the Markdown.
   - Write guidance as HTML comments and nothing to decide as prose.
     Both the comments and the unused placeholders disappear when a
     recipe is composed.
4. Touch nothing else. The dispatcher `.claude/skills/recipe/SKILL.md`
   never changes for a genre.

## Prove it

The proof is a composition on a project through the new genre, then
a render of what it composed. The composition in full is
[Compose a recipe](../use/compose-a-recipe.md). Use a project of your
own; `<slug>` stands for its slug.

```
/recipe
```

You should now see `<genre>` in the roster with its one-line
description, beside the genres that existed before.

```
/man recipe
```

You should now see the genre's description and its elicitation
checklist printed in full.

```
/recipe <genre> <slug>
```

Claude asks the checklist's questions in order, options and
trade-offs offered, decisions yours. The last question is the
language of the render; Claude proposes the project's language from
its project file and asks. On your confirmation Claude writes the
recipe once, with its history companion. You should now see
`recipes/<recipe>.md` and `recipes/<recipe>.history.md` in the
project, the recipe free of template comments and unused
placeholders, and Claude offering `/render <recipe>` as the next step.

```
/render <recipe> <slug>
```

You should now see the render at `renders/<recipe>.md`, or where the
recipe's `output:` sends it, and the plain file beside it where the
recipe's `## Format` names one. A genre that allows translations
yields one render per language.

## Record and release

The two files are recorded and released as any change of the forge:
[Make a change to the forge](how-a-change-is-made.md) says how.

## A worked example

An extender adds the genre `<genre>`, whose render is one kind of
Markdown document with a plain Word file beside it.

The definition, `.claude/skills/recipe/genres/<genre>.md`:

```
---
description: Compose a <genre> recipe: <what the render is>, with <what is made from it>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>. The
<file> is made from it in the two steps of a render; what each step
needs is the recipe's Format section.

Role: interviewer. Elicit the answers below from the principal,
options and trade-offs offered, decisions his, then compose the
recipe from the skeleton.

Elicitation checklist:
1. **<First matter>.** <What it settles.>
2. **<Second matter>.** <What it settles.>
3. **<Third matter>.** <What it settles.>
4. **Format.** Always `docx`. For the plain file: a reference
   document or none. For the published file: the template, the
   model, and what else the model must know.

The language question and the composition from the skeleton close
every genre.
```

The skeleton, `templates/recipe-<genre>.md`, with the base shape
kept and the placeholders the checklist fills:

```
---
project: <slug>
purpose: <purpose>
audience: <audience>
version: 0.1
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <name>

<!-- <genre>-genre recipe, composed via /recipe <genre>; the render
is <what the render is>, from which /render makes the plain file and
/publish the designed one. -->

## Inputs
- 10-intent.md

## Instructions
- <What the first matter settled.>
- <What the second matter settled.>
- <What the third matter settled.>
- Content comes from the Inputs only.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference
  <path | none>, page size <A4 | Letter>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must know>.

## Template
<the literal skeleton of the render, with placeholders>
```

No `languages:` line stands in this skeleton, since this genre does
not allow translations.

The run on a project `<slug>`. Bare `/recipe` lists `<genre>` with
its description. `/man recipe` prints the description and the four
questions. `/recipe <genre> <slug>` asks the four questions, then the
language; the extender answers each and confirms the write. The
project now holds `recipes/<recipe>.md` with `version: 0.1`, and
`recipes/<recipe>.history.md` beside it. `/render <recipe> <slug>`
makes `renders/<recipe>.md` and the plain Word file beside it. The
two new files of the engine are then recorded and released as any
change.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a recipe is.
- [Compose a recipe](../use/compose-a-recipe.md): the composition that proves a genre.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
