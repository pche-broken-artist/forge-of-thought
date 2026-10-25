---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 13b65ead49e90063
inputs:
  - .claude/skills/challenge/SKILL.md
  - .claude/skills/challenger-contract/SKILL.md#Output
---

# Challenge the thinking

This page shows how to have a challenger persona attack the substance of your thinking with `/challenge`. It is for the principal, the person whose thinking is being forged. A persona is an isolated subagent (a separate Claude run that does not see your conversation) with one set of blind spots to hunt.

## When to use it

Use it when you want the substance of a document tested: whether it is aimed at the right thing, not whether it is well written. Document quality is never what a challenge judges.

Run it before the next layer is first derived from the target. For the intent, that means before the first layer below it. An accepted challenge is cheap to absorb at that point. Run it again after any major shift of direction. Running it on a near-final artefact is late but not useless.

## The command

```
/challenge [persona] [artefact|path] [slug]
```

All three arguments are optional.

- Bare `/challenge` lists the personas and recommends which fits the project's subject. The recommendation is never a gate.
- `persona` names the challenger to run.
- `artefact|path` is the target: an artefact named as `/forge` names it, or any file of the project by its path. Without a target, the persona reads the whole chain.
- `slug` names the project. Claude infers it from context and asks if it is ambiguous.

A typical line:

```
/challenge <persona> 10-intent
```

The personas of today are listed in [Challenger personas](../reference/challenger-personas.md).

## What happens

1. Claude makes the project's ledger first, so that the agent reads a current file. The ledger is the single state file of a project, built from its documents.

   You should now see the ledger remade before the persona starts.

2. Claude invokes the persona's agent on the project and names the target. It passes the project path and the target, nothing else. The agent attacks the substance of the target and never its document quality. It returns a report with three to seven challenges ordered by severity, what is strong, and the questions it cannot answer from the documents.

   You should now see the agent's run finish and return its report to Claude.

3. Claude gives each challenge its numbered identifier and files the report word for word in the project's `challenges/` folder under a unique dated name. Nothing is added, dropped or reworded but the identifiers. It then remakes the ledger.

   You should now see a new dated file in `challenges/` and the challenges listed in the ledger.

4. Claude presents the report to you. First comes the overall read, then each challenge compressed to two or three sentences. Claude does not defend earlier drafting choices. Where it disagrees with a challenge, it says so plainly and separately, marked as its own view.

   You should now see the overall read, the compressed challenges and, set apart, any disagreement of Claude's marked as its own.

5. Where the answer to one of the challenger's open questions exists in your conversation but not in the documents, Claude answers it and flags that to you. Such a question usually means something true is missing from the document.

   You should now see those answers flagged.

6. Claude offers a walkthrough of the challenges. A walkthrough settles a list of items one per message, each closed by a verdict line. See [Walk through a list](walk-through-a-list.md).

   You should now see the offer of a walkthrough.

## What you have afterwards

- The report filed in `challenges/`, immutable.
- Each challenge in the ledger, with its state.
- After a walkthrough, each challenge settled. The verdict `accept` means the challenge is mended through `/forge` in the artefact it concerns, and its state becomes `accepted`. The other verdicts are the walkthrough's.

A rejected challenge is a normal, healthy outcome. So is a challenge that survives three rounds unresolved: park it and move on.

## If something goes wrong

- If you decline the walkthrough, the challenges wait.
- If the project is ambiguous, Claude asks which one you mean.
- If you are unsure which persona to pick, run bare `/challenge` and take the recommended fit.

## A worked example

You have written the intent of a project with the slug `my-project` and have not yet derived anything below it.

```
/challenge
```

Claude lists the personas and recommends one for the subject. You choose it:

```
/challenge <persona> 10-intent my-project
```

Claude remakes the ledger, runs the persona on the intent and files the report in `challenges/`. It tells you the overall read, then five challenges, most severe first, each in two or three sentences. It adds one line marked as its own view, where it disagrees with the fourth. You take the offered walkthrough: you accept two challenges, reject the fourth and park the fifth. The two accepted ones are mended through `/forge` in the intent.

## See also

- [Challenger personas](../reference/challenger-personas.md): the personas of today.
- [Walk through a list](walk-through-a-list.md): settling the challenges one by one.
- [The challenger](../about/the-challenger.md): what the challenger judges and why it may be wrong.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
