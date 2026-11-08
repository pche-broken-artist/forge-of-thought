---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 892aee73132ba30b
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

A research is the forge's way of looking up what the world has
already solved before the principal (the person whose thinking is
being forged) shapes an artefact of his own. This page explains why
a research is planned before anything is searched, how the searching
is kept honest, and how the result is put together. It is for the
user who wants to know what happens behind `/research`, for the
extender who changes it, and for the evaluator who asks whether the
mechanism holds. How to run one is on the page
[Research a topic](../use/research-a-topic.md).

## What it is

A research grounds the principal's artefacts in current practice.
For a key topic Claude researches what exists rather than inventing
it. Outside inspiration is a legitimate input. Durable findings are
stored in the project's `research/` directory, not left in the
conversation; what a research is as a resource of the project is on
the page [Sources and research](sources-and-research.md).

The quality of a research is made by its plan, not by the searching.
The plan breaks the topic into questions, and the principal sees and
confirms those questions before anything is searched or costs
anything. The plan is therefore the unit of his consent. The finished
note is not what he is asked to approve.

## How it works

### The plan

Before anything is drafted, Claude asks what the research serves and
what the principal already knows or wants excluded, one question per
message. It reads the project's indexes of sources and research and
names the notes and sources the plan will build on.

The draft plan has a fixed shape (the shape is on the page
[Research note and bundle](../reference/research-bundle.md)). Its
sections are:

- the purpose: the thread, position, decision or artefact the
  research feeds, and what is already known;
- the perspectives: the standpoints from which the topic is treated,
  each with the cards that serve it, or "no card" where a
  perspective is left empty on purpose;
