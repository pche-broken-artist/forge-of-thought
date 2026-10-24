---
project: forge
title: Research — a plan before the search, two model families on it
author: PCHe
version: 0.3
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What I want

When I give `/research` a topic, I want to see the research plan
before anything is searched: how the topic breaks into simpler
questions, how many agents go out and on what. I comment, we agree
the plan, and only then is it sent. The quality of a research is
made by that decomposition; the web searching itself is simple.
Today I get a finished note and never see the split.

I want the same plan run on two model families, Gemini beside
Claude, both doing the full work on every question; Claude then
lays the answers side by side, evaluates and synthesises. Before I
confirm the plan, the second model reads the draft and says what it
misses. One model alone is narrower than the web it searches.

What I want to be able to trust: that a research finds relevant and
up-to-date material, that it goes deep and does not slide over the
surface, that it is not filled with junk, and that it does not
overlook interesting things. Maximum quality; speed and token
economy come after.

## Why now

The four research notes of 2026-10-24 (`research/2026-10-24-*.md`)
say the measured losses of research systems are missed context,
shallow coverage, anchoring on early evidence and broken citations,
never the searching; a plan buys the one thing I asked for, seeing
the questions before they cost anything. The same topic developed
with Gemini in conversation
(`sources/gemini-research-protocol-proposal.md`) arrived at the
same picture from the other side.

## What I take, what I do not

From Gemini's proposal I take the multi-engine run, perspectives as
the axis of the split, a counter-question to every expectation, a
marked place for the unexpected, and a definition of done. I do not
take: a split of roles between the engines (one searches, the other
reasons), because two halves cannot be compared; recursive
deep-diving to a fixed depth; facts "verified" by a count of
agreeing sources; saturation as a percentage; skills on Gemini's
side that would duplicate the forge's own definition. And not
overengineering: a first version we can run next week, tuned on
real researches.

## How I want it built, lightly

One plan, agreed in a walkthrough, the second engine's additions
shown beside Claude's draft. One isolated agent per question per
engine, seeing the question and its brief, nothing of the
conversation. A research lands as one bundle in `research/` with
the plan and the synthesis at its head. The second engine is
reached by a script of the forge over its CLI, given a packet
composed from the forge's own definition in a run folder under
`tmp/`, never the forge as its workspace; `tmp/` becomes a proper
working folder of the engine, in git with its own README and ignore
file, runs kept for inspection. Every URL of
every note is opened by a script before the note is filed: the first
trial showed one engine inventing or misnumbering three of fourteen
sources, and nobody checks that by hand across cards and engines.
The result opens with a summary, the bundle with what the research
says and where the engines differ, each note with its answer in a
few sentences, in the words I would be told it in. Try it, tune it,
and only then write it into the intent, the design and whatever else
it touches. I say which depth I want: `/research --quick` for one
question answered by one engine and filed as one note,
`/research --deep` for the plan on two engines with a synthesis;
without the word, Claude proposes the depth in the plan and I
decide.

## Later, not in the first version

Divergent probes as agents of their own (an adjacent field, named
dissent, what is new or contested); a quote checked against its
page; a pass over what the agents opened and did not use; the
consultation command and the spool (THR.0740).

## Open

Where this lands when mined: POS.0050, POS.0800, THR.0290 (the
second way of researching has arrived).
