---
generated: 2026-10-09
made: mirrored
inputs-hash: 414b8ba5192c35d4
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md
---

# Verdict words

This page lists the words the principal types in a working
conversation and what each one does. It is for the person who uses the
forge and wants to look a word up.

## The verdict line

Every item of a walkthrough closes with this line:

`(a)ccept / (m)odify / (r)eject / (p)ark`

| Word | What it does |
|---|---|
| `accept` | Agreed. The text goes in as shown. |
| `modify` | A discussion opens on the item, and the solution found is put forward to be accepted. |
| `reject` | Not agreed. Nothing changes and the reason is recorded. |
| `park` | Not now. The item waits and comes back. |
| `obsolete` | No longer relevant, with a note why. |

## Single letters

The verdict line may be answered with one letter: `a`, `m`, `r` or
`p`, when that letter is the whole message. After `m` alone, Claude
asks what is to be changed. Claude's acknowledgement names the verdict
in full and says what it does.

## What the verdicts write

| Verdict | Written |
|---|---|
| `accept` | What the producing command says (`/critique`, `/challenge`, `/check`); for a source's proposals, a position with provenance. |
| `reject` | A decision record with the principal's reason, state `rejected`. The reviewer does not raise the item again. A rejected proposal from a source becomes a rejected direction in the intent. |
| `park` | State `parked`. |
| `obsolete` | State `obsolete`, with what made it moot. |

States in the ledger change only, never delete.

## Other words

| Word | What it does |
|---|---|
| `write` | Orders the write of the round. Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. It is added to the verdict line when the round looks finished. A `write` ordered at any moment writes what is agreed so far and does not close the round unless the principal says so. |
| `??` | Alone at the end of a message, or as the whole message: asks for Claude's honest opinion of what was just written. Three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | Ends a thought sent in several pieces. Until it, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are read as one input. |

## Words without a letter

No other word of the forge has a letter. `write`, `obsolete` and every
command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
