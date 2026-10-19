---
description: The history of one item by its ID — its wording today, its records, the archive rows that mention it and every citation, gathered by a script; Claude adds a few sentences of its own
argument-hint: "<ID> [project-slug]"
---

The history of one item (POS.1510, SOL.0630): what the project holds
of the item named by `$0`, printed in full for that one item and
nothing else. Read-only; this command writes nothing and runs
nothing but its script. This is the one way Claude reads an item's
history before proposing a change to it (CLAUDE.md, Versioning &
status): the log is searched by the script, never loaded whole into
the conversation.

1. The project is the slug given as the second argument, else the
   project in context (`forge` is the engine's own project); if that
   is ambiguous, ask.
2. Run `python scripts/forge-history.py <ID> <slug>` (a short form
   such as `pos580` is accepted) and print what it printed,
   unshortened. What the script gathers, from where and in what
   shape is its header's; `--full` prints every Was whole.
3. Add at most three sentences of Claude's own, marked as such: what
   the item says today, how it moved (born when, changed how many
   times, last at which version), and what hangs on it (a thread, a
   finding, a challenge among the citations). Nothing is derived
   from them and nothing is written: a change the reading suggests
   is proposed in the round that owns the item.

An ID nothing in the project knows is said so, as the script says
it; the command never guesses a near ID.
