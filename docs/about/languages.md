---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: ccd0f1eb67fca1ec
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The language rule of the forge says which language each kind of
document in a project is written in. The forge sets one output
language per project and keeps everything else in English. This page
is for the user who starts a project in a language other than English,
and for the evaluator who wants to know why a project holds documents
in more than one language.

## What it is

The forge as a system dictates one thing about language: a project
has one output language. The artefacts of the chain are written in
it. An artefact is a versioned document of the chain, such as the
intent, an assignment or any later layer. Every other document either
follows the artefacts or is fixed in English.

The principal is the person whose thinking is forged in the project.
He talks with Claude in a language of his own. That conversation
language is per-installation configuration, not a rule of the system.

## How it works

The output language is declared in the project file (`project.md`)
under the key `language`, as an ISO 639-1 code. Where the key is
absent, the output language is English.

Each kind of document then carries its language as follows:

- The artefacts of the chain (intent, assignment, later layers): the
  project's output language.
- The briefs (`00-brief*.md`): whatever language they are written in.
  They are the one exception among the artefacts.
- A work specification: the language of the artefacts.
- The file of a work product: the language its `## Making` section
  says.
- Records: always English.
- State: always English.
- Research: always English.
- Recipes: always English.
- A render: any language, or languages, its recipe declares. The first
  is the primary, and the rest are its translations, one render per
  language. How a recipe declares several languages is explained in
  [Renders and recipes](renders-and-recipes.md).
- The README of a project: English only. A translation of the README
  is a render.

English is also the notation throughout, whatever the project's
language. This covers:

- ID prefixes.
- The words `shall` and `shall not` in requirements.
- Status words.
- Front-matter keys.

Claude translates on write. The conversation may run in the
principal's language, and what lands in a file is written in the
language that file's kind carries.

The conversation language is set per installation, in the file of
instance facts `CLAUDE.local.md`, and every command reads it from
there. Where it is set on a new machine is shown in
[Set up the forge](../start/setup.md). It is never written into the
operating layer of the forge. It never appears in anything presented
outward. The README and the other outward-facing renders state only
the output-language rule.

For any term used here, see the [Glossary](../reference/glossary.md).

## Why

Records, state, research and recipes are always English for two
reasons:

- They are read by Claude, the reviewers and the checks, and never
  handed to the recipients of the project.
- One operating language lets those readers read every project the
  same way.

The reason the briefs are exempt is not recorded. The reason a work
product's file takes the language its `## Making` section says is not
recorded. The reason the README is English only is not recorded. The
reason the conversation language is never presented outward is not
recorded beyond its being per-installation configuration rather than
a rule of the system.

## A worked example

A generic project declares French in its project file:

```
language: fr
```

The principal talks with Claude in another language. The files of the
project then come out as follows:

| Document | Language |
|---|---|
| `00-brief.md` | whatever the principal wrote it in |
| `10-intent.md` | French, with English ID prefixes, status words and front-matter keys |
| a note in `research/` | English |
| `recipes/<recipe>.md` | English |
| the render of a recipe that declares `fr` and `en` | one render in French, the primary, and one in English, its translation |
| `README.md` | English |

Nothing in any of these files names the language of the conversation.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
