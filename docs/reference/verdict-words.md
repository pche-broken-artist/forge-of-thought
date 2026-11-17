---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: e27bc2a08448d8ba
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types in a walkthrough or at a step that needs his word. A walkthrough is the method in which Claude puts a list of items in front of him, one item per message. The words are typed exactly as shown.

## The verdict line

Every item of a walkthrough closes with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

The same line closes every step that needs the principal's consent, such as a write, a run, a commit or a change of a setting. It also closes every question of Claude's that asks him to decide. In each case Claude's recommendation is what `accept` means. A question for information Claude lacks closes with the question alone.

## The verdicts

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes and the reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. |

## Single letters

- A single letter (`a`, `m`, `q`, `r` or `p`) answers the verdict line when it is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.
- A message that says yes and also asks a question is `question`, never consent.

## Other words

| Word | Where | What it does |
|---|---|---|
| `write` | the end of a round of work | Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. It is typed in full. |
| `??` | alone at the end of a message, or as the whole message | Asks for Claude's honest opinion of what the principal has just written: three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | after a thought sent in pieces | Closes the pieces. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## Words without a letter

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
