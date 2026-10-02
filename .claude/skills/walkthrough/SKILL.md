---
description: The shape of a walkthrough and of an elicitation interview — one item per message, what an item carries, the verdict words, how verdicts reach the write. Not a command; read by the hook's pointer whenever a walkthrough or an interview runs.
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
are worked in order of weight. `park` is a legitimate verdict, not a
failure; a declined recommendation is not re-argued without new
facts.

## The verdict

Every item of a walkthrough ends in one proposition, worded so that
`accept` has exactly one meaning: yes to what is in front of the
principal. The proposition states what changes, or that nothing
changes, and what is recorded; where it goes against the reviewer's
suggestion, it says so. The message closes with the line
`(a)ccept / (m)odify / (r)eject / (p)ark`. An open question is not a
proposition: it closes with the question alone. Where Claude can, he
turns a question into a proposition, but never by filling a gap with
an assumption.

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted.
- `reject`: not agreed, nothing changes, the reason is recorded.
- `park`: not now. The item waits and comes back.
- `obsolete`: no longer relevant, with a note why.

The principal may answer the verdict line with a single letter, `a`,
`m`, `r` or `p`, when that letter is his whole message. After `m`
alone Claude asks what he wants changed. Claude's acknowledgement
names the verdict in full and says what it does. No other word of
the forge has a letter: `write`, `obsolete` and every command are
typed in full.

These are the verdict words of every walkthrough, whatever produced
the list; no command has words of its own.

## The elicitation interview

Runs the same way: one question per message, the answer acknowledged
before the next question is asked. When the principal sends a thought
in pieces (CLAUDE.md, Working methods, In pieces), no question until
his closing word.

## From verdicts to the write

Verdicts are carried in the conversation and written once at the
round's end (CLAUDE.md, prime directive 9). On `write` Claude
reflects the whole round back and, on the principal's yes, writes
everything carried as one round. `write` is added to the verdict
line when the round looks finished. What `accept` writes is the
producing command's (`/critique`, `/challenge`, `/check`; for a
source's proposals a position with provenance). The other verdicts
write the same wherever the list came from: `reject` a DEC with the
principal's reason, in the shape of `templates/decisions.md`, state
`rejected`, and the reviewer does not raise it again; `park` the
state `parked`; `obsolete` the state `obsolete`, with what made it
moot. States in the ledger change only, never delete. A source's
proposal that is rejected becomes a REJ in the intent. Until the
write, everything agreed is nowhere yet and
is said so (CLAUDE.md, prime directive 9).
