---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: d25aa898a805ecb9
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list of items that needs your decision, such as a reviewer's findings, challenges, open threads or the proposals of a source. This page is for you, the principal (the person whose thinking is forged), when such a list is put in front of you and you want to know what each message carries and how to answer it.

## When to use it

You do not start a walkthrough. It runs whenever a list needs your decision, whatever produced the list. Every command that produces a list ends by offering one. A conflict met by a save is laid out the same way, one conflict per message (see [Settle a conflict](settle-a-conflict.md)). The elicitation interview, where Claude draws out by questions what you have not yet articulated, runs the same way.

## What you do

You answer each item with a verdict. The closing line of every item is this one, and you can type it as it stands or answer it with a single letter:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

The letter must be your whole message. The word works too. The words and letters are listed exactly in [Verdict words](../reference/verdict-words.md).

## What happens

1. Claude puts one item in front of you and stops. Items come in order of weight.

   You should now see one item, never a table asking for every verdict at once and never a questionnaire.

2. The item carries, in this order: what it says and the situation behind it; what would change and for whom; Claude's recommendation with its reason and, for `accept`, the concrete text the document would receive.

   You should now see a proposition worded so that `accept` has exactly one meaning: yes to what is in front of you. It says what changes, or that nothing changes, and what is recorded.

3. You give a verdict.

   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution found is put forward to be accepted. After `m` alone Claude asks what you want changed.
   - `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. After `q` alone Claude asks what you want to ask.
   - `reject`: not agreed, nothing changes, your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why. It is the one verdict without a letter, so you type it in full.

   You should now see one line acknowledging your verdict by its full name and saying what it does, then the next item and nothing else.

4. The verdicts are carried in the conversation. Nothing is written yet. Until the write, everything agreed lives only in the conversation, and Claude says so.

   You should now see the list shrink item by item, with no file touched.

5. When the round looks finished, Claude adds `write` to the verdict line. You type `write` in full. Claude reflects the whole round back to you and, on your yes, writes everything carried as one round.

   You should now see the reflection first, then the write, and the ledger made afresh after it. (The ledger is the state of the project, made from its documents at read time.)

## What each verdict writes

- `accept` writes what the command that produced the list says (the fix) and a closing record of the item.
- `reject` writes a decision with your reason and its verdict line. The reviewer does not raise a rejected item again.
- `park` writes a decision with your reason and the verdict line saying what the item waits for.
- `obsolete` writes a decision with your reason and the verdict line saying it is obsolete, with what made it moot.

A state is never undone by deleting a record. It changes by a newer one.

## Questions that are not on a list

The same line closes every question of Claude's that asks you to decide, in a walkthrough or outside it. That covers a step that needs your consent, a choice between options, an either/or and the question whether to write. Such a question is one proposition, with Claude's recommendation as what `accept` means.

A yes that carries a question is `question`, never consent. Claude answers, then asks again.

Only a question for information Claude lacks ends with the question alone.

The elicitation interview follows the one-item rule in its own way: one question per message, and the answer acknowledged before the next question. When you send a thought in several pieces, Claude asks nothing until your closing word.

## If something goes wrong

- If a message of Claude's holds more than one item, or asks for every verdict at once, it has left the method. Ask for one item at a time.
- If you answer with a remark or a counter-thought where Claude asked for a verdict, it is read as `question`, never as a yes or a change.
- If an item is not worded so that `accept` has one meaning, answer `question` and ask what it would change.

For why the one-item rule exists and how it is held, see [The working methods](../about/working-methods.md). For the terms used here, see the [Glossary](../reference/glossary.md).

## A worked example

Claude has run a review and offers a walkthrough. The first item arrives.

```
Item 1 of 3, the heading "Scope of the chapter on setup":
the chapter says "the tool is installed once" but two later
paragraphs describe installing it per project.

Changing it affects the setup chapter and whoever follows it.

I recommend the first wording, because the later paragraphs are
the ones readers act on. The paragraph would read: "The tool is
installed once per project."

Accept means: the sentence is replaced as shown and the item is
recorded as closed.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You type `q` and then ask whether the second paragraph is also affected. Claude answers, changes nothing, and closes the item again with the same line. You type `a`. Claude replies with one line, "Accept: the sentence goes in as shown, written at the round's end", and carries item 2. After item 3, Claude adds `write` to the line, you type `write`, Claude reflects the round back, and you confirm. The fix and the records are written, and the ledger is made afresh.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
