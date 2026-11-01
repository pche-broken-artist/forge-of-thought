---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 6eb9f70a0ac82b2e
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

This page shows how Claude works a list of items that need your
decision, one item at a time, and how you answer. It is for you as the
principal (the person whose thinking is being forged). A list may be
findings of a critic, challenges, open threads, open questions or the
proposals of a source. The method is called a walkthrough. Terms of the
forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

You do not start a walkthrough with a command. It begins whenever Claude
has a list of items that need your decision, whatever produced the list.
Every command that produces such a list ends by offering one. You can
also ask for one in a word.

The elicitation interview, in which Claude draws out by questions what
you have not yet put into words, runs the same way.

## What you do

You answer each item with a verdict. Type a single letter or the word
in full:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

A letter works only when it is your whole message. `obsolete` is a
further verdict and is typed in full. `write` is also typed in full.

## What happens

1. Claude puts one item in front of you and stops. Items come in order
   of weight. It never puts a table asking for every verdict at once, or
   a questionnaire of several questions, in front of you.

   You should now see one item and the verdict line at its end.

2. The item carries, in this order:
   - what the item says, and the situation or evidence behind it, in a
     few sentences;
   - what would change and for whom;
   - Claude's recommendation with its reason and, for `accept`, the
     concrete text the document would receive, not a description of the
     edit.

   The item closes with one proposition worded so that `accept` has
   exactly one meaning: yes to what is in front of you. The proposition
   says what changes, or that nothing changes, and what is recorded.
   Where it goes against a reviewer's suggestion, it says so.

   You should now see the proposition and the verdict line.

3. You give your verdict.
   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item. The solution you find
     together is put forward to be accepted.
   - `question`: you ask about the open item. Nothing changes and
     nothing is written. Claude answers and closes the item again with
     the verdict line. A question is never read as a modification or a
     yes.
   - `reject`: not agreed, nothing changes, your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why.

   After `m` alone Claude asks what you want changed. After `q` alone it
   asks what you want to ask. A declined recommendation is not argued
   again unless there are new facts.

   You should now see one line that names your verdict in full and says
   what it does.

4. The next message carries the next item and nothing else. While you
   have an open question, Claude does not move on until you close the
   item.

   You should now see the next item.

5. When the round looks finished, Claude adds `write` to the verdict
   line. You type `write`. Claude reflects the whole round back to you
   first, and on your yes it writes everything carried as one round.

   You should now see the round reflected back, and after your yes the
   named files and sections that were written.

The same line closes every other question of Claude's that asks you to
decide, inside a walkthrough or outside it. Examples are a step that
needs your consent, a choice between options, an either/or and whether
to write. Each is one proposition, with Claude's recommendation as what
`accept` means. A message of yours that says yes and carries a question
is read as `question`, never as consent. Only a question for
information Claude lacks ends with the question alone.

## What you have afterwards

Until the write, everything agreed lives in the conversation only. Claude
says so, and never says nothing is lost while something exists only
there.

After the write:

- `accept` has written what the command that produced the list says (a
  fix to the document) and a closing record that the item is closed.
- `reject` has written a decision with your reason and the verdict line
  "rejected". The reviewer does not raise the item again.
- `park` has written a decision with your reason and the verdict line
  "parked until" what the item waits for.
- `obsolete` has written a decision with the verdict line "obsolete" and
  what made the item moot.
- A source's proposal that you reject becomes a rejected direction in
  the intent.

A state is never changed by deleting a record, only by a newer one. The
ledger (the table of the project's state, made at read time from the
documents) is made afresh after the write.

## If something goes wrong

The source gives no stop conditions and no messages for this method. If
a message of Claude's carries several items, or a table of verdicts,
that is not the method: ask for one item. The method is not enforced
by a stop, so it is held by what you accept.

## A worked example

A critic has returned a finding that a section of a document repeats
itself. Claude puts the first item in front of you.

```
The "Scope" section states the same limit twice, once in the
opening paragraph and once in its second item. A reader meets the
limit before the list and again inside it.

Cutting the opening sentence changes only that section and
affects no other document.

I recommend cutting the sentence from the opening paragraph, so
that the limit stands once, in the list. The paragraph would
then read:

  "This document covers the order process for new customers."

Accept means: the sentence is cut as shown and the finding is
closed.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You are not sure whether another document cites the sentence, so you
answer `q` and then ask. Claude answers, changes nothing, and closes the
item again with the same line. You answer `a`. Claude replies with one
line that says it takes this as `accept` and that the cut waits for the
write, and carries the next item. At the end Claude offers `write`; you
type it, read the round reflected back, say yes, and the cut and the
closing record are written once.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
