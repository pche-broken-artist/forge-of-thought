---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 898e99ea268bcee5
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command

This page shows how to use `/man`, the forge's manual, to read what a command or a working method does before you run it. It is for the principal (the person whose thinking is forged) who wants the answer in the conversation, without opening the files that define the command.

## When to use it

Use `/man` when you do not know which command fits, or when you know the command and want to see its arguments first. Use it too when you want the exact wording of a working method, such as the walkthrough.

## The command

```
/man [command | method]
```

`/manual` is an alias and takes the same arguments. The word `help` is not used because it is Claude Code's own command, hence the Unix name.

## What happens

`/man` is a reader, not a text of its own. Claude reads the files that own the matter at the moment of the call, so the page it prints is never older than those files. It runs nothing that it describes.

1. Bare `/man` prints the overview.
   - Every command with its arguments, and its purpose cut to one line. `/man` and `/manual` are included.
   - Every working method with the first sentence of its paragraph.
   - A closing line: `/man <command>` for a command's page, `/man <method>` for a method's.

   You should now see the commands and the working methods as two lists, and the closing line.

2. `/man <command>` prints the page of one command.
   - Its purpose and its arguments.
   - Its purpose in full, as the table of commands gives it.
   - The roster it dispatches over, where it has one. Each entry shows the description of its own file and, where the file has one, what the entry looks for: a lens section for a lens, a persona or a check, the elicitation checklist for a genre.
   - A closing line naming the skill file, for the reader who wants the whole procedure.

   You should now see the command's page, ending with the path of its skill file.

3. `/man <method>` prints the page of one working method. Claude matches the name without regard to case, and hyphens and spaces count alike. It prints the paragraph of the method in full and, where the method names a skill that holds its shape, the path of that skill.

   You should now see the paragraph of the method, and a skill path where there is one.

The page is printed in the conversation language, the whole of it, descriptions and lens sections included. Only the notation stays English: command names, file paths, IDs, front-matter keys and the names of the methods. Each method name is followed once by its translation.

## What you have afterwards

You have the page in the conversation and nothing else. No file is written and no command has run.

## If something goes wrong

- A name that is not a command: `/man` says so and lists the commands.
- A name that is not a working method: `/man` says so and lists the methods.

## A worked example

You want to know what a critic lens looks for before you run one. You type:

```
/man critique
```

Claude prints the purpose of the command, its arguments, and its purpose in full. Then it lists the lenses, each with its description and what it goes after. The page closes with the path of the skill file of the command. You now choose a lens and run it. If you want the whole table of commands as a page, it is in the reference below.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
