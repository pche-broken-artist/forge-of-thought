---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 61d25c04ad555cee
inputs:
  - .claude/skills/critique/SKILL.md
  - .claude/skills/critic-contract/SKILL.md#Output
---

# Critique the documents

This page shows how to run a critic lens on the quality of a project's documents with `/critique`. It is for the principal, the person whose thinking is forged, who wants an isolated reader to judge how well the documents are written. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you want the wording, structure and consistency of the documents judged, and not what they say. A lens judges document quality only, never substance. What the critic is and why it is blind to substance is explained in [The critic](../about/the-critic.md).

Every run is your decision. No lens runs when you save, and a release offers the lens `essence` once.

## The command

To see the lenses and which one fits the project now:

```
/critique
```

To run one lens on the whole chain, narrowed to nothing:

```
/critique <lens> <slug>
```

The optional target narrows the run to one artefact, named as `/forge` names it, or to any file of the project by its path. The file is read with the chain around it. The lenses of today are in [Critic lenses](../reference/critic-lenses.md).

## What happens

1. Bare `/critique` lists the available lenses and recommends the one that fits the project's state, by the fit each lens states for itself.
   You should now see the roster and a recommendation. It is a recommendation, never a gate.
2. With a lens, Claude first makes the project's ledger (the state of the project, made at read time) so that the critic reads a current file.
   You should now see the run start.
3. One isolated subagent (a reviewer that sees nothing of your conversation) reads the project's documents and judges their quality through that lens. It writes no file. It returns a report whose new findings carry no number yet.
   You should now see the run end with a report returned to Claude.
4. Claude gives each new finding its next free finding number and files the report in the project's `reviews/` folder. The text is kept word for word, with only the numbers added. The file is named after its date, the kind, the lens, the time and a short content hash.
   You should now see a new file in `reviews/`.
5. Claude makes the ledger again, so that the findings become rows of it.
   You should now see the findings counted as open in the ledger.
6. Claude presents the delta summary in the conversation language. It names the new findings with their severity, the ones verified resolved, the ones still open, the ones newly obsolete, and what awaits your verdict. For `essence`, the distillations come first, because the findings rest on them.
   You should now see the summary and an offer of a walkthrough.
7. Claude offers a walkthrough of the open findings, that is, settling them one by one. See [Walk through a list](walk-through-a-list.md). Here `accept` means an iteration of the artefact concerned through `/forge`, and the finding is then marked resolved. The other verdicts are the walkthrough's own. If you decline the walkthrough, the findings wait.
   You should now see the first finding, or the findings left waiting.

## What you have afterwards

- A report in `reviews/`, immutable from then on.
- Findings numbered in the project's sequence and counted in the ledger.
- Where you accepted a finding, a new iteration of the artefact through `/forge`.

## If something goes wrong

- If the project is ambiguous, Claude infers it from context and asks when it cannot.
- If a newly obsolete finding is named in the report, it is recorded with a decision at the walkthrough, not before.

The inputs name no other stop condition or message.

## A worked example

You run the lens that bare `/critique` recommended, on one artefact of the project `my-project`:

```
/critique <lens> intent my-project
```

Claude makes the ledger, the critic reads the intent with the chain around it, and the report returns with two new findings. Claude numbers them, files the report in `reviews/` and says: two new, none verified resolved, three still open, none newly obsolete, and the two new ones await your verdict. It then offers the walkthrough. You accept the first finding, and Claude iterates the intent through `/forge`.

## See also

- [Critic lenses](../reference/critic-lenses.md): the lenses of today.
- [Walk through a list](walk-through-a-list.md): settling the findings one by one.
- [The critic](../about/the-critic.md): what the critic judges and why it is blind.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
