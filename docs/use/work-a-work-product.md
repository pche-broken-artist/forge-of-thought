---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 3fa29fb79f596671
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

This page shows how you make an output of the project that has work of its own, such as a model, an analysis or a worked task, with `/work`. It is for the principal, the person whose thinking is being forged. A work product is two files in the project's `work/` folder: a specification that holds the way and the why, and the file that holds the content. The page [The work product](../about/the-work-product.md) says what a work product is and why it is neither an artefact nor a render.

## When to use it

- You want to see which work products the project has and whether each is up to date.
- You want to start a new work product.
- You want to rework the specification of an existing one, or make its file again.
- You have worked a file by hand and want it left alone.

## The command

```
/work [name] [slug]
```

Both arguments are optional. Without a name, the command lists the work products. With a name, it works that work product. Without a slug, Claude infers the project from context and asks if that is ambiguous.

A bare command, as it stands:

```
/work
```

A command with a placeholder name:

```
/work <name>
```

## What happens

### Bare: the roster

1. Claude remakes the ledger with its script, `python scripts/forge-ledger.py <slug>`, and reads the ledger's Work table.
   You should now see one line per work product: its file, its specification with the version, its inputs, when it was made and its state.
2. The state is one of three words: `current`, `stale` or `by hand`. [Ledger](../reference/ledger.md) lists the Work table and its state words.
   You should now see, for a work product not yet made, `—` as the date and `stale` as the state.
3. Claude recommends a next step only where the conversation suggests one.

### With a name: the specification

1. If `work/<name>.spec.md` does not exist, Claude asks first. Its birth is a step of its own and runs on your word. The specification is made from its template, with its history companion `work/<name>.spec.history.md`.
   You should now see a specification at version 0.1, and a row in the Work table that reads `stale`.
2. Claude reads the inputs the specification names, as they stand. Where the intent is among them, it reads the project's threads too.
3. You choose how the specification is worked.
   - Handed over: Claude works it alone from what you gave it, from research and from the sources, and returns a proposal. The proposal lists what it assumed and what it chose, each choice with what it was chosen against.
   - Found together: Claude interviews you.

   You should now see a specification that cites its inputs and never copies them. Its sections are:
   - Task
   - Inputs
   - Method
   - Assumptions, as ASM items
   - Open, as TBC items, each with an owner
   - Making

4. Claude reflects the round back to you and writes once, on your word. The specification is rewritten for coherence, unused placeholders and template comments are deleted, and the records are appended to the companion.
   You should now see the specification and its history changed together. Approval of the specification, version 1.0 and on, is your word alone.

### With a name: the file

1. On your word, in the same round or a later one, Claude makes `work/<name>.<ext>` as the specification's `## Making` section says. The file carries of the specification only what `## Making` says it carries. The making is then recorded in the specification's history.
   You should now see the file in `work/`.
2. Claude remakes the ledger and names what it wrote and where, and what the Work row says.
   You should now see the row read `current`.

### A file you worked by hand

You may work the file yourself and not want it remade. On your word, it is marked `by hand`, with a record in the specification's history. Claude never remakes such a file on its own: it names the file and offers.

A file by hand carries the states of the work and its wording. If you change the way or the why in it, that is its task, its inputs, its method or what it assumes, the change is carried into the specification in the same round. The record in the history names the change of the file.

## What you have afterwards

- A specification `work/<name>.spec.md` and its history companion `work/<name>.spec.history.md`.
- A file `work/<name>.<ext>`, once you have asked for it to be made.
- A Work row in the ledger that says whether the file is `current`, `stale` or `by hand`.

## If something goes wrong

- The project is ambiguous: Claude asks which one you mean.
- The specification does not exist: nothing is written until you say so.
- The row reads `stale`: the file has not been made yet, or the specification has changed since. Ask for the file to be made again.

## Where a conclusion goes

A conclusion that is to hold goes into the intent first, through [Forge the intent](forge-the-intent.md). The specification cites the intent and does not take its place.

## A worked example

A work product named `<name>`, in a project with the slug `<slug>`.

1. You type `/work`. Claude lists the work products, and `<name>` is not among them.
2. You type `/work <name> <slug>`. Claude says no specification exists and asks to create it. You agree.
3. You hand the work over with a few sentences. Claude returns a proposal with its assumptions and choices.
4. You judge the proposal, and Claude reflects the round back. You say write. The specification and its history are written once.
5. You ask for the file. Claude makes `work/<name>.<ext>` as `## Making` says and records it.
6. Claude remakes the ledger and tells you the Work row reads `current`.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
