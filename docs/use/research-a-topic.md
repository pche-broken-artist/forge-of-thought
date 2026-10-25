---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 5166bc9b6e96bbd8
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

This page shows how you get a planned, checked and indexed research
with `/research`, quick or deep, on one model family or two. It is for
the principal (the person whose thinking is being forged, that is you)
who wants grounding for an artefact without reinventing what the world
has already solved. Why a research is planned before it is searched
is explained in [How a research is made](../about/the-research.md).

## When to use it

Use it when a position, a layer of the chain or a design is about to
rest on an answer you do not yet have, or when one question must be
answered and cited. A research is stored in the project's `research/`
directory and is never edited once filed. What research is for is told
in [Sources and research](../about/sources-and-research.md).

There are two depths:

- `--deep`: a plan of several cards (a card is one question with its
  way of being answered), a bundle `research/YYYY-MM-DD-<topic>/`
  with the plan and the synthesis at its head, and one note per card
  per engine.
- `--quick`: one card, answered on the session model alone (the model
  Claude itself runs on in the conversation) and filed as one note.

`--deep` can take a second engine of another model family. It reads
the draft plan and answers every card on the same packet as the first.
What that engine is and how its independence is measured is told in
[Another model family](../about/another-model-family.md). What it
needs on the machine is in
[Install what the forge needs](../start/install.md).

If you give no depth word, Claude proposes the depth with its reason,
and you decide. It proposes quick where one question is to be answered
and cited, and deep where something will rest on the answer.

## The command

```
/research [--quick | --deep [--engine <name>]] <topic> [slug]
```

The only engine name today is `antigravity`. The slug is the project;
leave it out when the project is clear.

```
/research --deep --engine antigravity <topic> <slug>
```

## What happens

1. Claude asks what the research serves and what you already know or
   want left out. It asks one question per message. It reads the
   project's indexes of research and sources, and names the notes and
   sources it will build on. Nothing is searched.

   You should now see a short list of what the plan will build on,
   and your answers reflected back.

2. Claude drafts the plan. It holds:
   - the purpose
   - the perspectives
   - the assumptions, with a premortem (Claude's own answer to "the
     research is done and missed the most interesting thing: what was
     it?")
   - what is left out
   - the cards: each one question, with why it matters, what would
     answer it, where to look, a disconfirming query (a search
     written to find the opposite of what is expected) and a stop
     rule

   For a topic new to the project, the first card asks whether a
   synthesis already exists and in what words the field speaks. A
   card that needs two kinds of evidence is split into two cards.

   You should now see the draft plan. In a quick research you see the
   one card with the verdict line before anything is searched, and
   steps 3 and 7 are skipped.

3. With a second engine, it reads the draft plan and says what the
   plan misses or assumes. Claude says the model and the size of the
   run before it starts. The engine's additions are shown beside the
   draft and marked as the engine's. Claude takes nothing into the
   plan on its own judgement.

   You should now see the draft with the engine's additions marked.

4. A walkthrough of the plan follows. A walkthrough works a list one
   item per message, each closed with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. Perspectives
   come first, then the cards, then the rest. `(m)odify` is the normal
   verdict on a card. Nothing is searched and nothing is written until
   you confirm the plan. On your word the bundle is born with its plan
   as `00-plan.md`.

   You should now see the bundle directory with the plan in it.

5. Claude tells you the models and the number of runs before it
   dispatches. Each card is then searched apart from the
   conversation, and the agents never speak to each other. With a
   second engine, each card goes to both engines on the same packet.
   An engine you named but that cannot be used (not on the path, not
   signed in, quota spent) is said in one sentence with the script's
   reason, and the research goes on without it.

   You should now see the notes returning, one per card per engine.

6. Every note is checked before it is filed. Claude checks its shape,
   scans it for facts of your instance that must not be public, and
   has every URL it cites opened by
   `python scripts/forge-cite.py <note>`. A note with a dead or
   mismatched citation goes back once to its agent. A page that
   refuses or times out is said to be unverifiable and is not counted
   as a failure. With two engines, how independent the two notes of
   each card are is measured by
   `python scripts/forge-cite.py --independence <bundle>`. A note
   marked as written from the other engine's is sent back once, or is
   said in the synthesis to be no second voice.

   You should now see each note filed, or sent back with the reason.

7. Claude writes the synthesis from the notes alone, at the head of
   `00-plan.md`: completeness card by card, the answers side by side,
   what was unexpected, what was not found, and the measure of
   independence per card. Claude's own view comes last and apart,
   marked as its own. A second round is possible only for gaps the
   notes name, on your word, and there is no third.

   You should now see the synthesis in the plan file, with the bundle
   closed.

8. Claude adds one entry for the bundle to `research/00-INDEX.md`
   (question, answer in short, consult when) and remakes the ledger,
   the project's state report made from its documents at read time.

   You should now see the entry in the research index.

## What you have afterwards

- A bundle `research/YYYY-MM-DD-<topic>/` with the plan and the
  synthesis at its head and one note per card per engine. A quick
  research leaves one note `research/YYYY-MM-DD-<topic>.md`.
- One entry in `research/00-INDEX.md`.
- A report in the conversation. It leads with what the research says
  and where the engines differ. A change to an artefact is proposed
  through `/forge <state>`, never made silently.
- The run folder `tmp/research/<run>/`, kept for inspection. It is
  no source of truth.

The shape of a note, a bundle and its plan is in
[Research note and bundle](../reference/research-bundle.md).

## If something goes wrong

- An engine you named is unusable: Claude says so in one sentence
  with the script's reason, goes on as without it, and records the
  deviation in the bundle. It does not stop to ask.
- A run of the second engine fails on one card: that card goes on
  with the session model's note alone, and the deviation is recorded.
- A note fails the shape check: it goes back to its agent as a failed
  run and is not filed.
- A citation is dead or mismatched: the note goes back once with the
  report. If it comes back still failing, it is filed as it is, and
  the synthesis names every finding resting on it as without support.
- Two engines' notes share most of their sources or a third of their
  longer sentences: the check marks the second as written from the
  first. See step 6.
- The topic is too wide: past about seven cards, the cards are
  grouped, and if the groups still exceed that, the topic is several
  researches.

## A worked example

You type:

```
/research --deep --engine antigravity retry-strategies <slug>
```

1. Claude asks what the research serves. You answer that a design
   section on failure handling needs grounding. It asks what you
   already know, and you name one note you want it to start from.
2. It drafts a plan of four cards. The first asks whether a synthesis
   of retry strategies already exists. The engine's review suggests a
   perspective with no card; Claude shows it marked as the engine's.
3. In the walkthrough you accept two cards, modify one (`m`) to narrow
   its question, and accept the engine's perspective with a new card.
   You confirm, and the bundle is born with its plan.
4. Claude says how many runs follow and on which models. Eight notes
   come back, one per card per engine. One citation is dead, and that
   note is sent back and returns clean.
5. The independence check passes on all cards. The synthesis is filed,
   the index entry is written, and the ledger is remade.
6. The report opens with what the research says, names the one card
   where the engines differ, and proposes a change to the design
   through `/forge`. You decide whether to make it.

## See also

- [How a research is made](../about/the-research.md): why a research is planned before it is searched and how what it found is kept honest.
- [Another model family](../about/another-model-family.md): what the second engine is, how it is reached and how its independence is measured.
- [Research note and bundle](../reference/research-bundle.md): the shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
