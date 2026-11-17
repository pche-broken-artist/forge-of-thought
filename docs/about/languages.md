---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 8be028e3d0fda84f
inputs:
  - CLAUDE.md#Prime directives
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.2010
---

# Languages

The language rule of the forge says which language each kind of
document of a project carries. This page explains the rule, how it
applies across the documents of a project and the reasons for it. It
is for whoever works on a project and wants to know in which language
a document will be written, and for whoever evaluates the forge and
wants to know what it fixes about language and what it leaves open.

## What it is

The forge dictates one thing about the language of a project: a
project has one output language. The artefacts of the chain (the
intent, the assignment and every later layer) are written in it. That
language is the project's language.

Three languages can meet in one project:

- The project's language: the one output language. The project
  declares it, and its artefacts and the pages of its documentation
  ([The documentation](the-documentation.md)) are written in it.
- English: the operating language of the records, the state, the
  research and the recipes of every project, and the notation
  throughout.
- The conversation language: the language in which the principal
  (the person whose thinking is forged) and Claude talk. It belongs
  to an instance (one installation of the forge), not to a project.

The [Glossary](../reference/glossary.md) gives every term of the
forge in one line.

## How it works

**The project's language.** The project file (`project.md`) declares
the language under `language`, as an ISO 639-1 code. Where the
project file declares none, the language is English. Three kinds of
document are written in the project's language:

- the artefacts of the chain;
- the pages of the documentation, written in the project's language
  as its artefacts are;
- a work specification, which follows the artefacts.

The file of a work specification carries the language that the
`## Making` section of the specification says.

**The briefs.** The briefs (the files `00-brief*.md`) are the single
exception among the artefacts. A brief is kept in whatever language
it is written in.

**English as the operating language.** Everything else a project
holds is always English, whatever the project's language:

- records;
- state;
- research;
- recipes.

**English as the notation.** English is the notation throughout, in
a project of any language:

- ID prefixes;
- status words;
- front-matter keys;
- the fixed labels under which a story carries its parts, such as
  `Edge cases` and `Risks`.

**The verb of a requirement.** The verb of a requirement follows the
language of the artefact. In English the obligation is "shall" and
"shall not". An artefact in another language uses its own verb of
obligation. The forge names no word of any other language. What the
obligation of a requirement is, and why its verb follows the
artefact's language, is explained in
[The assignment](the-assignment.md).

**Renders and the README.** A render may be in any language its
recipe declares, and a translation is itself a render; a recipe in
several languages is the subject of
[Renders and recipes](renders-and-recipes.md). The README is English
only. A translation of the README is a render.

**The conversation language.** The working conversation runs in the
principal's language. That language is configuration of one instance,
not a rule of the forge. It is set in `CLAUDE.local.md`, and every
command reads it from there;
[Set up the forge](../start/setup.md) shows where it is set. It is
never presented outward. The README and the other outward-facing
renders state only the output-language rule.

**Translate on write.** The conversation and the document it works
on can be in different languages. Whatever is written into a document
is translated at the write into the language that document carries.

## Why

The reason for English as the operating language lies in who reads
what is written in it. Records, state, research and recipes are read
by Claude, the reviewers and the checks. They are never handed to the
recipients of the artefacts. One operating language is what lets
these readers read every project the same way.

The conversation language is kept out of the rule on a different
ground. It is configuration of one instance and not a rule of the
system: it is set in that instance's own file and never presented
outward.

For the other parts of the rule the reason is not recorded:

- why a project has one output language and not several;
- why the briefs are the exception among the artefacts;
- why the notation is English in a project of any language;
- why the README is English only.

## A worked example

Take a project whose project file declares a language other than
English. The principal works on it in an instance whose conversation
language is a third language. In one working conversation a
requirement is added to the assignment, a research note is made on
the way and a render is made for one audience. The table shows the
language of each thing written.

| What is written | Its language |
|---|---|
| The conversation between the principal and Claude | the conversation language of the instance |
| The text of the new requirement, in the assignment | the project's language, with that language's own verb of obligation |
| The ID prefix of the requirement, the status words and the front-matter keys of the assignment | English, as notation |
| The record of the change | English |
| The research note | English |
| The recipe of the render | English |
| The render | the language its recipe declares |
| The pages of the documentation | the project's language |
| The README | English |

What was agreed in the conversation is translated on write into the
language of the document that receives it. The conversation language
itself is presented nowhere outward.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
- [Renders and recipes](renders-and-recipes.md): a recipe in several
  languages.
- [The documentation](the-documentation.md): the pages, generated in
  the project's language.
- [The assignment](the-assignment.md): the obligation of a
  requirement and why its verb follows the artefact's language.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
