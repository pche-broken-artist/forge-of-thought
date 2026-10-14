---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 959d3ff5e9750d00
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command

`/man` is the forge's manual: a command that prints, in the conversation, what a command or a working method is for and how it is called. It is for you when you want to know what a command does before you run it. A working method is one of the named ways a conversation runs, such as the walkthrough.

## When to use it

- You want the list of commands and working methods.
- You want the purpose, the arguments and the roster of one command before you run it.
- You want the paragraph of one working method.

## The command

```
/man [command | method]
```

`/manual` is an alias and does the same with the same arguments. The word `help` is not used, because it is Claude Code's own command.

## What happens

`/man` reads the files that own the information at the moment of the call. It keeps no text of its own, so what it prints is always as current as those files. It only reads: it runs none of the commands it describes.

1. Bare `/man` prints the overview.
   - Every command, with its arguments and its purpose cut to one line. `/man` and `/manual` are in the list.
   - Every working method, with the first sentence of its paragraph.
   - A closing line: `/man <command>` for a command's page, `/man <method>` for a method's.

   You should now see the two lists and the closing line.

2. `/man <command>`, for example `/man critique`, prints the page of that command.
   - Its purpose and its arguments.
   - Its purpose in full, as the table of commands gives it.
   - The roster it dispatches over, where it has one. Each member of the roster (a lens, a persona, a check or a genre) comes with its own description and with what it looks for, so that you know it before you run it.
   - A closing line that names the skill file, the file that holds the whole procedure.

   You should now see the command's page, ending with the path of its skill file.

3. `/man <method>`, for example `/man walkthrough`, prints the paragraph of that working method in full. Case does not matter, and a hyphen and a space are alike. Where a skill holds the method's shape, its path follows.

   You should now see the method's paragraph and, where there is one, the path of its skill.

## What you have afterwards

A page in the conversation, in the conversation language. Command names, file paths, front-matter keys and the names of the methods stay in English, and each method name is followed once by its translation. Nothing is written to a file and nothing is run.

## If something goes wrong

- A command that does not exist: `/man` says so and prints the list of commands.
- A method that does not exist: `/man` says so and prints the list of methods.

## A worked example

You want to know what the critic's lenses look for before choosing one.

```
/man critique
```

You should now see the purpose and arguments of `/critique`, then the roster of lenses. Each lens is shown with its description and with its own section on what it goes after. The page ends with the path of the skill file of `/critique`. You choose a lens and run `/critique <lens>` yourself.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
