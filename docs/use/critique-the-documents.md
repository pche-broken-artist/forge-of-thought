---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: a03f0946f9a90cc0
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

`/critique` runs a critic lens on the quality of a project's documents. This page is for the principal, the person whose thinking is forged, who wants the documents read by a reviewer that has not seen the conversation.

## When to use it

Use it when you want to know how well the documents are written, never whether their substance is right. A lens judges document quality only. Nothing runs by itself: no lens runs at a save, and a release offers the lens `essence` once. Every other run is your word.

## The command

```
/critique essence my-project
```

The general form is `/critique [lens] [artefact|path] [slug]`. Every part is optional.

- Bare `/critique` lists the lenses and recommends the one that fits the project's state. The recommendation is advice, never a gate.
- With a lens, the run starts.
- A target narrows the run to one artefact, named as `/forge` names it, or to any file of the project by its path. The file is read with the chain around it.
- The slug names the project. Claude infers it from context and asks when it is ambiguous.

The lenses of today are on the page [Critic lenses](../reference/critic-lenses.md).

## What happens

1. Claude makes the project's ledger afresh, so that the reviewer reads a current file. The ledger is the single record of state, made from the documents at the moment it is read.
   You should now see Claude start the run on the project.
2. Claude hands one isolated subagent (a reviewer that sees nothing of your conversation) the project path and the target, and nothing else. The subagent reads the project's documents and judges them through its lens. It writes no file.
   You should now see the run wait for the subagent's report.
3. The report comes back with its findings unnumbered. Claude gives each new finding its number in the project's sequence and files the report in `reviews/`, word for word, with only those numbers added. The file's name carries the date, the kind, the lens, the time and a short content hash. Claude then makes the ledger afresh, so that the findings become rows.
   You should now see a new file in `reviews/` and its name.
4. Claude presents the delta summary in your conversation language: the new findings, those verified resolved, those still open, those newly obsolete, and what awaits your verdict. Findings carry a severity and a category. For `essence`, the distillations come first, because the findings rest on them.
   You should now see the summary.
5. Claude offers a walkthrough of the open findings. A walkthrough settles a list one item per message, each closed with a verdict line. Here `accept` means an iteration of the artefact concerned through `/forge`, and the finding is then resolved. The other verdicts are the walkthrough's own. If you decline, the findings wait.
   You should now see the offer, or the first finding if you accept it.

The way to settle the findings is on the page [Walk through a list](walk-through-a-list.md).

## What you have afterwards

- One report in `reviews/`, immutable, under its dated name.
- Every new finding numbered and entered in the ledger.
- Open findings that wait for your verdict, or are settled if you walked through them.

## If something goes wrong

- A lens that is not on the roster does not run. Bare `/critique` shows the lenses there are.
- An ambiguous project is asked about, never guessed.
- The reviewer never edits an artefact and never proposes substance. It proposes the fix of the document only.

## A worked example

You have a project `my-project` and want its intent read for wording that a stranger could not follow.

1. You type `/critique essence my-project intent`.
2. Claude makes the ledger, runs the reviewer on the intent with the chain around it, and files the report under `my-project/reviews/` in a name made of today's date, `critique`, `essence`, the time and a hash.
3. Claude tells you how many findings are new, which are still open and what waits for you, and offers a walkthrough.
4. You say yes. The first finding arrives with its verdict line. You answer `accept`, and Claude iterates the intent through `/forge` to mend it.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
