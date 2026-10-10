---
generated: 2026-10-10
made: mirrored
inputs-hash: 7c64a5f73079a0e7
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Verdict words

This page lists the words the principal types in a working conversation
and what each one does. It is for the person who runs the forge.

## The verdict line

Every item of a walkthrough closes with the line
`(a)ccept / (m)odify / (r)eject / (p)ark`.

| Word | What it does |
|---|---|
| `accept` | Agreed; the text goes in as shown. |
| `modify` | A discussion opens on the item; the solution found is put forward to be accepted. |
| `reject` | Not agreed; nothing changes; the reason is recorded. |
| `park` | Not now; the item waits and comes back. |
| `obsolete` | No longer relevant; a note says why. |

## Single letters

`a`, `m`, `r` and `p` each stand for the verdict of that letter when the
letter is the whole message. After `m` alone, Claude asks what is to be
changed. Claude's acknowledgement names the verdict in full and says what
it does.

## Other words

| Word | What it does |
|---|---|
| `write` | Orders the write of the round: Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. It is added to the verdict line when the round looks finished. |
| `??` | Alone at the end of a message, or as the whole message, asks for Claude's honest opinion of what was just written: three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | Ends a thought sent in pieces. Until it comes, each piece is answered with at most one line of acknowledgement; after it, the pieces are read as one input. |

## What has no letter

No other word of the forge has a letter. `write`, `obsolete` and every
command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
