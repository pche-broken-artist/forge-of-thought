---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: c2170d4e231fd230
inputs:
  - CLAUDE.md#Prime directives
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.1450
---

# Languages

The forge's language rule says which language each kind of document
in a project is written in. The forge dictates only one thing: a
project has one output language. This page explains which documents
carry that language, which are always English, and why. It is for
the user who works with a project and for the evaluator who wants to
understand how the forge is built.

## What it is

The rule separates what a project hands to people from what Claude
and the forge read for themselves. The principal (the person whose
thinking is being forged, with final authority over its content)
chooses the project's output language. Everything else follows from
that choice or is fixed in English.

The language of each kind of document:

- the artefacts (the documents of the chain, such as the intent, the
  assignment and every later layer): the project's language
- the briefs (the files `00-brief*.md`): whatever language they are
  written in; they are the one exception among the artefacts
- a work specification: the project's language, as the artefacts
- the file of a work product: the language its specification's
  `## Making` section says
- records, state, research and recipes: always English, whatever the
  project's language
- a render (an output made for one audience from the chain): any
  language its recipe declares

The terms above are each defined in one line in the
[Glossary](../reference/glossary.md).

English is also the notation throughout. ID prefixes, the word
`shall`, the status words and the keys of the front-matter are
English in every document, whatever its language.

## How it works

The project's language is the `language` field of its project file,
`project.md`. The value is a two-letter ISO 639-1 code. When the
field is absent, the project's language is English.

Claude translates on write. The conversation may run in one language
while the artefact is written in another. Claude writes the
artefact's text in the project's language at the moment it writes
the file.

A recipe may declare several languages: the first is primary, the
rest are translations made from it, one render per language, as
[Renders and recipes](renders-and-recipes.md) explains.

The conversation language is not part of this rule. It is a fact of
one instance (one installation of the forge), set per instance in
`CLAUDE.local.md` at the engine's root and read from there by every
command. Where it is set is shown in
[Set up the forge](../start/setup.md). It is never written into the
forge's own rules. It never appears in anything presented outward:
the README and every other outward-facing render state only the
rule of the output language. The README itself is English only; a
translation of it is a render.

## Why

Records, state, research and recipes are always English. This is
because they are read by Claude, the reviewers and the checks, and
never handed to the recipients. One operating language is what lets
them read every project the same way.

The conversation language stays out of the rules. This is because it
is a property of one instance, not of the system.

Why the forge holds a project to one output language, and not
several, is not recorded. The reason the briefs are exempt is not
recorded. The reason a work product's file takes its language from
its specification is not recorded. The reason Claude translates at
the moment of writing is not recorded.

## A worked example

A project file declares `language: fr`. The project's documents then
look like this:

| Document | Language |
|---|---|
| the brief `00-brief.md` | whatever the principal wrote it in |
| the intent `10-intent.md` | French |
| the project's records | English |
| the project's research notes | English |
| a recipe in `recipes/` | English |
| a render whose recipe declares French first and English second | French as primary, English as its translation, one render each |
| the ID prefixes, `shall`, the status words, the front-matter keys | English, in every document |

The principal may talk with Claude in a third language throughout.
That language shows up in none of these files.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
