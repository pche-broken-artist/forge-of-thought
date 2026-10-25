---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: ef9bad232f703f29
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

This page shows how you make an output of the project that needs work of its own, such as a model, an analysis or a worked task, with `/work`. It is for the principal (the person whose thinking is being forged) who wants that output made, and kept honest about the way and the reason it was made. What a work product is, and why it is neither an artefact of the chain nor a render, is explained in [The work product](../about/the-work-product.md).

A work product is two files in the project's `work/` folder. The specification, `work/<name>.spec.md`, holds the way and the why. The file, `work/<name>.<ext>`, holds the content.

## When to use it

- You want an output that is made with work of its own and is not a document of the chain.
- You want to see which work products the project has and whether each is up to date.
- You have worked a work product's file by hand and want it left alone.

## The command

```
/work [name] [slug]
```

Both words are optional. Without a name the command lists the project's work products. With a name it works that product. The slug names the project; where it is left out, Claude infers the project from the conversation and asks if that is ambiguous.

A line you can type as it stands:

```
/work <name>
```

## What happens

### Bare: the roster

1. Claude remakes the ledger (the file that holds the state of the project, made from its documents each time it is read) with its script.
   You should now see the ledger's Work table.
2. Claude lists each work product from that table:
   - its file
   - its specification and the specification's version
   - its inputs
   - when it was made
   - its state

   You should now see one entry per work product, and a next step only where the conversation suggests one.

The three states are `current`, `stale` and `by hand`. Their meaning is in [Ledger](../reference/ledger.md).

### With a name: the specification

1. Claude looks for `work/<name>.spec.md`. If it does not exist, its birth is a step of its own and happens on your word. The specification comes from the work template as a first draft, with its history companion `work/<name>.spec.history.md` beside it.
   You should now see two new files, and the Work table showing the product with no made date and the state `stale`.
2. Claude reads the inputs the specification names, as they stand. Where the intent is among them, it reads the project's threads too.
   You should now see Claude working from the named inputs and not from memory.
3. You choose how the specification is worked.
   - Handed over: Claude works it alone from what you gave it, from research and from the sources. It returns a proposal with its assumptions listed and each choice listed with what it was chosen against.
   - Found together: Claude interviews you, one question at a time.

   You should now see either a proposal with its assumptions and choices, or the first question of the interview.
4. Claude reflects the round back to you. It writes once, on your word: the specification rewritten for coherence, unused placeholders and template comments removed, and records added to the history companion. Where the file had been made before, a record puts the state back to `stale`.
   You should now see the names of the files written and, in the specification, the sections Task, Inputs, Method, Making, and Assumptions and Open where they have content.

The specification cites its inputs by ID and by path and never copies them. Its assumptions are written as ASM items and its open matters as TBC items, each open matter with an owner and what would close it. Its approval, from version 1.0 on, is your word alone.

### With a name: the file

1. On your word, in the same round or a later one, Claude makes `work/<name>.<ext>` as the specification's Making section says: by what means, in what format and in what language. The file carries of the specification only what Making says it carries.
   You should now see the file in `work/`.
2. Claude records the making in the specification's history. The Work table reads that record and shows the state `current`.
   You should now see the Work row with its made date and the state `current`.
3. Claude remakes the ledger and names what it wrote and where, and what the Work row says.
   You should now see that summary.

### A file you worked by hand

If you have worked the file by hand and do not want it remade, say so. The state becomes `by hand` on your word. Claude never remakes such a file on its own judgement. It may name the file and offer.

A file by hand carries the states of the work and its wording. If you change the way or the reason in it, that is, its task, its inputs, its method or what it assumes, the change is carried into the specification in the same round and written with it. The record in the specification's history names the change of the file.

## What you have afterwards

- A specification in `work/` with its history companion, which says the way and the why.
- The file, made from the specification, in the language and format the specification gave.
- A Work row that reads `current`, or `by hand` for a file you keep.

A conclusion that is to hold does not live in a work product. It goes into the intent first, as described in [Forge the intent](forge-the-intent.md).

## If something goes wrong

- The roster is empty: the project has no work product yet. Name one, and its specification is born on your word.
- The Work row reads `stale`: the specification has no making recorded, or a change was written after the last making. Make the file again on your word, or mark it `by hand` if you keep it.
- The project is ambiguous: Claude asks which project is meant. Give the slug.

The inputs record no further stop conditions or messages of the command.

## A worked example

You want a model of how orders move through a process. The product is called `<name>`.

1. You type `/work` and see that the project has no work product with this name.
2. You type `/work <name>`. Claude proposes to begin a specification and a history companion. You say yes. The Work table shows `<name>` as `stale`.
3. You hand the task over in two sentences. Claude returns a proposal. It lists two assumptions and one choice, with what that choice was chosen against. One open matter is recorded with an owner. You answer, and Claude reflects the round back. You say write, and the specification is written once.
4. You say make it. Claude makes `work/<name>.<ext>` as Making says and records the making in the specification's history.
5. You type `/work` again. The row for `<name>` shows its file, the specification and its version, its inputs, the made date and the state `current`.
6. Later you edit the file by hand and want it kept. You say so, and the row reads `by hand`.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
