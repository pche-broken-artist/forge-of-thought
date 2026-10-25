---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 5b2e5a62133ed2b9
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Walk through a list

A walkthrough is the way Claude works any list of items that needs
your decision: one item per message, each closed with a verdict
line that you answer. This page is for the principal (the person
whose thinking is being forged) and shows what you see and what you
type. Findings, challenges, open threads and the proposals of a
source are all worked this way, and so is every elicitation
interview.

## When to use it

You do not start a walkthrough. It begins whenever Claude has a list
that needs your decision, whatever produced the list: a critique, a
challenge, a check, a comparison, the state map of a project, open
threads. Whatever produces such a list ends by offering a
walkthrough, and you accept the offer.

## What you do

You answer each item with its verdict. The verdict line closing
every item is this one:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You may answer with a single letter, `a`, `m`, `q`, `r` or `p`, when
that letter is your whole message. You may also type the word. A
further verdict, `obsolete`, is available when an item no longer
matters; it has no letter and is typed in full. The exact words and
letters are on [Verdict words](../reference/verdict-words.md).

When the round looks finished, Claude adds `write` to the line. You
type `write` in full whenever you want what is agreed to be written.

## What happens

1. Claude puts one item in front of you and stops. Items come in
   order of weight, heaviest first. Each item carries, in this
   order:
   - what it says and the situation or evidence behind it;
   - what would change and for whom;
   - the recommendation with its reason, and for an `accept` the
     concrete text the artefact would receive, not a description of
     the edit.

   The item ends with one proposition, worded so that `accept`
   means exactly yes to what is in front of you. The proposition
   says what changes, or that nothing changes, and what is
   recorded.

   You should now see the item, its proposition and the verdict
   line, and nothing about the next item.

2. You give your verdict. Claude opens its next message with one
   line that names your verdict in full and says what it does, then
   carries the next item.

   You should now see that one-line acknowledgement followed by
   exactly one new item.

3. The verdicts mean this:
   - `accept`: agreed, the text goes in as shown.
   - `modify`: a discussion opens on the item, and the solution
     found is put forward for you to accept. After a bare `m`,
     Claude asks what you want changed.
   - `question`: you ask about the open item. Nothing changes and
     nothing is written. Claude answers and closes the item again
     with the verdict line. After a bare `q`, Claude asks what you
     want to ask.
   - `reject`: not agreed, nothing changes, your reason is
     recorded.
   - `park`: not now. The item waits and comes back.
   - `obsolete`: no longer relevant, with a note why.

   You should now see the same item again with the verdict line
   after a question, and the next item after any other verdict.

4. The verdicts are carried in the conversation and not written one
   by one. When you type `write`, Claude reflects the whole round
   back to you first, and writes only on your yes.

   You should now see the round restated, with the new wording of
   every change, before anything is written.

5. On your yes, everything carried is written as one round. What
   each verdict writes:
   - `accept`: what the command that produced the list says (the
     fix), and a record that the item is closed.
   - `reject`: a decision record with your reason and its verdict
     line. The item is not raised again.
   - `park`: a decision record with your reason, saying the item is
     parked until what you named.
   - `obsolete`: a decision record saying the item is obsolete and
     what made it moot.

   Afterwards Claude makes the ledger afresh (the single source of
   truth for state, made at read time from the documents). A state
   changes by a newer record, never by deleting an older one.

   You should now see the files Claude names as written, and the
   ledger rebuilt.

## What you have afterwards

Every item of the list has a verdict, and each verdict is in a file
that Claude names. Until the write, everything agreed is nowhere yet
and Claude says so. A rejected item is not raised again, and a
declined recommendation is not argued again without new facts.

## The same shape elsewhere

- The elicitation interview, in which Claude draws out what you have
  not yet articulated, runs the same way: one question per message,
  your answer acknowledged before the next question. When you send a
  thought in pieces and close it with a word such as "done", Claude
  asks nothing until that word.
- Every single step that needs your consent (a write, a commit, a
  push, a rename, a change of a setting) arrives as one proposition
  with the exact operation, its target and the reason, and closes
  with the same verdict line. A batch of sensitive operations is
  never run as one.
- The conflict a save meets is laid out one conflict per message in
  the same way: [Settle a conflict](settle-a-conflict.md).

## If something goes wrong

- Your message says yes but also asks something. It is read as
  `question`, never as consent. Claude answers and asks again.
- A remark or a counter-thought in answer to a proposal is not a
  yes either. Claude reworks the proposal and asks again.
- Claude puts several items or a table of verdicts in front of you.
  That is not the shape of a walkthrough; ask for one item at a
  time.
- A letter typed as part of a longer message is not read as a
  verdict. Type the letter alone, or the word.

## A worked example

Claude has a list of three findings from a critique of a project
named `example-project`. It opens with the heaviest.

Claude writes:

> Finding 1 of 3: two sections of the intent give different values
> for the same limit. Section A says five, section B says seven.
> Only section B changes, and only for readers of the intent.
> I recommend five, because the history shows that section B was
> written first. The text section B would receive: "The limit is
> five."
>
> Proposition: change section B to "The limit is five." and record
> the finding as closed.
>
> (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark

You type `q` and then, when asked, "Why five and not seven?"
Claude answers in a few sentences, changes nothing, and closes the
item again with the same verdict line.

You type `a`. Claude writes one line, "Accepted: section B will
read five, finding 1 closed on the write", and carries finding 2.

After finding 3, Claude adds `write` to the verdict line. You type
`write`. Claude reflects the round back, with the new wording and
the records. You say yes, Claude writes the files and names them,
and the ledger is made afresh.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [The working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
- [Settle a conflict](settle-a-conflict.md): the conflict of a save, laid out one conflict per message in the same way.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
