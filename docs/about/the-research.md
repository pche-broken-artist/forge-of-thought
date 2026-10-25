---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: af15e5575379d7c9
inputs:
  - projects/forge/10-intent.md#POS.0050
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.1890
  - projects/forge/10-intent.md#POS.1370
  - projects/forge/10-intent.md#REJ.0450
  - projects/forge/10-intent.md#REJ.0460
  - projects/forge/10-intent.md#REJ.0470
  - projects/forge/40-solution-design.md#SOL.0860
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
---

# How a research is made

A research is Claude's search of what the world already knows about
one topic, filed in the project so that it lasts. This page explains
why a research is planned before anything is searched, how the
searching agents are kept apart and kept honest, and how their notes
become one answer. It is for anyone who uses the forge, extends it or
weighs whether to trust it.

## What it is

A research grounds the principal's artefacts in what the world has
already solved. The principal is the person whose thinking is being
forged, and the artefacts are the documents of his chain. He does not
want to reinvent what others have already worked out, and outside
inspiration is a legitimate input. What a research finds is stored in
the project's `research/` folder rather than left in the
conversation; what that folder holds is described in
[Sources and research](sources-and-research.md).

The quality of a research is made by its plan, not by the searching.
The plan splits the topic into questions small enough to answer, and
the principal sees and confirms those questions before any of them is
searched.

## How it works

### The plan comes first

Before drafting, Claude asks what the research serves and what the
principal already knows or wants left out. It also reads the
project's indexes of research and sources, and names the notes and
sources the plan will build on. Nothing is searched at this point.

The plan then has these parts, in the shape of
`templates/research-plan.md`:

- Purpose: the thread, position, decision or artefact the research
  feeds, and what is already known.
- Perspectives: the standpoints from which the topic is treated, one
  line each, with the cards that serve it or "no card" where a
  perspective is left empty on purpose.
- Assumptions: what the plan takes for granted about where the answer
  lives, and what would make it rethink.
- A premortem: the question "the research is done and missed the
  most interesting thing: what was it?", answered once by Claude and
  marked as its own.
- Left out: the fields and questions considered and deliberately not
  pursued, so that "did not look" is a statement and not a silence.
- Cards: the questions themselves.
- Agents: how many agents will search, and the rule that fixed the
  count (one per card per engine).

A card is one question answered by one kind of evidence from one kind
of source. Each card carries these fields:

- Question: what is asked, about what, in what context, against what
  alternative.
- Why it matters: the decision or artefact it serves, in one
  sentence.
- What would answer it: one kind of evidence, and the kind of source
  it lives in.
- Where to look: kinds of source, more than one route, and the known
  items that must turn up.
- Disconfirming query: one search written to find the opposite of
  what is expected.
- Stop rule: when the search ends, such as a differently-worded query
  bringing nothing new and every perspective of the card having a
  primary source, or the budget of opened pages spent.

A card that needs two kinds of evidence is two cards. A card with
nothing under "why it matters" is cut. The reason for these two rules
is not recorded. For a topic new to the project, the first card asks
whether a synthesis already exists and in what words the field
speaks, and its answer may rewrite the other cards. The number of
cards is bounded by the kind rule, not by a count. Past about seven
cards they are grouped, and a topic whose groups still exceed that is
several researches.

The principal confirms the plan in a walkthrough. A walkthrough is
the forge's way of putting a list to the principal one item per
message, each closed with a verdict. Perspectives come first, then
the cards, then the rest. The plan is written nowhere until he
confirms it.

### Two depths

A research has one of two depths, which the principal names when he
asks for it:

- Deep (`--deep`): a plan of several cards and a bundle, that is a
  folder `research/YYYY-MM-DD-<topic>/` with the plan and the
  synthesis at its head and one note per card per engine.
- Quick (`--quick`): one card, filed as a single note. The card is
  still shown to the principal before anything is searched, and there
  is no synthesis.

Without the word, Claude proposes the depth in the plan with its
reason. It proposes quick where one question is to be answered and
cited, and deep where a position, a layer of the chain or a design
will rest on the answer. The principal decides. The exact shape of a
note, a bundle and its plan is set out in
[Research note and bundle](../reference/research-bundle.md).

A deep research may also run on a model of a second family beside
Claude, as [Another model family](another-model-family.md) explains.

### The searching agents

Every card is searched by its own agent. The agent is a subagent,
that is a separate instance of the model started for one task, which
sees nothing of the conversation and does not speak to the other
agents. What it sees is a packet made from the forge's own
definition:

- the card, word for word;
- the agent's brief, the same in every packet;
- the shape the note must have;
- the earlier notes the card names, attached as copies;
- the sentence that the agent writes no file and returns the whole
  note as its answer.

The agent's brief has one owner, the research command's own
definition, and is copied word for word into every packet. In the
person's terms it asks the agent to:

- start wide with short broad queries, read the result list, and only
  then open pages;
- open a page or not cite it, so that no finding rests on a search
  snippet or a search engine's summary;
- go upstream and cite the first publisher, using a copy only when the
  original cannot be reached, and then as a copy;
- read about a publisher before reading the publisher;
- exclude sources by kind, such as affiliate pages, mass-produced
  pages without author or date, and a vendor's blog on its own
  market, while a vendor's own documentation of its own product
  counts as a primary source;
