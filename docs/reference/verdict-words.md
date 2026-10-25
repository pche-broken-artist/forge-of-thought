---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 92a6a47dca597a3f
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is being forged) types in a walkthrough, or at a step that needs his word, and what each does. It is for anyone who answers Claude and wants to type the words exactly.

## The verdict line

Claude closes every item of a walkthrough with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |

`obsolete` is a sixth verdict. It has no letter and is typed in full. It means the item is no longer relevant, and a note says why.

## Single letters

- A single letter `a`, `m`, `q`, `r` or `p` answers the verdict line when the letter is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Where the verdict line closes

- Every item of a walkthrough ends with the line.
- Every step that needs the principal's consent ends with the same line. Such a step is a write, a run, a commit or a change of a setting. It arrives as one proposition.
- Every question of Claude's that asks the principal to decide ends with the same line, in a walkthrough or outside it.
- In each of these, Claude's recommendation is what `accept` means.
- A message that says yes and also asks a question is `question`, never consent.
- Only a question for information Claude lacks closes without the line. It closes with the question alone.

## Other words

| Word | What it does |
|---|---|
| `write` | Claude reflects the whole round back. On the principal's yes it writes everything carried in the conversation as one round. |
| `??` | Typed alone at the end of a message, or as the whole message, it asks Claude for its honest opinion of what the principal has just written. Claude gives three points at most, marked as its own. Nothing is written or filed. |
| a closing word such as "done" | Ends a thought sent in several messages. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## What has no letter

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
