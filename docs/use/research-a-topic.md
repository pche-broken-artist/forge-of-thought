---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 740ea4ad096ee171
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

This page is for the principal (the person whose thinking is being
forged) who wants a topic researched with `/research`: planned first,
searched only on the principal's word, checked and indexed. It shows
the two depths, quick and deep, and how a second engine of another
model family can answer the same questions beside Claude.

## When to use it

Use it when you do not want to reinvent what the world has already
solved, and an answer must be found and cited before an artefact of
the chain rests on it.

- Choose `--quick` when one question is to be answered and cited.
- Choose `--deep` when a position, a layer of the chain or a design
  will rest on the answer.
- Add `--engine antigravity` to a deep research when you want a second
  voice from another model family.

If you give neither word, Claude proposes a depth with its reason, and
you decide. Your word overrides its proposal.

## The command

```
/research [--quick | --deep [--engine <name>]] <topic> [slug]
```

One line that can be typed as it stands:

```
/research --deep --engine antigravity <topic> my-project
```

The last word is the slug of the project, when it names a project.
`--quick` takes no `--engine`.

The three results differ in what they leave in `research/`:

- `--deep` leaves a bundle `research/YYYY-MM-DD-<topic>/`. Its head
  is the plan, with the synthesis below it. Beside it lies one note
  per card per engine.
- `--deep --engine antigravity` is the same bundle, with a second
  engine that reads the draft plan and answers every card on the same
  packet as Claude. Both notes of a card sit in the bundle.
- `--quick` is one card, answered by Claude alone and filed as one
  note `research/YYYY-MM-DD-<topic>.md`.

A card is one question with why it matters, what would answer it,
where to look, a disconfirming query and a stop rule. The shape of a
note, a bundle and its plan is on
[Research note and bundle](../reference/research-bundle.md).

## What happens

1. Claude asks what the research serves and what you already know or
   want left out. It asks one question per message, and nothing is
   searched. It reads the indexes of `research/` and `sources/` and
   names the notes and sources the plan will build on.

   You should now see the notes and sources Claude will build on,
   named one by one.

2. Claude drafts the plan. The plan holds:
   - the purpose
   - the perspectives
   - the assumptions, with a premortem
   - what is left out
   - the cards

   For a topic new to the project, the first card asks whether a
   synthesis already exists and in what words the field speaks. A
   topic that is one card is said to be so, and the plan is one card.

   You should now see a draft plan, or for `--quick` one card with the
   verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`
   before anything is searched.

3. With a second engine, the engine reads the draft plan. Claude tells
   you the models and the size of the run before it starts. Its
   additions are shown beside the draft and marked as the engine's.
   Claude takes none of them into the plan on its own judgement.
   A quick research skips this step.

   You should now see the engine's additions beside the draft, marked
   as the engine's.

4. A walkthrough of the plan follows: a walkthrough is a list worked
   one item per message, each closed with the verdict line. The
   perspectives come first, then the cards. `(m)odify` is the normal
   verdict on a card. Nothing is written until you confirm. On your
   word the bundle is born with its plan as confirmed.

   You should now see the bundle folder, with `00-plan.md` in it.

5. Claude tells you the models and the number of runs before it
   dispatches. Each card is then searched apart from the conversation:
   the agent sees only a packet that holds the card, the rules of the
   search, the shape of the note and the known notes the card names.
   With two engines both answer the same packet, in parallel, and
   neither sees the other's note.

   You should now see the notes returning, one per card per engine.

6. Every note is checked before it is filed:
   - It is checked against its shape. For example, a finding that rests
     on a search snippet alone without saying so sends the note back.
   - It is scanned for facts of your own installation, so that none can
     be quoted into a public file.
   - Every URL it cites is opened by
     `python scripts/forge-cite.py <note>`.

   A note with a dead or mismatched citation goes back once to its
   agent. A page that refuses the check (a blocked or timed-out one) is
   said to be unverifiable and is not counted as a failure.

   With two engines, the independence of the two notes of each card is
   measured by `python scripts/forge-cite.py --independence <bundle>`.
   A note that shares most of its sources or a third of its longer
   sentences with the other was written from it, not from the web. It
   goes back once, or the synthesis says it is no second voice.

   You should now see every note filed, or a plain sentence saying what
   failed the check.

7. Claude writes the synthesis from the notes alone. It states the
   independence per card, and puts its own view last and apart, marked
   as its own. A second round is possible only for gaps the notes
   name, on your word; there is no third. A quick research has no
   synthesis.

   You should now see the synthesis under the plan in `00-plan.md`,
   and the bundle closed to change.

8. Claude writes one entry for the bundle in `research/00-INDEX.md`
   (question, answer in short, consult when) and remakes the
   ledger, the single source of truth for state.

   You should now see the new entry in the index of `research/`.

## What you have afterwards

- The bundle, or the single note, in `research/`. It is immutable
  once filed. Why research is kept that way is on
  [Sources and research](../about/sources-and-research.md).
- One entry for it in `research/00-INDEX.md`.
- A report from Claude that leads with what the research says and
  where the engines differ, not with a literature review.
- A change to an artefact, if the research suggests one, proposed
  through `/forge <state>`. Claude never makes it silently.
- The run folder `tmp/research/<run>/`, kept for inspection. It is no
  source of truth.

## If something goes wrong

- **A second engine is named but cannot be used** (not on PATH, not
  signed in, quota spent, or the answer cannot be read). Claude says
  so in one sentence with the reason the script prints, and the
  research goes on as without `--engine`. The plan records the
  deviation. It asks no question in the middle of the run. What a
  second engine needs on the machine is on
  [Install what the forge needs](../start/install.md).
- **The engine script refuses** with a reason on its error output:
  the tool is missing, its version is too old, the packet has no
  `packet.md`, the run changed the packet folder, or the answer is
  empty. The card then goes on with Claude's note alone, and the
  deviation is recorded.
- **A note has a dead or mismatched citation** after its second try.
  It is filed as it is, and the synthesis names every finding that
  rests on it as without support.
- **The independence check marks a note** as written from the other
  engine's. It goes back once, or the synthesis says it is no second
  voice.

## A worked example

You want a design question answered before a layer of the chain rests
on it. You type:

```
/research --deep --engine antigravity how teams handle retries in message queues my-project
```

1. Claude asks what the research serves. You answer that a design
   section depends on it and that you already know the basic
   back-off pattern. Claude names two earlier notes it will build on.
2. It shows a plan of four cards. Card 1 asks whether a synthesis of
   the field exists. The other three each have one question and one
   disconfirming query. The second engine's additions are shown beside
   the draft and marked as the engine's.
3. In the walkthrough you accept the perspectives, modify the wording
   of card 3 and accept the rest. You say yes, and the bundle
   `research/YYYY-MM-DD-<topic>/` is born with `00-plan.md`.
4. Claude says how many runs it will make and on which models. The
   notes return: `card-1.claude.md` and `card-1.antigravity.md`, and so
   on for each card.
5. The citation check sends one note back once. The independence
   check finds that card 3's two notes cite different sources.
6. Claude writes the synthesis, adds one index entry and reports first
   what the research says and where the two engines differ. It proposes
   a change to the design section through `/forge <state>`, and you
   decide.

## See also

- [How a research is made](../about/the-research.md): why a research is planned before it is searched and how what it found is kept honest.
- [Another model family](../about/another-model-family.md): what the second engine is, how it is reached and how its independence is measured.
- [Research note and bundle](../reference/research-bundle.md): the shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
