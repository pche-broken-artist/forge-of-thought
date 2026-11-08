---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: dd03d6d621e4fac6
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

A research is a durable answer to a question the project needs
answered from outside itself, found on the web by isolated agents and
kept in the project's `research/` directory. This page explains why a
research is planned before anything is searched, how the plan, the
search, the check and the synthesis follow one another, and why the
forge rejected the common shortcuts. It is for the user who wants to
know what a research gives him, for the extender who wants to know
where its rules live, and for the evaluator who wants to see how its
findings are kept honest. How to run one is the page
[Research a topic](../use/research-a-topic.md); what a research is as
a resource of the project is [Sources and
research](sources-and-research.md).

## What it is

A research grounds the artefacts of the principal (the person whose
thinking is being forged) in what the world has already solved. He
does not want to reinvent it: outside inspiration is a legitimate
input, and what was found is stored in `research/`, never left in the
conversation.

The quality of a research is made by its plan, not by the searching.
The plan breaks the topic into cards. A card is one question answered
by one kind of evidence from one kind of source. The plan is where
the principal sees the questions before they cost anything, and he
confirms it before a single page is opened.

A research has two depths.

- Deep: a plan of several cards, one isolated agent per card, and a
  bundle `research/YYYY-MM-DD-<topic>/` with the plan and the
  synthesis at its head and one note per card per engine.
- Quick: one card on the session model alone, filed as one note
  `research/YYYY-MM-DD-<topic>.md`, with no plan review and no
  synthesis. The card is still shown before the search.

The principal names the depth at the call. Without his word Claude
proposes one in the plan, with its reason: quick where one question is
to be answered and cited, deep where a position, a layer of the chain
or a design will rest on the answer. The principal decides.

A research is always written in English. The shape of a note, of a
bundle and of its plan is the page [Research note and
bundle](../reference/research-bundle.md).

## How it works

### The plan comes first

Before drafting, Claude asks what the research serves and what the
principal already knows or wants excluded, one question per message.
Nothing is searched. Claude reads the project's indexes of sources and
of research and names the notes and sources the plan will build on.

The draft plan has these sections.

- Purpose: what the research serves in the project, and what is
  already known.
- Perspectives: the standpoints from which the topic is looked at, one
  line each, with the cards that serve it, or "no card" where a
  perspective is left empty on purpose.
- Assumptions: what the plan takes for granted about where the answer
  lives, and what would make it rethink. Then a premortem, answered
  once by Claude and marked as its own: the research is done and
  missed the most interesting thing, what was it?
- Left out: the fields and questions considered and deliberately not
  pursued. "Did not look" is then a statement, not a silence.
- Cards: each one question, with why it matters, what would answer
  it, where to look, a disconfirming query and a stop rule.
- Agents: how many, and the rule that fixed the count, one per card
  per engine and none for a question another card answers.

A card that needs two kinds of evidence is two cards. A card with no
sentence under "why it matters" is cut. For a topic new to the
project the first card asks whether a synthesis already exists and in
what words the field speaks. Its return may rewrite the other cards,
and the plan says so. The bound on the number of cards is a rule of
kind, not a count: past about seven, cards are grouped, and if the
groups still exceed that, the topic is several researches.

The principal confirms the plan in a walkthrough (the list worked one
item per message, each closed with his verdict): perspectives first,
then the cards, then the rest. "Modify" is the normal verdict on a
card. The plan is written nowhere until he confirms it. On his word
the bundle is born with the plan as confirmed at its head.

A deep research may also run on a second model family beside the
session model, which reads the draft plan and then takes every card on
the same packet; how that engine is reached and how its independence
is measured is the page [Another model
family](another-model-family.md).

### Every card is searched by an isolated agent

For each card Claude makes a packet: the card word for word, the
agent's brief, the shape of a note, and the known notes the card
names. The packet is the whole context of the agent. Nothing of the
conversation reaches it, and no packet names a path of the bundle.
The agent's brief is owned by the research definition
(`.claude/skills/research/SKILL.md`) and is the same in every packet,
so that two answers to one question can be compared.

