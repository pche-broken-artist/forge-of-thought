---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 981f9c7d818be6ac
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (whoever's thinking is being forged) types in a walkthrough (a list of items worked one per message) or at a step that needs his word. It is for the reader who wants to know exactly what to type.

## The verdict line

Claude closes every proposition with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | You ask about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. Type it in full. |

## Single letters

- A single letter `a`, `m`, `q`, `r` or `p` counts as a verdict when it is your whole message.
- After `m` alone, Claude asks what you want changed.
- After `q` alone, Claude asks what you want to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Where the line appears

- Every item of a walkthrough ends with the line, whatever produced the list.
- Every step that needs your consent closes with the same line. Such a step is a write, a run, a commit or a change of a setting.
- Every question of Claude's that asks you to decide closes with the line. It is one proposition, and Claude's recommendation is what `accept` means.
- A question for information Claude lacks closes with the question alone, without the line.
- A message that says yes and also asks a question is `question`, never consent.
- No command has verdict words of its own.

## Other words

| Word | Where | What it does |
|---|---|---|
| `write` | At the end of a round of work | Claude reflects the whole round back and, on your yes, writes everything carried as one round. Type it in full. |
| `??` | Alone at the end of your message, or as the whole message | Claude gives its honest opinion of what you have just written: three points at most, marked as its own. Nothing is written or filed. |
| a closing word such as "done" | After a thought sent in several messages | Until the word arrives, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are read as one input. |

## What has no letter

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
