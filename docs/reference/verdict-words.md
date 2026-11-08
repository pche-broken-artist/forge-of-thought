---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 1e259cde4d282bc9
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal types in a walkthrough or at a step that needs his word, exactly as Claude reads them. The principal is whoever's thinking is being forged. A walkthrough is the way Claude works a list of items needing a decision, one item per message; the procedure is in [Walk through a list](../use/walk-through-a-list.md). Terms of the forge are in the [Glossary](glossary.md).

## The verdict line

Every item of a walkthrough closes with this line, typed by Claude as it stands:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |

## The single letters

- The principal may answer the verdict line with `a`, `m`, `q`, `r` or `p`.
- The letter counts only when it is his whole message.
- After `m` alone Claude asks what he wants changed.
- After `q` alone Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Where the line is used

- The verdict words are the same in every walkthrough, whatever produced the list. No command has words of its own.
- Every step that needs the principal's consent closes with the same line. Such a step is a write, a run, a commit or a change of a setting, and it arrives as one proposition.
- Every question of Claude's that asks the principal to decide closes with the same line. Such a question is a choice between options, an either/or or whether to write.
- In such a proposition Claude's recommendation is what `accept` means.
- A message that says yes and carries a question is `question`, never consent.
- Only a question for information Claude lacks closes with the question alone.

## Other words

| Word | What it does |
|---|---|
| `obsolete` | The item is no longer relevant. Claude notes why. It is typed in full, with no letter. |
| `write` | Asks Claude to reflect the whole round back and, on the principal's yes, to write everything carried in the conversation as one round. It is typed in full, with no letter. Claude adds it to the verdict line when the round looks finished. |
| `??` | Alone at the end of the principal's message, or as his whole message, it asks for Claude's honest opinion of what he has just written: three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | Closes a thought sent in pieces. Until it comes Claude answers each piece with at most one line of acknowledgement. After it the pieces are one input. |

## What has no letter

- No other word of the forge has a letter.
- `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
