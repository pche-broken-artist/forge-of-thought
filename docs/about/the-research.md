---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 73180409cd42e2c3
inputs:
  - projects/forge/10-intent.md#POS.0050
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.1890
  - projects/forge/10-intent.md#POS.1370
  - projects/forge/10-intent.md#REJ.0450
  - projects/forge/10-intent.md#REJ.0460
  - projects/forge/10-intent.md#REJ.0470
  - projects/forge/40-solution-design.md#SOL.0860
  - projects/forge/40-solution-design.md#SOL.0880
  - .claude/skills/research/SKILL.md
  - templates/research-plan.md
---

# How a research is made

A research is a look into what the world has already solved on a
topic, made from a plan that the
[principal](../reference/glossary.md) (the person whose thinking is
being forged) confirms before anything is searched. This page
explains how a research is planned, searched, checked and put
together, and why it is made in that order. It is for the reader who
runs a research, the one who extends the forge and the one who judges
how far a result can be trusted. How the command is run is on
[Research a topic](../use/research-a-topic.md).

## What it is

A research grounds the principal's
[artefacts](../reference/glossary.md) (the documents of the project's
chain) in what the world has already solved. The principal does not
want to reinvent it. For key topics Claude researches current best
practice rather than inventing, and outside inspiration is a
legitimate input. What is found is stored in the project's
`research/` directory, not left in the conversation.

The quality of a research is made by its plan, not by the searching.
The plan cuts the topic into cards. A card is one question answered
by one kind of evidence from one kind of source. An isolated agent
searches each card and returns one
[note](../reference/research-bundle.md). Claude puts the notes
together in a synthesis.

A research has two depths:

- **Deep**: a plan of several cards. It is filed as a
  [bundle](../reference/research-bundle.md), that is a directory
  `research/YYYY-MM-DD-<topic>/` with the plan and the synthesis at
  its head and one note per card per engine. An engine is the forge's
  name for a model family that searches. The forge names engines,
  never models.
- **Quick**: one card. The card is still shown before the search.
  There is no synthesis, and the result is filed as a single note
  `research/YYYY-MM-DD-<topic>.md`.

The principal names the depth with a word of the command. Without
the word, Claude proposes the depth in the plan and gives its reason:
quick where one question is to be answered and cited, deep where a
position, a layer of the chain or a design will rest on the answer.
The principal decides. A deep research can also run on a second
model family beside the first, asked for by name:
[Another model family](another-model-family.md) says how the second
engine is reached and how its independence is measured.

## How it works

The course of a deep research, from the first question to the
synthesis:

```
questions to the principal
  -> draft plan
  -> walkthrough of the plan: confirmed, the bundle is born
  -> per card: one packet, one isolated agent, one note
  -> per note: read against its shape, scanned for instance facts,
     every URL opened; a failing note goes back to its agent
  -> the note is filed
  -> synthesis, from the notes alone
  -> a second round for gaps the notes name, at most one
```

### The plan comes first

Before a plan is drafted, Claude asks what the research serves and
what the principal already knows or wants excluded, one question per
message. It reads the project's two indexes (the catalogues of its
research and of its sources) and names the notes and sources the plan
will build on. Nothing is searched.

The draft plan has these sections:

- **Purpose**: what the research serves in the project, and what is
  already known.
- **Perspectives**: the standpoints from which the topic is treated,
  one line each, with the cards that serve it, or "no card" where the
  plan leaves a perspective empty on purpose.
- **Assumptions**: what the plan takes for granted about where the
  answer lives, and what would make it rethink. Then a premortem,
  answered once by Claude and marked as its own: "the research is
  done and missed the most interesting thing: what was it?"
- **Left out**: the fields and questions considered and deliberately
  not pursued.
- **Cards**: the questions themselves.
- **Agents**: how many agents search, and the rule that fixed the
  count, which is one per card per engine and none for a question
  another card answers. Also whether a second round is allowed, and
  for what.

A card has six lines:

- **Question**: what is asked, about what, in what context, against
  what alternative.
- **Why it matters**: the decision or artefact the card serves, in
  one sentence.
- **What would answer it**: one kind of evidence, and the kind of
  source it lives in.
- **Where to look**: kinds of source, by more than one route, and the
  known items that must turn up.
- **Disconfirming query**: one search written to find the opposite of
  what is expected, and what is expected.
- **Stop rule**: a differently-worded query brings nothing new and
  every perspective of the card has a primary source, or the budget
  of opened pages is spent.

A card that needs two kinds of evidence or two kinds of source is two
cards. A card with no sentence under "Why it matters" is cut. For a
topic new to the project, the first card asks whether a synthesis
already exists and in what words the field speaks. Its return may
rewrite the other cards, and the plan says so. The number of cards is
bounded by the rule of kind, not by a count. Past about seven, cards
are grouped. Where the groups still exceed that, the topic is several
researches.

