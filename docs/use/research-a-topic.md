---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: b77d60fd85932238
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

This page shows how you get a planned, checked and indexed research with `/research`, quick or deep, on one model family or two. It is for you, the person who runs the forge and wants grounding for a document without reinventing what the world has already solved. The principal is the person whose thinking is being forged, and on this page that is you. Claude is the assistant that runs the research with you.

## When to use it

Use it when a thought of yours needs outside evidence before you write it down: a position, a layer of the chain or a design that will rest on the answer.

Choose the depth by the question:

- `--quick` fits one question that is to be answered and cited.
- `--deep` fits a topic where a position, a layer of the chain or a design will rest on the answer.

If you give no depth, Claude proposes one with its reason, and you decide.

## The command

```
/research [--quick | --deep [--engine <name>]] <topic> [slug]
```

A line that can be typed as it stands:

```
/research --deep --engine antigravity how do teams keep a style guide current my-project
```

The depths differ in what they leave behind.

- `--deep` makes a plan of several cards and a bundle `research/YYYY-MM-DD-<topic>/`. The plan and the synthesis stand at its head, and the bundle holds one note per card per engine.
- `--deep --engine antigravity` adds a second engine of another model family. It reads the draft plan and answers every card from the same packet of context as the first.
- `--quick` is one card, answered on the session model alone and filed as one note. A session is one running conversation with Claude. The session model is the model that conversation runs on.

A card is one question, answered by one kind of evidence from one kind of source. The second engine is named by the forge's own word for it and is never chosen by model. What it is and how it is reached is on [Another model family](../about/another-model-family.md).

## What happens

1. Claude asks what the research serves and what you already know or want left out. It asks one question per message. It reads the existing indexes and names the notes and sources the plan will build on.

   You should now see the questions one at a time, and then a list of the notes and sources the plan will rest on.

2. Claude drafts the plan. The plan holds:
   - the purpose
   - the perspectives
   - the assumptions, with a premortem (an imagined failure: the research is done and missed the most interesting thing)
   - what is left out
   - the cards

   Each card carries its question, why it matters, what would answer it, where to look, a disconfirming query and a stop rule. The disconfirming query is a search written to find the opposite of what is expected. For a topic new to your project, the first card asks whether a synthesis already exists.

   You should now see the draft plan. With `--quick` you see one card instead, with the verdict line, before anything is searched.

3. With a second engine, it reads the draft plan. Claude says the model and the size before this run. The engine's additions are shown beside the draft and marked as the engine's. Nothing of them enters the plan by Claude's own judgement.

   You should now see the engine's additions marked as its own, beside the draft.

4. You work through the plan in a walkthrough, which is one item per message, each closed with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The perspectives come first, then the cards. `(m)odify` is the normal verdict on a card.

   Nothing is searched and nothing is written until you confirm the plan. On your word the bundle is born with its plan.

   You should now see a folder `research/YYYY-MM-DD-<topic>/` holding `00-plan.md`, the plan as you confirmed it.

5. Claude tells you which models run and how many runs there will be, before it dispatches. Each card is then searched apart from the conversation, so that no agent sees what you and Claude have said. The agents write no file and return the whole note. A second engine answers every card on the same packet, in parallel.

   You should now see the notes coming back, one per card per engine.

6. Every note is checked before it is filed:
   - against the shape of a note
   - for facts of your instance that must not appear
   - for every URL it cites, which a script opens: `python scripts/forge-cite.py <note>`

   A note with a dead or mismatched citation goes back to its agent once. If it comes back still failing, it is filed as it is, and the synthesis names every finding that rests on it as without support. A page that refused the script, by a 403 or a timeout, is called unverifiable and is not counted as a failure.

   You should now see each note checked, and the failed ones sent back.

7. With two engines, Claude measures how independent the two notes of each card are: `python scripts/forge-cite.py --independence <bundle>`. A note that shares most of its sources, or a third of its sentences, with the other engine's was written from it and not from the web. It goes back once, or the synthesis says it is no second voice.

   You should now see, per card, a verdict on whether the second note is a voice of its own.

8. Claude writes the synthesis from the notes alone. It states the independence per card. Where the engines differ, it lays their answers side by side. Its own view comes last and apart, marked as its own. A second round is allowed only for gaps the notes name, on your word. There is no third round.

   You should now see the synthesis under the plan in `00-plan.md`.

9. Claude files one index entry for the bundle in `research/00-INDEX.md`, with a question, an answer in short and when to consult it. It then remakes the ledger. The ledger is the single record of the project's state, made when it is read.

   You should now see the new entry in the research index.

A bundle is immutable from the filing of the synthesis. A research of one card on one engine stays a single note, `research/YYYY-MM-DD-<topic>.md`.

## What you have afterwards

- A bundle with the confirmed plan and the synthesis at its head, and one note per card per engine. For a quick research, one note.
- One entry for it in the research index, and a remade ledger.
- A report from Claude that leads with what the research says and where the engines differ.
- A proposal, where the research suggests one, to change an artefact through `/forge <state>`. Claude never makes such a change silently.
- The run folder `tmp/research/<run>/`, kept for inspection. It is no source of truth.

The shape of a note, a bundle and its plan is on [Research note and bundle](../reference/research-bundle.md). Why a research is planned before it is searched is on [How a research is made](../about/the-research.md). What research is for and why it is immutable is on [Sources and research](../about/sources-and-research.md).

## If something goes wrong

- **The engine you named cannot be used.** It may be missing from the machine, not signed in or out of quota. Claude says so in one sentence with the script's reason. The research goes on as if you had not named it, and the bundle records the deviation. It does not stop to ask you. What a second engine needs on the machine is on [Install what the forge needs](../start/install.md).
- **A second-engine run fails on one card.** Claude says why, and that card goes on with the session model's note alone. The bundle records it.
- **A run changed its own packet folder.** The script refuses it and files nothing.
- **A citation is dead or mismatched.** The note goes back to its agent once. After that it is filed as it is, and the synthesis marks its findings as without support.
- **The plan is not what you want.** Nothing has been searched, so say `(m)odify` or `(r)eject` on the item. The plan is written nowhere until you confirm it.
- **You wanted a note on an unsettled gap.** A second round is possible once, on your word. A third is not.

## A worked example

You want to know how teams keep a style guide current. Your project slug is `my-project`.

1. You type `/research --deep how do teams keep a style guide current my-project`.
2. Claude asks what the research serves. You answer that it feeds a rule you are drafting. Claude asks what you already know. You say you have read two articles, and Claude names them and a note from an earlier research.
3. Claude drafts a plan of four cards. The first asks whether a synthesis of the field exists. The plan names a perspective of the tool maker and one of the editor, and leaves out publishing tools on purpose.
4. You go through it item by item. On the third card you answer `(m)odify` and narrow its question. You confirm, and the bundle is born with its plan.
5. Claude says the models and that four runs will go out. The four notes return, and a script opens every URL. One note is sent back for a dead link and returns clean.
6. Claude writes the synthesis, files one index entry, remakes the ledger and reports what the research says. It proposes one change to the intent through `/forge`, and you decide on it.

## See also

- [How a research is made](../about/the-research.md): why a research is planned before it is searched and how what it found is kept honest.
- [Another model family](../about/another-model-family.md): what the second engine is, how it is reached and how its independence is measured.
- [Research note and bundle](../reference/research-bundle.md): the shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
