---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Verdict words

The words the principal types in a working conversation and what each
does. For the user of the forge.

## The verdict line

Every item of a walkthrough closes with this line:

`(a)ccept / (m)odify / (r)eject / (p)ark`

| Word | What it does |
|---|---|
| `accept` | Agreed; the text goes in as shown. |
| `modify` | A discussion opens on the item, and the solution found is put forward to be accepted. |
| `reject` | Not agreed; nothing changes; the reason is recorded. |
| `park` | Not now; the item waits and comes back. |
| `obsolete` | No longer relevant; a note says why. |

## Single letters

`a`, `m`, `r` or `p` may answer the verdict line when the letter is
the whole message. After `m` alone, Claude asks what is to be changed.
Claude's acknowledgement names the verdict in full and says what it
does.

## Other words

| Word | What it does |
|---|---|
| `write` | Orders the write of the round: Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. |
| `??` | Alone at the end of a message, or as the whole message, asks for Claude's honest opinion of what was just written: three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | Ends a thought sent in several messages; until it, each piece gets at most one line of acknowledgement, after it the pieces are read as one input. |

## What has no letter

No other word of the forge has a letter. `write`, `obsolete` and every
command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
