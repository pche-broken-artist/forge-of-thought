---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 580e02c6f3a2782c
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

This page shows how you make an output of the project that has work of its own, such as a model, an analysis or a worked task, with `/work`. It is for the principal, the person whose thinking is being forged. A work product is two files in the `work/` folder of the project: a specification that says the way and the why, and the file that holds the content. What a work product is, and why it is neither an artefact nor a render, is on [The work product](../about/the-work-product.md).

## When to use it

- You want to see which work products the project has and in what state they are.
- You want to start a new work product.
- You want to change the specification of one, or make its file again.
- You have worked a file by hand and want it left alone.

## The command

```
/work [name] [slug]
```

Bare, `/work` lists the work products of the project. With a name, it works that product. The slug names the project and is needed only where Claude cannot tell which project you mean. A typed example, with a placeholder name:

```
/work cost-model
```

## What happens

**Bare `/work`: the roster.**

1. Claude reads the Work table of the project's ledger. The ledger is the file that holds the state of the project.
2. It lists each work product with its file, its specification and the version of it, its inputs, the date it was made and its state.
3. It recommends a next step only where the conversation suggests one.

You should now see one line of facts per work product, and a state that is `current`, `stale` or `by hand`. The three words are:

- `current`: the file was made from the specification as it stands.
- `stale`: the specification was written and no making followed.
- `by hand`: you worked the file yourself and do not want it remade.

**`/work <name>`: the specification and the file.**

1. If `work/<name>.spec.md` does not exist, Claude asks first. On your word it is born from the work template as version 0.1, with its history companion `work/<name>.spec.history.md` and a row in the Work table that has the made date `—` and the state `stale`. You should now see the two new files and the new row.
2. Claude reads the inputs the specification names, as they stand. Where the intent is among them, it reads the project's threads too.
3. You work the specification with Claude in one of two ways. You hand the work over with a few sentences of what you want: Claude works it alone from what you gave, from research and from the sources, and returns a proposal with its assumptions and its choices listed, each choice with what it was chosen against. Or you find it together: Claude interviews you. You should now see either a proposal or a first question.
4. Claude reflects the round back to you and writes once, on your word. The specification is rewritten for coherence, unused placeholders and template comments are deleted, the records are appended to the history companion, and the ledger row gets the new version and the state `stale`. You should now see Claude name the file and the section it wrote.
5. Claude makes the file on your word, in the same round or in a later one. It makes `work/<name>.<ext>` as the `## Making` section of the specification says, and the file carries of the specification only what that section says it carries. You should now see the ledger row with the inputs and their versions, the date made, and the state `current`.
6. Claude ends by naming what was written and where, and what the ledger row says.

Approval of the specification (version 1.0 and on) is your word, as in any versioned document.

## What the specification holds

The specification follows the work template. Its front-matter names the project and the file it makes. Its sections are these:

| Section | What it holds |
|---|---|
| Task | What is asked, for whom, and what the file is to show. |
| Inputs | Items by ID and files by path, as they stand, never copied. |
| Method | How the work is done: the model, the steps, the structure of the file. |
| Assumptions | The assumptions, numbered ASM. Deleted if there are none. |
| Open | The open matters, numbered TBC, each with an owner and what would close it. Deleted if there are none. |
| Making | How the file is made from the specification: by what means, in what format and language, and what of the specification the file carries. Never copied into the file. |

The specification is written in the language of the project. The file is in whatever language the work needs, and `## Making` says which.

## What you have afterwards

- The specification `work/<name>.spec.md` and its history companion.
- The file `work/<name>.<ext>`, once you have asked for it.
- A row in the Work table of the ledger. The table and its state words are on [Ledger](../reference/ledger.md).

## A file you want left alone

When you have worked the file by hand and do not want it remade, tell Claude. On your word the row is set to `by hand`. Claude never remakes such a file on its own judgement. If it thinks a remaking is due, it names the file and offers.

## A conclusion that is to hold

A conclusion of a work product that is to hold for the project does not stay in the specification or the file. It goes into the intent first, as described on [Forge the intent](forge-the-intent.md).

## If something goes wrong

- Claude cannot tell which project you mean: it asks. Give the slug.
- The row says `stale`: the specification was written and the file not made since. Ask for the making.
- The row says `by hand` and you want the file made again from the specification: say so, and Claude makes it on your word.

The skill prints no error messages of its own, so none are listed here.

## A worked example

You type:

```
/work cost-model
```

1. `work/cost-model.spec.md` does not exist, so Claude asks whether to create it. You say yes. You should now see the specification as version 0.1, `work/cost-model.spec.history.md`, and a Work row with the made date `—` and the state `stale`.
2. You hand it over: "a model of what the service costs per month, from the vendor offer in the sources". Claude reads the inputs and returns a proposal with its assumptions listed as ASM items and the open matters as TBC items, each with an owner.
3. You answer, Claude reflects the round back, and you say `write`. You should now see the specification at its new version, the records in the companion, and the row still `stale`.
4. You ask for the file. Claude makes `work/cost-model.<ext>` as `## Making` says. You should now see the row with the inputs and their versions, today's date and the state `current`.
5. Later you change the file by hand. You tell Claude it is yours to keep, and the row is set to `by hand`.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
