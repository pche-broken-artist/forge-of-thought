---
generated: 2026-10-10
made: mirrored
inputs-hash: c60b38b55b9dda8b
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Walk through a list

This page is for the person who works a list of items with Claude:
critique findings, challenges, differences between two requirement
sets, open threads, open questions, proposals from a source. It says
how the conversation runs, what each item shows you and how your
answers reach the files.

## What a walkthrough is

Whatever produces a list that needs your decision, the list is worked
the same way, and Claude offers a walkthrough at the end of the
command that made it. You see one item per message, in order of
weight. You answer it, and only then does the next item come.

Claude never puts a table asking for every verdict at once in front
of you, and never a questionnaire of several questions. A check
whether Claude has understood an item is an item of its own.

## What an item shows you

Each item carries, in this order:

1. What the item says and the situation or evidence behind it, in a
   few sentences.
2. What would change and for whom.
3. The recommendation with its reason. For accept, it gives the
   concrete text the document would receive, not a description of the
   edit.

A heading with a one-sentence reason is a label, not an item.

## How you answer

Every item ends in one proposition: it states what changes, or that
nothing changes, and what is recorded. Where it goes against what the
reviewer suggested, it says so. Accept always means yes to exactly
what is in front of you. The message closes with this line:

`(a)ccept / (m)odify / (r)eject / (p)ark`

- accept: agreed, the text goes in as shown.
- modify: a discussion opens on the item, and the solution found is
  put forward for you to accept. If you answer `m` alone, Claude asks
  what you want changed.
- reject: not agreed, nothing changes, your reason is recorded.
- park: not now. The item waits and comes back.
- obsolete: no longer relevant, with a note why. It is a fifth
  verdict, not on the closing line.

You may answer with a single letter, `a`, `m`, `r` or `p`, when that
letter is your whole message, or with the word. No other word of the
forge has a letter: `write`, `obsolete` and every command are typed in
full.

Claude's next message opens with one line naming your verdict in full
and saying what it does, then carries the next item and nothing else.

A question from you keeps the item open until you close it. An open
question is not a proposition, so such a message closes with the
question alone. Declining a recommendation is respected: Claude does
not argue it again without new facts.

## How the verdicts are written

Nothing is written item by item. Your verdicts are carried in the
conversation and written once, at the end of the round. When the round
looks finished, `write` is added to the verdict line. When you say
`write`, Claude reflects the whole round back to you first and, on
your yes, writes everything as one round. Until then, what you have
agreed is nowhere yet, and Claude says so.

What each verdict records:

- accept writes what the command that produced the list says (for a
  critique, a challenge or a check, that command's own way; for a
  source's proposals, a position with its provenance).
- reject records a decision with your reason, in the state `rejected`,
  and the reviewer does not raise the item again. A source's proposal
  that you reject becomes a rejected direction in the intent.
- park sets the state `parked`.
- obsolete sets the state `obsolete`, with what made the item moot.

States in the ledger change only, never delete.

## The interview runs the same way

The elicitation interview, where Claude draws out what you have not
yet put into words, follows the same rhythm: one question per message,
and your answer acknowledged before the next question. If you send one
thought in several pieces, Claude asks nothing until your closing
word.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [About the working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
