---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 4ed5657b63a55677
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

A research is how Claude looks up what the world has already solved
before the principal builds on it. The principal is the person whose
thinking is being forged. This page explains why a research is
planned before anything is searched, and how what it finds is kept
honest. It is written for anyone who uses the forge, extends it or
weighs it. How to run one is a separate page,
[Research a topic](../use/research-a-topic.md).

## What it is

A research grounds the principal's artefacts in what others have
already worked out. Its purpose is that he does not reinvent what the
world has already solved. Outside inspiration is a legitimate input.
What a research finds is stored in the project's `research/` folder
and not left in the conversation. What a research is as a resource of
the project is explained in
[Sources and research](sources-and-research.md).

The quality of a research is made by its plan, not by the searching.
The plan splits the topic into cards. A card is one question, answered
by one kind of evidence from one kind of source (the
[Glossary](../reference/glossary.md) gives every term of the forge in
one line).

## How it works

### The plan comes first

Before anything is searched, Claude asks the principal what the
research serves and what he already knows or wants left out. It asks
one question per message. It also reads the project's indexes of
research and sources, and names the notes and sources the plan will
build on.

Claude then drafts the plan. The plan holds these parts:

- Purpose: what the research serves in the project, and what is
  already known.
- Perspectives: the standpoints from which the topic is looked at,
  each with the cards that serve it, or "no card" where a perspective
  is left empty on purpose.
- Assumptions: what the plan takes for granted about where the answer
  lives, and what would make it rethink. Under them stands a
  premortem, answered once by Claude and marked as its own: "the
  research is done and missed the most interesting thing: what was
  it?"
- Left out: the fields and questions considered and deliberately not
  pursued, so that "did not look" is a statement and not a silence.
- Cards: the questions themselves.
- Agents: how many agents will search, and the rule that fixed the
  count.

Each card carries these fields:

- Question: what is asked, about what, in what context, against what
  alternative.
- Why it matters: the decision or artefact the card serves, in one
  sentence.
- What would answer it: one kind of evidence, and the kind of source
  it lives in.
- Where to look: kinds of source, by more than one route, and the
  known items that must turn up.
- Disconfirming query: one search written to find the opposite of
  what is expected, and what is expected.
- Stop rule: when the search ends.

A card that needs two kinds of evidence becomes two cards. A card with
no sentence under "why it matters" is cut. For a topic new to the
project, the first card asks whether a synthesis already exists and in
what words the field speaks. Its answer may rewrite the other cards,
and the plan says so. The number of cards is bounded by this rule of
kind, not by a count. Past about seven cards, the cards are grouped.
If the groups are still too many, the topic is several researches.

The principal confirms the plan in a walkthrough. A walkthrough works
a list of items one per message, each closed with a verdict, and here
it runs perspectives first, then the cards, then the rest. Modifying a
card is the normal verdict. The plan is written nowhere until the
principal confirms it.

### Two depths

A research has two depths:

- Deep: a plan of several cards, filed as a bundle. The bundle is one
  folder with the plan and the synthesis at its head and one note per
  card per engine.
- Quick: one card, filed as a single note. The card is still shown to
  the principal before anything is searched. A quick research has no
  synthesis.

The principal may name the depth when he calls the research. Where he
does not, Claude proposes it in the plan with its reason. It proposes
quick where one question is to be answered and cited. It proposes deep
where a position, a layer of the chain or a design will rest on the
answer. The principal decides. The shape of a note, a bundle and its
plan is set out in
[Research note and bundle](../reference/research-bundle.md).

### The search

Every card is searched by its own isolated agent. An agent here is a
separate run of a model (a subagent) that sees none of the
conversation. Its whole context is a packet, made from the forge's own
definition of a research. The packet holds the card word for word, the
agent's brief, the shape of a note and the known notes the card names.
The brief is the same in every packet. The agents never speak to each
other.

The brief sets the rules an agent searches by:

- Start wide, then narrow: broad queries first, the result list read
  before anything is opened.
- Open a page or do not cite it: no finding from a search snippet or
  a search engine's summary.
- Go upstream: cite the first publisher, and a copy only where the
  original cannot be reached, and then as a copy.
- Exclude sources by kind, never by a list: for example affiliate
  pages, pages mass-produced without an author or a date, and a
  vendor's blog on its own market. A vendor's own documentation about
  its own product is a primary source and is used.
- Name conflicts: two sources that disagree are both cited.
- Say what was not found: "no reliable source on X" is a finding.
- Run the card's disconfirming query and report what it found,
  including nothing.
- Spend a small budget of opened pages on primary sources, and stop by
  the card's stop rule or when the budget is spent.