Each agent is a subagent, a run of Claude that sees nothing of the
working conversation; the agents never speak to each other. Before
the agents run, Claude says the model and the size of the run. In the
person's terms, an agent does this.

- It answers the card as put. The question is the principal's, not
  the agent's to widen or narrow; a find that reconfigures the
  question goes under Unexpected while the card is still answered.
- It starts wide and then narrows: short broad queries first, the
  result list read before anything is opened.
- It opens the page or does not cite it. No finding comes from a
  search snippet or a search engine's summary; a summarising fetch is
  a tertiary source, and the note says so where it rests on one.
- It goes upstream and cites the first publisher. A copy, a
  syndication or a vendor's write-up of someone else's result is cited
  only when the original is unreachable, and then as a copy.
- It reads laterally before reading: who publishes this, what others
  say of them, what they sell. A page's own look, byline and dates
  count for nothing.
- It excludes sources by kind, never by list: affiliate pages,
  mass-produced pages without oversight, third-party content riding a
  host's reputation, a vendor's blog on its own market, undated pages
  for any time-sensitive claim. A vendor's own documentation about its
  own product is a primary source and is used.
- It records every source and every finding; a page it did not open
  is "not opened", whatever the search result said about it.
- It names conflicts: two sources that disagree are both cited, never
  one picked in silence. Agreement of copies is not agreement.
- It says what it did not find. "No reliable source on X" is a
  finding.
- It runs the disconfirming query of the card and reports what it
  found, including nothing.
- It spends its openings on primaries, about ten to fifteen pages and
  never many more. More calls have been measured to lower the
  accuracy of citations, not raise it.
- It stops by the card's stop rule or when the openings are spent,
  and writes in the Search record which ended the run.
- It never fabricates a source, a quote, a date or a figure. A quote
  is verbatim and short, with where in the page it stands. An
  identifier such as an arXiv number or a DOI is cited only from the
  page opened under it, never from memory.

The agent writes no file. Its whole note is its final message, and
Claude files it.

### Every note is checked before it is filed

Three checks stand between a returned note and the bundle.

1. Claude reads the note against the shape of a note. A finding
   resting on a snippet alone without saying so, a source cited for
   content but listed as not opened, a quote without its place or an
   empty Search record sends the note back to its agent as a failed
   run.
2. The note is scanned for the facts of the instance (names,
   accounts, hosts), as every file that may be quoted is scanned.
3. A script, `scripts/forge-cite.py`, opens every URL the note cites
   and reads an arXiv page for its title. A dead page, or an
   identifier that names another paper, is the mark of a fabricated
   citation. The note goes back to its agent once, with the report,
   as a failed run. A note that comes back still failing is filed as
   it is, and the synthesis names every finding that rests on a
   failed citation as without support. A page that refused or did not
   answer is unverifiable: the note says so, and it is never counted
   as a failure.

The check writes nothing into the note. The note is the agent's
record.

### The synthesis is Claude's, from the notes alone

When every note has returned, Claude writes the synthesis into the
head of the bundle, from the notes and nothing else, in this order.

- Completeness, card by card: answered, or not found and where it was
  looked; the stop rule met, or why searching ended; what the
  disconfirming query found, including nothing.
- Answers side by side: per card, the answers laid beside each other
  with the engine named. Agreement is reported as consistency, never
  as validation. The differences are spelled out, since they are the
  valuable part. Two engines citing the same copy count as one source.
- Unexpected, gathered: the Unexpected sections of every note, sorted
  by one test, a find that reconfigured a question or brought a
  mechanism from elsewhere against a find that adds a source to a
  point already made. Shown before any judgement.
- Not found, gathered: what every note reported not finding.
- Claude's view, last and apart: what Claude makes of it, marked as
  its own, verified or hypothesis said in plain words, and what it
  proposes to change in the chain.

