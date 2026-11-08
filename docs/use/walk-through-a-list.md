---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: bab472cb99493fcc
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list of items that needs your decision, one item per message, and this page is for the principal (the person whose thinking is being forged) who answers it. The list may be findings of a critic, challenges, open threads, differences between two requirement sets or the proposals of a source. Whatever produced the list, the walkthrough runs the same way.

## When to use it

You do not start a walkthrough by a command. It begins whenever a list of items waits for your decision, and every command that produces such a list ends by offering one. The elicitation interview, in which Claude draws out by questions what you have not yet put into words, runs the same way.

## What you do

You answer each item with one verdict. The shortest form is the single letter or the word at the end of the item, typed as it stands:

```
a
```

The words and letters are exactly these (the page [Verdict words](../reference/verdict-words.md) lists them):

- `accept` (letter `a`): agreed, the text goes in as shown.
- `modify` (letter `m`): a discussion opens on the item, and the solution found is put forward for you to accept.
- `question` (letter `q`): you ask about the open item.
- `reject` (letter `r`): not agreed, nothing changes, your reason is recorded.
- `park` (letter `p`): not now; the item waits and comes back.
- `obsolete`: no longer relevant, with a note why. It has no letter.

A letter counts only when it is your whole message. After `m` alone Claude asks what you want changed, and after `q` alone it asks what you want to ask. No other word of the forge has a letter: `write` and every command are typed in full.

## What happens

1. Claude puts one item in front of you and stops. Items come in order of weight.
   You should now see a single item and nothing else, with no table asking for every verdict at once.
2. The item carries three things in this order: what it says and the evidence behind it; what would change and for whom; Claude's recommendation with its reason and, for `accept`, the concrete text the document would receive.
   You should now see enough to decide without asking for an explanation.
3. The item closes with one proposition, worded so that `accept` means yes to what is in front of you. It states what changes, or that nothing changes, and what is recorded. Then comes the line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
   You should now see the verdict line as the last line of the message.
4. You answer. Claude's next message opens with one line that names your verdict in full and says what it does, and then carries the next item.
   You should now see the acknowledgement first and the next item after it.
5. If you answer `question`, nothing changes and nothing is written. Claude answers and closes the same item again with the verdict line. A question is never read as a modification or a yes, so the item stays open until you close it.
   You should now see your answer and the same item again, with the verdict line.
6. When the round looks finished, the verdict line also offers `write`. On `write` Claude reflects the whole round back to you, and on your yes it writes everything carried as one round, with one version bump for the whole round.
   You should now see the files and sections Claude names as written.

Until the write, everything agreed lives only in the conversation. Claude says so, and it says that nothing is written yet.

## Beyond the list

The same line closes every question of Claude's that asks you to decide, whether in a walkthrough or outside it. Examples are a step that needs your consent, a choice between options, an either/or, or whether to write. Each is one proposition, with Claude's recommendation as what `accept` means. A yes that carries a question is `question`, not consent. Only a question for information Claude lacks ends with the question alone.

## What you have afterwards

Each verdict has its own result in the write:

- `accept` writes what the command that produced the list says (the fix) and a closing record in the history of the document.
- `reject` writes a decision with your reason and its verdict line. The item is not raised again.
- `park` writes a decision with your reason and what the item waits for.
- `obsolete` writes a decision with what made the item moot.

A state is changed by a newer record or verdict, never by deleting one. After the write the ledger (the table of state that is made fresh from the documents at read time) is made afresh, so that it shows the new state.

## If something goes wrong

- If you want a different wording, answer `modify`. Claude opens a discussion and puts the solution forward again to be accepted.
- If you only want to understand the item, answer `question`. Nothing is changed by it.
- If you decline a recommendation, Claude does not argue it again without new facts.
- If a message carries several verdicts at once or a questionnaire, Claude is out of the method. Ask for one item at a time. The reason the one-item rule exists, and how a hook holds it, is on [The working methods](../about/working-methods.md).

## A worked example

A critic has returned a list of findings, and the first item is put to you. The text is generic.

```
Finding 1 of 4: the overview names two roles for the same
person, "owner" and "lead".

Evidence: section 2 says "owner", section 5 says "lead", and
nothing says they are one role.

Change: section 5 would read "owner". Readers of the overview
no longer wonder whether two people are meant.

Recommendation: accept, because one word per thing keeps the
text unambiguous. Section 5 would receive: "The owner signs
the plan."

Accept: section 5 says "owner" as shown and the finding is
recorded as closed.

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer `q` and then ask whether "lead" appears anywhere else. Claude answers and closes the item again with the same line, and nothing has changed. You then answer `a`. Claude's next message opens with one line, "Accepted: section 5 says owner, carried to the write", and carries finding 2. After the last finding you answer `write`, Claude reflects the round back, and on your yes it writes it.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