- name conflicts, citing both sides of a disagreement;
- say what was not found, because "no reliable source on X" is a
  finding;
- run the card's disconfirming query and report what it found,
  including nothing;
- spend its openings on primary sources, about ten to fifteen pages;
- never fabricate a source, a quote, a date or a figure.

The budget of openings has a reason in the brief itself. More calls
have been measured to lower the accuracy of citations, not raise it.

### The check before a note is filed

No note enters the project unchecked. Three checks run in order:

1. Claude reads the note against its shape. A note goes back to its
   agent as a failed run when a finding rests on a snippet without
   saying so, a source is cited for content but listed as not opened,
   a quote has no place, or the search record is empty.
2. A script scans the note for the facts of the instance (the names,
   hosts and accounts of one installation of the forge), as every
   file that may be quoted is scanned.
3. A script, `scripts/forge-cite.py`, opens every URL the note cites
   and reads an arXiv page for its title.

A dead page, or an identifier that names another paper, is the mark of
a fabricated citation. Such a note goes back to its agent once, with
the report. A note that comes back still failing is filed as it is,
and the synthesis names every finding resting on a failed citation as
without support. A page that refused or did not answer is
unverifiable. It is said so and never counted as a failure. The check
writes nothing into the note, because the note is the agent's record.

### The synthesis

When every note has returned, Claude writes the synthesis from the
notes alone, into the head of the bundle. It has these parts, in this
order:

- Completeness, card by card: answered or not found and where it was
  looked, the stop rule met or why the search ended, and what the
  disconfirming query found.
- The answers side by side, with agreement reported as consistency
  and never as validation, and the differences spelled out.
- The unexpected, gathered from every note before any judgement is
  made.
- What was not found, gathered.
- Claude's own view, last and apart, marked as its own and saying in
  plain words whether it is verified or a hypothesis.

A summary of the result stands at the top of the bundle, so that a
reader who stops there has the answer. A second round is allowed
only for gaps the notes name, and it runs on the principal's word.
There is never a third. A note, a bundle and its plan are immutable
from their filing.

```
 ask what it serves
        |
        v
 draft the plan --> walkthrough --> plan confirmed
                                         |
               +-------------------------+
               v            v            v
           card 1       card 2   ...  card n     one isolated agent each
               |            |            |
               v            v            v
        check: shape, instance facts, every URL opened
               |            |            |
               +------------+------------+
                            v
                synthesis from the notes alone
                            |
                            v
          second round for named gaps only, never a third
```

## Why

The plan is where the principal sees the questions before they cost
anything. The decomposition into cards is what makes a research good,
so it is the decomposition that he confirms. The plan, rather than the
finished note, is the unit of his consent, as the principal wished.

Each card has one kind of evidence and one stop rule, so that the
search of it can end on a rule and the note can say which rule ended
it.

The agents see nothing of the conversation, and their brief is
copied word for word from one owner. Why a packet carries nothing of
the conversation is not recorded beyond that.

Every citation is opened by a script because an agent can invent or
misnumber sources, and nobody checks that by hand across many cards.
Resolving the URL is the one mitigation of fabricated citations with
a measured effect.

Claude's own view stands last and apart because how sure a claim is
must be said in words. A claim never gains certainty by being written
into an artefact, and Claude's reading must not pass for what the
sources say. Gathering the unexpected before any judgement keeps it
visible; the reason for that order is not recorded beyond this.

Three ways of doing a research were considered and rejected:

- A recursive deep-dive to a fixed depth. Depth comes instead from the
  decomposition into cards, and from a second round only for gaps the
  notes name.
- A fact verified by a count of agreeing sources. Agreement of copies
  is not agreement. A source is opened, dated and placed by kind,
  conflicts are named, and a citation is verified by resolving it.
- Saturation measured as a percentage. The stop rule is a rule of
  kind: a differently-worded query bringing nothing new and every
  perspective with a primary source, or the openings spent, written
  into the search record.

Why an unanswered page counts as unverifiable rather than as a
failure is not recorded.

## A worked example

A generic card, as a plan might hold it:

```
#### Card 1: retention periods for meeting minutes
- **Question:** How long do public bodies keep meeting minutes, and
  is the period set by law or by internal policy?
- **Why it matters:** The intent's position on archiving rests on
  whether a legal minimum exists.
- **What would answer it:** Retention rules, from the legal texts
  or official guidance that set them.
- **Where to look:** National archive guidance; the statutes on
  public records; a records-management standard.
- **Disconfirming query:** "meeting minutes no retention
  requirement"; expected: rules exist in most jurisdictions.
- **Stop rule:** A differently-worded query brings nothing new and
  each jurisdiction named has a primary source; about fifteen pages
  opened at most.
```

The card asks one question and wants one kind of evidence (legal
texts or official guidance). If it had also asked how organisations
feel about the rule, that would need survey evidence, and it would be
a second card.

## See also

- [Research a topic](../use/research-a-topic.md): running `/research`.
- [Another model family](another-model-family.md): the second engine,
  how it is reached and how its independence is measured.
- [Sources and research](sources-and-research.md): research as a
  resource of the project.
- [Research note and bundle](../reference/research-bundle.md): the
  shape of a note, a bundle and its plan.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
