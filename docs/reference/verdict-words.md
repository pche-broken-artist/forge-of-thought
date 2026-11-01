---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: f271acff0454eb64
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (whoever's thinking is being forged) types in a walkthrough (a list worked one item per message) or at a step that needs his word, and what each does. Claude is the assistant that reads them.

## The verdict line

Every item of a walkthrough closes with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes. The reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. Typed in full. |

## The single letters

- The letter `a`, `m`, `q`, `r` or `p` is a verdict when it is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## Where the line stands

- Every item of a walkthrough ends in one proposition and closes with the line. `accept` means yes to what is in front of the principal.
- Every step that needs the principal's consent closes with the same line. Such a step is a write, a run, a commit or a change of a setting.
- Every question of Claude's that asks the principal to decide closes with the same line, in a walkthrough or outside it. Claude's recommendation is what `accept` means.
- A question for information Claude lacks closes with the question alone.
- A message that says yes and also asks a question is `question`, never consent.
- No command has verdict words of its own.

## Other words

| Word | What it does |
|---|---|
| `write` | Asks Claude to reflect the whole round back and, on the principal's yes, to write everything agreed as one round. It is added to the verdict line when the round looks finished. |
| `??` | Alone at the end of the principal's message, or as his whole message, it asks for Claude's honest opinion of what he has just written: three points at most, marked as Claude's own, nothing written or filed. |
| a closing word such as "done" | Ends a thought sent in several messages. Until it, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## Letters and full words

No other word of the forge has a letter. `write`, `obsolete` and every command are typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
