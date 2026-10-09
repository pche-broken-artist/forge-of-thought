---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About languages

This page explains which language each part of the forge is written
in, and why. It is for anyone who uses the forge or is weighing it up
and wants to know what is fixed and what is theirs to choose. It was
put together from two files: the rule as `CLAUDE.md` states it among
its prime directives, and the reason as the forge's own intent gives
it.

## One output language per project

The forge as a system dictates only one thing about language: a
project has one output language. The artefacts of the chain, the
intent, the assignment and every later layer, are written in the
language the project's ledger header declares in its `language`
field (an ISO 639-1 code). When the header declares none, the
language is English.

## What is always English

Everything else a project holds is always English, whatever the
project's language: its records, its state, its research and its
recipes.

The reason is who reads them. These documents are read by Claude, by
the reviewers and by the checks, and never handed to the recipients
of the work. One operating language is what lets them read every
project the same way.

English is also the notation throughout, in every document: the ID
prefixes, the word `shall`, the status words and the front-matter
keys.

## The exceptions

- **Briefs.** The briefs (`00-brief*.md`) are the one exception among
  the artefacts: each is kept in whatever language it was written in.
- **Renders.** A render may be in any language its recipe declares.
  A translation is a render.

## The conversation language

The language you and Claude talk in is not a property of the system.
It is an instance fact, set in `CLAUDE.local.md` at the engine root,
a file that is gitignored and filled by `/setup` on a new machine,
and every command reads it from there. It is never written into the
operating layer, and it never appears in outward-facing renders, the
README among them: those state only the output-language rule.

## Translate on write

The conversation and the project may run in different languages.
What is said in the conversation is translated when it is written, so
that each document lands in the language its kind calls for: the
project's language for the artefacts, English for everything else the
project holds, with the briefs and the renders as above.

## See also

- [Set up the forge](../start/setup.md): where the conversation
  language is set.
