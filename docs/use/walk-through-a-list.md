---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: eb35bf7aedf598b6
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list that needs your decision, one item at a time, so that you decide each item on its own. This page is for you, the principal (the person whose thinking is forged and who has the final word on content), whenever Claude puts a list of findings, challenges, threads or open questions in front of you.

## When to use it

A walkthrough runs whenever a list of items needs your decision, whatever produced the list: a critique, a challenge, a check, a comparison of two requirement sets, open threads, open questions or the proposals of a source. It also runs for an elicitation interview. You do not start it with a command. Claude ends whatever produces a list by offering it, and you may ask for it in a word.

## What you do

You answer each item with one verdict. The shortest answer is a single letter as your whole message:

```
a
```

## What happens

1. Claude puts the first item in front of you and stops. Items come in order of weight, and the next one does not appear before you have given your verdict. You should now see one item, never a table asking for every verdict at once.
2. The item says, in this order: what it says and the evidence behind it; what would change and for whom; Claude's recommendation with its reason and, for `accept`, the concrete text the artefact would receive. You should now see enough to decide without asking for an explanation.
3. The item closes with one proposition, worded so that `accept` means exactly one thing: yes to what is in front of you. It says what changes, or that nothing changes, and what is recorded. Under it stands the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. You should now see that line at the end of the message.
4. You answer with a letter or the word in full. Claude opens its next message with one line that names your verdict and says what it does, then carries the next item. You should now see one acknowledgement line and the next item, nothing else.
5. When the round looks finished, Claude adds `write` to the verdict line. You type `write` in full, Claude reflects the whole round back, and on your yes it writes everything carried as one round. You should now see Claude name the files and sections it wrote.

What each verdict does:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found is put forward for you to accept. After `m` alone, Claude asks what you want changed.
- `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. A question is never read as a change or as a yes. After `q` alone, Claude asks what you want to ask.
- `reject`: not agreed, nothing changes, and your reason is recorded.
- `park`: not now. The item waits and comes back.
- `obsolete`: no longer relevant, with a note on why. It has no letter and is typed in full.

`write` and every command are also typed in full. The exact words and letters are listed on [Verdict words](../reference/verdict-words.md).

## What gets written, and when

Verdicts are carried in the conversation and written once, at the round's end. Until then everything agreed is nowhere yet, and Claude says so.

- `accept` writes what the command that produced the list says (the fix) and a closing record.
- `reject` writes a decision with your reason and the verdict line "rejected". The item is not raised again.
- `park` writes a decision with the verdict "parked until" what you name.
- `obsolete` writes a decision with the verdict "obsolete" and what made the item moot.

A state is never changed by deleting a record. A newer record replaces it. After the write the ledger (the state of the project, made afresh from the documents at read time) is made again.

## The same line outside a list

The elicitation interview runs the same way: one question per message, and your answer is acknowledged before the next question comes. When you send one thought in pieces, Claude asks nothing until your closing word.

The same closing line ends every question of Claude's that asks you to decide, inside a walkthrough or outside it. Such questions are a step that needs your consent, a choice between options, an either/or, and whether to write. Each is one proposition, and Claude's recommendation is what `accept` means. A yes that carries a question is `question`, never consent. A question for information Claude lacks ends with the question alone.

## What you have afterwards

Every item has a verdict. Whatever you accepted, rejected, parked or declared obsolete is in a file, with your reason where the verdict needs one. Nothing agreed lives only in the conversation.

## If something goes wrong

- Claude puts two items, or several questions, in one message: answer the first and say so. The rule is one item per message.
- You are unsure about an item: answer `question`. Nothing changes until you give another verdict.
- You change your mind on an item already closed: say so. A newer record replaces the older one.

## A worked example

One item of a critique list, generic:

```
Item 2 of 5, finding on the assignment, section Scope.

The scope says "all regions" while the requirement REQ-A
names two. Whoever receives the assignment cannot tell
which is meant.

Change: the scope names the two regions. The recipients
no longer have to guess.

Recommendation: accept; the requirement is the more
precise of the two. The scope would read: "The regions
North and South."

Proposition: change the scope to name the two regions and
record the finding as closed.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer `q` and ask whether a third region was ever planned. Claude answers, changes nothing and closes the item again with the same line. You answer `a`. Claude's next message opens with one line, "Accepted: the scope will name the two regions", and carries item 3. At the end you type `write`. Claude reflects the five verdicts back, and on your yes it writes them as one round.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