The plan is confirmed in a [walkthrough](../reference/glossary.md)
(a list of items worked one per message, each closed with a line of
verdicts for the principal to choose from) before anything is
searched or costs anything. The perspectives come first, then the
cards, then the rest. The normal verdict on a card is "modify". The
plan is written nowhere until the principal confirms it. On the
principal's word the bundle is born, with the plan as confirmed, word
for word. A quick research has one card, shown in one message with
the line of verdicts, before anything is searched.

### Every card is searched in isolation

For each card Claude composes a packet. The packet is the whole
context of one agent. It holds:

- the card, word for word;
- the agent's brief, word for word, the same in every packet;
- the shape of a note;
- copies of the notes the project already holds that the card names,
  and the list of them;
- the sentence that the agent writes no file and returns the whole
  note as its final message.

Nothing of the conversation reaches a packet. One isolated agent with
access to the web takes each packet. The agents run in parallel and
never speak to each other. Claude says the model and the size of the
run before the agents start. The packets stay in the working folder
of the run under `tmp/` for inspection, and nothing there is a source
of truth.

The brief is kept in one place (the skill of the command,
`.claude/skills/research/SKILL.md`). It holds every agent to the same
conduct:

- **It answers the card as put.** The question belongs to the
  principal and is neither widened nor narrowed. A find that
  reconfigures the question is reported as unexpected, and the card
  is still answered.
- **It starts wide, then narrows.** Short broad queries come first,
  and the list of results is read before any page is opened.
- **It opens a page or does not cite it.** No finding rests on a
  search snippet or on a search engine's summary. A fetch that
  summarises a page is a tertiary source, and the note says where it
  rests on one. A page that was not opened is recorded as "not
  opened".
- **It goes upstream.** The first publisher is cited. A copy, a
  syndication, an aggregator or a vendor's write-up of someone else's
  result is cited only when the original is unreachable, and then as
  a copy.
- **It excludes sources by kind, never by a list.** Excluded are
  affiliate pages whose content comes from the merchant, pages
  mass-produced without oversight, third-party content that rides a
  host's reputation, a vendor's blog on its own market and undated
  pages for a time-sensitive claim. A vendor's own documentation
  about its own product is a primary source and is used.
- **It names conflicts.** Two sources that disagree are both cited,
  never one picked in silence. Agreement of copies is not agreement.
- **It says what it did not find.** "No reliable source on X" is a
  finding. The card's disconfirming query is run and its result
  reported, including nothing.
- **It stops by a rule.** The run ends by the card's stop rule or
  when the openings are spent (about ten to fifteen opened pages).
  The note's search record says which of the two ended the run.
- **It never fabricates.** No source, quote, date or figure is made
  up. A quote is verbatim and short, with its place in the page. An
  identifier of a paper is cited only from the page opened under it,
  never from memory.

Nothing that names a person, a company or a host of the principal's
own stands in a packet, and nothing of the kind enters a note.

### A note is checked before it is filed

Three checks stand between an agent's return and the filing, in this
order:

1. Claude reads the note against the shape of a note. A note fails
   where a finding rests on a snippet or a summarised fetch alone
   without saying so, where a source is cited for content but listed
   as not opened, where a quote has no place, or where the search
   record is empty. A failing note goes back to its agent as a failed
   run and is not filed.
