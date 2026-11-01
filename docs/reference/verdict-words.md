---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 868dea6bcd666ecc
inputs:
  - .claude/skills/walkthrough/SKILL.md
  - CLAUDE.md#Working methods
---

# Verdict words

This page lists the words and letters the principal (the person whose thinking is forged) types in a walkthrough, or at a step that needs his word, and what each does. A walkthrough is the working method in which a list of items is decided one item per message; the procedure is on [Walk through a list](../use/walk-through-a-list.md).

## The verdict line

Claude closes a proposition with this line:

`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`

The line closes every item of a walkthrough. It also closes every step that needs the principal's consent, and every question of Claude's that asks him to decide. In each case Claude's recommendation is what `accept` means.

A question for information Claude lacks closes with the question alone, without the line.

## The verdicts

| Word | Letter | What it does |
|---|---|---|
| `accept` | `a` | Agreed. The text goes in as shown. |
| `modify` | `m` | A discussion opens on the item. The solution found is put forward to be accepted. |
| `question` | `q` | The principal asks about the open item. Nothing changes and nothing is written. Claude answers and closes the item again with the verdict line. |
| `reject` | `r` | Not agreed. Nothing changes and the reason is recorded. |
| `park` | `p` | Not now. The item waits and comes back. |
| `obsolete` | none | No longer relevant, with a note why. Typed in full. |

## Single letters

- A single letter answers the verdict line only when it is the whole message.
- After `m` alone, Claude asks what the principal wants changed.
- After `q` alone, Claude asks what he wants to ask.
- Claude's acknowledgement names the verdict in full and says what it does.

## A yes that carries a question

A message that says yes and asks a question is `question`. It is not consent.

## Other words

| Word | What it does |
|---|---|
| `write` | Claude reflects the whole round back and, on the principal's yes, writes everything carried as one round. Claude adds it to the verdict line when the round looks finished. Typed in full. |
| `??` | Placed alone at the end of a message, or as the whole message, it asks for Claude's honest opinion of what the principal has just written. Claude gives three points at most, marked as its own, and writes and files nothing. |
| a closing word such as "done" | Ends a thought sent in pieces. Until it comes, Claude answers each piece with at most one line of acknowledgement. After it, the pieces are one input. |

## Letters and commands

No other word of the forge has a letter. Every command is typed in full.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the procedure the words belong to.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
