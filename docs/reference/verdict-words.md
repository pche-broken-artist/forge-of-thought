---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 6739c3b8eeb0bcde
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types in a walkthrough (a list of items worked one per message) or at a step that needs his word, and what each does. Use it when you need the exact word. The procedure the words belong to is on [Walk through a list](../use/walk-through-a-list.md); the terms of the forge are in the [Glossary](glossary.md).

## The verdict line

Every item of a walkthrough closes with this line, and so does every step that needs the principal's consent:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

## The verdicts

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed: the text goes in as shown. |
| `modify` | `m` | A discussion opens on the item, and the solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed: nothing changes and the reason is recorded. |
| `park` | `p` | Not now: the item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. |

`obsolete` is typed in full.

## The single letters

- The letters `a`, `m`, `q`, `r` and `p` answer the verdict line.
- A letter counts only when it is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Steps outside a walkthrough

- A step that needs the principal's consent (a write, a run, a commit, a change of a setting) arrives as one proposition and closes with the same verdict line.
- A message that says yes and also asks a question is `question`, not consent.

## Other words

| Word | What it does |
|---|---|
| `write` | Asks Claude to reflect the whole round back and, on the principal's yes, to write everything carried as one round. |
| `??` | Typed alone at the end of a message, or as the whole message: asks Claude's honest opinion of what the principal has just written. Three points at most, marked as Claude's own. Nothing is written or filed. |
| a closing word such as "done" | Ends a thought sent in several messages. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## What has no letter

- No other word of the forge has a letter.
- `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
