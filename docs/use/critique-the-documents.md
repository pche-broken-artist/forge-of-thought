---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 69797cafb031cde9
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

`/critique` runs a critic lens on the quality of a project's documents. It is for the principal (the person whose thinking is being forged) who wants an independent reading of the documents. The lens judges how well the documents are written, never whether their substance is right.

## When to use it

Use it when you want the documents read by a reviewer that has not seen your conversation. Each lens reads the documents for one kind of fault. The lenses of today are listed in [Critic lenses](../reference/critic-lenses.md). What the critic judges, and why it is blind to substance, is explained in [The critic](../about/the-critic.md).

No lens runs by itself. A save runs none. A release offers the lens `essence` once. Every other run is your word.

## The command

To see the lenses and which one fits the project now:

```
/critique
```

To run one lens over the whole project:

```
/critique essence
```

To narrow the run, name a target after the lens. The target is an artefact, named as `/forge` names it, or any file of the project by its path. The optional last word is the project slug, given when it cannot be inferred from the context:

```
/critique essence intent my-project
```

A file given by path is read with the chain around it.

## What happens

1. Bare `/critique` lists the lenses and recommends one that fits the state of the project. The recommendation is advice, not a gate.
   You should now see the roster of lenses with one recommended.
2. With a lens, Claude first makes the project's ledger (the file that records the state of the project) afresh, so that the reviewer reads a current file.
   You should now see no output yet, only the run starting.
3. Claude starts one subagent (an isolated reviewer that sees none of your conversation) for the lens. It is given the project and the target, nothing else. It reads the project's documents and judges their quality through its lens. It writes nothing and returns its report.
   You should now see Claude waiting for the report.
4. The report comes back with its findings unnumbered. Claude gives each new finding its number, then files the report word for word in the project's `reviews/` folder. The file is named by its date, the kind (critique), the lens, the time and a short hash of its content. Claude then makes the ledger again, so that the findings appear in it.
   You should now see a new file in `reviews/`.
5. Claude presents the summary of what changed since the last run, in the language of your conversation: the new findings with their severity, those verified as resolved, those still open, those now obsolete, and what waits for your verdict. For `essence`, the distillations come first, because the findings rest on them.
   You should now see that summary.
6. Claude offers a walkthrough of the open findings. A walkthrough settles a list one item per message; see [Walk through a list](walk-through-a-list.md). The verdict `accept` means an iteration of the artefact concerned through `/forge`, and the finding is then marked resolved. The other verdicts are the walkthrough's. If you decline the walkthrough, the findings wait.
   You should now see the first finding, closed with the line of verdicts.

## What you have afterwards

- A report in `reviews/`, immutable, exactly as the reviewer returned it apart from the finding numbers.
- The new findings in the ledger.
- Open findings that wait for your verdict, or are settled if you took the walkthrough.

## If something goes wrong

- If the project cannot be inferred from the context, Claude asks which project is meant.
- A report is never filed twice at once. Reports of several reviewers are filed one after another, so that no finding number is given twice.
- If the lens you name is not in the roster, run bare `/critique` and take a name from it.

## A worked example

You have just iterated the intent of a project called `my-project` and want it read for quality.

1. You type `/critique` and see the roster. Claude recommends `essence`.
2. You type `/critique essence intent my-project`.
3. Claude makes the ledger, the reviewer reads the intent with the chain around it, and Claude files the report in `reviews/`.
4. Claude tells you: three new findings, one earlier finding verified as resolved, two still open. It offers a walkthrough.
5. You say yes. The first finding appears, you answer `accept`, and Claude iterates the intent through `/forge` to mend it.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
