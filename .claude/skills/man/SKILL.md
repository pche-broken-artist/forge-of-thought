---
description: The forge's manual, read from its own definitions — bare = the commands and the working methods, with a command = its purpose, arguments and roster, with a method = its paragraph and skill, with a need in free words = the way the forge has for it
argument-hint: "[command | method | question]"
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
1. Resolve `$0` to `.claude/skills/<command>/SKILL.md`; if none
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

**`/man <method>` — the page of one working method.** Resolve `$0`
against the bold names of the Working methods section of CLAUDE.md
(case-insensitive, hyphens and spaces alike); print the paragraph in
full and, where it names a skill that holds the method's shape, that
skill's path. Unknown, and not a question: say so and list the methods
(step 2 of the overview).

**`/man <question>` — the way the forge has for a need said in free
words.** Anything that resolves to no command and no method is a
question (POS.1190).
1. Read the documentation's index, `docs/README.md`: every page
   carries the one question it answers. Choose the pages whose
   question meets the need. Where the need can be read two ways that
   lead to different pages, ask once, in one sentence, and wait.
2. Read the pages chosen; where a page names a skill or a definition
   and the detail matters, read it too. Nothing is answered from
   memory: every mechanism the answer names was read in this run.
3. Answer in plain sentences, in the conversation language: the way
   the forge has first, with what one types; then what matters to
   know on that way; where several ways fit, one recommended with
   its reason, once. Where the way leaves the forge — a repository
   to initialise, a program to install — say so plainly, since the
   forge does not do it. The pages read are named by path once, at
   the end.
4. Where the forge has nothing, say so; name the open thread of the
   forge's own project if one carries the need
   (`projects/forge/threads/`), and mark what Claude would do without
   a mechanism as his own (POS.1370).
5. Run nothing, write nothing, decide nothing: the answer shows a
   way.

Language: the conversation language (CLAUDE.md, prime directive 6 —
translate on write), the whole page, descriptions and Lens sections
included; only the notation stays English — command names, file
paths, IDs, front-matter keys and the bold names of the methods,
each followed by its translation once.
