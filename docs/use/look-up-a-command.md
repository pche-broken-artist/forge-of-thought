---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: a9a23d804d802b24
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command

`/man` is the forge's manual: the command that prints what a command or a working method is, for the user who wants to know it before running it. The working methods are the named ways a conversation between the principal (the person whose thinking is being forged) and Claude runs.

## When to use it

- You want the list of commands and methods.
- You want to know what one command is for, what arguments it takes, and what each entry of its roster looks for before you run it.
- You want the full wording of one working method.

## The command

```
/man [command | method]
```

`/manual` is an alias and does the same with the same arguments. The word `help` is Claude Code's own command, which is why the forge's manual has the Unix name.

## What happens

`/man` reads its answer at the moment of the call from the files that own it, so the manual is never older than the forge. It shortens what it reads to a line where it can. It runs none of the commands it describes. It prints in the conversation language: descriptions and the sections it quotes are translated, while command names, file paths, IDs and front-matter keys stay English.

1. Bare `/man` prints the overview. It lists every command with its arguments and its purpose cut to one line, `/man` and `/manual` included. Then it lists each working method with the first sentence of its paragraph. The last line says to use `/man <command>` for a command and `/man <method>` for a method.
   You should now see two lists and the closing line.
2. `/man <command>` prints the page of one command. It gives the purpose, the arguments and the full purpose from the commands table. Where the command works over a roster (checks, lenses, personas or genres), it lists each entry with its description. Where the entry's file has a section on what it looks for, that section is printed in full. For a genre, the checklist of questions is printed. The last line names the skill file that holds the whole procedure.
   You should now see the command's purpose, its arguments, its roster if it has one, and the path of its skill file.
3. `/man <method>` prints the page of one working method. The name is matched without regard to case, and hyphens and spaces count alike. It prints the paragraph in full and, where the method has a skill that holds its shape, that skill's path.
   You should now see the method's paragraph and, where there is one, its skill path.

## If something goes wrong

- The command you name does not exist: `/man` says so and prints the list of commands.
- The method you name does not exist: `/man` says so and prints the list of methods.

## A worked example

```
/man <command>
```

Replace `<command>` with a name from the overview. You see the command's purpose, then its arguments, then, if the command dispatches over a roster, one block for each member with what it looks for, and last the path of the skill file to read for the whole procedure. Nothing has run; to use the command, type it.

The table of all commands is also on the page [Commands](../reference/commands.md).

## See also

- [Commands](../reference/commands.md): the same table, as a page.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
