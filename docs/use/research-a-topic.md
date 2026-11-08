---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: be36cbd5b71b88cf
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

This page shows how to get a planned, checked and indexed research with `/research`, quick or deep, on one model family or two. It is for you, the principal: the person whose thinking is being forged and who decides what the research serves and what is kept.

## When to use it

Use it when you want grounding or inspiration for an artefact and do not want to reinvent what the world has already solved. Use `--quick` when one question is to be answered and cited. Use `--deep` when a position, a layer of the chain or a design will rest on the answer. Add a second engine when you want a voice from another model family beside Claude's.

## The command

```
/research [--quick | --deep [--engine <name>]] <topic> [slug]
```

A line that can be typed as it stands:

```
/research --deep --engine antigravity onboarding-checklists my-project
```

- `--deep` makes a plan of several cards and a bundle `research/YYYY-MM-DD-<topic>/`. The plan and the synthesis lie at its head, and there is one note per card per engine.
- `--deep --engine antigravity` adds a second engine of another model family. It reads the draft plan and answers every card on the same packet as Claude's own notes.
- `--quick` is one card, answered by Claude alone and filed as one note. It takes no `--engine`.
- Without the depth word, Claude proposes the depth with its reason, and you decide.
- The slug is the project's; the last word is taken as the slug when it names a project.

## What happens

1. Claude asks what the research serves and what you already know or want left out, one question per message. It names the notes and sources it will build on. You should now see the questions, one at a time, and nothing searched.
2. Claude drafts the plan. It holds the purpose, the perspectives, the assumptions with a premortem, what is left out and the cards. Each card is one question with why it matters, what would answer it, where to look, a disconfirming query and a stop rule. You should now see the draft plan.
3. With a second engine, its additions to the plan are shown beside the draft and marked as the engine's. Claude says the models and the size of the run before it starts. You should now see the engine's additions apart from Claude's draft.
4. You go through the plan in a walkthrough (a list worked one item per message, each closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`). The perspectives come first, then the cards. `(m)odify` is the normal verdict on a card. You should now see each item, one per message, waiting for your letter.
5. Nothing is searched and nothing is written until you confirm. On your word the bundle is born with its plan. You should now see the bundle's folder with `00-plan.md` in it.
6. Claude tells you the models and the number of runs before it dispatches. Each card is then searched apart from the conversation, so the searcher knows only the card. You should now see the notes come back, one per card per engine.
7. Every note is checked before it is filed. It is checked against its shape and scanned for facts of your own instance. Every URL it cites is opened by `python scripts/forge-cite.py <note>`. A note with a dead or mismatched citation is sent back once. You should now see the notes filed in the bundle.
8. With two engines, the independence of the two notes of each card is measured by `python scripts/forge-cite.py --independence <bundle>`. You should now see, per card, whether the second note stands as a second voice.
9. The synthesis follows. Claude writes it from the notes alone, with its own view last and apart. A second round is run only for gaps the notes name, and only on your word. There is no third round. You should now see the synthesis under the plan in `00-plan.md`.
10. One index entry is written for the bundle, and the ledger (the file that holds the state of the project, made when it is read) is remade. You should now see the entry in `research/00-INDEX.md`.

A quick research runs differently. It shows its one card with the verdict line before anything is searched. It has no plan review, no second engine and no synthesis.

## What you have afterwards

- A deep research leaves a bundle `research/YYYY-MM-DD-<topic>/`. Its head is `00-plan.md` with the confirmed plan and the synthesis. Beside it lies one note per card per engine.
- A quick research leaves one note `research/YYYY-MM-DD-<topic>.md`.
- One entry in `research/00-INDEX.md`, with the question, the answer in short and when to consult it.
- A report from Claude. It leads with what the research says and where the engines differ. A change to an artefact of the chain is proposed through `/forge <state>` and never made silently.
- The run folder `tmp/research/<run>/`, kept for inspection. It is no source of truth.

The bundle is immutable from the filing of the synthesis. The notes and the plan are English, always.

## If something goes wrong

- **A second engine is unusable.** It may not be on the path, not signed in or out of quota. Claude says so in one sentence with the script's reason. The research goes on without it, and the bundle records the deviation. Claude does not stop to ask. What a second engine needs on the machine is on [Install what the forge needs](../start/install.md).
- **A card's run by the second engine fails.** The card goes on with Claude's note alone, and the deviation is recorded.
- **A note has a dead or mismatched citation.** It goes back to its searcher once. A note that comes back still failing is filed as it is, and the synthesis names each finding resting on it as without support.
- **A URL is unverifiable** (a refusal or a timeout). It is said so and is not counted as a failure.
- **The independence check marks a second note as written from the first.** That note goes back once, or the synthesis says it is no second voice. What the measure is: [Another model family](../about/another-model-family.md).

## A worked example

You want to know how teams keep onboarding checklists alive. You type:

```
/research onboarding-checklists my-project
```

Claude proposes a depth with its reason: the answer will feed an assignment, so it recommends deep. You say deep, and add the engine.

1. Claude asks what the research serves. You answer that it feeds a new section of the intent, and that you already know the notes on handovers and want vendor marketing left out.
2. Claude drafts a plan of four cards. The first asks whether a synthesis already exists and in what words the field speaks.
3. The second engine's review shows one perspective with no card. You take it in with `(m)odify` on the third card.
4. You confirm. The bundle `research/YYYY-MM-DD-onboarding-checklists/` is born with its plan.
5. Claude says the models and the eight runs it will make. Eight notes return, and one is sent back for a dead link.
6. The independence measure passes on three cards and marks the fourth. That note is sent back once.
7. The synthesis is filed, the index entry is written, and the report says where the engines differ. It proposes a change to the intent through `/forge intent`.

## See also

- [How a research is made](../about/the-research.md): why a research is planned before it is searched and how what it found is kept honest.
- [Another model family](../about/another-model-family.md): what the second engine is, how it is reached and how its independence is measured.
- [Research note and bundle](../reference/research-bundle.md): the shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
