---
description: The shape of a walkthrough and of an elicitation interview — one item per message, what an item carries, how verdicts reach the write. Not a command; read by the hook's pointer whenever a walkthrough or an interview runs.
user-invocable: false
---

The working method named in CLAUDE.md (Working methods, Walkthrough;
its position POS.0850 in `projects/forge/10-intent.md`). It applies
whenever a list of items needs the principal's decision — critique
findings, challenges, differences between two requirement sets, open
threads, TBC items, proposals of a source — and to every elicitation
interview, whatever produced the list.

## One item per message

Claude puts one item in front of the principal and stops. The
principal gives his verdict. The next message opens with one line
acknowledging that verdict and then carries the next item, nothing
else. Never a verdict of Claude's own on the open item and the next
item in one message: a question from the principal keeps the item
open until he closes it. A check whether Claude has understood an
item fully is an item of its own. A table asking for every verdict at
once, or a questionnaire of several questions, is never put in front
of the principal.

## What an item carries

In this order, so that the principal can decide without asking for
an explanation:
1. what the item says and the situation or evidence behind it, in a
   few sentences;
2. what would change and for whom;
3. the recommendation with its reason and, for "accept", the concrete
   text the artefact would receive — never a description of the
   edit.

A heading with a one-sentence reason is a label, not an item. Items
are worked in order of weight. "Leave it open" is a legitimate
verdict, not a failure; a declined recommendation is not re-argued
without new facts.

## The elicitation interview

Runs the same way: one question per message, the answer acknowledged
before the next question is asked. When the principal sends a thought
in pieces (CLAUDE.md, Working methods, In pieces), no question until
his closing word.

## From verdicts to the write

Verdicts are carried in the conversation and written once at the
round's end (CLAUDE.md, prime directive 9), on the principal's
confirmation or at any moment on his order. The verdict vocabulary,
and what each verdict writes, is the producing command's
(`/critique`, `/challenge`, `/check`; for a source's proposals: a
position with provenance for "accept", a REJ for "reject"). Before
the write Claude reflects the whole round back. Until the write,
everything agreed is nowhere yet and is said so.
