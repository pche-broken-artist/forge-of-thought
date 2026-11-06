---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 13cd296dbc3a23e4
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

This page shows how to get a planned, checked and indexed research
with `/research`, in a quick or a deep form, on one model family or
on two. It is for the principal, the person whose thinking is being
forged, who wants grounding for an artefact without reinventing what
the world has already solved.

## When to use it

Use it when a question needs an answer that is cited, or when a
position, a layer of the chain or a design will rest on what the
world already knows. The quality of a research is made by its plan.
For that reason nothing is searched until you have confirmed the
plan.

There are two depths:

- `--quick`: one card, one question, answered on Claude's own model
  and filed as a single note.
- `--deep`: a plan of several cards and a bundle
  `research/YYYY-MM-DD-<topic>/`. The plan and the synthesis are at
  its head, with one note per card per engine.
- `--deep --engine antigravity`: the deep form with a second engine
  of another model family. It reads the draft plan and answers every
  card on the same packet.

If you give no depth, Claude proposes one with its reason. Quick
fits one question to be answered and cited. Deep fits a topic where
a position, a layer or a design will rest on the answer. You decide.

## The command

```
/research --deep --engine antigravity <topic> [slug]
```

The general form is `/research [--quick | --deep [--engine <name>]]
<topic> [slug]`. The slug names the project and is left out when
the work is in the project you are already in. `--quick` takes no
`--engine`.

A second engine needs a tool installed and signed in on your
machine: [Install what the forge needs](../start/install.md) says
what.

## What happens

1. **Claude asks what the plan needs.** It asks what the research
   serves and what you already know or want left out, one question
   per message. It reads the indexes of the project's research and
   sources and names the notes and sources it will build on.
   You should now see the questions, and then the list of what the
   plan builds on. Nothing has been searched.

2. **Claude drafts the plan.** The plan holds the purpose, the
   perspectives, the assumptions with a premortem, what is left out
   and the cards. Each card is one question. It carries why it
   matters, what would answer it, where to look, a disconfirming
   query and a stop rule. You should now see the draft plan, with
   the depth proposed if you gave none.

3. **With a second engine, it reads the draft.** Claude tells you
   the models and the size of the run before it starts. The engine's
   additions are shown beside the draft and marked as the engine's.
   Claude takes none of them into the plan by its own judgement.
   You should now see the engine's additions marked apart.

4. **You walk through the plan.** A walkthrough is a list worked one
   item per message, each closed with the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The
   perspectives come first, then the cards. `(m)odify` is the normal
   verdict on a card. Nothing is searched and nothing written until
   you confirm. On your word the bundle is born with its plan.
   You should now see the bundle's `00-plan.md` filed with the plan
   as you confirmed it.

5. **Each card is searched.** Claude tells you the models and the
   number of runs before it dispatches. Each card is searched apart
   from the conversation, so no card sees what you said. With two
   engines, each card goes to both on the same packet, and the
   notes of the two engines are kept apart until both have
   returned. You should now see one note per card per engine in
   the bundle.

6. **Every note is checked before it is filed.** Claude checks the
   note against its shape and scans it for facts of the instance.
   Then it opens every URL the note cites with:

   ```
   python scripts/forge-cite.py <note>
   ```

   A note with a dead or mismatched citation goes back once. A
   page that refused or timed out is said to be unverifiable and is
   not counted as a failure. You should now see a count of the URLs
   per note: ok, dead, unverifiable, mismatch.

7. **With two engines, the independence is measured.** For each card
   Claude runs:

   ```
   python scripts/forge-cite.py --independence <bundle>
   ```

   It prints the sources and sentences the two notes share, and a
   verdict. A note written from the other engine's note goes back
   once. Otherwise the synthesis says it is no second voice. You
   should now see a verdict per card.

8. **Claude writes the synthesis.** It makes it from the notes alone,
   with the independence of each card stated and Claude's own view
   last and apart. You should now see the synthesis in `00-plan.md`
   and the bundle closed.

9. **A second round, if the notes name gaps.** Claude proposes it
   with the gaps listed, and it runs only on your word. There is no
   third round.

10. **Index and ledger.** One entry for the bundle is written to
    `research/00-INDEX.md`. The ledger, the forge's state report
    made at read time from the documents, is remade. You should now
    see the bundle in the research index.

A quick research is shorter. Claude shows you its one card with the
verdict line before anything is searched. There is no plan review,
no second engine and no synthesis. The card is searched, the note
is checked as above, and it is filed as one note,
`research/YYYY-MM-DD-<topic>.md`.

## What you have afterwards

- A bundle `research/YYYY-MM-DD-<topic>/` with the plan and the
  synthesis in `00-plan.md` and one note per card per engine. A
  quick research leaves one note. The shape of a note and of a
  bundle is in [Research note and bundle](../reference/research-bundle.md).
- One entry in the research index.
- A report from Claude. It leads with what the research says and
  where the engines differ, not with a literature review. A change
  to an artefact is proposed through `/forge <state>`, never made
  silently.
- The run folder `tmp/research/<run>/`, kept for inspection. It is
  no source of truth.

Once filed, the bundle does not change. Why that is so is in
[Sources and research](../about/sources-and-research.md).

## If something goes wrong

- **A named engine cannot be used.** It may not be on the path, not
  signed in, or out of quota. Claude says so in one sentence with
  the script's reason. The research goes on without it, as if you
  had not named it, and the plan's deviations record it. You are
  not asked a question in the middle of the run.
- **A card's run with the second engine fails.** Claude says it with
  the script's reason. The card goes on with the first engine's note
  alone, and the deviations record it.
- **A note has a dead or mismatched citation.** The note goes back to
  its agent once with the report. If it comes back still failing, it
  is filed as it is, and the synthesis names every finding that rests
  on it as without support.
- **The second engine's note was written from the first's.** The
  independence measure marks it. The note goes back once, or the
  synthesis says it is no second voice.

## A worked example

You type:

```
/research --deep --engine antigravity how teams keep a decision log current my-project
```

1. Claude asks what the research serves. You answer that a section
   on decision records is being written, and you name one approach
   to leave out.
2. It names two earlier notes it will build on and shows a draft
   plan of four cards.
3. It tells you the models and the size, runs the second engine on
   the draft, and shows the engine's two additions marked as the
   engine's.
4. You walk through the perspectives, then the cards. You answer
   `(m)odify` on card two to narrow its question, `(r)eject` on one
   of the engine's additions, and `(a)ccept` on the rest. You say
   to write, and the bundle is born with its plan.
5. Claude tells you the models and eight runs, four cards on two
   engines, and dispatches them.
6. Every note is checked and every URL opened. One note comes back
   once for a dead link and then passes.
7. The independence verdict shows the two notes of card three share
   most of their sources. Claude sends the second note back, and
   the rerun is clear.
8. The synthesis is written, the index entry made, the ledger
   remade. Claude reports what the research says, where the two
   engines differ, and proposes one change to the intent through
   `/forge intent`.

## See also

- [How a research is made](../about/the-research.md): why a research is planned before it is searched and how what it found is kept honest.
- [Another model family](../about/another-model-family.md): what the second engine is, how it is reached and how its independence is measured.
- [Research note and bundle](../reference/research-bundle.md): the shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
