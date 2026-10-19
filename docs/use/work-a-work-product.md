---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 208f05adfd84b9d9
inputs:
  - .claude/skills/work/SKILL.md
  - templates/work.md
  - templates/ledger.md#Work
---

# Work a work product

`/work` is the command that makes an output of your project that has work of its own, such as a model, an analysis or a worked task. It is for you as the principal, the person whose thinking is being forged. Bare, it lists the project's work products. With a name, it works the specification of one of them with you and makes its file. A [work product](../about/the-work-product.md) is two files in `work/`: the specification, which holds the way and the why, and the file, which holds the content.

## When to use it

- You want to see which work products the project has and whether each is up to date.
- You want a new output with work of its own, and you want its way and its reasons written down beside it.
- You want to change the way a work product is made and remake its file.
- You have worked a file by hand and want Claude to leave it alone.

A conclusion that is to hold for the project does not belong in a work product. It goes into the intent first, as described in [Forge the intent](forge-the-intent.md).

## The command

```
/work [name] [slug]
```

The slug names the project. Claude infers it from the conversation and asks when it is ambiguous.

- `/work` alone shows the roster.
- `/work <name>` works the work product with that name, for example `/work sizing-model`.

## What happens

### Bare `/work`: the roster

1. Claude remakes the project's ledger with its script. The ledger is the file that holds the project's state.
2. Claude reads the Work table of the ledger and lists each work product with:
   - its file
   - its specification and the version of it
   - its inputs
   - when it was made
   - its state

   You should now see one line per work product, each in one of the states `current`, `stale` or `by hand`. The states are explained in [Ledger](../reference/ledger.md).
3. Claude recommends a next step only where the conversation suggests one.

### `/work <name>`: the specification and the file

1. **The specification is born, if it does not exist yet.** Claude proposes it as a step of its own, and it happens on your word. The specification `work/<name>.spec.md` is made from its template as version 0.1, with its history companion `work/<name>.spec.history.md` beside it. You should now see both files in `work/`, and a row for the work product in the Work table, with Made `—` and the state `stale`.
2. **Claude reads the inputs the specification names**, by ID and by path, as they stand. Where the intent is among them, it reads the project's threads with it. You should now see Claude say what it has read.
3. **The specification is worked with you**, in the way you choose:
   - Handed over: you give a few sentences of what you want, Claude works the specification alone from them, from research and from the sources, and returns a proposal. The proposal lists what Claude assumed and what it chose, each choice with what it was chosen against.
   - Found together: Claude draws the specification out of you by an interview, one question at a time.

   The specification cites its inputs and never copies them. You should now see a proposal or the next question.
4. **The round is reflected back and written once.** Claude restates what was understood, and on your word it writes the specification, rewritten for coherence, with unused placeholders and template comments removed, and appends the records to the companion. You should now see Claude name the file and the section it wrote. Approval of the specification, from version 1.0 on, is your word alone.
5. **The file is made on your word**, in the same round or a later one, as the specification's `## Making` section says. The file `work/<name>.<ext>` carries of the specification only what `## Making` says it carries. Claude then records the making in the specification's history. You should now see the file in `work/`.
6. **The ledger is remade.** Claude ends by naming what it wrote and where, and what the Work row now says. You should now see the state `current` in the row.

### A file you worked by hand

If you worked the file by hand and do not want it remade, say so and it becomes `by hand` on your word, with a record in the specification's history. Claude never remakes such a file on its own judgement. It names the file and offers.

A file by hand carries the states of the work and its wording. If you change the way or the why in it (its task, inputs, method or assumptions), Claude carries that change into the specification in the same round and writes it with it. The record in the history names the change of the file.

## The specification

The specification follows the template. Its sections are:

| Section | What it holds |
|---|---|
| Header | version, status (`draft` or `approved`), the project and the file it makes |
| Task | what is asked, for whom, and what the file is to show |
| Inputs | items by ID and files by path, as they stand, never copied |
| Method | how the work is done: the model, the steps, the structure of the file |
| Assumptions | assumptions, each with an ASM number; left out when there are none |
| Open | open questions, each with a TBC number, an owner and what would close it; left out when there are none |
| Making | how the file is made from the specification: by what means, in what format and language, and what of the specification the file carries |

The specification is written in the project's language. The file is in whatever language the work needs, which `## Making` says.

## What you have afterwards

- `work/<name>.spec.md`: the specification, with its version and status.
- `work/<name>.spec.history.md`: the history companion, with the records of the round.
- `work/<name>.<ext>`: the file, once you have let Claude make it.
- A Work row in the ledger that reads `current`, or `by hand` if you said so.

The row reads `stale` from the birth of the specification until a record of the making says otherwise.

## If something goes wrong

- The row says `stale` after you changed the specification: the file stands from an earlier making. Ask Claude to make it again on your word.
- The row says `stale` with Made `—`: the file has not been made yet. Ask Claude to make it.
- You do not want a hand-worked file remade: say it is `by hand`.
- The skill prints no error messages of its own. If the ledger script fails, Claude reports its message to you.

## A worked example

You want an analysis of how a pricing change would land, and you call it `sizing-model`.

1. You type `/work sizing-model`. There is no specification, so Claude proposes to make `work/sizing-model.spec.md` and its history companion and waits for your word.
2. You say yes. Both files appear, and the Work table shows the row with Made `—` and the state `stale`.
3. You hand the work over with two sentences of what you want. Claude reads the sources and returns a proposal, with its assumptions and each choice listed against the alternative it rejected.
4. You answer on the points you disagree with. Claude reflects the round back, you say `write`, and it writes the specification and the records.
5. You tell Claude to make the file. It writes `work/sizing-model.<ext>` as `## Making` says and records the making.
6. Claude remakes the ledger and tells you the row now reads `current`.

Later you find a conclusion in the analysis that the whole project should rely on. You do not leave it in the work product: you take it to the intent, as [Forge the intent](forge-the-intent.md) describes.

## See also

- [The work product](../about/the-work-product.md): what a work product is and why it is neither an artefact nor a render.
- [Forge the intent](forge-the-intent.md): where a conclusion that is to hold goes.
- [Ledger](../reference/ledger.md): the Work table and its state words.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
