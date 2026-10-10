---
generated: 2026-10-10
made: mirrored
inputs-hash: 130f511f53e7fcc2
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
  - CLAUDE.md
---

# Look up a command

This page is for a user who wants to know what a command does, which
arguments it takes or what a working method means, without leaving the
conversation. The way to do that is `/man`.

## What `/man` is

`/man [command | method]` is the forge's manual. It has no text of its
own. Each time you call it, it reads the files that own the
information, shortens them to the line, and prints the result in the
conversation. Nothing it prints can be out of date with the forge.

`/manual` is an alias: it does the same with the same arguments.

`/man` only reads. It runs none of the commands it describes. The word
`help` is not used for this, because `help` is Claude Code's own
command; hence the Unix name.

## The three ways to call it

### Bare: the overview

Type `/man`. You see:

1. Every command with its arguments, and its purpose cut to one line.
   `/man` and `/manual` are in the list.
2. Every working method by name, with the first sentence of its
   paragraph.
3. A closing line: `/man <command>` for a command's page,
   `/man <method>` for a method's.

### With a command: one command's page

Type `/man` followed by a command name. You see:

- the command's purpose, taken from its description;
- its arguments;
- the full purpose as the command table gives it;
- where the command dispatches over a roster, each entry of that
  roster with its description and what it looks for. For a check, a
  critic lens or a challenger persona that is its lens section; for a
  recipe genre it is its elicitation checklist. You can therefore
  know what a check, a lens, a persona or a genre goes after before
  you run it;
- a closing line naming the skill file, for when you want the whole
  procedure.

If no command of that name exists, `/man` says so and lists the
commands.

### With a method: one working method's page

Type `/man` followed by the name of a working method. The name is
matched without regard to case, and hyphens and spaces count alike. You
see the method's paragraph in full and, where a skill holds the
method's shape, the path of that skill. If the method is unknown,
`/man` says so and lists the methods.

## Language

The whole page is printed in the conversation language, descriptions
and lens sections included. Only the notation stays in English: command
names, file paths, IDs, front-matter keys and the bold names of the
methods, each followed by its translation once.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
