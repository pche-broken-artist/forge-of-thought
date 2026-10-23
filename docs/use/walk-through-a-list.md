---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: eee833918fbcae3a
inputs:
  - .claude/skills/walkthrough/SKILL.md
---

# Walk through a list

This page shows how any list that needs your decision is worked: one item at a time, with a fixed set of answers. It is for you as the principal, the person whose thinking is being forged. The same way runs on findings, challenges, open threads, open questions and the proposals of a source.

## When to use it

You use it whenever Claude hands you a list to decide. Claude puts the list into this form on its own, whatever produced it. A list of findings or challenges ends by offering it. An elicitation interview, where Claude draws out by questions what you have not yet put into words, runs the same way.

## What you do

You answer each item with one verdict. The verdict line closing every item is:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

You may answer with the single letter or with the word. A letter is accepted only when it is your whole message. When the round looks finished, Claude adds `write` to the line. Type `write` and `obsolete` in full, because no other word of the forge has a letter.

## What happens

1. Claude puts one item in front of you and stops. It works the items in order of weight, and it never asks for several verdicts at once.

   You should now see one item that carries, in this order: what it says and the situation behind it; what would change and for whom; and a recommendation with its reason. For `accept`, the recommendation includes the exact text the document would receive. The item ends with one proposition and the verdict line. The proposition says what changes, or that nothing does, and what is recorded.

2. You give your verdict.

   - `accept`: you agree, and the text goes in as shown.
   - `modify`: a discussion opens on the item. The solution you find together is put forward for you to accept.
   - `question`: you ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. A question is never read as a change or as a yes.
   - `reject`: you do not agree. Nothing changes, and your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: the item no longer matters, and a note says why.

   After `m` alone, Claude asks what you want changed. After `q` alone, it asks what you want to ask.

   You should now see one line that names your verdict in full and says what it does, followed by the next item and nothing else.

3. You repeat until the list is done. Nothing is written yet.

   You should now see Claude say that what you agreed is carried in the conversation only. It is saved nowhere until the write.

4. You type `write`. Claude reflects the whole round back to you first. On your yes, it writes everything carried as one round.

   You should now see what was written, with the file and section named.

## What you have afterwards

- For each `accept`, the fix that the producing command defines, together with a record that the item is closed.
- For each `reject`, a decision with your reason and a verdict line saying the item is rejected. A rejected item is not raised again.
- For each `park`, a decision with your reason and a verdict line saying what the item waits for.
- For each `obsolete`, a decision with the verdict line saying it is obsolete and what made it moot.
- A rejected proposal of a source becomes a rejected direction in the intent.
- The ledger, which Claude makes afresh after the write.

A state is changed by a newer record, never by deleting one.

## If something goes wrong

- If you ask something instead of giving a verdict, the item stays open until you close it. Claude never moves to the next item on its own judgement.
- If a table of verdicts or a questionnaire of several questions is put in front of you, that is not the method. Ask for one item at a time.
- If you send one longer thought in several messages, Claude acknowledges each piece with at most one line and asks nothing until your closing word.

## A worked example

This is one generic item from a list of findings.

> Finding 2 of 5: the section "Scope" names a recipient group in one place and a different group in another. The first mention is in the opening paragraph, the second in the closing list.
>
> What would change: the closing list would use the same group as the opening paragraph. Readers of the document would no longer have to guess which group is meant.
>
> I recommend accepting. The opening paragraph is the older wording and the closing list repeats it with a slip. The closing list would read: "Recipients: the platform team."
>
> Proposition: the closing list is changed as shown and the item is recorded as closed.
>
> (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark

You answer `q` and then ask which wording came first. Claude answers and shows the item again with the same verdict line. You answer `a`. Claude acknowledges that you accepted and what that does, then shows finding 3.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