- the assumptions: what the plan takes for granted about where the
  answer lives, what would make it rethink, and a premortem answered
  once by Claude and marked as its own ("the research is done and
  missed the most interesting thing: what was it?");
- what is left out: the fields and questions considered and
  deliberately not pursued, so that "did not look" is a statement
  and not a silence;
- the cards, described below;
- the agents: how many, and the rule that fixed the count, one per
  card per engine and none for a question another card answers.

The principal confirms the plan in a walkthrough (the forge's way of
working a list one item per message, each item closed with a verdict
of accept, modify, question, reject or park): the perspectives
first, then the cards, then the rest. Modify is the normal verdict on
a card. The plan is written nowhere until the principal confirms it.
On his word the plan is filed as the head of the research, and the
searching may begin.

### The cards

A card is one question answered by one kind of evidence from one
kind of source. A card that needs two kinds of evidence is two cards.
A card with nothing to say under "why it matters" is cut. Each card
carries:

- the question: what is asked, about what, in what context, against
  what alternative;
- why it matters: the decision or artefact it serves;
- what would answer it: one kind of evidence, and the kind of source
  it lives in;
- where to look: more than one route, and the known items that must
  turn up;
- a disconfirming query: one search written to find the opposite of
  what is expected, with what is expected;
- a stop rule: nothing new from a differently worded query, every
  perspective of the card with a primary source, and the budget of
  pages to open.

For a topic new to the project the first card asks whether a
synthesis already exists and in what words the field speaks. Its
return may rewrite the other cards, and the plan says so. The bound
on the number of cards is the kind rule, not a count. Past about
seven, cards are grouped. If the groups still exceed that, the topic
is several researches.

### Two depths

A research has two depths, said by the principal as a parameter of
the command.

- Deep: the whole course on the session model (the model the
  conversation runs on). The plan has several cards. The result is a
  bundle, a directory with the plan and the synthesis at its head
  and one note per card per engine.
- Quick: one card on the session model alone, filed as a single
  note. The card is still shown with the verdict line before anything
  is searched. There is no plan review and no synthesis.

Without the word, Claude proposes the depth with its reason: quick
where one question is to be answered and cited, deep where a
position, a layer of the chain or a design will rest on the answer.
The principal decides.

A deep research may also run on a second engine of another model
family beside the session model, so that two full answers to one
question can be laid side by side; how that engine is reached and how
its independence is measured is on the page
[Another model family](another-model-family.md).

### The search

Every card is searched by an isolated agent (a subagent: a run of the
model with a context of its own, which never sees the working
conversation). The agent sees a packet and nothing else. The packet
is composed from the forge's own definition: the card word for word,
the agent's brief, the shape a note must have, and the known notes
the card names. Nothing of the conversation reaches a packet, and the
brief is the same in every packet. The agent writes no file; it
returns the whole note as its final message, and Claude files it.

The brief tells the agent how to search and how to record. In the
reader's terms, the agent:

- answers the card as put, without widening or narrowing the
  question; a find that reconfigures the question goes into the
  note's Unexpected section while the card is still answered;
- starts wide and then narrows: short broad queries first, the
  result list read before anything is opened;
- opens a page or does not cite it: no finding rests on a search
  snippet or a search engine's summary, and a summarising fetch is
  named as a tertiary source where the note rests on one;
- goes upstream and cites the first publisher; a copy, a syndication
  or a vendor's write-up of someone else's result is cited only when
  the original is unreachable, and then as a copy;
- reads laterally before reading: who publishes this, what others say
  of them, what they sell; a page's own look, byline and dates count
  for nothing;
- excludes sources by kind, never by list: affiliate pages, pages
  mass-produced without oversight, third-party content riding a
  host's reputation, a vendor's blog on its own market, undated pages
  for a time-sensitive claim; a vendor's own documentation about its
  own product is a primary source and is used;
- records every source and every finding as the note's shape asks; a
  page it did not open is "not opened";
- names conflicts: two sources that disagree are both cited, never
  one picked in silence; agreement of copies is not agreement;
- says what it did not find: "no reliable source on X" is a finding;
- runs the disconfirming query of the card and reports what it found,
  including nothing;
- spends its openings on primaries, about ten to fifteen pages, and
  stops by the card's stop rule or when the openings are spent,
  writing in the note's search record which ended the run;
- never fabricates a source, a quote, a date or a figure; a quote is
  verbatim and short, with its place in the page; an identifier such
  as a DOI is cited only from the page opened under it, never from
  memory.

### The check before filing

No note is filed before three checks. First, Claude reads the note
against the shape of its template. A finding that rests on a snippet
or a summarised fetch without saying so, a source cited for content
but listed as not opened, a quote without its place, or an empty
search record sends the note back to its agent as a failed run.
Second, the note is scanned for the instance's facts, as every file
that may be quoted is scanned, so that no name, host or account of
the installation enters it. Third, a script opens every URL the note
cites and reads an arXiv page for its title.

A dead page, or an identifier that names another paper, is the mark
of a fabricated citation. Such a note goes back to its agent once,
with the report, as a failed run. A note that comes back still failing
is filed as it is, and the synthesis names every finding that rests
on a failed citation as without support. A page that refused or did
not answer is unverifiable: the note says so, and it is never counted
as a failure. The check writes nothing into the note. The note stays
the agent's record.

### The synthesis and the second round

When every note has returned, Claude writes the synthesis from the
notes alone, at the head of the bundle under the plan. It has a fixed
order:

- completeness, card by card: answered, or not found and where it
  was looked; the stop rule met, or why searching ended; what the
  disconfirming query found, including nothing;
- the answers side by side, per card, with the engine named;
  agreement is reported as consistency, never as validation;
- the Unexpected sections of every note gathered, sorted by one
  test: a find that reconfigured a question or brought a mechanism
  from elsewhere, against a find that only adds a source to a point
  already made; shown before any judgement;
- what was not found, gathered;
- Claude's own view, last and apart, marked as its own, verified or
  hypothesis said in plain words; what it proposes to change in the
  chain is proposed explicitly through the forge's command for the
  artefact, never written silently.

The bundle also opens with a summary, written at the synthesis: what
the research says in the words the principal is told it in, what was
unexpected and what it suggests for the project. Every difference
between the plan as confirmed and the run as it went is recorded under
Deviations, with its reason; "none" is a legitimate entry.

From the filing of the synthesis the bundle is immutable. A second
round is allowed only for gaps the notes name. Claude proposes it
with the gaps listed and runs it on the principal's word. There is no
third round.

Afterwards the research gets one entry in the project's research
index, written from the synthesis, and the ledger (the project's
state report, made at read time from its documents) is remade by its
script.

## Why

The plan comes first because the quality of a research is made by
the decomposition into questions, not by the searching. The plan is
where the principal sees the questions before they cost anything. The
plan was chosen as the unit of his consent, against the finished note
as before, because that was the principal's wish.

Each card is one question, one kind of evidence and one kind of
source so that the decomposition does the work. The reason a card
that needs two kinds is split, and the reason a card with nothing
under "why it matters" is cut, is not recorded beyond that rule.

The agent sees a packet made from the forge's own definition, with
the same brief in every packet, because the forge's definition is the
one owner of the agent's rules. The reason a packet carries nothing
of the conversation is the isolation that holds for every subagent of
the forge: an isolated agent reads every input from disk in its own
run, and nothing of the instance enters what it returns.

Every citation is opened before a note is filed because nobody checks
across cards and engines by hand whether a source was invented or
misnumbered, and resolving the URL is the one mitigation of fabricated
citations with a measured effect. An unverifiable page is never
counted as a failure; the reason is not recorded beyond the
distinction between a page that is dead and a page that did not
answer.

Claude's own view stands last and apart because how sure a claim is
must be said in words: whatever Claude brings as knowledge says
whether it is verified and on what, unverified, or a hypothesis, and
a claim never gains certainty by being written into an artefact. The
synthesis gathers the Unexpected before any judgement for the same
reason: Claude's constructions must not pass for facts. The reason
the synthesis is made from the notes alone is not recorded beyond
that.

Three ways of doing it were rejected.

- Recursive deep-diving to a fixed depth was rejected because depth
  comes from the decomposition into cards and from a second round
  only for gaps the notes name, never a third.
- A fact verified by a count of agreeing sources was rejected because
  agreement of copies is not agreement. A source is opened, dated and
  placed by kind, conflicts are named, and a citation is verified by
  resolving it.
- Saturation as a percentage was rejected because the stop rule is a
  kind rule: a differently worded query bringing nothing new and
  every perspective with a primary source, or the openings spent,
  written into the search record.

Every term used here is defined in one line in the
[Glossary](../reference/glossary.md).

## A worked example: a generic card

A card of a plan, taken from no project, in the shape the template
gives it:

```
#### Card 2: how distributed teams keep a shared glossary current
- **Question:** How do distributed teams keep a shared glossary of
  terms current once it exists, against the alternative of letting
  each team keep its own wording?
- **Why it matters:** The assignment will name one owner for the
  project's vocabulary, and the choice of owner rests on what has
  worked elsewhere.
- **What would answer it:** Published accounts of a glossary kept
  current over years, in practitioners' own write-ups or in a
  standards body's documented practice.
- **Where to look:** Standards bodies' process documents; engineering
  blogs of organisations known for documentation; the known note on
  documentation ownership must turn up.
- **Disconfirming query:** "shared glossary abandoned" and "glossary
  drift distributed teams": expected is that glossaries without a
  named owner decay, and the query looks for one that survived
  without an owner.
- **Stop rule:** Nothing new from a differently worded query, and
  each of the two perspectives of the card (owned and unowned
  glossaries) has a primary source; about twelve pages opened.
```

One question, one kind of evidence, one kind of source. A card that
also asked how the glossary is first built would be two cards.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
