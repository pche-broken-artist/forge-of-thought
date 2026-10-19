---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 83985f66487d946d
inputs:
  - .claude/skills/walkthrough/SKILL.md
---

# Walk through a list

This page shows how a list that needs your decision is worked, one item at a time, and how your verdicts reach the files. It is for the principal (the person whose thinking is forged and who decides), and it applies to any list: findings of a critic, challenges, open threads, open questions, proposals from a source.

A walkthrough is the name of this way of working. Claude is the assistant that runs it. The ledger is the file that holds the state of a project; it is made afresh after the write.

## When to use it

Use it whenever a command ends with a list of items for you to decide, or whenever you ask Claude to go through such a list. Claude offers it at the end of every command that produces a list. The same way of working runs the elicitation interview, in which Claude draws out by questions what you have not yet put into words.

## What you do

You answer each item with one letter, or the word in full. The line you answer is shown at the end of every item:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

When the letter is your whole message, it is read as the verdict. The exact words and letters are in [Verdict words](../reference/verdict-words.md).

`obsolete` is a further verdict. It is typed in full, as is `write`, because no other word of the forge has a letter.

## What happens

1. Claude puts one item in front of you and stops.
   You should now see a single item, never a table of items or a questionnaire.
2. You read the item. It carries, in this order, what it says with the situation behind it, what would change and for whom, and Claude's recommendation with its reason. For `accept`, the recommendation includes the concrete text that would be written, not a description of the edit.
   You should now see everything you need to decide without asking for an explanation.
3. The item closes with one proposition, worded so that `accept` means yes to exactly what is in front of you. It says what changes, or that nothing changes, and what is recorded.
   You should now see the verdict line below the proposition.
4. You give your verdict.
   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution found is put forward to be accepted. Alone, `m` makes Claude ask what you want changed.
   - `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. A question is never read as a modification or a yes. Alone, `q` makes Claude ask what you want to ask.
   - `reject`: not agreed, nothing changes, and your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why.

   You should now see Claude's acknowledgement, which names the verdict in full and says what it does.
5. The next message opens with that one line of acknowledgement and then carries the next item. Items are worked in order of weight.
   You should now see exactly one new item.
6. When the round looks finished, Claude adds `write` to the verdict line. Until you say `write`, everything agreed is carried in the conversation only. It is written nowhere yet, and Claude says so.
7. On `write`, Claude reflects the whole round back to you. On your yes, it writes everything carried as one round.
   You should now see a statement of which files were written.

## What you have afterwards

The verdicts are written once, at the end of the round. Each kind of verdict leaves this behind:

- `accept`: what the command that produced the list says is written (for a critic, the fix), together with a closing record of the item.
- `reject`: a decision with your reason and its verdict line. The item is not raised again.
- `park`: a decision with your reason and its verdict line, saying until what the item waits.
- `obsolete`: a decision with your reason and its verdict line, saying what made the item moot.

A state is never changed by deleting a record. It changes by a newer record. After the write, the ledger is made afresh from the records, so it shows the new state.

A proposal from a source that you reject is also kept as a rejected direction in the intent, so that it is not proposed again.

## If something goes wrong

- You are unsure about an item. Answer `question`. The item stays open until you close it with another verdict.
- Claude puts two items in one message, or asks for every verdict at once. That is not the method. Say so, and it returns to one item per message.
- You sent a long thought in pieces. Claude acknowledges each piece in a line and asks nothing until your closing word.

Why the rule of one item exists and how it is held in a long conversation is explained in [The working methods](../about/working-methods.md).

## A worked example

Claude has finished a critic run and offers a walkthrough. The first item arrives like this (the slug, the section and the wording are placeholders):

> The assignment of project `example` says in one section that delivery is monthly and in another that it is quarterly. The reader cannot tell which holds. Fixing it changes one sentence for the recipients and nothing else.
>
> Recommendation: keep the quarterly rhythm, because the second section is the one the success criteria rest on. The sentence would read: "Delivery is quarterly."
>
> Accept: the sentence goes in as shown and the item is closed in a record.
>
> `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

You ask: `q`. Claude asks what you want to ask. You write "Does the monthly figure appear anywhere else?" Claude answers, changes nothing, and closes the item again with the same verdict line. You answer `a`.

Claude acknowledges in one line, "Accepted: the sentence goes in as shown, written at the round's end", and carries the second item. After the last item you say `write`. Claude reflects the round back, you say yes, and the fixes and records are written in one round. The ledger is then made afresh.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
