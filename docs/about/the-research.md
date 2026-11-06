---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 9563f5c1e37b2098
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
answered, found on the web by isolated agents and kept in the
project's `research/` directory. This page explains what a research
is, how it goes from a plan to a filed synthesis, and why it is made
that way: why the plan comes before any search, and how what the
agents find is kept honest. It is for the user who orders one, the
extender who changes how it runs and the evaluator who wants to
judge whether its answers can be trusted. How to run one is the page
[Research a topic](../use/research-a-topic.md); what a note and a
bundle look like on disk is [Research note and
bundle](../reference/research-bundle.md).

## What it is

A research grounds the principal's artefacts in what the world has
already solved. The principal is the person whose thinking is
forged; his artefacts are the documents of the project's chain, the
intent and the layers below it. For a key topic Claude researches
current practice rather than inventing it. Outside inspiration is a
legitimate input. What is found is stored in `research/`, not left
in the conversation, so that it is there the next time the question
comes up ([Sources and research](sources-and-research.md) says how
the directory is catalogued).

The quality of a research is made by its plan, not by the searching.
The plan is the decomposition of the topic into questions, and it is
shown to the principal and confirmed before anything is searched or
costs anything.

A research has two depths. The principal names the depth as a
parameter of `/research`, in the shape `/save --quick` has; without
the word, Claude proposes a depth with its reason and the principal
decides.

- Deep: a plan of several cards, one isolated agent per card, and a
  bundle `research/YYYY-MM-DD-<topic>/` with the plan and the
  synthesis at its head (`00-plan.md`) and one note per card per
  engine (`<card>.<engine>.md`). Claude proposes it where a
  position, a layer of the chain or a design will rest on the
  answer.
- Quick: one card on the session model alone, filed as a single
  note `research/YYYY-MM-DD-<topic>.md`. The card is still shown
  before the search. There is no plan review, no second engine and
  no synthesis. Claude proposes it where one question is to be
  answered and cited.

A deep research may also run on an engine of another model family
beside the session model, which reads the draft plan and then takes
every card on the same packet as the session agent; how that engine
is reached and how its independence is measured is the page
[Another model family](another-model-family.md).

A note, a bundle and its plan are immutable from their filing: the
bundle from the filing of its synthesis. The bundle opens with a
summary and every note with its answer in a few sentences, in the
words the principal would be told it in. Every research is written
in English, as every record of the forge is.

## How it works

The course of a deep research runs in this order. A quick research
takes the same course without the plan walkthrough and without the
synthesis: one card, shown in one message with the verdict line, is
confirmed, searched, checked and filed.

**Questions before the plan.** Claude asks what the research serves,
and what the principal already knows or wants excluded. It asks one
question per message, as the elicitation interview has it (see the
[Glossary](../reference/glossary.md)). Nothing is searched. Claude
reads the indexes of `research/` and `sources/` and names the notes
and sources the plan will build on.

**The draft plan.** Claude drafts the plan in the shape the plan
skeleton gives. A plan has these parts:

- the purpose: what the research serves in the project, and what is
  already known;
- the perspectives: the standpoints the topic is looked at from, one
  line each, with the cards that serve it, or "no card" where a
  perspective is left empty on purpose;
