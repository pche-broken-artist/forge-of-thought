---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 7b35a56bbb0eec06
inputs:
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
  - templates/research.md
  - templates/index.md
  - scripts/forge-engine.py
  - scripts/forge-cite.py
---

# Research a topic

`/research` gets you a planned, checked and indexed research on a
topic, quick or deep, on one model family or two. This page is for
you as the principal (the person whose thinking is being forged) when
you want what the world already knows about a question, grounded in
cited sources, before you write or change an artefact. Terms of the
forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you do not want to reinvent what others have solved. The
quality of a research comes from its plan, not from the searching, so
the plan is shown to you and confirmed by you before anything is
searched.

Choose the depth by what will rest on the answer.

- `--quick`: one question is to be answered and cited.
- `--deep`: a position, a layer of the chain or a design will rest on
  the answer.
- `--deep --engine antigravity`: as deep, with a second engine of
  another model family beside Claude.

Without a depth word Claude proposes one with its reason, and you
decide.

## The command

```
/research [--quick | --deep [--engine <name>]] <topic> [slug]
```

For example:

```
/research --deep --engine antigravity how teams keep decision logs my-project
```

The last word is the project slug when it names a project; the rest is
the topic. A quick research takes no `--engine`. The only engine
today is `antigravity`; what it needs on the machine is on
[Install what the forge needs](../start/install.md).

## What happens

1. **Claude asks what the plan needs.** It asks what the research
   serves and what you already know or want left out, one question per
   message. It reads the indexes of the project's earlier research and
   sources and names the notes and sources it will build on. You
   should now see the notes and sources named, and nothing searched.
2. **Claude drafts the plan.** The plan holds the purpose, the
   perspectives, the assumptions with a premortem, what is left out
   and the cards. Each card is one question with why it matters, what
   would answer it, where to look, a disconfirming query (a search
   written to find the opposite of what is expected) and a stop rule.
   You should now see the draft plan, with the proposed depth where
   you gave none. A quick research shows its one card with the verdict
   line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark` at
   this point, before anything is searched.
3. **The second engine reads the draft** (only with `--engine`). Its
   additions to the plan are shown beside the draft and marked as the
   engine's. Claude takes nothing into the plan on its own judgement.
   You should now see the engine's additions apart from the draft.
4. **You walk the plan.** The walkthrough takes one item per message,
   perspectives first, then the cards. `(m)odify` is the normal
   verdict on a card. Nothing is searched and nothing written until
   you confirm. On your word the bundle is born with its plan. You
   should now see the folder `research/YYYY-MM-DD-<topic>/` with
   `00-plan.md` in it.
5. **Claude dispatches the cards.** It tells you the models and the
   number of runs before it starts. Each card is searched apart from
   the conversation, so a searcher sees the card and its attached
   notes and nothing else. With a second engine, it answers every
   card on the same packet. You should now see one note per card per
   engine arrive.
6. **Every note is checked before it is filed.** Claude checks the
   note against its shape and scans it for facts of the instance.
   Then it opens every URL the note cites:

   ```
   python scripts/forge-cite.py <note>
   ```

   A note with a dead or mismatched citation goes back once. A note
   that comes back still failing is filed as it is, and the synthesis
   names every finding resting on it as without support. With two
   engines, Claude then measures how independent the two notes of each
   card are:

   ```
   python scripts/forge-cite.py --independence <bundle>
   ```

   A note written from the other engine's note goes back once, or the
   synthesis says it is no second voice. You should now see each note
   filed with its citations checked.
7. **Claude writes the synthesis.** It is made from the notes alone,
   with the independence stated per card and Claude's own view last
   and apart. You should now see the synthesis in `00-plan.md`, which
   is immutable from then on. A second round is possible only for gaps
   the notes name, on your word; there is no third.
8. **Claude indexes the bundle.** One entry is written in
   `research/00-INDEX.md`, with the question, the answer in short and
   when to consult it. The ledger (the state of the project, made
   from its documents at read time) is remade. You should now see the
   new entry in the index.

A quick research is one card answered on the session model alone (the
model Claude runs on in your conversation). It has no plan review, no
second engine and no synthesis. It is filed as one note
`research/YYYY-MM-DD-<topic>.md`. The card before the search, the
note's shape and the citation check of step 6 hold for it as for a
deep one.

## What you have afterwards

- A deep research is a bundle `research/YYYY-MM-DD-<topic>/` with the
  plan and the synthesis at its head and one note per card per engine.
  The shape of a note, a bundle and its plan is on
  [Research note and bundle](../reference/research-bundle.md).
- A quick research is one note.
- One index entry and a remade ledger.
- A report from Claude that leads with what the research says and
  where the engines differ. A change it suggests to an artefact is
  proposed through `/forge <state>` and never made silently.
- A run folder `tmp/research/<run>/`, kept for inspection. It is no
  source of truth.

Research is immutable once filed. Why it is kept so is on
[Sources and research](../about/sources-and-research.md), and why it is
planned before it is searched is on
[How a research is made](../about/the-research.md).

## If something goes wrong

- **A named engine cannot be used** (not on PATH, not signed in, quota
  spent): Claude says it in one sentence with the script's reason, and
  the research goes on without it. The bundle records the deviation.
  Claude does not ask you in the middle of the run.
- **A second engine's run fails for one card:** the card goes on with
  Claude's note alone, and the bundle records it.
- **A citation is dead or mismatched:** the note goes back to be made
  again once. If it still fails, it is filed as it is and the synthesis
  says what rests on it without support.
- **The two notes of a card are not independent:** the note marked as
  written from the other goes back once, or the synthesis says it is no
  second voice. What a second engine is and how independence is
  measured is on [Another model family](../about/another-model-family.md).

## A worked example

You want to know how teams keep decision logs, for a project with the
slug `my-project`.

```
/research --deep my-topic my-project
```

Claude asks what the research serves; you answer that a decision log
is being designed. It asks what you already know; you say the one
format you have used and name the formats to leave out. It names two
earlier notes it will build on. You should now see the draft plan:
a first card asking whether a synthesis of the field already exists,
and further cards for the other questions.

You walk the plan. You modify one card to narrow its question and
reject another. You confirm, and the bundle is born with its plan.
Claude says how many runs it will make and on which models, and
dispatches. Each note is checked and its citations opened. One note
comes back with a dead link, is sent back once and returns clean.
The synthesis follows, with Claude's view last. The index gains one
entry. Claude reports what the research says and proposes one change
to the intent, to be made through `/forge intent` if you want it.

## See also

- [How a research is made](../about/the-research.md): why a research
  is planned before it is searched and how what it found is kept
  honest.
- [Another model family](../about/another-model-family.md): what the
  second engine is, how it is reached and how its independence is
  measured.
- [Research note and bundle](../reference/research-bundle.md): the
  shape of a note, a bundle and its plan.
- [Sources and research](../about/sources-and-research.md): what
  research is for and why it is immutable.
- [Install what the forge needs](../start/install.md): what a second
  engine needs on the machine.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
