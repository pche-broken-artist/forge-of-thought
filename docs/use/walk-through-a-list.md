---
generated: 2026-10-09
made: mirrored
inputs-hash: 1193e743509f335f
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Walk through a list

This page is for the user who is asked to decide a list of items: review findings, challenges, open threads, open questions or the proposals of a source. It says how such a list is put to you, what each item contains, how you answer and when what you decided is written down.

## When it applies

A walkthrough runs whenever a list of items needs your decision, whatever produced the list. Critique findings, challenges, differences between two requirement sets, open threads, open questions and the proposals of a source are all worked this way. Any command that produces a list ends by offering a walkthrough.

## One item per message

Claude puts one item in front of you and stops. You give your verdict. The next message opens with one line acknowledging that verdict and then carries the next item, nothing else.

- Items come in order of weight.
- You are never shown a table asking for every verdict at once, nor a questionnaire of several questions.
- If you ask a question about the item, the item stays open until you close it. Claude does not move on to the next one.
- A check on whether Claude has understood an item fully is an item of its own.

## What an item carries

Each item gives you, in this order, what you need to decide without asking for an explanation:

1. What the item says, and the situation or evidence behind it, in a few sentences.
2. What would change, and for whom.
3. The recommendation with its reason. For `accept` this includes the concrete text the document would receive, not a description of the edit.

A heading with a one-sentence reason is only a label, not an item.

## The verdict

Every item ends in one proposition, worded so that `accept` has exactly one meaning: yes to what is in front of you. The proposition says what changes, or that nothing changes, and what is recorded. Where it goes against the reviewer's suggestion, it says so. The message closes with this line:

`(a)ccept / (m)odify / (r)eject / (p)ark`

An open question is not a proposition. It closes with the question alone.

| Verdict | Meaning |
|---|---|
| `accept` | Agreed. The text goes in as shown. |
| `modify` | A discussion opens on the item, and the solution found is put forward for you to accept. |
| `reject` | Not agreed. Nothing changes and your reason is recorded. |
| `park` | Not now. The item waits and comes back. |
| `obsolete` | No longer relevant, with a note on why. |

`obsolete` is a fifth verdict, not shown on the closing line. `park` is a legitimate verdict, not a failure. A recommendation you decline is not argued again unless there are new facts.

### Answering

You may answer with a single letter, `a`, `m`, `r` or `p`, when that letter is your whole message, or with the word. After `m` alone, Claude asks what you want changed. Claude's acknowledgement names the verdict in full and says what it does.

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

The exact words and letters are listed in [Verdict words](../reference/verdict-words.md).

## From verdicts to the write

Verdicts are carried in the conversation and written once, at the end of the round. Until then, what you agreed is nowhere yet, and Claude says so.

When the round looks finished, `write` is added to the verdict line. On `write`, Claude reflects the whole round back to you. On your yes, it writes everything carried as one round.

What each verdict writes:

- `accept` writes what the command that produced the list says (the critique, challenge or check; for the proposals of a source, a position with its provenance).
- `reject` writes a decision with your reason, state `rejected`, and the reviewer does not raise the item again. A source's proposal that is rejected becomes a rejected direction in the intent.
- `park` sets the state `parked`.
- `obsolete` sets the state `obsolete`, with what made the item moot.

States change in the ledger and are never deleted.

## The elicitation interview

An interview, where Claude draws out by questions what you have not yet put into words, runs the same way: one question per message, and your answer acknowledged before the next question is asked. If you send one thought in several pieces, Claude asks nothing until your closing word.

## See also

- [Verdict words](../reference/verdict-words.md): the words and letters, exactly.
- [About the working methods](../about/working-methods.md): why the one-item rule exists and how a hook holds it.
