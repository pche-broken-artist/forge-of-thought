---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Walk through a list

This page is for the person who has to decide on a list: findings of
a review, challenges, differences between two sets of requirements,
open threads, open questions, the proposals of a source. It says how
the forge works through such a list with you, what each item shows,
and how your answers reach the files.

The same way of working applies to every list, whatever produced
it. No command has verdict words of its own.

## What happens

Items are put in front of you one per message, in order of weight,
heaviest first. Each message carries one item and stops. You give a
verdict; the next message opens with one line acknowledging it and
then carries the next item, nothing else.

You are never shown a table asking for every verdict at once, and
never a questionnaire of several questions.

If you ask a question about an item, the item stays open until you
close it. Claude does not give a verdict of his own on the open item
and move on in the same message. A check whether Claude has
understood an item fully is an item of its own.

## What an item shows

In this order, so that you can decide without asking for an
explanation:

1. What the item says, and the situation or evidence behind it, in a
   few sentences.
2. What would change, and for whom.
3. The recommendation with its reason. For accept, it includes the
   concrete text the document would receive, not a description of
   the edit.

A heading with a one-sentence reason is a label, not an item. A
recommendation you decline is not argued again unless there are new
facts.

## How you answer

Every item ends in one proposition, worded so that accept has exactly
one meaning: yes to what is in front of you. The proposition says
what changes, or that nothing changes, and what is recorded. Where it
goes against what the reviewer suggested, it says so. The message
closes with this line:

```
(a)ccept / (m)odify / (r)eject / (p)ark
```

You answer with the word or with its single letter (`a`, `m`, `r`,
`p`), when that letter is your whole message. After `m` alone you are
asked what you want changed. Claude's acknowledgement names the
verdict in full and says what it does. No other word of the forge has
a letter: `write`, `obsolete` and every command are typed in full.

| Verdict | Meaning |
|---|---|
| accept | Agreed; the text goes in as shown. |
| modify | A discussion opens on the item, and the solution found is put forward to be accepted. |
| reject | Not agreed; nothing changes; your reason is recorded. |
| park | Not now; the item waits and comes back. |
| obsolete | No longer relevant, with a note why. |

Park is a legitimate answer, not a failure. Obsolete is a fifth
verdict, typed in full. The exact words are on the page
[Verdict words](../reference/verdict-words.md).

An open question is not a proposition. When Claude has a question
rather than a proposal, the message closes with the question alone.
Where he can, he turns a question into a proposition, but never by
filling a gap with an assumption.

## How the verdicts reach the files

Your verdicts are carried in the conversation and written once, at
the end of the round. Until then everything agreed is nowhere yet,
and Claude says so.

1. When the round looks finished, `write` is added to the verdict
   line. You can also type `write` yourself.
2. Claude reflects the whole round back to you first.
3. On your yes, he writes everything carried as one round, with one
   version bump for the whole round.

What each verdict records:

- accept writes what the producing command says. For critique
  findings, challenges and checks that is the command's own; for the
  proposals of a source it is a position with its provenance.
- reject records a decision with your reason, and the item's state
  becomes `rejected`. The reviewer does not raise it again.
- park sets the state `parked`.
- obsolete sets the state `obsolete`, with what made the item moot.

States in the ledger change only; nothing is deleted. A rejected
proposal from a source becomes a rejected direction in the intent.

## The elicitation interview

When Claude draws out what you have not yet put into words, it runs
the same way: one question per message, and your answer acknowledged
before the next question is asked. If you send one thought in several
pieces, no question comes until you close it with your word, such as
"done".

## See also

- [Verdict words](../reference/verdict-words.md): the words and
  letters, exactly.
- [About the working methods](../about/working-methods.md): why the
  one-item rule exists and how a hook holds it.
