---
description: The forge's manual, read from its own definitions — bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill
argument-hint: "[command | method]"
---

The manual of the forge (POS.1190): a reader, never a text of its
own. Everything it prints is read at the moment of the call from the
files that own it — CLAUDE.md, the skills, the agents, the state and
genre files — and shortened to the line; nothing is stated here that
lives there. Read-only; it runs no command it describes. Alias:
`/manual` (`.claude/skills/manual/SKILL.md`). The word `help` is
Claude Code's own command, hence the Unix name.

**Bare `/man` — the overview.**
1. Read the Commands table of CLAUDE.md and print it as a list: the
   command with its arguments, then its purpose cut to one line.
   `/man` and `/manual` included.
2. Read the Working methods section of CLAUDE.md and print each
   method's name with the first sentence of its paragraph.
3. Close with one line: `/man <command>` for a command's page,
   `/man <method>` for a method's.

**`/man <command>` — the page of one command.**
1. Resolve `$1` to `.claude/skills/<command>/SKILL.md`; if none
   exists, say so and list the commands (step 1 of the overview).
2. Print the command's purpose (its `description`), its arguments
   (its `argument-hint`, else the CLAUDE.md row) and the CLAUDE.md
   row's purpose in full.
3. Print the roster the command dispatches over, where its skill
   names one: the same scan the bare command makes, read from that
   skill, each entry with the `description` of its own file and,
   where the file carries one, its `## Lens` section — for a genre
   its Elicitation checklist — in full, so that the user knows what
   a check, a lens, a persona or a genre looks for before running
   it. `/man` adds what each entry looks for and runs nothing.
4. Close with one line naming the skill file, for the reader who
   wants the whole procedure.

**`/man <method>` — the page of one working method.** Resolve `$1`
against the bold names of the Working methods section of CLAUDE.md
(case-insensitive, hyphens and spaces alike); print the paragraph in
full and, where it names a skill that holds the method's shape,
that skill's path. Unknown: say so and list the methods (step 2 of
the overview).

Language: the conversation language (CLAUDE.md, prime directive 6 —
translate on write), the whole page, descriptions and Lens sections
included; only the notation stays English — command names, file
paths, IDs, front-matter keys and the bold names of the methods,
each followed by its translation once.
