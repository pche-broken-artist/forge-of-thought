---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 82a6d6f08ebeb50f
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

This page shows how you run a critic lens on the quality of a project's documents with `/critique`. It is for the principal, the person whose thinking is forged and who alone decides what happens to the result. A lens is one way of reading the documents, and each lens is run by its own isolated agent.

## When to use it

Use it when you want the documents of a project read for their quality: whether they are clear, consistent and complete in form. It never judges substance, which is the challenger's work. Every run is your word. No lens runs at a save. A release offers the lens `essence` once, in one sentence, and runs it only if you agree.

## The command

```
/critique [lens] [artefact] [slug]
```

All three parts are optional. A typed example:

```
/critique essence my-project
```

- `lens`: the lens to run. See [Critic lenses](../reference/critic-lenses.md) for the lenses of today.
- `artefact`: narrows the run to one artefact, named the way `/forge` names it. How the target narrows the run is stated by the lens itself.
- `slug`: the project. Claude infers it from context and asks if it is ambiguous.

Bare `/critique` runs nothing. It lists the available lenses and recommends which one fits the project's state, going by the fit each lens states. The recommendation is advice and never a gate.

## What happens

1. You give a lens. Claude starts the agent of that lens and passes it only the project and the target, if you named one.

   You should now see Claude waiting while the agent works; you see nothing of the agent's reading.

2. The agent reads the project's documents in isolation and judges their quality through its lens. It never sees your conversation with Claude.

3. The agent writes a dated report in `reviews/` and adds its findings to the project's ledger. The ledger is the file that holds the project's state. The report is immutable: it is never edited afterwards, and a second run on the same day gets a suffixed name.

   You should now see a new file `reviews/YYYY-MM-DD-critique-<lens>.md`.

4. Claude checks that the report was filed and that the ledger was updated. It repairs the ledger bookkeeping where needed, without touching the findings themselves.

5. Claude presents a delta summary in the conversation language. It names:
   - the new findings, each with its severity
   - the findings verified as resolved
   - the findings still open
   - the findings that became obsolete
   - what awaits your verdict

   For `essence`, the distillations come first, because the findings rest on them.

   You should now see the delta summary.

6. Claude offers a walkthrough of the open findings. A walkthrough settles a list one item per message, as described in [Walk through a list](walk-through-a-list.md). Answering `accept` on a finding means an iteration of the artefact concerned through `/forge`, and the finding is then marked `resolved`. The other verdicts are those of the walkthrough.

   You should now see the offer of a walkthrough. If you decline it, the findings wait.

## What you have afterwards

- One immutable report in `reviews/`, in English.
- New findings in the ledger, each with its own ID, a severity and a category. [The critic](../about/the-critic.md) says what they mean.
- Earlier findings re-tested and their states updated.
- Nothing changed in any document of the chain until you accept a finding.

## If something goes wrong

- If no project is clear from context, Claude asks which one you mean.
- If the report or the ledger update is missing when the agent returns, Claude repairs the ledger bookkeeping. It does not change what the findings say.
- If you decline the walkthrough, nothing is lost: the findings stay open in the ledger until you settle them.

## A worked example

You have just revised the intent of a project with the slug `my-project` and want it read before a release.

1. You type `/critique` to see the roster. Claude lists the lenses and recommends one.
2. You type `/critique essence intent my-project`.
3. Claude reports: two new findings, one earlier finding verified resolved, one still open, none obsolete.
4. Claude offers a walkthrough. You accept it and take the first finding with `accept`.
5. The intent is iterated through `/forge`, and the finding is marked `resolved`.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