- Never fabricate a source, a quote, a date or a figure.

A research may also run each card on a model of a second family, on
the same packet, as explained in
[Another model family](another-model-family.md).

### The check before filing

No note is filed before it has been checked. The check has three
parts:

1. Claude reads the note against its shape. A note goes back to its
   agent as a failed run where a finding rests on a snippet without
   saying so, where a source is cited for content but listed as not
   opened, where a quote has no place in its page, or where the search
   record is empty.
2. The note is scanned for the facts of the instance (the one
   installation of the forge), such as names and hosts. Every file
   that may be quoted is scanned the same way.
3. A script opens every URL the note cites, and reads an arXiv page
   for its title.

A dead page, or an identifier that names another paper, sends the note
back to its agent once, with the report. A note that comes back still
failing is filed as it is. The synthesis then names every finding that
rests on a failed citation as without support. A page that refused or
did not answer is unverifiable. It is said so and is never counted as
a failure. The check writes nothing into the note, because the note is
the agent's record.

### The synthesis

When every note has returned, Claude writes the synthesis from the
notes alone. It runs in this order:

1. Completeness, card by card: answered or not found and where it was
   looked, the stop rule met or why the search ended, and what the
   disconfirming query found.
2. The answers side by side, card by card, with the differences
   spelled out.
3. The unexpected finds of every note, gathered before any judgement.
4. What was not found, gathered from every note.
5. Claude's own view, last and apart, marked as its own, and saying in
   plain words whether it is verified or a hypothesis.

A summary placed at the head of the bundle gives the result in the
words Claude reports it to the principal with. A note, a bundle and
its plan are not changed after they are filed.

A second round runs only for gaps the notes name. Claude proposes it
with the gaps listed, and it runs on the principal's word. There is
never a third round.

The course, from the first question to the filed bundle:

```
questions to the principal
  -> draft plan
  -> walkthrough: the principal confirms the plan
  -> one isolated agent per card, each on its packet
  -> check before filing: shape, instance facts, every URL opened
  -> synthesis by Claude, from the notes alone
  -> (a second round, only for gaps the notes name)
```

## Why

The plan comes before the search because the quality of a research is
made by how the topic is split into questions, not by the searching.
The plan is also where the principal sees the questions before they
cost anything. The confirmed plan, and not the finished note, is the
unit the principal consents to. That choice is the principal's wish.

The research exists so that the principal does not reinvent what the
world has already solved.

Every citation is opened before a note is filed, because models can
invent and misnumber sources. Nobody checks that by hand across many
cards. Resolving the URL is the one mitigation of fabricated citations
whose effect has been measured. Why an unanswered page is counted as
unverifiable rather than as a failure is not recorded. Why each note
is scanned for instance facts is that a note is a file that may be
quoted.

Claude's own view stands last and apart, because a claim never gains
certainty by being written down. Claude's constructions are kept from
passing for facts.

Several ways were rejected:

- No recursive deep-dive to a fixed depth. Depth comes from splitting
  the topic into cards, and from a second round only for gaps the
  notes name.
- No fact verified by a count of agreeing sources. Agreement of copies
  is not agreement. Instead a source is opened, dated and placed by
  kind, conflicts are named, and a citation is verified by resolving
  it.
- No saturation measured as a percentage. The stop rule is a rule of
  kind: a differently-worded query brings nothing new and every
  perspective has a primary source, or the budget of openings is
  spent. Which of them ended the search is written into the note's
  search record.

The reasons are not recorded for several other parts of the design:

- why a card holds one kind of evidence only;
- why every card carries a disconfirming query;
- why each agent sees nothing of the conversation;
- why the synthesis draws on the notes alone;
- why the unexpected finds are gathered before any judgement.

## A worked example

One card of a deep research, generic and taken from no project:

```
#### Card 2: formats of a team retrospective
- **Question:** Which formats of a retrospective do teams of up to ten
  people use, and what do practitioners report about each, against
  holding no retrospective at all?
- **Why it matters:** The working agreement of the team rests on
  whether a fixed format is worth adopting.
- **What would answer it:** Practitioners' reported experience, from
  published accounts by the teams or facilitators themselves.
- **Where to look:** Facilitators' own books and sites; conference
  talks by the teams; the original description of each named format.
- **Disconfirming query:** "retrospectives waste of time"; expected:
  critiques of ritual without change, few of them primary.
- **Stop rule:** A differently-worded query brings nothing new and
  every perspective of the card has a primary source; or the budget
  of openings is spent.
```

The card asks one question, answered by one kind of evidence from one
kind of source. If the principal also wanted measured outcomes from
studies, that would be a second card.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
