---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 0aaa478aa3ff6163
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
---

# Add a recipe genre

A recipe genre is one kind of render that `/recipe` knows how to
compose by interview: a genre definition carries the questions
Claude asks and points at the skeleton the recipe is composed from.
This page is for the extender who wants `/recipe` to offer a new
genre. It says which two files make a genre, what each holds, and how
you prove the addition works. What a recipe is and how a render is
made from it is explained in [Renders and
recipes](../about/renders-and-recipes.md); the genres that exist
today are listed in [Recipe genres](../reference/recipe-genres.md).

## Before you start

A genre is a change to the forge. How a change is proved, recorded
and released is said in [Make a change to the
forge](how-a-change-is-made.md); read that page first. The addition
of a genre is recorded and released as any change of the forge.

Two things hold before you touch a file:

- The `/recipe` command itself is a dispatcher and never changes
  when a genre is added. It lists the genre directory, resolves the
  genre you name and follows the genre file. Adding a genre means
  adding two files and nothing else.
- A recipe outside any genre stays legitimate. It is composed
  conversationally from `templates/recipe.md`. When a kind of render
  deserves a genre of its own is not recorded.

## The files

A genre is exactly two files. Their names share the genre's name.

| File | What it is | Modelled on |
|---|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the genre definition: what the render is, the role Claude takes, the elicitation checklist | `.claude/skills/recipe/genres/presentation.md` |
| `templates/recipe-<genre>.md` | the genre skeleton: the recipe shape with the genre's fixed rules and placeholders filled in | `templates/recipe-presentation.md` |

The base shape every recipe keeps is `templates/recipe.md`. That
skeleton owns the shape only: the front-matter, the title and the
four sections Inputs, Instructions, Format and Template. A genre
skeleton extends that shape and never replaces it. It keeps every
section and fills in what the genre fixes.

### The genre definition

The definition `.claude/skills/recipe/genres/<genre>.md` holds, in
this order:

- Front-matter with one key, `description`: one line saying what the
  genre composes and what comes out of it. Bare `/recipe` prints this
  line in its roster, so it is written for the reader of the roster.
- One line naming the genre and its skeleton:
  `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`
- A short paragraph on the product: what the render of this genre
  is, and what is or is not made from it afterwards. The
  presentation genre, for instance, says its render is source
  material for a deck and never the deck itself, and that the
  PowerPoint files are made from it in two further steps.
- The role Claude takes: interviewer. It elicits the answers from the
  principal (the person whose thinking is forged), offers options and
  trade-offs, leaves the decisions to him and then composes the
  recipe from the skeleton.
- The elicitation checklist: a numbered list of the points the
  interview settles, each with a bold name and a clause on what is
  asked. The points are the genre's own: they are the questions a
  recipe of this kind cannot be composed without. Where the render
  has a file beside it, the checklist's last point settles the
  format and the placeholders of the skeleton's Format section.
- The closing line: the language question and the composition from
  the skeleton close every genre.

The checklist does not ask the language question itself. That
question belongs to the frame every genre runs in, not to the genre,
and is asked after the checklist by `/recipe` step 2. The render's
language is what the recipe declares, so the question is never
skipped and never assumed.

### The genre skeleton

The skeleton `templates/recipe-<genre>.md` is `templates/recipe.md`
with the genre written in. It keeps:

- The front-matter of the base shape: `project`, `purpose`,
  `audience`, `version: 0.1`, `updated`, `last_change` derived from
  the history companion, and the optional `output` override.
  `purpose` may carry the genre's fixed wording with a placeholder
  inside it.
- The title `# Recipe — <purpose>`.
- A template comment under the title saying the recipe is composed
  through `/recipe <genre>` and what its render is.
- `## Inputs`: the artefacts the render is generated from, one per
  line, with a comment on what the genre takes as inputs.
- `## Instructions`: the rules the genre fixes for every recipe of
  its kind, with a placeholder `<...>` wherever the interview fills a
  value. The placeholders answer to the checklist: a point of the
  checklist has a place in the Instructions where its answer lands.
- `## Format`: only where the render has a plain file beside it. The
  base shape says a recipe without this section ends at the Markdown.
  Where the section stands, the genre fixes the format (`pptx` or
  `docx`) and leaves placeholders for the plain file's reference and
  the published file's template, model and further instructions.
- `## Template`: the literal skeleton of the render, always Markdown,
  with the genre's shape and placeholders.

A placeholder stands in angle brackets. A template comment stands in
`<!-- -->`. Both are deleted when a recipe is composed: `/recipe`
step 2 removes unused placeholders and all template comments, so the
skeleton may carry as much guidance as the composer needs.

