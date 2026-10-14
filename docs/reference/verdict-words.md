---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: b53c0c73193f9b09
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types to answer Claude in a walkthrough, and what each one does. The words are the same in every walkthrough, whatever produced the list. The procedure they belong to is on [Walk through a list](../use/walk-through-a-list.md).

## The verdict line

Claude closes every proposition of a walkthrough with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |

A question is never read as a modification or a yes.

## The single letters

The principal may answer the verdict line with one letter: `a`, `m`, `q`, `r` or `p`. The letter counts only when it is the whole message.

- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what the principal wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Words outside the verdict line

| Word | What it does |
|---|---|
| `obsolete` | The item is no longer relevant. It is given with a note why. |
| `write` | Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. Claude adds `write` to the verdict line when the round looks finished. |
| `??` | Typed alone at the end of a message, or as the whole message: Claude gives its honest opinion of what the principal has just written. It gives three points at most, marked as its own. Nothing is written or filed. |
| a closing word such as "done" | Ends a thought sent in pieces. Until then Claude answers each piece with at most one line of acknowledgement and asks nothing. After it the pieces are one input, read and worked as a whole. |

## Words that have no letter

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
