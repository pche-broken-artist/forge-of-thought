---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 11ed7d3ac3689f67
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

`/critique` runs one critic lens on the quality of a project's documents and brings back a report of findings. This page is for the principal (the person whose thinking is forged) who wants a second reading of the documents without handing over any decision.

## When to use it

Use it when you want the documents judged as documents: whether they are clear, consistent and complete in their form. A lens never judges the substance of the thinking. For that, the forge has the challenger, which is a different command. What the critic is and why it is blind to substance is explained in [The critic](../about/the-critic.md).

No lens runs by itself at a save. A release offers the lens `essence` once. Every other run happens on your word.

## The command

```
/critique [lens] [artefact|path] [slug]
```

Typed as it stands, with a placeholder slug:

```
/critique essence 10-intent my-project
```

- Bare `/critique` lists the lenses and recommends the one that fits the state of the project. The recommendation is never a gate.
- With a lens, the command runs it. The lenses of today are in [Critic lenses](../reference/critic-lenses.md).
- The target is optional. It is either one artefact, named as `/forge` names it, or any file of the project by its path. A file is read with the chain around it. Without a target, the whole chain is read.
- The slug is inferred from the context. If it is ambiguous, Claude asks.

## What happens

1. Claude makes the project's ledger first, so that the reader works from a current file. The ledger is the forge's record of state, made from the documents each time it is read.

   You should now see the ledger remade, with no message of its own.

2. Claude starts one isolated subagent for the lens, that is a separate Claude that never sees your conversation. It is given only the project and the target. It reads the project's documents and judges their quality through its lens.

   You should now see Claude waiting while the lens reads.

3. The report comes back with its findings unnumbered. The agent writes no file. Claude gives each new finding its next free number and files the report in `reviews/`, word for word, under a name made of its date, the kind, the lens, the time and a short content hash. Only the numbers are added.

   You should now see a report filed in the project's `reviews/` folder, and the ledger remade with its findings as rows.

4. Claude presents the delta summary in the conversation. It names the new findings, with the severity of each, the findings verified as resolved, those still open, those newly obsolete, and what awaits your verdict. For `essence`, the distillations come first, because the findings rest on them.

   You should now see the delta summary.

5. Claude offers a walkthrough of the open findings. A walkthrough settles a list one item at a time, each closed with a verdict line. The method is described in [Walk through a list](walk-through-a-list.md). Answering `accept` on a finding means an iteration of the artefact concerned through `/forge`, and the finding is then marked resolved. The other verdicts are those of the walkthrough.

   You should now see the first finding put to you, or, if you decline the walkthrough, the findings left waiting.

## What you have afterwards

- A report in `reviews/`. It is never edited again.
- New findings in the ledger, each with its own number.
- Your verdicts on the findings, if you took the walkthrough.

## If something goes wrong

- If the project cannot be inferred from the context, Claude asks which one you mean.
- If you decline the walkthrough, nothing is lost: the findings stay open until you settle them.
- A finding the report marks as newly obsolete is not closed by the run. It is closed by a decision at the walkthrough.

The inputs name no other stop condition and no message of the command.

## A worked example

You have just revised the intent of a project with the placeholder slug `my-project` and want it read.

1. You type `/critique` and see the roster with a recommended lens. You choose `essence`.
2. You type `/critique essence 10-intent my-project`.
3. Claude remakes the ledger, the lens reads the intent with the chain around it, and the report returns.
4. Claude files it as `reviews/<date>-critique-essence-<time>-<hash>.md` and says: three new findings, one earlier finding verified resolved, two still open, none newly obsolete.
5. Claude offers a walkthrough. You take it, answer `accept` to the first finding, and Claude iterates the intent through `/forge` to mend it.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
