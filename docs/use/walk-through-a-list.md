---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 07e2d8208e5f15b5
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list of items that needs the
decision of the principal (the person whose thinking is being forged),
one item at a time. This page is for you as the principal: it shows
what you see, what you answer and what is written when the round ends.
Findings of a review, challenges, open threads and proposals from a
source are all worked this way. The ledger (the state of the project,
made afresh from its documents whenever it is read) is remade after
the write.

## When to use it

You do not start a walkthrough with a command of its own. It runs
whenever a list of items waits for your decision. A review, a
challenge or a comparison on request ends by offering one. An
elicitation interview, where Claude draws out by questions what you
have not yet put into words, runs the same way.

## What you do

You answer each item with a verdict, one letter or the word in full:

```
a
```

The words and letters are listed exactly on
[Verdict words](../reference/verdict-words.md).

## What happens

1. Claude puts one item in front of you and stops. Items come in
   order of weight, the heaviest first.

   You should now see one item only, never a table asking for every
   verdict at once.

2. The item says, in this order, what it is and the evidence behind
   it, what would change and for whom, and Claude's recommendation
   with its reason. For `accept` the recommendation carries the
   concrete text that would be written, not a description of the
   edit.

   You should now see enough to decide without asking for an
   explanation.

3. The item closes with one proposition, worded so that `accept`
   means a plain yes to what stands in front of you, and then with
   this line:

   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

   You should now see that line at the end of the message.

4. You answer with a verdict:

   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution
     found is put forward to be accepted.
   - `question`: you ask about the open item. Nothing changes and
     nothing is written. Claude answers and closes the item again
     with the verdict line. A question is never read as a
     modification or a yes.
   - `reject`: not agreed, nothing changes, your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why.

   You may answer with a single letter (`a`, `m`, `q`, `r` or `p`)
   when that letter is your whole message. After `m` alone Claude
   asks what you want changed. After `q` alone it asks what you want
   to ask. `obsolete` and `write` are typed in full, because they
   have no letter.

   You should now see one line that names your verdict in full and
   says what it does.

5. The next message carries the next item and nothing else. While you
   have an open question, the item stays open: Claude never gives its
   own verdict on the open item and the next item in one message.

   You should now see the next item, or the end of the list.

6. When the round looks finished, `write` is added to the verdict
   line. You answer `write`. Claude reflects the whole round back to
   you first, and on your yes it writes everything carried, as one
   round.

   You should now see the named files and sections that were written.

The elicitation interview runs the same way: one question per
message, your answer acknowledged before the next question. When you
send one thought in several pieces, Claude asks no question until your
closing word.

## Every decision of Claude's closes the same way

The same line closes every question of Claude's that asks you to
decide, inside a walkthrough or outside it. That includes a step that
needs your consent, a choice between options, an either/or and the
question whether to write. Each is one proposition with Claude's
recommendation as what `accept` means.

A message that says yes and also asks a question is read as
`question`, never as consent. Only a question for information Claude
lacks ends with the question alone, without the line.

## What you have afterwards

Until `write`, everything agreed is carried in the conversation only,
and Claude says that it is nowhere yet. After `write`:

- `accept` writes what the command that produced the list says (the
  fix), together with a closing record.
- `reject` writes a decision with your reason and its verdict line.
  A rejected item is not raised again.
- `park` writes a decision with your reason and what the item waits
  for.
- `obsolete` writes a decision with what made the item moot.

A state is changed by a newer record, never by deleting one. The
ledger is made afresh after the write.

## If something goes wrong

- If you ask a question while answering, the answer is `question`:
  nothing is changed, and Claude closes the item again.
- If you send `m` or `q` alone, Claude asks what to change or what
  to ask before it goes on.
- If an item has been written nowhere yet, Claude says so; nothing
  is lost silently, and you may order a write of whatever is agreed
  so far at any moment.

## A worked example

Claude has a list of review findings. It opens with the heaviest:

> Finding 1 of 3. The chapter on installation tells the reader to
> run the setup before it says what the setup needs. A reader who
> follows it in order stops at the second step. Moving the sentence
> on the requirements above the first step changes the chapter only;
> nobody else is affected. I recommend it, because the order of the
> steps then matches the order of the work. The text would read:
> "Before you start, you need X and Y."
>
> Proposition: move the sentence on the requirements above the first
> step, and record the finding as closed.
>
> (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark

You answer:

```
q
```

Claude asks what you want to ask. You ask whether Y is really needed.
Claude answers and closes the item again with the same line. Nothing
has changed. You answer:

```
a
```

Claude acknowledges in one line that finding 1 is accepted and will
be written at the round's end, and then puts finding 2 in front of
you. After finding 3 it offers `write`. You answer `write`, Claude
reflects the round back, you say yes, and the files are written.

## See also

- [Verdict words](../reference/verdict-words.md): the words and
  letters, exactly.
- [The working methods](../about/working-methods.md): why the
  one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save,
  laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