## Steps

1. Write the genre definition
   `.claude/skills/recipe/genres/<genre>.md`. Start from the
   presentation definition as the model of the shape. Keep the
   front-matter `description`, the `Genre:` line, the product
   paragraph, the role, the checklist and the closing line. Replace
   the checklist's points with the ones your render needs settled.
   Keep the closing line as it stands.
   You should now see a file whose `description` reads as one line of
   a roster and whose checklist names the points of your genre only.
2. Write the genre skeleton `templates/recipe-<genre>.md`. Start from
   `templates/recipe.md` for the shape and from
   `templates/recipe-presentation.md` for the way a genre fills it.
   Keep every section of the base shape. Write the genre's fixed
   rules into Instructions with a placeholder for each answer the
   interview gives. Keep or drop Format by whether the render has a
   file beside it. Write the render's shape into Template.
   You should now see a skeleton where every point of your checklist
   has a place for its answer.
3. Check the two files agree. The `Genre:` line of the definition
   names the skeleton by its path. The checklist's last point, where
   the render has a file beside it, names the Format section's
   placeholders. No point of the checklist is without a place in the
   skeleton and no placeholder in the skeleton is without a point of
   the checklist that fills it.
   You should now see one name, `<genre>`, in both file names and in
   the `Genre:` line.
4. Run bare `/recipe`. It lists the genre directory, so the new genre
   appears with its one-line description without any change to the
   command.
   You should now see your genre in the roster beside the ones that
   existed before.

## Prove it

The commands, as they are typed:

- `/check engine`: the conformance check of the engine, on the two
  new files among the rest.
- `/recipe <genre> <slug>`: one composition on a project, where
  `<slug>` is the slug of a project you have. Claude follows the
  checklist point by point, asks the language question last, and
  composes the recipe from your skeleton into `recipes/<recipe>.md`
  with its history companion beside it. After the write it offers
  `/render <recipe>`.

The composition proves the genre: a point of the checklist with no
place in the skeleton, or a placeholder no point fills, shows up
there.

## Record and release

The two files are recorded and released as any change of the forge,
by the steps of [Make a change to the
forge](how-a-change-is-made.md). The roster of bare `/recipe` reads
the genre directory and needs no change of its own.

## A worked example

You want `/recipe` to compose a genre called `<genre>`.

First you write `.claude/skills/recipe/genres/<genre>.md`:

```markdown
---
description: Compose a <genre> recipe — <what the render is, in one line>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is> —
<what it is not>. <What is made from it afterwards, where the render
has a file beside it; what each step needs is the recipe's Format
section.>

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his (`/recipe`, step 2) —
then compose the recipe from the skeleton.

Elicitation checklist:
1. **<First point>.** <What is asked.>
2. **<Second point>.** <What is asked.>
3. **Inputs.** Which chain artefacts feed the render.
4. **<Further points of this genre>.** <What is asked.>
5. **Format.** <Only where the render has a file beside it: the
   format, and the placeholders of the skeleton's Format section.>

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

Then you write `templates/recipe-<genre>.md`:

```markdown
---
project: <slug>
purpose: <the genre's fixed purpose wording> <the particular>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/<recipe>.history.md>
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <name>

<!-- <genre>-genre recipe, composed via /recipe <genre>; the render
is <what the render is>. A recipe: CLAUDE.md, Document chain,
Renders. -->

## Inputs
<!-- Chain artefacts the render is generated from. -->
- 10-intent.md

## Instructions
- <A rule the genre fixes for every recipe of its kind.>
- Audience: <audience>. Register: <register>. Language: <English>.
- <The answer to the first point lands here.>
- <The answer to the second point lands here.>
- Content comes from the Inputs only — no invention, no softening.

## Format
<!-- Only where the render has a file beside it. The shape:
templates/recipe.md. -->
- Format: <pptx | docx>
- Plain file, made by `/render` through pandoc: reference
  <path | none>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must know>.

## Template
<The literal skeleton of the render, in Markdown, with
placeholders.>
```

Then you type `/recipe`. The roster lists `<genre>` with its one-line
description. Then you type `/recipe <genre> <slug>` on a project of
yours. Claude asks the points of your checklist one after another,
asks the language question last, proposes the language of the
project's ledger header, and on your confirmation writes
`recipes/<recipe>.md` and `recipes/<recipe>.history.md` from your
skeleton with the placeholders and comments removed. It offers
`/render <recipe>`. Then you type `/check engine` and settle what it
finds. Then the two files go the way of every change of the forge.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a
  recipe is.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
