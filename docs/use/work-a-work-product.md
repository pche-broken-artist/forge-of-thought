---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: b87e86b0aeea7aca
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

`/work` is the command that makes an output of a project with work of
its own, such as a model, an analysis or a worked task. This page is
for you when you want to list a project's work products, write the
specification of one, or have its file made. The principal is the
person whose thinking is being forged; "you" is the principal. The
ledger is the state report that a script makes from the project's
documents at read time.

A work product is two files in the project's `work/` folder. The
specification, `work/<name>.spec.md`, holds the way and the why. The
file, `work/<name>.<ext>`, holds the content and is named by the work
alone.

## When to use it

- You want to see which work products the project has and whether
  each is up to date.
- You want a new work product: its specification is to be written and
  its file made.
- You have worked a file by hand and do not want it remade.

## The command

```
/work [name] [slug]
```

Bare `/work` lists the roster. `/work <name>` works one product. The
slug names the project; where it is not clear from the conversation,
Claude asks. A real example of a line you can type:

```
/work <name> <slug>
```

## What happens

### Bare: the roster

1. Claude remakes the ledger with its script and reads the Work table.
   You should now see one line per work product with its file, its
   specification and version, its inputs, when it was made and its
   state.
2. The state is one of three words. `current` means the file was made
   from the specification as it stands. `stale` means the file is
   missing or the specification has moved on. `by hand` means you
   worked the file yourself and it is not to be remade. The Work table
   and its words are described in [Ledger](../reference/ledger.md).
3. Claude recommends a next step only where the conversation suggests
   one. You should now see a recommendation, or none.

### With a name: the specification

1. If `work/<name>.spec.md` does not exist, Claude asks first. On your
   word it is born from its template as a draft, with its history
   companion `work/<name>.spec.history.md` beside it. You should now
   see both files, and a row in the Work table with Made `—` and the
   state `stale`.
2. Claude reads the inputs the specification names, as they stand. The
   intent and the project's threads are read where they are among the
   inputs.
3. You work the specification with Claude in one of two ways.
   - Handed over: you give a few sentences of what you want, Claude
     works the specification alone from them, from research and from
     the sources, and returns a proposal. With it come its assumptions
     and its choices, each choice with what it was chosen against.
   - Found together: Claude interviews you, one question per message.

   You should now see a proposal or the questions.
4. Claude reflects the round back. On your word it writes once for the
   round: the specification is rewritten for coherence, unused
   placeholders and template comments are deleted, and the records are
   appended to the history companion. You should now see the
   specification and its companion changed.
5. Approval of the specification is your word alone. It follows the
   house scheme of versions, where a whole number is an approved one.

### With a name: the file

1. On your word, in the same round or a later one, Claude makes
   `work/<name>.<ext>` as the specification's `## Making` section says.
   The file carries of the specification only what that section says
   it carries. You should now see the file in `work/`.
2. Claude records the making in the specification's history. You
   should now see the Work row read `current`, with the time it was
   made.
3. Claude remakes the ledger and names what it wrote, where, and what
   the Work row says.

### A file you worked by hand

You can tell Claude that a file is worked by hand and is not to be
remade. The row then reads `by hand`. Claude never remakes such a file
on its own. It names the file and offers.

A file by hand carries the states of the work and its wording. If you
change the way or the why in it, that is its task, its inputs, its
method or what it assumes, the change is carried into the
specification in the same round and written with it. The record in the
specification's history names the change of the file.

## The specification

The specification has these sections, in this order:

- `Task`: what is asked, for whom, and what the file is to show.
- `Inputs`: items by ID and files by path, as they stand, never
  copied.
- `Method`: how the work is done, such as the model, the steps and the
  structure of the file.
- `Assumptions`: each an ASM item. The section is deleted if empty.
- `Open`: each a TBC item with an owner and what would close it. The
  section is deleted if empty.
- `Making`: how the file is made from the specification, by what
  means, in what format and language, and what of the specification
  the file carries.

The header carries the version, the status (`draft`, `approved` or
`superseded`), the project and the file the specification makes. The
specification cites and never copies. It is in the project's language;
the file is in whatever language the work needs, and `Making` says
which.

## What you have afterwards

- `work/<name>.spec.md` and its history companion, with the working
  of each round recorded.
- `work/<name>.<ext>`, once you have asked for it to be made.
- A Work row that says `current`, `stale` or `by hand`.

A conclusion that is to hold does not live in the work product. It
goes into the intent first, as described in
[Forge the intent](forge-the-intent.md). What a work product is, and
why it is neither an artefact of the chain nor a render, is explained
in [The work product](../about/the-work-product.md).

## If something goes wrong

- If the project is ambiguous, Claude asks which one you mean before
  it does anything.
- If a row reads `stale` and you did not expect it, a making is not
  recorded in the specification's history, or the specification has
  been changed since. Ask for the file to be made again.
- If a file reads `by hand`, `/work` will not remake it. Tell Claude
  if you want the file remade from the specification instead.

## A worked example

You want an analysis called `<name>` in the project `<slug>`.

1. You type `/work <name> <slug>`. The specification does not exist,
   so Claude asks whether to create it. You say yes. You should now
   see `work/<name>.spec.md` and `work/<name>.spec.history.md`.
2. You hand over three sentences of what the analysis is for. Claude
   reads the inputs, works the specification alone and returns a
   proposal with its assumptions and choices listed.
3. You judge the proposal, change two points and say `write`. You
   should now see the specification rewritten and the records
   appended.
4. You ask for the file. Claude makes `work/<name>.<ext>` as `Making`
   says and records the making. You should now see the Work row read
   `current`.
5. Later you edit the file yourself and tell Claude it is by hand. A
   bare `/work` now shows `by hand` in its state column.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
