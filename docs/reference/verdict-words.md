---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 2d3a75f515ac5dec
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types in a walkthrough, exactly as Claude reads them. It is for the principal at the keyboard. The procedure these words belong to is on [Walk through a list](../use/walk-through-a-list.md).

## The verdict line

Every item of a walkthrough closes with this line:

`(a)ccept / (m)odify / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |

## Other words

| Word | What it does |
|---|---|
| `obsolete` | The item is no longer relevant. A note says why. |
| `write` | Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. Claude adds it to the verdict line when the round looks finished. |
| `??` | Asks for Claude's honest opinion of what the principal has just written. It stands alone at the end of a message or is the whole message. Claude answers with three points at most, marked as its own. Nothing is written or filed. |
| a closing word such as "done" | Closes a thought sent in pieces. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## Single letters

- The letters `a`, `m`, `r` and `p` answer the verdict line only when the letter is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- Claude's acknowledgement names the verdict in full and says what it does.
- No other word of the forge has a letter.
- `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
