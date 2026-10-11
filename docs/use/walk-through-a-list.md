---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 96780f82f777c81f
inputs:
  - .claude/skills/walkthrough/SKILL.md
---

# Walk through a list

A walkthrough is the way any list that needs your decision is worked: one item per message, in order of weight, each closed with a verdict you give. This page is for you, the principal (the person whose thinking is being forged), when Claude puts a list of findings, challenges, threads or open questions in front of you. Every term of the forge is in one line in the [Glossary](../reference/glossary.md).

## When to use it

A walkthrough runs whenever a list of items needs your decision. The list may come from a critique, a challenge, a check, a comparison of two requirement sets, the open threads, open questions or the proposals of a source. It makes no difference which command produced the list. Claude also offers a walkthrough at the end of such a command.

The elicitation interview, in which Claude draws out by questions what you have not yet put into words, runs the same way.

## What you do

You answer each item with one verdict. The closing line of every item is:

```
(a)ccept / (m)odify / (r)eject / (p)ark
```

You may answer with a single letter, `a`, `m`, `r` or `p`, when that letter is your whole message. Or you may type the word. Nothing else in the forge has a letter: `write` and `obsolete` are typed in full, and so is every command.

## What happens

1. Claude puts one item in front of you and stops.

   An item carries, in this order:
   - what it says, with the situation or evidence behind it, in a few sentences;
   - what would change, and for whom;
   - the recommendation with its reason and, for `accept`, the concrete text the document would receive, never a description of the edit.

   The item ends in one proposition that says what changes, or that nothing changes, and what is recorded. Where the proposition goes against the reviewer's suggestion, it says so. `accept` always means yes to what is in front of you.

   You should now see one item, the verdict line, and no second item.

2. You give your verdict.

   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution you find together is put forward to be accepted. After a bare `m`, Claude asks what you want changed.
   - `reject`: not agreed, nothing changes, and your reason is recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why. It is a fifth verdict, not shown on the line.

   You should now see one line that names your verdict in full and says what it does.

3. A question from you keeps the item open.

   You may ask instead of deciding. Claude answers, and the item stays open until you close it. Claude does not move to the next item while it is open. A question that is only a check whether Claude has understood an item is an item of its own.

   You should now see the same item still open, with your question answered.

4. The next item follows.

   The message opens with the one-line acknowledgement and carries the next item, nothing else. You will never be shown a table that asks for every verdict at once, or a questionnaire of several questions. A heading with a one-sentence reason is a label, not an item.

   You should now see the next item, lighter in weight than the last.

5. When the round looks finished, `write` is added to the verdict line. Type `write` in full.

   Claude reflects the whole round back to you. On your yes it writes everything carried as one round.

   You should now see the files and sections that were written, named.

## What you have afterwards

Verdicts are carried in the conversation and written once, at the round's end. Until `write`, everything agreed is nowhere yet, and Claude says so.

What each verdict leaves behind, wherever the list came from:

- `accept` writes what the producing command says: a critique, a challenge or a check files its findings in its own way; for the proposals of a source it is a position with its provenance.
- `reject` writes a decision record with your reason, the item's state becomes `rejected`, and the reviewer does not raise it again. A source's proposal that you reject becomes a rejected direction in the intent.
- `park` sets the state `parked`.
- `obsolete` sets the state `obsolete`, with what made the item moot.

States in the ledger (the single record of state of a project) only change; nothing is deleted.

## If something goes wrong

- You want to decide several items at once: it is not offered. Take them one by one; `park` is a legitimate verdict, not a failure.
- You disagree with a recommendation: say `reject` or `modify`. A declined recommendation is not argued again unless there are new facts.
- Claude asks an open question and gives no proposition: answer it. Claude turns a question into a proposition where it can, never by filling a gap with an assumption.
- You send a thought in several pieces: Claude asks nothing until your closing word.

## A worked example

Claude shows one finding from a list, with a placeholder name:

> Finding 3 of 7 (the heaviest left). The page on `example-topic` says the review is optional in one section and required in another. A reader cannot tell which holds. This would change one sentence in section 2, for everyone who reads the page. I recommend the required reading, because the other sections assume it. For `accept`, the sentence in section 2 becomes: "The review is required before a release."
>
> Proposition: the sentence in section 2 is replaced as shown; the finding is recorded as resolved.
>
> (a)ccept / (m)odify / (r)eject / (p)ark

You answer `a`. Claude replies with one line, "Accepted: the sentence in section 2 is replaced as shown, to be written at the end of the round", and then shows finding 4. If you had answered `r` and given a reason, the reason would be recorded as a decision and the finding would not come back.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