- the assumptions: what the plan takes for granted about where the
  answer lives, what would make it rethink, and a premortem answered
  once by Claude and marked as its own ("the research is done and
  missed the most interesting thing: what was it?");
- what is left out: the fields and questions considered and not
  pursued, so that "did not look" is a statement and not a silence;
- the cards;
- the agents: how many, and the rule that fixed the count, one per
  card per engine and none for a question another card answers;
  whether a second round is allowed and for what.

A card is one question answered by one kind of evidence from one
kind of source. A card that needs two kinds of evidence is two
cards. A card with no sentence under "why it matters" is cut. Every
card carries the question, why it matters, what would answer it,
where to look, a disconfirming query and a stop rule. For a topic
new to the project the first card asks whether a synthesis already
exists and in what words the field speaks; its return may rewrite
the other cards, and the plan says so. The bound on the number of
cards is the kind rule, not a count. Past about seven, cards are
grouped; if the groups still exceed that, the topic is several
researches. A topic that is one card is said so, and the plan is one
card.

**The walkthrough of the plan.** The plan is confirmed in a
walkthrough, the forge's way of working a list of items one item per
message, each closed with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. Perspectives
come first, then the cards, then the rest. `(m)odify` is the normal
verdict on a card. The plan is written nowhere until the principal
confirms it. On his word the bundle is born: `00-plan.md` with the
plan as confirmed and the status `draft`. Its index entry waits for
the synthesis.

**The dispatch.** For every card Claude makes a packet folder under
`tmp/research/<run>/<card>/`. The packet is the whole context of the
agent, and it is made from the forge's own definition, never from
the conversation. It holds:

- the card, word for word;
- the agent's brief, word for word, the same text in every packet;
- the shape of a note, word for word;
- the list of the known notes attached to the card, and their
  copies;
- the sentence that the agent writes no file and returns the whole
  note as its final message.

No packet names a path of the bundle or of another engine's note;
the bundle is named by its directory name alone. Then Claude runs
one isolated subagent per card in parallel, with web access, its
prompt the packet's text and the path of its folder. A subagent is a
separate run of Claude that sees nothing of the working conversation
and reads everything it uses from disk. The agents never speak to
each other. Before the run Claude says the model and the size.

**What the agent does.** The agent's brief is owned by the research
definition, and it is the same for every card. In the person's
terms, the agent works like this:

- It answers the card as put; the question is the principal's, not
  the agent's to widen or narrow. A find that reconfigures the
  question goes under Unexpected in plain words, while the card is
  still answered.
- It starts wide and then narrows: short broad queries, the result
  list read before anything is opened, then pages opened.
- It opens a page or does not cite it. No finding rests on a search
  snippet or a search engine's summary. A summarising fetch is a
  tertiary source, and the note says so where it rests on one.
- It goes upstream and cites the first publisher. A copy, a
  syndication, an aggregator or a vendor's write-up of someone
  else's result is cited only when the original is unreachable, and
  then as a copy.
- It reads laterally before reading: who publishes a page, what
  others say of them, what they sell. A page's own look, byline and
  dates count for nothing.
- It excludes sources by kind, never by list. Excluded are affiliate
  pages whose content comes from the merchant, pages mass-produced
  without oversight, third-party content riding a host's reputation,
  a vendor's blog on its own market, and undated pages for any
  time-sensitive claim. A vendor's own documentation about its own
  product is a primary source and is used.
- It prefers recent sources where the field moves and timeless
  sources where it does not; for a recent topic, what the search
  returns beats what the agent remembers.
- It records every source and every finding in the note's shape. A
  page it did not open is "not opened", whatever the search result
  said about it.
- It names conflicts: two sources that disagree are both cited,
  never one picked in silence. Agreement of copies is not agreement.
- It says what it did not find; "no reliable source on X" is a
  finding. It runs the disconfirming query of the card and reports
  what it found, including nothing.
- It spends its openings on primary sources, about ten to fifteen
  pages and never many more. It stops by the card's stop rule or
  when the openings are spent, and writes in the Search record which
  of the two ended the run.
- It never fabricates a source, a quote, a date or a figure. A quote
  is verbatim and short, with where in the page it stands. An
  identifier such as a DOI or an arXiv number is cited only from the
  page opened under it, never from memory.
- Nothing in the packet names a person, a company or a host of the
  principal's own, and nothing of the kind enters the note.

Claude writes each agent's return as a note with its header filled:
the engine, the model word, the usage and the run.

**The check before filing.** No note is filed unchecked. The check
has three steps, in this order.

1. Claude reads the note against the template's shape. A finding
   that rests on a snippet or a summarised fetch alone without
   saying so, a source cited for content but listed as not opened, a
   quote without its place, or an empty Search record sends the note
   back to its agent as a failed run; it is not filed.
2. The note is scanned for the instance's facts by
   `scripts/docs-check.py`, as every file that may be quoted is
   scanned.
3. Every citation is opened by `scripts/forge-cite.py`, which
   resolves every URL the note cites and reads an arXiv page for its
   title. A dead page or an identifier that names another paper is
   the mark of a fabricated citation. Such a note goes back to its
   agent once, with the report, as a failed run. A note that comes
   back still failing is filed as it is, and the synthesis names
   every finding that rests on a failed citation as without support.
   A page that refused or did not answer (a 403, a timeout) is
   unverifiable: it is said so and never counted as a failure.

The check writes nothing into the note. The note is the agent's
record.

**The synthesis.** When every note has returned, Claude writes the
synthesis into `00-plan.md`, from the notes alone, in this order:

- completeness card by card: answered, or not found and where it was
  looked; the stop rule met, or why searching ended; what the
  disconfirming query found, including nothing;
- the answers side by side, the engine named at each; agreement is
  reported as consistency, never as validation, and two notes citing
  the same copy count as one source;
- the Unexpected of every note, gathered and sorted by one test, a
  find that reconfigured a question or brought a mechanism from
  elsewhere against a find that adds a source to a point already
  made, and shown before any judgement;
- what was not found, gathered from every note;
- Claude's view, last and apart: what Claude makes of it, marked as
  its own, said in plain words to be verified or a hypothesis, and
  what it proposes to change in the chain, through `/forge <state>`,
  never silently.

The summary at the head of the plan file is written now and placed
first, so that a reader who stops there has the result. Every
difference between the plan as confirmed and the run as it went is
recorded under Deviations with its reason; "None" is a legitimate
entry. The status becomes `immutable`.

A second round is possible only for gaps the notes name. Claude
proposes it with the gaps listed and runs it on the principal's
word. There is no third round.

**The index and the report.** One entry for the bundle goes into
`research/00-INDEX.md`, written from the synthesis; the ledger, the
project's state file made at read time, reads the head of the bundle
and is remade by its script. The run folder under `tmp/` stays as it
is, for inspection; nothing in `tmp/` is a source of truth. Claude
reports to the principal leading with what the research says and
where the engines differ, not with a literature review. What the
research suggests for an artefact of the chain is proposed
explicitly, through `/forge <state>`, never slipped in.

## Why

**Why the plan comes before the search.** The quality of a research
is made by the decomposition into cards, not by the searching. The
plan is where the principal sees the questions before they cost
anything. The plan was chosen as the unit of consent, against the
finished note as it had been before, because that was the
principal's wish.

**Why a card is one question, one kind of evidence, one kind of
source.** The inputs give the rule and its two consequences, two
kinds of evidence making two cards and a card without a sentence
under "why it matters" being cut, and no reason beyond the rule
itself. The reason for the bound of about seven cards is likewise
not recorded beyond the rule that the bound is a kind rule and not a
count.

**Why the agent sees only the packet.** The agent sees nothing of
the conversation and nothing of the instance, and a note may be
quoted, so nothing of the principal's own may enter it. The brief is
owned by one definition and copied verbatim into every packet, so
that every agent works to the same rules. One packet for every
engine was chosen against a packet per engine, so that the answers
to one question compare.

**Why every citation is opened.** Agents invent and misnumber
sources, and nobody checks that by hand across cards and engines.
Resolving the URL is the one mitigation of a fabricated citation
with a measured effect. The check writes nothing into the note,
because the note is the agent's record.

**Why the agent opens few pages.** More calls have been measured to
lower the accuracy of citations, not to raise it; the openings are
spent on primary sources.

**Why the synthesis is Claude's, from the notes alone, with its view
last.** How sure a claim is, is said in words: whatever Claude
brings as knowledge says plainly whether it is verified and on what,
unverified, or a hypothesis, and a claim never gains certainty by
being written into an artefact. Words, not marks: no mark of
certainty is introduced. The rule is Claude's conduct, so it holds
in the synthesis as in every layer of the chain and in the
conversation. Keeping Claude's view last and apart keeps its
constructions from passing for the agents' findings.

**Why no recursive deep-dive to a fixed depth.** Depth comes from
the decomposition into cards and from one second round for gaps the
notes name; a third round was rejected.

**Why no fact verified by a count of agreeing sources.** Agreement
of copies is not agreement. A source is opened, dated and placed by
kind, conflicts are named, and a citation is verified by resolving
it. In the synthesis, agreement is consistency, never validation.

**Why no saturation as a percentage.** The stop rule is a kind rule:
a differently-worded query bringing nothing new and every
perspective of the card with a primary source, or the openings
spent, and which of them ended the run is written into the Search
record.

**Why a research is immutable from its filing.** The reason is not
recorded in the inputs of this page.

## A worked example

One card of a generic plan, in the shape the plan skeleton gives.
The topic and the project are invented; the card shows the shape
only.

```
#### Card 2: retention of internal meeting minutes
- **Question:** What retention period do published
  records-management guidelines recommend for the internal meeting
  minutes of a private company, against keeping them indefinitely?
- **Why it matters:** The archiving rule of the assignment rests on
  it; without it the rule is a guess.
- **What would answer it:** The clause of a published guideline or
  standard that names a period, found in a standards body's or a
  national archive's own publication.
- **Where to look:** National archives' guidance pages; the
  publications of records-management associations; the records
  standard already registered in `sources/`, which must turn up.
- **Disconfirming query:** "meeting minutes retain permanently
  guidance", written to find a recommendation to keep minutes
  indefinitely; expected: guidelines name a bounded period.
- **Stop rule:** Nothing new from a differently-worded query, and
  every perspective of the card has a primary source; about ten to
  fifteen openings.
```

The card asks one question, names one kind of evidence (a clause
naming a period) in one kind of source (a published guideline), has
a sentence under why it matters, and gives the agent a query written
to prove it wrong. Had the card also asked what the law requires, it
would be two cards, since a statute is another kind of evidence from
another kind of source.

## See also

- [Research a topic](../use/research-a-topic.md): running
  `/research`.
- [Another model family](another-model-family.md): the second
  engine, how it is reached and how its independence is measured.
- [Sources and research](sources-and-research.md): research as a
  resource of the project.
- [Research note and bundle](../reference/research-bundle.md): the
  shape of a note, a bundle and its plan.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
