---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 19ba635e003d9b38
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list of items that needs your decision, such as findings, challenges or open threads: one item per message, each closed with a line you answer in a word. This page is for you, the principal (the person whose thinking is being forged), when Claude opens such a list.

## When to use it

A walkthrough starts by itself whenever a list needs your decision. A list can come from a critic's findings, a challenger's challenges, the differences between two sets of requirements, open threads, open questions or the proposals of a source. It can also come from a comparison you asked for. You do not start it by a command of its own: whatever produces a list ends by offering one.

## What you do

Answer each item with one letter, or with the word in full, when that is your whole message:

```
a
```

The words are `accept`, `modify`, `question`, `reject` and `park`, with the letters `a`, `m`, `q`, `r` and `p`. A further word, `obsolete`, is typed in full and has no letter. The exact words and letters are on [Verdict words](../reference/verdict-words.md).

## What happens

1. Claude puts the first item in front of you and stops. Items come in order of weight, the heaviest first.

   You should now see one item and nothing else: no table of verdicts, no list of questions.

2. The item says, in this order:
   - what it says and the situation or evidence behind it
   - what would change and for whom
   - Claude's recommendation with its reason and, for `accept`, the concrete text that would go in, not a description of the edit

   You should now see a proposition that states what changes (or that nothing changes) and what is recorded, followed by this line:

   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

3. You answer. What each verdict does:
   - `accept`: you agree, and the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution found is put forward to be accepted.
   - `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the same line. A question is never read as a modification or a yes.
   - `reject`: you do not agree. Nothing changes, and your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: the item is no longer relevant, with a note why.

   After `m` alone Claude asks what you want changed. After `q` alone it asks what you want to ask.

   You should now see one line that names your verdict in full and says what it does.

4. Claude carries the next item in the same message as that line, and only that. A question of yours keeps the item open until you close it.

   You should now see the next item, in the same shape.

5. Your verdicts are carried in the conversation and written once, at the round's end. When the round looks finished, Claude adds `write` to the line. You type `write` in full, and Claude reflects the whole round back to you first. On your yes it writes everything as one round.

   You should now see Claude name the file and section of each thing written.

Until that write, everything agreed is nowhere yet, and Claude says so.

## What you have afterwards

The write puts into the files what each verdict means:

- `accept` writes what the command that produced the list says, which is the fix, and a closing record.
- `reject` writes a decision with your reason and a verdict line saying the item was rejected. The reviewer does not raise a rejected item again.
- `park` writes a decision with a verdict line saying the item is parked until the thing you named.
- `obsolete` writes a decision with a verdict line saying the item is obsolete and what made it moot.

A state is never changed by deleting a record. It changes by a newer one. After the write the ledger, the single record of state, is made afresh from the documents.

## The same line outside a list

The elicitation interview, where Claude draws out by questions what you have not yet put into words, runs the same way: one question per message, and your answer acknowledged before the next question. When you send one thought in several pieces, Claude asks nothing until your closing word.

The same line closes every question of Claude's that asks you to decide, inside a walkthrough or outside it. Examples are a step that needs your consent, a choice between options, an either/or and whether to write. Each is one proposition, and Claude's recommendation is what `accept` means. A message that says yes and asks a question is `question`, never consent. Only a question for information Claude lacks ends with the question alone.

## A worked example

Claude has a list of three findings from a review. It opens the first:

```
Finding 1 of 3 (heaviest). The introduction promises a success
criterion, and the body has none. Readers of the assignment would
not know when the work is done.

What changes: the assignment gains one criterion, for the team that
receives it.

I recommend accepting. The text that would go in:

  SCR.0010 The report shall be accepted when every section has an
  owner named.

Accepting adds this line and records the finding as closed.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer `q`, and then ask whether the criterion fits a delegated task. Claude answers and closes the item again with the same line. Nothing has been written. You answer `a`. Claude says it has accepted finding 1 and will write it at the round's end, then opens finding 2 and stops. After finding 3 the line also offers `write`. You type `write`, Claude reflects the round back, and on your yes it writes all of it at once.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
