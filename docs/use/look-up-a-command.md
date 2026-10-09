---
generated: 2026-10-09
made: mirrored
inputs-hash: 4118238fac40d643
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
  - CLAUDE.md
---

# Look up a command

This page is for someone using the forge who wants to know what a command or a working method does, what arguments it takes and what it looks for, without opening the files. The command for it is `/man`, and `/manual` is its alias.

## What `/man` is

`/man [command | method]` is the forge's manual. It has no text of its own. Each time you call it, it reads the files that own the information (`CLAUDE.md`, the skills, the agents, the state and genre files) and shortens what it finds to a line. Because it reads at the moment of the call, it cannot be out of date with the definitions.

It is read-only. It runs none of the commands it describes. It prints in the conversation language, the whole page, descriptions included. Only the notation stays in English: command names, file paths, IDs, front-matter keys and the bold names of the methods, each followed once by its translation.

The word `help` is not used because it is Claude Code's own command. The forge took the Unix name `man` instead.

## The three ways to call it

### Bare: `/man`

You see two lists.

1. The commands, each with its arguments and its purpose cut to one line. `/man` and `/manual` are in the list too.
2. The working methods, each with its name and the first sentence of its paragraph.

The last line tells you what to type next: `/man <command>` for a command's page, `/man <method>` for a method's.

### With a command: `/man <command>`

You see the page of that command:

1. Its purpose, its arguments, and its purpose in full as the Commands table gives it.
2. Where the command dispatches over a roster (the checks, the critic lenses, the challenger personas, the recipe genres), every entry of the roster with its own description. Where an entry has a Lens section, or for a genre an elicitation checklist, that is printed in full. You learn what a check, a lens, a persona or a genre looks for before you run it. This is the part `/man` adds to the plain list: what each entry looks for.
3. A last line naming the skill file, for when you want the whole procedure.

If no skill exists for the name you gave, `/man` says so and prints the list of commands.

### With a method: `/man <method>`

The name is matched against the bold names of the working methods, ignoring case, and hyphens and spaces count alike. You see the method's paragraph in full and, where it names a skill that holds the method's shape, the path of that skill. An unknown name gets a plain message and the list of methods.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
