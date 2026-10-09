---
generated: 2026-10-09
made: derived
inputs-hash: afede2403726f35f
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About languages

This page explains which language each part of a project is written
in, where that is decided and why the forge holds it so. It is for
the user who works with a project and for the evaluator who wants to
understand how the forge treats language without running it. The
page was put together from the language rule in `CLAUDE.md` and
from the positions in `projects/forge/10-intent.md` that give the
reason behind the rule and the language of the documentation.

## One output language per project

The forge as a system dictates one thing about language: a project
has one output language. The artefacts of the chain, the intent, the
assignment and every later layer, are written in that language. It
is declared in the `language` field of the ledger header (an ISO
639-1 code), and when the field is absent the language is English.

Nothing else about a project's language is a system rule.

## Everything else is English

Everything a project holds besides its artefacts, the records, the
state, the research and the recipes, is always English, whatever the
project's output language is.

The reason is who reads these files. They are read by Claude, by the
reviewers and by the checks, and they are never handed to the
recipients of an assignment. One operating language is what lets
Claude, the reviewers and the checks read every project the same
way.

English is also the notation throughout: the ID prefixes, the word
`shall` in requirements, the status words and the front-matter keys
are English in every project, regardless of its output language.

## The exceptions among the artefacts

The one exception among the artefacts is the briefs (`00-brief*.md`).
A brief is kept in whatever language it was written in; it is not
translated into the project's language.

## Renders and translations

A render may be in any language its recipe declares. A translation
of an artefact is therefore a render: the artefact stays in the
project's language as the source of truth, and the translated text is
generated from it through a recipe.

## The documentation

The documentation of a project, the pages of which this one is a
part, is English only. A translation of it is a render, like any
other translation.

## The conversation language

The language the working conversation runs in is not a property of
the system. It is an instance fact, set in `CLAUDE.local.md` at the
engine root and read from there by every command. It is never written
into the operating layer of the forge and never presented outward:
the README and the other outward-facing renders state only the
output-language rule. How that file comes to be on a new machine is
the setup's business; see the page linked below.

## Translate on write

The rule is applied at the moment of writing. The conversation runs
in the conversation language; what is written into an artefact is
written in the project's language, and what is written into a record,
the state, research or a recipe is written in English. Translation
happens on write, not afterwards.

## See also

- [Set up the forge](../start/setup.md): where the conversation language is set.