2. The script `scripts/docs-check.py` scans the note for instance
   facts (facts of one installation, such as a person, a company or a
   host of the principal's own). Every file that may be quoted is
   scanned in this way.
3. The script `scripts/forge-cite.py` opens every URL the note cites,
   once, and judges each.

The script gives each URL one of four verdicts:

- **ok**: the citation resolves.
- **dead**: the page is dead.
- **mismatch**: an identifier of a paper names another paper than the
  note says. The script finds this where the title under an arXiv
  identifier shares too few words with the note's entry.
- **unverifiable**: the page refused or did not answer. This is said
  and never counted as a failure.

The script writes its report into the working folder of the run and
ends with a failure on anything dead or mismatched. It writes nothing
into the note.

A note with a dead or mismatched citation goes back to its agent
once, with the report, as a failed run. A note that comes back still
failing is filed as it is, and the synthesis names every finding that
rests on a failed citation as without support.

### The synthesis is made from the notes alone

When every note has returned, Claude writes the synthesis itself,
from the notes alone, under the plan at the head of the bundle. Its
parts stand in a fixed order:

- **Completeness, card by card**: whether the card was answered, or
  not found and where it was looked; whether the stop rule was met,
  or why searching ended; what the disconfirming query found,
  including nothing.
- **Answers side by side**: per card, the answers laid beside each
  other with the engine named. Agreement is reported as consistency,
  never as validation. The differences are spelled out: they are the
  valuable part. Two answers that cite the same copy are noted as one
  source, not two.
- **Unexpected, gathered**: what every note reported as unexpected,
  sorted by one test: a find that reconfigured a question or brought
  a mechanism from elsewhere, against a find that adds a source to a
  point already made. It is shown before any judgement.
- **Not found, gathered**: what every note reported not finding, put
  together.
- **Claude's view**: last and apart, marked as its own, with verified
  or hypothesis said in plain words. What it suggests for an artefact
  is proposed explicitly, never silently.

A summary is written at the synthesis and placed first in the head of
the bundle: what the research says, in the words Claude reports it to
the principal with. A reader who stops there has the result. Every
note opens in the same way, with its answer in a few sentences. Every
difference between the plan as confirmed and the run as it went is
recorded in the bundle with its reason, and "None" is a legitimate
entry. With the synthesis filed the bundle is immutable: nothing in
it changes afterwards.

A second round is run only for gaps the notes name. Claude proposes
it with the gaps listed, and it runs on the principal's word. There
is never a third.

The bundle then gets one entry in the index of the project's
research, written from the synthesis: the question, the answer in
short and when to consult it. How research serves a project as a
resource is on [Sources and research](sources-and-research.md).
Claude's report to the principal leads with what the research says,
not with a literature review.

## Why

**The plan before the search.** The quality of a research is made by
the decomposition into cards, not by the searching. The plan is also
where the principal sees the questions before they cost anything. The
design chose the plan as the unit of consent, against the finished
note. The reason it records is the wish of the forge's own principal.

**What is left out is written down.** The plan names the fields and
questions it does not pursue. "Did not look" is then a statement, not
a silence.

**A small budget of opened pages.** The agent's brief gives the
reason: more calls have been measured to lower the accuracy of
citations, not to raise it.

**Every citation opened by a script.** Nobody checks citations by
hand across cards and engines. Resolving the URL is the one
mitigation of fabricated citations with a measured effect. A dead
page or an identifier that names another paper is the mark of a
fabricated citation. A page that refused or did not answer is not a
failure. The reason is that a site that blocks bots is the normal
case. The check writes nothing into the note. The reason is that the
note is the agent's record.

**Claude's view last and apart.** Whatever Claude brings as knowledge
says in plain words whether it is verified and on what, unverified,
or a hypothesis. A claim never gains certainty by being written into
an artefact. In a synthesis the gathered notes therefore come first,
and Claude's own view stands after them, marked as its own.

Three things a research does not do, each with its reason:

- **No recursive deep-dive to a fixed depth.** Depth comes from the
  decomposition into cards and from the one second round for gaps the
  notes name.
- **No fact verified by a count of agreeing sources.** Agreement of
  copies is not agreement. A source is opened, dated and placed by
  kind, conflicts are named, and a citation is verified by resolving
  it.
- **No saturation as a percentage.** The stop rule is a rule of kind:
  a differently-worded query brings nothing new and every perspective
  has a primary source, or the openings are spent. Which of the two
  ended the run is written into the search record.

For three rules the reason is not recorded:

- why an agent sees nothing of the conversation;
- why a note with a failed citation goes back to its agent once and
  no more;
- why a second round is never followed by a third.

## A worked example

A generic card, in the shape the template of a plan
(`templates/research-plan.md`) gives:

```
#### Card 2: does a handover checklist reduce omissions
- **Question:** Does a written checklist at a shift handover reduce the items left out, in teams that hand over every day, against a handover told from memory?
- **Why it matters:** The decision whether handovers get a prescribed checklist rests on this answer.
- **What would answer it:** Measured comparisons of omissions with and without a checklist, in peer-reviewed studies.
- **Where to look:** Journals of the fields that hand over every day, reached by a database search and by the references of a review; the review the project already holds must turn up.
- **Disconfirming query:** "handover checklist no effect"; what is expected is that a checklist reduces omissions.
- **Stop rule:** A differently-worded query brings nothing new and every perspective of the card has a primary source, or twelve pages are opened.
```

This is one card: one question, one kind of evidence (measured
comparisons) and one kind of source (peer-reviewed studies). Had it
also asked how the people who hand over judge the checklist, that
would be a second kind of evidence from a second kind of source, and
a second card. Had nothing stood under "Why it matters", the card
would have been cut. The disconfirming query looks for the opposite
of what is expected, and the agent reports what it found, including
nothing. The stop rule tells the agent when to end, and the note's
search record says which part of the rule ended the run.

## See also

- [Research a topic](../use/research-a-topic.md): running
  `/research`.
- [Another model family](another-model-family.md): the second engine,
  how it is reached and how its independence is measured.
- [Sources and research](sources-and-research.md): research as a
  resource of the project.
- [Research note and bundle](../reference/research-bundle.md): the
  shape of a note, a bundle and its plan.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
