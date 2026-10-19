---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 2943113e8a8bef5d
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types in a walkthrough (a list of items worked one per message), exactly as Claude reads them. It is for the principal who wants to know what to type and what each word does. The procedure the words belong to is on [Walk through a list](../use/walk-through-a-list.md).

## The verdict line

Claude closes every proposition of a walkthrough with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

## The verdicts

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. |

## The single letters

- The letters are `a`, `m`, `q`, `r` and `p`.
- A letter counts only when it is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Other words

| Word | What it does |
|---|---|
| `write` | Orders the write of what is agreed in the round. Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. |
| `??` | Asks for Claude's honest opinion of what the principal has just written. It is typed alone or at the end of a message. Claude gives three points at most, marked as its own. Nothing is written or filed. |
| a closing word such as "done" | Closes a thought sent in pieces. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input, read and worked as a whole. |

## What has no letter

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
