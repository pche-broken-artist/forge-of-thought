---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 6fd5d57ef0b5884e
inputs:
  - CLAUDE.md#Prime directives
  - .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  - projects/forge/10-intent.md#POS.0060
  - projects/forge/10-intent.md#POS.0250
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.2010
---

# Languages

The forge sets one output language per project: the language its
project file declares, carried by the artefacts of the chain and by
the pages of the documentation. This page says which language each
kind of document carries, which parts stay English whatever the
project's language is, and why the rule is so. It is for the user
who works a project with Claude and for the evaluator who wants to
understand the rule without running anything.

## What it is

A project has one output language. It is the `language` of the
project file (`project.md`, the file that names the project's slug,
kind and language), given as an ISO 639-1 code. A project file
without a `language` means English.

That one language is all the forge dictates. The language of the
working conversation is not a rule of the system. It is a fact of
one instance (one installation of the forge), set in
`CLAUDE.local.md` and read from there by every command; where it is
set is said on [Set up the forge](../start/setup.md). It is never
written into the operating layer and never presented outward.

The principal is the person whose thinking is forged. He talks to
Claude in his own language. The files come out in the languages
below. Claude translates on write: what is agreed in the
conversation is written into the file in the language that file's
kind carries.

## How it works

Each kind of document has one language. The kinds fall into four
groups.

**The artefacts of the chain.** The intent, the assignment and every
later layer are written in the project's language. The briefs
(`00-brief*.md`) are the one exception among the artefacts: a brief
is kept in whatever language it was written in. The reason for the
exception is not recorded.

**The documentation.** The pages of the documentation are written in
the project's language, as its artefacts are; how the pages are made
is said on [The documentation](the-documentation.md). The README is
English only. A README in another language is a render, not a
second README.

**Records, state, research and recipes.** The records of a project,
its state (the ledger among it, the project's state file), its
research and its render recipes are always English, whatever the
project's language.

**Work, renders and the notation.**

- A work specification follows the artefacts: it is in the project's
  language. The work file beside it is in the language its
  `## Making` section says.
- A render is in any language, or languages, its recipe declares.
  Where a recipe declares several, the first is primary and the rest
  are its translations, one render per language; how a recipe
  declares them is said on
  [Renders and recipes](renders-and-recipes.md).
- English is the notation throughout: the ID prefixes, the status
  words and the front-matter keys are English in every project. So
  are the fixed labels of a user story (`Edge cases`, `Risks`,
  `Note`, `Questions`, `Reference`).

One word follows the artefact rather than the notation: the verb of
a requirement. A requirement is an obligation in the indicative. In
English the obligation is `shall` / `shall not`, strictly. An
artefact in another language uses that language's own verb of
obligation under the same rule, and the forge names no word of any
other language. Why the verb follows the artefact's language is said
on [The assignment](the-assignment.md).

Outward-facing renders, the README among them, state only the
output-language rule. The conversation language appears in none of
them.

## Why

The artefacts carry the project's language because the project, not
the forge, chooses the language its output is in. The forge dictates
only that there is one.

The records, the state, the research and the recipes are read by
Claude, by the reviewers and by the checks (the isolated agents that
review and verify a project; every term of the forge is in the
[Glossary](../reference/glossary.md)). They are never handed to the
recipients. One operating language is what lets Claude, the
reviewers and the checks read every project the same way. So they
are English in every project.

The conversation language is per-instance configuration, not a
system rule. Because it belongs to one installation and not to the
project, it is never presented outward, and the README states the
output-language rule alone.

The reason the README itself stays English, rather than following
the project's language as the pages do, is not recorded.

## A worked example

A project `my-project` has a project file that reads `language: fr`.
Its principal talks to Claude in whatever language his instance is
set to. The files of the project come out like this.

| File | Language |
|---|---|
| the project file | English notation; `language: fr` |
| `00-brief.md` | whatever language the brief was written in |
| the intent, the assignment, every later layer | French; the ID prefixes, the status words and the front-matter keys English |
| the requirements of the assignment | French, with the French verb of obligation in place of `shall` |
| the history of the intent, the decisions | English |
| the ledger | English |
| the research notes, the render recipes | English |
| the pages of the documentation | French |
| the README | English |
| a render whose recipe declares French and then English | one render in French, the primary, and one in English, its translation |
| a work specification | French |
| the work file beside the specification | the language its `## Making` section says |

When the principal and Claude agree a change to the intent in the
conversation, Claude writes it into the intent in French and records
it in the intent's history in English.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
