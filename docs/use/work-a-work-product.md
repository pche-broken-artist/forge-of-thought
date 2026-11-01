---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 12606bca01997e10
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

This page shows how you make an output of the project that has work of its own, such as a model, an analysis or a worked task, with `/work`. It is for you as the principal, the person whose thinking is forged. What a work product is, and why it is neither an artefact nor a render, is explained in [The work product](../about/the-work-product.md). Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use `/work` when the project needs a file that is made by work, not composed as a document of the chain and not generated from the chain. A work product is two files in the folder `work/`:

- the specification `work/<name>.spec.md`, which holds the way and the why;
- the file `work/<name>.<ext>`, which holds the content.

Use it bare to see which work products the project has.

## The command

To see the roster of the project's work products:

```
/work
```

To work one product, with a name and optionally the slug of the project:

```
/work <name> <slug>
```

Claude infers the project from the conversation. If it is ambiguous, Claude asks which one you mean.

## What happens

### Bare: the roster

1. Claude remakes the ledger (the file that holds the state of the project, made by a script each time it is read) and reads its Work table.
2. Claude lists each work product with its file, its specification and the specification's version, its inputs, when it was made and its state.

You should now see one line per work product. The state is one of:

- `current`: the file was made from the specification as it stands.
- `stale`: the specification has changed since the file was made, or the file was never made. A product that has no making yet shows `—` for the date and `stale`.
- `by hand`: you worked the file yourself and do not want it remade.

The table and its state words are described in [Ledger](../reference/ledger.md). Claude recommends a next step only where the conversation suggests one.

### With a name: the specification

1. If `work/<name>.spec.md` does not exist yet, Claude proposes to create it. It is born on your word, as a step of its own, from the work template as a draft, together with its history companion (the append-only file beside it that records every change).

   You should now see the new specification and its history companion, and the work product in the roster as `stale`.

2. Claude reads the inputs the specification names, as they stand. Where the intent is among them, it reads the project's threads too.

   You should now see Claude work from the named inputs and nothing else.

3. You work the specification with Claude, in the way you choose:

   - Handed over: you give Claude a few sentences, and it works the specification alone from them, from research and from the sources. It returns a proposal with its assumptions listed and each of its choices named with what it was chosen against.
   - Found together: Claude interviews you, one question at a time.

   The specification points to its inputs and never copies them. Assumptions are written as ASM items and open matters as TBC items, each open matter with an owner.

   You should now see a proposal, or the answers gathered in the interview, reflected back to you before anything is written.

4. At the end of the round Claude asks whether to write, and writes once, on your word. It rewrites the specification for coherence, deletes unused placeholders and template comments, and appends the records to the history companion. When a file had already been made, a record marks the product `stale`.

   You should now see Claude name what it wrote and where.

5. Claude makes the file `work/<name>.<ext>` on your word, in the same round or a later one. The `## Making` section of the specification says how: by what means, in what format and language, and what of the specification the file carries. Claude then records the making in the specification's history.

   You should now see the file in `work/`, and the Work row read `current`.

6. Claude remakes the ledger and ends by naming what was written, where, and what the Work row says.

### A file you worked by hand

If you have worked the file yourself and do not want it remade, tell Claude. On your word the product is recorded as `by hand`. Claude never remakes such a file on its own judgement. It may name the file and offer, and you decide.

A file by hand carries the states of the work and its wording. If you change in the file the way or the why, that is its task, its inputs, its method or what it assumes, the change is carried into the specification in the same round and written with it. The record in the specification's history names the change of the file.

## The specification

The specification has these sections:

- `Task`: what is asked, for whom, and what the file is to show.
- `Inputs`: items by ID and files by path, as they stand, never copied.
- `Method`: how the work is done, such as the model, the steps and the structure of the file.
- `Assumptions`: the ASM items. Left out when empty.
- `Open`: the TBC items, each with an owner and what would close it. Left out when empty.
- `Making`: how the file is made from the specification. It is never copied into the file.

The specification follows the language of the project. The file is in whatever language the work needs, and `Making` says which.

## What you have afterwards

- A specification `work/<name>.spec.md` with its history companion.
- A file `work/<name>.<ext>`, once you have asked for it to be made.
- A Work row in the ledger that reads `current`, or `by hand` where you said so.

Approval of the specification, from version 1.0 on, is your word as the house scheme of versions has it.

A conclusion that is to hold does not live in the work product. It goes into the intent first, and the work then cites it. How the intent is worked is in [Forge the intent](forge-the-intent.md).

## If something goes wrong

- The project is ambiguous: Claude asks which project you mean. Give the slug.
- The roster shows `stale` after you changed the specification: the file is out of date. Ask Claude to make it again.
- The roster shows `stale` and `—` for a product just born: the file has not been made yet. This is the normal state until a making is recorded.

## A worked example

You are in a project with the slug `<slug>` and want an analysis called `<name>`.

1. You type `/work <name> <slug>`. The specification does not exist, so Claude proposes to create it and its history companion. You agree.
2. You hand Claude two sentences about what the analysis is to show. Claude returns a specification proposal with a list of assumptions and choices. You answer, Claude reflects the answers back, and on your word it writes the specification once.
3. You say the file may be made. Claude makes `work/<name>.<ext>` as `Making` says and records the making.
4. You type `/work`. The roster shows `<name>` with its file, its specification and version, its inputs, the day it was made and the state `current`.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
