---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: bd79bf62034325ed
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

This page shows how you make an output of your project that has work
of its own, such as a model, an analysis or a worked task, with the
command `/work`. It is for the principal, the person whose thinking is
being forged, who wants such an output made and kept current. A work
product is two files in the folder `work/` of the project: a
specification that holds the way and the why, and a file that holds the
content. What a work product is, and why it is neither an artefact nor
a render, is explained in [The work product](../about/the-work-product.md).

## When to use it

- You want to see which work products the project has and whether
  each is up to date.
- You want a new output made with work of its own, and a record of how
  and why it was made.
- You want a file made again after its specification changed.
- You have worked a file by hand and want it left alone.

## The command

```
/work [name] [slug]
```

Both arguments are optional. A bare `/work` lists the work products.
`/work <name>` works the one called `<name>`. The slug names the
project; where it is left out, Claude infers the project from the
conversation and asks if that is ambiguous.

A real call looks like this, with a placeholder name:

```
/work cost-model
```

## What happens

### Bare: the roster

1. Claude remakes the ledger with its script and reads its Work table.
   The ledger is the state of the project, made at read time from its
   documents.
2. It lists each work product with its file, its specification and
   the version of that, its inputs, when it was made and its state.

You should now see one entry per work product. The state is one of
three words:

- `current`: the file was made from the specification as it stands.
- `stale`: the file is not made yet, or the specification has changed
  since.
- `by hand`: you worked the file yourself and it is not to be remade.

Claude recommends a next step only where the conversation suggests one.
The table and its state words are described in
[Ledger](../reference/ledger.md).

### With a name: the specification

1. If `work/<name>.spec.md` does not exist, Claude proposes to create
   it. It is born on your word, never as a by-product of something
   else. It comes from its template as version 0.1, together with its
   history companion, the file that records what changed and why.

   You should now see both files in `work/`, and the work in the
   roster as `stale`, with no date of making.

2. Claude reads the inputs the specification names, as they stand. Where
   the intent is among them, it reads the project's threads too.

   You should now see Claude naming what it has read.

3. You work the specification with Claude, in the way you choose. You
   can hand the work over with a few sentences of what you want, and
   Claude returns a proposal with what it assumed and what it chose. Or
   you can find the content together, by an interview of questions.

   You should now see a specification with these sections:

   - Task: what is asked, for whom and what the file is to show.
   - Inputs: items by ID and files by path, cited and never copied.
   - Method: how the work is done.
   - Assumptions: the things taken as true, each an ASM item.
   - Open: the open matters, each a TBC item with an owner and what
     would close it.
   - Making: how the file is made from the specification.

4. Claude reflects the round back and asks whether to write. It writes
   once per round, on your word. It rewrites the specification for
   coherence, deletes the unused placeholders and the template's
   comments, and appends the records to the companion.

   You should now see the specification and its history updated, and
   Claude naming the file and section it wrote.

   Approval of the specification, version 1.0 and on, is your word
   alone.

### The file

5. You tell Claude to make the file, in the same round or a later one.
   It makes `work/<name>.<ext>` as the section Making says: by what
   means, in what format and language, and which part of the
   specification the file carries. The file is in whatever language
   the work needs. The specification follows the project's language.

   You should now see the file in `work/`.

6. Claude records the making in the specification's history. The Work
   table reads that record.

   You should now see the work product as `current` in the roster.

7. Claude remakes the ledger and ends by naming what it wrote, where,
   and what the Work row says.

### A file you worked by hand

If you worked a file yourself and do not want it remade, say so. The
file is then `by hand` on your word, and the record says so. Claude
never remakes such a file on its own judgement. It names the file and
offers.

A file by hand carries the states of the work and its wording. If you
change the way or the why in the file, that is its task, inputs,
method or assumptions, Claude carries the change into the
specification in the same round. The record in the specification's
history names the change of the file.

## What you have afterwards

- A specification `work/<name>.spec.md` with its history companion
  `work/<name>.spec.history.md`. They hold the way and the why.
- A file `work/<name>.<ext>`. It holds the content.
- A Work row in the ledger that tells you whether the file is
  `current`, `stale` or `by hand`.

A conclusion of the work that is to hold for the project does not stay
in the specification or the file. It goes into the intent first, as
described in [Forge the intent](forge-the-intent.md).

## If something goes wrong

The inputs record no stop conditions and no printed messages for this
command. Two situations are described:

- The project is ambiguous. Claude asks which project you mean. Name
  the slug as the second argument.
- A row reads `stale`. Either no file is made yet, or the
  specification has changed since the last making. Ask Claude to make
  the file again, or say that the file is `by hand`.

## A worked example

You have a project and want a cost model. You type the bare command to
see what exists.

```
/work
```

The roster has no row called `cost-model`. You type the name.

```
/work cost-model
```

Claude proposes to create `work/cost-model.spec.md` and its history
companion. You agree. You hand the work over with two sentences on what
the model is to show. Claude reads the inputs, drafts the sections and
shows what it assumed as ASM items and what stays open as TBC items.
You judge them, and Claude writes once, on your word.

Then you tell Claude to make the file as Making says. Claude writes
`work/cost-model.<ext>`, records the making in the history and remakes
the ledger. The roster now reads `current` for `cost-model`.

Later you edit the file by hand and say it is not to be remade. The
roster reads `by hand`.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