The bundle opens with a summary: what the research says, in the words
Claude reports it to the principal with. Every note opens with its
answer in a few sentences. The plan, the notes and the bundle are
immutable from the filing of the synthesis. Every difference between
the plan as confirmed and the run as it went is recorded under
Deviations, with its reason; "none" is a legitimate entry.

A second round runs only for gaps the notes name. Claude proposes it
with the gaps listed, and it runs on the principal's word. There is
no third round.

Claude then reports to the principal, leading with what the research
says and where the answers differ, not with a literature review. What
the research suggests for an artefact of the chain is proposed
explicitly, through `/forge <state>`, never taken in silently.

## Why

**Why the plan comes before the search.** The quality of a research
is made by the decomposition into cards, not by the searching. The
plan is where the principal sees the questions before they cost
anything. The plan was chosen as the unit of consent, against the
finished note as before, because the principal wished it so.

**Why one question, one kind of evidence, one kind of source per
card.** The reason beyond the decomposition itself is not recorded.

**Why every citation is opened by a script.** Resolving the URL is the
one mitigation of a fabricated citation with a measured effect, and
nobody checks that by hand across cards and engines. A dead page or an
identifier that names another paper is exactly what a fabricated
citation looks like.

**Why Claude's view stands last and apart.** Whatever Claude brings
as knowledge says in plain words whether it is verified and on what,
unverified, or a hypothesis. A claim never gains certainty by being
written into an artefact. Keeping Claude's view apart from the
gathered findings keeps its constructions from passing for facts.

**Why nothing of the conversation reaches a packet.** The reason is
not recorded beyond the general rule for every isolated agent of the
forge.

**Why no recursive deep-dive to a fixed depth.** Depth comes from the
decomposition into cards and from a second round only for gaps the
notes name, never a third.

**Why no fact is verified by a count of agreeing sources.** Agreement
of copies is not agreement. A source is opened, dated and placed by
kind, conflicts are named, and a citation is verified by resolving it.

**Why no saturation as a percentage.** The stop rule is a rule of
kind: a differently-worded query brings nothing new and every
perspective has a primary source, or the openings are spent. Which of
these ended the run is written into the search record.

## A worked example: a generic card

A project is writing an assignment for a team of about a dozen people
and wants to replace a weekly status meeting with a written report.
One card of its research plan might read as follows.

```
#### Card 2: Written status instead of a weekly meeting
- **Question:** Does a written weekly status report, read
  asynchronously, reduce the time a team of five to twenty spends in
  status meetings, compared with a weekly meeting of the whole team?
- **Why it matters:** The assignment's deliverable on team rhythm
  rests on whether the saving is real or only moves the time.
- **What would answer it:** A measured before-and-after of meeting
  hours, from an organisation's own published engineering report or
  a peer-reviewed study.
- **Where to look:** Engineering blogs of organisations that made the
  change, as primaries; research databases for studies of
  asynchronous communication; practitioner books only for the words
  the field uses. Known items that must turn up: none.
- **Disconfirming query:** "written status reports more meetings"
  and "async status update failed"; expected: that written reports
  cut meeting time but not the number of one-to-one follow-ups.
- **Stop rule:** Nothing new from a differently-worded query, and
  both perspectives of the card (the team member, the manager) have a
  primary source; about a dozen openings.
```

The card asks one question, names one kind of evidence from one kind
of source, says what would find the opposite, and says when to stop.
A card that also asked whether the report should be a page or a table
would be a second card, since it needs another kind of evidence.

## See also

- [Research a topic](../use/research-a-topic.md): running
  `/research`.
- [Another model family](another-model-family.md): the second engine,
  how it is reached and how its independence is measured.
- [Sources and research](sources-and-research.md): research as a
  resource of the project.
- [Research note and bundle](../reference/research-bundle.md): the
  shape of a note, a bundle and its plan.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
