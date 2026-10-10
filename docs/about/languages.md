---
generated: 2026-10-10
made: derived
inputs-hash: 47a6c5e2d6a4a323
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About languages

This page explains which language each kind of document in a project
is written in, why the rule is drawn where it is, and where the
language of the working conversation is set. It is for the user who
works with the forge and for the evaluator who wants to understand
why a project can be in one language while most of its files are in
another. It was put together from `CLAUDE.md` (the rule, prime
directive 6) and `projects/forge/10-intent.md` (the reasons).

## One output language per project

The forge as a system dictates only one thing about language: a
project has one output language. The artefacts of the chain, the
intent, the assignment and every later layer, are written in the
language the project's ledger header declares in its `language`
field (an ISO 639-1 code). When the header has no such field, the
language is English.

Everything else a project holds is always English, whatever the
project's language: the records (histories, decisions, reviews,
challenges), the state (the ledger, the indexes), the research notes
and the render recipes. The reason is who reads them. These files are
read by Claude, by the isolated reviewers and by the checks, and they
are never handed to the recipients of an assignment. One operating
language is what lets Claude, the reviewers and the checks read every
project the same way.

English is also the notation throughout, in every project and every
language: the ID prefixes (`REQ`, `POS`, `DEC` and the rest), the
word `shall` in requirements, the status words (`draft`, `approved`,
`superseded`) and the front-matter keys.

The rule is written to the artefacts and nothing wider: the boundary
was narrowed to the artefacts on 2026-09-10.

## The exception: the briefs

The one exception among the artefacts is the briefs (`00-brief*.md`).
A brief is kept in whatever language it was written in. It is the
principal's own text of what he wants, and it is not translated into
the project's language.

## Renders and translations

A render may be in any language its recipe declares. A translation
of an artefact is therefore not a new artefact of the chain but a
render: the artefact stays the source of truth in the project's
language, and the recipe says what language the output is in. The
README of a project is English only; a translation of it is a render
too.

## Translate on write

When the conversation runs in one language and the project's output
language is another, the translation happens at the moment of
writing: what is agreed in the conversation is written into the
artefact in the project's language. The conversation is not a
document and carries no language rule of its own beyond where it is
set, below.

## The conversation language is an instance fact

What language the working conversation runs in is not a property of
the system and is not a rule of any project. It is per-instance
configuration: it lives in `CLAUDE.local.md` at the engine root, a
file of the instance that is kept out of the repository, and every
command reads it from there. `CLAUDE.md`, the operating file checked
into the engine, names the conversation language only as a thing
that exists, never by value.

Because it is an instance fact, the conversation language never
appears in anything that faces outward. The README and the other
outward-facing renders state only the output-language rule. The
document language is the project's own; the conversation language is
the person's.

## See also

- [Set up the forge](../start/setup.md): where the conversation language is set.
