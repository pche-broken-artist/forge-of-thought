---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 0c2ef577c4c99a41
inputs:
  - .claude/skills/man/SKILL.md
  - .claude/skills/manual/SKILL.md
---

# Look up a command

`/man` is the forge's manual: the command that prints what a command
or a working method does, so that you can read it before you run
anything. It is for the principal (the person whose thinking is
forged) who wants to know what a command takes, what it looks for or
how a method works.

## When to use it

Use it when you do not know which command fits, when you want to know
the arguments of a command, or when you want to know what a check, a
lens, a persona or a genre looks for before you run it. The word
`help` is not used for this: it is Claude Code's own command, which is
why the manual has the Unix name `man`. `/manual` is an alias that
does the same.

## The command

```
/man [command | method]
```

The three forms:

- `/man` alone prints the overview.
- `/man <command>` prints the page of one command, for example
  `/man check`.
- `/man <method>` prints the page of one working method, for example
  `/man walkthrough`.

The method name is matched without regard to case, and a hyphen and a
space count as the same.

## What happens

The manual has no text of its own. Claude (the model that works with
you) reads the files that own the facts at the moment of the call and
shortens them to a line. Nothing is stored, so the page is never out
of date. It only reads: it runs none of the commands it describes.

**Bare `/man`**

1. Claude reads the Commands table of the engine's `CLAUDE.md` and
   prints each command with its arguments and its purpose cut to one
   line. `/man` and `/manual` are in the list.
2. It reads the Working methods section and prints each method's name
   with the first sentence of its paragraph.
3. It closes with one line: `/man <command>` for a command's page,
   `/man <method>` for a method's.

You should now see the commands, the methods and the closing line.

**`/man <command>`**

1. Claude looks for the command's skill file,
   `.claude/skills/<command>/SKILL.md`. If there is none, it says so
   and prints the list of commands.
2. It prints the command's purpose, its arguments and the purpose from
   the Commands table in full.
3. Where the command works over a roster, it prints the roster. Each
   entry shows the description of its own file and, where the file has
   one, its Lens section in full. For a genre it shows the
   Elicitation checklist. This tells you what a check, a lens, a
   persona or a genre looks for before you run it.
4. It closes with one line naming the skill file, for the reader who
   wants the whole procedure.

You should now see the purpose, the arguments, the roster where there
is one, and the path of the skill file.

**`/man <method>`**

1. Claude matches the name against the bold names in the Working
   methods section. If none matches, it says so and lists the
   methods.
2. It prints the method's paragraph in full and, where the paragraph
   names a skill that holds the method's shape, that skill's path.

You should now see the whole paragraph of the method.

## What you have afterwards

A page in the conversation, and nothing else. No file is written and
no command has run. The page is in the conversation language, the
whole of it, descriptions and Lens sections included. Only the
notation stays English: command names, file paths, IDs, front-matter
keys and the names of the methods. Each method name is followed once
by its translation.

## If something goes wrong

- A command that has no skill file: the manual says so and lists the
  commands.
- A method that matches no name: the manual says so and lists the
  methods.

## A worked example

You want to know what the checks look for before choosing one.

```
/man check
```

Claude prints the purpose and the arguments of `/check`, then the
roster of checks. Each check appears with its description and, where
its file has one, its Lens section, which says what it verifies. The
page ends with the path of the skill file of `/check`. You can now
pick a check and run `/check <check> <slug>` yourself, with a
placeholder `<slug>` replaced by your project's slug.

## See also

- [Commands](../reference/commands.md): the same table, as a page.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
