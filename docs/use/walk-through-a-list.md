---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: b4e46cc4b5ed3d07
inputs:
  - .claude/skills/walkthrough/SKILL.md
---

# Walk through a list

A walkthrough is the way Claude works any list that needs your decision: one item per message, each closed with a proposition you answer in a word. This page is for you, the principal (the person whose thinking is being forged and who has the final word on content), when Claude puts such a list in front of you.

## When to use it

A walkthrough runs whenever a list of items needs your decision, whatever produced the list. These are the usual lists:

- the findings of a critique
- the challenges of a peer review
- the differences between two requirement sets
- open threads
- items still to be confirmed
- the proposals drawn from a source

An elicitation interview, where Claude draws out by questions what you have not yet put into words, runs the same way. You do not start a walkthrough with a command. Claude begins one as soon as such a list exists.

## What you do

You answer each item with one verdict, and you do it for every item in turn. The verdict line closes every proposition:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

Answer with the full word, or with its single letter when that letter is your whole message: `a`, `m`, `q`, `r` or `p`. No other word has a letter. `write` and `obsolete` are typed in full. The exact words and letters are listed in [Verdict words](../reference/verdict-words.md).

## What happens

1. Claude puts one item in front of you and stops.

   The item says, in this order:
   - what it states and the situation or evidence behind it, in a few sentences
   - what would change and for whom
   - Claude's recommendation with its reason, and for `accept` the concrete text the document would receive

   The item ends in one proposition. It states what changes, or that nothing changes, and what is recorded. Where it goes against the reviewer's suggestion, it says so.

   You should now see one item, one proposition and the verdict line, and nothing after it.

2. You give your verdict.

   - `accept`: you agree, and the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution you reach together is put forward for you to accept.
   - `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. A question is never read as a modification or a yes.
   - `reject`: you do not agree, nothing changes, and your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: the item is no longer relevant, and you give a note why.

   After `m` alone, Claude asks what you want changed. After `q` alone, it asks what you want to ask.

   You should now see Claude's acknowledgement, which names your verdict in full and says what it does.

3. Claude opens its next message with one line acknowledging the verdict, then carries the next item and nothing else.

   Items come in order of weight. A question from you keeps the open item open until you close it. Claude never gives a verdict of its own on the open item and puts the next item in the same message. It never puts a table that asks for every verdict at once, or a questionnaire of several questions, in front of you.

   You should now see the next item, closed with the verdict line.

4. When the round looks finished, Claude adds `write` to the verdict line. You answer `write`.

   Verdicts are carried in the conversation and written once, at the round's end. Until then everything agreed is nowhere yet, and Claude says so.

   You should now see Claude reflecting the whole round back to you. Say yes, and it writes everything as one round.

An elicitation interview follows steps 1 to 3 with questions in place of items: one question per message, your answer acknowledged before the next question is asked. When you send a thought in several pieces and close it with a word such as "done", Claude asks no question until that word.

## What you have afterwards

The write records each verdict in the same way wherever the list came from.

- `accept` writes what the producing command says. A critique, a challenge and a check each file their own result. For the proposals of a source, it writes a position with its provenance.
- `reject` writes a decision record with your reason, in the shape the decisions file uses, and the state `rejected`. The reviewer does not raise the item again. A rejected proposal of a source becomes a rejected direction in the intent.
- `park` writes the state `parked`.
- `obsolete` writes the state `obsolete`, with what made the item moot.

States in the ledger (the single file that holds the state of a project) change only. Nothing is deleted.

## A worked example

Claude has a list of findings from a critique of a project's assignment. It puts the heaviest one in front of you.

```
Finding 1 of 4. Two requirements of the group on reporting give
different deadlines for the same monthly report: the first says
the fifth working day, the second the tenth.

The recipients could not tell which date binds them. The second
requirement would be removed and the first kept.

I recommend keeping the fifth working day: the first requirement
names an owner, and the second does not.

Proposed text: remove the second requirement and add "the owner
named in the first requirement" to the first.

Accept means: the second requirement is removed and the finding is
recorded as resolved.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer `q` and then ask whether the tenth day comes from a source. Claude answers from the documents and closes the item again with the same verdict line. Nothing has changed. You answer `a`.

Claude's next message opens with one line, "Accepted: the second requirement is removed", and carries finding 2. After the fourth finding, the verdict line carries `write` as well. You answer `write`, Claude reflects the four verdicts back, you say yes, and one round is written.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
